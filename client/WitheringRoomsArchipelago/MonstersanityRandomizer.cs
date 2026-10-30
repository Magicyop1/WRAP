namespace WitheringRoomsArchipelago
{
    public static class MonstersanityRandomizer
    {
        public static void ProcessBestiary(
    MonsterBestiaryLoreItem bestiary)
        {
            if (bestiary == null)
                return;

            string guid = bestiary.GetGUID();

            /*
             * Goal detection must happen regardless...
             */
            GoalManager.ProcessDefeatedMonster(
                guid
            );

            if (!ArchipelagoClient.Monstersanity)
                return;

            MonsterLocationData? data =
                MonsterData.ByGuid(guid);

            if (data == null)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP MONSTER] No AP monster location for " +
                    $"{bestiary.GetTitle()} ({guid})"
                );

                return;
            }

            long locationId = data.LocationId;

            if (ArchipelagoClient.IsLocationChecked(locationId))
            {
                Plugin.LogSource.LogInfo(
                    $"[AP MONSTER] Already checked: " +
                    $"{data.LocationName} ({locationId})"
                );

                return;
            }

            if (!ArchipelagoClient.Connected)
            {
                Plugin.LogSource.LogWarning(
                    $"[AP MONSTER] Cannot send " +
                    $"{data.LocationName}: not connected."
                );

                return;
            }

            if (!ArchipelagoClient.SendLocationCheck(locationId))
                return;

            Plugin.LogSource.LogInfo(
                $"[AP MONSTER CHECK] Sending " +
                $"{data.LocationName}: {locationId}"
            );

            QueueMonsterNotification(
                bestiary,
                data
            );
        }


        private static void QueueMonsterNotification(
            MonsterBestiaryLoreItem bestiary,
            MonsterLocationData data)
        {
            if (!ArchipelagoClient.TryGetCheckInfo(
                    data.LocationId,
                    out long apItemId,
                    out string apItemName,
                    out string receivingPlayer))
            {
                Plugin.LogSource.LogWarning(
                    $"[AP MONSTER] Location {data.LocationId} " +
                    $"was sent, but no scout information was cached."
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
                bestiary,
                displayItem,
                apItemName,
                receivingPlayer,
                data.LocationName
            );
        }
    }
}