using System;
using System.Collections.Generic;
using System.Linq;

namespace WitheringRoomsArchipelago
{
    public sealed class RandomizedItemData
    {
        public string Name { get; }
        public string Guid { get; }

        public long ItemId { get; }
        public long? LocationId { get; }

        public bool CreatesLocation { get; }
        public bool IncludeInPool { get; }
        public bool RepeatableFiller { get; }

        public string? LocationNameOverride { get; }

        

        public string? LocationName
        {
            get
            {
                if (!CreatesLocation)
                    return null;

                if (!string.IsNullOrWhiteSpace(LocationNameOverride))
                    return LocationNameOverride;

                return $"Discover {Name}";
            }
        }

        public RandomizedItemData(
            string name,
            string guid,
            int key,
            bool createsLocation,
            bool includeInPool,
            bool repeatableFiller,
            string? locationNameOverride = null)
        {
            Name = name;
            Guid = guid;

            ItemId = ItemData.ItemIdBase + key;

            LocationId = createsLocation
                ? ItemData.LocationIdBase + key
                : null;

            CreatesLocation = createsLocation;
            IncludeInPool = includeInPool;
            RepeatableFiller = repeatableFiller;

            LocationNameOverride = locationNameOverride;
        }
    }

    public sealed class MultiDiscoveryLocationData
    {
        public int Ordinal { get; }
        public long LocationId { get; }
        public string LocationName { get; }

        public MultiDiscoveryLocationData(
            int ordinal,
            long locationId,
            string locationName)
        {
            Ordinal = ordinal;
            LocationId = locationId;
            LocationName = locationName;
        }
    }


    public static class ItemData
    {
        public const long ItemIdBase = 777000;
        public const long LocationIdBase = 778000;

        public const long MultiDiscoveryLocationIdBase = 782000;

        public static readonly Dictionary<string, int> MultiDiscoveryCounts =
        new()
        {
            ["Remembrance Tear"] = 12,
            ["Coin Purse"] = 5,
            ["Trickster Medal"] = 20,
        };


        public static readonly List<RandomizedItemData> Items = new()
        {


            // AUTO-GENERATED FROM items.csv
            // Paste into ItemData.Items.

            new(
                "Summoning Knife",
                "0e04d0decb256ab4795982a2599d74af",
                key: 1,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "League Curse Charm",
                "2a2211cb592eb4f46adf02b89923d207",
                key: 2,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "League Damage Charm",
                "d9489a3d89733bf4d88fcbfc920c78e6",
                key: 3,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "League Health Charm",
                "01a75de9242f2cf4992146c0819c4646",
                key: 4,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Curse Charm",
                "71d89d193c1ad1c448b3fcd00f3111ca",
                key: 5,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Health Charm",
                "e795e043a9a21114b85f5aa41c71fc47",
                key: 6,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Luck Charm",
                "25e43572613c0f24f86aa54206689023",
                key: 7,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Melee Charm",
                "7bcb2e388ae33924aa1b49b9e1c64db7",
                key: 8,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Poise Charm",
                "1c46cf82eeb80ac47bce9adcb1d47d00",
                key: 9,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Projectile Charm",
                "58c1aafd008b9cb41b7504d6eee00418",
                key: 10,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Resistance Charm",
                "bd10ce589c7f940449bbbb2f19256ff0",
                key: 11,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Speed Charm",
                "046b5a2e113ca2a4d889aab7be385119",
                key: 12,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Spell Charm",
                "94bffe933b362df4eae5c205b0062f3c",
                key: 13,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Rotted Charm",
                "f51c239fa04079b4b8e4e8da3b85baea",
                key: 14,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Onyx Pentagram",
                "ef1ca913f74daba46908e1d47ab43a05",
                key: 15,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Pentagram of Blood",
                "c383b118070ce754d97e3e84e3df5764",
                key: 16,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Mossy Pentagram",
                "12d62d0b3c5982047981a08d0d09a791",
                key: 17,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Pentagram of Flesh",
                "2deb4d86a1472b447b6ab89d0330d1a6",
                key: 18,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Lucky Necklace",
                "8ae1dec96d0d879479eb8c8094afa000",
                key: 19,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Gatehouse Spawn Room Discovery 1"
            ),

            new(
                "Golden Pentagram",
                "ad8945e928ea32e4780f4e57fdbb0c1a",
                key: 20,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Night Mother Amulet",
                "433fe53f4d1bdb7409a326f931b69d9e",
                key: 21,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Vampire Locket",
                "8808cc2488f904e44b4b238166daf190",
                key: 22,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Holy Pentagram",
                "989d011c3256c3e4a91e1a8ed56fee0f",
                key: 23,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Befouled Head",
                "7da9c50c25298e346a44de60ae7e0522",
                key: 24,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Small Cursed Snuffbox",
                "01c257fb0c675414c846b476e9ac2c72",
                key: 25,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Flight Codex",
                "59fb117e3994e8d4aa4ff0ad6899b19a",
                key: 26,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Margaret's Room Discovery 1"
            ),

            new(
                "Evasion Codex",
                "e91eac773ae06e5458006e76a21c819a",
                key: 27,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Inverted Gaze",
                "6ef7d3ab460c93546b910c170cb861fd",
                key: 28,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Lantern Familiar",
                "60d43b62eb51c0742a214af0cf637a63",
                key: 29,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Nightingale Doll",
                "f9019d4ac6632594dbde26aa83fd1e4e",
                key: 30,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Closed Gaze",
                "96b9f19cab7209e4ca88988c57ebcc56",
                key: 31,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Troy's Head",
                "0b05f1e0a046c4b45be8e76b9eff4b47",
                key: 32,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Perception Codex",
                "2d6db4bbf9b26bc42babc8cd226a8fa2",
                key: 33,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Guard Codex",
                "14336fc233369364fbdfc10dc67febf1",
                key: 34,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Large Cursed Snuffbox",
                "0fc1524f9fed7f442bffe1dc6567f105",
                key: 35,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Telescope Puzzle"
            ),

            new(
                "Second Chance Brooch",
                "a0588e090fc1eff418b9c93333181c9e",
                key: 36,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Pale Skull Ring",
                "b6ace7e7405386b4d937c6cc6e0c49bd",
                key: 37,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Ruffian Ring",
                "341da601c264c6d48be9a2b516e0d8c5",
                key: 38,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bloody Ring",
                "d35be4124e19204469a1b0cdd239b0f6",
                key: 39,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Gold Skull Ring",
                "142bc863c43e9df46af16e6fea0bbbd0",
                key: 40,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Shield Ring",
                "0db4a05a319ce0643bf659725e4d2f04",
                key: 41,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Knight's Ring",
                "74ab7bb3e55ede047b7a3c9e25da220a",
                key: 42,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Silver Skull Ring",
                "09b7663c4b6a684409837008cdfcc599",
                key: 43,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Hunter's Ring",
                "ce1632889288be1409f9108c2f0acec8",
                key: 44,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Barrel Ring",
                "20e816b0bbd55f14a94dd00273e3a23a",
                key: 45,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Skull Ring",
                "6f53473a95403234ea41c1f0d35af8c9",
                key: 46,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Gold Hunter's Ring",
                "acbf0d352592c99478d54c5c3cce29bd",
                key: 47,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Pale Hunter's Ring",
                "798061183fb5eaa499bce7c71359cec5",
                key: 48,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Critical Ring",
                "7dab139074ea1c24b91545b049d1cc6e",
                key: 49,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Savior Ring",
                "dea8b9964f515c54694e925fedd4648a",
                key: 50,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Phantom's Ring",
                "4e9ca3ddfbc1a6c4b81dac845f1af4e4",
                key: 51,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Rogue's Ring",
                "4e6e655adf6ec86499975f2f2198050c",
                key: 52,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Silver Bear Ring",
                "09cbdf2bbea191f41a18af1f391377e6",
                key: 53,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Covetous Ring",
                "126300cf3aed8734692c001c1e3d6ba6",
                key: 54,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Flesh Ring",
                "91e9f0cfefa583043bdddad702b65bd7",
                key: 55,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cursed Flesh Ring",
                "27943397c48af344f83d8c49d237d8b5",
                key: 56,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Gold Bear Ring",
                "9fb3ae2a81bd94d41adeda9365a2d946",
                key: 57,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Swift Ring",
                "08aeda98faea32844a7bd82a812612a2",
                key: 58,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Black Cross Ring",
                "14364140285554e41a426a2bc8a7349d",
                key: 59,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Burnt Ring",
                "65d63c4cf13a78f479e6197fba55a402",
                key: 60,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Curse Ward Ring",
                "a0c9f327863af73469175e3912001fbe",
                key: 61,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Frog's Eye Ring",
                "13eb73037dd9591408e418e9995b42eb",
                key: 62,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Red Life Ring",
                "30ff0e013fb8f214c8e9d900b9acc6c5",
                key: 63,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Castle Ring",
                "57aa29d44213ed44283b9156672f031a",
                key: 64,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Chromatic Ring",
                "2c7242b0de56dce4db9135d4b14bf3e4",
                key: 65,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cursed Explorer Ring",
                "57fc32a6bee324c4d8d541762497e92c",
                key: 66,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Rabbit's Heart Ring",
                "4f400f0ba0deacb408af5e88179a26e3",
                key: 67,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Fortress Ring",
                "faa9d44be7f33b144ace21c99f7ba6db",
                key: 68,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Gold Cross Ring",
                "6e91c70a30623b54389fddb3cf7b9fea",
                key: 69,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Necromancer's Ring",
                "64e3974b59e4a1c4faab7dd2b64c5a97",
                key: 70,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cursed Balance Ring",
                "6fa0aeedc050a914d8afbcb4158f0547",
                key: 71,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Necrotic Ring",
                "3ad34c4642d98e74bbe4813e186f7801",
                key: 72,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Ruby Ring",
                "e54b3cd031d54b44da72f232a4f39a49",
                key: 73,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Candle Ring",
                "7b69231edf687374a9992e61f513dac4",
                key: 74,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Margaret's Ring",
                "551418bd6e28dfe4e8c8c2271fc1c9af",
                key: 75,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Moonless Formless Ring",
                "9a7e21290e58fa74a90ef7bc0baa509b",
                key: 76,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Night Mother's Ring",
                "86d4b1848368c374e89b532fee9a3025",
                key: 77,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Gatehouse Spawn Room Discovery 2"
            ),

            new(
                "Priscilla's Ring",
                "7033b6a58da552340990c7297e7b91e6",
                key: 78,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Crescent Ring",
                "58a972b8a42925b49a2ace91fc8fea29",
                key: 79,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Dull Silver Ring",
                "ed54e01f28a1c1641a7fcf2a2f723dd1",
                key: 80,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Exquisite Gold Ring",
                "1422c4d8a5b6d08489268c08697e1d2b",
                key: 81,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Moon Ring",
                "dd4a15240a318fe49af3628624ace294",
                key: 82,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Eclipse Ring",
                "76f3fd53931084645a290a9a2e2cd6d3",
                key: 83,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Exquisite Silver Ring",
                "d2c8d21f4d52153428cce0cb041ac03c",
                key: 84,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bleeding Resistance Syringe",
                "8767d7f98fff58e48b26795c7b3a6e80",
                key: 85,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Violent Pill",
                "c5bc9010a0840434aac8255aca3e9c93",
                key: 86,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Paralysis Resistance Syringe",
                "8b1a2036541d9694d81066ee3b2d8a0a",
                key: 87,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Poison Resist Syringe",
                "cc865d9d6a8ee614b9913075a40b219d",
                key: 88,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Dexterous Pill",
                "c8e00a67017619b47acc9a47a3f42ee7",
                key: 89,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Weird Pill",
                "7a78d8011dd676342acde48b0963a287",
                key: 90,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Bandage",
                "c7e6298e40db6d94dab7f5ec80a6f0e8",
                key: 91,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Chocolate Cake",
                "fef9ef4284ef5bb4e9d89a8d306ab1a1",
                key: 92,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Warding Cupcake",
                "3d2ab4aad625c3b46b950b2665a358eb",
                key: 93,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "First Aid Kit",
                "7a4cab3f8e1c6624da413261a9bd290c",
                key: 94,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Hearty Roll",
                "a91aa55236bb565478172704564e9cdd",
                key: 95,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Poison Antidote",
                "abffc4a58c4fae147ad9fe85f175d171",
                key: 96,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Rarebit",
                "f4ae4bd0aaf82df459bc171585ec6e83",
                key: 97,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Ration",
                "b679a2259eefe4d44a3282e3ebfd9cf6",
                key: 98,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Corrupted Meat",
                "9e2e28bd9e5281c4cbccba0061910596",
                key: 99,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Scone",
                "582cc66a03491ed47bbb32d479838386",
                key: 100,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Cup of Tea",
                "940fc8d340ab90b4da5dc01ce22a45eb",
                key: 101,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Warding Candle",
                "a646287c4ba6736448200b4a75354b40",
                key: 102,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Acid Jar",
                "ecf6c16102bb3a941ac30ec0bbd40b9f",
                key: 103,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Ambrosia Jar",
                "15b82143a57adb0478a1434d097643e2",
                key: 104,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Blood Jar",
                "ff0b6f3451c69cd4796ab357c46f32f1",
                key: 105,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Curse Jar",
                "b4046e382f38d0d42a4cfb40800177a4",
                key: 106,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Elixir Jar",
                "f14e9abb553881c489fe4cdf127c5a98",
                key: 107,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Empty Jar",
                "52c4921fd0b2cd54dad42508980c4b6f",
                key: 108,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Incendiary Jar",
                "634e8e686bca7db4b83719aa4a1b2da1",
                key: 109,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Nail Trap",
                "57b4d571462d4e146a91227d23e83ea9",
                key: 110,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Paralysis Jar",
                "6190eab4ecd123c4ea8560781f5ef8dd",
                key: 111,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Paralysis Trap",
                "815640289a7d8cd46830de28535bee53",
                key: 112,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Poison Jar",
                "b620eea25af75294c8242c08c2f53da2",
                key: 113,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Tonic Jar",
                "cb650a4c26b9d4d4ea42335bae1251f3",
                key: 114,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Firearm License",
                "5d53c67b32d570249895dae308eb8240",
                key: 115,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Skull Key",
                "316410550ebed8d4fb69a1c7d7178e03",
                key: 116,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Advanced Wretch Pass",
                "c297e118df2e4ba4baae0be5ebe38b35",
                key: 117,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Labyrinth Market Key",
                "188968d0ea9663d47955f99067ec038c",
                key: 118,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Basic Wretch Pass",
                "30b2245239a786a4aadc7db1734aae90",
                key: 119,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Hotel Elevator Key",
                "314dd217f10573341a94d5250f5ab312",
                key: 120,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Jailer's Elevator Key",
                "c985949f08d9bc343b76b323ee15eeeb",
                key: 121,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Robert's Elevator Key",
                "37fd582c701a9044e98af2224929c3be",
                key: 122,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Robert's Backroom Discovery 1"
            ),

            new(
                "Cholera Clinic Cage Key",
                "bbe3f26cf697f7448b751d972a395a50",
                key: 123,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "St. Elli's Key",
                "8bf163e5226ded24fb4d045f72269670",
                key: 124,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Rusty Cage Key",
                "af9415dadb6404848bbcc2551cd39bfe",
                key: 125,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Dining Hall Invitation",
                "da59fd69a765c5847b883f4e62f22eb0",
                key: 126,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Door Handle",
                "c60a0b65f2b0f9541acb2107a42c888f",
                key: 127,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Blackett Attic Storage Discovery 1"
            ),

            new(
                "East Stairwell Key",
                "87e09fe50faa54b4f9528cd20c8443c7",
                key: 128,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Eviction Letter",
                "f584f391c3b350240825fe08b42acb28",
                key: 129,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Right Idol Eye",
                "8733011378a78854db88c16530c251d2",
                key: 130,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Entrance Hall Binding Spell",
                "5cc588540a9aeeb468c8a649d55edaf1",
                key: 131,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Entrance Hall Spell Key",
                "10b131bf509812840a3b9404e52de4f8",
                key: 132,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Entrance Hall Key",
                "402350cae0fee8a409fd210d06ca1e66",
                key: 133,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Front Door Key",
                "2107c183c60da5946a5aad3f5f11911d",
                key: 134,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Gatehouse Key",
                "d8bcf2190bd1fa8469531e588da16ec4",
                key: 135,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Dafydd's Back"
            ),

            new(
                "Grandfather Clock Key",
                "aad7d8862b70d974e9244f356b02723a",
                key: 136,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Night Mother's Disciple Book",
                "066d50b0c15bd8b499268c341734333f",
                key: 137,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Observatory Key",
                "3e32df5309d218d4badf215e14aae538",
                key: 138,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Occult Library Key",
                "f6debaee10c350b40be4f5ead88cc771",
                key: 139,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Murder Algebra Puzzle"
            ),

            new(
                "Puzzle Oracle",
                "7bca4e9f589e32e45867bff6f54a59fe",
                key: 140,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Electrical Generator",
                "6905aa76b72504c4e8a0f57ed0642dcc",
                key: 141,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Blackett House Key",
                "34f5ef0ccedf7124fb11fe6a1cb7a837",
                key: 142,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Crumbling Interior Key",
                "550896c3724cf264995161f8da758336",
                key: 143,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Waking Powder",
                "987bdb8909818444ba3dc62c818dcbef",
                key: 144,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Wretch Teleportation Spell",
                "cc51367a57d288346b0f539c82f1cfea",
                key: 145,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Blue Secret Passage Key",
                "03a8a5f9c95cc3c40ba523067f35873c",
                key: 146,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Skin Covered Key",
                "ffa6d4c13eefba543bddd6c586cbe455",
                key: 147,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Stairwell Spell Key",
                "ef8564d0bf51db84ebc43aa167f884bf",
                key: 148,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Strange Bedroom Key",
                "4bbd68b091bea824996669c33defd7d3",
                key: 149,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Ancient Rite: Outfit",
                "046f996923a576f45a0acf82ce326caa",
                key: 150,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Ancient Rite: Spell",
                "f60e6c930e98fd240b1cc815179f5725",
                key: 151,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Ancient Rite: Weapon",
                "6d5d687895d4ff5468b42869dbc73681",
                key: 152,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Vicar's Card",
                "54a4f51bb919d3e49880be433a0fbe86",
                key: 153,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Comforting Bear",
                "8fe96a9b54ea47b4ea30deab632e7f12",
                key: 154,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bible",
                "3b028c4621fe2a140ac7ace0bbc2d47b",
                key: 155,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Spiked Coffin Shield",
                "f96a8936bb45f8941817da614e040ad7",
                key: 156,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Corpse Hand",
                "c8b0990dfb4ad3643968cb4b034d42d1",
                key: 157,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Metal Shield",
                "b9021b31e821f80468dd2ce5155d71f4",
                key: 158,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Mirror Shield",
                "026eb2a8927e1ea49913a53ae834c134",
                key: 159,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Night Mother's Doll",
                "d8f28726c8b6afa49a05e294ca16bc48",
                key: 160,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Oil Lamp",
                "54dfce1cf6668c848923637d128c3231",
                key: 161,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Old Shield",
                "8b76efccd3ec9444985ef1176447b377",
                key: 162,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Spirit Dust Bag",
                "8ee76ea5098a41942b7c6500041ec290",
                key: 163,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Curious Statue",
                "c41a7316af66b7a4da711efd90b6e07d",
                key: 164,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Brass Telescope",
                "eb31b33403cd3204fb3a2bf70cfd5a03",
                key: 165,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Thurible",
                "90d521f87970d4a42bf18e71ba33e220",
                key: 166,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Old Wooden Shield",
                "652d4b219d3ff5942bd9a701b3c204b2",
                key: 167,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bee's Fashion Record",
                "7f74fc11c391c6043a7ba5e21820e80e",
                key: 168,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Margaret's Room Discovery 2"
            ),

            new(
                "Death's Fashion Record",
                "14cf4a4f18d1401469af8a903fd5ce62",
                key: 169,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Goat's Fashion Record",
                "7b94730ee46fdca4ca9e636f1162a334",
                key: 170,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Raven's Fashion Record",
                "0b98020ed2fac514381969f369ec25a2",
                key: 171,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Spider's Fashion Record",
                "6966d578331355e4cb6bb7570b15d9bf",
                key: 172,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Hardened Flesh",
                "5a2ff71cb3fb2a3478d6479139b91fe1",
                key: 173,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Starry Flamethrower",
                "51fae8b74f219ac43a5e2ac3eba8f00f",
                key: 174,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Starry Flesh",
                "2bc8159c6a197cd4482d36219fe9ad91",
                key: 175,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Starry Greatsword",
                "981faefdbfeddba49a106ee8a6a8075c",
                key: 176,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Alice Dress",
                "87cf811ba78769a4d82179f0b2b5f8e1",
                key: 177,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Golden Armor",
                "f5dbe7a0998459040a0fe5773e0dd501",
                key: 178,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bloody Apron",
                "fabbf27d95f34ca409a9ecb2cff1e9f3",
                key: 179,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bloody Dress",
                "d1aff8bdde88ef84fb0d75dbf79fed86",
                key: 180,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Blood Tower Second Floor Discovery 1"
            ),

            new(
                "Clown Suit",
                "e978f8f5be6b28a48afd631adcc1f697",
                key: 181,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cursed Armor",
                "a6e91642e12ce244fb3d9c1da1f171db",
                key: 182,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Doll Dress",
                "0ca5b55fb7b4a8d4aa1a70f62fcf492d",
                key: 183,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "British Army Uniform",
                "e3183a94f8c0be640a26e9ac817f129a",
                key: 184,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Elegant Dress",
                "0b8d68c17ff50c34dbcad1fad07dd985",
                key: 185,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Study Room Discovery 1"
            ),

            new(
                "Gentleman's Suit",
                "ccb141df6326b124a832e16680f34b6a",
                key: 186,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bloody Nightgown",
                "b0251c882a603fa439df50c74d33b644",
                key: 187,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Murderess Coat",
                "3bebcd48f42a8404c87b52a02c247f74",
                key: 188,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Crazy Butcher Purchase 1"
            ),

            new(
                "Green Cloak",
                "ef3b9a35fd64f764a8b4535930c0fd76",
                key: 189,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Nurse Uniform",
                "ed18eac8bab2f9f4eb819515ec2fe5e0",
                key: 190,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Floral Dress",
                "569a17e0fb4304547b28129cefcabec6",
                key: 191,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Phantom Threads",
                "21a84ce0d80fa7f4ba2198aa8af02bf8",
                key: 192,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Prismatic Dress",
                "42f9b451ae46aea44b3fe44c57b85664",
                key: 193,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Adventurer's Outfit",
                "cdff62907f5f52d49bf694673828b1b3",
                key: 194,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Ancient Labyrinth Discovery 1"
            ),

            new(
                "Rust Cloak",
                "08b790e3e82466947917524ab7dad475",
                key: 195,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Dirty Initiate Dress",
                "ca2ccd4d435e01c4394e1d526a207ba0",
                key: 196,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Knight's Armor",
                "36395ead2d7fa13409c8e1e25fbc3551",
                key: 197,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Starry Dress",
                "5f3ee41f0af26814cae3d67e55bb042a",
                key: 198,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Merry Band Cloak",
                "e509548d1570e9840b07b358ba0053f6",
                key: 199,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Unlucky Dress",
                "6ad2cca56804a434092eff8040c3a103",
                key: 200,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Initiate Dress",
                "0a61e772e5e6b77488778ffaaada65f7",
                key: 201,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Christmas Ghost Robe",
                "3a05b52ecf94e544eb834123aef2ac1b",
                key: 202,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cowboy Hat",
                "af25d57e28901d444a111e45b7ff83a6",
                key: 203,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Ancient Labyrinth Discovery 2"
            ),

            new(
                "Alice Wig",
                "0834dc79a89d3d84bad6c4f838e089e8",
                key: 204,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Golden Helmet",
                "3e2b5072503b56b4e82c2965d2b46756",
                key: 205,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bandages",
                "40c55dbaef3b48b4785f59d52349c34e",
                key: 206,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bell Helmet",
                "c27ab3a77e40ae5428e36c828dc51380",
                key: 207,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Chapter 3 Discovery 1"
            ),

            new(
                "Big Initiate Hat",
                "9e28501524ddf564789d3a7eca365008",
                key: 208,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Blindfold",
                "179c764b6836f68408da14695ad113d0",
                key: 209,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cat Ears",
                "3a66a7f814ec95d4f8497dce1687d8af",
                key: 210,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Fool's Cap",
                "2dc125d2c8a228345b78fb3954cabd52",
                key: 211,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cursed Helmet",
                "fbf444b0156003c4fbeb5448cfa0d630",
                key: 212,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Doll Bonnet",
                "5b5cd139986a03848ae784fd7709fa3d",
                key: 213,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Edgar's Bandage",
                "a7e199b01d4235e43a9f3a39e0a9b79d",
                key: 214,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Flaming Hood",
                "477990728a1e3d94eb5361cb7a61930e",
                key: 215,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Chapter 3 Discovery 2"
            ),

            new(
                "Spectacles",
                "946d14b6511086f47b4a5fdcf7743ee7",
                key: 216,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Head Lamp",
                "b8dac5dc4ca79fc4593cdadd78a65b32",
                key: 217,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Jailkeeper Head",
                "61cb87c0e9bba9c4a9d142d814f6ff79",
                key: 218,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Medusa Head",
                "56b3c28277ae0b34d87eb7a60a3d20df",
                key: 219,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Ancient Labyrinth Discovery 3"
            ),

            new(
                "Necromancer Helm",
                "65f998181464ac8449331aa963d8a1dd",
                key: 220,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Ancient Labyrinth Discovery 4"
            ),

            new(
                "Night Mother's Mask",
                "0b76c903c8aec0c4387b4fc35ec1d004",
                key: 221,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Nurse's Hat",
                "d7098d1155e74c04b9294bd83862f96c",
                key: 222,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Pumpkin",
                "304a8751bdf8a7b4d930d6ab4505601d",
                key: 223,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Crown",
                "ca4f56f18c855714c92abfbbddc376fe",
                key: 224,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Masked Man Purchase (Flipped World)"
            ),

            new(
                "Sack",
                "0b3ba885adefe464289c0ea2a127c1f5",
                key: 225,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Short Cloth",
                "984d3a60693e8dd42ab0f23d609ef04b",
                key: 226,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "French Pins",
                "9b6d893a61597ff4da65999be1fca289",
                key: 227,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Skin Mask",
                "0d04a8bd13c56974d834b4d32f17bb42",
                key: 228,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Knight's Helm",
                "d0f86ec0f4b176c49a83eb5b8d5b1bf3",
                key: 229,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Starry Head Sack",
                "a3cdae23298e71644850ac3715e15667",
                key: 230,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Top Hat",
                "0e882fa9d2e8b9e4da453c218b8f4c28",
                key: 231,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Merry Band Mask",
                "75184a2b8abafe844981befe56840ffc",
                key: 232,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Tricorne Hat",
                "1960eab6d9bb64e4e991bbe4be30c867",
                key: 233,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Punishment Cage",
                "4a1c7538c6c12ec43b3b906fa369b7d9",
                key: 234,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Hairpin",
                "8c5212805f28edb41bcb9161766a1f2a",
                key: 235,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Mourning Veil",
                "ece19e2b2d8b9144ea3c74dbbf9f7074",
                key: 236,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Vicar Helmet",
                "2760676f16c305340be97437a0abaed4",
                key: 237,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Initiate Hat",
                "43dc9b2f464420f46ba40107e6668d09",
                key: 238,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Big Wretch Hat",
                "655db955a5315b84689147e381753d04",
                key: 239,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Zombie Outfit",
                "f41e3c91c85bbb04abefab003ea629a8",
                key: 240,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Night Mother Outfit",
                "75a4b6d9476d8cf499a4a5c94a717667",
                key: 241,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Gambler's Mystery Sack",
                "1ef2d6183ad9bfe42aee0e49fabc81e1",
                key: 242,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Gold Hagsack",
                "54b3138efb2ca8944897e185599eda5e",
                key: 243,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Healing Hagsack",
                "dd7af67e9d985b845838df7deac34f52",
                key: 244,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Jar Sack",
                "b3161f8a01cec7a4ba7d0538832e0b0c",
                key: 245,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Warrior's Mystery Sack",
                "da6b9d44cc5142a48bcd817e07e0e3eb",
                key: 246,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Melee Hagsack",
                "1a7a431d777890a48965b4f5d65fad38",
                key: 247,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Occult Mystery Hagsack",
                "49769bfdb46dfd642b8e2d693a45df12",
                key: 248,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Spell Hagsack",
                "818f26a205f650b4bafdbc5325cc70bd",
                key: 249,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "War Hagsack",
                "bb8bf5d7ad5358a45889fb027ddbd461",
                key: 250,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Baleful Influence Book",
                "9e902d9b855607a47954a7fd935d3b7f",
                key: 251,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Burning Protection Book",
                "4141f43b326bd7045857a525c5a48b55",
                key: 252,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Possession Book",
                "e0ec740b07d03e549aca1fa3da50fef6",
                key: 253,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Summon Spears Book",
                "435100b9ff8e2ad4092adc05f5bcc10b",
                key: 254,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Fireball Book",
                "c726a7c972edc9440abf99192a25a2b0",
                key: 255,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Corpse Hex Book",
                "6b5e1b03dacee154a9dc5fdd26038ad5",
                key: 256,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Curse Form Book",
                "dcca2d3651d08d0428e7345dfb73cac9",
                key: 257,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Healing Barrier Book",
                "ce72fb8e06364be4b8269c3006cd5d1e",
                key: 258,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Annihilation Spell",
                "deced5ca707efb64f826bbbd377a4133",
                key: 259,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Armor Spell",
                "afbd1acf76ff6394889507767e07b5eb",
                key: 260,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Enchant Spell",
                "3092fe4b0ce674f4daeafb27d3006b82",
                key: 261,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Harvest Field Spell",
                "851c27c2434e79a43b76ddc2c47e9d95",
                key: 262,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Curse Ball Spell",
                "fec85b062f6ead548932cb61702b0092",
                key: 263,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Door Hex Spell",
                "ef922bfde6d67f943ab83ea49c67df09",
                key: 264,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Curse Orbs Scroll",
                "b809c204e964ef846a743114cc8277b4",
                key: 265,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Dummy Spell",
                "85060d6e5d309b343b0778e7a5dd6db6",
                key: 266,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Advanced Grimoire",
                "ae8cc38c59d51ce46907a9023be2591e",
                key: 267,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Basic Grimoire",
                "4f1c1a85edbe95448b48ebc13b09c192",
                key: 268,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Blank Scroll",
                "8f0cce130af86334ea0ef433acc30cd1",
                key: 269,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Boat Pass",
                "36b08b91f3e79de46b1fb30336857314",
                key: 270,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Boatman Purchase 1"
            ),

            new(
                "Bone Ash",
                "7bd63485952d3cd4583719ebd2dc05b0",
                key: 271,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Broken Shotgun",
                "b765e38b3dbdebe45a21dc56bc20e918",
                key: 272,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bronze Finger",
                "746ea404555deb444931cc560761f3cb",
                key: 273,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Duwern Burial Ground Map",
                "e464cd399717647499b553aa31aa6987",
                key: 274,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Circus Prize Ticket",
                "1f939494f405f8845a1dcbab622743ab",
                key: 275,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Circus Ticket",
                "ae08cf165d334b04cac9894e8b2e35f6",
                key: 276,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Coin Purse",
                "3fb5bc4d3132e63448a9d1a4b4c6f1fe",
                key: 277,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cursed Grimoire",
                "bae272b2e9131d94b96462db44711f91",
                key: 278,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "First Angel Kindling",
                "f98a2c3a72056164abc51339f8ff13a5",
                key: 279,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "First Angel Map",
                "3ea3dd9741566e04eb3b8c4ae0392542",
                key: 280,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Gun Powder",
                "308a18b849fe9614fb0a4dcc1a687174",
                key: 281,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Gunsmith Kit",
                "2bac89f17ee79f74fad33ed21329aedd",
                key: 282,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Blank Initiate Book",
                "508778659f929134e847a6cabb95e8fa",
                key: 283,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Initiate's Grimoire",
                "759336cc0f2cec04783c0017f2431ba7",
                key: 284,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Advanced Lab Manual",
                "d19d4c895ce08bc4784ddf6a29da2798",
                key: 285,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Organ Chamber Safe Puzzle"
            ),

            new(
                "Basic Lab Manual",
                "2a9a49cb74e54774ba5e2896442c9c4d",
                key: 286,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Grease Lab Manual",
                "d2566b829764a1848a9805cfb07c078a",
                key: 287,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Rakesh's Diary",
                "07df8bfde55c6204b89ae5191dd6606c",
                key: 288,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Mark of Sin",
                "5d12a53681878ce409410de626439d94",
                key: 289,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Medicinal Herbs",
                "c6ab33b7478837946b05f5b090d44e94",
                key: 290,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Ancient Blood",
                "6c09cb12358c3414a8e193e10409732e",
                key: 291,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Corrupted Finger",
                "55789e69d995cdc44868fa2b1feec995",
                key: 292,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Corrupted Heart",
                "77f2e623f1a919a4e92c3de6e5e163af",
                key: 293,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Corrupted Liver",
                "471f3bbfc41aea74785ce2edac15941c",
                key: 294,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Curse Sentinel Candle",
                "f4f3b18c79d58b1459d5a8440b0ac16b",
                key: 295,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Dream Essence",
                "2b5918a2f3a52fe49a8fbdab9982de51",
                key: 296,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Human Finger",
                "c8700e822fed1fe408f1d4a31cc40432",
                key: 297,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Nightingale Bones",
                "d0cfab7285c80d744970d4d5c89c4aa6",
                key: 298,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Spectral Remains",
                "c7fe77d9d3c1f5941a3e7cbd216e3800",
                key: 299,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Organ Grease",
                "3bb3995c1342a534caf40f8d1b3de11c",
                key: 300,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Witch Ashes",
                "213f03d748f2fad42929ea5ff2648fd2",
                key: 301,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Paralysis Leaf",
                "6f58f3e056b444045982b6d3a7cfbed2",
                key: 302,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Photographic Dry Plate",
                "b2e89246819a058469e2329f33870381",
                key: 303,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Photograph",
                "dbf4f375283de3942ac3a4417caca53e",
                key: 304,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Blood Stained Letter",
                "c214b613e3e0d344a9c42e30a0db3263",
                key: 305,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Idol Tainted Heart",
                "a475597e37db10e499f7ab5de31d1e31",
                key: 306,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Rose's Diary",
                "7b3eef4337dbaac44bdff846600aa71d",
                key: 307,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Poison Leaf",
                "e8882cbe92586aa40b24271877004063",
                key: 308,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Audio Command Wax Cylinder",
                "74b869c65c6799a4fb84127bb27b44ec",
                key: 309,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Remembrance Tear",
                "f9963d2cb930848499dde457be80671a",
                key: 310,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Scrap Metal",
                "faafdddb70ac08f44b65c99045bcd6ac",
                key: 311,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Starry Grimoire",
                "a6bf6212e624b6c44ae4ee96b24a3556",
                key: 312,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Starry Remembrance Tear",
                "95dc386e9ca92f947a2795e8e2f138b2",
                key: 313,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Strange Coin",
                "450742c721bfc3d41aa6c90c6763a7cc",
                key: 314,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Sulphuric Acid",
                "6ebbd5e16da5ff5489af837b4532fb1e",
                key: 315,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Trickster Medal",
                "52624890009918245b7befa41c239227",
                key: 316,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Village Token",
                "1aa44765b12fe3b49972aa689be2ff72",
                key: 317,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Black Wax",
                "21b8d6b67868ee44da6902118d83f64b",
                key: 318,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Blue Wax",
                "3675f6c3bcd496c43a20e07f015782d4",
                key: 319,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Green Wax",
                "3a7246809a1209b4c91a8e79b25de136",
                key: 320,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Orange Wax",
                "8719f901f02aceb40a85ac4f88e39c70",
                key: 321,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Purple Wax",
                "731af5d6590936f4e8d38cfd1dd67e4a",
                key: 322,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Red Wax",
                "d7fbf1c508dd12d44a9ccc67e8b937ec",
                key: 323,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "White Wax",
                "370a04a0e699b974b8673c93a6e7e7d9",
                key: 324,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Yellow Wax",
                "f638bd307c7f4524489656c2d581e6f4",
                key: 325,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Labyrinth Organ Chamber Upgrade",
                "c99876c3752a5944b8595554ed77215b",
                key: 326,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Organ Chamber Upgrade",
                "a003ff7a9f11eea498d720c32e226ce0",
                key: 327,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Skeleton Merchant Purchase 1"
            ),

            new(
                "Advanced Organ Chamber Upgrade",
                "b938d2fe17372ba4f9829c6a93a3bdca",
                key: 328,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bloody Thread",
                "0a59935db03f75f4d930e99c813c099d",
                key: 329,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Arcane Salts",
                "42e3ff9953f6eb245a240602bf3bbabd",
                key: 330,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Weapon Upgrade Kit",
                "bc5a272db8f4c95499d61a0e61f894fa",
                key: 331,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Book of Burdens",
                "4a97077027aed8545bccbe878ff58864",
                key: 332,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bloody Bell",
                "add64c1791b32c944973800173a61408",
                key: 333,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Initiate's Candlestick",
                "0300b27548b95e545980b33363220530",
                key: 334,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Apprentice's Candlestick",
                "955f7db3f59109942a664f719ab4eae4",
                key: 335,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Creepy Doll",
                "057b3f7ce32b23541bb9e1471e13671b",
                key: 336,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "\"Drink Me\" Potion",
                "5d86c2bf430dd414091ae78dcdbe14ab",
                key: 337,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "\"Eat Me\" Cake",
                "4d6c751db604f274ab74759037297188",
                key: 338,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Erasure Ritual",
                "d5bb23564b627484ebf2b87fb1a840c4",
                key: 339,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Organ Chamber Discovery"
            ),

            new(
                "Dog Whistle",
                "560cccd8f1e05f64d8db1b30f56448c3",
                key: 340,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cholera Patient Head",
                "b87f7bb4ecea3de45b616e129e8fa9af",
                key: 341,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Pocket Mirror",
                "204657f494970cb44a72f26f418a80d2",
                key: 342,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Portable Crafting Kit",
                "1178ac622fd056b4faf7d5c5d0efb5e2",
                key: 343,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Pottery Shard",
                "1a5a9b13db7c2394ab67233ec605246e",
                key: 344,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Safe Room Twig",
                "d6aaa1910458bc74d9ab2c36e4d0891c",
                key: 345,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Spirit Twig",
                "aa17660c48d93d14e8fa5c2fd0b54818",
                key: 346,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Spirit Branch",
                "17701339ddb08214faaa747a174ed695",
                key: 347,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Camera",
                "7c69aefc3ee0f864687fac77df040d43",
                key: 348,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Skeleton Merchant Purchase 2"
            ),

            new(
                "Bayonet",
                "1f479579822c284499976d940e0646ee",
                key: 349,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Bloody Dao",
                "0292899c079286d46b42683dd372378c",
                key: 350,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: "Blood Tower First Floor Discovery 1"
            ),

            new(
                "Grenade",
                "746a96ac2486b44488550fc310600cc4",
                key: 351,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Tesla Coil Mace",
                "87359e0cbf5daa744bf6f75aeb3f922d",
                key: 352,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Night Mother's Blade",
                "33ecd5dff8d20d3428fac3417f2cf2f9",
                key: 353,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Shotgun",
                "7d5bdd16998187e40b1f7b166c27027f",
                key: 354,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Shotgun Shell",
                "6152ee2d116c4034da72a299d0f6c734",
                key: 355,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Empty Shotgun Shell",
                "231fe325302fb1147a4519adfe2af7fd",
                key: 356,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                ".455 Webley Bullet",
                "326db830b0afd804091f49a6d554e9eb",
                key: 357,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Webley Mk. VI",
                "bdfe4b3881964fc4a944e1d6981ecb57",
                key: 358,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Pipe",
                "295d59b23990f614bbf1ad5b9d59e570",
                key: 359,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Axe",
                "04fb20bb10aec284491a0588051f57c9",
                key: 360,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Cleaver",
                "5a16e815369b7bc4c8e385f27c15cf82",
                key: 361,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Flaming Grease",
                "c82ec7dd7b394af469ac73bd7703870e",
                key: 362,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Poison Grease",
                "3192764001d73634ea3f30c58d35ea0f",
                key: 363,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Cutting Grease",
                "48a7af44497718148a8924e97a6593ed",
                key: 364,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Firework",
                "22caa4735077aa74ca2a6fa30bddab6a",
                key: 365,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Sickle",
                "dde6988e84a2f7c42a4033ae1a040ff7",
                key: 366,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Old Sword",
                "b812dea5c2199ed4cb38460a0713c7e2",
                key: 367,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Scythe",
                "2ae667425bb5f8e47beb9ae7211d83b7",
                key: 368,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Golden Spear",
                "d7c0760c8fd06084b8014775fcb2b903",
                key: 369,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Knife",
                "1d472eb78b3f71645b05f7f337331955",
                key: 370,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Rapier",
                "e6c4816ecefffd849baa6c9dffe9d069",
                key: 371,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Throwing Knife",
                "84afb6062ce9d5945811298c6774399b",
                key: 372,
                createsLocation: false,
                includeInPool: true,
                repeatableFiller: true,
                locationNameOverride: null
            ),

            new(
                "Torch",
                "7551c369a79167745a7019b75546fa24",
                key: 373,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Whip",
                "9f7f8fdd319db344aa07c3623182ff78",
                key: 374,
                createsLocation: true,
                includeInPool: true,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Violence",
                "bac564db57b14474c99eecf65449bf60",
                key: 375,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Dexterity",
                "01b7b23a340555042859eedd701a9b22",
                key: 376,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Weirdness",
                "a54c78d4df7532640926c3c29ee7e10f",
                key: 377,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Ascend",
                "f1b3ecff40c31e6428af91392483c91f",
                key: 378,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Warding",
                "1e6e6189970624042b1f3846f06f3edd",
                key: 379,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Vigor",
                "b4e4f9b8e71ef644db0fa1328453d0f4",
                key: 380,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Fortune",
                "262a2da694001ac4795d0f36b6c806c7",
                key: 381,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Fortitude",
                "11364c5347334a843a7eb702430220a5",
                key: 382,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Immunity",
                "da31c7dabb490a444bbf1b7b2b9f3e6f",
                key: 383,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),

            new(
                "Agility",
                "7bfa1ab0967fbd34baa026ef06519fd4",
                key: 384,
                createsLocation: false,
                includeInPool: false,
                repeatableFiller: false,
                locationNameOverride: null
            ),






        };


        public static RandomizedItemData? ByGuid(string guid)
        {
            return Items.FirstOrDefault(
                x => string.Equals(
                    x.Guid,
                    guid,
                    StringComparison.OrdinalIgnoreCase
                )
            );
        }


        public static RandomizedItemData? ByItemId(long itemId)
        {
            return Items.FirstOrDefault(
                x => x.ItemId == itemId
            );
        }

        /*
        public static RandomizedItemData? ByLocationId(long locationId)
        {
            return Items.FirstOrDefault(
                x => x.LocationId == locationId
            );
        }
        */

        public static List<RandomizedItemData> RandomizedItems()
        {
            return Items
                .Where(x => x.CreatesLocation)
                .ToList();
        }


        public static List<RandomizedItemData> PoolItems()
        {
            return Items
                .Where(x => x.IncludeInPool)
                .ToList();
        }


        public static List<RandomizedItemData> FillerItems()
        {
            return Items
                .Where(
                    x => x.IncludeInPool &&
                         x.RepeatableFiller
                )
                .ToList();
        }

        public static RandomizedItemData? ByLocationId(long locationId)
        {
            foreach (RandomizedItemData data in RandomizedItems())
            {
                if (data.LocationId.HasValue &&
                    data.LocationId.Value == locationId)
                {
                    return data;
                }
            }

            return null;
        }

        public static bool IsMultiDiscoveryItem(
    RandomizedItemData data)
        {
            if (data == null)
                return false;

            return MultiDiscoveryCounts.ContainsKey(data.Name);
        }


        public static bool IsMultiDiscoveryItem(string guid)
        {
            RandomizedItemData? data = ByGuid(guid);

            return data != null &&
                   IsMultiDiscoveryItem(data);
        }


        public static List<MultiDiscoveryLocationData>
            GetMultiDiscoveryLocations(
                RandomizedItemData data)
        {
            List<MultiDiscoveryLocationData> result = new();

            if (data == null)
                return result;

            if (!MultiDiscoveryCounts.TryGetValue(
                    data.Name,
                    out int count) ||
                count <= 0)
            {
                return result;
            }


            string locationPrefix =
                data.Name == "Trickster Medal"
                    ? "Bryn Bach Abbey Trial Completion"
                    : $"Discover {data.Name}";

            /*
             * The ordinary item key is recoverable from ItemId:
             *
             *     ItemId = ItemIdBase + key
             *
             * Multi-discovery location #1 uses the ordinary
             * key-derived location ID even though this item's
             * CreatesLocation flag is false.
             */
            long key =
                data.ItemId - ItemIdBase;

            long firstLocationId =
                LocationIdBase + key;

            result.Add(
                new MultiDiscoveryLocationData(
                    1,
                    firstLocationId,
                    $"{locationPrefix} 1"
                )
            );

            /*
             * Extra locations begin at MultiDiscoveryLocationIdBase.
             *
             * Reserve ranges deterministically in ItemData.Items order.
             * This matches the item/key ordering used by the generated
             * APWorld data.
             */
            long extraOffset = 0;

            foreach (RandomizedItemData candidate in Items)
            {
                if (candidate == data)
                    break;

                if (MultiDiscoveryCounts.TryGetValue(
                        candidate.Name,
                        out int candidateCount) &&
                    candidateCount > 1)
                {
                    extraOffset += candidateCount - 1;
                }
            }

            for (int ordinal = 2;
                 ordinal <= count;
                 ordinal++)
            {
                long locationId =
                    MultiDiscoveryLocationIdBase +
                    extraOffset +
                    (ordinal - 2);

                result.Add(
                    new MultiDiscoveryLocationData(
                        ordinal,
                        locationId,
                        $"{locationPrefix} {ordinal}"
                    )
                );
            }

            return result;
        }


        public static List<MultiDiscoveryLocationData>
            GetMultiDiscoveryLocations(string guid)
        {
            RandomizedItemData? data = ByGuid(guid);

            if (data == null)
                return new List<MultiDiscoveryLocationData>();

            return GetMultiDiscoveryLocations(data);
        }

        public static IReadOnlyList<RandomizedItemData> All()
        {
            return Items;
        }
    }
}