from typing import Optional
from BaseClasses import Item, ItemClassification as IC
from .gamedata import ITEM_TABLE, FILLER_TABLE, Spriteling, Treasure, BossMedal, StageDoor, Junk, Trap
from worlds.AutoWorld import World
import dolphin_memory_engine as DME

"logic to set progression value of spritelings depending on settings"
"logic to give player a fixed amount of big keys depending on big keys set"


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

    def __init__(self, name: str, player: int, data: Spriteling | Junk | Trap | Treasure | BossMedal | StageDoor,
                 classification: Optional[IC] = None) -> None:
        super().__init__(
            name,
            data.classification if classification is None else classification,
            None if data.ItemID is None else WwItem.get_apid(data.ItemID),
            player,
        )
        self.itemtype = data.ItemType
        self.item_id = data.memvalue
        self.address = data.memloc

    @staticmethod
    def get_apid(ItemID: int) -> int:
        """
        Compute the Archipelago ID for the given item code.

        :param ItemID: The unique code for the item.
        :return: The computed Archipelago ID.
        """
        #base_id: int = 2322432
        return ItemID

    def get_hpaddress(address) -> int:
        """
        compute dynamic mem address
        """
        if address is None:
            address = DME.read_word(0x801c5820) + 0xd8
        return address

LOOKUP_ID_TO_NAME: dict[int, str] = {
    WwItem.get_apid(data.memvalue): item for item, data in ITEM_TABLE.items() if data.memvalue is not None
}


def create_item(world, name):
    if name in ITEM_TABLE:
        return WwItem(name, world.player, ITEM_TABLE[name], world.determine_item_classification(name))
    raise KeyError(f"Invalid item name: {name}")


def create_filler(world, name):
    if name in FILLER_TABLE:
        return WwItem(name, world.player, FILLER_TABLE[name], world.determine_item_classification(name))
    raise KeyError(f"Invalid item name: {name}")


def create_items(world) -> None:
    itemlist: list[WwItem] = []
    for item in ITEM_TABLE:
        itemlist.append(world.create_item(item))
    #filler item generation to fill remaining checks
    totalitems = len(itemlist)
    itemlist += [world.create_filler() for _ in
        range(len(world.multiworld.get_unfilled_locations(world.player)) - totalitems)]

    world.multiworld.itempool += itemlist