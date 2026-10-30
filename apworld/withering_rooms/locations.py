from BaseClasses import Location

from .data import (
    RANDOMIZED_ITEMS,
    LORE_LOCATIONS,
    MONSTER_LOCATIONS,
    REMEMBRANCE_LOCATIONS,
    MULTI_DISCOVERY_COUNTS,
    MULTI_DISCOVERY_LOCATION_ID_BASE,
)


GAME_NAME = "Withering Rooms"


class WitheringRoomsLocation(Location):
    game = GAME_NAME


def discovery_location_names(
    item_name: str,
    location_name_override: str | None = None,
) -> list[str]:
    """
    Return all Archipelago discovery location names for an item.

    Normal items:
        ["Discover Cleaver"]

    Multi-discovery items:
        [
            "Discover Remembrance Tear 1",
            "Discover Remembrance Tear 2",
            ...
        ]

    Location-name overrides retain their existing one-location
    behavior and should not be combined with multi-discovery.
    """

    count = MULTI_DISCOVERY_COUNTS.get(item_name, 1)

    if location_name_override:
        if count != 1:
            raise RuntimeError(
                f"{item_name!r} has both a location-name override "
                "and a multi-discovery count."
            )

        return [location_name_override]

    if count <= 0:
        raise RuntimeError(
            f"{item_name!r} has invalid multi-discovery count {count}."
        )

    if count == 1:
        return [f"Discover {item_name}"]

    prefix = (
        "Bryn Bach Abbey Trial Completion"
        if item_name == "Trickster Medal"
        else f"Discover {item_name}"
    )

    return [
        f"{prefix} {index}"
        for index in range(1, count + 1)
    ]


def build_discovery_locations() -> list[tuple[str, int, str]]:
    """
    Returns:
        (location_name, location_id, item_name)

    The first discovery location uses the item's historical
    LOCATION_ID_BASE + key ID.

    Additional ordinal locations use the reserved
    MULTI_DISCOVERY_LOCATION_ID_BASE range.
    """

    result: list[tuple[str, int, str]] = []
    next_extra_id = MULTI_DISCOVERY_LOCATION_ID_BASE

    for item_name, data in sorted(
        RANDOMIZED_ITEMS.items(),
        key=lambda pair: pair[1].key,
    ):
        if not data.creates_location:
            continue

        names = discovery_location_names(
            item_name,
            data.location_name_override,
        )

        for index, location_name in enumerate(names):
            if index == 0:
                location_id = data.location_id
            else:
                location_id = next_extra_id
                next_extra_id += 1

            result.append(
                (location_name, location_id, item_name)
            )

    return result


DISCOVERY_LOCATIONS = build_discovery_locations()


LOCATION_NAME_TO_ID = {
    location_name: location_id
    for location_name, location_id, _item_name
    in DISCOVERY_LOCATIONS
}


LOCATION_NAME_TO_ID.update({
    location_name: data.location_id
    for location_name, data in LORE_LOCATIONS.items()
})


LOCATION_NAME_TO_ID.update({
    location_name: data.location_id
    for location_name, data in MONSTER_LOCATIONS.items()
})


LOCATION_NAME_TO_ID.update({
    location_name: data.location_id
    for location_name, data in REMEMBRANCE_LOCATIONS.items()
})

LOCATION_NAME_TO_ITEM = {
    location_name: item_name
    for location_name, _location_id, item_name
    in DISCOVERY_LOCATIONS
}