using UnityEngine;

namespace WitheringRoomsArchipelago
{
    public static class GameItems
    {
        public static Item? FindItemByGuid(string guid)
        {
            // Fast path: already-loaded object.
            var items = Resources.FindObjectsOfTypeAll<Item>();

            foreach (var item in items)
            {
                if (item != null && item.GetGUID() == guid)
                    return item;
            }

            // Slow/fallback path: ask Withering Rooms' database.
            var databases =
                Resources.FindObjectsOfTypeAll<ItemDatabase>();

            foreach (var database in databases)
            {
                if (database == null)
                    continue;

                try
                {
                    Item? item = database.CardForGUID(guid);

                    if (item != null)
                        return item;
                }
                catch (System.Exception ex)
                {
                    Plugin.LogSource.LogWarning(
                        $"[GAME ITEMS] Database lookup failed for {guid}: {ex}"
                    );
                }
            }

            Plugin.LogSource.LogWarning(
                $"[GAME ITEMS] Could not resolve item GUID {guid}."
            );

            return null;
        }


        private static Item? FindLoadedItemByGuid(
            string guid)
        {
            var items =
                Resources.FindObjectsOfTypeAll<Item>();

            foreach (var item in items)
            {
                if (item != null &&
                    item.GetGUID() == guid)
                {
                    return item;
                }
            }

            return null;
        }


        private static Item? FindItemInDatabase(
            string guid)
        {
            var databases =
                Resources.FindObjectsOfTypeAll<ItemDatabase>();

            Plugin.LogSource.LogInfo(
                $"[GAME ITEMS] Found {databases.Length} " +
                $"loaded ItemDatabase object(s)."
            );

            foreach (var database in databases)
            {
                if (database == null)
                    continue;

                try
                {
                    Item? item =
                        database.CardForGUID(guid);

                    if (item != null)
                        return item;
                }
                catch (System.Exception ex)
                {
                    Plugin.LogSource.LogWarning(
                        $"[GAME ITEMS] ItemDatabase.CardForGUID " +
                        $"failed: {ex.Message}"
                    );
                }
            }

            return null;
        }


        public static void LogItemAvailability(
            string name,
            string guid)
        {
            var items =
                Resources.FindObjectsOfTypeAll<Item>();

            bool found = false;

            foreach (var item in items)
            {
                if (item != null &&
                    item.GetGUID() == guid)
                {
                    found = true;
                    break;
                }
            }

            if (found)
            {
                Plugin.LogSource.LogInfo(
                    $"[GAME ITEMS] {name} IS directly loaded. " +
                    $"GUID={guid}"
                );
            }
            else
            {
                Plugin.LogSource.LogWarning(
                    $"[GAME ITEMS] {name} is NOT directly loaded. " +
                    $"GUID={guid}. " +
                    $"Loaded Item count={items.Length}"
                );
            }
        }
    }
}