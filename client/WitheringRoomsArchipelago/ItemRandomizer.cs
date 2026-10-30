using System.Collections.Generic;
using UnityEngine;
using System.Linq;

namespace WitheringRoomsArchipelago
{
    public static class ItemRandomizer
    {

        private sealed class PendingLinkedSuppression
        {
            public int Quantity;
            public int ExpiresFrame;
            public string PrimaryGuid = "";
        }


        private static readonly Dictionary<
            string,
            PendingLinkedSuppression>
            pendingLinkedSecondarySuppressions =
                new Dictionary<
                    string,
                    PendingLinkedSuppression>(
                        System.StringComparer.OrdinalIgnoreCase
                );
        private static readonly HashSet<string> CheckedItems = new();
        private static readonly HashSet<string> UnlockedItems = new();

        private static readonly string[] RerollFillerNames =
        {
            "Strange Coin",
            "Red Wax",
            "Blue Wax",
            "Yellow Wax"
        };

        private static bool bypassRandomizer = false;

        public static bool BypassRandomizer => bypassRandomizer;

        private static readonly Dictionary<string, int>
    pendingNewItemAdditions = new();

        private static readonly Dictionary<string, int>
    pendingInternalNewItemAdditions = new();



        public static void ArmLinkedSecondarySuppression(
        Item primary,
        int quantity)
        {
            if (primary == null || quantity <= 0)
                return;

            string primaryGuid =
                primary.GetGUID();

            if (!LinkedItemPairs.TryGetSecondaryForPrimary(
                    primaryGuid,
                    out string secondaryGuid))
            {
                return;
            }


            /*
             * Sanity-check the hardcoded relationship against the
             * game's own Item.impliedOnAcquireItem field.
             *
             * If a game update changes the relationship, we would rather
             * log it and fail safely than suppress an unrelated item.
             */
            Item implied =
                primary.impliedOnAcquireItem;

            if (implied == null)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LINKED ITEM] {primary.GetTitle()} is in the " +
                    $"linked-pair table, but impliedOnAcquireItem is NULL. " +
                    $"Not arming suppression."
                );

                return;
            }


            string runtimeSecondaryGuid =
                implied.GetGUID();

            if (!string.Equals(
                    runtimeSecondaryGuid,
                    secondaryGuid,
                    System.StringComparison.OrdinalIgnoreCase))
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LINKED ITEM] Pair mismatch for " +
                    $"{primary.GetTitle()}. Expected implied GUID " +
                    $"{secondaryGuid}, runtime says " +
                    $"{runtimeSecondaryGuid}. Not suppressing."
                );

                return;
            }


            if (!pendingLinkedSecondarySuppressions.TryGetValue(
                    secondaryGuid,
                    out PendingLinkedSuppression pending))
            {
                pending =
                    new PendingLinkedSuppression();

                pendingLinkedSecondarySuppressions[
                    secondaryGuid
                ] = pending;
            }


            pending.Quantity += quantity;
            pending.PrimaryGuid = primaryGuid;

            /*
             * The implied NewItem has historically appeared immediately
             * inside the primary AddItem flow.
             *
             * Give it a few frames of tolerance, but do NOT leave a
             * permanent suppression token around that could swallow a
             * legitimate later acquisition.
             */
            pending.ExpiresFrame =
                Time.frameCount + 10;


            Plugin.LogSource.LogInfo(
                $"[AP LINKED ITEM] Armed implied-item suppression: " +
                $"{primary.GetTitle()} -> {implied.GetTitle()} " +
                $"x{quantity}, expiresFrame={pending.ExpiresFrame}"
            );
        }


        public static bool TryConsumeLinkedSecondarySuppression(
            Item item,
            int quantity)
        {
            if (item == null || quantity <= 0)
                return false;

            string guid =
                item.GetGUID();

            if (string.IsNullOrEmpty(guid))
                return false;


            if (!pendingLinkedSecondarySuppressions.TryGetValue(
                    guid,
                    out PendingLinkedSuppression pending))
            {
                return false;
            }


            if (Time.frameCount > pending.ExpiresFrame)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LINKED ITEM] Expired unused linked suppression " +
                    $"for {item.GetTitle()} ({guid})."
                );

                pendingLinkedSecondarySuppressions.Remove(
                    guid
                );

                return false;
            }


            if (pending.Quantity < quantity)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LINKED ITEM] Linked suppression quantity mismatch " +
                    $"for {item.GetTitle()}: pending={pending.Quantity}, " +
                    $"requested={quantity}. Leaving acquisition untouched."
                );

                pendingLinkedSecondarySuppressions.Remove(
                    guid
                );

                return false;
            }


            pending.Quantity -= quantity;

            if (pending.Quantity <= 0)
            {
                pendingLinkedSecondarySuppressions.Remove(
                    guid
                );
            }


            Plugin.LogSource.LogWarning(
                $"[AP LINKED ITEM] Suppressed vanilla implied award: " +
                $"{item.GetTitle()} x{quantity}. " +
                $"Source primary GUID={pending.PrimaryGuid}"
            );

            return true;
        }

        private static void TrySendLinkedPartnerDiscovery(
    string sourceGuid)
        {
            if (!LinkedItemPairs.TryGetPartner(
                    sourceGuid,
                    out string partnerGuid))
            {
                return;
            }


            // Already satisfied -- nothing to do.
            if (CheckedItems.Contains(partnerGuid))
                return;


            RandomizedItemData? partnerData =
                ItemData.ByGuid(partnerGuid);

            if (partnerData == null ||
                !partnerData.CreatesLocation ||
                !partnerData.LocationId.HasValue)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LINKED ITEM] Partner GUID {partnerGuid} " +
                    $"does not resolve to a canonical AP location."
                );

                return;
            }


            Plugin.LogSource.LogInfo(
                $"[AP LINKED ITEM] Natural linked discovery: " +
                $"{sourceGuid} also checks " +
                $"{partnerData.Name} ({partnerGuid})."
            );


            if (!SendItemDiscoveryCheck(partnerGuid))
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LINKED ITEM] Could not send linked check for " +
                    $"{partnerData.Name}; leaving it unchecked."
                );

                return;
            }


            CheckedItems.Add(partnerGuid);


            Item? partnerItem =
                GameItems.FindItemByGuid(partnerGuid);

            if (partnerItem == null)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LINKED ITEM] Sent linked location for " +
                    $"{partnerData.Name}, but its Item object is not loaded; " +
                    $"skipping notification presentation."
                );

                return;
            }


            long locationId =
                partnerData.LocationId.Value;


            if (ArchipelagoClient.TryGetCheckInfo(
                    locationId,
                    out long apItemId,
                    out string apItemName,
                    out string receivingPlayer))
            {
                Item? displayItem = null;

                RandomizedItemData? replacementData =
                    ItemData.ByItemId(apItemId);

                if (replacementData != null)
                {
                    displayItem =
                        GameItems.FindItemByGuid(
                            replacementData.Guid
                        );
                }


                ArchipelagoNotifications.QueueCheckSent(
                    partnerItem,
                    displayItem,
                    apItemName,
                    receivingPlayer,
                    partnerData.LocationName
                );
            }
        }


        public static void ExpectInternalAddItemFromNewItem(
    Item item,
    int quantity)
        {
            if (item == null || quantity <= 0)
                return;

            string guid =
                item.GetGUID();

            if (string.IsNullOrEmpty(guid))
                return;

            if (pendingInternalNewItemAdditions.TryGetValue(
                    guid,
                    out int pending))
            {
                pendingInternalNewItemAdditions[guid] =
                    pending + quantity;
            }
            else
            {
                pendingInternalNewItemAdditions[guid] =
                    quantity;
            }

            Plugin.LogSource.LogInfo(
                $"[AP ITEM FLOW] Marked expected AddItem as " +
                $"AP-internal: {item.GetTitle()} x{quantity} " +
                $"(pendingInternal=" +
                $"{pendingInternalNewItemAdditions[guid]})"
            );
        }


        public static bool ConsumeExpectedInternalAddItem(
            Item item,
            int quantity)
        {
            if (item == null || quantity <= 0)
                return false;

            string guid =
                item.GetGUID();

            if (string.IsNullOrEmpty(guid))
                return false;

            if (!pendingInternalNewItemAdditions.TryGetValue(
                    guid,
                    out int pending))
            {
                return false;
            }

            if (pending <= quantity)
            {
                pendingInternalNewItemAdditions.Remove(
                    guid
                );
            }
            else
            {
                pendingInternalNewItemAdditions[guid] =
                    pending - quantity;
            }

            return true;
        }

        public static void ExpectAddItemFromNewItem(
            Item item,
            int quantity)
        {
            if (item == null || quantity <= 0)
                return;

            string guid = item.GetGUID();

            if (string.IsNullOrEmpty(guid))
                return;

            if (pendingNewItemAdditions.TryGetValue(
                guid,
                out int pending))
            {
                pendingNewItemAdditions[guid] =
                    pending + quantity;
            }
            else
            {
                pendingNewItemAdditions[guid] =
                    quantity;
            }

            Plugin.LogSource.LogInfo(
                $"[AP ITEM FLOW] Expecting AddItem from NewItem: " +
                $"{item.GetTitle()} x{quantity} " +
                $"(pending={pendingNewItemAdditions[guid]})"
            );
        }


        public static bool ConsumeExpectedAddItem(
            Item item,
            int quantity)
        {
            if (item == null || quantity <= 0)
                return false;

            string guid = item.GetGUID();

            if (string.IsNullOrEmpty(guid))
                return false;

            if (!pendingNewItemAdditions.TryGetValue(
                guid,
                out int pending))
            {
                return false;
            }

            if (pending <= quantity)
            {
                pendingNewItemAdditions.Remove(guid);
            }
            else
            {
                pendingNewItemAdditions[guid] =
                    pending - quantity;
            }

            Plugin.LogSource.LogInfo(
                $"[AP ITEM FLOW] Consumed expected AddItem: " +
                $"{item.GetTitle()} x{quantity}"
            );

            return true;
        }

        public static bool IsInternalGameStateItem(Item item)
        {
            if (item == null)
                return false;

            string title = item.GetTitle() ?? "";

            return
                title.StartsWith("item_name_Tutorial_") ||
                title.StartsWith("item_name_Chapter") ||
                title.Contains("Tutorial");
        }

        public static bool ProcessNaturalItem(
    ref Item item,
    int quantity,
    MansionSimulationObject? sourceObject = null)
        {
            if (item == null)
                return true;

            string guid = item.GetGUID();

            var iconRef = item.icon;

            Plugin.LogSource.LogInfo(
                $"[AP ICON TEST] Item: " +
                $"{item.GetTitle()} ({guid})"
            );

            Plugin.LogSource.LogInfo(
                $"[AP ICON TEST] Icon Valid: " +
                $"{iconRef.Valid()}"
            );

            Plugin.LogSource.LogInfo(
                $"[AP ICON TEST] Icon path: " +
                $"{iconRef.path}"
            );

            Plugin.LogSource.LogInfo(
                $"[AP ICON TEST] Icon guid: " +
                $"{iconRef.guid}"
            );

            Plugin.LogSource.LogInfo(
                $"[AP ICON TEST] Icon GetGUID(): " +
                $"{iconRef.GetGUID()}"
            );

            Plugin.LogSource.LogInfo(
                $"[AP ICON TEST] Icon DebugName(): " +
                $"{iconRef.DebugName()}"
            );

            var tex =
                iconRef.LoadSync<Texture2D>(true);

            Plugin.LogSource.LogInfo(
                tex != null
                    ? $"[AP ICON TEST] Loaded icon texture: " +
                      $"{tex.name} ({tex.width}x{tex.height})"
                    : "[AP ICON TEST] LoadSync<Texture2D> returned null."
            );

            RandomizedItemData? data =
                ItemData.ByGuid(guid);

            // Not part of AP item data.
            if (data == null)
                return true;

            if (!ArchipelagoClient.ChallengeStart &&
                (data.Name == "Gatehouse Key" ||
                 data.Name == "Strange Bedroom Key"))
            {
                return true;
            }

            // This MUST occur before the ordinary single-discovery
            // item path below. Multi-discovery items use their normal
            // LocationId for ordinal 1, followed by the additional
            // MultiDiscoveryLocationIdBase locations for ordinals 2+.
            //

            if (ItemData.IsMultiDiscoveryItem(data))
            {
                int checksPerAcquisition =
                    data.Name == "Trickster Medal" ? 2 : 1;

                List<MultiDiscoveryLocationData> pendingLocations =
                    ItemData.GetMultiDiscoveryLocations(data)
                        .Where(location =>
                            !ArchipelagoClient.IsLocationChecked(
                                location.LocationId))
                        .Take(checksPerAcquisition)
                        .ToList();

                if (pendingLocations.Count > 0)
                {
                    bool notificationQueued = false;

                    foreach (MultiDiscoveryLocationData location
                             in pendingLocations)
                    {
                        if (!SendMultiDiscoveryCheck(data, location))
                        {
                            Plugin.LogSource.LogWarning(
                                $"[AP MULTI DISCOVERY] Failed to send " +
                                $"{location.LocationName}."
                            );

                            return false;
                        }

                        // Current notification UI supports one pending popup.
                        // All checks are sent, but display only the first here.
                        if (!notificationQueued)
                        {
                            QueueDiscoveryNotification(
                                item,
                                location.LocationId,
                                location.LocationName
                            );

                            notificationQueued = true;
                        }
                    }

                    // A completed trial awards AP checks,
                    // not the natural physical medal.
                    return false;
                }

                Plugin.LogSource.LogInfo(
                    $"[AP MULTI DISCOVERY] All locations for " +
                    $"{data.Name} are already checked."
                );

                return ProcessCheckedOrExhaustedItem(
                    ref item,
                    guid,
                    sourceObject
                );
            }


            // =========================================================
            // ORDINARY RANDOMIZED ITEMS
            // =========================================================

            if (!data.CreatesLocation)
                return true;

            // ---------------------------------------------------------
            // FIRST NATURAL DISCOVERY ALWAYS CHECKS THE LOCATION,
            // regardless of whether AP has already unlocked this item.
            // ---------------------------------------------------------
            if (!CheckedItems.Contains(guid))
            {
                Plugin.LogSource.LogInfo(
                    $"[AP CHECK] First discovery: " +
                    $"{item.GetTitle()} ({guid})"
                );

                if (!data.LocationId.HasValue)
                {
                    Plugin.LogSource.LogWarning(
                        $"[AP CHECK] Missing location ID for " +
                        $"{data.Name}."
                    );

                    return false;
                }

                long locationId =
                    data.LocationId.Value;

                if (!SendItemDiscoveryCheck(guid))
                {
                    Plugin.LogSource.LogWarning(
                        $"[AP CHECK] Could not send check for " +
                        $"{data.Name}; leaving it unchecked."
                    );

                    return false;
                }

                CheckedItems.Add(guid);

                QueueDiscoveryNotification(
                    item,
                    locationId,
                    data.LocationName!
                );

                TrySendLinkedPartnerDiscovery(guid);

                // This physical copy represents a location check.
                // Suppress the natural copy.
                return false;
            }

            // Location already checked.
            return ProcessCheckedOrExhaustedItem(
                ref item,
                guid,
                sourceObject
            );
        }

        private static Item? TryRerollFromTreasureSource(
    MansionSimulationObject sourceObject,
    Item originalItem)
        {
            try
            {
                SimulationTreasureComponent treasure =
                    sourceObject.GetComponent<SimulationTreasureComponent>();

                if (treasure == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP TREASURE REROLL] " +
                        "Source object has no SimulationTreasureComponent."
                    );

                    return null;
                }

                MansionSimulationManager manager =
                    MansionSimulationManager.instance;

                if (manager == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP TREASURE REROLL] " +
                        "MansionSimulationManager.instance is null."
                    );

                    return null;
                }

                TreasureTable alternateTable =
                    treasure.alternateTreasureTable;

                TreasureTableTweaks tweaks =
                    treasure.tweaks;

                int gold;

                Item replacement =
                    manager.RerollTreasure(
                        sourceObject,
                        alternateTable,
                        tweaks,
                        out gold
                    );

                if (replacement == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP TREASURE REROLL] " +
                        "Vanilla RerollTreasure returned null."
                    );

                    return null;
                }

                Plugin.LogSource.LogInfo(
                    $"[AP TREASURE REROLL] Vanilla roll: " +
                    $"{originalItem.GetTitle()} -> " +
                    $"{replacement.GetTitle()}, gold={gold}"
                );

                return replacement;
            }
            catch (System.Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP TREASURE REROLL] Exception: {ex}"
                );

                return null;
            }
        }

        private static Item? GetReplacementFiller()
        {
            var fillerItems = ItemData.FillerItems()
                .Where(data => RerollFillerNames.Contains(data.Name))
                .ToList();

            if (fillerItems.Count == 0)
            {
                Plugin.LogSource.LogWarning(
                    "[AP REROLL] No reroll filler items are defined."
                );

                return null;
            }

            int startIndex = UnityEngine.Random.Range(
                0,
                fillerItems.Count
            );

            // Try every permitted filler once, beginning at a random point.
            // This avoids failing merely because one particular
            // ScriptableObject has not been loaded.
            for (int offset = 0; offset < fillerItems.Count; offset++)
            {
                int index =
                    (startIndex + offset) % fillerItems.Count;

                RandomizedItemData data =
                    fillerItems[index];

                Item? item =
                    GameItems.FindItemByGuid(data.Guid);

                if (item != null)
                    return item;
            }

            Plugin.LogSource.LogWarning(
                "[AP REROLL] No permitted reroll filler item " +
                "could be found in loaded game objects."
            );

            return null;
        }

        public static void UnlockAndGiveArchipelagoItem(
            Item item,
            int quantity = 1)
        {
            if (item == null)
                return;

            string guid = item.GetGUID();

            UnlockedItems.Add(guid);

            Plugin.LogSource.LogInfo(
                $"[AP UNLOCK] {item.GetTitle()} ({guid})"
            );

            GiveInternalNewItem(item, quantity);
        }

        public static void GiveInternalNewItem(
            Item item,
            int quantity = 1)
        {
            if (item == null)
                return;

            bypassRandomizer = true;

            LocalizedString testSource = item.GetRawTitle();

            try
            {
                Plugin.LogSource.LogInfo(
                    $"[AP INTERNAL GRANT] " +
                    $"{item.GetTitle()} x{quantity}"
                );

                Inventory.instance.NewItem(
                    item,
                    testSource,
                    false,
                    false,
                    false,
                    null,
                    quantity
                );
            }
            finally
            {
                bypassRandomizer = false;
            }
        }


        private static bool IsRandomizedItem(string guid)
        {
            RandomizedItemData? data = ItemData.ByGuid(guid);

            return data != null && data.CreatesLocation;
        }

        private static void QueueDiscoveryNotification(
    Item sourceItem,
    long locationId,
    string locationName)
        {
            if (ArchipelagoClient.TryGetCheckInfo(
                locationId,
                out long apItemId,
                out string apItemName,
                out string receivingPlayer))
            {
                Plugin.LogSource.LogInfo(
                    $"[AP CHECK] Notification queued: " +
                    $"{apItemName} ({receivingPlayer}) / " +
                    $"{locationName}"
                );

                Item? displayItem = null;

                RandomizedItemData? replacementData =
                    ItemData.ByItemId(apItemId);

                if (replacementData != null)
                {
                    displayItem =
                        GameItems.FindItemByGuid(
                            replacementData.Guid
                        );
                }

                ArchipelagoNotifications.QueueCheckSent(
                    sourceItem,
                    displayItem,
                    apItemName,
                    receivingPlayer,
                    locationName
                );
            }
            else
            {
                Plugin.LogSource.LogWarning(
                    $"[AP CHECK] Location {locationId} was sent, " +
                    $"but no scout information was cached."
                );
            }
        }


        private static bool ProcessCheckedOrExhaustedItem(
    ref Item item,
    string guid,
    MansionSimulationObject? sourceObject)
        {
            // AP has unlocked this item:
            // later natural copies are allowed normally.

            TrySendLinkedPartnerDiscovery(guid);

            if (UnlockedItems.Contains(guid))
                return true;

            Item originalItem = item;

            // Prefer a vanilla treasure-table reroll whenever we know
            // which simulation object produced this pickup.
            if (sourceObject != null)
            {
                Item? replacement =
                    TryRerollFromTreasureSource(
                        sourceObject,
                        originalItem
                    );

                if (replacement != null)
                {
                    Plugin.LogSource.LogInfo(
                        $"[AP TREASURE REROLL] " +
                        $"{originalItem.GetTitle()} -> " +
                        $"{replacement.GetTitle()}"
                    );

                    item = replacement;
                    return true;
                }

                Plugin.LogSource.LogWarning(
                    $"[AP TREASURE REROLL] " +
                    $"Could not obtain usable reroll for " +
                    $"{originalItem.GetTitle()}."
                );
            }

            /*
             * No valid treasure-table reroll was available.
             *
             * For now retain the existing filler fallback. This protects
             * direct AddItem acquisitions and unusual treasure paths while
             * we validate the vanilla reroll mechanism.
             */
            Item? filler = GetReplacementFiller();

            if (filler == null)
            {
                Plugin.LogSource.LogWarning(
                    "[AP REROLL] Could not find replacement filler."
                );

                return false;
            }

            Plugin.LogSource.LogInfo(
                $"[AP REROLL FALLBACK] " +
                $"{originalItem.GetTitle()} -> " +
                $"{filler.GetTitle()}"
            );

            item = filler;
            return true;
        }

        private static bool SendMultiDiscoveryCheck(
    RandomizedItemData data,
    MultiDiscoveryLocationData location)
        {
            if (!ArchipelagoClient.Connected)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP CHECK] Cannot send " +
                    $"{location.LocationName}: not connected."
                );

                return false;
            }

            Plugin.LogSource.LogInfo(
                $"[AP MULTI DISCOVERY] Sending " +
                $"{location.LocationName}: " +
                $"{location.LocationId} " +
                $"(ordinal={location.Ordinal})"
            );

            return ArchipelagoClient.SendLocationCheck(
                location.LocationId
            );
        }

        private static bool SendItemDiscoveryCheck(string guid)
        {
            RandomizedItemData? data =
                ItemData.ByGuid(guid);

            if (data == null)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP CHECK] No item data for GUID {guid}"
                );

                return false;
            }

            if (!data.LocationId.HasValue)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP CHECK] {data.Name} has no AP location."
                );

                return false;
            }

            if (!ArchipelagoClient.Connected)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP CHECK] Cannot send {data.Name}: not connected."
                );

                return false;
            }

            Plugin.LogSource.LogInfo(
                $"[AP CHECK] Sending {data.Name}: " +
                $"{data.LocationId.Value}"
            );

            return ArchipelagoClient.SendLocationCheck(
                data.LocationId.Value
            );
        }

        /// <summary>
        /// Called after a vanilla authored AddRemoveItemAction(Add) finishes.
        ///
        /// Normal successful rewards should already have passed through the
        /// existing inventory interception and marked the AP location checked.
        /// This method only fills the semantic gap where the authored reward
        /// action executed but vanilla skipped the physical acquisition (most
        /// importantly because the player already owns the item).
        /// </summary>
        public static bool ProcessAuthoredRewardAction(
            Item item,
            string sourceDescription)
        {
            if (item == null)
                return false;

            try
            {
                string guid = item.GetGUID();

                if (string.IsNullOrEmpty(guid))
                    return false;

                RandomizedItemData? data =
                    ItemData.ByGuid(guid);

                // Only canonical real randomized acquisition locations.
                // Hidden quest/state tokens naturally fall outside this path.
                if (data == null ||
                    !data.CreatesLocation ||
                    !data.LocationId.HasValue)
                {
                    return false;
                }

                // If the ordinary acquisition hook already handled this
                // action, the location is checked and the postfix is a no-op.
                if (CheckedItems.Contains(guid))
                {
                    Plugin.LogSource.LogInfo(
                        $"[AP DIALOG REWARD] {sourceDescription}: " +
                        $"{data.Name} already checked; no fallback needed."
                    );

                    return true;
                }

                Plugin.LogSource.LogWarning(
                    $"[AP DIALOG REWARD] {sourceDescription}: authored Add " +
                    $"for {data.Name} completed while its AP location is " +
                    $"still unchecked. Sending fallback discovery check."
                );

                if (!SendItemDiscoveryCheck(guid))
                {
                    Plugin.LogSource.LogWarning(
                        $"[AP DIALOG REWARD] Could not send fallback check " +
                        $"for {data.Name}; leaving it unchecked."
                    );

                    return false;
                }

                CheckedItems.Add(guid);

                QueueDiscoveryNotification(
                    item,
                    data.LocationId.Value,
                    data.LocationName!
                );

                Plugin.LogSource.LogWarning(
                    $"[AP DIALOG REWARD] Fallback discovery completed: " +
                    $"{data.LocationName} ({data.LocationId.Value})."
                );

                return true;
            }
            catch (System.Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP DIALOG REWARD] Failed processing authored reward " +
                    $"from {sourceDescription}: {ex}"
                );

                return false;
            }
        }


        public static void RestoreCheckedItem(string guid)
        {
            if (string.IsNullOrEmpty(guid))
                return;

            CheckedItems.Add(guid);

            Plugin.LogSource.LogInfo(
                $"[AP STATE] Restored checked item {guid}"
            );
        }

        public static void RestoreUnlockedItem(string guid)
        {
            if (UnlockedItems.Add(guid))
            {
                Plugin.LogSource.LogInfo(
                    $"[AP STATE] Restored unlocked item {guid}"
                );
            }
        }

        public static void ClearUnlockedItems()
        {
            UnlockedItems.Clear();
        }

        public static void ClearCheckedItems()
        {
            CheckedItems.Clear();
        }

        private static readonly System.Random rng = new();

        private static RandomizedItemData? GetRandomFiller()
        {
            var fillerItems = ItemData.FillerItems();

            if (fillerItems.Count == 0)
            {
                Plugin.LogSource.LogWarning(
                    "[AP REROLL] No filler items are defined."
                );

                return null;
            }

            return fillerItems[
                rng.Next(fillerItems.Count)
            ];
        }

        public static bool HandleReceivedArchipelagoItem(
    RandomizedItemData data,
    int quantity = 1)
        {
            Item? item =
    GameItems.FindItemByGuid(data.Guid);

            if (item == null)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP RECEIVE] Could not currently resolve " +
                    $"{data.Name} ({data.Guid})."
                );

                GameItems.LogItemAvailability(
                    data.Name,
                    data.Guid
                );

                return false;
            }

            if (data.CreatesLocation)
            {
                UnlockedItems.Add(data.Guid);

                Plugin.LogSource.LogInfo(
                    $"[AP UNLOCK] {data.Name} ({data.Guid})"
                );
            }

            GiveInternalNewItem(
                item,
                quantity
            );

            return true;
        }

        public static bool ShouldSatisfyVanillaHasCondition(
    Item item)
        {
            if (item == null)
                return false;

            try
            {
                string guid = item.GetGUID();

                if (string.IsNullOrEmpty(guid))
                    return false;

                RandomizedItemData? data =
                    ItemData.ByGuid(guid);

                // Only substitute AP location state for items that actually
                // represent randomized vanilla acquisition locations.
                if (data == null ||
                    !data.CreatesLocation ||
                    !data.LocationId.HasValue)
                {
                    return false;
                }

                // IMPORTANT:
                // This deliberately means "the vanilla acquisition location
                // was reached", NOT "Archipelago sent us this item".
                return CheckedItems.Contains(guid);
            }
            catch (System.Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP QUEST COMPAT] Failed checking virtual " +
                    $"vanilla acquisition: {ex}"
                );

                return false;
            }
        }

        public static bool ShouldSuppressVanillaLoadRestore(
    Item item)
        {
            if (item == null)
                return false;

            try
            {
                string guid = item.GetGUID();

                if (string.IsNullOrEmpty(guid))
                    return false;

                RandomizedItemData? data =
                    ItemData.ByGuid(guid);

                // Only canonical randomized vanilla acquisition locations
                // participate in this protection.
                //
                // This deliberately excludes internal quest/state items and
                // special multi-discovery handling such as Tears/Coin Purses.
                if (data == null ||
                    !data.CreatesLocation ||
                    !data.LocationId.HasValue)
                {
                    return false;
                }

                // The vanilla source has already been consumed as an AP check,
                // but Archipelago has not actually given this item to us.
                //
                // In that state, vanilla load-time fixups must not recreate the
                // physical item.
                return CheckedItems.Contains(guid) &&
                       !UnlockedItems.Contains(guid);
            }
            catch (System.Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP LOAD REPAIR] Failed checking load-time " +
                    $"restore suppression: {ex}"
                );

                return false;
            }
        }

        public static bool IsLocationChecked(string guid)
        {
            if (string.IsNullOrEmpty(guid))
                return false;

            return CheckedItems.Contains(guid);
        }

        public static bool IsItemUnlocked(string guid)
        {
            if (string.IsNullOrEmpty(guid))
                return false;

            return UnlockedItems.Contains(guid);
        }



        private static bool TryGetNextMultiDiscoveryLocation(
    RandomizedItemData data,
    out MultiDiscoveryLocationData? location)
        {
            location = null;

            if (data == null ||
                !ItemData.IsMultiDiscoveryItem(data))
            {
                return false;
            }

            List<MultiDiscoveryLocationData> locations =
                ItemData.GetMultiDiscoveryLocations(data);

            foreach (MultiDiscoveryLocationData candidate
                     in locations)
            {
                if (!ArchipelagoClient.IsLocationChecked(
                        candidate.LocationId))
                {
                    location = candidate;
                    return true;
                }
            }

            return false;
        }
    }

    public static class MerchantRandomizer
    {
        private static int purchaseDepth = 0;

        public static bool PurchaseInProgress =>
            purchaseDepth > 0;

        public static void BeginPurchase()
        {
            purchaseDepth++;
        }

        public static void EndPurchase()
        {
            if (purchaseDepth > 0)
                purchaseDepth--;
        }

        public static bool ProcessPurchasedItem(
            ref Item item,
            int quantity
            )
        {
            return ItemRandomizer.ProcessNaturalItem(
                ref item,
                quantity
            );
        }

        private static int _refreshStoreDepth = 0;

        private static readonly HashSet<string>
            _uncheckedMerchantItemGuids = new HashSet<string>();

        public static bool RefreshStoreInProgress =>
            _refreshStoreDepth > 0;

        public static void BeginRefreshStore()
        {
            _refreshStoreDepth++;

            if (_refreshStoreDepth == 1)
                _uncheckedMerchantItemGuids.Clear();
        }

        public static void RegisterUncheckedMerchantItem(
            RandomizedItemData data)
        {
            if (data == null ||
                string.IsNullOrEmpty(data.Guid))
            {
                return;
            }

            _uncheckedMerchantItemGuids.Add(
                data.Guid.ToLowerInvariant()
            );
        }

        public static bool ShouldIgnoreVanillaOwnership(Item item)
        {
            if (!RefreshStoreInProgress ||
                item == null)
            {
                return false;
            }

            try
            {
                string guid = item.GetGUID();

                if (string.IsNullOrEmpty(guid))
                    return false;

                return _uncheckedMerchantItemGuids.Contains(
                    guid.ToLowerInvariant()
                );
            }
            catch
            {
                return false;
            }
        }

        public static void EndRefreshStore()
        {
            if (_refreshStoreDepth > 0)
                _refreshStoreDepth--;

            if (_refreshStoreDepth == 0)
                _uncheckedMerchantItemGuids.Clear();
        }

        public static bool TryGetMerchantLocation(
    CraftingCombination combo,
    out RandomizedItemData? data)
        {
            data = null;

            if (combo == null)
                return false;

            /*
             * Archipelago merchant locations represent items the PLAYER BUYS.
             *
             * CraftingUIController is also used for:
             *
             *   - ordinary crafting
             *   - selling player-owned items
             *
             * Those must remain completely vanilla and must never participate
             * in AP merchant stock filtering/presentation.
             */
            if (combo.craftingType !=
                CraftingCombination.CraftingType.Purchase)
            {
                return false;
            }

            Item item = combo.result;

            if (item == null)
                return false;

            string guid = item.GetGUID();

            if (string.IsNullOrEmpty(guid))
                return false;

            RandomizedItemData? found =
                ItemData.ByGuid(guid);

            if (found == null ||
                !found.CreatesLocation ||
                !found.LocationId.HasValue)
            {
                return false;
            }

            data = found;
            return true;
        }


        public static bool IsMerchantLocationChecked(
            CraftingCombination combo)
        {
            if (!TryGetMerchantLocation(
                    combo,
                    out RandomizedItemData? data) ||
                data == null ||
                !data.LocationId.HasValue)
            {
                return false;
            }

            return ArchipelagoClient.IsLocationChecked(
                data.LocationId.Value
            );
        }


    }
}