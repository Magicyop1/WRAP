from dataclasses import dataclass

from Options import (
    DefaultOnToggle,
    OptionSet,
    PerGameCommonOptions,
    Range,
    Toggle,
)


class CompletionGoals(OptionSet):
    """
    Determines which objectives must be completed to finish
    the Archipelago slot.

    Every listed goal is required.

    Available goals:
    - Priscilla Mostyn
    - God Millie
    """
    display_name = "Completion Goals"

    valid_keys = {
        "Priscilla Mostyn",
        "God Millie",
    }

    default = {
        "Priscilla Mostyn",
    }

class ChallengeStart(Toggle):
    """
    Randomizes the Gatehouse Key and Strange Bedroom Key.

    When disabled, these two early-game keys remain vanilla,
    allowing normal access to the main game immediately.
    """
    display_name = "Challenge Start"


class Loresanity(DefaultOnToggle):
    """Adds Lore entries as Archipelago locations."""
    display_name = "Loresanity"


class Monstersanity(DefaultOnToggle):
    """Adds first-time monster kills as Archipelago locations."""
    display_name = "Monstersanity"


class ExtraRemembranceTears(Range):
    """
    Adds extra Remembrance Tears to the Archipelago item pool, provided there are enough location slots.
    """
    display_name = "Extra Remembrance Tears"
    range_start = 0
    range_end = 10
    default = 0


class ExtraCoinPurses(Range):
    """
    Adds extra Coin Purses to the Archipelago item pool, provided there are enough location slots.
    """
    display_name = "Extra Coin Purses"
    range_start = 0
    range_end = 5
    default = 0


class ExtraStats(Range):
    """
    Adds AP Items that deliver +1 to a given stat. One item for each stat is added for each value of this stat. So if it is set to 4, 40 new items will be added to the pool if possible.
    Can cut down on filler added to pool significantly.
    """
    display_name = "Extra Stats"
    range_start = 0
    range_end = 5
    default = 2



class DeathLink(Toggle):
    """When enabled, deaths are shared with other DeathLink-enabled players."""
    display_name = "DeathLink"
    default = 0



@dataclass
class WitheringRoomsOptions(PerGameCommonOptions):
    challenge_start: ChallengeStart
    loresanity: Loresanity
    monstersanity: Monstersanity
    extra_remembrance_tears: ExtraRemembranceTears
    extra_coin_purses: ExtraCoinPurses
    extra_stats: ExtraStats
    death_link: DeathLink
    completion_goals: CompletionGoals