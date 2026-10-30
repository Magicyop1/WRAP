using System;
using System.Collections.Generic;

namespace WitheringRoomsArchipelago
{
    public sealed class RemembranceShrineLocationData
    {
        public string LocationName { get; }

        public string Name { get; }
        public string RoomGuid { get; }
        public long LocationId { get; }

        public RemembranceShrineLocationData(
            string name,
            string roomGuid,
            long locationId,
            string locationName)
        {
            Name = name;
            LocationName = locationName;
            RoomGuid = roomGuid;
            LocationId = locationId;

        }
    }

    public static class RemembranceShrineData
    {
        private static readonly List<RemembranceShrineLocationData>
            Locations = new()
            {
                // AUTO-GENERATED FROM remembrance_shrines.csv
// Paste into RemembranceShrineData.Locations.

new(
    "CoffinRoom",
    "658bb443034365f4f95d8300d22e20e8",
    locationId: 781001,
    locationName: "Coffin Room Remembrance Shrine Offering"
),

new(
    "HedgeMazeFinalRoom",
    "87ffb81f6ce06304e8c1385d3c08d1ff",
    locationId: 781002,
    locationName: "Hedge Maze Final Room Remembrance Shrine Offering"
),

new(
    "NowhereRoomCard",
    "8a3a0192a94794949998c22a826750a5",
    locationId: 781003,
    locationName: "Nowhere Remembrance Shrine Offering"
),

new(
    "OccultLibraryRoom",
    "6004319eb2f5de547ae38b9bef18431a",
    locationId: 781004,
    locationName: "Occult Library Remembrance Shrine Offering"
),

new(
    "RightHouseExitRoom",
    "8f6f1e72e7d4f914a9e0dab8499e1528",
    locationId: 781005,
    locationName: "Right House Exit Remembrance Shrine Offering"
),

new(
    "TombCard",
    "2bf2226d4f4d0ea499f8eefdce0b01da",
    locationId: 781006,
    locationName: "Tomb Remembrance Shrine Offering"
),

new(
    "WestStairwellCard",
    "b298ac5c5d9cd8b4d857ca4eb8932744",
    locationId: 781007,
    locationName: "West Stairwell Remembrance Shrine Offering"
),

new(
    "WineRoom",
    "68e5dd6d1531c7e478b10d98f1aa7701",
    locationId: 781008,
    locationName: "Wine Room Remembrance Shrine Offering"
),

new(
    "BlackettAtticStorageRoom",
    "112a6ccbc4510564fb0a9064e215d877",
    locationId: 781009,
    locationName: "Blackett Attic Storage Room Remembrance Shrine Offering"
),

new(
    "Observatory",
    "d7d694fb5f60763428690238f4ce0839",
    locationId: 781010,
    locationName: "Observatory Remembrance Shrine Offering"
),

new(
    "TombCard_Chapter2",
    "285d223bbd79fe5479419e03c71995ff",
    locationId: 781011,
    locationName: "Chapter 2 Tomb Remembrance Shrine Offering"
),

new(
    "UpperFloorMargaretRoomCard",
    "d71eed4b5dbaa5844867a286b1eb84b0",
    locationId: 781012,
    locationName: "Upper Floor Margaret Room Remembrance Shrine Offering"
),

new(
    "1916_AtticPrisonRoom",
    "de703ddba4a2aae468ba765115c23a8b",
    locationId: 781013,
    locationName: "1916 Attic Prison Remembrance Shrine Offering"
),

new(
    "1916_LeftHouseExitRoom",
    "2f348ff005b0b36478479aecb9655f69",
    locationId: 781014,
    locationName: "1916 Left House Exit Remembrance Shrine Offering"
),

new(
    "1916_StrangeBedroom",
    "a76e8e95a9e80da46ba2c5416bdff7b6",
    locationId: 781015,
    locationName: "1916 Strange Bedroom Remembrance Shrine Offering"
),

new(
    "1916_UpperBanquetHallCard",
    "937e57f0501006a4aafb294d9609c9ff",
    locationId: 781016,
    locationName: "1916 Upper Banquet Hall Remembrance Shrine Offering"
),

new(
    "1916_WestStairWellCard",
    "c52803e0f6ac66a44a654639db767869",
    locationId: 781017,
    locationName: "1916 West Stairwell Remembrance Shrine Offering"
),

new(
    "ChurchSecondStairwell",
    "ccb53dafabc639747a6e793ee274ee69",
    locationId: 781018,
    locationName: "Church Second Stairwell Remembrance Shrine Offering"
),

new(
    "EastForestVillageRoomCard",
    "3ddb9378dc824d34aa71fbcad8c1e4fc",
    locationId: 781019,
    locationName: "East Forest Village Remembrance Shrine Offering"
),

new(
    "Nowhere3RoomCard",
    "26e1473cfbc315e44975412617ca9906",
    locationId: 781020,
    locationName: "1916 Nowhere Remembrance Shrine Offering"
),

new(
    "WestForestCard",
    "460e766149bf29f48a3164d785f3fc57",
    locationId: 781021,
    locationName: "West Forest Remembrance Shrine Offering"
),

new(
    "BloodTowerSecondFloorHall",
    "b2961fb14de8d2e44907b900f3d31b29",
    locationId: 781022,
    locationName: "Blood Tower Second Floor Hall Remembrance Shrine Offering"
),

            };

        private static readonly Dictionary<
            string,
            RemembranceShrineLocationData
        > ByRoomGuidLookup = BuildRoomGuidLookup();

        private static Dictionary<
            string,
            RemembranceShrineLocationData
        > BuildRoomGuidLookup()
        {
            var result = new Dictionary<
                string,
                RemembranceShrineLocationData
            >(StringComparer.OrdinalIgnoreCase);

            foreach (RemembranceShrineLocationData data in Locations)
            {
                result[data.RoomGuid] = data;
            }

            return result;
        }

        public static IEnumerable<RemembranceShrineLocationData> All()
        {
            return Locations;
        }

        public static RemembranceShrineLocationData? ByRoomGuid(
            string roomGuid)
        {
            if (string.IsNullOrEmpty(roomGuid))
                return null;

            if (ByRoomGuidLookup.TryGetValue(
                    roomGuid,
                    out RemembranceShrineLocationData? data))
            {
                return data;
            }

            return null;
        }
    }
}