from typing import TYPE_CHECKING
from collections.abc import Callable
from BaseClasses import CollectionState, Item, MultiWorld
from . import locations, items, Options
from worlds.AutoWorld import LogicMixin
from worlds.generic.Rules import set_rule


class WwLogic(LogicMixin):
    multiworld: MultiWorld
    def isAccessible(self, player: int) -> bool:
        if locations.WwLocation.region == "Greenhorn Forest":
            return True
        if locations.WwLocation.region in items.WwItem.name:
            return True
        else: 
            return False
def set_rules() -> None:

    def set_rule_if_exists(location_name: str, rule: Callable[[CollectionState], bool]) -> None:
        player = self.isAccessible

