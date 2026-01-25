from typing import Any, NamedTuple, TYPE_CHECKING, Optional
from enum import Enum
from collections.abc import Iterable
from BaseClasses import Item, ItemClassification as IC
from gamedata import ITEM_TABLE, Spriteling, Junk, Trap, Treasure, BossMedal, StageDoor
from worlds.AutoWorld import World

"logic to set progression value of spritelings depending on settings"
"logic to give player a fixed amount of big keys depending on big keys set"
def generateItem(items: str | Iterable[str], world: World) -> Item | list[Item]:
	"""
    Create items based on their names.
    Depending on the input, this function can return a single item or a list of items.

    :param items: The name or names of the items to create.
    :param world: The game world.
    :raises KeyError: If an unknown item name is provided.
    :return: A single item or a list of items.
    """
	ret: list[Item] = []
	singleton = False
	if isinstance(items, str):
		items = [items]
		singleton = True
	for item in items:
		if item in ITEM_TABLE:
			ret.append(world.create_item(item))
		else:
			raise KeyError(f"Unknown item {item}")

	return ret[0] if singleton else ret


class WwItem(Item):
    """
    This class represents an item in Warioworld.

    :param name: The item's name.
    :param player: The ID of the player who owns the item.
    :param data: The data associated with this item.
    :param classification: Optional classification to override the default.
    """

    game: str = "Warioworld"
    type: Optional[str]

    def __init__(self, name: str, player: int, data: Spriteling | Junk | Trap | Treasure | BossMedal | StageDoor,	classification: Optional[IC] = None) -> None:
        super().__init__(
            name,
            data.classification if classification is None else classification,
            None if data.ItemID is None else WwItem.get_apid(data.ItemID),
            player,
        )

        self.type = data.ItemType
        self.item_id = data.value

    @staticmethod
    def get_apid(code: int) -> int:
        """
        Compute the Archipelago ID for the given item code.

        :param code: The unique code for the item.
        :return: The computed Archipelago ID.
        """
        base_id: int = 2322432
        return base_id + code