from typing import NamedTuple

class Treasure(NamedTuple):
    """loc is vanilla location"""
    loc: int
    value: int
    name: str

Treasures_h = [
    Treasure(0x801ce3b8,	1,	"Ruby"),
    Treasure(0x801ce3b8,	2,	"Opal"),
    Treasure(0x801ce3b8,	4,	"Amethyst"),
    Treasure(0x801ce3b8,	8,	"Amber"),
    Treasure(0x801ce3b8,	10,	"Sapphire"),
    Treasure(0x801ce3b8,	20,	"Topaz"),
    Treasure(0x801ce3b8,	40,	"Emerald"),
    Treasure(0x801ce3b8,	80,	"Diamond"),
    Treasure(0x801ce3c8,	1,	"Porcelain Urn"),
    Treasure(0x801ce3c8,	2,	"Fine China"),
    Treasure(0x801ce3c8,	4,	"Ceramic Vase"),
    Treasure(0x801ce3c8,	8,	"Teapot"),
    Treasure(0x801ce3c8,	10,	"Vase"),
    Treasure(0x801ce3c8,	20,	"Precious Pot"),
    Treasure(0x801ce3c8,	40,	"Lucky Figurine"),
    Treasure(0x801ce3c8,	80,	"NES"),
    Treasure(0x801ce3e8,	1,	"Candlestick"),
    Treasure(0x801ce3e8,	2,	"Silver Candlestick"),
    Treasure(0x801ce3e8,	4,	"Forest Painting"),
    Treasure(0x801ce3e8,	8,	"Castle Painting"),
    Treasure(0x801ce3e8,	10,	"Crystal Ball"),
    Treasure(0x801ce3e8,	20,	"Knight's Helmet"),
    Treasure(0x801ce3e8,	40,	"Gladiator's Helmet"),
    Treasure(0x801ce3e8,	80,	"Ornate Bag"),
    Treasure(0x801ce3f8,	1,	"Bugle"),
    Treasure(0x801ce3f8,	2,	"Tambourine"),
    Treasure(0x801ce3f8,	4,	"Triangle"),
    Treasure(0x801ce3f8,	8,	"Clarinet"),
    Treasure(0x801ce3f8,	10,	"Trombone"),
    Treasure(0x801ce3f8,	20,	"Saxophone"),
    Treasure(0x801ce3f8,	40,	"Drum"),
    Treasure(0x801ce3f8,	80,	"Nintendo64"),
    Treasure(0x801ce418,	1,	"Nice Glass"),
    Treasure(0x801ce418,	2,	"Ancient Chalice"),
    Treasure(0x801ce418,	4,	"Nice Cup"),
    Treasure(0x801ce418,	8,	"Ornate Decanter"),
    Treasure(0x801ce418,	10,	"Glass Decanter"),
    Treasure(0x801ce418,	20,	"Nice Saucer"),
    Treasure(0x801ce418,	40,	"Glass Bowl"),
    Treasure(0x801ce418,	80,	"Jade Box"),
    Treasure(0x801ce428,	1,	"Nice Goblet"),
    Treasure(0x801ce428,	2,	"Violin"),
    Treasure(0x801ce428,	4,	"Earring"),
    Treasure(0x801ce428,	8,	"Jewelled Sword"),
    Treasure(0x801ce428,	10,	"Gold Tiara"),
    Treasure(0x801ce428,	20,	"Nice Sceptre"),
    Treasure(0x801ce428,	40,	"King's Crown"),
    Treasure(0x801ce428,	80,	"GameBoy Advance"),
    Treasure(0x801ce448,	1,	"Big Mirror"),
    Treasure(0x801ce448,	2,	"Antique Clock"),
    Treasure(0x801ce448,	4,	"Gold Mirror"),
    Treasure(0x801ce448,	8,	"Stained Glass"),
    Treasure(0x801ce448,	10,	"Bronze Mirror"),
    Treasure(0x801ce448,	20,	"Gold Clock"),
    Treasure(0x801ce448,	40,	"Gold Pocketwatch"),
    Treasure(0x801ce448,	80,	"Crazy Glasses"),
    Treasure(0x801ce458,	1,	"Ancient Ring"),
    Treasure(0x801ce458,	2,	"Ancient Necklace"),
    Treasure(0x801ce458,	4,	"Ancient Relief"),
    Treasure(0x801ce458,	8,	"Small Pyramid"),
    Treasure(0x801ce458,	10,	"Ancient Bracelet"),
    Treasure(0x801ce458,	20,	"Anubis Statue"),
    Treasure(0x801ce458,	40,	"Monarch Mask"),
    Treasure(0x801ce458,	80,	"Nintendo GameCube"),]

class TreasureCheck(NamedTuple):
    value: int
    name: str
    loc: int

Chests_b = [
    TreasureCheck(1,	"Greenhorn Forest Red Chest",	0x801ce408),
    TreasureCheck(2,	"Greenhorn Forest Yellow Chest",	0x801ce408),
    TreasureCheck(4,	"Greenhorn Forest Chartreuse Chest",	0x801ce408),
    TreasureCheck(8,	"Greenhorn Forest Green Chest",	0x801ce408),
    TreasureCheck(10,	"Greenhorn Forest Cyan Chest",	0x801ce408),
    TreasureCheck(20,	"Greenhorn Forest Blue Chest",	0x801ce408),
    TreasureCheck(40,	"Greenhorn Forest Purple Chest",	0x801ce408),
    TreasureCheck(80,	"Greenhorn Forest Pink Chest",	0x801ce408),
    TreasureCheck(1,	"Greenhorn Ruins Red Chest",	0x801ce409),
    TreasureCheck(2,	"Greenhorn Ruins Yellow Chest",	0x801ce409),
    TreasureCheck(4,	"Greenhorn Ruins Chartreuse Chest",	0x801ce409),
    TreasureCheck(8,	"Greenhorn Ruins Green Chest",	0x801ce409),
    TreasureCheck(10,	"Greenhorn Ruins Cyan Chest",	0x801ce409),
    TreasureCheck(20,	"Greenhorn Ruins Blue Chest",	0x801ce409),
    TreasureCheck(40,	"Greenhorn Ruins Purple Chest",	0x801ce409),
    TreasureCheck(80,	"Greenhorn Ruins Pink Chest",	0x801ce409),
    TreasureCheck(1,	"Horror Manor Red Chest",	0x801ce40a),
    TreasureCheck(2,	"Horror Manor Yellow Chest",	0x801ce40a),
    TreasureCheck(4,	"Horror Manor Chartreuse Chest",	0x801ce40a),
    TreasureCheck(8,	"Horror Manor Green Chest",	0x801ce40a),
    TreasureCheck(10,	"Horror Manor Cyan Chest",	0x801ce40a),
    TreasureCheck(20,	"Horror Manor Blue Chest",	0x801ce40a),
    TreasureCheck(40,	"Horror Manor Purple Chest",	0x801ce40a),
    TreasureCheck(80,	"Horror Manor Pink Chest",	0x801ce40a),
    TreasureCheck(1,	"Wonky Circus Red Chest",	0x801ce40b),
    TreasureCheck(2,	"Wonky Circus Yellow Chest",	0x801ce40b),
    TreasureCheck(4,	"Wonky Circus Chartreuse Chest",	0x801ce40b),
    TreasureCheck(8,	"Wonky Circus Green Chest",	0x801ce40b),
    TreasureCheck(10,	"Wonky Circus Cyan Chest",	0x801ce40b),
    TreasureCheck(20,	"Wonky Circus Blue Chest",	0x801ce40b),
    TreasureCheck(40,	"Wonky Circus Purple Chest",	0x801ce40b),
    TreasureCheck(80,	"Wonky Circus Pink Chest",	0x801ce40b),
    TreasureCheck(1,	"Shivering Mountains Red Chest",	0x801ce40c),
    TreasureCheck(2,	"Shivering Mountains Yellow Chest",	0x801ce40c),
    TreasureCheck(4,	"Shivering Mountains Chartreuse Chest",	0x801ce40c),
    TreasureCheck(8,	"Shivering Mountains Green Chest",	0x801ce40c),
    TreasureCheck(10,	"Shivering Mountains Cyan Chest",	0x801ce40c),
    TreasureCheck(20,	"Shivering Mountains Blue Chest",	0x801ce40c),
    TreasureCheck(40,	"Shivering Mountains Purple Chest",	0x801ce40c),
    TreasureCheck(80,	"Shivering Mountains Pink Chest",	0x801ce40c),
    TreasureCheck(1,	"Beanstalk Way Red Chest",	0x801ce40d),
    TreasureCheck(2,	"Beanstalk Way Yellow Chest",	0x801ce40d),
    TreasureCheck(4,	"Beanstalk Way Chartreuse Chest",	0x801ce40d),
    TreasureCheck(8,	"Beanstalk Way Green Chest",	0x801ce40d),
    TreasureCheck(10,	"Beanstalk Way Cyan Chest",	0x801ce40d),
    TreasureCheck(20,	"Beanstalk Way Blue Chest",	0x801ce40d),
    TreasureCheck(40,	"Beanstalk Way Purple Chest",	0x801ce40d),
    TreasureCheck(80,	"Beanstalk Way Pink Chest",	0x801ce40d),
    TreasureCheck(1,	"Mirror Mansion Red Chest",	0x801ce40e),
    TreasureCheck(2,	"Mirror Mansion Yellow Chest",	0x801ce40e),
    TreasureCheck(4,	"Mirror Mansion Chartreuse Chest",	0x801ce40e),
    TreasureCheck(8,	"Mirror Mansion Green Chest",	0x801ce40e),
    TreasureCheck(10,	"Mirror Mansion Cyan Chest",	0x801ce40e),
    TreasureCheck(20,	"Mirror Mansion Blue Chest",	0x801ce40e),
    TreasureCheck(40,	"Mirror Mansion Purple Chest",	0x801ce40e),
    TreasureCheck(80,	"Mirror Mansion Pink Chest",	0x801ce40e),
    TreasureCheck(1,	"Pecan Sands Red Chest",	0x801ce40f),
    TreasureCheck(2,	"Pecan Sands Yellow Chest",	0x801ce40f),
    TreasureCheck(4,	"Pecan Sands Chartreuse Chest",	0x801ce40f),
    TreasureCheck(8,	"Pecan Sands Green Chest",	0x801ce40f),
    TreasureCheck(10,	"Pecan Sands Cyan Chest",	0x801ce40f),
    TreasureCheck(20,	"Pecan Sands Blue Chest",	0x801ce40f),
    TreasureCheck(40,	"Pecan Sands Purple Chest",	0x801ce40f),
    TreasureCheck(80,	"Pecan Sands Pink Chest",	0x801ce40f),]

class Spriteling(NamedTuple):
    """loc is vanilla location"""
    loc: int
    value: int
    name: str

Spritelings_h = [
    Spriteling(0x801ce3b4,	1,	"Greenhorn Forest Red Spriteling"),
    Spriteling(0x801ce3b4,	2,	"Greenhorn Forest Yellow Spriteling"),
    Spriteling(0x801ce3b4,	4,	"Greenhorn Forest Green Spriteling"),
    Spriteling(0x801ce3b4,	8,	"Greenhorn Forest Blue Spriteling"),
    Spriteling(0x801ce3b4,	10,	"Greenhorn Forest Purple Spriteling"),
    Spriteling(0x801ce3c4,	1,	"Greenhorn Ruins Red Spriteling"),
    Spriteling(0x801ce3c4,	2,	"Greenhorn Ruins Yellow Spriteling"),
    Spriteling(0x801ce3c4,	4,	"Greenhorn Ruins Green Spriteling"),
    Spriteling(0x801ce3c4,	8,	"Greenhorn Ruins Blue Spriteling"),
    Spriteling(0x801ce3c4,	10,	"Greenhorn Ruins Purple Spriteling"),
    Spriteling(0x801ce3e4,	1,	"Horror Manor Red Spriteling"),
    Spriteling(0x801ce3e4,	2,	"Horror Manor Yellow Spriteling"),
    Spriteling(0x801ce3e4,	4,	"Horror Manor Green Spriteling"),
    Spriteling(0x801ce3e4,	8,	"Horror Manor Blue Spriteling"),
    Spriteling(0x801ce3e4,	10,	"Horror Manor Purple Spriteling"),
    Spriteling(0x801ce3f4,	1,	"Wonky Circus Red Spriteling"),
    Spriteling(0x801ce3f4,	2,	"Wonky Circus Yellow Spriteling"),
    Spriteling(0x801ce3f4,	4,	"Wonky Circus Green Spriteling"),
    Spriteling(0x801ce3f4,	8,	"Wonky Circus Blue Spriteling"),
    Spriteling(0x801ce3f4,	10,	"Wonky Circus Purple Spriteling"),
    Spriteling(0x801ce414,	1,	"Shivering Mountains Red Spriteling"),
    Spriteling(0x801ce414,	2,	"Shivering Mountains Yellow Spriteling"),
    Spriteling(0x801ce414,	4,	"Shivering Mountains Green Spriteling"),
    Spriteling(0x801ce414,	8,	"Shivering Mountains Blue Spriteling"),
    Spriteling(0x801ce414,	10,	"Shivering Mountains Purple Spriteling"),
    Spriteling(0x801ce424,	1,	"Beanstalk Way Red Spriteling"),
    Spriteling(0x801ce424,	2,	"Beanstalk Way Yellow Spriteling"),
    Spriteling(0x801ce424,	4,	"Beanstalk Way Green Spriteling"),
    Spriteling(0x801ce424,	8,	"Beanstalk Way Blue Spriteling"),
    Spriteling(0x801ce424,	10,	"Beanstalk Way Purple Spriteling"),
    Spriteling(0x801ce444,	2,	"Mirror Mansion Yellow Spriteling"),
    Spriteling(0x801ce444,	4,	"Mirror Mansion Green Spriteling"),
    Spriteling(0x801ce444,	8,	"Mirror Mansion Blue Spriteling"),
    Spriteling(0x801ce444,	10,	"Mirror Mansion Purple Spriteling"),
    Spriteling(0x801ce454,	1,	"Pecan Way Red Spriteling"),
    Spriteling(0x801ce454,	2,	"Pecan Way Yellow Spriteling"),
    Spriteling(0x801ce454,	4,	"Pecan Way Green Spriteling"),
    Spriteling(0x801ce454,	8,	"Pecan Way Blue Spriteling"),
    Spriteling(0x801ce454,	10,	"Pecan Way Purple Spriteling"),]

class Cage(NamedTuple):
    value: int
    name: str
    loc: int

Cages_b = [ 

    Cage(1,	"Greenhorn Forest Caged Red Spriteling",	0x801ce3d8),
    Cage(2,	"Greenhorn Forest Caged Yellow Spriteling",	0x801ce3d8),
    Cage(4,	"Greenhorn Forest Caged Green Spriteling",	0x801ce3d8),
    Cage(8,	"Greenhorn Forest Caged Blue Spriteling",	0x801ce3d8),
    Cage(10,	"Greenhorn Forest Caged Purple Spriteling",	0x801ce3d8),
    Cage(1,	"Greenhorn Ruins Caged Red Spriteling",	0x801ce3d9),
    Cage(2,	"Greenhorn Ruins Caged Yellow Spriteling",	0x801ce3d9),
    Cage(4,	"Greenhorn Ruins Caged Green Spriteling",	0x801ce3d9),
    Cage(8,	"Greenhorn Ruins Caged Blue Spriteling",	0x801ce3d9),
    Cage(10,	"Greenhorn Ruins Caged Purple Spriteling",	0x801ce3d9),
    Cage(1,	"Horror Manor Caged Red Spriteling",	0x801ce3da),
    Cage(2,	"Horror Manor Caged Yellow Spriteling",	0x801ce3da),
    Cage(4,	"Horror Manor Caged Green Spriteling",	0x801ce3da),
    Cage(8,	"Horror Manor Caged Blue Spriteling",	0x801ce3da),
    Cage(10,	"Horror Manor Caged Purple Spriteling",	0x801ce3da),
    Cage(1,	"Wonky Circus Caged Red Spriteling",	0x801ce3db),
    Cage(2,	"Wonky Circus Caged Yellow Spriteling",	0x801ce3db),
    Cage(4,	"Wonky Circus Caged Green Spriteling",	0x801ce3db),
    Cage(8,	"Wonky Circus Caged Blue Spriteling",	0x801ce3db),
    Cage(10,	"Wonky Circus Caged Purple Spriteling",	0x801ce3db),
    Cage(1,	"Shivering Mountains Caged Red Spriteling",	0x801ce3dc),
    Cage(2,	"Shivering Mountains Caged Yellow Spriteling",	0x801ce3dc),
    Cage(4,	"Shivering Mountains Caged Green Spriteling",	0x801ce3dc),
    Cage(8,	"Shivering Mountains Caged Blue Spriteling",	0x801ce3dc),
    Cage(10,	"Shivering Mountains Caged Purple Spriteling",	0x801ce3dc),
    Cage(1,	"Beanstalk Way Caged Red Spriteling",	0x801ce3dd),
    Cage(2,	"Beanstalk Way Caged Yellow Spriteling",	0x801ce3dd),
    Cage(4,	"Beanstalk Way Caged Green Spriteling",	0x801ce3dd),
    Cage(8,	"Beanstalk Way Caged Blue Spriteling",	0x801ce3dd),
    Cage(10,	"Beanstalk Way Caged Purple Spriteling",	0x801ce3dd),
    Cage(1,	"Mirror Mansion Caged Red Spriteling",	0x801ce3de),
    Cage(2,	"Mirror Mansion Caged Yellow Spriteling",	0x801ce3de),
    Cage(4,	"Mirror Mansion Caged Green Spriteling",	0x801ce3de),
    Cage(8,	"Mirror Mansion Caged Blue Spriteling",	0x801ce3de),
    Cage(10,	"Mirror Mansion Caged Purple Spriteling",	0x801ce3de),
    Cage(1,	"Pecan Way Caged Red Spriteling",	0x801ce3df),
    Cage(2,	"Pecan Way Caged Yellow Spriteling",	0x801ce3df),
    Cage(4,	"Pecan Way Caged Green Spriteling",	0x801ce3df),
    Cage(8,	"Pecan Way Caged Blue Spriteling",	0x801ce3df),
    Cage(10,	"Pecan Way Caged Purple Spriteling",	0x801ce3df),]

class BossMedal(NamedTuple):
    loc = 0x801ce3ac
    value: int
    name: str

BossMedals_h = [
    BossMedal(1,	"Greenfist Boss Medal"),
    BossMedal(2,	"Sandworm Boss Medal"),
    BossMedal(4,	"DinoMighty Big Key Fragment"),
    BossMedal(8,	"Brawl Doll Boss Medal"),
    BossMedal(10,	"Clown-a-Round Boss Medal"),
    BossMedal(20,	"Dual Dragon Big Key Fragment"),
    BossMedal(40,	"Winter Windster Boss Medal"),
    BossMedal(80,	"Spideraticus Boss Medal"),
    BossMedal(100,	"Red-Brief J Big Key Fragment"),
    BossMedal(200,	"The Mean Emcee Boss Medal"),
    BossMedal(400,	"Ironsider Boss Medal"),
    BossMedal(800,	"Captain Skull Big Key Fragment"),]

class StageDoor(NamedTuple):
    loc = 0x801ce3d0
    value: int
    name: str

Doors_b = [
    StageDoor(1,	"Greenhorn Ruins Door"),
    StageDoor(2,	"DinoMighty's Showdown Door"),
    StageDoor(4,	"Horror Manor Door"),
    StageDoor(8,	"Wonky Circus Door"),
    StageDoor(10,	"Dual Dragon's Showdown Door"),
    StageDoor(20,	"Shivering Mountains Door"),
    StageDoor(40,	"Beanstalk Way Door"),
    StageDoor(80,	"Red-Brief J's Showdown Door"),
    StageDoor(100,	"Mirror Mansion Door"),
    StageDoor(200,	"Pecan Sands Door"),
    StageDoor(400,	"Captain Skull's Showdown Door"),]

class BossBeat(NamedTuple):
    loc = 0x801ce3d2
    value: int
    name: str

Bosses_b = [
    BossBeat(1,	"Defeated Greenfist"),
    BossBeat(2,	"Defeated Sandworm"),
    BossBeat(4,	"Defeated DinoMighty"),
    BossBeat(8,	"Defeated Brawl Doll"),
    BossBeat(10,	"Defeated Clown-a-Round"),
    BossBeat(20,	"Defeated Dual Dragon"),
    BossBeat(80,	"Defeated Spideraticus"),
    BossBeat(100,	"Defeated Red-Brief J"),
    BossBeat(200,	"Defeated The Mean Emcee"),
    BossBeat(400,	"Defeated Ironsider"),
    BossBeat(800,	"Defeated Captain Skull"),]