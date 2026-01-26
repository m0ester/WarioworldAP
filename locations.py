from BaseClasses import Location
from gamedata import Chest, Cage, BossBeat

class WwLocation(Location):
    game: str = "Warioworld"

    def __init__(self, player: int, name: str, data: Chest | Cage | BossBeat):
        address = None if data.CheckID is None else address = data.loc
        name=data.name
        super().__init__(player, name, address)

        self.code = data.CheckID
        if isinstance(data.name, BossBeat):
            self.stage_id = data.name.split()[1:]
        else:
            self.stage_id = data.name.split()[:2]
        self.region = self.stage_id
        self.bit = data.value
        self.address = self.address