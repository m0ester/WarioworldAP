from typing import NamedTuple
from BaseClasses import ItemClassification as IC

PROG = IC.progression
FILL = IC.filler
USEF = IC.useful
SKIP = IC.skip_balancing
TRAP = IC.trap

class Treasure(NamedTuple):
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

class Chest(NamedTuple):
    memvalue: int
    memloc: int
    CheckID: int
    region: str

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

class Spriteling(NamedTuple):
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

class Cage(NamedTuple):
    memvalue: int
    memloc: int
    CheckID: int
    region: str

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

class BossBeat(NamedTuple):
    memvalue: int
    CheckID: int
    region: str
    memloc = 0x801ce3d2

Bosses_b: dict[str, BossBeat] = {
    "Defeated Greenfist":   BossBeat(1,	105, "Greenhorn Forest"),
    "Defeated Sandworm":    BossBeat(2,	106,    "Greenhorn Ruins"),
    "Defeated DinoMighty":  BossBeat(4, 107,    "DinoMighty's Showdown"),
    "Defeated Brawl Doll":  BossBeat(8, 108,    "Horror Manor"),
    "Defeated Clown-a-Round":   BossBeat(0x10,  109,    "Wonky Circus"),
    "Defeated Dual Dragon": BossBeat(0x20,  110,    "Dual Dragon's Showdown"),
    "Defeated Winter Windster": BossBeat(0x40,  111,    "Shivering Mountains"),
    "Defeated Spideraticus":    BossBeat(0x80,  112,    "Beanstalk Way"),
    "Defeated Red-Brief J": BossBeat(0x10,  113,    "Red-Brief J's Showdown"),
    "Defeated The Mean Emcee":  BossBeat(0x200, 114,    "Mirror Mansion"),
    "Defeated Ironsider":   BossBeat(0x400,	115,    "Pecan Sands"),
    "Defeated Captain Skull":   BossBeat(0x800, 116,    "Captain Skull's Showdown"),
    "Defeated Black Jewel": BossBeat(0x1000,    None,   None),}

class Junk(NamedTuple):
    loc: int
    value: int
    name: str
    ItemID: int
    classification = FILL
    ItemType = "Junk"

#JunkItems: list = [
 #   Junk(0x801ce3a4,    +50, "50 coins", 128),
  #  Junk(DME.read_word(0x801c5820) + 0xd8, +2, "Garlic", 129),
#]

class Trap(NamedTuple):
    loc: int 
    value: int
    name: str
    ItemID: int
    classification = TRAP
    ItemType = "Trap"

#TrapItems: list = [
 #   Trap(0x801ce3a4,  -50, "Unithorn Attack", 130),
  #  Trap(DME.read_word(0x801c5820) + 0xd8,  0,  "Death Trap",   131),
   # Trap(DME.read_word(0x801c5820) + 0xd8,  -2, "Take Damage", 132),
#]

ITEM_TABLE = {
    **Spritelings_h,
    **Treasures_h,
    **BossMedals_h,
    **Doors_b,
}

CHECK_TABLE = {
    **Chests_b,
    **Cages_b,
    **Bosses_b,
}