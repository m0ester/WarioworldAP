from BaseClasses import Region

regions = [
    "Greenhorn Forest",
    "Greenhorn Ruins",
    "DinoMighty's Showdown",
    "Horror Manor",
    "Wonky Circus",
    "Dual Dragon's Showdown",
    "Shivering Mountains",
    "Beanstalk Way",
    "Red-Brief J's Showdown",
    "Mirror Mansion",
    "Pecan Sands",
    "Captain Skull's Showdown",
]

def create_region(world, name) -> Region:
    reg = Region(name, world.player, world.multiworld)
    world.multiworld.regions.append(reg)
    return reg

def create_regions(world):
    create_region(world, "Menu")
    for name in regions:
        create_region(world, name)


def connect_regions(world):
    for name in regions:
        from_region = world.get_region("Menu")
        to_region = world.get_region(name)
        from_region.connect(to_region, f"Menu -> {name}")