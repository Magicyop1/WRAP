using System;
using System.Collections.Generic;

namespace WitheringRoomsArchipelago
{
    public static class LoreRandomizer
    {
        public static void ProcessNaturalLore(
    LoreItem lore)
        {
            if (lore == null)
                return;

            string guid = lore.GetGUID();

            if (!ArchipelagoClient.Loresanity)
                return;

            LoreLocationData? data =
                LoreData.ByGuid(guid);

            if (data == null)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LORE] No AP lore location for " +
                    $"{lore.GetTitle()} ({guid})"
                );

                return;
            }

            long locationId =
                data.LocationId;

            if (locationId <= 0)
            {
                Plugin.LogSource.LogInfo(
                    $"[AP LORE] Recognized temporary lore entry: " +
                    $"{data.Name} ({guid}); " +
                    $"no AP location ID assigned yet."
                );

                return;
            }

            if (ArchipelagoClient.IsLocationChecked(locationId))
            {
                Plugin.LogSource.LogInfo(
                    $"[AP LORE] Already checked: " +
                    $"{data.Name} ({locationId})"
                );

                return;
            }

            if (!ArchipelagoClient.Connected)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LORE] Cannot send {data.Name}: " +
                    $"not connected."
                );

                return;
            }

            if (!ArchipelagoClient.SendLocationCheck(locationId))
                return;

            Plugin.LogSource.LogInfo(
                $"[AP LORE CHECK] Sending {data.Name}: " +
                $"{locationId}"
            );

            QueueLoreNotification(
                lore,
                data
            );
        }


        private static void QueueLoreNotification(
    LoreItem lore,
    LoreLocationData data)
        {
            if (!ArchipelagoClient.TryGetCheckInfo(
                    data.LocationId,
                    out long apItemId,
                    out string apItemName,
                    out string receivingPlayer))
            {
                Plugin.LogSource.LogWarning(
                    $"[AP LORE] Location {data.LocationId} was sent, " +
                    $"but no scout information was cached."
                );

                return;
            }

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
                lore,
                displayItem,
                apItemName,
                receivingPlayer,
                data.LocationName
            );
        }
    }
}