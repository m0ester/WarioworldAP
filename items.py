from typing import Any, NamedTuple, TYPE_CHECKING
from enum import Enum
from BaseClasses import ItemClassification as IC
import gamedata
	
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

def get_spriteling(spriteling: str, stage: str) -> str:
      return f"(spriteling) in (stage)"

data_table: list[WwItemData] = [
      
]