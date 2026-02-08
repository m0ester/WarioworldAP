from typing import ClassVar, Any
import zipfile
import yaml
import os
from base64 import b64encode
from Utils import visualize_regions as visualise_regions
from BaseClasses import Item
from BaseClasses import ItemClassification as IC
from BaseClasses import Region, Tutorial
from worlds.AutoWorld import WebWorld, World
from worlds.LauncherComponents import Component, icon_paths, Type, components, launch_subprocess
from worlds.Files import APPlayerContainer

from .Items import WwItem, create_item, create_items, create_filler
from .Locations import WwLocation
from .gamedata import CHECK_TABLE, ITEM_TABLE, FILLER_TABLE, BigKeys, Spriteling
from .Settings import WwOptions
from .Regions import create_regions, connect_regions
from .Rules import set_rules

VERSION: tuple[int, int, int] = (0, 1, 2)

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

    def set_spriteling_classification(self, name: str) -> IC | None:
        adjusted_classification = None
        if self.options.endingtype.value in {0, 1}:
            adjusted_classification = IC.filler
        return adjusted_classification

    #def set_classification(self, name: str) -> IC | None:

        classification = ITEM_TABLE[name].classification
        if isinstance(ITEM_TABLE[name], Spriteling):
            if self.options.endingtype == 0 | 1:
                classification = IC.filler
            return classification
        else:
            return classification

    def create_item(self, name):
        return create_item(self, name)

    def create_items(self):
        givenkeys = []
        if self.options.big_key_fragments:
            givenkeys = self.random.sample(BigKeys, k=self.options.big_key_fragments.value)
            for key in givenkeys:
                self.push_precollected(Item(key, IC.progression, self.item_name_to_id[key], self.player))
        create_items(self, givenkeys)

    def set_rules(self):
        Rules.set_rules(self)

    def fill_slot_data(self) -> dict[str, any]:
        visualise_regions(self.multiworld.get_region("Menu", self.player), f"Player{self.player}.puml",
            show_entrance_names=True,
            regions_to_highlight=self.multiworld.get_all_state(self.player).reachable_regions[
                self.player])
        return{
            "death_link": self.options.death_link.value,
            "big key fragments": self.options.big_key_fragments.value,
            "spriteling requirement": self.options.endingtype.value,
        }

    #def create_event(self):
     #   Event.create_event(self)
    def generate_output(self, output_directory: str) -> None:
        multiworld = self.multiworld
        player = self.player
        # Output seed name and slot number to seed RNG in randomiser client.
        output_data = {
            "Version": list(VERSION),
            "Seed": multiworld.seed_name,
            "Slot": player,
            "Name": self.player_name,
            "Locations": {},
            "Entrances": {},
        }
        #apww = WwContainer(
         #   path=os.path.join(
          #      output_directory, f"{multiworld.get_out_file_name_base(player)}{WwContainer.patch_file_ending}"
           # ),
            #player=player,
            #player_name=self.player_name,
            #data=output_data
        #)
        #apww.write()


class WwContainer(APPlayerContainer):
    """
    This class defines the container file for Warioworld.
    """

    game: str = "Warioworld"
    patch_file_ending: str = ".apww"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        if "data" in kwargs:
            self.data = kwargs["data"]
            del kwargs["data"]

        super().__init__(*args, **kwargs)

    def write_contents(self, opened_zipfile: zipfile.ZipFile) -> None:
        """
        Write the contents of the container file.
        """
        super().write_contents(opened_zipfile)

        # Record the data for the game under the key `plando`.
        opened_zipfile.writestr("plando", b64encode(bytes(yaml.safe_dump(self.data, sort_keys=False), "utf-8")))