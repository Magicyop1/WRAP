using System;
using HarmonyLib;
using UnityEngine;

namespace WitheringRoomsArchipelago
{
    // ================================================================
    // TEMPORARY HIGH-LEVEL MANSION TRACE
    // ================================================================
    //
    // Static native analysis shows GameScenarioManager.OnSpawningPlayer
    // calling this method during mansion creation.
    //
    // Keep this for the next test so we can confirm the runtime chain.
    //
    [HarmonyPatch(
        typeof(MansionSimulationManager),
        nameof(MansionSimulationManager.GenerateMansion),
        new Type[]
        {
            typeof(MansionCard),
            typeof(int)
        }
    )]
    internal static class MansionSimulationManager_GenerateMansion_APTrace
    {
        [HarmonyPrefix]
        private static void Prefix(
            [HarmonyArgument(0)] MansionCard card,
            [HarmonyArgument(1)] int seed)
        {
            try
            {
                int chapter =
                    GameScenarioManager.instance != null
                        ? GameScenarioManager.instance.chapterIndex
                        : -1;

                Plugin.LogSource.LogWarning(
                    $"[AP MANSION TRACE] GenerateMansion called. " +
                    $"chapter={chapter}, seed={seed}, " +
                    $"card='{(card != null ? card.name : "NULL")}'"
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP MANSION TRACE] GenerateMansion trace failed: {ex}"
                );
            }
        }
    }


    // ================================================================
    // CHAPTER 4 GRANDFATHER CLOCK INJECTION
    // ================================================================
    //
    // MansionGenerator.ConstructRoom is the logical per-room generation
    // method. It runs before the room's FurnitureInstance list has been
    // finalized, making this a much better injection seam than
    // HHMansionGenerator.GenerateRoom.
    //
    [HarmonyPatch(
        typeof(MansionGenerator),
        "ConstructRoom",
        new Type[]
        {
            typeof(Rand),
            typeof(RoomInstance)
        }
    )]
    internal static class Chapter4ClockInjector
    {
        private const int Chapter3 = 3;
        private const int Chapter4 = 4;

        private const string ChurchPlayerRoomGuid =
            "6db1480b99c5f8141b1aa2f1194e663e";

        private const string ChurchPlayerRoomName =
            "ChurchRoom_Player";

        private const string StrangeBedroomGuid =
            "a76e8e95a9e80da46ba2c5416bdff7b6";

        private const string StrangeBedroomName =
            "1916_StrangeBedroom";

        /*
         * Normal GrandfatherClock FurnitureCard from resources.assets.
         *
         * This is NOT one of the SetTo12 / SetTo1159 / NoKey variants.
         */
        private const string GrandfatherClockFurnitureGuid =
            "73f36f5351918634183a62c8d479d557";

        private const string GrandfatherClockName =
            "GrandfatherClock";

        private static FurnitureCardDeck? cachedClockDeck;


        [HarmonyPrefix]
        private static void Prefix(
            [HarmonyArgument(1)] RoomInstance room)
        {
            try
            {
                if (room == null)
                    return;

                GameScenarioManager scenario =
                    GameScenarioManager.instance;

                int chapter =
                    scenario != null
                        ? scenario.chapterIndex
                        : -1;

                /*
 * Only Chapters 3 and 4 currently need injected clocks.
 */
                if (chapter != Chapter3 &&
                    chapter != Chapter4)
                {
                    return;
                }

                RoomInstanceConfig config =
                    room.GetConfig();

                if (config == null ||
                    config.roomCard == null)
                {
                    return;
                }

                RoomCard roomCard =
                    config.roomCard;

                if (!ShouldInjectClock(
                        chapter,
                        roomCard))
                {
                    return;
                }

                string guid =
                    SafeGuid(roomCard);

                Plugin.LogSource.LogWarning(
                    $"[AP CLOCK INJECT] Target room encountered. " +
                    $"Room='{roomCard.name}', GUID='{guid}', chapter={chapter}"
                );



                if (RoomContainsGrandfatherClock(
                        roomCard))
                {
                    Plugin.LogSource.LogInfo(
                        "[AP CLOCK] Target RoomCard already contains " +
                        "a GrandfatherClock furniture deck."
                    );

                    return;
                }

                if (roomCard.furnitureDeckSet == null ||
                    roomCard.furnitureDeckSet.decks == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP CLOCK] Target RoomCard has no usable " +
                        "furnitureDeckSet."
                    );

                    return;
                }

                FurnitureCardDeck? clockDeck =
                    GetGrandfatherClockDeck();

                if (clockDeck == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP CLOCK] Could not find an already-loaded " +
                        "GrandfatherClock furniture deck."
                    );

                    return;
                }

                int before =
                    roomCard.furnitureDeckSet.decks.Count;

                /*
                 * This happens BEFORE vanilla ConstructRoom builds the
                 * FurnitureInstance data for this room.
                 */
                roomCard.furnitureDeckSet.decks.Add(
                    clockDeck
                );

                int after =
                    roomCard.furnitureDeckSet.decks.Count;

                Plugin.LogSource.LogWarning(
                    $"[AP CLOCK] Injected GrandfatherClock deck BEFORE " +
                    $"logical room construction. DeckCount {before} -> {after}."
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP CLOCK] ConstructRoom prefix failed: {ex}"
                );
            }
        }


        [HarmonyPostfix]
        private static void Postfix(
            [HarmonyArgument(1)] RoomInstance room)
        {
            try
            {
                if (room == null)
                    return;

                GameScenarioManager scenario =
    GameScenarioManager.instance;

                if (scenario == null)
                    return;

                int chapter =
                    scenario.chapterIndex;

                if (chapter != Chapter3 &&
                    chapter != Chapter4)
                {
                    return;
                }

                RoomInstanceConfig config =
                    room.GetConfig();

                if (config == null ||
    config.roomCard == null ||
    !ShouldInjectClock(
        chapter,
        config.roomCard))
                {
                    return;
                }

                var furniture =
                    config.GetRawFurniture();

                if (furniture == null)
                {
                    Plugin.LogSource.LogWarning(
                        "[AP CLOCK TRACE] ConstructRoom finished, but " +
                        "GetRawFurniture() returned NULL."
                    );

                    return;
                }

                bool foundClock = false;

                for (int i = 0;
                     i < furniture.Count;
                     i++)
                {
                    FurnitureInstance instance =
                        furniture[i];

                    if (instance == null ||
                        instance.card == null)
                    {
                        continue;
                    }

                    FurnitureCard card =
                        instance.card;

                    if (IsGrandfatherClock(card))
                    {
                        foundClock = true;

                        Plugin.LogSource.LogWarning(
                            $"[AP CLOCK INJECT TRACE] Generated logical clock! " +
                            $"Room='{config.roomCard.name}', chapter={chapter}, " +
                            $"Furniture[{i}]='{card.name}', " +
                            $"GUID='{SafeGuid(card)}'"
                        );
                    }
                }

                Plugin.LogSource.LogWarning(
                    $"[AP CLOCK TRACE] ConstructRoom finished for " +
                    $"ChurchRoom_Player. FurnitureCount={furniture.Count}, " +
                    $"GrandfatherClockGenerated={foundClock}"
                );
            }
            catch (Exception ex)
            {
                Plugin.LogSource.LogError(
                    $"[AP CLOCK TRACE] ConstructRoom postfix failed: {ex}"
                );
            }
        }


        private static bool ShouldInjectClock(
    int chapter,
    RoomCard roomCard)
        {
            if (roomCard == null)
                return false;

            string guid =
                SafeGuid(roomCard);

            /*
             * Chapter 4 emergency clock:
             * immediately available inside the locked church start.
             */
            if (chapter == Chapter4)
            {
                if (string.Equals(
                        guid,
                        ChurchPlayerRoomGuid,
                        StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(
                        roomCard.name,
                        ChurchPlayerRoomName,
                        StringComparison.OrdinalIgnoreCase))
                {
                    return true;
                }
            }

            /*
             * Chapters 3 and 4:
             * guarantee a normal clock in the Strange Bedroom.
             */
            if (chapter == Chapter3 ||
                chapter == Chapter4)
            {
                if (string.Equals(
                        guid,
                        StrangeBedroomGuid,
                        StringComparison.OrdinalIgnoreCase) ||
                    string.Equals(
                        roomCard.name,
                        StrangeBedroomName,
                        StringComparison.OrdinalIgnoreCase))
                {
                    return true;
                }
            }

            return false;
        }


        private static FurnitureCardDeck?
            GetGrandfatherClockDeck()
        {
            if (cachedClockDeck != null &&
                DeckContainsGrandfatherClock(
                    cachedClockDeck))
            {
                return cachedClockDeck;
            }

            RoomCard[] rooms =
                Resources.FindObjectsOfTypeAll<RoomCard>();

            if (rooms == null)
                return null;

            FurnitureCardDeck? fallback =
                null;

            for (int roomIndex = 0;
                 roomIndex < rooms.Length;
                 roomIndex++)
            {
                RoomCard sourceRoom =
                    rooms[roomIndex];

                if (sourceRoom == null ||
                    sourceRoom.furnitureDeckSet == null ||
                    sourceRoom.furnitureDeckSet.decks == null)
                {
                    continue;
                }

                FurnitureDeckSet set =
                    sourceRoom.furnitureDeckSet;

                for (int deckIndex = 0;
                     deckIndex < set.decks.Count;
                     deckIndex++)
                {
                    FurnitureCardDeck deck =
                        set.decks[deckIndex];

                    if (deck == null ||
                        !DeckContainsGrandfatherClock(
                            deck))
                    {
                        continue;
                    }

                    /*
                     * Prefer a deck containing ONLY the clock so we don't
                     * accidentally import unrelated furniture along with it.
                     */
                    if (deck.cards != null &&
                        deck.cards.Length == 1)
                    {
                        cachedClockDeck =
                            deck;

                        Plugin.LogSource.LogWarning(
                            $"[AP CLOCK] Found one-card GrandfatherClock " +
                            $"deck in RoomCard '{sourceRoom.name}', " +
                            $"furnitureDeck[{deckIndex}]."
                        );

                        return deck;
                    }

                    /*
                     * Keep a fallback in case the shipped assets don't
                     * contain an isolated clock deck.
                     */
                    if (fallback == null)
                    {
                        fallback =
                            deck;
                    }
                }
            }

            if (fallback != null)
            {
                cachedClockDeck =
                    fallback;

                Plugin.LogSource.LogWarning(
                    "[AP CLOCK] No isolated GrandfatherClock deck was " +
                    "found; using the first deck containing the clock."
                );
            }

            return fallback;
        }


        private static bool RoomContainsGrandfatherClock(
            RoomCard room)
        {
            if (room == null ||
                room.furnitureDeckSet == null ||
                room.furnitureDeckSet.decks == null)
            {
                return false;
            }

            FurnitureDeckSet set =
                room.furnitureDeckSet;

            for (int i = 0;
                 i < set.decks.Count;
                 i++)
            {
                if (DeckContainsGrandfatherClock(
                        set.decks[i]))
                {
                    return true;
                }
            }

            return false;
        }


        private static bool DeckContainsGrandfatherClock(
            FurnitureCardDeck deck)
        {
            if (deck == null ||
                deck.cards == null)
            {
                return false;
            }

            for (int i = 0;
                 i < deck.cards.Length;
                 i++)
            {
                FurnitureCardEntry entry =
                    deck.cards[i];

                if (entry == null ||
                    entry.card == null)
                {
                    continue;
                }

                if (IsGrandfatherClock(
                        entry.card))
                {
                    return true;
                }
            }

            return false;
        }


        private static bool IsGrandfatherClock(
            FurnitureCard card)
        {
            if (card == null)
                return false;

            string guid =
                SafeGuid(card);

            if (string.Equals(
                    guid,
                    GrandfatherClockFurnitureGuid,
                    StringComparison.OrdinalIgnoreCase))
            {
                return true;
            }

            return string.Equals(
                card.name,
                GrandfatherClockName,
                StringComparison.Ordinal
            );
        }


        private static string SafeGuid(
    RoomCard obj)
        {
            if (obj == null)
                return "";

            try
            {
                return obj.GetGUID() ?? "";
            }
            catch
            {
                return "";
            }
        }


        private static string SafeGuid(
            FurnitureCard obj)
        {
            if (obj == null)
                return "";

            try
            {
                return obj.GetGUID() ?? "";
            }
            catch
            {
                return "";
            }
        }
    }
}