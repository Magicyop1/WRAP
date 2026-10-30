using System;
using System.Collections.Generic;
using System.Linq;

namespace WitheringRoomsArchipelago
{
    public sealed class MonsterLocationData
    {
        public string Name { get; }
        public string Guid { get; }
        public long LocationId { get; }
        public string LocationName { get; }

        public MonsterLocationData(
            string name,
            string guid,
            long locationId,
            string locationName = null)
        {
            Name = name;
            Guid = guid;
            LocationId = locationId;
            LocationName = locationName ?? name;
        }
    }


    public static class MonsterData
    {
        private static readonly List<MonsterLocationData> Locations =
            new()
            {
           

                new(
                    "Beast Nightingale",
                    "b2044414e03716f42966c1f79a49e083",
                    locationId: 780001,
                    locationName: "Defeat Beast Nightingale"
                ),

                new(
                    "Butcher Surgeon",
                    "93706b45b7134af4ba2a64573e3147a8",
                    locationId: 780002,
                    locationName: "Defeat Butcher Surgeon"
                ),

                new(
                    "Night Mother Disciple",
                    "079a4a217ddd20e40b61458bb0c6ee1c",
                    locationId: 780003,
                    locationName: "Defeat Night Mother Disciple"
                ),

                new(
                    "Millie Erwood (Amalgamation)",
                    "d2e0a222769853d4c8bc1bc58c827842",
                    locationId: 780004,
                    locationName: "Defeat Millie Erwood (Amalgamation)"
                ),

                new(
                    "Priscilla Mostyn",
                    "01ddaaf8d4565dc4cb95742a922c1dae",
                    locationId: 780005,
                    locationName: "Defeat Priscilla Mostyn"
                ),

                new(
                    "Graverider",
                    "c73bf444b48a8ba458fb433d53200719",
                    locationId: 780006,
                    locationName: "Defeat Graverider"
                ),

                new(
                    "Old King",
                    "984fe3e9aa9e0824aa625ae96009ca33",
                    locationId: 780007,
                    locationName: "Defeat Old King"
                ),

                new(
                    "Dr. Robert Blackett",
                    "5ba9cc84838e5904f9b3b8a70399b22f",
                    locationId: 780008,
                    locationName: "Defeat Dr. Robert Blackett"
                ),

                new(
                    "Sothach & Baw",
                    "c55e3666e39af744b9a76d02f23ac4c1",
                    locationId: 780009,
                    locationName: "Defeat Sothach & Baw"
                ),

                new(
                    "Final Experiment",
                    "93719839da5681248b2a0ea99ba9712e",
                    locationId: 780010,
                    locationName: "Defeat Final Experiment"
                ),

                new(
                    "Millie Erwood (God)",
                    "9b58dc0db02dbf24fbb430eba593df8e",
                    locationId: 780011,
                    locationName: "Defeat Millie Erwood (God)"
                ),

                new(
                    "First Witch",
                    "fd5276ef539590847bad2d39c3343c8c",
                    locationId: 780012,
                    locationName: "Defeat First Witch"
                ),

                new(
                    "Aborted Experiment",
                    "6dbabdb8d6ef61241b7bb040d6eda636",
                    locationId: 780013,
                    locationName: "Defeat Aborted Experiment"
                ),

                new(
                    "Ancient Champion",
                    "1b0b0b5bf00538b42a232f054944c50d",
                    locationId: 780014,
                    locationName: "Defeat Ancient Champion"
                ),

                new(
                    "Ancient Ghoul",
                    "28af26cd9549cad45917fbf74655398c",
                    locationId: 780015,
                    locationName: "Defeat Ancient Ghoul"
                ),

                new(
                    "Martyr",
                    "8bf09a0c5a7892a4dad477b0a3df305f",
                    locationId: 780016,
                    locationName: "Defeat Martyr"
                ),

                new(
                    "Big Wretch",
                    "c8123e344ced1644c9e77259024234e4",
                    locationId: 780017,
                    locationName: "Defeat Big Wretch"
                ),

                new(
                    "Executioner Wretch",
                    "cd0dd4e6f9003ee44bdfca95ece2487f",
                    locationId: 780018,
                    locationName: "Defeat Executioner Wretch"
                ),

                new(
                    "Corpulent Zombie",
                    "8933c5444606d694fb279a46bcefba56",
                    locationId: 780019,
                    locationName: "Defeat Corpulent Zombie"
                ),

                new(
                    "Burning Zombie",
                    "6937bdad26ab43b4985427681bda5f66",
                    locationId: 780020,
                    locationName: "Defeat Burning Zombie"
                ),

                new(
                    "Cloaked Ghoul",
                    "cdebe188fe98dbf41bb4f02e775a9127",
                    locationId: 780021,
                    locationName: "Defeat Cloaked Ghoul"
                ),

                new(
                    "Hunter Ghoul",
                    "027ad5ab689d27347b468f8cea296439",
                    locationId: 780022,
                    locationName: "Defeat Hunter Ghoul"
                ),

                new(
                    "Mechanical Priscilla",
                    "4980270ee7e43794882ddbffb4cfb713",
                    locationId: 780023,
                    locationName: "Defeat Mechanical Priscilla"
                ),

                new(
                    "Twin Cage",
                    "c05bc333e57c67140afd16a09fcfa711",
                    locationId: 780024,
                    locationName: "Defeat Twin Cage"
                ),

                new(
                    "Cursed Armor",
                    "f10990658d656034e8094b8468f7d6e1",
                    locationId: 780025,
                    locationName: "Defeat Cursed Armor"
                ),

                new(
                    "Bodybag",
                    "d1e110c9868a2894188aec60f768d107",
                    locationId: 780026,
                    locationName: "Defeat Bodybag"
                ),

                new(
                    "Bodybag (Trash)",
                    "e946b8f41dafcda40a47dd009d062ee5",
                    locationId: 780027,
                    locationName: "Defeat Bodybag (Trash)"
                ),

                new(
                    "Felix & Horace",
                    "361a9a14be71fb94285e547ebd7c02fe",
                    locationId: 780028,
                    locationName: "Defeat Felix & Horace"
                ),

                new(
                    "Elite Armor",
                    "b54ade75857a88d4bb5653bf01302327",
                    locationId: 780029,
                    locationName: "Defeat Elite Armor"
                ),

                new(
                    "Angel (Primeval)",
                    "161797579f5fc2d498cc35aa66fb301f",
                    locationId: 780030,
                    locationName: "Defeat Angel (Primeval)"
                ),

                new(
                    "Angel (Fool)",
                    "0e01d34f3c6a81d4495aa2d437624764",
                    locationId: 780031,
                    locationName: "Defeat Angel (Fool)"
                ),

                new(
                    "Angel (Spearman)",
                    "986c66847f4fa4a41b7c93f87af9478b",
                    locationId: 780032,
                    locationName: "Defeat Angel (Spearman)"
                ),

                new(
                    "Angel (Starry)",
                    "e0f13e62d62c7364b96e8ef8214cdb3c",
                    locationId: 780033,
                    locationName: "Defeat Angel (Starry)"
                ),

                new(
                    "Vomit Zombie (Cholera Patient)",
                    "0d167d73106da064da90c2eac3e761a9",
                    locationId: 780034,
                    locationName: "Defeat Vomit Zombie (Cholera Patient)"
                ),

                new(
                    "Ghost (Physician)",
                    "a97623c695dad3c48ac1787757179b59",
                    locationId: 780035,
                    locationName: "Defeat Ghost (Physician)"
                ),

                new(
                    "Ghost (Child)",
                    "c2c0fe28c7eabdd43b1956a99c49daec",
                    locationId: 780036,
                    locationName: "Defeat Ghost (Child)"
                ),

                new(
                    "Ghost (Initiate)",
                    "0ef1d75d3715c5b4aac535c0428b8f62",
                    locationId: 780037,
                    locationName: "Defeat Ghost (Initiate)"
                ),

                new(
                    "Grave Knight",
                    "bccbe89d3eb60e4459df55f4f5f51b79",
                    locationId: 780038,
                    locationName: "Defeat Grave Knight"
                ),

                new(
                    "Groundskeeper (Dafydd)",
                    "56029ccd620d4834c8589fd462b1233c",
                    locationId: 780039,
                    locationName: "Defeat Groundskeeper (Dafydd)"
                ),

                new(
                    "Gurney Physician",
                    "a835d722d64f58642abb37dc0e559271",
                    locationId: 780040,
                    locationName: "Defeat Gurney Physician"
                ),

                new(
                    "Antenna Head",
                    "c2e70597ae8335f4ebdc7a3833cc758c",
                    locationId: 780041,
                    locationName: "Defeat Antenna Head"
                ),

                new(
                    "Heavy Zombie (Cholera Patient)",
                    "f3a0eea6c4dc99748ba975618aff029f",
                    locationId: 780042,
                    locationName: "Defeat Heavy Zombie (Cholera Patient)"
                ),

                new(
                    "Bog Behemoth",
                    "7485e742ff5455a469f52b374cf39837",
                    locationId: 780043,
                    locationName: "Defeat Bog Behemoth"
                ),

                new(
                    "Horse Girl",
                    "6ef448d93bcd66c45a0d274ebeb1b959",
                    locationId: 780044,
                    locationName: "Defeat Horse Girl"
                ),

                new(
                    "Floating Failure",
                    "27c0a5b4e414e50449e8263619f2727e",
                    locationId: 780045,
                    locationName: "Defeat Floating Failure"
                ),

                new(
                    "Burdened Brother",
                    "c726fa366008e2947aa8d1bd8fbfd412",
                    locationId: 780046,
                    locationName: "Defeat Burdened Brother"
                ),

                new(
                    "Initiate",
                    "bee72906c57bd0540a4544e6807c0e3a",
                    locationId: 780047,
                    locationName: "Defeat Initiate"
                ),

                new(
                    "Trickster Initiate",
                    "2945380a3eea6964a8007c59d2595f66",
                    locationId: 780048,
                    locationName: "Defeat Trickster Initiate"
                ),

                new(
                    "Jailkeeper",
                    "316d396b227e8a340a119f6256717232",
                    locationId: 780049,
                    locationName: "Defeat Jailkeeper"
                ),

                new(
                    "Worshipper",
                    "de540ee1646ff264da08ed786ebdb815",
                    locationId: 780050,
                    locationName: "Defeat Worshipper"
                ),

                new(
                    "Ghost (Lady)",
                    "2dffc5c630d3a9c469d6cdc848ef212b",
                    locationId: 780051,
                    locationName: "Defeat Ghost (Lady)"
                ),

                new(
                    "Flykeeper",
                    "9d5428b910457d34f88e4154ec99a00f",
                    locationId: 780052,
                    locationName: "Defeat Flykeeper"
                ),

                new(
                    "Heavy Legless Zombie",
                    "6e7007764274d6d4b87483dc841ced27",
                    locationId: 780053,
                    locationName: "Defeat Heavy Legless Zombie"
                ),

                new(
                    "Legless Zombie",
                    "0501c3dc2f5b2e046a9dd80cb2c4b391",
                    locationId: 780054,
                    locationName: "Defeat Legless Zombie"
                ),

                new(
                    "Little Wretch",
                    "b289a505ec24f3c4ab4e4547b903b1ce",
                    locationId: 780055,
                    locationName: "Defeat Little Wretch"
                ),

                new(
                    "Lost Horse",
                    "e5b89d084be8c254bb5f58b313dd04f3",
                    locationId: 780056,
                    locationName: "Defeat Lost Horse"
                ),

                new(
                    "Mad Witch",
                    "f51a8a96f22b1f14da86621f2af8557f",
                    locationId: 780057,
                    locationName: "Defeat Mad Witch"
                ),

                new(
                    "Giant Zombie",
                    "bff0f9b7bc6b94141a515b363288c862",
                    locationId: 780058,
                    locationName: "Defeat Giant Zombie"
                ),

                new(
                    "Possessed Chest",
                    "f662ad06ff770dd40b31ac1dc1021c80",
                    locationId: 780059,
                    locationName: "Defeat Possessed Chest"
                ),

                new(
                    "Mudman",
                    "cebedaded89126b4689300748b8e9352",
                    locationId: 780060,
                    locationName: "Defeat Mudman"
                ),

                new(
                    "Necromancer",
                    "a58d6b75877c88449b6bf157fe48e2a8",
                    locationId: 780061,
                    locationName: "Defeat Necromancer"
                ),

                new(
                    "Caged Ghoul",
                    "84af05c8fba24ec48b13d51c48e6c622",
                    locationId: 780062,
                    locationName: "Defeat Caged Ghoul"
                ),

                new(
                    "Peter Mostyn",
                    "76383b16240aed2418e13f5026182a41",
                    locationId: 780063,
                    locationName: "Defeat Peter Mostyn"
                ),

                new(
                    "Possessed Painting",
                    "08f525c2822ba7342b486268c5f0674d",
                    locationId: 780064,
                    locationName: "Defeat Possessed Painting"
                ),

                new(
                    "Ghost (Vicar)",
                    "f0af7c881428567488d429da4b6fc031",
                    locationId: 780065,
                    locationName: "Defeat Ghost (Vicar)"
                ),

                new(
                    "Maid (Charlotte)",
                    "b26cb483759eba041a6ef86ac0576be6",
                    locationId: 780066,
                    locationName: "Defeat Maid (Charlotte)"
                ),

                new(
                    "Rival Witch (Violent)",
                    "7c01257de99339241b6bdb8a3ab43ff0",
                    locationId: 780067,
                    locationName: "Defeat Rival Witch (Violent)"
                ),

                new(
                    "Rival Witch (Weird)",
                    "0bd547a08fa628341ad0e0751414993e",
                    locationId: 780068,
                    locationName: "Defeat Rival Witch (Weird)"
                ),

                new(
                    "Rogue Ghoul",
                    "6eb3e208d8549f94bb0d29f81b620a40",
                    locationId: 780069,
                    locationName: "Defeat Rogue Ghoul"
                ),

                new(
                    "Rotted Initiate",
                    "ed0b7fe12a0a2784c9c6f305e9cb5bfa",
                    locationId: 780070,
                    locationName: "Defeat Rotted Initiate"
                ),

                new(
                    "Beast Zombie (Cholera Patient)",
                    "913f827e89118764aa6bf0cc4b8a07fd",
                    locationId: 780071,
                    locationName: "Defeat Beast Zombie (Cholera Patient)"
                ),

                new(
                    "Necrotic Beast Zombie",
                    "91647998debdcce4fa3fcc49b975992e",
                    locationId: 780072,
                    locationName: "Defeat Necrotic Beast Zombie"
                ),

                new(
                    "Zombie (Cholera Patient)",
                    "1d5c87a52f939c743a962820f9a47a68",
                    locationId: 780073,
                    locationName: "Defeat Zombie (Cholera Patient)"
                ),

                new(
                    "Bloody Man",
                    "ee9e7f820924e0342946b0c9fbf7ccfb",
                    locationId: 780074,
                    locationName: "Defeat Bloody Man"
                ),

                new(
                    "Skinned Witch",
                    "15eaed93fa33c9046a0ac5ac8d3b2021",
                    locationId: 780075,
                    locationName: "Defeat Skinned Witch"
                ),

                new(
                    "Giant Maid (Tara)",
                    "996ab4052345eca42803e859bd5dc301",
                    locationId: 780076,
                    locationName: "Defeat Giant Maid (Tara)"
                ),

                new(
                    "Sage Armor",
                    "a0bdfb3209a15d24e910762ea54de05f",
                    locationId: 780077,
                    locationName: "Defeat Sage Armor"
                ),

                new(
                    "Curse Sentinel",
                    "b21410dc684f48f4bb9bc9d46bc3b80e",
                    locationId: 780078,
                    locationName: "Defeat Curse Sentinel"
                ),

                new(
                    "Upper Initiate",
                    "074a4ef550eaf654e9ec0b54c8898273",
                    locationId: 780079,
                    locationName: "Defeat Upper Initiate"
                ),

                new(
                    "Valley Zombie",
                    "f6b7fc8d2587ea64da56163d0dda4fce",
                    locationId: 780080,
                    locationName: "Defeat Valley Zombie"
                ),

                new(
                    "Ghost (Soldier)",
                    "81b6d0404876ddc48a13ff0d9cf45d3e",
                    locationId: 780081,
                    locationName: "Defeat Ghost (Soldier)"
                ),

                new(
                    "Jailkeeper Zombie",
                    "3e4aa7974087dab4b96461c034b5691d",
                    locationId: 780082,
                    locationName: "Defeat Jailkeeper Zombie"
                ),

                new(
                    "King's Eye",
                    "8b3d23e175ee01c4485ebdc57e1af169",
                    locationId: 780083,
                    locationName: "Defeat King's Eye"
                ),

                new(
                    "Grenadier Zombie",
                    "deee637d0db484d4086717713075bb6c",
                    locationId: 780084,
                    locationName: "Defeat Grenadier Zombie"
                ),

                new(
                    "Labyrinth Knight",
                    "f12782c55d1397445860bc6891e9093a",
                    locationId: 780085,
                    locationName: "Defeat Labyrinth Knight"
                ),

                new(
                    "Nurse Zombie",
                    "454ff6a949cd4c44783b2eac79c4bf8b",
                    locationId: 780086,
                    locationName: "Defeat Nurse Zombie"
                ),

                new(
                    "Soldier Zombie",
                    "f6919623e04f40a46ab39cf8b3263dcd",
                    locationId: 780087,
                    locationName: "Defeat Soldier Zombie"
                ),

                new(
                    "Flamethrower Zombie",
                    "0c1a24d5a3b844f43b7dba45431eb29b",
                    locationId: 780088,
                    locationName: "Defeat Flamethrower Zombie"
                ),

                new(
                    "Emma",
                    "690ab4af318eed341ae39472a7d9c575",
                    locationId: 780089,
                    locationName: "Defeat Emma"
                ),

            };


        public static MonsterLocationData? ByGuid(string guid)
        {
            return Locations.FirstOrDefault(
                x => string.Equals(
                    x.Guid,
                    guid,
                    StringComparison.OrdinalIgnoreCase
                )
            );
        }


        public static IReadOnlyList<MonsterLocationData> All()
        {
            return Locations;
        }
    }
}