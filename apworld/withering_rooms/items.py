from BaseClasses import Item

from .data import RANDOMIZED_ITEMS


GAME_NAME = "Withering Rooms"


class WitheringRoomsItem(Item):
    game = GAME_NAME


ITEM_NAME_TO_ID = {
    name: data.item_id
    for name, data in RANDOMIZED_ITEMS.items()
}