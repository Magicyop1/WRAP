using System;
using System.Collections.Generic;
using HarmonyLib;
using UnityEngine;

namespace WitheringRoomsArchipelago
{
    /// <summary>
    /// A conservative gate for physical/gameplay-mutating AP actions.
    ///
    /// Inventory.Ready() becomes true too early during save loading.  In the
    /// failing logs it became true before InventoryState.LoadSave, mansion
    /// generation, the second InventoryState.LoadSave pass, and
    /// MansionSimulationManager.ApplySaveGame.
    ///
    /// We therefore require the mansion simulation itself to be ready and
    /// stable before tutorial grants, AP item delivery, or DeathLink can
    /// mutate gameplay state.
    /// </summary>
    internal static class VanillaLoadSafetyGate
    {
        private const float StructuralSettleSeconds = 2.0f;

        private static float lastStructuralEventTime = -1f;
        private static int loadSaveDepth;

        private static bool lastReportedOpen;
        private static string lastReportedReason = string.Empty;
        private static bool hasReportedState;

        public static void NotifyLoadSaveEntered()
        {
            loadSaveDepth++;
            Touch("InventoryState.LoadSave entered");
        }

        public static void NotifyLoadSaveExited()
        {
            if (loadSaveDepth > 0)
                loadSaveDepth--;

            Touch("InventoryState.LoadSave exited");
        }

        public static void NotifyMansionGenerationStarted(
            MansionCard card,
            int seed)
        {
            Touch(
                $"GenerateMansion started: " +
                $"'{(card != null ? card.name : "NULL")}', seed={seed}"
            );
        }

        public static void NotifyApplySaveGameStarted()
        {
            Touch("MansionSimulationManager.ApplySaveGame entered");
        }

        public static void NotifyApplySaveGameFinished(
            bool preApplyMismatch,
            Exception? exception)
        {
            Touch(
                $"MansionSimulationManager.ApplySaveGame exited " +
                $"(preApplyMismatch={preApplyMismatch}, " +
                $"exception={(exception != null ? exception.GetType().Name : "none")})"
            );
        }

        public static bool CanMutateGameplayState()
        {
            string reason;
            bool open = Evaluate(out reason);

            ReportTransition(open, reason);
            return open;
        }

        private static bool Evaluate(out string reason)
        {
            if (loadSaveDepth > 0 || InventoryLoadRepairGuard.Active)
            {
                reason = "InventoryState.LoadSave active";
                return false;
            }

            if (Inventory.instance == null ||
                !Inventory.instance.Ready())
            {
                reason = "inventory not ready";
                return false;
            }

            MansionSimulationManager manager =
                MansionSimulationManager.instance;

            if (manager == null)
            {
                reason = "MansionSimulationManager.instance is null";
                return false;
            }

            try
            {
                if (manager.IsMansionUnderConstruction())
                {
                    reason = "mansion under construction";
                    return false;
                }

                if (!manager.Ready())
                {
                    reason = "mansion simulation manager not ready";
                    return false;
                }
            }
            catch (Exception ex)
            {
                reason =
                    $"mansion readiness probe failed: {ex.GetType().Name}";
                return false;
            }

            PlayerController player = PlayerController.instance;

            if (player == null ||
                player.currentRoom == null)
            {
                reason = "player/currentRoom not ready";
                return false;
            }

            if (lastStructuralEventTime >= 0f)
            {
                float elapsed =
                    Time.unscaledTime - lastStructuralEventTime;

                if (elapsed < StructuralSettleSeconds)
                {
                    reason =
                        "settling after vanilla load/mansion event";
                    return false;
                }
            }

            reason = "vanilla inventory + mansion + player state stable";
            return true;
        }

        private static void Touch(string description)
        {
            lastStructuralEventTime = Time.unscaledTime;

            Plugin.LogSource.LogInfo(
                $"[AP LOAD SAFETY] {description}; AP gameplay mutation gated."
            );
        }

        private static void ReportTransition(
            bool open,
            string reason)
        {
            if (hasReportedState &&
                open == lastReportedOpen &&
                string.Equals(
                    reason,
                    lastReportedReason,
                    StringComparison.Ordinal))
            {
                return;
            }

            hasReportedState = true;
            lastReportedOpen = open;
            lastReportedReason = reason;

            if (open)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LOAD SAFETY] Gate OPEN: {reason}."
                );
            }
            else
            {
                Plugin.LogSource.LogInfo(
                    $"[AP LOAD SAFETY] Gate closed: {reason}."
                );
            }
        }
    }


    /// <summary>
    /// Compares the saved mansion simulation-object list directly with the
    /// freshly regenerated manager lookup immediately before vanilla applies
    /// the save.
    ///
    /// This should reveal ALL missing objects, not merely the first one that
    /// causes vanilla ApplySaveGame to abort.
    /// </summary>
    internal static class MansionLoadDiagnostics
    {
        private const int MaxMissingObjectLines = 50;

        public static bool AnalyzeBeforeApply(
            MansionSimulationManager manager,
            MansionSaveGame saveGame)
        {
            try
            {
                if (manager == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP MANSION DIAG] ApplySaveGame: manager is null."
                    );
                    return false;
                }

                if (saveGame == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP MANSION DIAG] ApplySaveGame: saveGame is null."
                    );
                    return false;
                }

                int savedCount =
                    saveGame.savedObjects != null
                        ? saveGame.savedObjects.Count
                        : 0;

                int lookupCount =
                    manager.guidToSimulationObject != null
                        ? manager.guidToSimulationObject.Count
                        : 0;

                int savedLookupCount =
                    saveGame.guidToObjectLookup != null
                        ? saveGame.guidToObjectLookup.Count
                        : 0;

                Plugin.LogSource.LogWarning(
                    $"[AP MANSION DIAG] PRE-APPLY: " +
                    $"savedObjects={savedCount}, " +
                    $"savedGuidLookup={savedLookupCount}, " +
                    $"generatedGuidLookup={lookupCount}, " +
                    $"chapter={SafeChapter()}, " +
                    $"managerReady={SafeManagerReady(manager)}, " +
                    $"underConstruction={SafeUnderConstruction(manager)}"
                );

                if (saveGame.savedObjects == null ||
                    manager.guidToSimulationObject == null)
                {
                    return false;
                }

                int missing = 0;
                int missingMansionStart = 0;
                int missingSpawnedLater = 0;
                int savedSheetBeasts = 0;
                int missingSheetBeasts = 0;
                int presentSheetBeasts = 0;

                // Keep a compact list so one pathological save does not flood
                // the entire BepInEx log.
                List<string> missingLines = new();

                for (int i = 0;
                     i < saveGame.savedObjects.Count;
                     i++)
                {
                    MansionSimulationObjectSaveState state =
                        saveGame.savedObjects[i];

                    if (state == null ||
                        string.IsNullOrEmpty(state.guid))
                    {
                        continue;
                    }

                    bool sheetBeast =
                        state.guid.IndexOf(
                            "SheetBeast",
                            StringComparison.OrdinalIgnoreCase) >= 0;

                    if (sheetBeast)
                        savedSheetBeasts++;

                    bool exists =
                        manager.guidToSimulationObject.ContainsKey(
                            state.guid
                        );

                    if (exists)
                    {
                        if (sheetBeast)
                            presentSheetBeasts++;

                        continue;
                    }

                    missing++;

                    if (state.spawnedAfterMansionStart)
                        missingSpawnedLater++;
                    else
                        missingMansionStart++;

                    if (sheetBeast)
                        missingSheetBeasts++;

                    if (missingLines.Count < MaxMissingObjectLines)
                    {
                        missingLines.Add(
                            $"guid='{state.guid}', " +
                            $"cardGUID='{state.cardGUID}', " +
                            $"room='{state.mansionRoomAddress}', " +
                            $"objectType={state.objectType}, " +
                            $"spawnedAfterStart={state.spawnedAfterMansionStart}"
                        );
                    }
                }

                Plugin.LogSource.LogWarning(
                    $"[AP MANSION DIAG] Saved->generated comparison: " +
                    $"missing={missing}/{savedCount}, " +
                    $"missingMansionStart={missingMansionStart}, " +
                    $"missingSpawnedLater={missingSpawnedLater}, " +
                    $"SheetBeasts(saved/present/missing)=" +
                    $"{savedSheetBeasts}/{presentSheetBeasts}/{missingSheetBeasts}"
                );

                for (int i = 0; i < missingLines.Count; i++)
                {
                    Plugin.LogSource.LogWarning(
                        $"[AP MANSION DIAG] MISSING[{i + 1}]: " +
                        missingLines[i]
                    );
                }

                if (missing > missingLines.Count)
                {
                    Plugin.LogSource.LogWarning(
                        $"[AP MANSION DIAG] " +
                        $"{missing - missingLines.Count} additional missing " +
                        $"object(s) omitted from log."
                    );
                }

                if (missing == 0)
                {
                    Plugin.LogSource.LogInfo(
                        "[AP MANSION DIAG] All saved simulation-object GUIDs " +
                        "exist in the regenerated mansion before ApplySaveGame."
                    );
                }

                return missing > 0;
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP MANSION DIAG] PRE-APPLY analysis failed: {ex}"
                );

                return false;
            }
        }

        private static int SafeChapter()
        {
            try
            {
                return GameScenarioManager.instance != null
                    ? GameScenarioManager.instance.chapterIndex
                    : -1;
            }
            catch
            {
                return -1;
            }
        }

        private static bool SafeManagerReady(
            MansionSimulationManager manager)
        {
            try
            {
                return manager.Ready();
            }
            catch
            {
                return false;
            }
        }

        private static bool SafeUnderConstruction(
            MansionSimulationManager manager)
        {
            try
            {
                return manager.IsMansionUnderConstruction();
            }
            catch
            {
                return true;
            }
        }
    }


    [HarmonyPatch(
        typeof(MansionSimulationManager),
        nameof(MansionSimulationManager.GenerateMansion),
        new Type[]
        {
            typeof(MansionCard),
            typeof(int)
        }
    )]
    internal static class MansionSimulationManager_GenerateMansion_LoadSafety_Patch
    {
        [HarmonyPrefix]
        private static void Prefix(
            [HarmonyArgument(0)] MansionCard card,
            [HarmonyArgument(1)] int seed)
        {
            VanillaLoadSafetyGate.NotifyMansionGenerationStarted(
                card,
                seed
            );
        }
    }


    [HarmonyPatch(
        typeof(MansionSimulationManager),
        nameof(MansionSimulationManager.ApplySaveGame),
        new Type[] { typeof(MansionSaveGame) }
    )]
    internal static class MansionSimulationManager_ApplySaveGame_APDiagnostics_Patch
    {
        [HarmonyPrefix]
        private static void Prefix(
            MansionSimulationManager __instance,
            [HarmonyArgument(0)] MansionSaveGame saveGame,
            out bool __state)
        {
            VanillaLoadSafetyGate.NotifyApplySaveGameStarted();

            __state = MansionLoadDiagnostics.AnalyzeBeforeApply(
                __instance,
                saveGame
            );
        }

        [HarmonyFinalizer]
        private static Exception? Finalizer(
            Exception? __exception,
            bool __state)
        {
            VanillaLoadSafetyGate.NotifyApplySaveGameFinished(
                __state,
                __exception
            );

            return __exception;
        }
    }
}
