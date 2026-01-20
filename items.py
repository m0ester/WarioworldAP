from typing import Any, NamedTuple, TYPE_CHECKING


class WwItem(Item):
    game = str:"Warioworld"
	
class ItemType(Enum):
	SPRITELING = 0
	TREASURE = 1
	RED_DIAMOND = 2
	BOSS_MEDAL = 3
	ENTRANCE = 4
	STATUE_PIECE = 5

class WwItemData(NamedTuple):
    name: str
    classification: int
    address: int
    quantity: int
    item_id: Optional[int]