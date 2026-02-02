from typing import NamedTuple
from BaseClasses import ItemClassification as IC
from dataclasses import dataclass

PROG = IC.progression
FILL = IC.filler
USEF = IC.useful
SKIP = IC.skip_balancing
TRAP = IC.trap

@dataclass
class Treasure():
    """loc is vanilla location
    value is ingame value
    ItemID is archipelago itemcode
    """
    memloc: int
    memvalue: int
    ItemID: int
    classification = FILL
    ItemType = "Treasure"

Treasures_h: dict[str, Treasure] = {
"Ruby": 	Treasure(0x801ce3b8,	1, 1),
"Opal":	Treasure(0x801ce3b8,	2, 2),
"Amethyst":	Treasure(0x801ce3b8,	4, 3),
"Amber":	Treasure(0x801ce3b8,	8,    4),
"Sapphire":	Treasure(0x801ce3b8,	0x10, 5),
"Topaz":	Treasure(0x801ce3b8,	0x20,    6),
"Emerald":	Treasure(0x801ce3b8,	0x40,  7),
"Diamond":	Treasure(0x801ce3b8,	0x80,  8),
"Porcelain Urn":	Treasure(0x801ce3c8,	1,    9),
"Fine China":	Treasure(0x801ce3c8,	2,   10),
"Ceramic Vase":	Treasure(0x801ce3c8,	4, 11),
"Teapot":	Treasure(0x801ce3c8,	8,   12),
"Vase":	Treasure(0x801ce3c8,	0x10, 13),
"Precious Pot":	Treasure(0x801ce3c8,	0x20, 14),
"Lucky Figurine":	Treasure(0x801ce3c8,	0x40,   15),
"NES":	Treasure(0x801ce3c8,	0x80,	16),
"Candlestick":	Treasure(0x801ce3e8,	1,  17),
"Silver Candlestick":	Treasure(0x801ce3e8,	2,   18),
"Forest Painting":	Treasure(0x801ce3e8,	4,  19),
"Castle Painting":	Treasure(0x801ce3e8,	8, 20),
"Crystal Ball":	Treasure(0x801ce3e8,	0x10, 21),
"Knight's Helmet":	Treasure(0x801ce3e8,	0x20,  22),
"Gladiator's Helmet":	Treasure(0x801ce3e8,	0x40,   23),
"Ornate Bag":	Treasure(0x801ce3e8,	0x80,   24),
"Bugle":	Treasure(0x801ce3f8,	1,	25),
"Tambourine":	Treasure(0x801ce3f8,	2,	26),
"Triangle":	Treasure(0x801ce3f8,	4,	27),
"Clarinet":	Treasure(0x801ce3f8,	8,	28),
"Trombone":	Treasure(0x801ce3f8,	0x10,	29),
"Saxophone":	Treasure(0x801ce3f8,	0x20,	30),
"Drum":	Treasure(0x801ce3f8,	0x40,	31),
"Nintendo64":	Treasure(0x801ce3f8,	0x80,	32),
"Nice Glass":	Treasure(0x801ce418,	1,	33),
"Ancient Chalice":	Treasure(0x801ce418,	2,	34),
"Nice Cup":	Treasure(0x801ce418,	4,	35),
"Ornate Decanter":	Treasure(0x801ce418,	8,	36),
"Glass Decanter":	Treasure(0x801ce418,	0x10,	37),
"Nice Saucer":	Treasure(0x801ce418,	0x20,	38),
"Glass Bowl":	Treasure(0x801ce418,	0x40,	39),
"Jade Box":	Treasure(0x801ce418,	0x80,	40),
"Nice Goblet":	Treasure(0x801ce428,	1,	41),
"Violin":	Treasure(0x801ce428,	2,	42),
"Earring":	Treasure(0x801ce428,	4,	43),
"Jewelled Sword":	Treasure(0x801ce428,	8,	44),
"Gold Tiara":	Treasure(0x801ce428,	0x10,	45),
"Nice Sceptre":	Treasure(0x801ce428,	0x20,	46),
"King's Crown":	Treasure(0x801ce428,	0x40,	47),
"GameBoy Advance":	Treasure(0x801ce428,	0x80,	48),
"Big Mirror":	Treasure(0x801ce448,	1,	49),
"Antique Clock":	Treasure(0x801ce448,	2,	50),
"Gold Mirror":	Treasure(0x801ce448,	4,	51),
"Stained Glass":	Treasure(0x801ce448,	8,	52),
"Bronze Mirror":	Treasure(0x801ce448,	0x10,	53),
"Gold Clock":	Treasure(0x801ce448,	0x20,	54),
"Gold Pocketwatch":	Treasure(0x801ce448,	0x40,	55),
"Crazy Glasses":	Treasure(0x801ce448,	0x80,	56),
"Ancient Ring":	Treasure(0x801ce458,	1,	57),
"Ancient Necklace":	Treasure(0x801ce458,	2,	58),
"Ancient Relief":	Treasure(0x801ce458,	4,	59),
"Small Pyramid":	Treasure(0x801ce458,	8,	60),
"Ancient Bracelet":	Treasure(0x801ce458,	0x10,	61),
"Anubis Statue":	Treasure(0x801ce458,	0x20,	62),
"Monarch Mask":	Treasure(0x801ce458,	0x40,	63),
"Nintendo GameCube":	Treasure(0x801ce458,	0x80,	64),}

@dataclass
class CHECK():
    memvalue: int
    memloc: int
    CheckID: int
    region: str

@dataclass
class Chest(CHECK):
    pass
Chests_b: dict[str, Chest] = {
    "Greenhorn Forest Red Chest":	Chest(1,    0x801ce408, 1, "Greenhorn Forest"),
    "Greenhorn Forest Yellow Chest":    Chest(2,	0x801ce408, 2,  "Greenhorn Forest"),
    "Greenhorn Forest Chartreuse Chest":    Chest(4,	0x801ce408, 3,  "Greenhorn Forest"),
    "Greenhorn Forest Green Chest": Chest(8,	0x801ce408, 4,  "Greenhorn Forest"),
    "Greenhorn Forest Cyan Chest":  Chest(0x10,	0x801ce408, 5,  "Greenhorn Forest"),
    "Greenhorn Forest Blue Chest":  Chest(0x20,	0x801ce408, 6,  "Greenhorn Forest"),
    "Greenhorn Forest Purple Chest": Chest(0x40,	0x801ce408, 7,  "Greenhorn Forest"),
    "Greenhorn Forest Pink Chest":  Chest(0x80,	0x801ce408, 8,  "Greenhorn Forest"),
    "Greenhorn Ruins Red Chest":    Chest(1,	0x801ce409, 9,  "Greenhorn Ruins"),
    "Greenhorn Ruins Yellow Chest": Chest(2,    0x801ce409, 10, "Greenhorn Ruins"),
    "Greenhorn Ruins Chartreuse Chest": Chest(4,    0x801ce409, 11, "Greenhorn Ruins"),
    "Greenhorn Ruins Green Chest":  Chest(8,	0x801ce409, 12, "Greenhorn Ruins"),
    "Greenhorn Ruins Cyan Chest":   Chest(0x10, 0x801ce409, 13, "Greenhorn Ruins"),
    "Greenhorn Ruins Blue Chest":   Chest(0x20,	0x801ce409, 14, "Greenhorn Ruins"),
    "Greenhorn Ruins Purple Chest": Chest(0x40,	0x801ce409, 15, "Greenhorn Ruins"),
    "Greenhorn Ruins Pink Chest":   Chest(0x80,	0x801ce409, 16, "Greenhorn Ruins"),
    "Horror Manor Red Chest":   Chest(1,	0x801ce40a, 17, "Horror Manor"),
    "Horror Manor Yellow Chest":    Chest(2,    0x801ce40a, 18, "Horror Manor"),
    "Horror Manor Chartreuse Chest":    Chest(4,    0x801ce40a, 19, "Horror Manor"),
    "Horror Manor Green Chest": Chest(8,    0x801ce40a, 20, "Horror Manor"),
    "Horror Manor Cyan Chest": Chest(0x10,0x801ce40a, 21,   "Horror Manor"),
    "Horror Manor Blue Chest":	Chest(0x20,	0x801ce40a, 22,"Horror Manor"),
    "Horror Manor Purple Chest":    Chest(0x40,	0x801ce40a, 23, "Horror Manor"),
    "Horror Manor Pink Chest":  Chest(0x80,	0x801ce40a, 24, "Horror Manor"),
    "Wonky Circus Red Chest":   Chest(1,	0x801ce40b, 25, "Wonky Circus"),
    "Wonky Circus Yellow Chest":    Chest(2,	0x801ce40b, 26, "Wonky Circus"),
    "Wonky Circus Chartreuse Chest":    Chest(4,	0x801ce40b, 27, "Wonky Circus"),
    "Wonky Circus Green Chest":	Chest(8,    0x801ce40b, 28, "Wonky Circus"),
    "Wonky Circus Cyan Chest":  Chest(0x10,	0x801ce40b, 29, "Wonky Circus"),
    "Wonky Circus Blue Chest":  Chest(0x20,	0x801ce40b, 30, "Wonky Circus"),
    "Wonky Circus Purple Chest":    Chest(0x40,	0x801ce40b, 31, "Wonky Circus"),
    "Wonky Circus Pink Chest":	Chest(0x80,	0x801ce40b, 32, "Wonky Circus"),
    "Shivering Mountains Red Chest":	Chest(1,	0x801ce40c, 33, "Shivering Mountains"),
    "Shivering Mountains Yellow Chest": Chest(2,	0x801ce40c, 34, "Shivering Mountains"),
    "Shivering Mountains Chartreuse Chest": Chest(4,	0x801ce40c, 35, "Shivering Mountains"),
    "Shivering Mountains Green Chest":  Chest(8,    0x801ce40c, 36, "Shivering Mountains"),
    "Shivering Mountains Cyan Chest":	Chest(0x10,	0x801ce40c, 37, "Shivering Mountains"),
    "Shivering Mountains Blue Chest":   Chest(0x20,	0x801ce40c, 38, "Shivering Mountains"),
    "Shivering Mountains Purple Chest": Chest(0x40,	0x801ce40c, 39, "Shivering Mountains"),
    "Shivering Mountains Pink Chest":	Chest(0x80,	0x801ce40c, 40, "Shivering Mountains"),
    "Beanstalk Way Red Chest":	Chest(1,	0x801ce40d, 41, "Beanstalk Way"),
    "Beanstalk Way Yellow Chest":   Chest(2,	0x801ce40d, 42, "Beanstalk Way"),
    "Beanstalk Way Chartreuse Chest":	Chest(4,	0x801ce40d, 43, "Beanstalk Way"),
    "Beanstalk Way Green Chest":    Chest(8,	0x801ce40d, 44, "Beanstalk Way"),
    "Beanstalk Way Cyan Chest": Chest(0x10,	0x801ce40d, 45, "Beanstalk Way"),
    "Beanstalk Way Blue Chest":	Chest(0x20,	0x801ce40d, 46, "Beanstalk Way"),
    "Beanstalk Way Purple Chest":   Chest(0x40,	0x801ce40d, 47, "Beanstalk Way"),
    "Beanstalk Way Pink Chest": Chest(0x80,	0x801ce40d, 48, "Beanstalk Way"),
    "Mirror Mansion Red Chest": Chest(1,	0x801ce40e, 49, "Mirror Mansion"),
    "Mirror Mansion Yellow Chest": Chest(2,    0x801ce40e, 50,  "Mirror Mansion"),
    "Mirror Mansion Chartreuse Chest":  Chest(4,	0x801ce40e, 51, "Mirror Mansion"),
    "Mirror Mansion Green Chest":   Chest(8,	0x801ce40e, 52, "Mirror Mansion"),
    "Mirror Mansion Cyan Chest":    Chest(0x10,	0x801ce40e, 53, "Mirror Mansion"),
    "Mirror Mansion Blue Chest":    Chest(0x20,	0x801ce40e, 54, "Mirror Mansion"),
    "Mirror Mansion Purple Chest":  Chest(0x40,	0x801ce40e, 55,  "Mirror Mansion"),
    "Mirror Mansion Pink Chest":    Chest(0x80,	0x801ce40e, 56, "Mirror Mansion"),
    "Pecan Sands Red Chest":    Chest(1,	0x801ce40f, 57, "Pecan Sands"),
    "Pecan Sands Yellow Chest": Chest(2,    0x801ce40f, 58, "Pecan Sands"),
    "Pecan Sands Chartreuse Chest": Chest(4,	0x801ce40f, 59, "Pecan Sands"),
    "Pecan Sands Green Chest":	Chest(8,    0x801ce40f, 60, "Pecan Sands"),
    "Pecan Sands Cyan Chest":   Chest(0x10,	0x801ce40f, 61, "Pecan Sands"),
    "Pecan Sands Blue Chest":   Chest(0x20,	0x801ce40f, 62, "Pecan Sands"),
    "Pecan Sands Purple Chest": Chest(0x40,	0x801ce40f, 63, "Pecan Sands"),
    "Pecan Sands Pink Chest":   Chest(0x80,	0x801ce40f, 64, "Pecan Sands"),}

@dataclass
class Spriteling():
    memloc: int
    memvalue: int
    ItemID: int
    classification =  PROG
    ItemType = "Spriteling"

Spritelings_h: dict[str, Spriteling] = {
"Greenhorn Forest Red Spriteling":	Spriteling(0x801ce3b4,	1,	65),
"Greenhorn Forest Yellow Spriteling":	Spriteling(0x801ce3b4,	2,	66),
"Greenhorn Forest Green Spriteling":	Spriteling(0x801ce3b4,	4,	67),
"Greenhorn Forest Blue Spriteling":	Spriteling(0x801ce3b4,	8,	68),
"Greenhorn Forest Purple Spriteling":	Spriteling(0x801ce3b4,	0x10,	69),
"Greenhorn Ruins Red Spriteling":	Spriteling(0x801ce3c4,	1,	70),
"Greenhorn Ruins Yellow Spriteling":	Spriteling(0x801ce3c4,	2,	71),
"Greenhorn Ruins Green Spriteling":	Spriteling(0x801ce3c4,	4,	72),
"Greenhorn Ruins Blue Spriteling":	Spriteling(0x801ce3c4,	8,	73),
"Greenhorn Ruins Purple Spriteling":	Spriteling(0x801ce3c4,	0x10,	74),
"Horror Manor Red Spriteling":	Spriteling(0x801ce3e4,	1,	75),
"Horror Manor Yellow Spriteling":	Spriteling(0x801ce3e4,	2,	76),
"Horror Manor Green Spriteling":	Spriteling(0x801ce3e4,	4,	77),
"Horror Manor Blue Spriteling":	Spriteling(0x801ce3e4,	8,	78),
"Horror Manor Purple Spriteling":	Spriteling(0x801ce3e4,	0x10,	79),
"Wonky Circus Red Spriteling":	Spriteling(0x801ce3f4,	1,	80),
"Wonky Circus Yellow Spriteling":	Spriteling(0x801ce3f4,	2,	81),
"Wonky Circus Green Spriteling":	Spriteling(0x801ce3f4,	4,	82),
"Wonky Circus Blue Spriteling":	Spriteling(0x801ce3f4,	8,	83),
"Wonky Circus Purple Spriteling":	Spriteling(0x801ce3f4,	0x10,	84),
"Shivering Mountains Red Spriteling":	Spriteling(0x801ce414,	1,	85),
"Shivering Mountains Yellow Spriteling":	Spriteling(0x801ce414,	2,	86),
"Shivering Mountains Green Spriteling":	Spriteling(0x801ce414,	4,	87),
"Shivering Mountains Blue Spriteling":	Spriteling(0x801ce414,	8,	88),
"Shivering Mountains Purple Spriteling":	Spriteling(0x801ce414,	0x10,	89),
"Beanstalk Way Red Spriteling":	Spriteling(0x801ce424,	1,	90),
"Beanstalk Way Yellow Spriteling":	Spriteling(0x801ce424,	2,	91),
"Beanstalk Way Green Spriteling":	Spriteling(0x801ce424,	4,	92),
"Beanstalk Way Blue Spriteling":	Spriteling(0x801ce424,	8,	93),
"Beanstalk Way Purple Spriteling":	Spriteling(0x801ce424,	0x10,	94),
"Mirror Mansion Red Spriteling":	Spriteling(0x801ce444,	1,	95),
"Mirror Mansion Yellow Spriteling":	Spriteling(0x801ce444,	2,	96),
"Mirror Mansion Green Spriteling":	Spriteling(0x801ce444,	4,	97),
"Mirror Mansion Blue Spriteling":	Spriteling(0x801ce444,	8,	98),
"Mirror Mansion Purple Spriteling":	Spriteling(0x801ce444,	0x10,	99),
"Pecan Sands Red Spriteling":	Spriteling(0x801ce454,	1,	100),
"Pecan Sands Yellow Spriteling":	Spriteling(0x801ce454,	2,	101),
"Pecan Sands Green Spriteling":	Spriteling(0x801ce454,	4,	102),
"Pecan Sands Blue Spriteling":	Spriteling(0x801ce454,	8,	103),
"Pecan Sands Purple Spriteling":	Spriteling(0x801ce454,	0x10,	104),}

@dataclass
class Cage(CHECK):
    pass
Cages_b: dict[str, Cage] = {
    "Greenhorn Forest Red Spriteling Cage": Cage(1,	0x801ce3d8, 65, "Greenhorn Forest"),
    "Greenhorn Forest Yellow Spriteling Cage":  Cage(2,	0x801ce3d8, 66, "Greenhorn Forest"),
    "Greenhorn Forest Green Spriteling Cage":	Cage(4,	0x801ce3d8, 67, "Greenhorn Forest"),
    "Greenhorn Forest Blue Spriteling Cage":	Cage(8,	0x801ce3d8, 68, "Greenhorn Forest"),
    "Greenhorn Forest Purple Spriteling Cage":	Cage(0x10,	0x801ce3d8, 69, "Greenhorn Forest"),
    "Greenhorn Ruins Red Spriteling Cage":	Cage(1,	0x801ce3d9, 70, "Greenhorn Ruins"),
    "Greenhorn Ruins Yellow Spriteling Cage":	Cage(2,	0x801ce3d9, 71, "Greenhorn Ruins"),
    "Greenhorn Ruins Green Spriteling Cage":	Cage(4,	0x801ce3d9, 72, "Greenhorn Ruins"),
    "Greenhorn Ruins Blue Spriteling Cage":	Cage(8,	0x801ce3d9, 73, "Greenhorn Ruins"),
    "Greenhorn Ruins Purple Spriteling Cage":	Cage(0x10,	0x801ce3d9, 74, "Greenhorn Ruins"),
    "Horror Manor Red Spriteling Cage":	Cage(1,	0x801ce3da, 75, "Horror Manor"),
    "Horror Manor Yellow Spriteling Cage":	Cage(2,	0x801ce3da, 76, "Horror Manor"),
    "Horror Manor Green Spriteling Cage":	Cage(4,	0x801ce3da, 77, "Horror Manor"),
    "Horror Manor Blue Spriteling Cage":	Cage(8,	0x801ce3da, 78, "Horror Manor"),
    "Horror Manor Purple Spriteling Cage":	Cage(0x10,	0x801ce3da, 79, "Horror Manor"),
    "Wonky Circus Red Spriteling Cage":	Cage(1,	0x801ce3db, 80, "Wonky Circus"),
    "Wonky Circus Yellow Spriteling Cage":	Cage(2,	0x801ce3db, 81, "Wonky Circus"),
    "Wonky Circus Green Spriteling Cage":	Cage(4,	0x801ce3db, 82, "Wonky Circus"),
    "Wonky Circus Blue Spriteling Cage":	Cage(8,	0x801ce3db, 83, "Wonky Circus"),
    "Wonky Circus Purple Spriteling Cage":	Cage(0x10,	0x801ce3db, 84, "Wonky Circus"),
    "Shivering Mountains Red Spriteling Cage":	Cage(1,	0x801ce3dc, 85, "Shivering Mountains"),
    "Shivering Mountains Yellow Spriteling Cage":	Cage(2,	0x801ce3dc, 86, "Shivering Mountains"),
    "Shivering Mountains Green Spriteling Cage":	Cage(4,	0x801ce3dc, 87, "Shivering Mountains"),
    "Shivering Mountains Blue Spriteling Cage":	Cage(8,	0x801ce3dc, 88, "Shivering Mountains"),
    "Shivering Mountains Purple Spriteling Cage":	Cage(0x10,	0x801ce3dc, 89, "Shivering Mountains"),
    "Beanstalk Way Red Spriteling Cage":	Cage(1,	0x801ce3dd, 90, "Beanstalk Way"),
    "Beanstalk Way Yellow Spriteling Cage":	Cage(2,	0x801ce3dd, 91, "Beanstalk Way"),
    "Beanstalk Way Green Spriteling Cage":	Cage(4,	0x801ce3dd, 92, "Beanstalk Way"),
    "Beanstalk Way Blue Spriteling Cage":	Cage(8,	0x801ce3dd, 93, "Beanstalk Way"),
    "Beanstalk Way Purple Spriteling Cage":	Cage(0x10,	0x801ce3dd, 94, "Beanstalk Way"),
    "Mirror Mansion Red Spriteling Cage":	Cage(1,	0x801ce3de, 95, "Mirror Mansion"),
    "Mirror Mansion Yellow Spriteling Cage":	Cage(2,	0x801ce3de, 96, "Mirror Mansion"),
    "Mirror Mansion Green Spriteling Cage":	Cage(4,	0x801ce3de, 97, "Mirror Mansion"),
    "Mirror Mansion Blue Spriteling Cage":	Cage(8,	0x801ce3de, 98, "Mirror Mansion"),
    "Mirror Mansion Purple Spriteling Cage":	Cage(0x10,	0x801ce3de, 99, "Mirror Mansion"),
    "Pecan Sands Red Spriteling Cage":	Cage(1,	0x801ce3df, 100,    "Pecan Sands"),
    "Pecan Sands Yellow Spriteling Cage":	Cage(2,	0x801ce3df, 101,    "Pecan Sands"),
    "Pecan Sands Green Spriteling Cage":	Cage(4,	0x801ce3df, 102,    "Pecan Sands"),
    "Pecan Sands Blue Spriteling Cage":	Cage(8,	0x801ce3df, 103,    "Pecan Sands"),
    "Pecan Sands Purple Spriteling Cage":	Cage(0x10,	0x801ce3df, 104,    "Pecan Sands"),}

class BossMedal(NamedTuple):
    memvalue: int
    ItemID: int
    classification = PROG
    ItemType = "BossMedal"
    memloc = 0x801ce3ac

BossMedals_h: dict[str, BossMedal] = {
	"Greenfist Boss Medal":    BossMedal(1, 105),
	"Sandworm Boss Medal":	BossMedal(2,  106),
    "DinoMighty Big Key Fragment":	BossMedal(4,  107),
    "Brawl Doll Boss Medal":	BossMedal(8,   108),
    "Clown-a-Round Boss Medal":	BossMedal(0x10, 109),
    "Dual Dragon Big Key Fragment":	BossMedal(0x20, 110),
    "Winter Windster Boss Medal":	BossMedal(0x40,   111),
    "Spideraticus Boss Medal":	BossMedal(0x80,  112),
    "Red-Brief J Big Key Fragment":	BossMedal(0x100, 113),
    "The Mean Emcee Boss Medal":	BossMedal(0x200,	114),
    "Ironsider Boss Medal":	BossMedal(0x400,	115),
    "Captain Skull Big Key Fragment":	BossMedal(0x800,   116),
    }

class StageDoor(NamedTuple):
    memvalue: int
    ItemID: int
    classification = PROG
    ItemType = "StageDoor"
    memloc = 0x801ce3d0

Doors_b: dict [str, StageDoor] = {
    "Greenhorn Ruins Door":	StageDoor(1,	 117),
    "DinoMighty's Showdown Door":	StageDoor(2,	118),
    "Horror Manor Door":	StageDoor(4,	119),
    "Wonky Circus Door":	StageDoor(8,	120),
    "Dual Dragon's Showdown Door":	StageDoor(0x10,  121),
    "Shivering Mountains Door":	StageDoor(0x20, 122),
    "Beanstalk Way Door":	StageDoor(0x40,   123),
    "Red-Brief J's Showdown Door":	StageDoor(0x80,  124),
    "Mirror Mansion Door":	StageDoor(0x100,  125),
    "Pecan Sands Door":	StageDoor(0x200,	126),
    "Captain Skull's Showdown Door":	StageDoor(0x400,    127),}

@dataclass
class BossBeat(CHECK):
    pass

Bosses_b: dict[str, BossBeat] = {
    "Defeated Greenfist":   BossBeat(1, 0x801ce3d2,	105, "Greenfist"),
    "Defeated Sandworm":    BossBeat(2, 0x801ce3d2,	106,    "Sandworm"),
    "Defeated DinoMighty":  BossBeat(4, 0x801ce3d2, 107,    "DinoMighty's Showdown"),
    "Defeated Brawl Doll":  BossBeat(8, 0x801ce3d2, 108,    "Brawl Doll"),
    "Defeated Clown-a-Round":   BossBeat(0x10,  0x801ce3d2,  109,    "Clown-a-Round"),
    "Defeated Dual Dragon": BossBeat(0x20,  0x801ce3d2,  110,    "Dual Dragon's Showdown"),
    "Defeated Winter Windster": BossBeat(0x40,  0x801ce3d2,  111,    "Winter Windster"),
    "Defeated Spideraticus":    BossBeat(0x80,  0x801ce3d2,  112,    "Spideraticus"),
    "Defeated Red-Brief J": BossBeat(0x10,  0x801ce3d2,  113,    "Red-Brief J's Showdown"),
    "Defeated The Mean Emcee":  BossBeat(0x200, 0x801ce3d2, 114,    "The Mean Emcee"),
    "Defeated Ironsider":   BossBeat(0x400, 0x801ce3d2,	115,    "Ironsider"),
    "Defeated Captain Skull":   BossBeat(0x800, 0x801ce3d2, 116,    "Captain Skull's Showdown"),
    "Opened Greenhorn Ruins Door": BossBeat(1, 0x801ce3d2, 117, "Greenfist"),
    "Opened DinoMighty's Door": BossBeat(2, 0x801ce3d2, 118, "Sandworm"),
    "Opened Horror Manor Door": BossBeat(4, 0x801ce3d2, 119, "DinoMighty's Showdown"),
    "Opened Wonky Circus Door": BossBeat(8, 0x801ce3d2, 120, "Brawl Doll"),
    "Opened Dual Dragon Door": BossBeat(0x10, 0x801ce3d2, 121, "Clown-a-Round"),
    "Opened Shivering Mountains Door": BossBeat(0x20, 0x801ce3d2, 122, "Dual Dragon's Showdown"),
    "Opened Beanstalk Way Door": BossBeat(0x40, 0x801ce3d2, 123, "Winter Windster"),
    "Opened Red-Brief J Door": BossBeat(0x80, 0x801ce3d2, 124, "Spideraticus"),
    "Opened Mirror Mansion Door": BossBeat(0x10, 0x801ce3d2, 125, "Red-Brief J's Showdown"),
    "Opened Pecan Sands Door": BossBeat(0x200, 0x801ce3d2, 126, "The Mean Emcee"),
    "Opened Captain Skull Door": BossBeat(0x400, 0x801ce3d2, 127, "Ironsider"),
    "Victory": BossBeat(0x1000, 0x801ce3d2,    None,   "Menu"),}

class RedDiamond(NamedTuple):
    """loc is vanilla location
    value is ingame value
    ItemID is archipelago itemcode
    """
    memloc: int
    memvalue: int
    ItemID: int
    classification = PROG
    ItemType = "Red Diamond"

Diamonds_h: dict [str, RedDiamond] = {
"Greenhorn Forest Red Diamond 1":	RedDiamond(0x801ce3ba,	1,	128),
"Greenhorn Forest Red Diamond 2":	RedDiamond(0x801ce3ba,	2,	129),
"Greenhorn Forest Red Diamond 3":	RedDiamond(0x801ce3ba,	4,	130),
"Greenhorn Forest Red Diamond 4":	RedDiamond(0x801ce3ba,	8,	131),
"Greenhorn Forest Red Diamond 5":	RedDiamond(0x801ce3ba,	0x10,	132),
"Greenhorn Forest Red Diamond 6":	RedDiamond(0x801ce3ba,	0x20,	133),
"Greenhorn Forest Red Diamond 7":	RedDiamond(0x801ce3ba,	0x40,	134),
"Greenhorn Forest Red Diamond 8":	RedDiamond(0x801ce3ba,	0x80,	135),
"Greenhorn Ruins Red Diamond 1":	RedDiamond(0x801ce3ca,	1,	136),
"Greenhorn Ruins Red Diamond 2":	RedDiamond(0x801ce3ca,	2,	137),
"Greenhorn Ruins Red Diamond 3":	RedDiamond(0x801ce3ca,	4,	138),
"Greenhorn Ruins Red Diamond 4":	RedDiamond(0x801ce3ca,	8,	139),
"Greenhorn Ruins Red Diamond 5":	RedDiamond(0x801ce3ca,	0x10,	140),
"Greenhorn Ruins Red Diamond 6":	RedDiamond(0x801ce3ca,	0x20,	141),
"Greenhorn Ruins Red Diamond 7":	RedDiamond(0x801ce3ca,	0x40,	142),
"Greenhorn Ruins Red Diamond 8":	RedDiamond(0x801ce3ca,	0x80,	143),
"Horror Manor Red Diamond 1":	RedDiamond(0x801ce3ea,	1,	144),
"Horror Manor Red Diamond 2":	RedDiamond(0x801ce3ea,	2,	145),
"Horror Manor Red Diamond 3":	RedDiamond(0x801ce3ea,	4,	146),
"Horror Manor Red Diamond 4":	RedDiamond(0x801ce3ea,	8,	147),
"Horror Manor Red Diamond 5":	RedDiamond(0x801ce3ea,	0x10,	148),
"Horror Manor Red Diamond 6":	RedDiamond(0x801ce3ea,	0x20,	149),
"Horror Manor Red Diamond 7":	RedDiamond(0x801ce3ea,	0x40,	150),
"Horror Manor Red Diamond 8":	RedDiamond(0x801ce3ea,	0x80,	151),
"Wonky Circus Red Diamond 1":	RedDiamond(0x801ce3fa,	1,	152),
"Wonky Circus Red Diamond 2":	RedDiamond(0x801ce3fa,	2,	153),
"Wonky Circus Red Diamond 3":	RedDiamond(0x801ce3fa,	4,	154),
"Wonky Circus Red Diamond 4":	RedDiamond(0x801ce3fa,	8,	155),
"Wonky Circus Red Diamond 5":	RedDiamond(0x801ce3fa,	0x10,	156),
"Wonky Circus Red Diamond 6":	RedDiamond(0x801ce3fa,	0x20,	157),
"Wonky Circus Red Diamond 7":	RedDiamond(0x801ce3fa,	0x40,	158),
"Wonky Circus Red Diamond 8":	RedDiamond(0x801ce3fa,	0x80,	159),
"Shivering Mountains Red Diamond 1":	RedDiamond(0x801ce41a,	1,	160),
"Shivering Mountains Red Diamond 2":	RedDiamond(0x801ce41a,	2,	161),
"Shivering Mountains Red Diamond 3":	RedDiamond(0x801ce41a,	4,	162),
"Shivering Mountains Red Diamond 4":	RedDiamond(0x801ce41a,	8,	163),
"Shivering Mountains Red Diamond 5":	RedDiamond(0x801ce41a,	0x10,	164),
"Shivering Mountains Red Diamond 6":	RedDiamond(0x801ce41a,	0x20,	165),
"Shivering Mountains Red Diamond 7":	RedDiamond(0x801ce41a,	0x40,	166),
"Shivering Mountains Red Diamond 8":	RedDiamond(0x801ce41a,	0x80,	167),
"Beanstalk Way Red Diamond 1":	RedDiamond(0x801ce42a,	1,	168),
"Beanstalk Way Red Diamond 2":	RedDiamond(0x801ce42a,	2,	169),
"Beanstalk Way Red Diamond 3":	RedDiamond(0x801ce42a,	4,	170),
"Beanstalk Way Red Diamond 4":	RedDiamond(0x801ce42a,	8,	171),
"Beanstalk Way Red Diamond 5":	RedDiamond(0x801ce42a,	0x10,	172),
"Beanstalk Way Red Diamond 6":	RedDiamond(0x801ce42a,	0x20,	173),
"Beanstalk Way Red Diamond 7":	RedDiamond(0x801ce42a,	0x40,	174),
"Beanstalk Way Red Diamond 8":	RedDiamond(0x801ce42a,	0x80,	175),
"Mirror Mansion Red Diamond 1":	RedDiamond(0x801ce44a,	1,	176),
"Mirror Mansion Red Diamond 2":	RedDiamond(0x801ce44a,	2,	177),
"Mirror Mansion Red Diamond 3":	RedDiamond(0x801ce44a,	4,	178),
"Mirror Mansion Red Diamond 4":	RedDiamond(0x801ce44a,	8,	179),
"Mirror Mansion Red Diamond 5":	RedDiamond(0x801ce44a,	0x10,	180),
"Mirror Mansion Red Diamond 6":	RedDiamond(0x801ce44a,	0x20,	181),
"Mirror Mansion Red Diamond 7":	RedDiamond(0x801ce44a,	0x40,	182),
"Mirror Mansion Red Diamond 8":	RedDiamond(0x801ce44a,	0x80,	183),
"Pecan Sands Red Diamond 1":	RedDiamond(0x801ce45a,	1,	184),
"Pecan Sands Red Diamond 2":	RedDiamond(0x801ce45a,	2,	185),
"Pecan Sands Red Diamond 3":	RedDiamond(0x801ce45a,	4,	186),
"Pecan Sands Red Diamond 4":	RedDiamond(0x801ce45a,	8,	187),
"Pecan Sands Red Diamond 5":	RedDiamond(0x801ce45a,	0x10,	188),
"Pecan Sands Red Diamond 6":	RedDiamond(0x801ce45a,	0x20,	189),
"Pecan Sands Red Diamond 7":	RedDiamond(0x801ce45a,	0x40,	190),
"Pecan Sands Red Diamond 8":	RedDiamond(0x801ce45a,	0x80,	191)}


@dataclass
class DiamondPickup(CHECK):
    pass

DiamondPickups_b: dict[str, DiamondPickup] = {
"Greenhorn Forest Trapdoor Red Diamond 1":	DiamondPickup(1,	0x801ce400,	128,	"Greenhorn Forest"),
"Greenhorn Forest Trapdoor Red Diamond 2":	DiamondPickup(2,	0x801ce400,	129,	"Greenhorn Forest"),
"Greenhorn Forest Trapdoor Red Diamond 3":	DiamondPickup(4,	0x801ce400,	130,	"Greenhorn Forest"),
"Greenhorn Forest Trapdoor Red Diamond 4":	DiamondPickup(8,	0x801ce400,	131,	"Greenhorn Forest"),
"Greenhorn Forest Trapdoor Red Diamond 5":	DiamondPickup(0x10,	0x801ce400,	132,	"Greenhorn Forest"),
"Greenhorn Forest Trapdoor Red Diamond 6":	DiamondPickup(0x20,	0x801ce400,	133,	"Greenhorn Forest"),
"Greenhorn Forest Trapdoor Red Diamond 7":	DiamondPickup(0x40,	0x801ce400,	134,	"Greenhorn Forest"),
"Greenhorn Forest Trapdoor Red Diamond 8":	DiamondPickup(0x80,	0x801ce400,	135,	"Greenhorn Forest"),
"Greenhorn Ruins Trapdoor Red Diamond 1":	DiamondPickup(1,	0x801ce401,	136,	"Greenhorn Ruins"),
"Greenhorn Ruins Trapdoor Red Diamond 2":	DiamondPickup(2,	0x801ce401,	137,	"Greenhorn Ruins"),
"Greenhorn Ruins Trapdoor Red Diamond 3":	DiamondPickup(4,	0x801ce401,	138,	"Greenhorn Ruins"),
"Greenhorn Ruins Trapdoor Red Diamond 4":	DiamondPickup(8,	0x801ce401,	139,	"Greenhorn Ruins"),
"Greenhorn Ruins Trapdoor Red Diamond 5":	DiamondPickup(0x10,	0x801ce401,	140,	"Greenhorn Ruins"),
"Greenhorn Ruins Trapdoor Red Diamond 6":	DiamondPickup(0x20,	0x801ce401,	141,	"Greenhorn Ruins"),
"Greenhorn Ruins Trapdoor Red Diamond 7":	DiamondPickup(0x40,	0x801ce401,	142,	"Greenhorn Ruins"),
"Greenhorn Ruins Trapdoor Red Diamond 8":	DiamondPickup(0x80,	0x801ce401,	143,	"Greenhorn Ruins"),
"Horror Manor Trapdoor Red Diamond 1":	DiamondPickup(1,	0x801ce402,	144,	"Horror Manor"),
"Horror Manor Trapdoor Red Diamond 2":	DiamondPickup(2,	0x801ce402,	145,	"Horror Manor"),
"Horror Manor Trapdoor Red Diamond 3":	DiamondPickup(4,	0x801ce402,	146,	"Horror Manor"),
"Horror Manor Trapdoor Red Diamond 4":	DiamondPickup(8,	0x801ce402,	147,	"Horror Manor"),
"Horror Manor Trapdoor Red Diamond 5":	DiamondPickup(0x10,	0x801ce402,	148,	"Horror Manor"),
"Horror Manor Trapdoor Red Diamond 6":	DiamondPickup(0x20,	0x801ce402,	149,	"Horror Manor"),
"Horror Manor Trapdoor Red Diamond 7":	DiamondPickup(0x40,	0x801ce402,	150,	"Horror Manor"),
"Horror Manor Trapdoor Red Diamond 8":	DiamondPickup(0x80,	0x801ce402,	151,	"Horror Manor"),
"Wonky Circus Trapdoor Red Diamond 1":	DiamondPickup(1,	0x801ce403,	152,	"Wonky Circus"),
"Wonky Circus Trapdoor Red Diamond 2":	DiamondPickup(2,	0x801ce403,	153,	"Wonky Circus"),
"Wonky Circus Trapdoor Red Diamond 3":	DiamondPickup(4,	0x801ce403,	154,	"Wonky Circus"),
"Wonky Circus Trapdoor Red Diamond 4":	DiamondPickup(8,	0x801ce403,	155,	"Wonky Circus"),
"Wonky Circus Trapdoor Red Diamond 5":	DiamondPickup(0x10,	0x801ce403,	156,	"Wonky Circus"),
"Wonky Circus Trapdoor Red Diamond 6":	DiamondPickup(0x20,	0x801ce403,	157,	"Wonky Circus"),
"Wonky Circus Trapdoor Red Diamond 7":	DiamondPickup(0x40,	0x801ce403,	158,	"Wonky Circus"),
"Wonky Circus Trapdoor Red Diamond 8":	DiamondPickup(0x80,	0x801ce403,	159,	"Wonky Circus"),
"Shivering Mountains Trapdoor Red Diamond 1":	DiamondPickup(1,	0x801ce404,	160,	"Shivering Mountains"),
"Shivering Mountains Trapdoor Red Diamond 2":	DiamondPickup(2,	0x801ce404,	161,	"Shivering Mountains"),
"Shivering Mountains Trapdoor Red Diamond 3":	DiamondPickup(4,	0x801ce404,	162,	"Shivering Mountains"),
"Shivering Mountains Trapdoor Red Diamond 4":	DiamondPickup(8,	0x801ce404,	163,	"Shivering Mountains"),
"Shivering Mountains Trapdoor Red Diamond 5":	DiamondPickup(0x10,	0x801ce404,	164,	"Shivering Mountains"),
"Shivering Mountains Trapdoor Red Diamond 6":	DiamondPickup(0x20,	0x801ce404,	165,	"Shivering Mountains"),
"Shivering Mountains Trapdoor Red Diamond 7":	DiamondPickup(0x40,	0x801ce404,	166,	"Shivering Mountains"),
"Shivering Mountains Trapdoor Red Diamond 8":	DiamondPickup(0x80,	0x801ce404,	167,	"Shivering Mountains"),
"Beanstalk Way Trapdoor Red Diamond 1":	DiamondPickup(1,	0x801ce405,	168,	"Beanstalk Way"),
"Beanstalk Way Trapdoor Red Diamond 2":	DiamondPickup(2,	0x801ce405,	169,	"Beanstalk Way"),
"Beanstalk Way Trapdoor Red Diamond 3":	DiamondPickup(4,	0x801ce405,	170,	"Beanstalk Way"),
"Beanstalk Way Trapdoor Red Diamond 4":	DiamondPickup(8,	0x801ce405,	171,	"Beanstalk Way"),
"Beanstalk Way Trapdoor Red Diamond 5":	DiamondPickup(0x10,	0x801ce405,	172,	"Beanstalk Way"),
"Beanstalk Way Trapdoor Red Diamond 6":	DiamondPickup(0x20,	0x801ce405,	173,	"Beanstalk Way"),
"Beanstalk Way Trapdoor Red Diamond 7":	DiamondPickup(0x40,	0x801ce405,	174,	"Beanstalk Way"),
"Beanstalk Way Trapdoor Red Diamond 8":	DiamondPickup(0x80,	0x801ce405,	175,	"Beanstalk Way"),
"Mirror Mansion	Trapdoor Red Diamond 1":	DiamondPickup(1,	0x801ce406,	176,	"Mirror Mansion"),
"Mirror Mansion	Trapdoor Red Diamond 2":	DiamondPickup(2,	0x801ce406,	177,	"Mirror Mansion"),
"Mirror Mansion	Trapdoor Red Diamond 3":	DiamondPickup(4,	0x801ce406,	178,	"Mirror Mansion"),
"Mirror Mansion	Trapdoor Red Diamond 4":	DiamondPickup(8,	0x801ce406,	179,	"Mirror Mansion"),
"Mirror Mansion	Trapdoor Red Diamond 5":	DiamondPickup(0x10,	0x801ce406,	180,	"Mirror Mansion"),
"Mirror Mansion	Trapdoor Red Diamond 6":	DiamondPickup(0x20,	0x801ce406,	181,	"Mirror Mansion"),
"Mirror Mansion	Trapdoor Red Diamond 7":	DiamondPickup(0x40,	0x801ce406,	182,	"Mirror Mansion"),
"Mirror Mansion	Trapdoor Red Diamond 8":	DiamondPickup(0x80,	0x801ce406,	183,	"Mirror Mansion"),
"Pecan Sands Trapdoor Red Diamond 1":	DiamondPickup(1,	0x801ce407,	184,	"Pecan Sands"),
"Pecan Sands Trapdoor Red Diamond 2":	DiamondPickup(2,	0x801ce407,	185,	"Pecan Sands"),
"Pecan Sands Trapdoor Red Diamond 3":	DiamondPickup(4,	0x801ce407,	186,	"Pecan Sands"),
"Pecan Sands Trapdoor Red Diamond 4":	DiamondPickup(8,	0x801ce407,	187,	"Pecan Sands"),
"Pecan Sands Trapdoor Red Diamond 5":	DiamondPickup(0x10,	0x801ce407,	188,	"Pecan Sands"),
"Pecan Sands Trapdoor Red Diamond 6":	DiamondPickup(0x20,	0x801ce407,	189,	"Pecan Sands"),
"Pecan Sands Trapdoor Red Diamond 7":	DiamondPickup(0x40,	0x801ce407,	190,	"Pecan Sands"),
"Pecan Sands Trapdoor Red Diamond 8":	DiamondPickup(0x80,	0x801ce407,	191,	"Pecan Sands"),
}

class Junk(NamedTuple):
    memloc: int | None
    memvalue: int
    ItemID: int | None
    classification = FILL
    ItemType = "Junk"

JunkItems: dict[str, Junk] = {
    "50 coins": Junk(0x801ce3a4,    +50, None),
    "Garlic":   Junk(None,   +2,   None),
}

class Trap(NamedTuple):
    memloc: int | None
    memvalue: int
    ItemID: int | None
    classification = TRAP
    ItemType = "Trap"

TrapItems: dict[str, Trap] = {
    "Unithorn Attack":    Trap(0x801ce3a4,  -50, None),
    "Death Trap":   Trap(None,  0,  None),
    "Take Damage": Trap(None,  -2, None),
}

ITEM_TABLE = {
    **Spritelings_h,
    **Treasures_h,
    **BossMedals_h,
    **Doors_b,
    **Diamonds_h,
}

FILLER_TABLE = {
    **JunkItems,
    **TrapItems,
}

CHECK_TABLE = {
    **Chests_b,
    **Cages_b,
    **Bosses_b,
    **DiamondPickups_b,
}

BigKeys = [x for x in BossMedals_h.keys() if "Big Key Fragment" in x]
GFRedDiamonds = [x for x in Diamonds_h.keys() if "Greenhorn Forest Red Diamond" in x]
GRRedDiamonds = [x for x in Diamonds_h.keys() if "Greenhorn Ruins Red Diamond" in x]
HMRedDiamonds = [x for x in Diamonds_h.keys() if "Horror Manor Red Diamond" in x]
WCRedDiamonds = [x for x in Diamonds_h.keys() if "Wonky Circus Red Diamond" in x]
SMRedDiamonds = [x for x in Diamonds_h.keys() if "Shivering Mountains Red Diamond" in x]
BWRedDiamonds = [x for x in Diamonds_h.keys() if "Beanstalk Way Red Diamond" in x]
MMRedDiamonds = [x for x in Diamonds_h.keys() if "Mirror Mansion Red Diamond" in x]
PSRedDiamonds = [x for x in Diamonds_h.keys() if "Pecan Sands Red Diamond" in x]