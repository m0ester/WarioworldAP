from BaseClasses import CollectionState

def has_greenhornruins(world, state: CollectionState):
    return state.has("Greenhorn Ruins Door", world.player)

def has_dinomighty(world, state: CollectionState):
    return state.has("DinoMighty's Showdown Door", world.player)

def has_horrormanor(world, state: CollectionState):
    return state.has("Horror Manor Door", world.player)

def has_wonkycircus(world, state: CollectionState):
    return state.has("Wonky Circus Door", world.player)

def has_dualdragon(world, state: CollectionState):
    return state.has("Dual Dragon's Showdown Door", world.player)

def has_shivering(world, state: CollectionState):
    return state.has("Shivering Mountains Door", world.player)

def has_beanstalkway(world, state: CollectionState):
    return state.has("Beanstalk Way Door", world.player)

def has_redbriefj(world, state: CollectionState):
    return state.has("Red-Brief J's Showdown Door", world.player)

def has_mirrormansion(world, state: CollectionState):
    return state.has("Mirror Mansion Door", world.player)

def has_pecansands(world, state: CollectionState):
    return state.has("Pecan Sands Door", world.player)

def has_captainskull(world, state: CollectionState):
    return state.has("Captain Skull's Showdown Door", world.player)

def has_blackjewel(world, state: CollectionState):
    return (state.has("DinoMighty Big Key Fragment", world.player)
            and state.has("Dual Dragon Big Key Fragment", world.player)
            and state.has("Red-Brief J Big Key Fragment", world.player)
            and state.has("Captain Skull Big Key Fragment", world.player))

def get_rules(world):
    rules = {
        "entrances": {
            "Menu -> Greenhorn Forest":
                lambda state: True,

            "Menu -> Greenhorn Ruins":
                lambda state:
                    state.has("Greenhorn Ruins Door", world.player),

            "Menu -> DinoMighty's Showdown":
                lambda state:
                    state.has("DinoMighty's Showdown Door", world.player),

            "Menu -> Horror Manor":
                lambda state:
                state.has("Horror Manor Door", world.player),

            "Menu -> Wonky Circus":
                lambda state:
                state.has("Wonky Circus Door", world.player),

            "Menu -> Dual Dragon's Showdown":
                lambda state:
                state.has("Dual Dragon's Showdown Door", world.player),

            "Menu -> Shivering Mountains":
                lambda state:
                state.has("Shivering Mountains Door", world.player),

            "Menu -> Beanstalk Way":
                lambda state:
                state.has("Beanstalk Way Door", world.player),

            "Menu -> Red-Brief J's Showdown":
                lambda state:
                state.has("Red-Brief J's Showdown Door", world.player),

            "Menu -> Mirror Mansion":
                lambda state:
                state.has("Mirror Mansion Door", world.player),

            "Menu -> Pecan Sands":
                lambda state:
                state.has("Pecan Sands Door", world.player),

            "Menu -> Captain Skull's Showdown":
                lambda state:
                state.has("Captain Skull's Showdown Door", world.player),
        }
    }
    return rules


def set_rules(world):
    from . import WwWorld
    world: WwWorld
    rules_lookup = get_rules(world)
    for entrance_name, rule in rules_lookup["entrances"].items():
        try:
            world.get_entrance(entrance_name).access_rule = rule
        except KeyError:
            pass

    #world.get_location("Victory").access_rule = lambda state: False
    world.multiworld.completion_condition[world.player] = lambda state: has_blackjewel(world, state)

