from Options import Choice, NamedRange, PerGameCommonOptions, Range, DeathLink
from dataclasses import dataclass

class Goal(Choice):
    """Victory condition for the game.
    Final Boss: Defeat the Black Jewel after collecting a set amount of Big Key Fragments
    Fragments: Collect a set amount of Big Key Fragments to win"""
    display_name = "Goal"
    default = 0
    option_final_boss = 0


class StartingFragments(Range):
    """How many Big Key Fragments are given on start?
    Recommended: 2 for a large pool of checks, 4 for a small or solo playthrough, set to 4 by default"""
    display_name = "Big Key Fragment Requirement"
    default = 0
    range_start = 0
    range_end = 4

class SpritelingRequirement(NamedRange):
    """How many spritelings are needed for goal completion
    Silver ending (21) by default, you may change to other endings here:
    Plant: 0-1
    Wooden: 2-10
    Stone: 11-20
    Silver: 21-30
    Golden: 31-39
    Treasure: all 40
    or set your own!"""
    display_name = "Ending Type"
    default = 21
    range_start = 0
    range_end = 40
    special_range_names = {
        "plant": 0,
        "wooden": 2,
        "stone": 11,
        "silver": 21,
        "golden": 31,
        "treasure": 40,}

#class StageRandomiser(Choice):
#    """randomises which stages are unlocked instead of opening them one by one, set to on by default"""
#    display_name = "Stage Randomiser"
#    option_vanilla = 0
#    option_default = 1
#    default = 1

@dataclass
class WwOptions(PerGameCommonOptions):
    goal: Goal
    big_key_fragments: StartingFragments
    endingtype: SpritelingRequirement
    #stage_randomiser: StageRandomiser
    death_link: DeathLink