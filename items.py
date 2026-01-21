from typing import Any, NamedTuple, TYPE_CHECKING
from enum import Enum
from BaseClasses import Item, ItemClassification as IC
import gamedata

PROG = IC.progression
FILL = IC.filler
USEF = IC.useful
SKIP = IC.skip_balancing
TRAP = IC.trap

class ItemType(Enum):
	SPRITELING = 0
	TREASURE = 1
	RED_DIAMOND = 2
	BOSS_MEDAL = 3
	DOOR = 4
	STATUE_PIECE = 5
    OTHER = 6

class WwItemData(NamedTuple):
    type: str
    classification: IC
    quantity: int
    address: int = 0
    item_type: ItemType = ItemType.OTHER

class WwItem(Item):
	game: str = "Warioworld"

	def __init__(self, name: str, player: int, data: WwItemData, classification: Optional[IC] = None) -> None:
		super().__init__(
			name,
			data.classification if classification is None else classification,
			None if data.code is None else WwItem.get_Apid(data.code),
		)
	
	def get_apID(code: int) -> int:
		"""retrieve the ap ID"""