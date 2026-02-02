from BaseClasses import Location
from .gamedata import CHECK
from .regions import *

class WwLocation(Location):
    game: str = "Warioworld"

 #   def __init__(self, player: int, name: str, parent: Region, data: CHECK):
  #      address = None if data.CheckID is None else WwLocation.get_apid(data.CheckID)
   #     super().__init__(player, name, address=address)
    #    self.code = data.CheckID
     #   self.region = data.region
      #  self.bit = data.memvalue
       # self.address = data.memloc

    #@staticmethod
    #def get_apid(code: int) -> int:
     #   return code

