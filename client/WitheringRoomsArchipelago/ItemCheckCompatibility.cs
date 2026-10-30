using System;
using System.Collections.Generic;
using System.Text;
using HarmonyLib;

namespace WitheringRoomsArchipelago
{
    /// <summary>
    /// Central compatibility rule for vanilla quest/story ItemChecks.
    ///
    /// For a canonical randomized item that creates an Archipelago location,
    /// "has this happened in the vanilla world?" is represented by whether
    /// that item's canonical AP location has been checked, NOT by whether the
    /// player physically owns a copy received from Archipelago.
    ///
    /// V2 note:
    /// The old implementation tried to scope-patch Inventory.HasItem() /
    /// Inventory.GetItemCount() while ItemCheck.Check() was executing.  That
    /// does not catch ItemCheck's native IL2CPP inventory lookup path.  V2
    /// therefore lets vanilla ItemCheck.Check() run, then directly recomputes
    /// only ItemChecks that actually contain a canonical AP item.
    /// </summary>
    internal static class ArchipelagoQuestState
    {
        public static bool TryGetCanonicalLocationCount(
            Item item,
            out int count)
        {
            return TryGetCanonicalLocationState(
                item,
                out _,
                out _,
                out count
            );
        }

        public static bool TryGetCanonicalLocationCount(
            string guid,
            out int count)
        {
            count = 0;

            if (string.IsNullOrEmpty(guid))
                return false;

            RandomizedItemData? data =
                ItemData.ByGuid(guid);

            if (data == null ||
                !data.CreatesLocation ||
                !data.LocationId.HasValue)
            {
                return false;
            }

            bool checkedLocation =
                ArchipelagoClient.IsLocationChecked(
                    data.LocationId.Value
                );

            // A canonical discovery location is boolean world-state.
            count = checkedLocation ? 1 : 0;
            return true;
        }

        public static bool TryGetCanonicalLocationState(
            Item item,
            out RandomizedItemData? data,
            out bool checkedLocation,
            out int count)
        {
            data = null;
            checkedLocation = false;
            count = 0;

            if (item == null)
                return false;

            string guid = item.GetGUID();

            if (string.IsNullOrEmpty(guid))
                return false;

            data = ItemData.ByGuid(guid);

            // Internal quest tokens, filler-only entries, etc. retain normal
            // vanilla inventory semantics.
            if (data == null ||
                !data.CreatesLocation ||
                !data.LocationId.HasValue)
            {
                data = null;
                return false;
            }

            checkedLocation =
                ArchipelagoClient.IsLocationChecked(
                    data.LocationId.Value
                );

            count = checkedLocation ? 1 : 0;
            return true;
        }
    }


    [HarmonyPatch(
        typeof(ItemCheck),
        nameof(ItemCheck.Check),
        new Type[] { }
    )]
    public static class ItemCheck_Check_APCompatibility_V2_Patch
    {
        private static readonly HashSet<string> LoggedOutcomes =
            new HashSet<string>();

        private static readonly object LogLock =
            new object();

        [HarmonyPostfix]
        public static void Postfix(
            ItemCheck __instance,
            ref bool __result)
        {
            // Until the AP session is connected, vanilla remains authoritative.
            if (!ArchipelagoClient.Connected ||
                __instance == null)
            {
                return;
            }

            // Important safety boundary: do not replace ordinary ItemChecks.
            // V2 only intervenes when at least one required/anti item is a
            // canonical AP discovery item.
            if (!ContainsCanonicalAPItem(__instance))
                return;

            bool vanillaResult = __result;

            try
            {
                if (!TryEvaluateWithAPWorldState(
                        __instance,
                        out bool correctedResult,
                        out string detail))
                {
                    return;
                }

                __result = correctedResult;

                LogOutcomeOnce(
                    vanillaResult,
                    correctedResult,
                    __instance,
                    detail
                );
            }
            catch (Exception ex)
            {
                // Fail safe: if our reconstruction ever encounters an
                // unexpected authored shape, leave the original vanilla result.
                __result = vanillaResult;

                Plugin.LogSource.LogWarning(
                    $"[AP ITEMCHECK COMPAT V2] Direct evaluation failed; " +
                    $"keeping vanilla result={vanillaResult}. {ex}"
                );
            }
        }

        private static bool ContainsCanonicalAPItem(
            ItemCheck check)
        {
            if (check.items != null)
            {
                for (int i = 0; i < check.items.Count; i++)
                {
                    ItemAndQuantity entry = check.items[i];

                    if (entry == null || entry.item == null)
                        continue;

                    if (ArchipelagoQuestState.TryGetCanonicalLocationCount(
                            entry.item,
                            out _))
                    {
                        return true;
                    }
                }
            }

            if (check.antiItems != null)
            {
                for (int i = 0; i < check.antiItems.Count; i++)
                {
                    ItemAndQuantity entry = check.antiItems[i];

                    if (entry == null || entry.item == null)
                        continue;

                    if (ArchipelagoQuestState.TryGetCanonicalLocationCount(
                            entry.item,
                            out _))
                    {
                        return true;
                    }
                }
            }

            return false;
        }

        private static bool TryEvaluateWithAPWorldState(
            ItemCheck check,
            out bool correctedResult,
            out string detail)
        {
            correctedResult = false;
            detail = "";

            Inventory inventory = Inventory.instance;

            if (inventory == null)
                return false;

            bool passed = true;
            bool usedCanonicalAPState = false;
            StringBuilder sb = new StringBuilder();

            // Required items: authored quantity must be present.
            if (check.items != null)
            {
                for (int i = 0; i < check.items.Count; i++)
                {
                    ItemAndQuantity entry = check.items[i];

                    if (entry == null || entry.item == null)
                        continue;

                    int effectiveCount = GetEffectiveCount(
                        inventory,
                        entry.item,
                        "required",
                        i,
                        entry.quantity,
                        ref usedCanonicalAPState,
                        sb
                    );

                    if (effectiveCount < entry.quantity)
                        passed = false;
                }
            }

            // Anti-items: reaching the authored quantity makes the base check
            // fail.  This mirrors the required-item threshold in reverse.
            if (check.antiItems != null)
            {
                for (int i = 0; i < check.antiItems.Count; i++)
                {
                    ItemAndQuantity entry = check.antiItems[i];

                    if (entry == null || entry.item == null)
                        continue;

                    int effectiveCount = GetEffectiveCount(
                        inventory,
                        entry.item,
                        "anti",
                        i,
                        entry.quantity,
                        ref usedCanonicalAPState,
                        sb
                    );

                    if (effectiveCount >= entry.quantity)
                        passed = false;
                }
            }

            // Preserve vanilla quest-token semantics directly through the
            // Inventory method used for CompletableQuestToken status checks.
            if (check.quest != null)
            {
                bool questPassed =
                    inventory.MatchesCompleted(
                        check.quest,
                        check.questStatus
                    );

                if (!questPassed)
                    passed = false;

                if (sb.Length > 0)
                    sb.Append(" | ");

                sb.Append(
                    $"quest='{SafeQuestTitle(check.quest)}' " +
                    $"questGuid={SafeGuid(check.quest)} " +
                    $"questStatus={check.questStatus} " +
                    $"questPassed={questPassed}"
                );
            }

            // If no canonical AP item was actually encountered, do not replace
            // vanilla even if this method was entered after the pre-scan.
            if (!usedCanonicalAPState)
                return false;

            correctedResult =
                check.invert
                    ? !passed
                    : passed;

            detail = sb.ToString();
            return true;
        }

        private static int GetEffectiveCount(
            Inventory inventory,
            Item item,
            string role,
            int index,
            int requiredQuantity,
            ref bool usedCanonicalAPState,
            StringBuilder sb)
        {
            int physicalCount =
                inventory.GetItemCount(item);

            if (!ArchipelagoQuestState.TryGetCanonicalLocationState(
                    item,
                    out RandomizedItemData? data,
                    out bool checkedLocation,
                    out int apWorldCount))
            {
                return physicalCount;
            }

            usedCanonicalAPState = true;

            string guid = item.GetGUID();
            bool apUnlocked =
                ItemRandomizer.IsItemUnlocked(guid);

            if (sb.Length > 0)
                sb.Append(" | ");

            sb.Append(
                $"{role}[{index}]='{data!.Name}' " +
                $"guid={guid} " +
                $"requiredQty={requiredQuantity} " +
                $"physicalCount={physicalCount} " +
                $"APChecked={checkedLocation} " +
                $"APUnlocked={apUnlocked} " +
                $"effectiveCount={apWorldCount}"
            );

            return apWorldCount;
        }

        private static void LogOutcomeOnce(
            bool vanillaResult,
            bool correctedResult,
            ItemCheck check,
            string detail)
        {
            string key =
                $"{vanillaResult}|{correctedResult}|{check.invert}|" +
                $"{check.questStatus}|{detail}";

            lock (LogLock)
            {
                if (!LoggedOutcomes.Add(key))
                    return;
            }

            string questName =
                check.quest == null
                    ? "<null>"
                    : SafeQuestTitle(check.quest);

            Plugin.LogSource.LogWarning(
                $"[AP ITEMCHECK COMPAT V2] " +
                $"vanillaResult={vanillaResult} " +
                $"correctedResult={correctedResult} " +
                $"invert={check.invert} " +
                $"quest='{questName}' " +
                $"questStatus={check.questStatus}" +
                (string.IsNullOrEmpty(detail)
                    ? ""
                    : $" | {detail}")
            );
        }

        private static string SafeQuestTitle(
            CompletableQuestToken quest)
        {
            try
            {
                return quest.GetTitle() ?? quest.name ?? "<unnamed>";
            }
            catch
            {
                try
                {
                    return quest.name ?? "<unnamed>";
                }
                catch
                {
                    return "<unavailable>";
                }
            }
        }

        private static string SafeGuid(
            CompletableQuestToken quest)
        {
            try
            {
                return quest.GetGUID() ?? "";
            }
            catch
            {
                return "";
            }
        }
    }
}
