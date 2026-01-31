from Options import Choice, NamedRange, PerGameCommonOptions, Range, DeathLink

class Goal(Choice):
    """Victory condition for the game.
    Final Boss: Defeat the Black Jewel after collecting a set amount of Big Key Fragments
    Fragments: Collect a set amount of Big Key Fragments to win"""
    display_name = "Goal"
    option_FinalBoss = 0


class FragmentRequirement(Range):
    """How many Big Key Fragments are required to complete the set goal
    Recommended: 2 for a large pool of checks, 4 for a small or solo playthrough, set to 4 by default"""
    display_name = "Big Key Fragment Requirement"
    default = 4
    Range_start = 0
    Range_end = 4

class SpritelingRequirement(NamedRange):
    """How many spritelings are needed for goal completion
    Plant ending by default, you may change to other endings here
    Plant: 1
    Wooden: 2 or more
    Stone: 11 or more
    Silver: 21 or more
    Golden: 31 or more
    Treasure: all 40
    or set your own!"""
    display_name = "Ending Type"
    default = 0
    range_start = 0
    range_end = 40
    special_range_names = {
        "plant": 0,
        "wooden": 2,
        "stone": 11,
        "silver": 21,
        "golden": 31,
        "treasure": 40,}

class StageRandomiser(Choice):
    """randomises which stages are unlocked instead of opening them one by one, set to on by default"""
    display_name = "Stage Randomiser"
    option_vanilla = 0
    option_default = 1
    default = 1

class WwOptions(PerGameCommonOptions):
    goal: Goal
    BigKeyFragments: FragmentRequirement
    ending: SpritelingRequirement
    stage_randomiser: StageRandomiser
    deathlink: DeathLink