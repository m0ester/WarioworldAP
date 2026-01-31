from Cython.Shadow import address
from BaseClasses import Location
from .gamedata import Chest, Cage, BossBeat
import inspect
class WwLocation(Location):
    game: str = "Warioworld"

    def __init__(self, player: int, name: str, data: Chest | Cage | BossBeat):
        address = None if data.CheckID is None else WwLocation.get_apid(data.CheckID)
        super().__init__(player, name, address=address)
        #PUT REGIONS IN THE GAMEDATA CHECKS
        self.code = data.CheckID
        self.region = data.region
        self.bit = data.memvalue
        self.address = self.address
    @staticmethod
    def get_apid(code: int) -> int:

        base_id=2326528
        return base_id + code

boss_to_stage: dict [str, str] ={
        "Defeated Greenfist" : "Greenhorn Forest",
        "Defeated Sandworm" : "Greenhorn Ruins",
        "Defeated Dinomighty" : "Dinomighty's Showdown",
        "Defeated Brawl Doll":  "Horror Manor",
        "Defeated Clown-a-Round":  "Wonky Circus",
        "Defeated Dual Dragon":     "Dual Dragon's Showdown",
        "Defeated Winter Windster": "Shivering Mountains",
        "Defeated Spideraticus":    "Beanstalk Way",
        "Defeated Red-Brief J":     "Red-Brief J's Showdown",
        "Defeated The Mean Emcee":  "Mirror Mansion",
        "Defeated Ironsider":       "Pecan Sands",
        "Defeated Captain Skull":   "Captain Skull's Showdown",
}