using System;
using System.Collections.Generic;
using HarmonyLib;
using Il2CppInterop.Runtime;
using UnityEngine;

namespace WitheringRoomsArchipelago
{
    /// <summary>
    /// Archipelago compatibility for CompletableQuestToken.autoCompleteItems.
    ///
    /// Vanilla uses physical ownership of entries in autoCompleteItems as a
    /// signal that a quest has advanced/completed. In Archipelago, a physical
    /// item may have arrived from another world long before its vanilla source
    /// was reached, so physical ownership is not authoritative world state.
    ///
    /// Strategy:
    ///   1. Remove only canonical randomized AP items from vanilla
    ///      autoCompleteItems lists before inventory reconstruction/acquisition.
    ///   2. Remember those quest -> AP-location relationships ourselves.
    ///   3. Complete an ACTIVE quest token only after the corresponding AP
    ///      discovery location has actually been checked.
    ///
    /// Internal/non-randomized quest tokens remain in autoCompleteItems and
    /// continue to use completely vanilla behavior.
    /// </summary>
    internal static class QuestAutoCompleteCompatibility
    {
        private sealed class Relation
        {
            public CompletableQuestToken Quest = null!;
            public Item TriggerItem = null!;
            public string QuestGuid = "";
            public string QuestName = "";
            public string TriggerGuid = "";
            public string TriggerName = "";
            public long LocationId;
        }

        private static readonly List<Relation> Relations = new();
        private static readonly HashSet<string> RelationKeys = new();
        private static readonly HashSet<string> LoggedCompletions = new();

        private static bool configured;
        private static bool configuring;
        private static float nextUpdateTime;

        private const float UpdateIntervalSeconds = 0.25f;

        /// <summary>
        /// Finds every CompletableQuestToken asset and strips canonical AP
        /// discovery items out of autoCompleteItems. Safe to call repeatedly.
        ///
        /// This deliberately does NOT restore the physical-item triggers on a
        /// temporary AP disconnect. Once an AP session has configured the game,
        /// allowing those triggers back in would reintroduce the exact sequence
        /// break this compatibility layer prevents.
        /// </summary>
        public static void EnsureConfigured()
        {
            if (configured || configuring)
                return;

            if (!ArchipelagoClient.Connected)
                return;

            configuring = true;

            try
            {
                var databases =
                    Resources.FindObjectsOfTypeAll<ItemDatabase>();

                if (databases == null || databases.Length == 0)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP QUEST AUTOCOMPLETE] ItemDatabase assets are not " +
                        "available yet; will retry."
                    );
                    return;
                }

                bool sawCompletableQuestToken = false;
                int strippedCount = 0;

                foreach (ItemDatabase database in databases)
                {
                    if (database == null)
                        continue;

                    var allItems = database.AllCardsCached();

                    if (allItems == null)
                        continue;

                    foreach (Item item in allItems)
                    {
                        if (item == null)
                            continue;

                        string runtimeType = "";

                        try
                        {
                            runtimeType =
                                item.GetIl2CppType().FullName ?? "";
                        }
                        catch
                        {
                            continue;
                        }

                        if (runtimeType != "CompletableQuestToken" &&
                            !runtimeType.EndsWith(
                                ".CompletableQuestToken",
                                StringComparison.Ordinal))
                        {
                            continue;
                        }

                        IntPtr itemPtr =
                            IL2CPP.Il2CppObjectBaseToPtr(item);

                        if (itemPtr == IntPtr.Zero)
                            continue;

                        CompletableQuestToken quest =
                            new CompletableQuestToken(itemPtr);

                        sawCompletableQuestToken = true;

                        var autoItems = quest.autoCompleteItems;

                        if (autoItems == null || autoItems.Count == 0)
                            continue;

                        string questGuid = SafeGuid(quest);
                        string questName = SafeTitle(quest);

                        // Remove backwards so indices remain valid.
                        for (int i = autoItems.Count - 1; i >= 0; i--)
                        {
                            Item trigger = autoItems[i];

                            if (trigger == null)
                                continue;

                            if (!ArchipelagoQuestState.TryGetCanonicalLocationState(
                                    trigger,
                                    out RandomizedItemData? data,
                                    out _,
                                    out _))
                            {
                                // Hidden/internal/non-randomized trigger:
                                // preserve vanilla semantics.
                                continue;
                            }

                            if (data == null || !data.LocationId.HasValue)
                                continue;

                            string triggerGuid = trigger.GetGUID() ?? "";
                            string key = questGuid + "|" + triggerGuid;

                            // Remove the physical trigger from the actual quest
                            // asset even if another database exposed the same
                            // relation earlier.
                            autoItems.RemoveAt(i);
                            strippedCount++;

                            if (RelationKeys.Add(key))
                            {
                                Relation relation = new Relation
                                {
                                    Quest = quest,
                                    TriggerItem = trigger,
                                    QuestGuid = questGuid,
                                    QuestName = questName,
                                    TriggerGuid = triggerGuid,
                                    TriggerName = data.Name,
                                    LocationId = data.LocationId.Value
                                };

                                Relations.Add(relation);

                                Plugin.LogSource.LogInfo(
                                    "[AP QUEST AUTOCOMPLETE] Replaced vanilla " +
                                    $"physical trigger: quest='{questName}' " +
                                    $"questGuid={questGuid} " +
                                    $"trigger='{data.Name}' " +
                                    $"triggerGuid={triggerGuid} " +
                                    $"locationId={data.LocationId.Value}"
                                );
                            }
                        }
                    }
                }

                // If assets were not fully available, leave configured=false
                // so the next safe opportunity retries.
                if (!sawCompletableQuestToken)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP QUEST AUTOCOMPLETE] No CompletableQuestToken " +
                        "assets were available yet; will retry."
                    );
                    return;
                }

                configured = true;

                Plugin.LogSource.LogInfo(
                    "[AP QUEST AUTOCOMPLETE] Configuration complete. " +
                    $"relations={Relations.Count}, strippedEntries={strippedCount}."
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogWarning(
                    "[AP QUEST AUTOCOMPLETE] Configuration failed; " +
                    $"will retry. {ex}"
                );
            }
            finally
            {
                configuring = false;
            }
        }

        /// <summary>
        /// Call once per ArchipelagoBehaviour.Update(). The method throttles
        /// itself and refuses to mutate quest state while vanilla load/generation
        /// is in an unsafe transition.
        /// </summary>
        public static void Update()
        {
            if (!ArchipelagoClient.Connected)
                return;

            EnsureConfigured();

            if (!configured)
                return;

            if (!VanillaLoadSafetyGate.CanMutateGameplayState())
                return;

            Inventory inventory = Inventory.instance;

            if (inventory == null || !inventory.Ready())
                return;

            if (Time.unscaledTime < nextUpdateTime)
                return;

            nextUpdateTime =
                Time.unscaledTime + UpdateIntervalSeconds;

            for (int i = 0; i < Relations.Count; i++)
            {
                Relation relation = Relations[i];

                try
                {
                    // The vanilla source has not happened yet.
                    if (!ArchipelagoClient.IsLocationChecked(
                            relation.LocationId))
                    {
                        continue;
                    }

                    // Already done: never replay completion/rewards.
                    if (inventory.HasCompleted(relation.Quest))
                        continue;

                    // The source may be checked before the quest is formally
                    // given. Wait until the quest token is active, then complete
                    // it immediately. This preserves normal quest ordering.
                    if (!inventory.HasItem(relation.Quest))
                        continue;

                    Plugin.LogSource.LogWarning(
                        "[AP QUEST AUTOCOMPLETE] AP location is checked and " +
                        "quest is active; applying vanilla completion now. " +
                        $"quest='{relation.QuestName}' " +
                        $"questGuid={relation.QuestGuid} " +
                        $"trigger='{relation.TriggerName}' " +
                        $"triggerGuid={relation.TriggerGuid} " +
                        $"locationId={relation.LocationId}"
                    );

                    inventory.SetCompleted(relation.Quest);

                    bool completedAfter =
                        inventory.HasCompleted(relation.Quest);

                    string completionKey =
                        relation.QuestGuid + "|" + relation.TriggerGuid;

                    if (LoggedCompletions.Add(completionKey))
                    {
                        Plugin.LogSource.LogWarning(
                            "[AP QUEST AUTOCOMPLETE] Completion result: " +
                            $"quest='{relation.QuestName}' " +
                            $"completedAfter={completedAfter}"
                        );
                    }
                }
                catch (Exception ex)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP QUEST AUTOCOMPLETE] Sync failed for " +
                        $"quest='{relation.QuestName}' / " +
                        $"trigger='{relation.TriggerName}': {ex}"
                    );
                }
            }
        }

        private static string SafeTitle(Item item)
        {
            try
            {
                return item.GetTitle() ?? item.name ?? "<unnamed>";
            }
            catch
            {
                try
                {
                    return item.name ?? "<unnamed>";
                }
                catch
                {
                    return "<unavailable>";
                }
            }
        }

        private static string SafeGuid(Item item)
        {
            try
            {
                return item.GetGUID() ?? "";
            }
            catch
            {
                return "";
            }
        }
    }


    /// <summary>
    /// Earliest important safety hook: strip AP-controlled autoCompleteItems
    /// before vanilla reconstructs inventory from a save.
    /// </summary>
    [HarmonyPatch(
        typeof(InventoryState),
        nameof(InventoryState.LoadSave),
        new Type[] { typeof(InventorySaveGame) }
    )]
    internal static class InventoryState_LoadSave_QuestAutoCompleteCompat_Patch
    {
        [HarmonyPrefix]
        [HarmonyPriority(Priority.First)]
        private static void Prefix()
        {
            QuestAutoCompleteCompatibility.EnsureConfigured();
        }
    }


    /// <summary>
    /// Fallback safety hook for any item acquisition that occurs before the
    /// normal gameplay Update loop has had a chance to configure the relation
    /// table. Runs before the existing AP AddItem interception.
    /// </summary>
    [HarmonyPatch(
        typeof(Inventory),
        nameof(Inventory.AddItem),
        new Type[]
        {
            typeof(Item),
            typeof(int),
            typeof(Inventory.ReportItemTelemetry),
            typeof(Inventory.QueuedNewItem)
        }
    )]
    internal static class Inventory_AddItem_QuestAutoCompleteCompat_Patch
    {
        [HarmonyPrefix]
        [HarmonyPriority(Priority.First)]
        private static void Prefix()
        {
            QuestAutoCompleteCompatibility.EnsureConfigured();
        }
    }
}
