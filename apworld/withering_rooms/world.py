from BaseClasses import (
    Item,
    ItemClassification,
    Region,
    LocationProgressType,
)
from worlds.AutoWorld import World
from worlds.generic.Rules import add_rule

from .data import (
    RANDOMIZED_ITEMS,
    LORE_LOCATIONS,
    MONSTER_LOCATIONS,
    REMEMBRANCE_LOCATIONS,
    MULTI_DISCOVERY_COUNTS,
    MANDATORY_ITEM_COUNTS,
)

from .options import WitheringRoomsOptions
from .items import (
    WitheringRoomsItem,
    ITEM_NAME_TO_ID,
)
from .locations import (
    WitheringRoomsLocation,
    LOCATION_NAME_TO_ID,
    LOCATION_NAME_TO_ITEM,
    discovery_location_names,
)

from .regions import (
    DEFAULT_LOCATION_REGION_KEY,
    REQUIRED_PROGRESSION_ITEM_NAMES,
    create_regions as create_world_regions,
    structurally_reachable_region_keys,
)


# Requirements to COMPLETE an item discovery, not to enter its source room.
# Applies to every chapter in which a canonical item source is reachable.
DISCOVERY_ACCESS_REQUIREMENTS: dict[str, tuple[str, ...]] = {
    "Eviction Letter": ("Nurse Uniform",),
    "Basic Wretch Pass": ("Nurse Uniform",),
    "Advanced Wretch Pass": (
        "Nurse Uniform", "Eviction Letter", "Basic Wretch Pass",
    ),
    "Nightingale Doll": ("Waking Powder",),
}

MONSTER_ACCESS_REQUIREMENTS: dict[str, tuple[str, ...]] = {
    "Defeat Dr. Robert Blackett": ("Cholera Clinic Cage Key",),
}


GOAL_DEFINITIONS = {
    "Priscilla Mostyn": {
        "monster_location": "Defeat Priscilla Mostyn",
        "event_item": "Victory - Priscilla Mostyn",
    },
    "God Millie": {
        "monster_location": "Defeat Millie Erwood (God)",
        "event_item": "Victory - God Millie",
    },
}


class WitheringRoomsWorld(World):
    """
    Archipelago Multiworld implementation for the 2.5D horror RPG roguelike Withering Rooms.
    """

    game = "Withering Rooms"
    options_dataclass = WitheringRoomsOptions
    options: WitheringRoomsOptions

    item_name_to_id = ITEM_NAME_TO_ID
    location_name_to_id = LOCATION_NAME_TO_ID

    required_client_version = (0, 6, 0)

    GOAL_EVENT_ITEMS = {
        "Priscilla Mostyn": "Victory - Priscilla Mostyn",
        "God Millie": "Victory - God Millie",
    }
    GOAL_MONSTER_LOCATIONS = {
        "Priscilla Mostyn": "Defeat Priscilla Mostyn",
        "God Millie": "Defeat Millie Erwood (God)",
    }



    def create_item(self, name: str) -> Item:
        data = RANDOMIZED_ITEMS[name]

        return WitheringRoomsItem(
            name,
            data.classification,
            data.item_id,
            self.player,
        )

    def create_goal_event(
        self,
        goal_name: str,
        regions: dict[str, Region],
    ) -> None:
        if goal_name not in GOAL_DEFINITIONS:
            raise RuntimeError(
                f"Unknown completion goal: {goal_name!r}"
            )

        goal_data = GOAL_DEFINITIONS[goal_name]

        monster_location_name = (
            goal_data["monster_location"]
        )

        event_item_name = (
            goal_data["event_item"]
        )

        if monster_location_name not in MONSTER_LOCATIONS:
            raise RuntimeError(
                f"Completion goal {goal_name!r} references "
                f"unknown monster location "
                f"{monster_location_name!r}."
            )

        monster_data = MONSTER_LOCATIONS[
            monster_location_name
        ]

        viable_keys = monster_data.viable_region_keys

        if not viable_keys:
            raise RuntimeError(
                f"Completion goal {goal_name!r} has no "
                "resolved viable region."
            )

        # -----------------------------------------
        # Exactly one possible source region
        # -----------------------------------------

        if len(viable_keys) == 1:
            region_key = viable_keys[0]

            if region_key not in regions:
                raise RuntimeError(
                    f"Completion goal {goal_name!r}: "
                    f"unknown region {region_key!r}"
                )

            parent_region = regions[region_key]

        # -----------------------------------------
        # Multiple possible source regions:
        # create an OR-reachability sink
        # -----------------------------------------

        else:
            goal_region = Region(
                f"Goal Access: {goal_name}",
                self.player,
                self.multiworld,
            )

            self.multiworld.regions.append(
                goal_region
            )

            for region_key in viable_keys:
                if region_key not in regions:
                    raise RuntimeError(
                        f"Completion goal {goal_name!r}: "
                        f"unknown region {region_key!r}"
                    )

                regions[region_key].connect(
                    goal_region
                )

            parent_region = goal_region

        # Address=None makes this an AP event location,
        # not a networked randomized location.
        event_location = WitheringRoomsLocation(
            self.player,
            f"Goal: {goal_name}",
            None,
            parent_region,
        )

        # Code=None likewise makes this an event item.
        event_item = WitheringRoomsItem(
            event_item_name,
            ItemClassification.progression,
            None,
            self.player,
        )

        event_location.place_locked_item(
            event_item
        )

        parent_region.locations.append(
            event_location
        )

    def create_regions(self) -> None:
        # Validate that every item referenced by region access rules
        # actually exists in the AP item database.
        missing_rule_items = (
            set(REQUIRED_PROGRESSION_ITEM_NAMES)
            - set(RANDOMIZED_ITEMS)
        )

        if missing_rule_items:
            raise RuntimeError(
                "Region logic references undefined AP items: "
                + ", ".join(sorted(missing_rule_items))
            )

        # Also validate items used by per-check requirements.
        location_rule_items = {
            name
            for requirements in (
                *DISCOVERY_ACCESS_REQUIREMENTS.values(),
                *MONSTER_ACCESS_REQUIREMENTS.values(),
            )
            for name in requirements
        }
        unknown_location_rule_items = location_rule_items - set(RANDOMIZED_ITEMS)
        if unknown_location_rule_items:
            raise RuntimeError(
                "Location logic references undefined AP items: "
                + ", ".join(sorted(unknown_location_rule_items))
            )
        if set(DISCOVERY_ACCESS_REQUIREMENTS) - set(RANDOMIZED_ITEMS):
            raise RuntimeError("Discovery access rules reference undefined discoveries")
        if set(MONSTER_ACCESS_REQUIREMENTS) - set(MONSTER_LOCATIONS):
            raise RuntimeError("Monster access rules reference undefined monsters")

        configured_special_items = (
            set(MULTI_DISCOVERY_COUNTS)
            | set(MANDATORY_ITEM_COUNTS)
        )

        unknown_special_items = (
            configured_special_items
            - set(RANDOMIZED_ITEMS)
        )

        if unknown_special_items:
            raise RuntimeError(
                "Special item-count configuration references "
                "undefined items: "
                + ", ".join(sorted(unknown_special_items))
            )

        for item_name, count in MULTI_DISCOVERY_COUNTS.items():
            if count < 1:
                raise RuntimeError(
                    f"{item_name!r} has invalid discovery count {count}."
                )

            if not RANDOMIZED_ITEMS[item_name].creates_location:
                raise RuntimeError(
                    f"{item_name!r} has multiple discovery locations "
                    "but creates_location=False."
                )

        regions = create_world_regions(self)

        default_region = regions[
            DEFAULT_LOCATION_REGION_KEY
        ]

        structurally_reachable = (
            structurally_reachable_region_keys()
        )

        for item_name, data in RANDOMIZED_ITEMS.items():
            if not data.creates_location:
                continue

            if not self.is_item_randomized(item_name):
                continue

            location_names = discovery_location_names(
                item_name,
                data.location_name_override,
            )

            for location_name in location_names:
                location_id = LOCATION_NAME_TO_ID[location_name]

                viable_keys = data.viable_region_keys

                unresolved_region = not viable_keys

                has_reachable_source = any(
                    region_key in structurally_reachable
                    for region_key in viable_keys
                )

                progression_unsafe = (
                    unresolved_region
                    or not has_reachable_source
                )

                if not viable_keys:
                    parent_region = default_region

                elif len(viable_keys) == 1:
                    region_key = viable_keys[0]

                    if region_key not in regions:
                        raise RuntimeError(
                            f"{location_name}: unknown region "
                            f"{region_key!r}"
                        )

                    parent_region = regions[region_key]

                else:
                    check_region = Region(
                        f"Location Access: {location_name}",
                        self.player,
                        self.multiworld,
                    )

                    self.multiworld.regions.append(check_region)

                    for region_key in viable_keys:
                        if region_key not in regions:
                            raise RuntimeError(
                                f"{location_name}: unknown region "
                                f"{region_key!r}"
                            )

                        regions[region_key].connect(check_region)

                    parent_region = check_region

                location = WitheringRoomsLocation(
                    self.player,
                    location_name,
                    location_id,
                    parent_region,
                )

                if progression_unsafe:
                    location.progress_type = (
                        LocationProgressType.EXCLUDED
                    )

                requirements = DISCOVERY_ACCESS_REQUIREMENTS.get(item_name, ())
                if requirements:
                    add_rule(
                        location,
                        lambda state, requirements=requirements, player=self.player:
                            all(state.has(name, player) for name in requirements),
                    )

                parent_region.locations.append(location)

        # =========================================
        # Remembrance Shrine locations
        # =========================================

        for location_name, data in REMEMBRANCE_LOCATIONS.items():

            viable_keys = data.viable_region_keys

            # Every authored Remembrance Shrine should have a
            # resolved canonical region. Treat a missing region
            # as a data error rather than silently placing the
            # check in the default region.
            if not viable_keys:
                raise RuntimeError(
                    f"{location_name}: Remembrance Shrine has "
                    "no viable region."
                )

            # -----------------------------------------
            # Exactly one possible source region
            # -----------------------------------------

            if len(viable_keys) == 1:
                region_key = viable_keys[0]

                if region_key not in regions:
                    raise RuntimeError(
                        f"{location_name}: unknown Remembrance "
                        f"Shrine region {region_key!r}"
                    )

                parent_region = regions[region_key]

            # -----------------------------------------
            # Multiple possible source regions:
            # create an OR-reachability sink
            # -----------------------------------------

            else:
                check_region = Region(
                    f"Location Access: {location_name}",
                    self.player,
                    self.multiworld,
                )

                self.multiworld.regions.append(
                    check_region
                )

                for region_key in viable_keys:
                    if region_key not in regions:
                        raise RuntimeError(
                            f"{location_name}: unknown Remembrance "
                            f"Shrine region {region_key!r}"
                        )

                    regions[region_key].connect(
                        check_region
                    )

                parent_region = check_region

            location = WitheringRoomsLocation(
                self.player,
                location_name,
                data.location_id,
                parent_region,
            )

            add_rule(
                location,
                lambda state, player=self.player:
                    state.has("Occult Library Key", player)
            )

            parent_region.locations.append(location)
        # =========================================
        # Loresanity locations
        # =========================================

        if self.options.loresanity:

            for location_name, data in LORE_LOCATIONS.items():

                viable_keys = data.viable_region_keys

                # -----------------------------------------
                # No resolved source yet
                # -----------------------------------------

                unresolved_region = not viable_keys

                if not viable_keys:
                    parent_region = default_region

                # -----------------------------------------
                # Exactly one possible source region
                # -----------------------------------------

                elif len(viable_keys) == 1:
                    region_key = viable_keys[0]

                    if region_key not in regions:
                        raise RuntimeError(
                            f"{location_name}: unknown lore region "
                            f"{region_key!r}"
                        )

                    parent_region = regions[region_key]

                # -----------------------------------------
                # Multiple possible source regions:
                # create an OR-reachability sink
                # -----------------------------------------

                else:
                    check_region = Region(
                        f"Location Access: {location_name}",
                        self.player,
                        self.multiworld,
                    )

                    self.multiworld.regions.append(
                        check_region
                    )

                    for region_key in viable_keys:
                        if region_key not in regions:
                            raise RuntimeError(
                                f"{location_name}: unknown lore region "
                                f"{region_key!r}"
                            )

                        regions[region_key].connect(
                            check_region
                        )

                    parent_region = check_region

                location = WitheringRoomsLocation(
                    self.player,
                    location_name,
                    data.location_id,
                    parent_region,
                )

                # Unknown-source lore checks are allowed to
                # exist, but must never hold progression.
                if (
                    unresolved_region
                    or not data.progression_allowed
                ):
                    location.progress_type = (
                        LocationProgressType.EXCLUDED
                    )

                parent_region.locations.append(location)

        if self.options.monstersanity:

            for location_name, data in MONSTER_LOCATIONS.items():

                viable_keys = data.viable_region_keys

                # -----------------------------------------
                # No resolved source yet
                # -----------------------------------------

                unresolved_region = not viable_keys

                if not viable_keys:
                    parent_region = default_region

                # -----------------------------------------
                # Exactly one possible source region
                # -----------------------------------------

                elif len(viable_keys) == 1:
                    region_key = viable_keys[0]

                    if region_key not in regions:
                        raise RuntimeError(
                            f"{location_name}: unknown monster region "
                            f"{region_key!r}"
                        )

                    parent_region = regions[region_key]

                # -----------------------------------------
                # Multiple possible source regions:
                # create an OR-reachability sink
                # -----------------------------------------

                else:
                    check_region = Region(
                        f"Location Access: {location_name}",
                        self.player,
                        self.multiworld,
                    )

                    self.multiworld.regions.append(
                        check_region
                    )

                    for region_key in viable_keys:
                        if region_key not in regions:
                            raise RuntimeError(
                                f"{location_name}: unknown monster region "
                                f"{region_key!r}"
                            )

                        regions[region_key].connect(
                            check_region
                        )

                    parent_region = check_region

                location = WitheringRoomsLocation(
                    self.player,
                    location_name,
                    data.location_id,
                    parent_region,
                )

                # Unknown-source monster checks are allowed to
                # exist, but must never hold progression.
                if (
                    unresolved_region
                    or not data.progression_allowed
                ):
                    location.progress_type = (
                        LocationProgressType.EXCLUDED
                    )

                requirements = MONSTER_ACCESS_REQUIREMENTS.get(location_name, ())
                if requirements:
                    add_rule(
                        location,
                        lambda state, requirements=requirements, player=self.player:
                            all(state.has(name, player) for name in requirements),
                    )

                parent_region.locations.append(location)

        # =========================================
        # Completion goal events
        # =========================================

        selected_goals = (
            self.options.completion_goals.value
        )

        if not selected_goals:
            raise RuntimeError(
                "At least one Withering Rooms completion "
                "goal must be selected."
            )

        for goal_name in selected_goals:
            self.create_goal_event(
                goal_name,
                regions,
            )

    def get_filler_item_name(self) -> str:
        filler_names = [
            name
            for name, data in RANDOMIZED_ITEMS.items()
            if data.include_in_pool
            and data.repeatable_filler
        ]

        if not filler_names:
            raise RuntimeError(
                "Withering Rooms has no repeatable filler items defined."
            )

        return self.random.choice(filler_names)


    def is_item_randomized(self, name: str) -> bool:
        if not self.options.challenge_start and name in {
            "Gatehouse Key",
            "Strange Bedroom Key",
        }:
            return False

        return True


    def fill_slot_data(self) -> dict:
        return {
            "challenge_start": bool(
                self.options.challenge_start.value
            ),
            "loresanity": bool(
                self.options.loresanity.value
            ),
            "monstersanity": bool(
                self.options.monstersanity.value
            ),
            "death_link": bool(
                self.options.death_link.value
            ),
            "completion_goals": sorted(
                self.options.completion_goals.value
            ),

        }


    def create_items(self) -> None:
        location_count = sum(
            MULTI_DISCOVERY_COUNTS.get(name, 1)
            for name, data in RANDOMIZED_ITEMS.items()
            if data.creates_location
            and self.is_item_randomized(name)
        )
        # Remembrance Shrines are always present.
        location_count += len(
            REMEMBRANCE_LOCATIONS
        )

        if self.options.loresanity:
            location_count += len(
                LORE_LOCATIONS
            )

        if self.options.monstersanity:
            location_count += len(
                MONSTER_LOCATIONS
            )

        fixed_item_names: list[str] = []

        for name, data in RANDOMIZED_ITEMS.items():
            if not data.include_in_pool:
                continue

            if data.repeatable_filler:
                continue

            if not self.is_item_randomized(name):
                continue

            count = MANDATORY_ITEM_COUNTS.get(name, 1)

            if count <= 0:
                raise RuntimeError(
                    f"{name!r} has invalid mandatory item count {count}."
                )

            fixed_item_names.extend([name] * count)

        if len(fixed_item_names) > location_count:
            raise RuntimeError(
                "Withering Rooms has more fixed pool items "
                f"({len(fixed_item_names)}) than locations "
                f"({location_count})."
            )

        requested_extra_tears = (
            self.options.extra_remembrance_tears.value
        )

        available_filler_slots = (
            location_count - len(fixed_item_names)
        )

        extra_tear_count = min(
            requested_extra_tears,
            available_filler_slots,
        )

        # Extra Remembrance Tears replace filler slots.
        # They do NOT create additional locations.
        fixed_item_names.extend(
            ["Remembrance Tear"] * extra_tear_count
        )



        requested_extra_coin_purses = (
            self.options.extra_coin_purses.value
        )

        available_filler_slots = (
            location_count - len(fixed_item_names)
        )

        extra_coin_purse_count = min(
            requested_extra_coin_purses,
            available_filler_slots,
        )

        fixed_item_names.extend(
            ["Coin Purse"] * extra_coin_purse_count
        )



        requested_extra_stats = (
            self.options.extra_stats
        )

        available_filler_slots = (
            location_count - len(fixed_item_names)
        )

        extra_stats_count = min(
            requested_extra_stats*10,
            available_filler_slots,
        )

        extra_stats_count = extra_stats_count // 10


        fixed_item_names.extend(
            ["Vigor"] * extra_stats_count
        )
        fixed_item_names.extend(
            ["Violence"] * extra_stats_count
        )
        fixed_item_names.extend(
            ["Dexterity"] * extra_stats_count
        )
        fixed_item_names.extend(
            ["Weirdness"] * extra_stats_count
        )
        fixed_item_names.extend(
            ["Ascend"] * extra_stats_count
        )
        fixed_item_names.extend(
            ["Warding"] * extra_stats_count
        )
        fixed_item_names.extend(
            ["Fortune"] * extra_stats_count
        )
        fixed_item_names.extend(
            ["Fortitude"] * extra_stats_count
        )
        fixed_item_names.extend(
            ["Immunity"] * extra_stats_count
        )
        fixed_item_names.extend(
            ["Agility"] * extra_stats_count
        )

        # Add all mandatory/fixed items
        for item_name in fixed_item_names:
            self.multiworld.itempool.append(
                self.create_item(item_name)
            )

        # Fill every remaining location with normal filler.
        filler_count = (
            location_count - len(fixed_item_names)
        )

        for _ in range(filler_count):
            self.multiworld.itempool.append(
                self.create_item(
                    self.get_filler_item_name()
                )
            )

    def set_rules(self) -> None:
        required_event_items = tuple(
            GOAL_DEFINITIONS[goal_name]["event_item"]
            for goal_name
            in self.options.completion_goals.value
        )

        if not required_event_items:
            raise RuntimeError(
                "At least one Withering Rooms completion "
                "goal must be selected."
            )

        self.multiworld.completion_condition[
            self.player
        ] = lambda state: all(
            state.has(
                event_item_name,
                self.player,
            )
            for event_item_name
            in required_event_items
        )

    
    def generate_early(self) -> None:
        if not self.options.completion_goals.value:
            raise RuntimeError(
                "At least one Withering Rooms completion "
                "goal must be selected."
            )

        # Guarantee an attempt to place one of the two
        # early hallway escape keys in our own first sphere.
        escape_key = self.random.choice((
            "Blue Secret Passage Key",
            "East Stairwell Key",
        ))

        self.multiworld.early_items[self.player][
            escape_key
        ] = 1

        # Make the Chapter 1 exit item available in
        # the multiworld's first logical sphere.
        self.multiworld.early_items[self.player][
            "Right Idol Eye"
        ] = 1
