from typing import ClassVar

from Utils import visualize_regions as visualise_regions
from BaseClasses import Item
from BaseClasses import ItemClassification as IC
from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, icon_paths, Type, components, launch_subprocess

from .Items import WwItem, create_item, create_items, create_filler
from .Locations import WwLocation
from .gamedata import CHECK_TABLE, ITEM_TABLE, FILLER_TABLE, BigKeys
from .Settings import WwOptions
from .Regions import create_regions, connect_regions
from .Rules import set_rules


def run_client() -> None:
    """
    Launch the Warioworld client.
    """
    print("Running Warioworld Client")
    from .WwClient import main

    launch_subprocess(main, name="WarioworldClient")


components.append(
    Component(
        "Warioworld Client", func=run_client, component_type=Type.CLIENT,
        icon = "WwAPlogo",
    )
)
icon_paths["WwAPlogo"] = "ap:worlds.WarioworldAP/icons/logo.png"
class WwWeb(WebWorld):
    """
    This class handles the web interface for The Wind Waker.

    The web interface includes the setup guide and the options page for generating YAMLs.
    """

    tutorials = [
        Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Warioworld Archipelago software on your computer.",
            "English",
            "setup_en.md",
            "setup/en",
            ["tanjo3", "Lunix"],
        )
    ]
    theme = "ocean"
    rich_text_options_doc = True

class WwWorld(World):
    options_dataclass = WwOptions
    options: WwOptions

    game: ClassVar[str] = "Warioworld"
    topology_present: bool = True

    item_name_to_id: ClassVar[dict[str, int]] = {
        name: data.ItemID for name, data in ITEM_TABLE.items() if data.ItemID is not None
    }
    location_name_to_id: ClassVar[dict[str, int]] = {
        name: data.CheckID for name, data in CHECK_TABLE.items() if data.CheckID is not None
    }

    item_name_groups: ClassVar[dict[str, set[str]]]

    required_client_version: tuple[int, int, int] = (0, 6, 5)

    web: ClassVar[WwWeb] = WwWeb()

    #set_rules = set_rules
    def __init__(self, multiworld, player):
        super().__init__(multiworld, player)
        self.itemlist = []

    def create_regions(self) -> None:
        """
        Create and connect regions for the Warioworld world.
        """
        create_regions(self)
        connect_regions(self)

        player = self.player
        options = self.options

        # Assign each location to their region.
        for name,data in CHECK_TABLE.items():
            if data.region is None:
                continue
            region: Region = self.multiworld.get_region(data.region, player)
            location = WwLocation(player, name, data.CheckID, region)
            region.locations.append(location)

    def determine_item_classification(self, name: str) -> IC | None:
        adjusted_classification = None
        if self.options.ending == 0 | 1:
            adjusted_classification = IC.filler
        return adjusted_classification

    def create_item(self, name):
        return create_item(self, name)

    def create_items(self):
        if self.options.big_key_fragments:
            self.random.sample(BigKeys, k=self.options.big_key_fragments.value)
            for key in BigKeys:
                self.push_precollected(Item(key, IC.progression, self.item_name_to_id[key], self.player))
        create_items(self)

    def set_rules(self):
        Rules.set_rules(self)

    def fill_slot_data(self):
        visualise_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml",
            show_entrance_names=True,
            regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                self.player])

    #def create_event(self):
     #   Event.create_event(self)
