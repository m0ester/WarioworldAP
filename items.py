from typing import Any, NamedTuple, TYPE_CHECKING
from enum import Enum
from BaseClassees import ItemClassification as IC
from gamedata import Treasure, Spriteling, BossMedal, StageDoor
	
class ItemType(Enum):
	SPRITELING = 0
	TREASURE = 1
	RED_DIAMOND = 2
	BOSS_MEDAL = 3
	DOOR = 4
	STATUE_PIECE = 5

class WwItemData(NamedTuple):
    type: str
    classification: IC
    quantity: int