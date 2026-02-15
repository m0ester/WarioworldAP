from BaseClasses import CollectionState
from .gamedata import GFRedDiamonds, GRRedDiamonds, HMRedDiamonds, WCRedDiamonds ,SMRedDiamonds, BWRedDiamonds, MMRedDiamonds, PSRedDiamonds

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

def has_greenfist(world, state: CollectionState):
    return state.has_from_list_unique(GFRedDiamonds, world.player, 3)

def has_sandworm(world, state: CollectionState):
    return state.has_from_list_unique(GRRedDiamonds, world.player, 3)

def has_brawldoll(world, state: CollectionState):
    return state.has_from_list_unique(HMRedDiamonds, world.player, 4)

def has_clownaround(world, state: CollectionState):
    return state.has_from_list_unique(WCRedDiamonds, world.player, 4)

def has_winterwindster(world, state: CollectionState):
    return state.has_from_list_unique(SMRedDiamonds, world.player, 5)

def has_spideraticus(world, state: CollectionState):
    return state.has_from_list_unique(BWRedDiamonds, world.player, 5)

def has_themeanemcee(world, state: CollectionState):
    return state.has_from_list_unique(MMRedDiamonds, world.player, 6)

def has_ironsider(world, state: CollectionState):
    return state.has_from_list_unique(PSRedDiamonds, world.player, 6)


def get_rules(world):
    rules = {
        "entrances": {
            "Menu -> FinalBoss":
                lambda state: has_blackjewel(world,state),

            "Menu -> Greenhorn Forest":
                lambda state: True,

            "Greenhorn Forest -> Greenfist":
                lambda state: has_greenfist(world, state),

            "Menu -> Greenhorn Ruins":
                lambda state: has_greenhornruins(world, state),

            "Greenhorn Ruins -> Sandworm":
                lambda state: has_sandworm(world, state),

            "Menu -> DinoMighty's Showdown":
                lambda state: has_dinomighty(world, state),

            "Menu -> Horror Manor":
                lambda state: has_horrormanor(world, state),

            "Horror Manor -> Brawl Doll":
                lambda state: has_brawldoll(world, state),

            "Menu -> Wonky Circus":
                lambda state: has_wonkycircus(world, state),

            "Wonky Circus -> Clown-a-Round":
                lambda state: has_wonkycircus(world, state),

            "Menu -> Dual Dragon's Showdown":
                lambda state: has_dualdragon(world, state),

            "Menu -> Shivering Mountains":
                lambda state: has_shivering(world, state),

            "Shivering Mountains -> Winter Windster":
                lambda state: has_winterwindster(world, state),

            "Menu -> Beanstalk Way":
                lambda state: has_beanstalkway(world, state),

            "Beanstalk Way -> Spideraticus":
                lambda state: has_spideraticus(world, state),

            "Menu -> Red-Brief J's Showdown":
                lambda state: has_redbriefj(world, state),

            "Menu -> Mirror Mansion":
                lambda state: has_mirrormansion(world, state),

            "Mirror Mansion -> The Mean Emcee":
                lambda state: has_themeanemcee(world, state),

            "Menu -> Pecan Sands":
                lambda state: has_pecansands(world, state),

            "Pecan Sands -> Ironsider":
                lambda state: has_ironsider(world, state),

            "Menu -> Captain Skull's Showdown":
                lambda state: has_captainskull(world, state),
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
    world.multiworld.completion_condition[world.player] = lambda state: state.can_reach_location("VictoryLoc", world.player)
    #and WwOptions.ending == SpritelingsCollected)
