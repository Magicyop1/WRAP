using System;
using System.Collections.Generic;
using HarmonyLib;

namespace WitheringRoomsArchipelago
{
    /// <summary>
    /// Tracks when vanilla is inside InventoryState.LoadSave().
    ///
    /// This remains thread-local so an unrelated InventoryItems.Add on
    /// another thread cannot accidentally inherit the load-save context.
    /// </summary>
    internal static class InventoryLoadRepairGuard
    {
        [ThreadStatic]
        private static int loadSaveDepth;

        public static bool Active =>
            loadSaveDepth > 0;

        public static void Enter()
        {
            loadSaveDepth++;
        }

        public static void Exit()
        {
            if (loadSaveDepth > 0)
                loadSaveDepth--;
        }
    }


    /// <summary>
    /// Diagnostics for the incoming InventorySaveGame payload.
    ///
    /// The important distinction is between:
    ///   1. an item represented by the actual save payload, and
    ///   2. an item synthesized later inside InventoryState.LoadSave,
    ///      e.g. by ItemFixUpRuleset.
    ///
    /// We deliberately do NOT change suppression semantics here.  This
    /// class only records enough evidence to tell those two cases apart.
    /// </summary>
    internal static class InventoryLoadDiagnostics
    {
        private const string RightIdolEyeGuid =
            "8733011378a78854db88c16530c251d2";

        private const string EastStairwellKeyGuid =
            "87e09fe50faa54b4f9528cd20c8443c7";

        private const string ToolSackLimiterGuid =
            "47e656aedf569e840ad7bead9da931d8";

        private const string TutorialPreMargaretGuid =
            "5e8790be1f4ec8645b086908672fd63b";

        private const string WretchMetGuid =
            "5c674501ff9046d46848a6a275bf9ee5";

        private const string AllowedToRememberGuid =
            "c90f00ae5363b2d4798b07fd3d03cd87";

        private const string WretchTrySpellGuid =
            "1fdf66728bf94a942bd5ddc501addd48";


        private const string WretchEarlierQuestGuid =
    "23d2318f8989f474a8a0f090f097ef2b";

        private const string WretchCraftQuestGuid =
            "952bb0e989f429847bc41ded61105a54";

        private static readonly string[] WatchedGuids =
        {
            RightIdolEyeGuid,
            EastStairwellKeyGuid,
            ToolSackLimiterGuid,
            TutorialPreMargaretGuid,
            WretchMetGuid,
            AllowedToRememberGuid,
            WretchTrySpellGuid,

            // New Wretch diagnostics:
            WretchEarlierQuestGuid,
            WretchCraftQuestGuid
        };

        private static readonly HashSet<string> SavedInstanceGuids =
            new(StringComparer.OrdinalIgnoreCase);

        private static readonly HashSet<string> SavedTemplateGuids =
            new(StringComparer.OrdinalIgnoreCase);

        private static readonly Dictionary<string, int> SavedInstanceCounts =
            new(StringComparer.OrdinalIgnoreCase);

        private static readonly Dictionary<string, int> SavedTemplateCounts =
            new(StringComparer.OrdinalIgnoreCase);

        private static int loadPassCounter;
        private static int currentLoadPass;
        private static int currentSaveEntryCount;

        public static int CurrentLoadPass => currentLoadPass;

        public static bool CurrentSaveContains(string guid)
        {
            if (string.IsNullOrEmpty(guid))
                return false;

            return SavedInstanceGuids.Contains(guid) ||
                   SavedTemplateGuids.Contains(guid);
        }

        public static bool CurrentSaveContainsAsTemplate(string guid)
        {
            return !string.IsNullOrEmpty(guid) &&
                   SavedTemplateGuids.Contains(guid);
        }

        public static void BeginLoadSave(InventorySaveGame saveGame)
        {
            currentLoadPass = ++loadPassCounter;
            currentSaveEntryCount = 0;

            SavedInstanceGuids.Clear();
            SavedTemplateGuids.Clear();
            SavedInstanceCounts.Clear();
            SavedTemplateCounts.Clear();

            try
            {
                if (saveGame?.items != null)
                {
                    currentSaveEntryCount = saveGame.items.Length;

                    for (int i = 0; i < saveGame.items.Length; i++)
                    {
                        var entry = saveGame.items[i];

                        if (entry == null)
                            continue;

                        if (!string.IsNullOrEmpty(entry.guid))
                        {
                            SavedInstanceGuids.Add(entry.guid);
                            IncrementCount(SavedInstanceCounts, entry.guid);
                        }

                        if (!string.IsNullOrEmpty(entry.templateGUID))
                        {
                            SavedTemplateGuids.Add(entry.templateGUID);
                            IncrementCount(SavedTemplateCounts, entry.templateGUID);
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP LOAD DIAG] Pass {currentLoadPass}: " +
                    $"failed reading InventorySaveGame.items: {ex}"
                );
            }

            Plugin.LogSource.LogWarning(
                $"[AP LOAD DIAG] BEGIN InventoryState.LoadSave pass " +
                $"{currentLoadPass}. entries={currentSaveEntryCount}, " +
                $"instanceGuids={SavedInstanceGuids.Count}, " +
                $"templateGuids={SavedTemplateGuids.Count}"
            );

            foreach (string guid in WatchedGuids)
                LogWatchedGuid("PRE", guid);
        }

        public static void EndLoadSave()
        {
            foreach (string guid in WatchedGuids)
                LogWatchedGuid("POST", guid);

            Plugin.LogSource.LogWarning(
                $"[AP LOAD DIAG] END InventoryState.LoadSave pass " +
                $"{currentLoadPass}."
            );
        }

        public static void LogAdd(Item item)
        {
            if (item == null)
                return;

            try
            {
                string guid = item.GetGUID();

                if (string.IsNullOrEmpty(guid))
                    return;

                bool watched =
                    IsWatched(guid);

                bool savedPayload =
                    CurrentSaveContains(guid);

                /*
                 * Ordinary reconstruction from InventorySaveGame is expected
                 * and extremely noisy.
                 *
                 * Only retain:
                 *   - identities we are explicitly watching, or
                 *   - additions NOT represented by the save payload.
                 *
                 * The latter are possible ItemFixUpRuleset synthesis and are
                 * exactly what we're interested in diagnosing.
                 */
                if (!watched && savedPayload)
                    return;

                int liveQuantity =
                    GetLiveQuantity(item);

                string classification =
                    savedPayload
                        ? "SAVED_PAYLOAD"
                        : "SYNTHETIC_NOT_IN_SAVE";

                string message =
                    $"[AP LOAD ADD] pass={currentLoadPass} " +
                    $"item='{SafeTitle(item)}' " +
                    $"guid={guid} " +
                    $"class={classification} " +
                    $"savedAsTemplate=" +
                    $"{CurrentSaveContainsAsTemplate(guid)} " +
                    $"liveQtyBefore={liveQuantity} " +
                    $"APChecked={ItemRandomizer.IsLocationChecked(guid)} " +
                    $"APUnlocked={ItemRandomizer.IsItemUnlocked(guid)}";

                if (savedPayload)
                {
                    // Watched but otherwise ordinary reconstruction.
                    Plugin.LogSource.LogInfo(message);
                }
                else
                {
                    // High-value anomaly: vanilla is adding something that
                    // was not represented by the incoming save payload.
                    Plugin.LogSource.LogWarning(message);
                }
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP LOAD DIAG] Failed classifying " +
                    $"InventoryItems.Add: {ex}"
                );
            }
        }

        private static void LogWatchedGuid(
            string phase,
            string guid)
        {
            try
            {
                Item? item = GameItems.FindItemByGuid(guid);
                int liveQuantity = item != null
                    ? GetLiveQuantity(item)
                    : -1;

                Plugin.LogSource.LogInfo(
                    $"[AP LOAD WATCH] pass={currentLoadPass} {phase} " +
                    $"name='{(item != null ? SafeTitle(item) : "UNRESOLVED")}' " +
                    $"guid={guid} " +
                    $"savedInstance={SavedInstanceGuids.Contains(guid)} " +
                    $"savedInstanceCount={GetCount(SavedInstanceCounts, guid)} " +
                    $"savedTemplate={SavedTemplateGuids.Contains(guid)} " +
                    $"savedTemplateCount={GetCount(SavedTemplateCounts, guid)} " +
                    $"liveQty={liveQuantity} " +
                    $"APChecked={ItemRandomizer.IsLocationChecked(guid)} " +
                    $"APUnlocked={ItemRandomizer.IsItemUnlocked(guid)}"
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LOAD WATCH] pass={currentLoadPass} {phase} " +
                    $"guid={guid} diagnostic failed: {ex.Message}"
                );
            }
        }

        private static int GetLiveQuantity(Item item)
        {
            try
            {
                if (Inventory.instance == null)
                    return -1;

                ItemInfo? info = Inventory.instance.GetInfo(item);

                return info != null
                    ? info.quantity
                    : 0;
            }
            catch
            {
                return -1;
            }
        }


        private static void IncrementCount(
            Dictionary<string, int> counts,
            string guid)
        {
            if (counts.TryGetValue(guid, out int count))
                counts[guid] = count + 1;
            else
                counts[guid] = 1;
        }

        private static int GetCount(
            Dictionary<string, int> counts,
            string guid)
        {
            return counts.TryGetValue(guid, out int count)
                ? count
                : 0;
        }

        private static bool IsWatched(string guid)
        {
            for (int i = 0; i < WatchedGuids.Length; i++)
            {
                if (string.Equals(
                        WatchedGuids[i],
                        guid,
                        StringComparison.OrdinalIgnoreCase))
                {
                    return true;
                }
            }

            return false;
        }

        private static string SafeTitle(Item item)
        {
            try
            {
                return item.GetTitle() ?? "";
            }
            catch
            {
                return "";
            }
        }
    }


    /// <summary>
    /// Establishes a narrow scope around vanilla InventoryState.LoadSave().
    ///
    /// Native analysis shows that the ItemFixUpRuleset pass which logs
    /// "Found missing awarded item" runs inside this method.
    /// </summary>
    [HarmonyPatch(
        typeof(InventoryState),
        nameof(InventoryState.LoadSave),
        new Type[] { typeof(InventorySaveGame) }
    )]
    internal static class InventoryState_LoadSave_APRepairScope_Patch
    {
        [HarmonyPrefix]
        private static void Prefix(
            [HarmonyArgument(0)] InventorySaveGame saveGame)
        {
            InventoryLoadRepairGuard.Enter();
            VanillaLoadSafetyGate.NotifyLoadSaveEntered();
            InventoryLoadDiagnostics.BeginLoadSave(saveGame);

            Plugin.LogSource.LogInfo(
                "[AP LOAD REPAIR] Entered InventoryState.LoadSave."
            );
        }

        [HarmonyFinalizer]
        private static Exception? Finalizer(
            Exception? __exception)
        {
            try
            {
                InventoryLoadDiagnostics.EndLoadSave();
            }
            finally
            {
                InventoryLoadRepairGuard.Exit();
                VanillaLoadSafetyGate.NotifyLoadSaveExited();
            }

            Plugin.LogSource.LogInfo(
                "[AP LOAD REPAIR] Exited InventoryState.LoadSave."
            );

            return __exception;
        }
    }


    /// <summary>
    /// Retains the existing narrow suppression behavior, while logging enough
    /// information to distinguish ordinary save reconstruction from synthetic
    /// load-time additions.
    /// </summary>
    [HarmonyPatch(
        typeof(InventoryItems),
        nameof(InventoryItems.Add),
        new Type[] { typeof(ItemInfo) }
    )]
    internal static class InventoryItems_Add_APLoadRepair_Patch
    {
        [HarmonyPrefix]
        private static bool Prefix(
            ItemInfo __0,
            ref ItemInfo __result)
        {
            if (!InventoryLoadRepairGuard.Active)
                return true;

            if (__0 == null ||
                __0.item == null)
            {
                return true;
            }

            // DIAGNOSTIC ONLY.  This does not affect the decision below.
            InventoryLoadDiagnostics.LogAdd(__0.item);

            if (!ItemRandomizer.ShouldSuppressVanillaLoadRestore(
                    __0.item))
            {
                return true;
            }

            string guid = string.Empty;

            try
            {
                guid = __0.item.GetGUID();
            }
            catch
            {
            }

            Plugin.LogSource.LogWarning(
                $"[AP LOAD REPAIR] Suppressed vanilla load-time " +
                $"restore of randomized item ({guid}): " +
                $"location checked, item not AP-unlocked. " +
                $"saveClass=" +
                $"{(InventoryLoadDiagnostics.CurrentSaveContains(guid) ? "SAVED_PAYLOAD" : "SYNTHETIC_NOT_IN_SAVE")}"
            );

            // InventoryItems.Add(ItemInfo) returns ItemInfo.
            // Preserve a sensible return value for the vanilla caller.
            __result = __0;

            return false;
        }
    }
}
