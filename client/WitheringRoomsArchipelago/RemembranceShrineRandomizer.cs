using System;

namespace WitheringRoomsArchipelago
{
    public static class RemembranceShrineRandomizer
    {
        public static void ProcessShrineActivation(
            RoomCard roomCard)
        {
            if (roomCard == null)
                return;

            string roomGuid = roomCard.GetGUID();

            if (string.IsNullOrEmpty(roomGuid))
            {
                Plugin.LogSource.LogWarning(
                    "[AP SHRINE] Activated shrine has no RoomCard GUID."
                );

                return;
            }

            RemembranceShrineLocationData? data =
                RemembranceShrineData.ByRoomGuid(
                    roomGuid
                );

            if (data == null)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP SHRINE] No AP shrine location for " +
                    $"{roomCard.name} ({roomGuid})."
                );

                return;
            }

            long locationId = data.LocationId;

            if (ArchipelagoClient.IsLocationChecked(
                    locationId))
            {
                Plugin.LogSource.LogInfo(
                    $"[AP SHRINE] Already checked: " +
                    $"{data.LocationName} ({locationId})"
                );

                return;
            }

            if (!ArchipelagoClient.Connected)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP SHRINE] Cannot send " +
                    $"{data.LocationName}: not connected."
                );

                return;
            }

            if (!ArchipelagoClient.SendLocationCheck(locationId))
            {
                return;
            }

            Plugin.LogSource.LogInfo(
                $"[AP SHRINE CHECK] Sent " +
                $"{data.LocationName} ({locationId})"
            );

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

                Item? offeringItem =
                    GameItems.FindItemByGuid(
                        "55789e69d995cdc44868fa2b1feec995"
                    );

                if (offeringItem != null)
                {
                    ArchipelagoNotifications.QueueCheckSent(
                        offeringItem,
                        displayItem,
                        apItemName,
                        receivingPlayer,
                        data.LocationName
                    );
                }
                else
                {
                    Plugin.LogSource.LogWarning(
                        "[AP SHRINE] Could not resolve Corrupted Finger " +
                        "for shrine check notification."
                    );
                }
            }
            else
            {
                Plugin.LogSource.LogWarning(
                    $"[AP SHRINE] Location {locationId} was sent, " +
                    $"but no scout information was cached."
                );
            }
        }
    }
}