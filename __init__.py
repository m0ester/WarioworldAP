import os
from base64 import b64encode
from collections.abc import Mapping
from dataclasses import fields
from typing import Any, ClassVar

import yaml

from BaseClasses import Item
from BaseClasses import ItemClassification as IC
from BaseClasses import MultiWorld, Region, Tutorial
from Options import Toggle
from worlds.AutoWorld import WebWorld, World
from worlds.generic.Rules import add_item_rule
from worlds.LauncherComponents import Component, SuffixIdentifier, Type, components, launch_subprocess

from .items import WwItem
from .locations import WwLocation
from .gamedata import CHECK_TABLE, ITEM_TABLE
from .Options import WwOptions
from .Rules import set_rules

def run_client() -> None:
    """
    Launch the Warioworld client.
    """
    print("Running Warioworld Client")
    from .WwClient import main

    launch_subprocess(main, name="TheWindWakerClient")


components.append(
    Component(
        "Warioworld Client", func=run_client, component_type=Type.CLIENT, file_identifier=SuffixIdentifier(".apww")
    )
)

class WwWorld(World):
    options_dataclass = WwOptions
    options: WwOptions

    game: ClassVar[str] = "Warioworld"
    topology_present: bool = True

    item_name_to_id: ClassVar[dict[str, int]] = {
        name: WwItem.get_apid(data.code) for name, data in ITEM_TABLE.items() if data.code is not None
    }
    location_name_to_id: ClassVar[dict[str, int]] = {
        name: WwLocation.get_apid(data.code) for name, data in CHECK_TABLE.items() if data.code is not None
    }

    item_name_groups: ClassVar[dict[str, set[str]]]

    required_client_version: tuple[int, int, int] = (0, 6, 5)

    origin_region_name: str = "Overworld"

    set_rules = set_rules

    def setup_base_regions(self) -> None:

        def get_access_rule(region: str) -> str:
            snake_case_region = region.lower().replace("'", "").replace(" ", "_")
            return f"can_access_{snake_case_region}"

        multiworld = self.multiworld
        player = self.player

        # "The Overworld" region contains all locations that are not in a randomizable region.
        Overworld = Region("Overworld", player, multiworld)
        multiworld.regions.append(Overworld)
        #for stages that require keys
        GF = Region("Greenhorn Forest", player, multiworld)
        GR = Region("Greenhorn Ruins", player, multiworld)
        DS = Region("Dinomighty's Showdown", player, multiworld)
        HM = Region("Horror Manor", player, multiworld)
        WC = Region("Wonky Circus", player, multiworld)
        DD = Region("Dual Dragon's Showdown", player, multiworld)


    def create_regions(self) -> None:
        """
        Create and connect regions for the The Wind Waker world.

        This method first randomizes the charts and picks the required bosses if these options are enabled.
        It then loops through all the world's progress locations and creates the locations, assigning dungeon locations
        to their respective dungeons.
        Finally, the flags for sunken treasure locations are updated as appropriate, and the entrances are randomized
        if that option is enabled.
        """
        self.setup_base_regions()

        player = self.player
        options = self.options

        # Assign each location to their region.
        for location_name in sorted(self.progress_locations):
            data = CHECK_TABLE[location_name]

            region = self.get_region(data.region)
            location = WwLocation(player, location_name, region, data)

    def determine_item_classification(self, name: str) -> IC | None:
        adjusted_classification = None
        if self.options.ending == 0 | 1:
            adjusted_classification = IC.filler
        return adjusted_classification
    
    def create_item(self, name):
        """
        Create an item for this world type and player.

        :param name: The name of the item to create.
        :raises KeyError: If an invalid item name is provided.
        """
        if name in ITEM_TABLE:
            return WwItem(name, self.player, ITEM_TABLE[name], self.determine_item_classification(name))
        raise KeyError(f"Invalid item name: {name}")
    