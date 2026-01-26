from typing import NamedTuple
import dolphin_memory_engine as DME
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
    loc: int
    value: int
    name: str
    ItemID: int
    classification = FILL
    ItemType = 1

Treasures_h: dict = [
    Treasure(0x801ce3b8,	1,	"Ruby", 1),
    Treasure(0x801ce3b8,	2,	"Opal", 2),
    Treasure(0x801ce3b8,	4,	"Amethyst", 3),
    Treasure(0x801ce3b8,	8,	"Amber",    4),
    Treasure(0x801ce3b8,	0x10,	"Sapphire", 5),
    Treasure(0x801ce3b8,	0x20,	"Topaz",    6),
    Treasure(0x801ce3b8,	0x40,	"Emerald",  7),
    Treasure(0x801ce3b8,	0x80,	"Diamond",  8),
    Treasure(0x801ce3c8,	1,	"Porcelain Urn",    9),
    Treasure(0x801ce3c8,	2,	"Fine China",   10),
    Treasure(0x801ce3c8,	4,	"Ceramic Vase", 11),
    Treasure(0x801ce3c8,	8,	"Teapot",   12),
    Treasure(0x801ce3c8,	0x10,	"Vase", 13),
    Treasure(0x801ce3c8,	0x20,	"Precious Pot", 14),
    Treasure(0x801ce3c8,	0x40,	"Lucky Figurine",   15),
    Treasure(0x801ce3c8,	0x80,	"NES",  16),
    Treasure(0x801ce3e8,	1,	"Candlestick",  17),
    Treasure(0x801ce3e8,	2,	"Silver Candlestick",   18),
    Treasure(0x801ce3e8,	4,	"Forest Painting",  19),
    Treasure(0x801ce3e8,	8,	"Castle Painting",  20),
    Treasure(0x801ce3e8,	0x10,	"Crystal Ball", 21),
    Treasure(0x801ce3e8,	0x20,	"Knight's Helmet",  22),
    Treasure(0x801ce3e8,	0x40,	"Gladiator's Helmet",   23),
    Treasure(0x801ce3e8,	0x80,	"Ornate Bag",   24),
    Treasure(0x801ce3f8,	1,	"Bugle",    25),
    Treasure(0x801ce3f8,	2,	"Tambourine",   26),
    Treasure(0x801ce3f8,	4,	"Triangle", 27),
    Treasure(0x801ce3f8,	8,	"Clarinet", 28),
    Treasure(0x801ce3f8,	0x10,	"Trombone", 29),
    Treasure(0x801ce3f8,	0x20,	"Saxophone",    30),
    Treasure(0x801ce3f8,	0x40,	"Drum", 31),
    Treasure(0x801ce3f8,	0x80,	"Nintendo64",   32),
    Treasure(0x801ce418,	1,	"Nice Glass",   33),
    Treasure(0x801ce418,	2,	"Ancient Chalice",  34),
    Treasure(0x801ce418,	4,	"Nice Cup", 35),
    Treasure(0x801ce418,	8,	"Ornate Decanter",  36),
    Treasure(0x801ce418,	0x10,	"Glass Decanter",   37),
    Treasure(0x801ce418,	0x20,	"Nice Saucer",  38),
    Treasure(0x801ce418,	0x40,	"Glass Bowl",   39),
    Treasure(0x801ce418,	0x80,	"Jade Box", 40),
    Treasure(0x801ce428,	1,	"Nice Goblet",  41),
    Treasure(0x801ce428,	2,	"Violin",   42),
    Treasure(0x801ce428,	4,	"Earring",  43),
    Treasure(0x801ce428,	8,	"Jewelled Sword",   44),
    Treasure(0x801ce428,	0x10,	"Gold Tiara",   45),
    Treasure(0x801ce428,	0x20,	"Nice Sceptre", 46),
    Treasure(0x801ce428,	0x40,	"King's Crown", 47),
    Treasure(0x801ce428,	0x80,	"GameBoy Advance",  48),
    Treasure(0x801ce448,	1,	"Big Mirror",   49),
    Treasure(0x801ce448,	2,	"Antique Clock",    50),
    Treasure(0x801ce448,	4,	"Gold Mirror",  51),
    Treasure(0x801ce448,	8,	"Stained Glass",    52),
    Treasure(0x801ce448,	0x10,	"Bronze Mirror",    53),
    Treasure(0x801ce448,	0x20,	"Gold Clock",   54),
    Treasure(0x801ce448,	0x40,	"Gold Pocketwatch", 55),
    Treasure(0x801ce448,	0x80,	"Crazy Glasses",    56),
    Treasure(0x801ce458,	1,	"Ancient Ring", 57),
    Treasure(0x801ce458,	2,	"Ancient Necklace", 58),
    Treasure(0x801ce458,	4,	"Ancient Relief",   59),
    Treasure(0x801ce458,	8,	"Small Pyramid",    60),
    Treasure(0x801ce458,	0x10,	"Ancient Bracelet", 61),
    Treasure(0x801ce458,	0x20,	"Anubis Statue",   62),
    Treasure(0x801ce458,	0x40,	"Monarch Mask", 63),
    Treasure(0x801ce458,	0x80,	"Nintendo GameCube",    64),]

class Chest(NamedTuple):
    value: int
    name: str
    loc: int
    CheckID: int

Chests_b: dict = [
    Chest(1,	"Greenhorn Forest Red Chest",	0x801ce408, 1),
    Chest(2,	"Greenhorn Forest Yellow Chest",	0x801ce408, 2),
    Chest(4,	"Greenhorn Forest Chartreuse Chest",	0x801ce408, 3),
    Chest(8,	"Greenhorn Forest Green Chest",	0x801ce408, 4),
    Chest(0x10,	"Greenhorn Forest Cyan Chest",	0x801ce408, 5),
    Chest(0x20,	"Greenhorn Forest Blue Chest",	0x801ce408, 6),
    Chest(0x40,	"Greenhorn Forest Purple Chest",	0x801ce408, 7),
    Chest(0x80,	"Greenhorn Forest Pink Chest",	0x801ce408, 8),
    Chest(1,	"Greenhorn Ruins Red Chest",	0x801ce409, 9),
    Chest(2,	"Greenhorn Ruins Yellow Chest",	0x801ce409, 10),
    Chest(4,	"Greenhorn Ruins Chartreuse Chest",	0x801ce409, 11),
    Chest(8,	"Greenhorn Ruins Green Chest",	0x801ce409, 12),
    Chest(0x10,	"Greenhorn Ruins Cyan Chest",	0x801ce409, 13),
    Chest(0x20,	"Greenhorn Ruins Blue Chest",	0x801ce409, 14),
    Chest(0x40,	"Greenhorn Ruins Purple Chest",	0x801ce409, 15),
    Chest(0x80,	"Greenhorn Ruins Pink Chest",	0x801ce409, 16),
    Chest(1,	"Horror Manor Red Chest",	0x801ce40a, 17),
    Chest(2,	"Horror Manor Yellow Chest",	0x801ce40a, 18),
    Chest(4,	"Horror Manor Chartreuse Chest",	0x801ce40a, 19),
    Chest(8,	"Horror Manor Green Chest",	0x801ce40a, 20),
    Chest(0x10,	"Horror Manor Cyan Chest",	0x801ce40a, 21),
    Chest(0x20,	"Horror Manor Blue Chest",	0x801ce40a, 22),
    Chest(0x40,	"Horror Manor Purple Chest",	0x801ce40a, 23),
    Chest(0x80,	"Horror Manor Pink Chest",	0x801ce40a, 24),
    Chest(1,	"Wonky Circus Red Chest",	0x801ce40b, 25),
    Chest(2,	"Wonky Circus Yellow Chest",	0x801ce40b, 26),
    Chest(4,	"Wonky Circus Chartreuse Chest",	0x801ce40b, 27),
    Chest(8,	"Wonky Circus Green Chest",	0x801ce40b, 28),
    Chest(0x10,	"Wonky Circus Cyan Chest",	0x801ce40b, 29),
    Chest(0x20,	"Wonky Circus Blue Chest",	0x801ce40b, 30),
    Chest(0x40,	"Wonky Circus Purple Chest",	0x801ce40b, 31),
    Chest(0x80,	"Wonky Circus Pink Chest",	0x801ce40b, 32),
    Chest(1,	"Shivering Mountains Red Chest",	0x801ce40c, 33),
    Chest(2,	"Shivering Mountains Yellow Chest",	0x801ce40c, 34),
    Chest(4,	"Shivering Mountains Chartreuse Chest",	0x801ce40c, 35),
    Chest(8,	"Shivering Mountains Green Chest",	0x801ce40c, 36),
    Chest(0x10,	"Shivering Mountains Cyan Chest",	0x801ce40c, 37),
    Chest(0x20,	"Shivering Mountains Blue Chest",	0x801ce40c, 38),
    Chest(0x40,	"Shivering Mountains Purple Chest",	0x801ce40c, 39),
    Chest(0x80,	"Shivering Mountains Pink Chest",	0x801ce40c, 40),
    Chest(1,	"Beanstalk Way Red Chest",	0x801ce40d, 41),
    Chest(2,	"Beanstalk Way Yellow Chest",	0x801ce40d, 42),
    Chest(4,	"Beanstalk Way Chartreuse Chest",	0x801ce40d, 43),
    Chest(8,	"Beanstalk Way Green Chest",	0x801ce40d, 44),
    Chest(0x10,	"Beanstalk Way Cyan Chest",	0x801ce40d, 45),
    Chest(0x20,	"Beanstalk Way Blue Chest",	0x801ce40d, 46),
    Chest(0x40,	"Beanstalk Way Purple Chest",	0x801ce40d, 47),
    Chest(0x80,	"Beanstalk Way Pink Chest",	0x801ce40d, 48),
    Chest(1,	"Mirror Mansion Red Chest",	0x801ce40e, 49),
    Chest(2,	"Mirror Mansion Yellow Chest",	0x801ce40e, 50),
    Chest(4,	"Mirror Mansion Chartreuse Chest",	0x801ce40e, 51),
    Chest(8,	"Mirror Mansion Green Chest",	0x801ce40e, 52),
    Chest(0x10,	"Mirror Mansion Cyan Chest",	0x801ce40e, 53),
    Chest(0x20,	"Mirror Mansion Blue Chest",	0x801ce40e, 54),
    Chest(0x40,	"Mirror Mansion Purple Chest",	0x801ce40e, 55),
    Chest(0x80,	"Mirror Mansion Pink Chest",	0x801ce40e, 56),
    Chest(1,	"Pecan Sands Red Chest",	0x801ce40f, 57),
    Chest(2,	"Pecan Sands Yellow Chest",	0x801ce40f, 58),
    Chest(4,	"Pecan Sands Chartreuse Chest",	0x801ce40f, 59),
    Chest(8,	"Pecan Sands Green Chest",	0x801ce40f, 60),
    Chest(0x10,	"Pecan Sands Cyan Chest",	0x801ce40f, 61),
    Chest(0x20,	"Pecan Sands Blue Chest",	0x801ce40f, 62),
    Chest(0x40,	"Pecan Sands Purple Chest",	0x801ce40f, 63),
    Chest(0x80,	"Pecan Sands Pink Chest",	0x801ce40f, 64),]

class Spriteling(NamedTuple):
    loc: int
    value: int
    name: str
    ItemID: int
    classification =  FILL
    ItemType = 2

Spritelings_h: dict = [
    Spriteling(0x801ce3b4,	1,	"Greenhorn Forest Red Spriteling",  65),
    Spriteling(0x801ce3b4,	2,	"Greenhorn Forest Yellow Spriteling",   66),
    Spriteling(0x801ce3b4,	4,	"Greenhorn Forest Green Spriteling",    67),
    Spriteling(0x801ce3b4,	8,	"Greenhorn Forest Blue Spriteling", 68),
    Spriteling(0x801ce3b4,	0x10,	"Greenhorn Forest Purple Spriteling",   69),
    Spriteling(0x801ce3c4,	1,	"Greenhorn Ruins Red Spriteling",   70),
    Spriteling(0x801ce3c4,	2,	"Greenhorn Ruins Yellow Spriteling",    71),
    Spriteling(0x801ce3c4,	4,	"Greenhorn Ruins Green Spriteling", 72),
    Spriteling(0x801ce3c4,	8,	"Greenhorn Ruins Blue Spriteling",  73),
    Spriteling(0x801ce3c4,	0x10,	"Greenhorn Ruins Purple Spriteling",    74),
    Spriteling(0x801ce3e4,	1,	"Horror Manor Red Spriteling",  75),
    Spriteling(0x801ce3e4,	2,	"Horror Manor Yellow Spriteling",   76),
    Spriteling(0x801ce3e4,	4,	"Horror Manor Green Spriteling",    77),
    Spriteling(0x801ce3e4,	8,	"Horror Manor Blue Spriteling", 78),
    Spriteling(0x801ce3e4,	0x10,	"Horror Manor Purple Spriteling",   79),
    Spriteling(0x801ce3f4,	1,	"Wonky Circus Red Spriteling",  80),
    Spriteling(0x801ce3f4,	2,	"Wonky Circus Yellow Spriteling",   81),
    Spriteling(0x801ce3f4,	4,	"Wonky Circus Green Spriteling",    82),
    Spriteling(0x801ce3f4,	8,	"Wonky Circus Blue Spriteling", 83),
    Spriteling(0x801ce3f4,	0x10,	"Wonky Circus Purple Spriteling",   84),
    Spriteling(0x801ce414,	1,	"Shivering Mountains Red Spriteling",   85),
    Spriteling(0x801ce414,	2,	"Shivering Mountains Yellow Spriteling",    86),
    Spriteling(0x801ce414,	4,	"Shivering Mountains Green Spriteling", 87),
    Spriteling(0x801ce414,	8,	"Shivering Mountains Blue Spriteling",  88),
    Spriteling(0x801ce414,	0x10,	"Shivering Mountains Purple Spriteling",    89),
    Spriteling(0x801ce424,	1,	"Beanstalk Way Red Spriteling", 90),
    Spriteling(0x801ce424,	2,	"Beanstalk Way Yellow Spriteling",  91),
    Spriteling(0x801ce424,	4,	"Beanstalk Way Green Spriteling",   92),
    Spriteling(0x801ce424,	8,	"Beanstalk Way Blue Spriteling",    93),
    Spriteling(0x801ce424,	0x10,	"Beanstalk Way Purple Spriteling",  94),
    Spriteling(0x801ce444,	1,	"Mirror Mansion Red Spriteling", 95),
    Spriteling(0x801ce444,	2,	"Mirror Mansion Yellow Spriteling", 96),
    Spriteling(0x801ce444,	4,	"Mirror Mansion Green Spriteling",  97),
    Spriteling(0x801ce444,	8,	"Mirror Mansion Blue Spriteling",   98),
    Spriteling(0x801ce444,	0x10,	"Mirror Mansion Purple Spriteling", 99),
    Spriteling(0x801ce454,	1,	"Pecan Way Red Spriteling", 100),
    Spriteling(0x801ce454,	2,	"Pecan Way Yellow Spriteling",  101),
    Spriteling(0x801ce454,	4,	"Pecan Way Green Spriteling",   102),
    Spriteling(0x801ce454,	8,	"Pecan Way Blue Spriteling",    103),
    Spriteling(0x801ce454,	0x10,	"Pecan Way Purple Spriteling",  104),]

class Cage(NamedTuple):
    value: int
    name: str
    loc: int
    CheckID: int

Cages_b: dict = [ 

    Cage(1,	"Greenhorn Forest Caged Red Spriteling",	0x801ce3d8, 65),
    Cage(2,	"Greenhorn Forest Caged Yellow Spriteling",	0x801ce3d8, 66),
    Cage(4,	"Greenhorn Forest Caged Green Spriteling",	0x801ce3d8, 67),
    Cage(8,	"Greenhorn Forest Caged Blue Spriteling",	0x801ce3d8, 68),
    Cage(0x10,	"Greenhorn Forest Caged Purple Spriteling",	0x801ce3d8, 69),
    Cage(1,	"Greenhorn Ruins Caged Red Spriteling",	0x801ce3d9, 70),
    Cage(2,	"Greenhorn Ruins Caged Yellow Spriteling",	0x801ce3d9, 71),
    Cage(4,	"Greenhorn Ruins Caged Green Spriteling",	0x801ce3d9, 72),
    Cage(8,	"Greenhorn Ruins Caged Blue Spriteling",	0x801ce3d9, 73),
    Cage(0x10,	"Greenhorn Ruins Caged Purple Spriteling",	0x801ce3d9, 74),
    Cage(1,	"Horror Manor Caged Red Spriteling",	0x801ce3da, 75),
    Cage(2,	"Horror Manor Caged Yellow Spriteling",	0x801ce3da, 76),
    Cage(4,	"Horror Manor Caged Green Spriteling",	0x801ce3da, 77),
    Cage(8,	"Horror Manor Caged Blue Spriteling",	0x801ce3da, 78),
    Cage(0x10,	"Horror Manor Caged Purple Spriteling",	0x801ce3da, 79),
    Cage(1,	"Wonky Circus Caged Red Spriteling",	0x801ce3db, 80),
    Cage(2,	"Wonky Circus Caged Yellow Spriteling",	0x801ce3db, 81),
    Cage(4,	"Wonky Circus Caged Green Spriteling",	0x801ce3db, 82),
    Cage(8,	"Wonky Circus Caged Blue Spriteling",	0x801ce3db, 83),
    Cage(0x10,	"Wonky Circus Caged Purple Spriteling",	0x801ce3db, 84),
    Cage(1,	"Shivering Mountains Caged Red Spriteling",	0x801ce3dc, 85),
    Cage(2,	"Shivering Mountains Caged Yellow Spriteling",	0x801ce3dc, 86),
    Cage(4,	"Shivering Mountains Caged Green Spriteling",	0x801ce3dc, 87),
    Cage(8,	"Shivering Mountains Caged Blue Spriteling",	0x801ce3dc, 88),
    Cage(0x10,	"Shivering Mountains Caged Purple Spriteling",	0x801ce3dc, 89),
    Cage(1,	"Beanstalk Way Caged Red Spriteling",	0x801ce3dd, 90),
    Cage(2,	"Beanstalk Way Caged Yellow Spriteling",	0x801ce3dd, 91),
    Cage(4,	"Beanstalk Way Caged Green Spriteling",	0x801ce3dd, 92),
    Cage(8,	"Beanstalk Way Caged Blue Spriteling",	0x801ce3dd, 93),
    Cage(0x10,	"Beanstalk Way Caged Purple Spriteling",	0x801ce3dd, 94),
    Cage(1,	"Mirror Mansion Caged Red Spriteling",	0x801ce3de, 95),
    Cage(2,	"Mirror Mansion Caged Yellow Spriteling",	0x801ce3de, 96),
    Cage(4,	"Mirror Mansion Caged Green Spriteling",	0x801ce3de, 97),
    Cage(8,	"Mirror Mansion Caged Blue Spriteling",	0x801ce3de, 98),
    Cage(0x10,	"Mirror Mansion Caged Purple Spriteling",	0x801ce3de, 99),
    Cage(1,	"Pecan Way Caged Red Spriteling",	0x801ce3df, 100),
    Cage(2,	"Pecan Way Caged Yellow Spriteling",	0x801ce3df, 101),
    Cage(4,	"Pecan Way Caged Green Spriteling",	0x801ce3df, 102),
    Cage(8,	"Pecan Way Caged Blue Spriteling",	0x801ce3df, 103),
    Cage(0x10,	"Pecan Way Caged Purple Spriteling",	0x801ce3df, 104),]

class BossMedal(NamedTuple):
    loc = 0x801ce3ac
    value: int
    name: str
    ItemID: int
    classification = PROG
    ItemType = 3

BossMedals_h: dict = [
    BossMedal(1,	"Greenfist Boss Medal", 105),
    BossMedal(2,	"Sandworm Boss Medal",  106),
    BossMedal(4,	"DinoMighty Big Key Fragment",  107),
    BossMedal(8,	"Brawl Doll Boss Medal",   108),
    BossMedal(0x10,	"Clown-a-Round Boss Medal", 109),
    BossMedal(0x20,	"Dual Dragon Big Key Fragment", 110),
    BossMedal(0x40,	"Winter Windster Boss Medal",   111),
    BossMedal(0x80,	"Spideraticus Boss Medal",  112),
    BossMedal(0x100,	"Red-Brief J Big Key Fragment", 113),
    BossMedal(0x200,	"The Mean Emcee Boss Medal",    114),
    BossMedal(0x400,	"Ironsider Boss Medal", 115),
    BossMedal(0x800,	"Captain Skull Big Key Fragment",   116),]

class StageDoor(NamedTuple):
    loc = 0x801ce3d0
    value: int
    name: str
    ItemID: int
    classification = PROG
    ItemType = 4

Doors_b: dict = [
    StageDoor(1,	"Greenhorn Ruins Door", 117),
    StageDoor(2,	"DinoMighty's Showdown Door",   118),
    StageDoor(4,	"Horror Manor Door",    119),
    StageDoor(8,	"Wonky Circus Door",    120),
    StageDoor(0x10,	"Dual Dragon's Showdown Door",  121),
    StageDoor(0x20,	"Shivering Mountains Door", 122),
    StageDoor(0x40,	"Beanstalk Way Door",   123),
    StageDoor(0x80,	"Red-Brief J's Showdown Door",  124),
    StageDoor(0x100,	"Mirror Mansion Door",  125),
    StageDoor(0x200,	"Pecan Sands Door", 126),
    StageDoor(0x400,	"Captain Skull's Showdown Door",    127),]

class BossBeat(NamedTuple):
    loc = 0x801ce3d2
    value: int
    name: str
    CheckID: int

Bosses_b: dict = [
    BossBeat(1,	"Defeated Greenfist",   105),
    BossBeat(2,	"Defeated Sandworm",    106),
    BossBeat(4,	"Defeated DinoMighty",  107),
    BossBeat(8,	"Defeated Brawl Doll",  108),
    BossBeat(0x10,	"Defeated Clown-a-Round",   109),
    BossBeat(0x20,	"Defeated Dual Dragon", 110),
    BossBeat(0x40,  "Defeated Winter Windster", 111),
    BossBeat(0x80,	"Defeated Spideraticus",    112),
    BossBeat(0x10,	"Defeated Red-Brief J", 113),
    BossBeat(0x200,	"Defeated The Mean Emcee",  114),
    BossBeat(0x400,	"Defeated Ironsider",   115),
    BossBeat(0x800,	"Defeated Captain Skull",   116),
    BossBeat(0x1000,  "Defeated Black Jewel", 117),]

class Junk(NamedTuple):
    loc: int
    value: int
    name: str
    ItemID: int
    classification = FILL
    ItemType = 5

JunkItems: dict = [
    Junk(0x801ce3a4,    +50, "50 coins", 128),
    Junk(DME.read_word(0x801c5820) + 0xd8, +2, "Garlic", 129),
]

class Trap(NamedTuple):
    loc: int 
    value: int
    name: str
    ItemID: int
    classification = TRAP
    ItemType = 6

TrapItems: dict = [
    Trap(0x801ce3a4,  -50, "Unithorn Attack", 130),
    Trap(DME.read_word(0x801c5820) + 0xd8,  0,  "Death Trap",   131),
    Trap(DME.read_word(0x801c5820) + 0xd8,  -2, "Take Damage", 132),
]

ITEM_TABLE: dict = [
    Spritelings_h,
    TrapItems,
    JunkItems,
    Treasures_h,
    BossMedals_h,
    Doors_b,
]

CHECK_TABLE: dict = [
    Chests_b,
    Cages_b,
    Bosses_b,
]