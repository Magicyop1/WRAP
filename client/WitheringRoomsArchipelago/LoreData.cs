using System;
using System.Collections.Generic;

namespace WitheringRoomsArchipelago
{
    /// <summary>
    /// Temporary Loresanity location database.
    ///
    /// This will be replaced/generated from wr_lore_locations.csv
    /// once the lore census is complete.
    /// </summary>
    public sealed class LoreLocationData
    {
        public string Guid { get; }
        public string Name { get; }
        public long LocationId { get; }
        public string LocationName { get; }

        public LoreLocationData(
            string name,
            string guid,
            long locationId,
            string locationName)
        {
            Guid = guid;
            Name = name;
            LocationId = locationId;
            LocationName = locationName ?? name;
        }
    }


    public static class LoreData
    {
        private static readonly List<LoreLocationData> Locations =
            new List<LoreLocationData>()
            {

                // AUTO-GENERATED FROM lore.csv
                // Paste into LoreData.Locations.

                new(
                    "Gazette, June 8th, 1910",
                    "fa8fb4a09429d6847a52ac806edbdd2d",
                    locationId: 779001,
                    locationName: "Read Gazette, June 8th, 1910"
                ),

                new(
                    "Gazette, September 2nd, 1915",
                    "d23d266803fa49144ba1389f8a16a679",
                    locationId: 779002,
                    locationName: "Read Gazette, September 2nd, 1915"
                ),

                new(
                    "Gazette, January 15, 1895",
                    "7666a04d9005fb24caef6eeb1e2147a1",
                    locationId: 779003,
                    locationName: "Read Gazette, January 15, 1895"
                ),

                new(
                    "Gazette, July 20th, 1916",
                    "e674a7cd52210d040995cc96e22962c5",
                    locationId: 779004,
                    locationName: "Read Gazette, July 20th, 1916"
                ),

                new(
                    "Expedition Notes 1",
                    "57ef5fb858252f8458bc67cc78fcfc9c",
                    locationId: 779005,
                    locationName: "Read Expedition Notes 1"
                ),

                new(
                    "Expedition Notes 2",
                    "bf98b13e007d49d4e815a0b45183c8c3",
                    locationId: 779006,
                    locationName: "Read Expedition Notes 2"
                ),

                new(
                    "Expedition Notes 3",
                    "14f710a778fa7ab40bb270cf646d5599",
                    locationId: 779007,
                    locationName: "Read Expedition Notes 3"
                ),

                new(
                    "Case Notes 1",
                    "b66229e598b12c7458db97eb5c4954e3",
                    locationId: 779008,
                    locationName: "Read Case Notes 1"
                ),

                new(
                    "Case Notes 2",
                    "b6229a9f44dcda84cae1b53fb63530b2",
                    locationId: 779009,
                    locationName: "Read Case Notes 2"
                ),

                new(
                    "Case Notes 3",
                    "3176e07356419ef4eb2bf4e51b9156aa",
                    locationId: 779010,
                    locationName: "Read Case Notes 3"
                ),

                new(
                    "Gatehouse Key",
                    "370c390c95936f645be297e9bde82a5c",
                    locationId: 779011,
                    locationName: "Read Gatehouse Key"
                ),

                new(
                    "Special Placement Log",
                    "1d466c305a473f349a785445e3cf0056",
                    locationId: 779012,
                    locationName: "Read Special Placement Log"
                ),

                new(
                    "Mostyn House Map",
                    "f064c4007d9c61b44895ccf2052190df",
                    locationId: 779013,
                    locationName: "Read Mostyn House Map"
                ),

                new(
                    "Disciple's Path",
                    "8a303dd7b1afcec4790845393f686fbd",
                    locationId: 779014,
                    locationName: "Read Disciple's Path"
                ),

                new(
                    "Ode to a Nightingale",
                    "928634c124cbd9049a9fc247c15ce45e",
                    locationId: 779015,
                    locationName: "Read Ode to a Nightingale"
                ),

                new(
                    "Outcast's Diary, 1916",
                    "6ae264750e37d0c4d81c1abb611d26cf",
                    locationId: 779016,
                    locationName: "Read Outcast's Diary, 1916"
                ),

                new(
                    "Father's Letter",
                    "e1975b50877ff61418c856da1a690c4d",
                    locationId: 779017,
                    locationName: "Read Father's Letter"
                ),

                new(
                    "The Feast",
                    "c02a399fe9ea70f4c92a287064ba0785",
                    locationId: 779018,
                    locationName: "Read The Feast"
                ),

                new(
                    "About Beca",
                    "80b9c5012e8855e4b9b19bbceffc3076",
                    locationId: 779019,
                    locationName: "Read About Beca"
                ),

                new(
                    "To Father",
                    "2f0a7e1371bd0944ea8e0d8e6f2fa14a",
                    locationId: 779020,
                    locationName: "Read To Father"
                ),

                new(
                    "Welcome to the Blood Tower",
                    "bb77f20eb80b3934f8a33c543cdb21ba",
                    locationId: 779021,
                    locationName: "Read Welcome to the Blood Tower"
                ),

                new(
                    "Welsh Country Houses 1",
                    "e5e3ffeee48d91540bdee7b1422f722a",
                    locationId: 779022,
                    locationName: "Read Welsh Country Houses 1"
                ),

                new(
                    "Welsh Country Houses 2",
                    "7a9e9069df960854d99ebc4744f6d2e4",
                    locationId: 779023,
                    locationName: "Read Welsh Country Houses 2"
                ),

                new(
                    "Welsh Country Houses 3",
                    "ea5a7aa8157b1f54a89b5f23040996c3",
                    locationId: 779024,
                    locationName: "Read Welsh Country Houses 3"
                ),

                new(
                    "Welsh Country Houses 4",
                    "af4fb766fb0f67f4fae9a9fed474d7bf",
                    locationId: 779025,
                    locationName: "Read Welsh Country Houses 4"
                ),

                new(
                    "Welsh Country Houses 5",
                    "8adfb1582bb0bab4aa7998a245f3ddb5",
                    locationId: 779026,
                    locationName: "Read Welsh Country Houses 5"
                ),

                new(
                    "Welsh Country Houses 6",
                    "bc4ea5d2098e603449b84d0496b9d220",
                    locationId: 779027,
                    locationName: "Read Welsh Country Houses 6"
                ),

                new(
                    "Welsh Country Houses 7",
                    "3e626afb3171f974d935bf96c6a735cd",
                    locationId: 779028,
                    locationName: "Read Welsh Country Houses 7"
                ),

                new(
                    "Boiler Room Note",
                    "feca8e21b81517745b9bb344620ff6a8",
                    locationId: 779029,
                    locationName: "Read Boiler Room Note"
                ),

                new(
                    "Cagewood Memorial",
                    "ba82b8360b4af8c489f7510ab7c242ed",
                    locationId: 779030,
                    locationName: "Read Cagewood Memorial"
                ),

                new(
                    "Hedge Maze Shopping List",
                    "174a4f23eb4ee5f45a417e4a215ac66a",
                    locationId: 779031,
                    locationName: "Read Hedge Maze Shopping List"
                ),

                new(
                    "Hunting Guide",
                    "0002b52d6382d004da8e2cbe865632d3",
                    locationId: 779032,
                    locationName: "Read Hunting Guide"
                ),

                new(
                    "drsfenechod oanjiire",
                    "fdebc0eae21609a4b86fa242641b56c0",
                    locationId: 779033,
                    locationName: "Read drsfenechod oanjiire"
                ),

                new(
                    "Wrong Room",
                    "19131a9cbb539024a9aa27148cdb3956",
                    locationId: 779034,
                    locationName: "Read Wrong Room"
                ),

                new(
                    "Outcast’s Diary, 1885",
                    "7e3b0a890c1d41840946c0a3b123d379",
                    locationId: 779035,
                    locationName: "Read Outcast’s Diary, 1885"
                ),

                new(
                    "Outcast's Diary, 1886",
                    "3ecc8396a189ef845bd51d1e5313f21b",
                    locationId: 779036,
                    locationName: "Read Outcast's Diary, 1886"
                ),

                new(
                    "Outcast's Diary, 1887",
                    "5bea87b63046e0d4d96cd63991e57bc0",
                    locationId: 779037,
                    locationName: "Read Outcast's Diary, 1887"
                ),

                new(
                    "Part I",
                    "6eed845124391a94791b733757f2d5ad",
                    locationId: 779038,
                    locationName: "Read Part I"
                ),

                new(
                    "Poncer's Chess 1",
                    "f52f902abb3ab954cbcce7c00f12cd84",
                    locationId: 779040,
                    locationName: "Read Poncer's Chess 1"
                ),

                new(
                    "Poncer's Chess 2",
                    "69da986c18337a244aa857e6aee9694f",
                    locationId: 779041,
                    locationName: "Read Poncer's Chess 2"
                ),

                new(
                    "Poncer's Chess 3",
                    "2f080248d6fc4d945b66fc0aaa53c1d7",
                    locationId: 779042,
                    locationName: "Read Poncer's Chess 3"
                ),

                new(
                    "Priscilla's Dream Histories 1",
                    "9786027b3dba58d4b983443f4b961844",
                    locationId: 779043,
                    locationName: "Read Priscilla's Dream Histories 1"
                ),

                new(
                    "Priscilla's Dream Histories 2",
                    "831cc516808f7144cb1e2672a7a81910",
                    locationId: 779044,
                    locationName: "Read Priscilla's Dream Histories 2"
                ),

                new(
                    "Priscilla's Dream Histories 3",
                    "95d8efd72fcc48948a6d41f09cab5819",
                    locationId: 779045,
                    locationName: "Read Priscilla's Dream Histories 3"
                ),

                new(
                    "Priscilla's Storage Note",
                    "9034636f7163f1640b9291159d732757",
                    locationId: 779046,
                    locationName: "Read Priscilla's Storage Note"
                ),

                new(
                    "Blood Tower Schematic",
                    "7d8b6160ec83ef741939996a1010be7c",
                    locationId: 779047,
                    locationName: "Read Blood Tower Schematic"
                ),

                new(
                    "Research Avenues",
                    "ed317ef177557f346aab32c81f972980",
                    locationId: 779048,
                    locationName: "Read Research Avenues"
                ),

                new(
                    "Lab Notes",
                    "0d23c6ca6c56a4e489ad941a74a2f9de",
                    locationId: 779049,
                    locationName: "Read Lab Notes"
                ),

                new(
                    "Memorandum",
                    "039648b950bf4334492e252d6f72c2ce",
                    locationId: 779050,
                    locationName: "Read Memorandum"
                ),

                new(
                    "To Robert",
                    "496f78da1f24ee34caee561b5943c8c3",
                    locationId: 779051,
                    locationName: "Read To Robert"
                ),

                new(
                    "Wiring Requirements",
                    "a60908674dbdba94a8517baac5b84b88",
                    locationId: 779052,
                    locationName: "Read Wiring Requirements"
                ),

                new(
                    "Philosophiae Somnium 1",
                    "89f07ea47fe508b4299512b1785d1828",
                    locationId: 779053,
                    locationName: "Read Philosophiae Somnium 1"
                ),

                new(
                    "Philosophiae Somnium 2",
                    "d6732e5c15ac77c4594be2368bfecc2c",
                    locationId: 779054,
                    locationName: "Read Philosophiae Somnium 2"
                ),

                new(
                    "Philosophiae Somnium 3",
                    "51de3d30ffc1eb8419b1d1d87f34d31a",
                    locationId: 779055,
                    locationName: "Read Philosophiae Somnium 3"
                ),

                new(
                    "Philosophiae Somnium 4",
                    "c0cbaab1e1fdc1c4c969b0e626cc862d",
                    locationId: 779056,
                    locationName: "Read Philosophiae Somnium 4"
                ),

                new(
                    "Philosophiae Somnium 5",
                    "889b54510d4ddfa4c88448e68c5d9d93",
                    locationId: 779057,
                    locationName: "Read Philosophiae Somnium 5"
                ),

                new(
                    "Philosophiae Somnium 6",
                    "301f50f354169f440be1d551f0670d5f",
                    locationId: 779058,
                    locationName: "Read Philosophiae Somnium 6"
                ),

                new(
                    "Bloody Letter",
                    "f4c6bcd3f3051564293de122df06c1a6",
                    locationId: 779059,
                    locationName: "Read Bloody Letter"
                ),

                new(
                    "To Wretch",
                    "9e744b6fc0b20294594b128dad40d860",
                    locationId: 779060,
                    locationName: "Read To Wretch"
                ),

                new(
                    "To Nightingale",
                    "42b61640bb8bec8409c790155d0af007",
                    locationId: 779061,
                    locationName: "Read To Nightingale"
                ),

                new(
                    "Organ Processing Note",
                    "f99446b3fae54c8478cf60f074354424",
                    locationId: 779062,
                    locationName: "Read Organ Processing Note"
                ),

                new(
                    "To the First Witch",
                    "cc1c78804df493b48a436a004ee41590",
                    locationId: 779063,
                    locationName: "Read To the First Witch"
                ),

                new(
                    "Inscription",
                    "05bed47101f878743a241650adb25ebf",
                    locationId: 779064,
                    locationName: "Read Inscription"
                ),

                new(
                    "Priscilla Mostyn",
                    "033bedfa81a381f42b4859dc6edc04ab",
                    locationId: 779065,
                    locationName: "Read Priscilla Mostyn"
                ),

                new(
                    "Peter Mostyn",
                    "8b5697b4aab55cb418d42f65fbd2da79",
                    locationId: 779066,
                    locationName: "Read Peter Mostyn"
                ),

                new(
                    "Alfred Mostyn",
                    "43e32d847f5a7a047a0a1dd62cc790c3",
                    locationId: 779067,
                    locationName: "Read Alfred Mostyn"
                ),

                new(
                    "Anne Mostyn",
                    "71d2094420372c04ea3040bafa6ac3a7",
                    locationId: 779068,
                    locationName: "Read Anne Mostyn"
                ),

                new(
                    "Spirits: Theory & Practice 1",
                    "190a597540163cf4b9d9cad974ca9a31",
                    locationId: 779069,
                    locationName: "Read Spirits: Theory & Practice 1"
                ),

                new(
                    "Spirits: Theory & Practice 2",
                    "ad5bb440faa989b429dc98c973404990",
                    locationId: 779070,
                    locationName: "Read Spirits: Theory & Practice 2"
                ),

                new(
                    "Combat Training Procedure",
                    "627640c1fdfd3e74f8e3d75e79166157",
                    locationId: 779071,
                    locationName: "Read Combat Training Procedure"
                ),

                new(
                    "Tactics Manual",
                    "b17bf26f8b5bab9489412e00d1aa97b6",
                    locationId: 779072,
                    locationName: "Read Tactics Manual"
                ),

                new(
                    "The Horrors of Messina",
                    "81fa1f9c9b986584685e7ad19ba18c66",
                    locationId: 779075,
                    locationName: "Read The Horrors of Messina"
                ),




            };


        private static readonly Dictionary<string, LoreLocationData>
            ByGuidLookup =
                new Dictionary<string, LoreLocationData>(
                    StringComparer.OrdinalIgnoreCase
                );


        static LoreData()
        {
            foreach (LoreLocationData data in Locations)
            {
                ByGuidLookup[data.Guid] = data;
            }
        }


        public static LoreLocationData? ByGuid(
            string guid)
        {
            if (string.IsNullOrEmpty(guid))
                return null;

            if (ByGuidLookup.TryGetValue(
                    guid,
                    out LoreLocationData? data))
            {
                return data;
            }

            return null;
        }


        public static IReadOnlyList<LoreLocationData> All()
        {
            return Locations;
        }
    }
}