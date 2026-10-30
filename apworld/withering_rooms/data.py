from dataclasses import dataclass

from BaseClasses import ItemClassification


ITEM_ID_BASE = 777000
LOCATION_ID_BASE = 778000
LORE_LOCATION_ID_BASE = 779000
MONSTER_LOCATION_ID_BASE = 780000
REMEMBRANCE_LOCATION_ID_BASE = 781000


MULTI_DISCOVERY_LOCATION_ID_BASE = 782000



MULTI_DISCOVERY_COUNTS: dict[str, int] = {
    "Remembrance Tear": 12,
    "Coin Purse": 5,
    "Trickster Medal": 20,
}


MANDATORY_ITEM_COUNTS: dict[str, int] = {
    "Remembrance Tear": 34,
    "Coin Purse": 5,
    "Trickster Medal": 10,
}


@dataclass(frozen=True)
class RandomizedItemData:
    key: int
    guid: str
    classification: ItemClassification

    creates_location: bool = False
    include_in_pool: bool = True
    unique_in_pool: bool = False
    repeatable_filler: bool = False

    location_name_override: str | None = None
    viable_region_keys: tuple[str, ...] = ()

    @property
    def item_id(self) -> int:
        return ITEM_ID_BASE + self.key

    @property
    def location_id(self) -> int | None:
        if not self.creates_location:
            return None
        return LOCATION_ID_BASE + self.key


@dataclass(frozen=True)
class LoreLocationData:
    key: int
    guid: str
    viable_region_keys: tuple[str, ...] = ()
    progression_allowed: bool = True

    @property
    def location_id(self) -> int:
        return LORE_LOCATION_ID_BASE + self.key


@dataclass(frozen=True)
class MonsterLocationData:
    key: int
    guid: str
    viable_region_keys: tuple[str, ...]
    progression_allowed: bool

    @property
    def location_id(self) -> int:
        return MONSTER_LOCATION_ID_BASE + self.key


@dataclass(frozen=True)
class RemembranceLocationData:
    key: int
    room_guid: str
    viable_region_keys: tuple[str, ...]

    @property
    def location_id(self) -> int:
        return REMEMBRANCE_LOCATION_ID_BASE + self.key


RANDOMIZED_ITEMS: dict[str, RandomizedItemData] = {


    # AUTO-GENERATED FROM items.csv
    # Paste into RANDOMIZED_ITEMS.

    'Summoning Knife': RandomizedItemData(
        key=1,
        guid='0e04d0decb256ab4795982a2599d74af',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'League Curse Charm': RandomizedItemData(
        key=2,
        guid='2a2211cb592eb4f46adf02b89923d207',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'League Damage Charm': RandomizedItemData(
        key=3,
        guid='d9489a3d89733bf4d88fcbfc920c78e6',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'League Health Charm': RandomizedItemData(
        key=4,
        guid='01a75de9242f2cf4992146c0819c4646',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Curse Charm': RandomizedItemData(
        key=5,
        guid='71d89d193c1ad1c448b3fcd00f3111ca',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S3:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOT', 'S4:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOT'),
    ),

    'Health Charm': RandomizedItemData(
        key=6,
        guid='e795e043a9a21114b85f5aa41c71fc47',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S3:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOT', 'S4:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOT'),
    ),

    'Luck Charm': RandomizedItemData(
        key=7,
        guid='25e43572613c0f24f86aa54206689023',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S3:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOT', 'S4:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOT'),
    ),

    'Melee Charm': RandomizedItemData(
        key=8,
        guid='7bcb2e388ae33924aa1b49b9e1c64db7',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOT', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOT'),
    ),

    'Poise Charm': RandomizedItemData(
        key=9,
        guid='1c46cf82eeb80ac47bce9adcb1d47d00',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S3:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOT', 'S4:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOT'),
    ),

    'Projectile Charm': RandomizedItemData(
        key=10,
        guid='58c1aafd008b9cb41b7504d6eee00418',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOT', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOT'),
    ),

    'Resistance Charm': RandomizedItemData(
        key=11,
        guid='bd10ce589c7f940449bbbb2f19256ff0',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S3:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOT', 'S4:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOT'),
    ),

    'Speed Charm': RandomizedItemData(
        key=12,
        guid='046b5a2e113ca2a4d889aab7be385119',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOT', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOT'),
    ),

    'Spell Charm': RandomizedItemData(
        key=13,
        guid='94bffe933b362df4eae5c205b0062f3c',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticCloseHall', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOT', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOT'),
    ),

    'Rotted Charm': RandomizedItemData(
        key=14,
        guid='f51c239fa04079b4b8e4e8da3b85baea',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Onyx Pentagram': RandomizedItemData(
        key=15,
        guid='ef1ca913f74daba46908e1d47ab43a05',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:b865704bfa3d595429325b2e098831e5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:b865704bfa3d595429325b2e098831e5', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOT'),
    ),

    'Pentagram of Blood': RandomizedItemData(
        key=16,
        guid='c383b118070ce754d97e3e84e3df5764',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:b865704bfa3d595429325b2e098831e5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:b865704bfa3d595429325b2e098831e5', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOT'),
    ),

    'Mossy Pentagram': RandomizedItemData(
        key=17,
        guid='12d62d0b3c5982047981a08d0d09a791',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:b865704bfa3d595429325b2e098831e5', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOT', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:b865704bfa3d595429325b2e098831e5', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOT'),
    ),

    'Pentagram of Flesh': RandomizedItemData(
        key=18,
        guid='2deb4d86a1472b447b6ab89d0330d1a6',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b865704bfa3d595429325b2e098831e5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:b865704bfa3d595429325b2e098831e5', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Lucky Necklace': RandomizedItemData(
        key=19,
        guid='8ae1dec96d0d879479eb8c8094afa000',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Gatehouse Spawn Room Discovery 1',
        viable_region_keys=('S2:ROOM:e550141cbe7d0794898d5383ebeb7df6',),
    ),

    'Golden Pentagram': RandomizedItemData(
        key=20,
        guid='ad8945e928ea32e4780f4e57fdbb0c1a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:b865704bfa3d595429325b2e098831e5', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOT', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:b865704bfa3d595429325b2e098831e5', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOT'),
    ),

    'Night Mother Amulet': RandomizedItemData(
        key=21,
        guid='433fe53f4d1bdb7409a326f931b69d9e',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:00643b3d395ecd44e9c2980ce311d42b', 'S4:ROOM:00643b3d395ecd44e9c2980ce311d42b'),
    ),

    'Vampire Locket': RandomizedItemData(
        key=22,
        guid='8808cc2488f904e44b4b238166daf190',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT'),
    ),

    'Holy Pentagram': RandomizedItemData(
        key=23,
        guid='989d011c3256c3e4a91e1a8ed56fee0f',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:b865704bfa3d595429325b2e098831e5', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOT', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:b865704bfa3d595429325b2e098831e5', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOT'),
    ),

    'Befouled Head': RandomizedItemData(
        key=24,
        guid='7da9c50c25298e346a44de60ae7e0522',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Small Cursed Snuffbox': RandomizedItemData(
        key=25,
        guid='01c257fb0c675414c846b476e9ac2c72',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Flight Codex': RandomizedItemData(
        key=26,
        guid='59fb117e3994e8d4aa4ff0ad6899b19a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override="Margaret's Room Discovery 1",
        viable_region_keys=('S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0',),
    ),

    'Evasion Codex': RandomizedItemData(
        key=27,
        guid='e91eac773ae06e5458006e76a21c819a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:4701166c9b412f34cad491a232827334'),
    ),

    'Inverted Gaze': RandomizedItemData(
        key=28,
        guid='6ef7d3ab460c93546b910c170cb861fd',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Lantern Familiar': RandomizedItemData(
        key=29,
        guid='60d43b62eb51c0742a214af0cf637a63',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Nightingale Doll': RandomizedItemData(
        key=30,
        guid='f9019d4ac6632594dbde26aa83fd1e4e',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:4946ce2c8d5ba0c4c94386976c6c2bd1', 'S4:ROOM:4946ce2c8d5ba0c4c94386976c6c2bd1'),
    ),

    'Closed Gaze': RandomizedItemData(
        key=31,
        guid='96b9f19cab7209e4ca88988c57ebcc56',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Troy's Head": RandomizedItemData(
        key=32,
        guid='0b05f1e0a046c4b45be8e76b9eff4b47',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Perception Codex': RandomizedItemData(
        key=33,
        guid='2d6db4bbf9b26bc42babc8cd226a8fa2',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Guard Codex': RandomizedItemData(
        key=34,
        guid='14336fc233369364fbdfc10dc67febf1',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOT', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Large Cursed Snuffbox': RandomizedItemData(
        key=35,
        guid='0fc1524f9fed7f442bffe1dc6567f105',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Telescope Puzzle',
        viable_region_keys=('S2:ROOM:d7d694fb5f60763428690238f4ce0839',),
    ),

    'Second Chance Brooch': RandomizedItemData(
        key=36,
        guid='a0588e090fc1eff418b9c93333181c9e',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Speakeasy', 'S4:AREA:mansion_import_1__Speakeasy'),
    ),

    'Pale Skull Ring': RandomizedItemData(
        key=37,
        guid='b6ace7e7405386b4d937c6cc6e0c49bd',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOT'),
    ),

    'Ruffian Ring': RandomizedItemData(
        key=38,
        guid='341da601c264c6d48be9a2b516e0d8c5',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOT', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Bloody Ring': RandomizedItemData(
        key=39,
        guid='d35be4124e19204469a1b0cdd239b0f6',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOT'),
    ),

    'Gold Skull Ring': RandomizedItemData(
        key=40,
        guid='142bc863c43e9df46af16e6fea0bbbd0',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOT'),
    ),

    'Shield Ring': RandomizedItemData(
        key=41,
        guid='0db4a05a319ce0643bf659725e4d2f04',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOT'),
    ),

    "Knight's Ring": RandomizedItemData(
        key=42,
        guid='74ab7bb3e55ede047b7a3c9e25da220a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Silver Skull Ring': RandomizedItemData(
        key=43,
        guid='09b7663c4b6a684409837008cdfcc599',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    "Hunter's Ring": RandomizedItemData(
        key=44,
        guid='ce1632889288be1409f9108c2f0acec8',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S8:ROOM:714150db49d065f46a10c44f71bedad3'),
    ),

    'Barrel Ring': RandomizedItemData(
        key=45,
        guid='20e816b0bbd55f14a94dd00273e3a23a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Skull Ring': RandomizedItemData(
        key=46,
        guid='6f53473a95403234ea41c1f0d35af8c9',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    "Gold Hunter's Ring": RandomizedItemData(
        key=47,
        guid='acbf0d352592c99478d54c5c3cce29bd',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    "Pale Hunter's Ring": RandomizedItemData(
        key=48,
        guid='798061183fb5eaa499bce7c71359cec5',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Critical Ring': RandomizedItemData(
        key=49,
        guid='7dab139074ea1c24b91545b049d1cc6e',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Savior Ring': RandomizedItemData(
        key=50,
        guid='dea8b9964f515c54694e925fedd4648a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    "Phantom's Ring": RandomizedItemData(
        key=51,
        guid='4e9ca3ddfbc1a6c4b81dac845f1af4e4',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    "Rogue's Ring": RandomizedItemData(
        key=52,
        guid='4e6e655adf6ec86499975f2f2198050c',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOT', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Silver Bear Ring': RandomizedItemData(
        key=53,
        guid='09cbdf2bbea191f41a18af1f391377e6',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Covetous Ring': RandomizedItemData(
        key=54,
        guid='126300cf3aed8734692c001c1e3d6ba6',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Flesh Ring': RandomizedItemData(
        key=55,
        guid='91e9f0cfefa583043bdddad702b65bd7',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Cursed Flesh Ring': RandomizedItemData(
        key=56,
        guid='27943397c48af344f83d8c49d237d8b5',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Gold Bear Ring': RandomizedItemData(
        key=57,
        guid='9fb3ae2a81bd94d41adeda9365a2d946',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Swift Ring': RandomizedItemData(
        key=58,
        guid='08aeda98faea32844a7bd82a812612a2',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Black Cross Ring': RandomizedItemData(
        key=59,
        guid='14364140285554e41a426a2bc8a7349d',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Burnt Ring': RandomizedItemData(
        key=60,
        guid='65d63c4cf13a78f479e6197fba55a402',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Curse Ward Ring': RandomizedItemData(
        key=61,
        guid='a0c9f327863af73469175e3912001fbe',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    "Frog's Eye Ring": RandomizedItemData(
        key=62,
        guid='13eb73037dd9591408e418e9995b42eb',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Red Life Ring': RandomizedItemData(
        key=63,
        guid='30ff0e013fb8f214c8e9d900b9acc6c5',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Castle Ring': RandomizedItemData(
        key=64,
        guid='57aa29d44213ed44283b9156672f031a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Chromatic Ring': RandomizedItemData(
        key=65,
        guid='2c7242b0de56dce4db9135d4b14bf3e4',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Cursed Explorer Ring': RandomizedItemData(
        key=66,
        guid='57fc32a6bee324c4d8d541762497e92c',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S2:AREA:mansion_UpperBalcony', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    "Rabbit's Heart Ring": RandomizedItemData(
        key=67,
        guid='4f400f0ba0deacb408af5e88179a26e3',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Fortress Ring': RandomizedItemData(
        key=68,
        guid='faa9d44be7f33b144ace21c99f7ba6db',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Gold Cross Ring': RandomizedItemData(
        key=69,
        guid='6e91c70a30623b54389fddb3cf7b9fea',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    "Necromancer's Ring": RandomizedItemData(
        key=70,
        guid='64e3974b59e4a1c4faab7dd2b64c5a97',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOT', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Cursed Balance Ring': RandomizedItemData(
        key=71,
        guid='6fa0aeedc050a914d8afbcb4158f0547',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOT', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Necrotic Ring': RandomizedItemData(
        key=72,
        guid='3ad34c4642d98e74bbe4813e186f7801',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_0__CholeraHallway', 'S4:AREA:mansion_import_2_import_0__CholeraHallway'),
    ),

    'Ruby Ring': RandomizedItemData(
        key=73,
        guid='e54b3cd031d54b44da72f232a4f39a49',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Infirmary', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOT', 'S4:AREA:mansion_import_1__Infirmary', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Candle Ring': RandomizedItemData(
        key=74,
        guid='7b69231edf687374a9992e61f513dac4',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:c3c7869b2d5e4b54ab0435736cf75408',),
    ),

    "Margaret's Ring": RandomizedItemData(
        key=75,
        guid='551418bd6e28dfe4e8c8c2271fc1c9af',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S2:AREA:mansion_MovingTrainArea', 'S4:AREA:mansion_BTRoof'),
    ),

    'Moonless Formless Ring': RandomizedItemData(
        key=76,
        guid='9a7e21290e58fa74a90ef7bc0baa509b',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Night Mother's Ring": RandomizedItemData(
        key=77,
        guid='86d4b1848368c374e89b532fee9a3025',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Gatehouse Spawn Room Discovery 2',
        viable_region_keys=('S2:ROOM:e550141cbe7d0794898d5383ebeb7df6',),
    ),

    "Priscilla's Ring": RandomizedItemData(
        key=78,
        guid='7033b6a58da552340990c7297e7b91e6',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Crescent Ring': RandomizedItemData(
        key=79,
        guid='58a972b8a42925b49a2ace91fc8fea29',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Dull Silver Ring': RandomizedItemData(
        key=80,
        guid='ed54e01f28a1c1641a7fcf2a2f723dd1',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Exquisite Gold Ring': RandomizedItemData(
        key=81,
        guid='1422c4d8a5b6d08489268c08697e1d2b',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOT'),
    ),

    'Moon Ring': RandomizedItemData(
        key=82,
        guid='dd4a15240a318fe49af3628624ace294',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Nowhere', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOT'),
    ),

    'Eclipse Ring': RandomizedItemData(
        key=83,
        guid='76f3fd53931084645a290a9a2e2cd6d3',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOT'),
    ),

    'Exquisite Silver Ring': RandomizedItemData(
        key=84,
        guid='d2c8d21f4d52153428cce0cb041ac03c',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOT', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOT'),
    ),

    'Bleeding Resistance Syringe': RandomizedItemData(
        key=85,
        guid='8767d7f98fff58e48b26795c7b3a6e80',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Violent Pill': RandomizedItemData(
        key=86,
        guid='c5bc9010a0840434aac8255aca3e9c93',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Paralysis Resistance Syringe': RandomizedItemData(
        key=87,
        guid='8b1a2036541d9694d81066ee3b2d8a0a',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Poison Resist Syringe': RandomizedItemData(
        key=88,
        guid='cc865d9d6a8ee614b9913075a40b219d',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Dexterous Pill': RandomizedItemData(
        key=89,
        guid='c8e00a67017619b47acc9a47a3f42ee7',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Weird Pill': RandomizedItemData(
        key=90,
        guid='7a78d8011dd676342acde48b0963a287',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Bandage': RandomizedItemData(
        key=91,
        guid='c7e6298e40db6d94dab7f5ec80a6f0e8',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Chocolate Cake': RandomizedItemData(
        key=92,
        guid='fef9ef4284ef5bb4e9d89a8d306ab1a1',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Warding Cupcake': RandomizedItemData(
        key=93,
        guid='3d2ab4aad625c3b46b950b2665a358eb',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'First Aid Kit': RandomizedItemData(
        key=94,
        guid='7a4cab3f8e1c6624da413261a9bd290c',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Hearty Roll': RandomizedItemData(
        key=95,
        guid='a91aa55236bb565478172704564e9cdd',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Poison Antidote': RandomizedItemData(
        key=96,
        guid='abffc4a58c4fae147ad9fe85f175d171',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Rarebit': RandomizedItemData(
        key=97,
        guid='f4ae4bd0aaf82df459bc171585ec6e83',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Ration': RandomizedItemData(
        key=98,
        guid='b679a2259eefe4d44a3282e3ebfd9cf6',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Corrupted Meat': RandomizedItemData(
        key=99,
        guid='9e2e28bd9e5281c4cbccba0061910596',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Scone': RandomizedItemData(
        key=100,
        guid='582cc66a03491ed47bbb32d479838386',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Cup of Tea': RandomizedItemData(
        key=101,
        guid='940fc8d340ab90b4da5dc01ce22a45eb',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Warding Candle': RandomizedItemData(
        key=102,
        guid='a646287c4ba6736448200b4a75354b40',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Acid Jar': RandomizedItemData(
        key=103,
        guid='ecf6c16102bb3a941ac30ec0bbd40b9f',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Ambrosia Jar': RandomizedItemData(
        key=104,
        guid='15b82143a57adb0478a1434d097643e2',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Blood Jar': RandomizedItemData(
        key=105,
        guid='ff0b6f3451c69cd4796ab357c46f32f1',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Curse Jar': RandomizedItemData(
        key=106,
        guid='b4046e382f38d0d42a4cfb40800177a4',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Elixir Jar': RandomizedItemData(
        key=107,
        guid='f14e9abb553881c489fe4cdf127c5a98',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Empty Jar': RandomizedItemData(
        key=108,
        guid='52c4921fd0b2cd54dad42508980c4b6f',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Incendiary Jar': RandomizedItemData(
        key=109,
        guid='634e8e686bca7db4b83719aa4a1b2da1',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Nail Trap': RandomizedItemData(
        key=110,
        guid='57b4d571462d4e146a91227d23e83ea9',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Paralysis Jar': RandomizedItemData(
        key=111,
        guid='6190eab4ecd123c4ea8560781f5ef8dd',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Paralysis Trap': RandomizedItemData(
        key=112,
        guid='815640289a7d8cd46830de28535bee53',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Poison Jar': RandomizedItemData(
        key=113,
        guid='b620eea25af75294c8242c08c2f53da2',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Tonic Jar': RandomizedItemData(
        key=114,
        guid='cb650a4c26b9d4d4ea42335bae1251f3',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Firearm License': RandomizedItemData(
        key=115,
        guid='5d53c67b32d570249895dae308eb8240',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Hallway', 'S4:AREA:mansion_import_1__Hallway'),
    ),

    'Skull Key': RandomizedItemData(
        key=116,
        guid='316410550ebed8d4fb69a1c7d7178e03',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Advanced Wretch Pass': RandomizedItemData(
        key=117,
        guid='c297e118df2e4ba4baae0be5ebe38b35',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Hallway', 'S4:AREA:mansion_import_1__Hallway'),
    ),

    'Labyrinth Market Key': RandomizedItemData(
        key=118,
        guid='188968d0ea9663d47955f99067ec038c',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:b865704bfa3d595429325b2e098831e5', 'S4:ROOM:b865704bfa3d595429325b2e098831e5'),
    ),

    'Basic Wretch Pass': RandomizedItemData(
        key=119,
        guid='30b2245239a786a4aadc7db1734aae90',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Hallway', 'S4:AREA:mansion_import_1__Hallway'),
    ),

    'Hotel Elevator Key': RandomizedItemData(
        key=120,
        guid='314dd217f10573341a94d5250f5ab312',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Jailer's Elevator Key": RandomizedItemData(
        key=121,
        guid='c985949f08d9bc343b76b323ee15eeeb',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Robert's Elevator Key": RandomizedItemData(
        key=122,
        guid='37fd582c701a9044e98af2224929c3be',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override="Robert's Backroom Discovery 1",
        viable_region_keys=('S4:ROOM:aa2ea50e664bfb94dba39a36ae0985a7',),
    ),

    'Cholera Clinic Cage Key': RandomizedItemData(
        key=123,
        guid='bbe3f26cf697f7448b751d972a395a50',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "St. Elli's Key": RandomizedItemData(
        key=124,
        guid='8bf163e5226ded24fb4d045f72269670',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__ChurchUpperHallway', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:AREA:mansion_import_1__ChurchUpperHallway', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e'),
    ),

    'Rusty Cage Key': RandomizedItemData(
        key=125,
        guid='af9415dadb6404848bbcc2551cd39bfe',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:9b93a0c714ee7e747b9be0ecb172a84c',),
    ),

    'Dining Hall Invitation': RandomizedItemData(
        key=126,
        guid='da59fd69a765c5847b883f4e62f22eb0',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Door Handle': RandomizedItemData(
        key=127,
        guid='c60a0b65f2b0f9541acb2107a42c888f',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Blackett Attic Storage Discovery 1',
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877',),
    ),

    'East Stairwell Key': RandomizedItemData(
        key=128,
        guid='87e09fe50faa54b4f9528cd20c8443c7',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_EastStairwell', 'S1:AREA:mansion_Hallway', 'S2:AREA:mansion_import_0__CoffinRoom', 'S2:AREA:mansion_import_0__EastStairwell', 'S3:AREA:mansion_import_2__ChurchBellTower', 'S4:AREA:mansion_import_1__ChurchBellTower'),
    ),

    'Eviction Letter': RandomizedItemData(
        key=129,
        guid='f584f391c3b350240825fe08b42acb28',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Hallway', 'S4:AREA:mansion_import_1__Hallway'),
    ),

    'Right Idol Eye': RandomizedItemData(
        key=130,
        guid='8733011378a78854db88c16530c251d2',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:8bb5ddfba2ed94045994524da6dd9653',),
    ),

    'Entrance Hall Binding Spell': RandomizedItemData(
        key=131,
        guid='5cc588540a9aeeb468c8a649d55edaf1',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64',),
    ),

    'Entrance Hall Spell Key': RandomizedItemData(
        key=132,
        guid='10b131bf509812840a3b9404e52de4f8',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Entrance Hall Key': RandomizedItemData(
        key=133,
        guid='402350cae0fee8a409fd210d06ca1e66',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Front Door Key': RandomizedItemData(
        key=134,
        guid='2107c183c60da5946a5aad3f5f11911d',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Gatehouse Key': RandomizedItemData(
        key=135,
        guid='d8bcf2190bd1fa8469531e588da16ec4',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override="Dafydd's Back",
        viable_region_keys=('S0:ROOM:205312511cf1e074fbfd024e9a102ef6',),
    ),

    'Grandfather Clock Key': RandomizedItemData(
        key=136,
        guid='aad7d8862b70d974e9244f356b02723a',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S2:AREA:mansion_UpperBalcony'),
    ),

    "Night Mother's Disciple Book": RandomizedItemData(
        key=137,
        guid='066d50b0c15bd8b499268c341734333f',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Observatory Key': RandomizedItemData(
        key=138,
        guid='3e32df5309d218d4badf215e14aae538',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839'),
    ),

    'Occult Library Key': RandomizedItemData(
        key=139,
        guid='f6debaee10c350b40be4f5ead88cc771',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Murder Algebra Puzzle',
        viable_region_keys=('S1:ROOM:6004319eb2f5de547ae38b9bef18431a',),
    ),

    'Puzzle Oracle': RandomizedItemData(
        key=140,
        guid='7bca4e9f589e32e45867bff6f54a59fe',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Electrical Generator': RandomizedItemData(
        key=141,
        guid='6905aa76b72504c4e8a0f57ed0642dcc',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Blackett House Key': RandomizedItemData(
        key=142,
        guid='34f5ef0ccedf7124fb11fe6a1cb7a837',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Crumbling Interior Key': RandomizedItemData(
        key=143,
        guid='550896c3724cf264995161f8da758336',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Waking Powder': RandomizedItemData(
        key=144,
        guid='987bdb8909818444ba3dc62c818dcbef',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Wretch Teleportation Spell': RandomizedItemData(
        key=145,
        guid='cc51367a57d288346b0f539c82f1cfea',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Hallway', 'S4:AREA:mansion_import_1__Hallway'),
    ),

    'Blue Secret Passage Key': RandomizedItemData(
        key=146,
        guid='03a8a5f9c95cc3c40ba523067f35873c',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701',),
    ),

    'Skin Covered Key': RandomizedItemData(
        key=147,
        guid='ffa6d4c13eefba543bddd6c586cbe455',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Stairwell Spell Key': RandomizedItemData(
        key=148,
        guid='ef8564d0bf51db84ebc43aa167f884bf',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Strange Bedroom Key': RandomizedItemData(
        key=149,
        guid='4bbd68b091bea824996669c33defd7d3',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Ancient Rite: Outfit': RandomizedItemData(
        key=150,
        guid='046f996923a576f45a0acf82ce326caa',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Ancient Rite: Spell': RandomizedItemData(
        key=151,
        guid='f60e6c930e98fd240b1cc815179f5725',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Ancient Rite: Weapon': RandomizedItemData(
        key=152,
        guid='6d5d687895d4ff5468b42869dbc73681',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Vicar's Card": RandomizedItemData(
        key=153,
        guid='54a4f51bb919d3e49880be433a0fbe86',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Comforting Bear': RandomizedItemData(
        key=154,
        guid='8fe96a9b54ea47b4ea30deab632e7f12',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOT', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOT'),
    ),

    'Bible': RandomizedItemData(
        key=155,
        guid='3b028c4621fe2a140ac7ace0bbc2d47b',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Spiked Coffin Shield': RandomizedItemData(
        key=156,
        guid='f96a8936bb45f8941817da614e040ad7',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_0__CholeraHallway', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:AREA:mansion_import_2_import_0__CholeraHallway', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Corpse Hand': RandomizedItemData(
        key=157,
        guid='c8b0990dfb4ad3643968cb4b034d42d1',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6'),
    ),

    'Metal Shield': RandomizedItemData(
        key=158,
        guid='b9021b31e821f80468dd2ce5155d71f4',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Mirror Shield': RandomizedItemData(
        key=159,
        guid='026eb2a8927e1ea49913a53ae834c134',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:4f1ffd7c92ff8a54197228f5c14d5c2e', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    "Night Mother's Doll": RandomizedItemData(
        key=160,
        guid='d8f28726c8b6afa49a05e294ca16bc48',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b'),
    ),

    'Oil Lamp': RandomizedItemData(
        key=161,
        guid='54dfce1cf6668c848923637d128c3231',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_EastCourtyard', 'S2:AREA:mansion_import_0__HedgeMazeBoss', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839'),
    ),

    'Old Shield': RandomizedItemData(
        key=162,
        guid='8b76efccd3ec9444985ef1176447b377',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT'),
    ),

    'Spirit Dust Bag': RandomizedItemData(
        key=163,
        guid='8ee76ea5098a41942b7c6500041ec290',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Curious Statue': RandomizedItemData(
        key=164,
        guid='c41a7316af66b7a4da711efd90b6e07d',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Brass Telescope': RandomizedItemData(
        key=165,
        guid='eb31b33403cd3204fb3a2bf70cfd5a03',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Thurible': RandomizedItemData(
        key=166,
        guid='90d521f87970d4a42bf18e71ba33e220',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Old Wooden Shield': RandomizedItemData(
        key=167,
        guid='652d4b219d3ff5942bd9a701b3c204b2',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    "Bee's Fashion Record": RandomizedItemData(
        key=168,
        guid='7f74fc11c391c6043a7ba5e21820e80e',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override="Margaret's Room Discovery 2",
        viable_region_keys=('S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0',),
    ),

    "Death's Fashion Record": RandomizedItemData(
        key=169,
        guid='14cf4a4f18d1401469af8a903fd5ce62',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Goat's Fashion Record": RandomizedItemData(
        key=170,
        guid='7b94730ee46fdca4ca9e636f1162a334',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:c5bc31984f08d13439ec5e5412297319',),
    ),

    "Raven's Fashion Record": RandomizedItemData(
        key=171,
        guid='0b98020ed2fac514381969f369ec25a2',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Spider's Fashion Record": RandomizedItemData(
        key=172,
        guid='6966d578331355e4cb6bb7570b15d9bf',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64',),
    ),

    'Hardened Flesh': RandomizedItemData(
        key=173,
        guid='5a2ff71cb3fb2a3478d6479139b91fe1',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Starry Flamethrower': RandomizedItemData(
        key=174,
        guid='51fae8b74f219ac43a5e2ac3eba8f00f',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Starry Flesh': RandomizedItemData(
        key=175,
        guid='2bc8159c6a197cd4482d36219fe9ad91',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Starry Greatsword': RandomizedItemData(
        key=176,
        guid='981faefdbfeddba49a106ee8a6a8075c',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Alice Dress': RandomizedItemData(
        key=177,
        guid='87cf811ba78769a4d82179f0b2b5f8e1',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884'),
    ),

    'Golden Armor': RandomizedItemData(
        key=178,
        guid='f5dbe7a0998459040a0fe5773e0dd501',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Bloody Apron': RandomizedItemData(
        key=179,
        guid='fabbf27d95f34ca409a9ecb2cff1e9f3',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Bloody Dress': RandomizedItemData(
        key=180,
        guid='d1aff8bdde88ef84fb0d75dbf79fed86',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Blood Tower Second Floor Discovery 1',
        viable_region_keys=('S4:AREA:mansion_BTSecondFloor',),
    ),

    'Clown Suit': RandomizedItemData(
        key=181,
        guid='e978f8f5be6b28a48afd631adcc1f697',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Cursed Armor': RandomizedItemData(
        key=182,
        guid='a6e91642e12ce244fb3d9c1da1f171db',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Doll Dress': RandomizedItemData(
        key=183,
        guid='0ca5b55fb7b4a8d4aa1a70f62fcf492d',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884'),
    ),

    'British Army Uniform': RandomizedItemData(
        key=184,
        guid='e3183a94f8c0be640a26e9ac817f129a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Elegant Dress': RandomizedItemData(
        key=185,
        guid='0b8d68c17ff50c34dbcad1fad07dd985',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Study Room Discovery 1',
        viable_region_keys=('S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0',),
    ),

    "Gentleman's Suit": RandomizedItemData(
        key=186,
        guid='ccb141df6326b124a832e16680f34b6a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884'),
    ),

    'Bloody Nightgown': RandomizedItemData(
        key=187,
        guid='b0251c882a603fa439df50c74d33b644',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S4:ROOM:2708d10a22614a84296aa1a0632ea9cf'),
    ),

    'Murderess Coat': RandomizedItemData(
        key=188,
        guid='3bebcd48f42a8404c87b52a02c247f74',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Crazy Butcher Purchase 1',
        viable_region_keys=('S3:AREA:mansion_AtticEastStairwell', 'S4:AREA:mansion_import_2__AtticEastStairwell'),
    ),

    'Green Cloak': RandomizedItemData(
        key=189,
        guid='ef3b9a35fd64f764a8b4535930c0fd76',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Nurse Uniform': RandomizedItemData(
        key=190,
        guid='ed18eac8bab2f9f4eb819515ec2fe5e0',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Infirmary', 'S4:AREA:mansion_import_1__Infirmary'),
    ),

    'Floral Dress': RandomizedItemData(
        key=191,
        guid='569a17e0fb4304547b28129cefcabec6',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Phantom Threads': RandomizedItemData(
        key=192,
        guid='21a84ce0d80fa7f4ba2198aa8af02bf8',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Prismatic Dress': RandomizedItemData(
        key=193,
        guid='42f9b451ae46aea44b3fe44c57b85664',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Adventurer's Outfit": RandomizedItemData(
        key=194,
        guid='cdff62907f5f52d49bf694673828b1b3',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Ancient Labyrinth Discovery 1',
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56',),
    ),

    'Rust Cloak': RandomizedItemData(
        key=195,
        guid='08b790e3e82466947917524ab7dad475',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Dirty Initiate Dress': RandomizedItemData(
        key=196,
        guid='ca2ccd4d435e01c4394e1d526a207ba0',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Knight's Armor": RandomizedItemData(
        key=197,
        guid='36395ead2d7fa13409c8e1e25fbc3551',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d'),
    ),

    'Starry Dress': RandomizedItemData(
        key=198,
        guid='5f3ee41f0af26814cae3d67e55bb042a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Merry Band Cloak': RandomizedItemData(
        key=199,
        guid='e509548d1570e9840b07b358ba0053f6',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Unlucky Dress': RandomizedItemData(
        key=200,
        guid='6ad2cca56804a434092eff8040c3a103',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64'),
    ),

    'Initiate Dress': RandomizedItemData(
        key=201,
        guid='0a61e772e5e6b77488778ffaaada65f7',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:8bb5ddfba2ed94045994524da6dd9653',),
    ),

    'Christmas Ghost Robe': RandomizedItemData(
        key=202,
        guid='3a05b52ecf94e544eb834123aef2ac1b',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884'),
    ),

    'Cowboy Hat': RandomizedItemData(
        key=203,
        guid='af25d57e28901d444a111e45b7ff83a6',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Ancient Labyrinth Discovery 2',
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56',),
    ),

    'Alice Wig': RandomizedItemData(
        key=204,
        guid='0834dc79a89d3d84bad6c4f838e089e8',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Golden Helmet': RandomizedItemData(
        key=205,
        guid='3e2b5072503b56b4e82c2965d2b46756',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Bandages': RandomizedItemData(
        key=206,
        guid='40c55dbaef3b48b4785f59d52349c34e',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Bell Helmet': RandomizedItemData(
        key=207,
        guid='c27ab3a77e40ae5428e36c828dc51380',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Chapter 3 Discovery 1',
        viable_region_keys=('S3:ROOT',),
    ),

    'Big Initiate Hat': RandomizedItemData(
        key=208,
        guid='9e28501524ddf564789d3a7eca365008',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac'),
    ),

    'Blindfold': RandomizedItemData(
        key=209,
        guid='179c764b6836f68408da14695ad113d0',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_AtticCloseHall', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
    ),

    'Cat Ears': RandomizedItemData(
        key=210,
        guid='3a66a7f814ec95d4f8497dce1687d8af',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Fool's Cap": RandomizedItemData(
        key=211,
        guid='2dc125d2c8a228345b78fb3954cabd52',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Cursed Helmet': RandomizedItemData(
        key=212,
        guid='fbf444b0156003c4fbeb5448cfa0d630',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Doll Bonnet': RandomizedItemData(
        key=213,
        guid='5b5cd139986a03848ae784fd7709fa3d',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Edgar's Bandage": RandomizedItemData(
        key=214,
        guid='a7e199b01d4235e43a9f3a39e0a9b79d',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Flaming Hood': RandomizedItemData(
        key=215,
        guid='477990728a1e3d94eb5361cb7a61930e',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Chapter 3 Discovery 2',
        viable_region_keys=('S3:ROOT',),
    ),

    'Spectacles': RandomizedItemData(
        key=216,
        guid='946d14b6511086f47b4a5fdcf7743ee7',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
    ),

    'Head Lamp': RandomizedItemData(
        key=217,
        guid='b8dac5dc4ca79fc4593cdadd78a65b32',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d'),
    ),

    'Jailkeeper Head': RandomizedItemData(
        key=218,
        guid='61cb87c0e9bba9c4a9d142d814f6ff79',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Medusa Head': RandomizedItemData(
        key=219,
        guid='56b3c28277ae0b34d87eb7a60a3d20df',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Ancient Labyrinth Discovery 3',
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56',),
    ),

    'Necromancer Helm': RandomizedItemData(
        key=220,
        guid='65f998181464ac8449331aa963d8a1dd',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Ancient Labyrinth Discovery 4',
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56',),
    ),

    "Night Mother's Mask": RandomizedItemData(
        key=221,
        guid='0b76c903c8aec0c4387b4fc35ec1d004',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Nurse's Hat": RandomizedItemData(
        key=222,
        guid='d7098d1155e74c04b9294bd83862f96c',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Infirmary', 'S4:AREA:mansion_import_1__Infirmary'),
    ),

    'Pumpkin': RandomizedItemData(
        key=223,
        guid='304a8751bdf8a7b4d930d6ab4505601d',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
    ),

    'Crown': RandomizedItemData(
        key=224,
        guid='ca4f56f18c855714c92abfbbddc376fe',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Masked Man Purchase (Flipped World)',
        viable_region_keys=('S1:AREA:mansion_Hallway',),
    ),

    'Sack': RandomizedItemData(
        key=225,
        guid='0b3ba885adefe464289c0ea2a127c1f5',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Short Cloth': RandomizedItemData(
        key=226,
        guid='984d3a60693e8dd42ab0f23d609ef04b',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
    ),

    'French Pins': RandomizedItemData(
        key=227,
        guid='9b6d893a61597ff4da65999be1fca289',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
    ),

    'Skin Mask': RandomizedItemData(
        key=228,
        guid='0d04a8bd13c56974d834b4d32f17bb42',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Knight's Helm": RandomizedItemData(
        key=229,
        guid='d0f86ec0f4b176c49a83eb5b8d5b1bf3',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
    ),

    'Starry Head Sack': RandomizedItemData(
        key=230,
        guid='a3cdae23298e71644850ac3715e15667',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Top Hat': RandomizedItemData(
        key=231,
        guid='0e882fa9d2e8b9e4da453c218b8f4c28',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
    ),

    'Merry Band Mask': RandomizedItemData(
        key=232,
        guid='75184a2b8abafe844981befe56840ffc',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Tricorne Hat': RandomizedItemData(
        key=233,
        guid='1960eab6d9bb64e4e991bbe4be30c867',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:0e47785bff17bee4abcd516280874216'),
    ),

    'Punishment Cage': RandomizedItemData(
        key=234,
        guid='4a1c7538c6c12ec43b3b906fa369b7d9',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:c1ab381440a89aa4c8a28ce2d75b7527', 'S4:ROOM:c1ab381440a89aa4c8a28ce2d75b7527'),
    ),

    'Hairpin': RandomizedItemData(
        key=235,
        guid='8c5212805f28edb41bcb9161766a1f2a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
    ),

    'Mourning Veil': RandomizedItemData(
        key=236,
        guid='ece19e2b2d8b9144ea3c74dbbf9f7074',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:be1e434f6b7059843ab7f4de19742b75', 'S4:ROOM:be1e434f6b7059843ab7f4de19742b75'),
    ),

    'Vicar Helmet': RandomizedItemData(
        key=237,
        guid='2760676f16c305340be97437a0abaed4',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Initiate Hat': RandomizedItemData(
        key=238,
        guid='43dc9b2f464420f46ba40107e6668d09',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:8bb5ddfba2ed94045994524da6dd9653',),
    ),

    'Big Wretch Hat': RandomizedItemData(
        key=239,
        guid='655db955a5315b84689147e381753d04',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__Hallway', 'S4:AREA:mansion_import_1__Hallway'),
    ),

    'Zombie Outfit': RandomizedItemData(
        key=240,
        guid='f41e3c91c85bbb04abefab003ea629a8',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:c3c7869b2d5e4b54ab0435736cf75408',),
    ),

    'Night Mother Outfit': RandomizedItemData(
        key=241,
        guid='75a4b6d9476d8cf499a4a5c94a717667',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Gambler's Mystery Sack": RandomizedItemData(
        key=242,
        guid='1ef2d6183ad9bfe42aee0e49fabc81e1',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Gold Hagsack': RandomizedItemData(
        key=243,
        guid='54b3138efb2ca8944897e185599eda5e',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Healing Hagsack': RandomizedItemData(
        key=244,
        guid='dd7af67e9d985b845838df7deac34f52',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Jar Sack': RandomizedItemData(
        key=245,
        guid='b3161f8a01cec7a4ba7d0538832e0b0c',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Warrior's Mystery Sack": RandomizedItemData(
        key=246,
        guid='da6b9d44cc5142a48bcd817e07e0e3eb',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Melee Hagsack': RandomizedItemData(
        key=247,
        guid='1a7a431d777890a48965b4f5d65fad38',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Occult Mystery Hagsack': RandomizedItemData(
        key=248,
        guid='49769bfdb46dfd642b8e2d693a45df12',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Spell Hagsack': RandomizedItemData(
        key=249,
        guid='818f26a205f650b4bafdbc5325cc70bd',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'War Hagsack': RandomizedItemData(
        key=250,
        guid='bb8bf5d7ad5358a45889fb027ddbd461',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Baleful Influence Book': RandomizedItemData(
        key=251,
        guid='9e902d9b855607a47954a7fd935d3b7f',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Burning Protection Book': RandomizedItemData(
        key=252,
        guid='4141f43b326bd7045857a525c5a48b55',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Possession Book': RandomizedItemData(
        key=253,
        guid='e0ec740b07d03e549aca1fa3da50fef6',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Summon Spears Book': RandomizedItemData(
        key=254,
        guid='435100b9ff8e2ad4092adc05f5bcc10b',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Fireball Book': RandomizedItemData(
        key=255,
        guid='c726a7c972edc9440abf99192a25a2b0',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Corpse Hex Book': RandomizedItemData(
        key=256,
        guid='6b5e1b03dacee154a9dc5fdd26038ad5',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Curse Form Book': RandomizedItemData(
        key=257,
        guid='dcca2d3651d08d0428e7345dfb73cac9',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Healing Barrier Book': RandomizedItemData(
        key=258,
        guid='ce72fb8e06364be4b8269c3006cd5d1e',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Annihilation Spell': RandomizedItemData(
        key=259,
        guid='deced5ca707efb64f826bbbd377a4133',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Armor Spell': RandomizedItemData(
        key=260,
        guid='afbd1acf76ff6394889507767e07b5eb',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Enchant Spell': RandomizedItemData(
        key=261,
        guid='3092fe4b0ce674f4daeafb27d3006b82',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Harvest Field Spell': RandomizedItemData(
        key=262,
        guid='851c27c2434e79a43b76ddc2c47e9d95',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Curse Ball Spell': RandomizedItemData(
        key=263,
        guid='fec85b062f6ead548932cb61702b0092',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Door Hex Spell': RandomizedItemData(
        key=264,
        guid='ef922bfde6d67f943ab83ea49c67df09',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Curse Orbs Scroll': RandomizedItemData(
        key=265,
        guid='b809c204e964ef846a743114cc8277b4',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Dummy Spell': RandomizedItemData(
        key=266,
        guid='85060d6e5d309b343b0778e7a5dd6db6',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Advanced Grimoire': RandomizedItemData(
        key=267,
        guid='ae8cc38c59d51ce46907a9023be2591e',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334',),
    ),

    'Basic Grimoire': RandomizedItemData(
        key=268,
        guid='4f1c1a85edbe95448b48ebc13b09c192',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S2:AREA:mansion_import_0__CoffinRoom', 'S3:AREA:mansion_import_2__ChurchBellTower', 'S4:AREA:mansion_import_1__ChurchBellTower'),
    ),

    'Blank Scroll': RandomizedItemData(
        key=269,
        guid='8f0cce130af86334ea0ef433acc30cd1',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Boat Pass': RandomizedItemData(
        key=270,
        guid='36b08b91f3e79de46b1fb30336857314',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Boatman Purchase 1',
        viable_region_keys=('S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock'),
    ),

    'Bone Ash': RandomizedItemData(
        key=271,
        guid='7bd63485952d3cd4583719ebd2dc05b0',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Broken Shotgun': RandomizedItemData(
        key=272,
        guid='b765e38b3dbdebe45a21dc56bc20e918',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Bronze Finger': RandomizedItemData(
        key=273,
        guid='746ea404555deb444931cc560761f3cb',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Duwern Burial Ground Map': RandomizedItemData(
        key=274,
        guid='e464cd399717647499b553aa31aa6987',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Circus Prize Ticket': RandomizedItemData(
        key=275,
        guid='1f939494f405f8845a1dcbab622743ab',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Circus Ticket': RandomizedItemData(
        key=276,
        guid='ae08cf165d334b04cac9894e8b2e35f6',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Coin Purse': RandomizedItemData(
        key=277,
        guid='3fb5bc4d3132e63448a9d1a4b4c6f1fe',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Cursed Grimoire': RandomizedItemData(
        key=278,
        guid='bae272b2e9131d94b96462db44711f91',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'First Angel Kindling': RandomizedItemData(
        key=279,
        guid='f98a2c3a72056164abc51339f8ff13a5',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'First Angel Map': RandomizedItemData(
        key=280,
        guid='3ea3dd9741566e04eb3b8c4ae0392542',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Gun Powder': RandomizedItemData(
        key=281,
        guid='308a18b849fe9614fb0a4dcc1a687174',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Gunsmith Kit': RandomizedItemData(
        key=282,
        guid='2bac89f17ee79f74fad33ed21329aedd',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Blank Initiate Book': RandomizedItemData(
        key=283,
        guid='508778659f929134e847a6cabb95e8fa',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Initiate's Grimoire": RandomizedItemData(
        key=284,
        guid='759336cc0f2cec04783c0017f2431ba7',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Advanced Lab Manual': RandomizedItemData(
        key=285,
        guid='d19d4c895ce08bc4784ddf6a29da2798',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Organ Chamber Safe Puzzle',
        viable_region_keys=('S2:ROOM:062ae9bea49cd3e49b7f617a5533b9c1',),
    ),

    'Basic Lab Manual': RandomizedItemData(
        key=286,
        guid='2a9a49cb74e54774ba5e2896442c9c4d',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493',),
    ),

    'Grease Lab Manual': RandomizedItemData(
        key=287,
        guid='d2566b829764a1848a9805cfb07c078a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Rakesh's Diary": RandomizedItemData(
        key=288,
        guid='07df8bfde55c6204b89ae5191dd6606c',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Mark of Sin': RandomizedItemData(
        key=289,
        guid='5d12a53681878ce409410de626439d94',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Medicinal Herbs': RandomizedItemData(
        key=290,
        guid='c6ab33b7478837946b05f5b090d44e94',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Ancient Blood': RandomizedItemData(
        key=291,
        guid='6c09cb12358c3414a8e193e10409732e',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Corrupted Finger': RandomizedItemData(
        key=292,
        guid='55789e69d995cdc44868fa2b1feec995',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Corrupted Heart': RandomizedItemData(
        key=293,
        guid='77f2e623f1a919a4e92c3de6e5e163af',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Corrupted Liver': RandomizedItemData(
        key=294,
        guid='471f3bbfc41aea74785ce2edac15941c',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Curse Sentinel Candle': RandomizedItemData(
        key=295,
        guid='f4f3b18c79d58b1459d5a8440b0ac16b',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Dream Essence': RandomizedItemData(
        key=296,
        guid='2b5918a2f3a52fe49a8fbdab9982de51',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Human Finger': RandomizedItemData(
        key=297,
        guid='c8700e822fed1fe408f1d4a31cc40432',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Nightingale Bones': RandomizedItemData(
        key=298,
        guid='d0cfab7285c80d744970d4d5c89c4aa6',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Spectral Remains': RandomizedItemData(
        key=299,
        guid='c7fe77d9d3c1f5941a3e7cbd216e3800',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Organ Grease': RandomizedItemData(
        key=300,
        guid='3bb3995c1342a534caf40f8d1b3de11c',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Witch Ashes': RandomizedItemData(
        key=301,
        guid='213f03d748f2fad42929ea5ff2648fd2',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Paralysis Leaf': RandomizedItemData(
        key=302,
        guid='6f58f3e056b444045982b6d3a7cfbed2',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Photographic Dry Plate': RandomizedItemData(
        key=303,
        guid='b2e89246819a058469e2329f33870381',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Photograph': RandomizedItemData(
        key=304,
        guid='dbf4f375283de3942ac3a4417caca53e',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Blood Stained Letter': RandomizedItemData(
        key=305,
        guid='c214b613e3e0d344a9c42e30a0db3263',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Idol Tainted Heart': RandomizedItemData(
        key=306,
        guid='a475597e37db10e499f7ab5de31d1e31',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    "Rose's Diary": RandomizedItemData(
        key=307,
        guid='7b3eef4337dbaac44bdff846600aa71d',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Poison Leaf': RandomizedItemData(
        key=308,
        guid='e8882cbe92586aa40b24271877004063',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Audio Command Wax Cylinder': RandomizedItemData(
        key=309,
        guid='74b869c65c6799a4fb84127bb27b44ec',
        classification=ItemClassification.progression,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Remembrance Tear': RandomizedItemData(
        key=310,
        guid='f9963d2cb930848499dde457be80671a',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Scrap Metal': RandomizedItemData(
        key=311,
        guid='faafdddb70ac08f44b65c99045bcd6ac',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Starry Grimoire': RandomizedItemData(
        key=312,
        guid='a6bf6212e624b6c44ae4ee96b24a3556',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Starry Remembrance Tear': RandomizedItemData(
        key=313,
        guid='95dc386e9ca92f947a2795e8e2f138b2',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Strange Coin': RandomizedItemData(
        key=314,
        guid='450742c721bfc3d41aa6c90c6763a7cc',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Sulphuric Acid': RandomizedItemData(
        key=315,
        guid='6ebbd5e16da5ff5489af837b4532fb1e',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Trickster Medal': RandomizedItemData(
        key=316,
        guid='52624890009918245b7befa41c239227',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:d16f239e499149b44a43c2c0c1708e84',),
    ),

    'Village Token': RandomizedItemData(
        key=317,
        guid='1aa44765b12fe3b49972aa689be2ff72',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Black Wax': RandomizedItemData(
        key=318,
        guid='21b8d6b67868ee44da6902118d83f64b',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Blue Wax': RandomizedItemData(
        key=319,
        guid='3675f6c3bcd496c43a20e07f015782d4',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Green Wax': RandomizedItemData(
        key=320,
        guid='3a7246809a1209b4c91a8e79b25de136',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Orange Wax': RandomizedItemData(
        key=321,
        guid='8719f901f02aceb40a85ac4f88e39c70',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Purple Wax': RandomizedItemData(
        key=322,
        guid='731af5d6590936f4e8d38cfd1dd67e4a',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Red Wax': RandomizedItemData(
        key=323,
        guid='d7fbf1c508dd12d44a9ccc67e8b937ec',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'White Wax': RandomizedItemData(
        key=324,
        guid='370a04a0e699b974b8673c93a6e7e7d9',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Yellow Wax': RandomizedItemData(
        key=325,
        guid='f638bd307c7f4524489656c2d581e6f4',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Labyrinth Organ Chamber Upgrade': RandomizedItemData(
        key=326,
        guid='c99876c3752a5944b8595554ed77215b',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054'),
    ),

    'Organ Chamber Upgrade': RandomizedItemData(
        key=327,
        guid='a003ff7a9f11eea498d720c32e226ce0',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Skeleton Merchant Purchase 1',
        viable_region_keys=('S3:AREA:mansion_import_2__Nowhere', 'S4:AREA:mansion_import_1__Nowhere'),
    ),

    'Advanced Organ Chamber Upgrade': RandomizedItemData(
        key=328,
        guid='b938d2fe17372ba4f9829c6a93a3bdca',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:4a81144fa467b92469f748262217b4dc'),
    ),

    'Bloody Thread': RandomizedItemData(
        key=329,
        guid='0a59935db03f75f4d930e99c813c099d',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Arcane Salts': RandomizedItemData(
        key=330,
        guid='42e3ff9953f6eb245a240602bf3bbabd',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Weapon Upgrade Kit': RandomizedItemData(
        key=331,
        guid='bc5a272db8f4c95499d61a0e61f894fa',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Book of Burdens': RandomizedItemData(
        key=332,
        guid='4a97077027aed8545bccbe878ff58864',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Bloody Bell': RandomizedItemData(
        key=333,
        guid='add64c1791b32c944973800173a61408',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOT', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOT'),
    ),

    "Initiate's Candlestick": RandomizedItemData(
        key=334,
        guid='0300b27548b95e545980b33363220530',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:AREA:mansion_AtticCloseHall', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
    ),

    "Apprentice's Candlestick": RandomizedItemData(
        key=335,
        guid='955f7db3f59109942a664f719ab4eae4',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S2:AREA:mansion_UpperBalcony', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Creepy Doll': RandomizedItemData(
        key=336,
        guid='057b3f7ce32b23541bb9e1471e13671b',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    '"Drink Me" Potion': RandomizedItemData(
        key=337,
        guid='5d86c2bf430dd414091ae78dcdbe14ab',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    '"Eat Me" Cake': RandomizedItemData(
        key=338,
        guid='4d6c751db604f274ab74759037297188',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Erasure Ritual': RandomizedItemData(
        key=339,
        guid='d5bb23564b627484ebf2b87fb1a840c4',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Organ Chamber Discovery',
        viable_region_keys=('S2:ROOM:062ae9bea49cd3e49b7f617a5533b9c1',),
    ),

    'Dog Whistle': RandomizedItemData(
        key=340,
        guid='560cccd8f1e05f64d8db1b30f56448c3',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Cholera Patient Head': RandomizedItemData(
        key=341,
        guid='b87f7bb4ecea3de45b616e129e8fa9af',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_0__CholeraHallway', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:AREA:mansion_import_2_import_0__CholeraHallway', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6'),
    ),

    'Pocket Mirror': RandomizedItemData(
        key=342,
        guid='204657f494970cb44a72f26f418a80d2',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Portable Crafting Kit': RandomizedItemData(
        key=343,
        guid='1178ac622fd056b4faf7d5c5d0efb5e2',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Pottery Shard': RandomizedItemData(
        key=344,
        guid='1a5a9b13db7c2394ab67233ec605246e',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Safe Room Twig': RandomizedItemData(
        key=345,
        guid='d6aaa1910458bc74d9ab2c36e4d0891c',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Spirit Twig': RandomizedItemData(
        key=346,
        guid='aa17660c48d93d14e8fa5c2fd0b54818',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Spirit Branch': RandomizedItemData(
        key=347,
        guid='17701339ddb08214faaa747a174ed695',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_AtticCloseHall', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__Speakeasy', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__Speakeasy', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticCloseHall', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Camera': RandomizedItemData(
        key=348,
        guid='7c69aefc3ee0f864687fac77df040d43',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Skeleton Merchant Purchase 2',
        viable_region_keys=('S3:AREA:mansion_import_2__Nowhere', 'S4:AREA:mansion_import_1__Nowhere'),
    ),

    'Bayonet': RandomizedItemData(
        key=349,
        guid='1f479579822c284499976d940e0646ee',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:177e80995678556489ddd11b5be5a982', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:177e80995678556489ddd11b5be5a982', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Bloody Dao': RandomizedItemData(
        key=350,
        guid='0292899c079286d46b42683dd372378c',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override='Blood Tower First Floor Discovery 1',
        viable_region_keys=('S4:AREA:mansion_BTFirstFloor',),
    ),

    'Grenade': RandomizedItemData(
        key=351,
        guid='746a96ac2486b44488550fc310600cc4',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Tesla Coil Mace': RandomizedItemData(
        key=352,
        guid='87359e0cbf5daa744bf6f75aeb3f922d',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_import_2__ChurchBasement', 'S4:AREA:mansion_import_1__ChurchBasement'),
    ),

    "Night Mother's Blade": RandomizedItemData(
        key=353,
        guid='33ecd5dff8d20d3428fac3417f2cf2f9',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Shotgun': RandomizedItemData(
        key=354,
        guid='7d5bdd16998187e40b1f7b166c27027f',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Shotgun Shell': RandomizedItemData(
        key=355,
        guid='6152ee2d116c4034da72a299d0f6c734',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Empty Shotgun Shell': RandomizedItemData(
        key=356,
        guid='231fe325302fb1147a4519adfe2af7fd',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    '.455 Webley Bullet': RandomizedItemData(
        key=357,
        guid='326db830b0afd804091f49a6d554e9eb',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Webley Mk. VI': RandomizedItemData(
        key=358,
        guid='bdfe4b3881964fc4a944e1d6981ecb57',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Pipe': RandomizedItemData(
        key=359,
        guid='295d59b23990f614bbf1ad5b9d59e570',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:177e80995678556489ddd11b5be5a982', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:177e80995678556489ddd11b5be5a982', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Axe': RandomizedItemData(
        key=360,
        guid='04fb20bb10aec284491a0588051f57c9',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:177e80995678556489ddd11b5be5a982', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:177e80995678556489ddd11b5be5a982', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Cleaver': RandomizedItemData(
        key=361,
        guid='5a16e815369b7bc4c8e385f27c15cf82',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Flaming Grease': RandomizedItemData(
        key=362,
        guid='c82ec7dd7b394af469ac73bd7703870e',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Poison Grease': RandomizedItemData(
        key=363,
        guid='3192764001d73634ea3f30c58d35ea0f',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Cutting Grease': RandomizedItemData(
        key=364,
        guid='48a7af44497718148a8924e97a6593ed',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Firework': RandomizedItemData(
        key=365,
        guid='22caa4735077aa74ca2a6fa30bddab6a',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Sickle': RandomizedItemData(
        key=366,
        guid='dde6988e84a2f7c42a4033ae1a040ff7',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT'),
    ),

    'Old Sword': RandomizedItemData(
        key=367,
        guid='b812dea5c2199ed4cb38460a0713c7e2',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT'),
    ),

    'Scythe': RandomizedItemData(
        key=368,
        guid='2ae667425bb5f8e47beb9ae7211d83b7',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOT', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOT'),
    ),

    'Golden Spear': RandomizedItemData(
        key=369,
        guid='d7c0760c8fd06084b8014775fcb2b903',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT'),
    ),

    'Knife': RandomizedItemData(
        key=370,
        guid='1d472eb78b3f71645b05f7f337331955',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S1:AREA:mansion_Hallway', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:658bb443034365f4f95d8300d22e20e8', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S1:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S1:ROOT', 'S2:AREA:mansion_UpperBalcony', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:658bb443034365f4f95d8300d22e20e8', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c555058a3ee200f4e9b383dd59c27fcb', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:fab4efe66fa3f5242a47eda9b42f3347', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOT', 'S3:AREA:mansion_AtticEastStairwell', 'S3:ROOM:177e80995678556489ddd11b5be5a982', 'S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:bc560941b4184f847bf3883b06374596', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:177e80995678556489ddd11b5be5a982', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:bc560941b4184f847bf3883b06374596', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:d2e521f0e59f1bd41bade9b08c1a7b64', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S8:ROOM:714150db49d065f46a10c44f71bedad3', 'S9:ROOM:9b0e1ee388cc25640af9a3da47a45dac'),
    ),

    'Rapier': RandomizedItemData(
        key=371,
        guid='e6c4816ecefffd849baa6c9dffe9d069',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:177e80995678556489ddd11b5be5a982', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:177e80995678556489ddd11b5be5a982', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Throwing Knife': RandomizedItemData(
        key=372,
        guid='84afb6062ce9d5945811298c6774399b',
        classification=ItemClassification.filler,
        creates_location=False,
        include_in_pool=True,
        unique_in_pool=False,
        repeatable_filler=True,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Torch': RandomizedItemData(
        key=373,
        guid='7551c369a79167745a7019b75546fa24',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:177e80995678556489ddd11b5be5a982', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:177e80995678556489ddd11b5be5a982', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Whip': RandomizedItemData(
        key=374,
        guid='9f7f8fdd319db344aa07c3623182ff78',
        classification=ItemClassification.useful,
        creates_location=True,
        include_in_pool=True,
        unique_in_pool=True,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=('S2:AREA:mansion_UpperBalcony', 'S2:AREA:mansion_import_0__Nowhere', 'S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:a9a2e274a103a9e4d9a96cc91eaa62ff', 'S2:ROOM:ba55108c9186809438df7c41e6072178', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:d7d694fb5f60763428690238f4ce0839', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S2:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:AREA:mansion_AtticEastStairwell', 'S3:AREA:mansion_import_2__Burial', 'S3:AREA:mansion_import_2__EastForestDock', 'S3:AREA:mansion_import_2__FirstAngel', 'S3:AREA:mansion_import_2__Nowhere', 'S3:AREA:mansion_import_2__SwampBoatLeft', 'S3:AREA:mansion_import_2__SwampBoatRight', 'S3:AREA:mansion_import_2__SwampDock', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:177e80995678556489ddd11b5be5a982', 'S3:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S3:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:a9cbd07a936154f43b868686c45ec054', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S3:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S3:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S3:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S3:ROOT', 'S4:AREA:mansion_import_1__Burial', 'S4:AREA:mansion_import_1__EastForestDock', 'S4:AREA:mansion_import_1__FirstAngel', 'S4:AREA:mansion_import_1__Nowhere', 'S4:AREA:mansion_import_1__SwampBoatLeft', 'S4:AREA:mansion_import_1__SwampBoatRight', 'S4:AREA:mansion_import_1__SwampDock', 'S4:AREA:mansion_import_2__AtticEastStairwell', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:177e80995678556489ddd11b5be5a982', 'S4:ROOM:29faf4f4bef9bf64fac5cae13e238d51', 'S4:ROOM:31bb9022ed7e45949a7329d4621988b5', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7ad7c84ebeacfd4498e4a107c5ed7c96', 'S4:ROOM:7eb4f691cb94b7143a9b40f6bb69bbc0', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:a9cbd07a936154f43b868686c45ec054', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:cdeab43c9f21ebe4783c685e34404c63', 'S4:ROOM:cf6306dbc9ed022499fb5829f934e9a5', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:de703ddba4a2aae468ba765115c23a8b', 'S4:ROOM:dfa842cb97bc7e24fb2ad3974af63777', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:fef3beeb2fd01454aaddc1bdf3b2ec56', 'S4:ROOT', 'S6:ROOM:83b55f07665f4664882449ad3a6a013a'),
    ),

    'Violence': RandomizedItemData(
        key=375,
        guid='bac564db57b14474c99eecf65449bf60',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Dexterity': RandomizedItemData(
        key=376,
        guid='01b7b23a340555042859eedd701a9b22',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Weirdness': RandomizedItemData(
        key=377,
        guid='a54c78d4df7532640926c3c29ee7e10f',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Ascend': RandomizedItemData(
        key=378,
        guid='f1b3ecff40c31e6428af91392483c91f',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Warding': RandomizedItemData(
        key=379,
        guid='1e6e6189970624042b1f3846f06f3edd',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Vigor': RandomizedItemData(
        key=380,
        guid='b4e4f9b8e71ef644db0fa1328453d0f4',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Fortune': RandomizedItemData(
        key=381,
        guid='262a2da694001ac4795d0f36b6c806c7',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Fortitude': RandomizedItemData(
        key=382,
        guid='11364c5347334a843a7eb702430220a5',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Immunity': RandomizedItemData(
        key=383,
        guid='da31c7dabb490a444bbf1b7b2b9f3e6f',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),

    'Agility': RandomizedItemData(
        key=384,
        guid='7bfa1ab0967fbd34baa026ef06519fd4',
        classification=ItemClassification.useful,
        creates_location=False,
        include_in_pool=False,
        unique_in_pool=False,
        repeatable_filler=False,
        location_name_override=None,
        viable_region_keys=(),
    ),








}

LORE_LOCATIONS: dict[str, LoreLocationData] = {



    # AUTO-GENERATED FROM lore.csv
    # Paste into LORE_LOCATIONS.

    'Read Gazette, June 8th, 1910': LoreLocationData(
        key=1,
        guid='fa8fb4a09429d6847a52ac806edbdd2d',
        viable_region_keys=('S3:ROOM:035e4019a5fce0842830813a97db605a', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:035e4019a5fce0842830813a97db605a', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Gazette, September 2nd, 1915': LoreLocationData(
        key=2,
        guid='d23d266803fa49144ba1389f8a16a679',
        viable_region_keys=('S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Gazette, January 15, 1895': LoreLocationData(
        key=3,
        guid='7666a04d9005fb24caef6eeb1e2147a1',
        viable_region_keys=('S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Gazette, July 20th, 1916': LoreLocationData(
        key=4,
        guid='e674a7cd52210d040995cc96e22962c5',
        viable_region_keys=('S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Expedition Notes 1': LoreLocationData(
        key=5,
        guid='57ef5fb858252f8458bc67cc78fcfc9c',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Read Expedition Notes 2': LoreLocationData(
        key=6,
        guid='bf98b13e007d49d4e815a0b45183c8c3',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Read Expedition Notes 3': LoreLocationData(
        key=7,
        guid='14f710a778fa7ab40bb270cf646d5599',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Read Case Notes 1': LoreLocationData(
        key=8,
        guid='b66229e598b12c7458db97eb5c4954e3',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493'),
        progression_allowed=True,
    ),

    'Read Case Notes 2': LoreLocationData(
        key=9,
        guid='b6229a9f44dcda84cae1b53fb63530b2',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493'),
        progression_allowed=True,
    ),

    'Read Case Notes 3': LoreLocationData(
        key=10,
        guid='3176e07356419ef4eb2bf4e51b9156aa',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493'),
        progression_allowed=True,
    ),

    'Read Gatehouse Key': LoreLocationData(
        key=11,
        guid='370c390c95936f645be297e9bde82a5c',
        viable_region_keys=('S0:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4'),
        progression_allowed=True,
    ),

    'Read Special Placement Log': LoreLocationData(
        key=12,
        guid='1d466c305a473f349a785445e3cf0056',
        viable_region_keys=('S0:ROOM:133e8a902fbe4cd489588321c6220496', 'S2:ROOM:133e8a902fbe4cd489588321c6220496'),
        progression_allowed=True,
    ),

    'Read Mostyn House Map': LoreLocationData(
        key=13,
        guid='f064c4007d9c61b44895ccf2052190df',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    "Read Disciple's Path": LoreLocationData(
        key=14,
        guid='8a303dd7b1afcec4790845393f686fbd',
        viable_region_keys=('S3:ROOM:26fd6bb2fdd05824c9eb24801d5785b9', 'S4:ROOM:26fd6bb2fdd05824c9eb24801d5785b9'),
        progression_allowed=True,
    ),

    'Read Ode to a Nightingale': LoreLocationData(
        key=15,
        guid='928634c124cbd9049a9fc247c15ce45e',
        viable_region_keys=('S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6'),
        progression_allowed=True,
    ),

    "Read Outcast's Diary, 1916": LoreLocationData(
        key=16,
        guid='6ae264750e37d0c4d81c1abb611d26cf',
        viable_region_keys=('S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S3:ROOM:f93edcdc13b40e24c84122a5b36254f6', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:f93edcdc13b40e24c84122a5b36254f6'),
        progression_allowed=True,
    ),

    "Read Father's Letter": LoreLocationData(
        key=17,
        guid='e1975b50877ff61418c856da1a690c4d',
        viable_region_keys=('S5:ROOM:5d82d41c31d490c44a9d3c0e4eadf5ae',),
        progression_allowed=True,
    ),

    'Read The Feast': LoreLocationData(
        key=18,
        guid='c02a399fe9ea70f4c92a287064ba0785',
        viable_region_keys=('S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366',),
        progression_allowed=True,
    ),

    'Read About Beca': LoreLocationData(
        key=19,
        guid='80b9c5012e8855e4b9b19bbceffc3076',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Read To Father': LoreLocationData(
        key=20,
        guid='2f0a7e1371bd0944ea8e0d8e6f2fa14a',
        viable_region_keys=('S4:ROOM:aa2ea50e664bfb94dba39a36ae0985a7',),
        progression_allowed=True,
    ),

    'Read Welcome to the Blood Tower': LoreLocationData(
        key=21,
        guid='bb77f20eb80b3934f8a33c543cdb21ba',
        viable_region_keys=('S4:ROOM:9a3947e53f0047b4b80379e7cd902a2c',),
        progression_allowed=True,
    ),

    'Read Welsh Country Houses 1': LoreLocationData(
        key=22,
        guid='e5e3ffeee48d91540bdee7b1422f722a',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    'Read Welsh Country Houses 2': LoreLocationData(
        key=23,
        guid='7a9e9069df960854d99ebc4744f6d2e4',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    'Read Welsh Country Houses 3': LoreLocationData(
        key=24,
        guid='ea5a7aa8157b1f54a89b5f23040996c3',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    'Read Welsh Country Houses 4': LoreLocationData(
        key=25,
        guid='af4fb766fb0f67f4fae9a9fed474d7bf',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    'Read Welsh Country Houses 5': LoreLocationData(
        key=26,
        guid='8adfb1582bb0bab4aa7998a245f3ddb5',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    'Read Welsh Country Houses 6': LoreLocationData(
        key=27,
        guid='bc4ea5d2098e603449b84d0496b9d220',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    'Read Welsh Country Houses 7': LoreLocationData(
        key=28,
        guid='3e626afb3171f974d935bf96c6a735cd',
        viable_region_keys=('S3:ROOM:4946ce2c8d5ba0c4c94386976c6c2bd1', 'S3:ROOM:124780ac826cdad48a31357559193cea', 'S3:ROOM:bb51714b3c1a52b478da0dc7fd29494c', 'S3:ROOM:f6506e24711de724a825ad8458fe6f56', 'S3:ROOM:f8fcc9a46a69dae4c8543a2b2de6e901', 'S3:ROOM:9dd22a6334af8b145af89e43a2ed6926', 'S3:ROOM:cc056cc7b6ba10747821280e91f7edfe', 'S3:ROOM:8d662b96f10d0824c8b3091b07d57038', 'S3:ROOM:c58a98c089b5e4048847b5b46c220a6f', 'S3:ROOM:e5d782c6f82204942886a77e3c23379e', 'S3:ROOM:87b7d0bdd928d8243a8095e121dcb981', 'S3:ROOM:b20962f013be0c04bb1cc6171abff10e', 'S4:ROOM:4946ce2c8d5ba0c4c94386976c6c2bd1', 'S4:ROOM:124780ac826cdad48a31357559193cea', 'S4:ROOM:bb51714b3c1a52b478da0dc7fd29494c', 'S4:ROOM:f6506e24711de724a825ad8458fe6f56', 'S4:ROOM:f8fcc9a46a69dae4c8543a2b2de6e901', 'S4:ROOM:9dd22a6334af8b145af89e43a2ed6926', 'S4:ROOM:cc056cc7b6ba10747821280e91f7edfe', 'S4:ROOM:8d662b96f10d0824c8b3091b07d57038', 'S4:ROOM:c58a98c089b5e4048847b5b46c220a6f', 'S4:ROOM:e5d782c6f82204942886a77e3c23379e', 'S4:ROOM:87b7d0bdd928d8243a8095e121dcb981', 'S4:ROOM:b20962f013be0c04bb1cc6171abff10e'),
        progression_allowed=True,
    ),

    'Read Boiler Room Note': LoreLocationData(
        key=29,
        guid='feca8e21b81517745b9bb344620ff6a8',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285'),
        progression_allowed=True,
    ),

    'Read Cagewood Memorial': LoreLocationData(
        key=30,
        guid='ba82b8360b4af8c489f7510ab7c242ed',
        viable_region_keys=('S3:ROOM:358bfb18e3f56f148829927580e06851', 'S4:ROOM:358bfb18e3f56f148829927580e06851'),
        progression_allowed=True,
    ),

    'Read Hedge Maze Shopping List': LoreLocationData(
        key=31,
        guid='174a4f23eb4ee5f45a417e4a215ac66a',
        viable_region_keys=('S1:ROOM:7f899b6da02c7104abaac94492f8a0b7', 'S2:ROOM:7f899b6da02c7104abaac94492f8a0b7'),
        progression_allowed=True,
    ),

    'Read Hunting Guide': LoreLocationData(
        key=32,
        guid='0002b52d6382d004da8e2cbe865632d3',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Read drsfenechod oanjiire': LoreLocationData(
        key=33,
        guid='fdebc0eae21609a4b86fa242641b56c0',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Read Wrong Room': LoreLocationData(
        key=34,
        guid='19131a9cbb539024a9aa27148cdb3956',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493'),
        progression_allowed=True,
    ),

    'Read Outcast’s Diary, 1885': LoreLocationData(
        key=35,
        guid='7e3b0a890c1d41840946c0a3b123d379',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493'),
        progression_allowed=True,
    ),

    "Read Outcast's Diary, 1886": LoreLocationData(
        key=36,
        guid='3ecc8396a189ef845bd51d1e5313f21b',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493'),
        progression_allowed=True,
    ),

    "Read Outcast's Diary, 1887": LoreLocationData(
        key=37,
        guid='5bea87b63046e0d4d96cd63991e57bc0',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S1:ROOM:7f0caea353b0644468542a538ef5940a', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S1:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:68e5dd6d1531c7e478b10d98f1aa7701', 'S2:ROOM:7f0caea353b0644468542a538ef5940a', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:c66aed44f2688de4d8c089ecf44177fd', 'S2:ROOM:d29fc8753acdcb140b1cd3efb2e6cb75', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493'),
        progression_allowed=True,
    ),

    'Read Part I': LoreLocationData(
        key=38,
        guid='6eed845124391a94791b733757f2d5ad',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    "Read Poncer's Chess 1": LoreLocationData(
        key=40,
        guid='f52f902abb3ab954cbcce7c00f12cd84',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    "Read Poncer's Chess 2": LoreLocationData(
        key=41,
        guid='69da986c18337a244aa857e6aee9694f',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    "Read Poncer's Chess 3": LoreLocationData(
        key=42,
        guid='2f080248d6fc4d945b66fc0aaa53c1d7',
        viable_region_keys=('S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    "Read Priscilla's Dream Histories 1": LoreLocationData(
        key=43,
        guid='9786027b3dba58d4b983443f4b961844',
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    "Read Priscilla's Dream Histories 2": LoreLocationData(
        key=44,
        guid='831cc516808f7144cb1e2672a7a81910',
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    "Read Priscilla's Dream Histories 3": LoreLocationData(
        key=45,
        guid='95d8efd72fcc48948a6d41f09cab5819',
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    "Read Priscilla's Storage Note": LoreLocationData(
        key=46,
        guid='9034636f7163f1640b9291159d732757',
        viable_region_keys=('S2:ROOM:c8f4efab99e398344a28df1ed57e3d6b',),
        progression_allowed=True,
    ),

    'Read Blood Tower Schematic': LoreLocationData(
        key=47,
        guid='7d8b6160ec83ef741939996a1010be7c',
        viable_region_keys=('S1:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S2:ROOM:ff20e4731ebfba04794ea5cee1ea7493', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366'),
        progression_allowed=True,
    ),

    'Read Research Avenues': LoreLocationData(
        key=48,
        guid='ed317ef177557f346aab32c81f972980',
        viable_region_keys=('S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366',),
        progression_allowed=True,
    ),

    'Read Lab Notes': LoreLocationData(
        key=49,
        guid='0d23c6ca6c56a4e489ad941a74a2f9de',
        viable_region_keys=('S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:44a0b846306655242a084161bd97a1ab', 'S3:ROOM:8aca0ad5386797d4eab3a10db3f603fd', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:44a0b846306655242a084161bd97a1ab', 'S4:ROOM:8aca0ad5386797d4eab3a10db3f603fd'),
        progression_allowed=True,
    ),

    'Read Memorandum': LoreLocationData(
        key=50,
        guid='039648b950bf4334492e252d6f72c2ce',
        viable_region_keys=('S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:44a0b846306655242a084161bd97a1ab', 'S3:ROOM:8aca0ad5386797d4eab3a10db3f603fd', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:44a0b846306655242a084161bd97a1ab', 'S4:ROOM:8aca0ad5386797d4eab3a10db3f603fd'),
        progression_allowed=True,
    ),

    'Read To Robert': LoreLocationData(
        key=51,
        guid='496f78da1f24ee34caee561b5943c8c3',
        viable_region_keys=('S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366',),
        progression_allowed=True,
    ),

    'Read Wiring Requirements': LoreLocationData(
        key=52,
        guid='a60908674dbdba94a8517baac5b84b88',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Read Philosophiae Somnium 1': LoreLocationData(
        key=53,
        guid='89f07ea47fe508b4299512b1785d1828',
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Philosophiae Somnium 2': LoreLocationData(
        key=54,
        guid='d6732e5c15ac77c4594be2368bfecc2c',
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Philosophiae Somnium 3': LoreLocationData(
        key=55,
        guid='51de3d30ffc1eb8419b1d1d87f34d31a',
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877', 'S2:ROOM:269ddde7338be024ebdee99c72c5d08c', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:c77f57149972f5d41988df3954cb2ec1', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Philosophiae Somnium 4': LoreLocationData(
        key=56,
        guid='c0cbaab1e1fdc1c4c969b0e626cc862d',
        viable_region_keys=('S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Philosophiae Somnium 5': LoreLocationData(
        key=57,
        guid='889b54510d4ddfa4c88448e68c5d9d93',
        viable_region_keys=('S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Philosophiae Somnium 6': LoreLocationData(
        key=58,
        guid='301f50f354169f440be1d551f0670d5f',
        viable_region_keys=('S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read Bloody Letter': LoreLocationData(
        key=59,
        guid='f4c6bcd3f3051564293de122df06c1a6',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Read To Wretch': LoreLocationData(
        key=60,
        guid='9e744b6fc0b20294594b128dad40d860',
        viable_region_keys=('S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:4701166c9b412f34cad491a232827334', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:4701166c9b412f34cad491a232827334', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:7f07cf71649aede4d9518d0282dae7b7', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:87ba22aabf3ef06409652a1df942d33c', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:e780c42ddf3f66b4b92aa3432af6d0f4', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Read To Nightingale': LoreLocationData(
        key=61,
        guid='42b61640bb8bec8409c790155d0af007',
        viable_region_keys=('S2:ROOM:d7d694fb5f60763428690238f4ce0839',),
        progression_allowed=True,
    ),

    'Read Organ Processing Note': LoreLocationData(
        key=62,
        guid='f99446b3fae54c8478cf60f074354424',
        viable_region_keys=('S2:ROOM:062ae9bea49cd3e49b7f617a5533b9c1',),
        progression_allowed=True,
    ),

    'Read To the First Witch': LoreLocationData(
        key=63,
        guid='cc1c78804df493b48a436a004ee41590',
        viable_region_keys=('S2:ROOM:935ecafeead9e3640ba5c4530bf373d6',),
        progression_allowed=True,
    ),

    'Read Inscription': LoreLocationData(
        key=64,
        guid='05bed47101f878743a241650adb25ebf',
        viable_region_keys=('S1:ROOM:c3c7869b2d5e4b54ab0435736cf75408',),
        progression_allowed=True,
    ),

    'Read Priscilla Mostyn': LoreLocationData(
        key=65,
        guid='033bedfa81a381f42b4859dc6edc04ab',
        viable_region_keys=('S1:ROOM:2bf2226d4f4d0ea499f8eefdce0b01da', 'S2:ROOM:285d223bbd79fe5479419e03c71995ff'),
        progression_allowed=True,
    ),

    'Read Peter Mostyn': LoreLocationData(
        key=66,
        guid='8b5697b4aab55cb418d42f65fbd2da79',
        viable_region_keys=('S1:ROOM:2bf2226d4f4d0ea499f8eefdce0b01da', 'S2:ROOM:285d223bbd79fe5479419e03c71995ff'),
        progression_allowed=True,
    ),

    'Read Alfred Mostyn': LoreLocationData(
        key=67,
        guid='43e32d847f5a7a047a0a1dd62cc790c3',
        viable_region_keys=('S1:ROOM:2bf2226d4f4d0ea499f8eefdce0b01da', 'S2:ROOM:285d223bbd79fe5479419e03c71995ff'),
        progression_allowed=True,
    ),

    'Read Anne Mostyn': LoreLocationData(
        key=68,
        guid='71d2094420372c04ea3040bafa6ac3a7',
        viable_region_keys=('S1:ROOM:2bf2226d4f4d0ea499f8eefdce0b01da', 'S2:ROOM:285d223bbd79fe5479419e03c71995ff'),
        progression_allowed=True,
    ),

    'Read Spirits: Theory & Practice 1': LoreLocationData(
        key=69,
        guid='190a597540163cf4b9d9cad974ca9a31',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    'Read Spirits: Theory & Practice 2': LoreLocationData(
        key=70,
        guid='ad5bb440faa989b429dc98c973404990',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    'Read Combat Training Procedure': LoreLocationData(
        key=71,
        guid='627640c1fdfd3e74f8e3d75e79166157',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Read Tactics Manual': LoreLocationData(
        key=72,
        guid='b17bf26f8b5bab9489412e00d1aa97b6',
        viable_region_keys=('S1:ROOM:051cb404d950e9d42b3c5425079cbaaa', 'S2:ROOM:051cb404d950e9d42b3c5425079cbaaa'),
        progression_allowed=True,
    ),

    'Read The Horrors of Messina': LoreLocationData(
        key=75,
        guid='81fa1f9c9b986584685e7ad19ba18c66',
        viable_region_keys=(),
        progression_allowed=False,
    ),





}

MONSTER_LOCATIONS: dict[str, MonsterLocationData] = {

    'Defeat Beast Nightingale': MonsterLocationData(
        key=1,
        guid='b2044414e03716f42966c1f79a49e083',
        viable_region_keys=('S3:ROOM:92c3a57034feac94caf31db1ae296ee2', 'S4:ROOM:92c3a57034feac94caf31db1ae296ee2'),
        progression_allowed=True,
    ),

    'Defeat Butcher Surgeon': MonsterLocationData(
        key=2,
        guid='93706b45b7134af4ba2a64573e3147a8',
        viable_region_keys=('S1:ROOM:8bb5ddfba2ed94045994524da6dd9653',),
        progression_allowed=True,
    ),

    'Defeat Night Mother Disciple': MonsterLocationData(
        key=3,
        guid='079a4a217ddd20e40b61458bb0c6ee1c',
        viable_region_keys=('S3:ROOM:ea14c71acead82e46bb18ccdde0e1024', 'S4:ROOM:ea14c71acead82e46bb18ccdde0e1024'),
        progression_allowed=True,
    ),

    'Defeat Millie Erwood (Amalgamation)': MonsterLocationData(
        key=4,
        guid='d2e0a222769853d4c8bc1bc58c827842',
        viable_region_keys=('S2:ROOM:9b0e1ee388cc25640af9a3da47a45dac',),
        progression_allowed=True,
    ),

    'Defeat Priscilla Mostyn': MonsterLocationData(
        key=5,
        guid='01ddaaf8d4565dc4cb95742a922c1dae',
        viable_region_keys=('S4:ROOM:0d4c5d7aa3a6101429767f340ec797fe',),
        progression_allowed=True,
    ),

    'Defeat Graverider': MonsterLocationData(
        key=6,
        guid='c73bf444b48a8ba458fb433d53200719',
        viable_region_keys=('S3:ROOM:4fc426c644a0fbf43b47040378138b91', 'S4:ROOM:4fc426c644a0fbf43b47040378138b91'),
        progression_allowed=True,
    ),

    'Defeat Old King': MonsterLocationData(
        key=7,
        guid='984fe3e9aa9e0824aa625ae96009ca33',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Defeat Dr. Robert Blackett': MonsterLocationData(
        key=8,
        guid='5ba9cc84838e5904f9b3b8a70399b22f',
        viable_region_keys=('S3:ROOM:dc93676a46633de47b1c412abcb4fa37', 'S4:ROOM:dc93676a46633de47b1c412abcb4fa37'),
        progression_allowed=True,
    ),

    'Defeat Sothach & Baw': MonsterLocationData(
        key=9,
        guid='c55e3666e39af744b9a76d02f23ac4c1',
        viable_region_keys=('S3:ROOM:6875a1f8d25c06943824c80005455299', 'S4:ROOM:6875a1f8d25c06943824c80005455299'),
        progression_allowed=True,
    ),

    'Defeat Final Experiment': MonsterLocationData(
        key=10,
        guid='93719839da5681248b2a0ea99ba9712e',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Defeat Millie Erwood (God)': MonsterLocationData(
        key=11,
        guid='9b58dc0db02dbf24fbb430eba593df8e',
        viable_region_keys=('S1:ROOM:16db6f2c004830f458a930645c68976c', 'S2:ROOM:16db6f2c004830f458a930645c68976c', 'S3:ROOM:16db6f2c004830f458a930645c68976c', 'S4:ROOM:16db6f2c004830f458a930645c68976c'),
        progression_allowed=True,
    ),

    'Defeat First Witch': MonsterLocationData(
        key=12,
        guid='fd5276ef539590847bad2d39c3343c8c',
        viable_region_keys=('S2:ROOM:8d3cdc0c5cc494f43937baf87b82ac64',),
        progression_allowed=True,
    ),

    'Defeat Aborted Experiment': MonsterLocationData(
        key=13,
        guid='6dbabdb8d6ef61241b7bb040d6eda636',
        viable_region_keys=('S3:ROOM:9ca21e04fba6f4d4c8de03bb54f847ed', 'S4:ROOM:9ca21e04fba6f4d4c8de03bb54f847ed'),
        progression_allowed=True,
    ),

    'Defeat Ancient Champion': MonsterLocationData(
        key=14,
        guid='1b0b0b5bf00538b42a232f054944c50d',
        viable_region_keys=('S3:ROOM:5501a6de091a2fd45bc18f15546c1669', 'S4:ROOM:5501a6de091a2fd45bc18f15546c1669'),
        progression_allowed=True,
    ),

    'Defeat Ancient Ghoul': MonsterLocationData(
        key=15,
        guid='28af26cd9549cad45917fbf74655398c',
        viable_region_keys=('S2:ROOM:b001f2eadfee12942bc9013be2b59b56', 'S2:ROOM:f8eae91672f98f24da4659f815725bf9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee'),
        progression_allowed=True,
    ),

    'Defeat Martyr': MonsterLocationData(
        key=16,
        guid='8bf09a0c5a7892a4dad477b0a3df305f',
        viable_region_keys=('S3:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S3:ROOM:495194bff5c657148a34fbd57190db56', 'S3:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S4:ROOM:495194bff5c657148a34fbd57190db56', 'S4:ROOM:6db1480b99c5f8141b1aa2f1194e663e', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
        progression_allowed=True,
    ),

    'Defeat Big Wretch': MonsterLocationData(
        key=17,
        guid='c8123e344ced1644c9e77259024234e4',
        viable_region_keys=('S2:ROOM:062ae9bea49cd3e49b7f617a5533b9c1', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:f4f941e3d2e3ee84d92e5bed9b5793b3', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
        progression_allowed=True,
    ),

    'Defeat Executioner Wretch': MonsterLocationData(
        key=18,
        guid='cd0dd4e6f9003ee44bdfca95ece2487f',
        viable_region_keys=('S2:ROOM:062ae9bea49cd3e49b7f617a5533b9c1', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:f4f941e3d2e3ee84d92e5bed9b5793b3', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b'),
        progression_allowed=True,
    ),

    'Defeat Corpulent Zombie': MonsterLocationData(
        key=19,
        guid='8933c5444606d694fb279a46bcefba56',
        viable_region_keys=('S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:950d91f6b5420934d993598944fa6737', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:950d91f6b5420934d993598944fa6737'),
        progression_allowed=True,
    ),

    'Defeat Burning Zombie': MonsterLocationData(
        key=20,
        guid='6937bdad26ab43b4985427681bda5f66',
        viable_region_keys=('S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S3:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a'),
        progression_allowed=True,
    ),

    'Defeat Cloaked Ghoul': MonsterLocationData(
        key=21,
        guid='cdebe188fe98dbf41bb4f02e775a9127',
        viable_region_keys=('S2:ROOM:b001f2eadfee12942bc9013be2b59b56', 'S2:ROOM:f8eae91672f98f24da4659f815725bf9', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee'),
        progression_allowed=True,
    ),

    'Defeat Hunter Ghoul': MonsterLocationData(
        key=22,
        guid='027ad5ab689d27347b468f8cea296439',
        viable_region_keys=('S2:ROOM:8f6f1e72e7d4f914a9e0dab8499e1528', 'S2:ROOM:b001f2eadfee12942bc9013be2b59b56', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7'),
        progression_allowed=True,
    ),

    'Defeat Mechanical Priscilla': MonsterLocationData(
        key=23,
        guid='4980270ee7e43794882ddbffb4cfb713',
        viable_region_keys=('S3:ROOM:1554ebe61a392d3478433664175b7d1d', 'S3:ROOM:dc8951b0cc909aa4e91c31ca9e25eaba', 'S4:ROOM:1554ebe61a392d3478433664175b7d1d', 'S4:ROOM:dc8951b0cc909aa4e91c31ca9e25eaba'),
        progression_allowed=True,
    ),

    'Defeat Twin Cage': MonsterLocationData(
        key=24,
        guid='c05bc333e57c67140afd16a09fcfa711',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Defeat Cursed Armor': MonsterLocationData(
        key=25,
        guid='f10990658d656034e8094b8468f7d6e1',
        viable_region_keys=('S2:ROOM:062ae9bea49cd3e49b7f617a5533b9c1', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:f4f941e3d2e3ee84d92e5bed9b5793b3', 'S3:ROOM:00643b3d395ecd44e9c2980ce311d42b', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:00643b3d395ecd44e9c2980ce311d42b', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b'),
        progression_allowed=True,
    ),

    'Defeat Bodybag': MonsterLocationData(
        key=26,
        guid='d1e110c9868a2894188aec60f768d107',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S1:ROOM:9b93a0c714ee7e747b9be0ecb172a84c', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:133e8a902fbe4cd489588321c6220496', 'S2:ROOM:237ec54119fbefe4e9b097bfb5b06173', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:9b93a0c714ee7e747b9be0ecb172a84c', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b001f2eadfee12942bc9013be2b59b56', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:e550141cbe7d0794898d5383ebeb7df6', 'S2:ROOM:f8eae91672f98f24da4659f815725bf9', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:bd5d16a7d64a62449a335809034150fa', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:bd5d16a7d64a62449a335809034150fa', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7'),
        progression_allowed=True,
    ),

    'Defeat Bodybag (Trash)': MonsterLocationData(
        key=27,
        guid='e946b8f41dafcda40a47dd009d062ee5',
        viable_region_keys=('S2:ROOM:133e8a902fbe4cd489588321c6220496', 'S2:ROOM:237ec54119fbefe4e9b097bfb5b06173', 'S2:ROOM:e550141cbe7d0794898d5383ebeb7df6', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac'),
        progression_allowed=True,
    ),

    'Defeat Felix & Horace': MonsterLocationData(
        key=28,
        guid='361a9a14be71fb94285e547ebd7c02fe',
        viable_region_keys=('S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:b2961fb14de8d2e44907b900f3d31b29'),
        progression_allowed=True,
    ),

    'Defeat Elite Armor': MonsterLocationData(
        key=29,
        guid='b54ade75857a88d4bb5653bf01302327',
        viable_region_keys=('S2:ROOM:133e8a902fbe4cd489588321c6220496', 'S2:ROOM:237ec54119fbefe4e9b097bfb5b06173', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:e550141cbe7d0794898d5383ebeb7df6'),
        progression_allowed=True,
    ),

    'Defeat Angel (Primeval)': MonsterLocationData(
        key=30,
        guid='161797579f5fc2d498cc35aa66fb301f',
        viable_region_keys=('S1:ROOM:8f6f1e72e7d4f914a9e0dab8499e1528', 'S2:ROOM:8f55a06d7932fc042ba12dd99d71f628', 'S2:ROOM:8f6f1e72e7d4f914a9e0dab8499e1528', 'S3:ROOM:3e660b693cfd33c4ebeb4c054598e16c', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:231cd759bd21a7c42895cf7b1cc9c6e8', 'S4:ROOM:3e660b693cfd33c4ebeb4c054598e16c', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b'),
        progression_allowed=True,
    ),

    'Defeat Angel (Fool)': MonsterLocationData(
        key=31,
        guid='0e01d34f3c6a81d4495aa2d437624764',
        viable_region_keys=('S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:e5f35de124231d941b0752f6f8afe627', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:8aca0ad5386797d4eab3a10db3f603fd', 'S3:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f5b06d3cff618d142a6bbee639772d19', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:8aca0ad5386797d4eab3a10db3f603fd', 'S4:ROOM:ccb53dafabc639747a6e793ee274ee69', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f5b06d3cff618d142a6bbee639772d19'),
        progression_allowed=True,
    ),

    'Defeat Angel (Spearman)': MonsterLocationData(
        key=32,
        guid='986c66847f4fa4a41b7c93f87af9478b',
        viable_region_keys=('S2:ROOM:c5bc31984f08d13439ec5e5412297319', 'S3:ROOM:5501a6de091a2fd45bc18f15546c1669', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:5501a6de091a2fd45bc18f15546c1669', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b'),
        progression_allowed=True,
    ),

    'Defeat Angel (Starry)': MonsterLocationData(
        key=33,
        guid='e0f13e62d62c7364b96e8ef8214cdb3c',
        viable_region_keys=('S2:ROOM:2edba680374170444a93d37a208d2bcb', 'S3:ROOM:494ab3ae44fd75840add8b6d4f90f44c', 'S3:ROOM:cd6bfc4d210647742b2fd390d614eeb0', 'S4:ROOM:494ab3ae44fd75840add8b6d4f90f44c', 'S4:ROOM:bdc5a629a6c94624fa4d5cb547e7e3e8', 'S4:ROOM:cd6bfc4d210647742b2fd390d614eeb0'),
        progression_allowed=True,
    ),

    'Defeat Vomit Zombie (Cholera Patient)': MonsterLocationData(
        key=34,
        guid='0d167d73106da064da90c2eac3e761a9',
        viable_region_keys=('S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:e7a5a3e8291cea14bb774a2e0d48797e', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7'),
        progression_allowed=True,
    ),

    'Defeat Ghost (Physician)': MonsterLocationData(
        key=35,
        guid='a97623c695dad3c48ac1787757179b59',
        viable_region_keys=('S1:ROOM:544dd3a94d8394648bb89a013ef59df4', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:544dd3a94d8394648bb89a013ef59df4', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:f8eae91672f98f24da4659f815725bf9'),
        progression_allowed=True,
    ),

    'Defeat Ghost (Child)': MonsterLocationData(
        key=36,
        guid='c2c0fe28c7eabdd43b1956a99c49daec',
        viable_region_keys=('S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:010dfab9209448341b16b4aa74406b23'),
        progression_allowed=True,
    ),

    'Defeat Ghost (Initiate)': MonsterLocationData(
        key=37,
        guid='0ef1d75d3715c5b4aac535c0428b8f62',
        viable_region_keys=('S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:0e47785bff17bee4abcd516280874216', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:0e47785bff17bee4abcd516280874216', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d'),
        progression_allowed=True,
    ),

    'Defeat Grave Knight': MonsterLocationData(
        key=38,
        guid='bccbe89d3eb60e4459df55f4f5f51b79',
        viable_region_keys=('S3:ROOM:00643b3d395ecd44e9c2980ce311d42b', 'S4:ROOM:00643b3d395ecd44e9c2980ce311d42b'),
        progression_allowed=True,
    ),

    'Defeat Groundskeeper (Dafydd)': MonsterLocationData(
        key=39,
        guid='56029ccd620d4834c8589fd462b1233c',
        viable_region_keys=('S1:ROOM:2b722c05c0b44124d835b16489324003', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:2b722c05c0b44124d835b16489324003', 'S2:ROOM:d082561199983014ab8467548c4245eb'),
        progression_allowed=True,
    ),

    'Defeat Gurney Physician': MonsterLocationData(
        key=40,
        guid='a835d722d64f58642abb37dc0e559271',
        viable_region_keys=('S2:ROOM:062ae9bea49cd3e49b7f617a5533b9c1', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:f4f941e3d2e3ee84d92e5bed9b5793b3', 'S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:56c1de89453a37c4b946391eb0609346'),
        progression_allowed=True,
    ),

    'Defeat Antenna Head': MonsterLocationData(
        key=41,
        guid='c2e70597ae8335f4ebdc7a3833cc758c',
        viable_region_keys=('S3:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S3:ROOM:dc8951b0cc909aa4e91c31ca9e25eaba', 'S3:ROOM:e34ef0237675d6041aeb8a58102bf7cf', 'S4:ROOM:7fc7d70d5ab6540458662160c122cde2', 'S4:ROOM:dc8951b0cc909aa4e91c31ca9e25eaba', 'S4:ROOM:e34ef0237675d6041aeb8a58102bf7cf'),
        progression_allowed=True,
    ),

    'Defeat Heavy Zombie (Cholera Patient)': MonsterLocationData(
        key=42,
        guid='f3a0eea6c4dc99748ba975618aff029f',
        viable_region_keys=('S1:ROOM:051cb404d950e9d42b3c5425079cbaaa', 'S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2b722c05c0b44124d835b16489324003', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:844151552e7d4ed4ca673fd59f7dff56', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:051cb404d950e9d42b3c5425079cbaaa', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2b722c05c0b44124d835b16489324003', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:f8eae91672f98f24da4659f815725bf9', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683'),
        progression_allowed=True,
    ),

    'Defeat Bog Behemoth': MonsterLocationData(
        key=43,
        guid='7485e742ff5455a469f52b374cf39837',
        viable_region_keys=('S3:ROOM:f008a354ae29a30469757e93b1afddc3', 'S4:ROOM:f008a354ae29a30469757e93b1afddc3'),
        progression_allowed=True,
    ),

    'Defeat Horse Girl': MonsterLocationData(
        key=44,
        guid='6ef448d93bcd66c45a0d274ebeb1b959',
        viable_region_keys=('S3:ROOM:b865704bfa3d595429325b2e098831e5', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:b865704bfa3d595429325b2e098831e5'),
        progression_allowed=True,
    ),

    'Defeat Floating Failure': MonsterLocationData(
        key=45,
        guid='27c0a5b4e414e50449e8263619f2727e',
        viable_region_keys=('S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:2708d10a22614a84296aa1a0632ea9cf', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:f2f4404e46e6dcc4c8739b70c1bfa6d7'),
        progression_allowed=True,
    ),

    'Defeat Burdened Brother': MonsterLocationData(
        key=46,
        guid='c726fa366008e2947aa8d1bd8fbfd412',
        viable_region_keys=('S1:ROOM:00ef042b5ccfaf64b9c3df45df9e83f7', 'S2:ROOM:9458d03a0f36c6a418f209555440e533', 'S3:ROOM:00ef042b5ccfaf64b9c3df45df9e83f7', 'S4:ROOM:00ef042b5ccfaf64b9c3df45df9e83f7'),
        progression_allowed=True,
    ),

    'Defeat Initiate': MonsterLocationData(
        key=47,
        guid='bee72906c57bd0540a4544e6807c0e3a',
        viable_region_keys=('S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683'),
        progression_allowed=True,
    ),

    'Defeat Trickster Initiate': MonsterLocationData(
        key=48,
        guid='2945380a3eea6964a8007c59d2595f66',
        viable_region_keys=('S2:ROOM:062ae9bea49cd3e49b7f617a5533b9c1', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:f4f941e3d2e3ee84d92e5bed9b5793b3', 'S3:ROOM:96a3a54238545494dbfe5aaa232e8296', 'S4:ROOM:96a3a54238545494dbfe5aaa232e8296'),
        progression_allowed=True,
    ),

    'Defeat Jailkeeper': MonsterLocationData(
        key=49,
        guid='316d396b227e8a340a119f6256717232',
        viable_region_keys=('S3:ROOM:dc8951b0cc909aa4e91c31ca9e25eaba', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:dc8951b0cc909aa4e91c31ca9e25eaba'),
        progression_allowed=True,
    ),

    'Defeat Worshipper': MonsterLocationData(
        key=50,
        guid='de540ee1646ff264da08ed786ebdb815',
        viable_region_keys=('S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:f8415f01d217288468c7f3f57005916a'),
        progression_allowed=True,
    ),

    'Defeat Ghost (Lady)': MonsterLocationData(
        key=51,
        guid='2dffc5c630d3a9c469d6cdc848ef212b',
        viable_region_keys=('S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:010dfab9209448341b16b4aa74406b23'),
        progression_allowed=True,
    ),

    'Defeat Flykeeper': MonsterLocationData(
        key=52,
        guid='9d5428b910457d34f88e4154ec99a00f',
        viable_region_keys=('S3:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S3:ROOM:f008a354ae29a30469757e93b1afddc3', 'S4:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S4:ROOM:f008a354ae29a30469757e93b1afddc3'),
        progression_allowed=True,
    ),

    'Defeat Heavy Legless Zombie': MonsterLocationData(
        key=53,
        guid='6e7007764274d6d4b87483dc841ced27',
        viable_region_keys=('S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
        progression_allowed=True,
    ),

    'Defeat Legless Zombie': MonsterLocationData(
        key=54,
        guid='0501c3dc2f5b2e046a9dd80cb2c4b391',
        viable_region_keys=('S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
        progression_allowed=True,
    ),

    'Defeat Little Wretch': MonsterLocationData(
        key=55,
        guid='b289a505ec24f3c4ab4e4547b903b1ce',
        viable_region_keys=('S1:ROOM:00ef042b5ccfaf64b9c3df45df9e83f7', 'S2:ROOM:9458d03a0f36c6a418f209555440e533', 'S3:ROOM:00ef042b5ccfaf64b9c3df45df9e83f7', 'S4:ROOM:00ef042b5ccfaf64b9c3df45df9e83f7'),
        progression_allowed=True,
    ),

    'Defeat Lost Horse': MonsterLocationData(
        key=56,
        guid='e5b89d084be8c254bb5f58b313dd04f3',
        viable_region_keys=('S3:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S3:ROOM:358bfb18e3f56f148829927580e06851', 'S3:ROOM:5501a6de091a2fd45bc18f15546c1669', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S4:ROOM:358bfb18e3f56f148829927580e06851', 'S4:ROOM:5501a6de091a2fd45bc18f15546c1669', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b'),
        progression_allowed=True,
    ),

    'Defeat Mad Witch': MonsterLocationData(
        key=57,
        guid='f51a8a96f22b1f14da86621f2af8557f',
        viable_region_keys=('S2:ROOM:062ae9bea49cd3e49b7f617a5533b9c1', 'S2:ROOM:1d93c8cea551ce24a9d51ef11d29c334', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:97362787167af3a4c8791ca7367c541a', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S2:ROOM:f4f941e3d2e3ee84d92e5bed9b5793b3', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f008a354ae29a30469757e93b1afddc3', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f008a354ae29a30469757e93b1afddc3'),
        progression_allowed=True,
    ),

    'Defeat Giant Zombie': MonsterLocationData(
        key=58,
        guid='bff0f9b7bc6b94141a515b363288c862',
        viable_region_keys=('S1:ROOM:544dd3a94d8394648bb89a013ef59df4', 'S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:544dd3a94d8394648bb89a013ef59df4', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc'),
        progression_allowed=True,
    ),

    'Defeat Possessed Chest': MonsterLocationData(
        key=59,
        guid='f662ad06ff770dd40b31ac1dc1021c80',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Defeat Mudman': MonsterLocationData(
        key=60,
        guid='cebedaded89126b4689300748b8e9352',
        viable_region_keys=('S2:ROOM:c5bc31984f08d13439ec5e5412297319', 'S3:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S3:ROOM:f008a354ae29a30469757e93b1afddc3', 'S4:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S4:ROOM:f008a354ae29a30469757e93b1afddc3'),
        progression_allowed=True,
    ),

    'Defeat Necromancer': MonsterLocationData(
        key=61,
        guid='a58d6b75877c88449b6bf157fe48e2a8',
        viable_region_keys=(),
        progression_allowed=False,
    ),

    'Defeat Caged Ghoul': MonsterLocationData(
        key=62,
        guid='84af05c8fba24ec48b13d51c48e6c622',
        viable_region_keys=('S2:ROOM:cc8165106a4c1514a8ff4d2ea628f8d1', 'S3:ROOM:4a81144fa467b92469f748262217b4dc', 'S3:ROOM:f008a354ae29a30469757e93b1afddc3', 'S4:ROOM:4a81144fa467b92469f748262217b4dc', 'S4:ROOM:f008a354ae29a30469757e93b1afddc3'),
        progression_allowed=True,
    ),

    'Defeat Peter Mostyn': MonsterLocationData(
        key=63,
        guid='76383b16240aed2418e13f5026182a41',
        viable_region_keys=('S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:c2e874939ceb14b4ab039cd3fa27bc03'),
        progression_allowed=True,
    ),

    'Defeat Possessed Painting': MonsterLocationData(
        key=64,
        guid='08f525c2822ba7342b486268c5f0674d',
        viable_region_keys=('S2:ROOM:f4f941e3d2e3ee84d92e5bed9b5793b3',),
        progression_allowed=True,
    ),

    'Defeat Ghost (Vicar)': MonsterLocationData(
        key=65,
        guid='f0af7c881428567488d429da4b6fc031',
        viable_region_keys=('S1:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S1:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S2:ROOM:ad2eb7ac5d31ecd47bbc4f1681eb235c', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:dd0a3ffd48449cb419c22a6d290d4d92', 'S3:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S3:ROOM:f008a354ae29a30469757e93b1afddc3', 'S4:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S4:ROOM:f008a354ae29a30469757e93b1afddc3'),
        progression_allowed=True,
    ),

    'Defeat Maid (Charlotte)': MonsterLocationData(
        key=66,
        guid='b26cb483759eba041a6ef86ac0576be6',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2b722c05c0b44124d835b16489324003', 'S1:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S1:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S1:ROOM:844151552e7d4ed4ca673fd59f7dff56', 'S1:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S1:ROOM:bc560941b4184f847bf3883b06374596', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S1:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2b722c05c0b44124d835b16489324003', 'S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:6004319eb2f5de547ae38b9bef18431a', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:bc560941b4184f847bf3883b06374596', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S2:ROOM:f8eae91672f98f24da4659f815725bf9'),
        progression_allowed=True,
    ),

    'Defeat Rival Witch (Violent)': MonsterLocationData(
        key=67,
        guid='7c01257de99339241b6bdb8a3ab43ff0',
        viable_region_keys=('S1:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S2:ROOM:133e8a902fbe4cd489588321c6220496', 'S2:ROOM:237ec54119fbefe4e9b097bfb5b06173', 'S2:ROOM:c3c7869b2d5e4b54ab0435736cf75408', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e550141cbe7d0794898d5383ebeb7df6', 'S3:ROOM:bd5d16a7d64a62449a335809034150fa', 'S4:ROOM:aa2ea50e664bfb94dba39a36ae0985a7', 'S4:ROOM:bd5d16a7d64a62449a335809034150fa'),
        progression_allowed=True,
    ),

    'Defeat Rival Witch (Weird)': MonsterLocationData(
        key=68,
        guid='0bd547a08fa628341ad0e0751414993e',
        viable_region_keys=('S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S2:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744', 'S3:ROOM:358bfb18e3f56f148829927580e06851', 'S3:ROOM:505dc005fd3d4ee4d8e5cd37d8c13b87', 'S3:ROOM:61f06994f528c9c449d9882db2c6302d', 'S3:ROOM:c01d848b76049e6499b3b8a0d16bf405', 'S4:ROOM:358bfb18e3f56f148829927580e06851', 'S4:ROOM:505dc005fd3d4ee4d8e5cd37d8c13b87', 'S4:ROOM:61f06994f528c9c449d9882db2c6302d', 'S4:ROOM:aa2ea50e664bfb94dba39a36ae0985a7', 'S4:ROOM:c01d848b76049e6499b3b8a0d16bf405'),
        progression_allowed=True,
    ),

    'Defeat Rogue Ghoul': MonsterLocationData(
        key=69,
        guid='6eb3e208d8549f94bb0d29f81b620a40',
        viable_region_keys=('S3:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S3:ROOM:5501a6de091a2fd45bc18f15546c1669', 'S3:ROOM:bd5d16a7d64a62449a335809034150fa', 'S4:ROOM:24f9c06af26d3574c96998160d17c3c5', 'S4:ROOM:5501a6de091a2fd45bc18f15546c1669', 'S4:ROOM:bd5d16a7d64a62449a335809034150fa'),
        progression_allowed=True,
    ),

    'Defeat Rotted Initiate': MonsterLocationData(
        key=70,
        guid='ed0b7fe12a0a2784c9c6f305e9cb5bfa',
        viable_region_keys=('S3:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:084a4197f0bdf0f4ea16dae5b9e5532e', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:f8415f01d217288468c7f3f57005916a'),
        progression_allowed=True,
    ),

    'Defeat Beast Zombie (Cholera Patient)': MonsterLocationData(
        key=71,
        guid='913f827e89118764aa6bf0cc4b8a07fd',
        viable_region_keys=('S1:ROOM:2b722c05c0b44124d835b16489324003', 'S1:ROOM:9b93a0c714ee7e747b9be0ecb172a84c', 'S1:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:2b722c05c0b44124d835b16489324003', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:9b93a0c714ee7e747b9be0ecb172a84c', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d082561199983014ab8467548c4245eb', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683'),
        progression_allowed=True,
    ),

    'Defeat Necrotic Beast Zombie': MonsterLocationData(
        key=72,
        guid='91647998debdcce4fa3fcc49b975992e',
        viable_region_keys=('S3:ROOM:56c1de89453a37c4b946391eb0609346', 'S3:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:56c1de89453a37c4b946391eb0609346', 'S4:ROOM:618760d59bf5f5a4686c2496df8d2b41', 'S4:ROOM:ca281500dce1fdf4dbb2c3f17dbff906', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42'),
        progression_allowed=True,
    ),

    'Defeat Zombie (Cholera Patient)': MonsterLocationData(
        key=73,
        guid='1d5c87a52f939c743a962820f9a47a68',
        viable_region_keys=('S1:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S1:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S2:ROOM:0fccfcb48451429458c5f3f100ff39a5', 'S2:ROOM:2fd1b86b76189fb4bad2259351b03285', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683'),
        progression_allowed=True,
    ),

    'Defeat Bloody Man': MonsterLocationData(
        key=74,
        guid='ee9e7f820924e0342946b0c9fbf7ccfb',
        viable_region_keys=('S2:ROOM:f4f941e3d2e3ee84d92e5bed9b5793b3', 'S3:ROOM:035e4019a5fce0842830813a97db605a', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:d085d8f32dde5f841a165dcee303da42', 'S3:ROOM:e6b27af64fb997348b5f9751f41ec4f0', 'S4:ROOM:035e4019a5fce0842830813a97db605a', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:d085d8f32dde5f841a165dcee303da42', 'S4:ROOM:e6b27af64fb997348b5f9751f41ec4f0'),
        progression_allowed=True,
    ),

    'Defeat Skinned Witch': MonsterLocationData(
        key=75,
        guid='15eaed93fa33c9046a0ac5ac8d3b2021',
        viable_region_keys=('S4:ROOM:452b86b94cfd2214cb7154fe44fbd42b',),
        progression_allowed=True,
    ),

    'Defeat Giant Maid (Tara)': MonsterLocationData(
        key=76,
        guid='996ab4052345eca42803e859bd5dc301',
        viable_region_keys=('S1:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:133e8a902fbe4cd489588321c6220496', 'S2:ROOM:237ec54119fbefe4e9b097bfb5b06173', 'S2:ROOM:a129ba69899cd4b4ab4f84554abe9605', 'S2:ROOM:c99ce3f217c1f864cb02a0eb78eaf995', 'S2:ROOM:dcc0c3336cbfbcd419762f4e210339a4', 'S2:ROOM:e550141cbe7d0794898d5383ebeb7df6', 'S2:ROOM:e635186987e1efe45bd9c64612995976', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc'),
        progression_allowed=True,
    ),

    'Defeat Sage Armor': MonsterLocationData(
        key=77,
        guid='a0bdfb3209a15d24e910762ea54de05f',
        viable_region_keys=('S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:aeddb816451e0aa4a8d72f5ef7b63da3', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:aeddb816451e0aa4a8d72f5ef7b63da3'),
        progression_allowed=True,
    ),

    'Defeat Curse Sentinel': MonsterLocationData(
        key=78,
        guid='b21410dc684f48f4bb9bc9d46bc3b80e',
        viable_region_keys=('S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:010dfab9209448341b16b4aa74406b23'),
        progression_allowed=True,
    ),

    'Defeat Upper Initiate': MonsterLocationData(
        key=79,
        guid='074a4ef550eaf654e9ec0b54c8898273',
        viable_region_keys=('S2:ROOM:5c0062ec6cb1f7b40be1fa82a67ec5a0', 'S2:ROOM:63ff0a124ac5f8f42b5028f250bf9ca1', 'S2:ROOM:935ecafeead9e3640ba5c4530bf373d6', 'S2:ROOM:bff6137cf70487547bd37b12bc1ba143', 'S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0'),
        progression_allowed=True,
    ),

    'Defeat Valley Zombie': MonsterLocationData(
        key=80,
        guid='f6b7fc8d2587ea64da56163d0dda4fce',
        viable_region_keys=('S3:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S3:ROOM:3e248e88711439d499310ded7668e024', 'S3:ROOM:d8a68342b53bcf04d905b38502e82884', 'S4:ROOM:13106d5f63b05ae4780f246081c8cfab', 'S4:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc', 'S4:ROOM:3e248e88711439d499310ded7668e024', 'S4:ROOM:d8a68342b53bcf04d905b38502e82884'),
        progression_allowed=True,
    ),

    'Defeat Ghost (Soldier)': MonsterLocationData(
        key=81,
        guid='81b6d0404876ddc48a13ff0d9cf45d3e',
        viable_region_keys=('S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
        progression_allowed=True,
    ),

    'Defeat Jailkeeper Zombie': MonsterLocationData(
        key=82,
        guid='3e4aa7974087dab4b96461c034b5691d',
        viable_region_keys=('S3:ROOM:5501a6de091a2fd45bc18f15546c1669', 'S4:ROOM:3bd2ebb4273291545af9a127fdc60dee', 'S4:ROOM:5501a6de091a2fd45bc18f15546c1669', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683'),
        progression_allowed=True,
    ),

    "Defeat King's Eye": MonsterLocationData(
        key=83,
        guid='8b3d23e175ee01c4485ebdc57e1af169',
        viable_region_keys=('S3:ROOM:010dfab9209448341b16b4aa74406b23', 'S3:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S3:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:010dfab9209448341b16b4aa74406b23', 'S4:ROOM:485ac8870d4600e40bd7cdd0aa6766ac', 'S4:ROOM:6e9af6473da5bbc42b7427fea2daf91a', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:937e57f0501006a4aafb294d9609c9ff', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
        progression_allowed=True,
    ),

    'Defeat Grenadier Zombie': MonsterLocationData(
        key=84,
        guid='deee637d0db484d4086717713075bb6c',
        viable_region_keys=('S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
        progression_allowed=True,
    ),

    'Defeat Labyrinth Knight': MonsterLocationData(
        key=85,
        guid='f12782c55d1397445860bc6891e9093a',
        viable_region_keys=('S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683'),
        progression_allowed=True,
    ),

    'Defeat Nurse Zombie': MonsterLocationData(
        key=86,
        guid='454ff6a949cd4c44783b2eac79c4bf8b',
        viable_region_keys=('S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:8872cd71c789dfc4d94e03b8dbc82d7f', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
        progression_allowed=True,
    ),

    'Defeat Soldier Zombie': MonsterLocationData(
        key=87,
        guid='f6919623e04f40a46ab39cf8b3263dcd',
        viable_region_keys=('S3:ROOM:76d460f1d9901864db42515b6e53b11c', 'S3:ROOM:83b55f07665f4664882449ad3a6a013a', 'S3:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S3:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S3:ROOM:f2b6fd0039c5d75498351fea7f6a1f58', 'S4:ROOM:5fa6aa51c7adc1648bbd874fd6df3366', 'S4:ROOM:6d7e59e34542d484facd24cb81aa7683', 'S4:ROOM:76d460f1d9901864db42515b6e53b11c', 'S4:ROOM:83b55f07665f4664882449ad3a6a013a', 'S4:ROOM:90b5d805d370a154da21ff8f0f7d6322', 'S4:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6', 'S4:ROOM:ae4a93b459f4e3041b4f47cad99f9cd6', 'S4:ROOM:f2b6fd0039c5d75498351fea7f6a1f58'),
        progression_allowed=True,
    ),

    'Defeat Flamethrower Zombie': MonsterLocationData(
        key=88,
        guid='0c1a24d5a3b844f43b7dba45431eb29b',
        viable_region_keys=('S3:ROOM:79474450751fbea4e987a363436baf6c', 'S3:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S3:ROOM:b0200cc273847294db5d00e850060b97', 'S3:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S3:ROOM:f8415f01d217288468c7f3f57005916a', 'S4:ROOM:79474450751fbea4e987a363436baf6c', 'S4:ROOM:8a7a7c4dab9dd774cb2c09fddefc14b7', 'S4:ROOM:b0200cc273847294db5d00e850060b97', 'S4:ROOM:c84c6430bbec03f4d837c586ad44384b', 'S4:ROOM:f8415f01d217288468c7f3f57005916a'),
        progression_allowed=True,
    ),

    'Defeat Emma': MonsterLocationData(
        key=89,
        guid='690ab4af318eed341ae39472a7d9c575',
        viable_region_keys=('S1:ROOM:c5bc31984f08d13439ec5e5412297319',),
        progression_allowed=True,
    ),

}

REMEMBRANCE_LOCATIONS: dict[
    str,
    RemembranceLocationData
] = {

    'Coffin Room Remembrance Shrine Offering': RemembranceLocationData(
        key=1,
        room_guid='658bb443034365f4f95d8300d22e20e8',
        viable_region_keys=('S1:ROOM:658bb443034365f4f95d8300d22e20e8',),
    ),

    'Hedge Maze Final Room Remembrance Shrine Offering': RemembranceLocationData(
        key=2,
        room_guid='87ffb81f6ce06304e8c1385d3c08d1ff',
        viable_region_keys=('S1:ROOM:87ffb81f6ce06304e8c1385d3c08d1ff',),
    ),

    'Nowhere Remembrance Shrine Offering': RemembranceLocationData(
        key=3,
        room_guid='8a3a0192a94794949998c22a826750a5',
        viable_region_keys=('S1:ROOM:8a3a0192a94794949998c22a826750a5',),
    ),

    'Occult Library Remembrance Shrine Offering': RemembranceLocationData(
        key=4,
        room_guid='6004319eb2f5de547ae38b9bef18431a',
        viable_region_keys=('S1:ROOM:6004319eb2f5de547ae38b9bef18431a',),
    ),

    'Right House Exit Remembrance Shrine Offering': RemembranceLocationData(
        key=5,
        room_guid='8f6f1e72e7d4f914a9e0dab8499e1528',
        viable_region_keys=('S1:ROOM:8f6f1e72e7d4f914a9e0dab8499e1528',),
    ),

    'Tomb Remembrance Shrine Offering': RemembranceLocationData(
        key=6,
        room_guid='2bf2226d4f4d0ea499f8eefdce0b01da',
        viable_region_keys=('S1:ROOM:2bf2226d4f4d0ea499f8eefdce0b01da',),
    ),

    'West Stairwell Remembrance Shrine Offering': RemembranceLocationData(
        key=7,
        room_guid='b298ac5c5d9cd8b4d857ca4eb8932744',
        viable_region_keys=('S1:ROOM:b298ac5c5d9cd8b4d857ca4eb8932744',),
    ),

    'Wine Room Remembrance Shrine Offering': RemembranceLocationData(
        key=8,
        room_guid='68e5dd6d1531c7e478b10d98f1aa7701',
        viable_region_keys=('S1:ROOM:68e5dd6d1531c7e478b10d98f1aa7701',),
    ),

    'Blackett Attic Storage Room Remembrance Shrine Offering': RemembranceLocationData(
        key=9,
        room_guid='112a6ccbc4510564fb0a9064e215d877',
        viable_region_keys=('S2:ROOM:112a6ccbc4510564fb0a9064e215d877',),
    ),

    'Observatory Remembrance Shrine Offering': RemembranceLocationData(
        key=10,
        room_guid='d7d694fb5f60763428690238f4ce0839',
        viable_region_keys=('S2:ROOM:d7d694fb5f60763428690238f4ce0839',),
    ),

    'Chapter 2 Tomb Remembrance Shrine Offering': RemembranceLocationData(
        key=11,
        room_guid='285d223bbd79fe5479419e03c71995ff',
        viable_region_keys=('S2:ROOM:285d223bbd79fe5479419e03c71995ff',),
    ),

    'Upper Floor Margaret Room Remembrance Shrine Offering': RemembranceLocationData(
        key=12,
        room_guid='d71eed4b5dbaa5844867a286b1eb84b0',
        viable_region_keys=('S2:ROOM:d71eed4b5dbaa5844867a286b1eb84b0',),
    ),

    '1916 Attic Prison Remembrance Shrine Offering': RemembranceLocationData(
        key=13,
        room_guid='de703ddba4a2aae468ba765115c23a8b',
        viable_region_keys=('S3:ROOM:de703ddba4a2aae468ba765115c23a8b',),
    ),

    '1916 Left House Exit Remembrance Shrine Offering': RemembranceLocationData(
        key=14,
        room_guid='2f348ff005b0b36478479aecb9655f69',
        viable_region_keys=('S3:ROOM:2f348ff005b0b36478479aecb9655f69',),
    ),

    '1916 Strange Bedroom Remembrance Shrine Offering': RemembranceLocationData(
        key=15,
        room_guid='a76e8e95a9e80da46ba2c5416bdff7b6',
        viable_region_keys=('S3:ROOM:a76e8e95a9e80da46ba2c5416bdff7b6',),
    ),

    '1916 Upper Banquet Hall Remembrance Shrine Offering': RemembranceLocationData(
        key=16,
        room_guid='937e57f0501006a4aafb294d9609c9ff',
        viable_region_keys=('S3:ROOM:937e57f0501006a4aafb294d9609c9ff',),
    ),

    '1916 West Stairwell Remembrance Shrine Offering': RemembranceLocationData(
        key=17,
        room_guid='c52803e0f6ac66a44a654639db767869',
        viable_region_keys=('S3:ROOM:c52803e0f6ac66a44a654639db767869',),
    ),

    'Church Second Stairwell Remembrance Shrine Offering': RemembranceLocationData(
        key=18,
        room_guid='ccb53dafabc639747a6e793ee274ee69',
        viable_region_keys=('S3:ROOM:ccb53dafabc639747a6e793ee274ee69',),
    ),

    'East Forest Village Remembrance Shrine Offering': RemembranceLocationData(
        key=19,
        room_guid='3ddb9378dc824d34aa71fbcad8c1e4fc',
        viable_region_keys=('S3:ROOM:3ddb9378dc824d34aa71fbcad8c1e4fc',),
    ),

    '1916 Nowhere Remembrance Shrine Offering': RemembranceLocationData(
        key=20,
        room_guid='26e1473cfbc315e44975412617ca9906',
        viable_region_keys=('S3:ROOM:26e1473cfbc315e44975412617ca9906',),
    ),

    'West Forest Remembrance Shrine Offering': RemembranceLocationData(
        key=21,
        room_guid='460e766149bf29f48a3164d785f3fc57',
        viable_region_keys=('S3:ROOM:460e766149bf29f48a3164d785f3fc57',),
    ),

    'Blood Tower Second Floor Hall Remembrance Shrine Offering': RemembranceLocationData(
        key=22,
        room_guid='b2961fb14de8d2e44907b900f3d31b29',
        viable_region_keys=('S4:ROOM:b2961fb14de8d2e44907b900f3d31b29',),
    ),

}