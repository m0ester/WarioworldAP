from typing import Optional
from BaseClasses import Item, ItemClassification as IC
from .gamedata import ITEM_TABLE, FILLER_TABLE, NET_TABLE, Spriteling, Treasure, BossMedal, StageDoor, Junk, Trap, RedDiamond, StatuePart

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

    def __init__(self, name: str, player: int, data: Spriteling | Junk | Trap | Treasure | BossMedal | RedDiamond | StatuePart | StageDoor,
                 classification: IC | None = None) -> None:
        super().__init__(
            name,
            data.classification if classification is None else classification,
            data.ItemID,
            player,
        )
        self.itemtype = data.ItemType
        self.itemID = data.ItemID
        self.memvalue = data.memvalue
        self.address = data.memloc


LOOKUP_ID_TO_NAME: dict[int, str] = {
    data.ItemID: item for item, data in NET_TABLE.items() if data.ItemID is not None
}


def create_item(world, name):
    if name in ITEM_TABLE:
        if isinstance(ITEM_TABLE[name], Spriteling):
            return WwItem(name, world.player, ITEM_TABLE[name], world.set_spriteling_classification(name))
        else:
            return WwItem(name, world.player, ITEM_TABLE[name], ITEM_TABLE[name].classification)
    raise KeyError(f"Invalid item name: {name}")


def create_filler(world, name):
    if name in FILLER_TABLE:
        return WwItem(name, world.player, FILLER_TABLE[name], FILLER_TABLE[name].classification)
    raise KeyError(f"Invalid item name: {name}")


def create_items(world, givenkeys) -> None:
    itemlist: list[WwItem] = []
    for item in ITEM_TABLE:
        if item not in givenkeys:
            itemlist.append(world.create_item(item))
    #filler item generation to fill remaining checks
    totalitems = len(itemlist)
    print(totalitems)
    itemlist += [create_filler(world, world.random.choice(list(FILLER_TABLE.keys()))) for _ in
        range(len(world.multiworld.get_unfilled_locations(world.player)) - totalitems)]

    world.multiworld.itempool += itemlist