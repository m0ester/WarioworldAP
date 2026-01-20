class PlayerInfo():
    """addresses for all data in the game that are relevant for an APworld
    w = word
    h = half
    bh = bitfield half
    b = byte
    bb = bitfield byte"""
    #vanilla addresses:
    CharInfo_w = 0x801ce3a0
    #Vanilla Offsets
    Coins_w = +0x4
    Kills_w = +0x8
    Medals_bh = +0xc
    #custom addresses
    DoorsOpened_bh = +0x30
    BossesBeat_bh = +0x32
    
class StageInfo():
    #vanilla addresses
    GF = 0X801CE3B0
    GR = 0X801CE3C0
    HM = 0X801CE3E0
    WC = 0X801CE3F0
    SM = 0X801CE410
    BW = 0X801CE420
    MM = 0X801CE440
    PS = 0X801CE450

    #vanilla offsets
    """All bitfield halves except BRC
    BRC = BattleRing Clears
    Sprite = Spritelings
    GSF = Gold Statue Fragments
    RDF = Red Diamond Fragments
    RDFU = Red Diamond Fragments Used
    C for checks"""
    BRC = +0x0
    Sprite = +0x4
    GSF = +0x6
    Treasure = +0x8
    RDF = +0xa
    RDFU = +0xc

    #custom addresses
    SpriteC = 0x801ce3d8
    GSFC = 0x801ce400
    TreasureC = 0x801ce408
    RDFC = 0x801ce430

    #custom offsets
    """all bitfield bytes"""
    GFC = +0X0
    GRC = +0X1
    HMC = +0X2
    WCC = +0X3
    SMC = +0X4
    BWC = +0X5
    MMC = +0X6
    PSC = +0X7