import sys
import inspect
from pydses import *

map_name = 'm10_01_00_00'  # Undead Burg / Parish
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11010000
BASE_PART = 1010000


class DEBUG(IntEnum):
    GET_WATCHTOWER_BASEMENT_KEY = False
    GET_BURG_LATCHKEY = False
    BLIGHTTOWN_BELL_RUNG = False
    GET_PALADIN_GAUNTLETS = False
    GET_ASHEN_RING = False
    DARK_ANOR_LONDO = False
    RHEA_IN_PARISH = False
    TAURUS_DEMON_DEAD = False
    HAUNTING_SEMBLANCE_DEAD = False
    BELL_GARGOYLES_DEAD = False


class GOOD(IntEnum):
    ParishCellKey = 2017
    WorkersKey = 2018
    WatchtowerKey = 2019
    BurgLatchkey = 2021
    MasterKey = 2100
    

# Full list of gauntlets that can operate the Parish lever.
HeavyGauntlets = (22000, 72000, 82000, 122000, 442000, 472000, 492000, 532000, 692000)


class OBJ(IntEnum):
    ParishGate = 1011101
    FlamingBarrel = 1011102


class CUTSCENE(IntEnum):
    BellGargoylesAppear = 100110


class ITEMLOT(IntEnum):
    HornedScourgeReward = 2900
    UnhallowedSpecterReward = 2910
    ReaperRansackerReward = 2930
    LithicBond = 4900
    EmpyreanBond = 4920


class EVENT(IntEnum):
    BellGargoylesDead = 3
    ReaperRansackerDead = 11012015
    TaurusDemonDead = 11010901
    HornedScourgeDead = 11012013
    LithicWitness = 11502020
    EmpyreanWitness = 11502022
    CapraDemonTransformed = 11012000
    CapriciousThrallActive = 11012010
    CapriciousThrallTrapped = 11012011
    CapriciousThrallDead = 11012012
    HauntingSemblanceDead = 11010904
    UnhallowedSpecterDead = 11012014
    ParishGateOpen = 61010610
    BlighttownBellRung = 11400200
    ParishNitoCutsceneWarp = 11012003
    NitoDead = 7
    NitoAwake = 11310000
    BellGargoylesAppeared = 11012004
    DarkAnorLondo = 11510400
    JareelDead = 11510901
    BlackKnightSwordDead = 11812020
    BlackKnightGreatswordDead = 11012005
    BlackKnightHalberdDead = 11202002
    BlackKnightAxeDead = 11502000
    AllBlackKnightsDead = 11802000
    CapriciousThrallStableFooting = 11012501
    LithicBondObtained = 50004900
    EmpyreanBondObtained = 50004920

    GriggsFreedFromBurg = 1111
    GriggsInFirelink = 1112
    GriggsPreparingToLeaveFirelink = 1113
    GriggsHostile = 1114
    GriggsDead = 1115
    GriggsHollowInSens = 1117


class RING(IntEnum):
    RingOfAsh = 152


class TEXT(IntEnum):
    CapraDemonName = 2240
    CapriciousThrallName = 2245
    HauntingSemblance = 2300
    ProfaneImage = 2301
    UnhallowedSpecter = 2302
    ForbiddenVisage = 2302
    DoesNotOpenFromThisSide = 10010161
    Unlocked = 10010162  # use for one-sided shortcuts
    ItsLocked = 10010163
    Open = 10010400
    UsedWatchtowerBasementKey = 10010878
    UsedResidenceKey = 10010881
    BellLeverRusted = 10010176
    RingOfAshWarms = 10010627
    RingOfAshHot = 10010628
    ExamineStatue = 10010716
    LithicStatue = 10010717
    EmpyreanStatue = 10010719
    MasterKeyShattered = 10010883
    NothingHappened = 10010633
    ThrallHasFled = 10010123


class CHR(IntEnum):
    Player = 10000
    Hellkite = 1010300  # main Hellkite on bridge
    HauntingSemblance = 1010340
    ProfaneImage = 1010341
    DarkHauntingSemblance = 1010342
    UnhallowedSpecter = 1010343
    TaurusDemon = 1010700
    HornedScourge = 1010701
    CapraDemon = 1010750
    CapriciousThrall = 1010751
    BellGargoyleOne = 1010800
    BellGargoyleTwo = 1010801
    BellGargoyleStatue = 1010802
    ReaperGargoyle = 1010803
    RansackerGargoyle = 1010804
    BonfireBerenikeKnight = 1010320
    BlackKnightGreatsword = 1010350
    BarrelKicker = 1010103
    SenLithicStatue = 1010878
    SenEmpyreanStatue = 1010879
    FemaleUndeadMerchant = 6240
    Solaire = 6001  # normal NPC, not his summon
    Griggs = 6040
    Rhea = 6072
    Andre = 6190
    UndeadMerchant = 6230
    Oswald = 6370
    DepravedApostate = 6850


class ANIM(IntEnum):
    ThrallTransformation = 4000
    ThrallRetreat = 4001
    ThrallAmbushAttack = 4002


class REGION(IntEnum):
    BasementDoorTop = 1012676  # cannot open from this side
    BasementDoorBottom = 1012677  # open
    DepthsDoorTop = 1012678  # cannot open from this side
    DepthsDoorBottom = 1012679  # open
    BellCheck = 1012680
    FemaleMerchantRunawayOne = 1012685
    FemaleMerchantRunawayTwo = 1012686
    DepravedApostateTrigger = 1012687
    DepravedApostateSignPoint = 1012688
    HornedScourgeTrigger = 1012689
    HornedScourgeCatchBox = 1012690
    HornedScourgeStart = 1012691
    HauntingSemblanceTrigger = 1012876


def event0():
    """ Constructor event. """
    header(0)

    if DEBUG.GET_WATCHTOWER_BASEMENT_KEY:
        item.award_item_to_host_only(2720)
    if DEBUG.GET_BURG_LATCHKEY:
        item.award_item_to_host_only(1010460)
    if DEBUG.BLIGHTTOWN_BELL_RUNG:
        flag.enable(EVENT.BlighttownBellRung)
    if DEBUG.GET_PALADIN_GAUNTLETS:
        item.award_item_to_host_only(1300030)
    if DEBUG.GET_ASHEN_RING:
        item.award_item_to_host_only(2750)
    if DEBUG.DARK_ANOR_LONDO:
        flag.enable(EVENT.DarkAnorLondo)
    if DEBUG.TAURUS_DEMON_DEAD:
        flag.enable(EVENT.TaurusDemonDead)
    if DEBUG.HAUNTING_SEMBLANCE_DEAD:
        flag.enable(EVENT.HauntingSemblanceDead)
    if DEBUG.BELL_GARGOYLES_DEAD:
        flag.enable(EVENT.BellGargoylesDead)

    skip_if_event_flag_off(1, EVENT.DarkAnorLondo)
    light.set_area_texture_parambank_slot_index(10, 1)

    run_event(11010008)  # Register bonfires, ladders, and three hazardous fires.
    map.register_bonfire(11010968, 1011963)  # (New) Bonfire in old Capra Demon room.

    flag.disable(11010580)  # Reset flag for Sunlight Altar interaction.

    # If Parish gate is open, replay opening animation and enable navimesh through it.
    skip_if_event_flag_off(2, EVENT.ParishGateOpen)
    anim.end_animation(OBJ.ParishGate, 2)
    navimesh.add_navimesh_collision_bitflags(1013100, 1)

    # Host only: disable phantom fog walls.
    skip_if_client(22)
    for fog_wall, fog_sfx in zip((994, 996, 998, 988, 986, 984, 982, 980, 978, 976, 974),
                                 (995, 997, 999, 989, 987, 985, 983, 981, 979, 977, 975)):
        obj.disable(1011000 + fog_wall)
        sfx.delete_map_sfx(1011000 + fog_sfx, False)

    # Checkpoint fog.
    run_event_with_slot(11010090, 0, args=(1011700, 1011701, 1012600, 1012601))
    run_event_with_slot(11010090, 1, args=(1011702, 1011703, 1012602, 1012603))
    run_event_with_slot(11010090, 2, args=(1011788, 1011789, 1012604, 1012605))

    # Gravelord events.
    for gravelord_event in (5070, 5071, 5072):
        run_event(BASE_FLAG + gravelord_event)

    run_event(11010903)  # Stop Armored Tusk from respawning.
    run_event(11015110)  # Hollow ambush near Undead Merchant
    run_event(11015113)  # Trigger for archer on turret near locked house
    run_event(11015112)  # Hollow beneath Tusk who leads you into room full of them
    run_event(11015130)  # Crystal Lizard appears
    run_event(11010710)  # Crystal Lizard dies and awards items
    run_event(11010111)  # Hollow past bridge kicks open door
    run_event(11010120)  # Flaming barrel trap (moved to earlier)

    # DOORS

    # Applies special effect that lets you open one-way shortcuts to Lower Burg and Depths.
    run_event_with_slot(11010150, 0, args=(11010160, 1012401, 1012400))
    run_event_with_slot(11010150, 1, args=(11010161, REGION.BasementDoorBottom, REGION.BasementDoorTop))
    # Disables above shortcut doors once activated.
    run_event_with_slot(11010160, 0, args=(11010160, 1011314))  # Lower Burg gate door.
    run_event_with_slot(11010160, 1, args=(11010161, 1011311))  # Basement door to Lower Burg.

    # Open basic doors with a specific key or Master Key (can be closed again).
    run_event_with_slot(11010180, 1, args=(11010181, 10010881, 1011317, TEXT.MasterKeyShattered, GOOD.BurgLatchkey))
    run_event_with_slot(11010180, 2, args=(11010182, 10010881, 1011312, TEXT.MasterKeyShattered, GOOD.BurgLatchkey))
    run_event_with_slot(11010140, 0, args=(11010140, 10010881, 1011310, TEXT.MasterKeyShattered, GOOD.BurgLatchkey))
    run_event_with_slot(11010140, 1, args=(11010141, 10010876, 1011308, TEXT.MasterKeyShattered, GOOD.ParishCellKey))
    run_event_with_slot(11010140, 2, args=(11010142, 10010878, 1011316, TEXT.MasterKeyShattered, GOOD.WatchtowerKey))
    # Door from the Depths to Lower Burg (Workers' Key) can't be closed again.
    run_event_with_slot(11010162, 0, args=(11010162, 10010877, 1011306, TEXT.MasterKeyShattered, GOOD.WorkersKey))

    run_event_with_slot(11010101, 0, args=(1011320, 1, 101, 121, 7110))  # Aqueduct shortcut.
    run_event_with_slot(11010102, 0, args=(11010142, 1011320, 100))  # Wrong side of aqueduct shortcut.

    # Parish gate events.
    run_event(11015185)  # Parish gate lever operation flags (triggered by autonomous lever).
    run_event(11010611)  # Wait ten frames before lever becomes usable again.
    run_event(11010600)  # Gate opening and closing.
    run_event(11010601)  # Damage from being crushed by gate.
    run_event(11015116)  # Trigger for gate-closing Hollow.
    run_event(11010609)  # Enable gate activation after enemy is triggered.
    run_event(11010607)  # Change gate-opening Hollow nest after they open the gate.
    run_event(11010608)  # Change nest of Armored Tusk depending on whether gate is opened or closed.

    # Miscellaneous.
    run_event(11010621)  # Pull lever opening gate near Sunlight Altar.
    run_event(11010700)  # Ring Bell of Awakening above Parish.
    run_event(11012002)  # (New) Award Bell achievement when you return from Nito cutscene.
    run_event(11015170)  # Play bell sounds online.
    run_event(11010100)  # Kick down shortcut ladder below bridge.
    run_event(11010780)  # Hellkite breaks a spire on its first landing above Sunlight Altar.
    run_event(11010580)  # Kneel to Sunlight Altar (complex).
    run_event(11010585)  # Enable flag for above event after two frames.
    run_event(11012005)  # (New) Black Knight Greatsword appears on watchtower if you have the Ring of Ash.
    run_event(11012006)  # (New) Flag for Oswald enabled when you approach the bell lever.
    run_event(11012008)  # (New) Darkwraiths appear, and kill Channelers, in Dark Anor Londo, and Hollows power up.
    run_event(11012020)  # (New) Lithic Sen statue.
    run_event(11012021)  # (New) Empyrean Sen statue.
    run_event(11012017)  # (New) Message that Thrall has fled appears on death.
    run_event(11012044)  # (New) Monitor resting at Parish Turret bonfire for warping.

    # BELL GARGOYLES

    sound.disable_map_sound(1013800)
    skip_if_event_flag_on(1, EVENT.BellGargoylesDead)
    sound.disable_map_sound(1013801)  # Play ambience on the Parish roof if Gargoyles are dead.

    # Dead:
    skip_if_event_flag_off(6, EVENT.BellGargoylesDead)
    run_event(11015392)
    obj.disable(1011990)
    sfx.delete_map_sfx(1011991, False)
    obj.disable(1011992)
    sfx.delete_map_sfx(1011993, False)
    skip(11)
    # Alive:
    for gargoyle_event in (0, 5390, 5391, 5393, 5392, 1, 5394, 5395, 5396):
        # Standard, except for 5396, which triggers the second Gargoyle. Tails are initialized in 5392.
        run_event(BASE_FLAG + gargoyle_event)
    run_event_with_slot(11015397, 0, args=(1010800, 5350, 5350, 1010810))  # Tail cut reward for first Gargoyle.
    run_event_with_slot(11015398, 0, args=(1010801, 1010811))  # Remove tail of second Gargoyle.

    # REAPER AND RANSACKER

    run_event(11015472)
    run_event(11012015)

    # TAURUS DEMON

    sound.disable_map_sound(1013802)
    # If Taurus Demon is dead:
    skip_if_event_flag_off(6, 11010901)
    run_event(11010901)  # Note that this script disables the Taurus Demon, not its behavior script.
    obj.disable(1011890)
    sfx.delete_map_sfx(1011891, False)
    obj.disable(1011892)
    sfx.delete_map_sfx(1011893, False)
    skip(8)
    # If Taurus Demon is alive:
    for taurus_event in (5380, 5381, 5383, 5382, 5384, 5385, 5386, 901):
        run_event(BASE_FLAG + taurus_event)

    # HORNED SCOURGE

    run_event(11015492)  # Trigger.
    run_event(11015494)  # Jumps back up if it falls off.
    run_event(11012013)  # Death.

    # CAPRA DEMON / CAPRICIOUS THRALL

    sound.disable_map_sound(1013803)
    sound.disable_map_sound(1013804)
    # Thrall is dead or gone:
    skip_if_event_flag_off(9, 11012000)
    run_event(11012000)
    obj.disable(1011790)
    sfx.delete_map_sfx(1011791, False)
    sfx.delete_map_sfx(1011771, False)
    sfx.delete_map_sfx(1011772, False)
    obj.disable(1011797)
    sfx.delete_map_sfx(1011798, False)
    sfx.delete_map_sfx(1011799, False)  # extra fog above entrance
    skip(9)
    flag.disable(EVENT.CapriciousThrallStableFooting)  # No saving in arena until Thrall is dead/gone.
    run_event(11015370)  # Host enters fog.
    run_event(11015371)  # Client enters fog.
    run_event(11015373)  # Battle trigger.
    run_event(11015372)  # Behavior.
    run_event(11015374)  # Music on.
    run_event(11015375)  # Music off.
    run_event(11010902)  # Death.
    run_event(11012000)  # Transforms into Thrall.

    # HAUNTING SEMBLANCE & PROFANE IMAGE (NEW)

    sound.disable_map_sound(1013805)
    # Already dead:
    skip_if_event_flag_off(7, EVENT.HauntingSemblanceDead)
    run_event(11010904)  # Disables both entities.
    obj.disable(1011792)
    sfx.delete_map_sfx(1011793, False)
    sfx.delete_map_sfx(1011794, False)  # this tall fog has two SFX parts
    obj.disable(1011795)
    sfx.delete_map_sfx(1011796, False)
    skip(9)
    run_event(11015360)
    run_event(11015361)
    run_event(11015363)
    run_event(11015362)
    run_event(11015364)
    run_event(11015365)
    run_event(11015366)  # Profane Image emerges
    run_event(11015367)  # Profane Image warps around
    run_event(11010904)

    # HAUNTING SEMBLANCE & UNHALLOWED SPECTER (NEW)

    run_event(11015482)  # Trigger.
    run_event(11015486)  # Unhallowed Specter appearance (runs warping event).
    run_event(11012014)  # Death.

    # HELLKITE

    # Flags:
    #  790: First encounter done.
    #  791: One-off bridge sweep done.
    #  900: Dead.
    # 5305: Jump down and engage player on the bridge (due to frustration).
    # 5306: Player is currently frustrating the hellkite (20 seconds before it jumps down).
    # 5310: Fire breath attack is underway (prevents further triggers until done).
    # 5311: Hellkite is down on the bridge with you at close-range.
    # 5317: Jump down and engage player on the bridge (due to being attacked).

    # Regions:
    # 1012302: Start point for bridge sweep.
    # 1012310: Main perch.
    # 1012330: Middle of bridge. (Originally only triggered fire after kicking the ladder.)
    # 1012331: Inside Altar bonfire room.
    # 1012332: First half of bridge. (Originally only triggered fire after kicking the ladder.)
    # 1012333: Far end of bridge, right under the perch.
    # 1012335: One side of the safe space (frustrates).
    # 1012336: Other side of the safe space (frustrates).

    # Hellkite is dead:
    skip_if_event_flag_off(2, 11010900)
    run_event(11010900)  # Dead or departed. ('Manually killed' at 10% health; immortal otherwise.)
    skip(29)
    # Hellkite is alive:
    run_event(11010899)  # Initialization.
    run_event(11010900)  # Dead or departed.
    run_event(11010782)  #
    run_event(11010783)
    run_event(11010790)  # First encounter.
    run_event(11010791)  # Arrival bridge swoop.
    run_event(11015301)  # Tail initialization and cut.
    run_event(11010784)  # Toggles flag 5300 based on Hellkite message 500 (on) and 600 (off).
    run_event(11015302)  # Fire breath trigger.
    run_event(11015303)  # Determines if 'frustration timer' should run (enables 5306).
    run_event(11015304)  # Runs 'frustration timer' for 20 seconds before enabling 5305.
    run_event(11010851)
    run_event(11010852)
    run_event_with_slot(11010890, 0, args=tuple(range(11015320, 11015327)))
    run_event_with_slot(11010890, 1, args=tuple(range(11015327, 11015334)))
    run_event_with_slot(11010890, 2, args=tuple(range(11015334, 11015341)))
    run_event(11010850)
    run_event(11015307)
    run_event(11015308)
    for slot, args in enumerate(zip((10, 20, 30, 40, 50, 60, 70, 80, 90, 100),
                                    (3000, 3001, 3002, 3009, 3010, 7004, 7005, 7008, 7009, 7011))):
        run_event_with_slot(11010200, slot, args=args)

    # Hollows hanging over the ledges below the start of Undead Burg. (Fourth argument is delay, always zero.)
    for slot, (hollow, trigger_hollow, distance, delay) in enumerate(zip((250, 251, 260, 261, 262, 263),
                                                                         (250, 250, 260, 261, 262, 262),
                                                                         (5.0, 5.5, 3.0, 4.0, 3.0, 3.0),
                                                                         (0.0, 0.0, 1.0, 0.0, 0.0, 0.0))):
        run_event_with_slot(11015250, slot, args=(BASE_PART + hollow, BASE_PART + trigger_hollow, distance, delay),
                            arg_types='iiff')

    # Thief ambushes in Lower Burg. First three have a delay after Capra Demon battle begins.
    run_event_with_slot(11010135, 0, args=(1011250, 1010150, 1012150, 13.0), arg_types='iiif')
    run_event_with_slot(11010135, 1, args=(1011251, 1010151, 1012150, 26.0), arg_types='iiif')
    run_event_with_slot(11010135, 2, args=(1011252, 1010152, 1012150, 39.0), arg_types='iiif')
    run_event_with_slot(11010130, 0, args=(1011253, 1010153, 1012151))
    run_event_with_slot(11010130, 1, args=(1011254, 1010154, 1012151))
    run_event_with_slot(11010130, 2, args=(1011255, 1010155, 1012151))

    # Non-respawning enemies:
    run_event_with_slot(11010860, 4, args=(1010131, 0, 0))  # (New) Crushed Hollow
    run_event_with_slot(11010860, 5, args=(1010371, 0, 0))  # (New) Lower Channeler
    run_event_with_slot(11010860, 6, args=(6010, 0, 0))  # Gate-opening Hollow
    run_event(11012007)  # Berenike Knight that prevents bonfire from appearing.
    run_event(11012016)  # Three Thieves in narrow Lower Burg (after all three are killed together).

    # Treasure corpses in pots.
    run_event_with_slot(11010400, 2, args=(1011652, 1011502))
    run_event_with_slot(11010400, 3, args=(1011653, 1011503))
    run_event_with_slot(11010400, 4, args=(1011654, 1011504))

    # Treasure chests.
    run_event_with_slot(11010650, 0, args=(1011670, 11010650))
    run_event_with_slot(11010650, 1, args=(1011671, 11010651))


def event50():
    """ NPC constructor. """
    header(50, 0)
    # (New) Disable Horned Scourge before it can be killed by kill planes.
    chr.disable(CHR.HornedScourge)

    # Reset positions of Solaire, Griggs, Rhea, Andre, Undead Merchant, Lautrec when sin is absolved (because this
    # is the map it's absolved in).
    run_event(11010583)

    # Havel removed here.
    chr.humanity_registration(6540, 8310)  # Solaire summon
    chr.humanity_registration(6590, 8462)  # Lautrec summon

    run_event(11015100)  # Solaire summon sign.
    run_event(11015101)  # Solaire enters Gargoyles fog.
    run_event(11015103)  # Lautrec summon sign.
    run_event(11015104)  # Lautrec enters Gargoyles fog.

    # (NEW) DEPRAVED APOSTATE (invasion)

    chr.humanity_registration(CHR.DepravedApostate, 8366)
    run_event(11015630)
    run_event(11010810)

    # SOLAIRE

    chr.humanity_registration(CHR.Solaire, 8310)
    skip_if_event_flag_on(4, 1007)  # Waiting at Sunlight Altar.
    skip_if_event_flag_on(3, 1004)  # Hostile in Undead Burg.
    skip_if_event_flag_on(2, 1001)  # Spoken to after Taurus Demon.
    skip_if_event_flag_on(1, 1000)  # Waiting after Taurus Demon.
    chr.disable(CHR.Solaire)  # Solaire only here given one of the above four story flags.
    # Move Solaire to Sunlight Altar if Anor Londo event complete. (This used to be a weird double skip-skip.)
    skip_if_event_flag_off(1, 11510594)
    warp.warp_and_set_floor(CHR.Solaire, 'region', 1012530, -1, 1013050)
    run_event_with_slot(11010510, 0, args=(CHR.Solaire, 1004))  # Hostile (in Burg).
    run_event_with_slot(11010520, 0, args=(CHR.Solaire, 1000, 1029, 1005))  # Dead (in Burg).
    run_event_with_slot(11010530, 0, args=(CHR.Solaire, 1000, 1029, 1001))
    # 1004 OFF + 1000 ON + 11010591 ON --> enable only 1001.
    run_event_with_slot(11010531, 0, args=(CHR.Solaire, 1000, 1029, 1007))
    # 1004 OFF + 1008 ON + 11510594 ON --> enable only 1007, move to Sunlight Altar.

    # GRIGGS

    chr.humanity_registration(CHR.Griggs, 8342)
    skip_if_event_flag_range_not_all_off(1, 1110, 1111)  # Griggs is only here if trapped (1110) or just freed (1111).
    chr.disable(CHR.Griggs)
    run_event_with_slot(11010510, 1, args=(CHR.Griggs, 1114))  # Hostile (in Burg).
    run_event_with_slot(11010520, 1, args=(CHR.Griggs, 1110, 1119, 1115))  # Dead (in Burg).
    run_event_with_slot(11010532, 0, args=(CHR.Griggs, 1110, 1119, 1111))  # Freed from house.

    # RHEA

    if DEBUG.RHEA_IN_PARISH:
        flag.disable_chunk(1170, 1189)
        flag.enable(1175)

    chr.humanity_registration(CHR.Rhea, 8358)
    skip_if_event_flag_on(1, 1175)
    chr.disable(CHR.Rhea)
    run_event_with_slot(11010533, 0, args=(CHR.Rhea, 1170, 1189, 1175))
    run_event_with_slot(11010501, 0, args=(CHR.Rhea, 1179))  # Hostile (no resistance).
    run_event_with_slot(11010535, 0, args=(CHR.Rhea, 1170, 1189, 1180))  # Dead.
    # Disable Rhea based on story flags.
    run_event_with_slot(11010534, 0, args=(CHR.Rhea, 1170, 1189, 1181))
    # Petrus kills Rhea.
    run_event_with_slot(11010537, 0, args=(CHR.Rhea, 1170, 1189, 1177))
    # Reset Rhea's 'danger index'.
    run_event(11010538)
    # Enable flag 815 when player picks up Rhea's Pendant ("confirm assassination").
    run_event(11010539)
    # (Old) Disabled old Parish Berenike Knight if Rhea is present.

    # (Old) ANDRE OF ASTORA (moved to Sen's Fortress)

    # UNDEAD MERCHANT

    run_event_with_slot(11010510, 4, args=(CHR.UndeadMerchant, 1401))  # Hostile.
    run_event_with_slot(11010520, 4, args=(CHR.UndeadMerchant, 1400, 1409, 1402))  # Dead.

    # OSWALD OF CARIM

    chr.humanity_registration(CHR.Oswald, 8486)
    skip_if_event_flag_on(1, 11010581)
    chr.disable(CHR.Oswald)
    run_event_with_slot(11010510, 7, args=(CHR.Oswald, 1701))  # Hostile.
    run_event_with_slot(11010520, 7, args=(CHR.Oswald, 1700, 1709, 1702))  # Dead.
    run_event_with_slot(11010581, 0, args=(CHR.Oswald,))  # Watches for bell being rung.
    run_event(11012009)  # Oswald sells Velka's Rapier if you have an active pact with Velka.

    # FEMALE UNDEAD MERCHANT (Firelink flags for Female Undead Merchant)

    # run_event_with_slot(11020504, 8, args=(CHR.FemaleUndeadMerchant, 1411))  # Runs away.
    run_event_with_slot(11010520, 8, args=(CHR.FemaleUndeadMerchant, 1410, 1413, 1412))  # Dead.


def event11010008():
    """ Initialize bonfires and ladders. Now only spawns Turret bonfire if Berenike Knight is dead. """
    header(11010008, 0)
    skip_if_event_flag_on(2, 11012007)  # Berenike Knight dead.
    obj.disable(1011961)
    skip(1)
    map.register_bonfire(11010984, 1011961)

    map.register_bonfire(11010976, 1011962)
    map.register_bonfire(11010960, 1011964)
    for ladder_id, ladder_flag_1, ladder_flag_2 in zip(
            range(1011140, 1011153),
            range(11010010, 11010035, 2),
            range(11010011, 11010036, 2)):
        if ladder_id == 1011149:
            continue  # Skip shortcut ladder.
        map.register_ladder(ladder_flag_1, ladder_flag_2, ladder_id)
    obj.create_damaging_object(11010300, 1011450, 200, 5000, DamageTargetType.character, 1.2, 0.0, 1.0)
    obj.create_damaging_object(11010308, 1011407, 100, 5000, DamageTargetType.character, 0.7, 0.0, 1.0)
    obj.create_damaging_object(11010309, 1011408, 100, 5000, DamageTargetType.character, 0.7, 0.0, 1.0)


def event11010000():
    """ Bell Gargoyles appear for the first time (cutscene), which requires you to possess one of the rust-breaking
    gauntlets. (You only need to have the item with you, not equipped.) """
    header(11010000, 1)
    skip_if_this_event_off(2)
    chr.disable(CHR.BellGargoyleStatue)
    end()

    # Fog now disabled, for host only.
    network.disable_sync()
    obj.disable(1011990)
    sfx.delete_map_sfx(1011991)
    obj.disable(1011992)
    sfx.delete_map_sfx(1011993)
    network.enable_sync()

    chr.disable_ai(CHR.BellGargoyleStatue)
    chr.set_standby_animation_settings(CHR.BellGargoyleStatue, standby_animation=7000)
    chr.enable_invincibility(CHR.BellGargoyleStatue)
    chr.disable_health_bar(CHR.BellGargoyleStatue)
    chr.disable_health_bar(CHR.BellGargoyleTwo)  # New; health bar randomly appears.
    chr.disable(CHR.BellGargoyleOne)
    # Fog entrance flag (5390) no longer required; enabled below.
    if_host(1)
    if_player_inside_region(1, 1012999)
    for gauntlet_id in HeavyGauntlets:
        if_player_has_armor(-1, gauntlet_id)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    skip_if_multiplayer(2)
    cutscene.play_cutscene_to_player(CUTSCENE.BellGargoylesAppear, CutsceneType.skippable, CHR.Player)
    skip(1)
    cutscene.play_cutscene_to_player(CUTSCENE.BellGargoylesAppear, CutsceneType.unskippable, CHR.Player)
    wait_frames(1)
    chr.disable(CHR.BellGargoyleStatue)
    chr.enable(CHR.BellGargoyleOne)
    flag.enable(11015390)
    obj.enable(1011990)
    sfx.create_map_sfx(1011991)
    obj.enable(1011992)
    sfx.create_map_sfx(1011993)


def event11015390():
    """ Bell Gargoyle entrance fog for host; activation now disabled until cutscene triggered. """
    header(11015390, 0)
    if_event_flag_off(1, 3)  # Gargoyles alive
    if_event_flag_on(1, 11010000)  # Gargoyles have appeared (new)
    if_action_button_in_region(1, 1012998, 10010403, line_intersects=1011990, boss_version=True)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1012997)
    anim.force_animation(CHR.Player, 7410)
    restart()


def event11015100():
    """ Solaire summon sign; now doesn't appear until you've fought Gargoyles for the first time. """
    header(11015100, 0)
    skip_if_client(1)
    chr.set_network_update_authority(6540, UpdateAuthority.forced)
    skip_if_this_event_off(1)
    chr.disable(CHR.Solaire)
    skip_if_event_flag_on(3, 11015106)
    if_client(2)
    if_event_flag_on(2, 11015102)
    skip_if_condition_true(1, 2)
    chr.disable(6540)
    end_if_event_flag_on(3)  # Gargoyles dead.
    if_host(1)
    if_character_human(1, CHR.Player)
    for solaire_story_flag in (1004, 1005, 1006, 1010, 1011):
        # These flags prohibit Solaire's appearance.
        if_event_flag_on(-1, solaire_story_flag)
    if_condition_false(1, -1)
    if_entity_backread_enabled(1, 6540)
    if_event_flag_on(1, 11010000)  # New: Gargoyles must have appeared, so he can't help on your first try.
    if_condition_true(0, 1)
    message.place_summon_sign(SummonSignType.blue_eye_sign, 6540, 1012000, 11015102, 11015106)
    chr.disable(CHR.Solaire)


def event11015103():
    """ Lautrec summon sign; doesn't appear until you've fought Gargoyles for the first time. """
    header(11015103, 0)
    skip_if_client(1)
    chr.set_network_update_authority(6590, UpdateAuthority.forced)
    skip_if_event_flag_on(3, 11015107)
    if_client(2)
    if_event_flag_on(2, 11015105)
    skip_if_condition_true(1, 2)
    chr.disable(6590)
    end_if_event_flag_on(3)  # Gargoyles dead.
    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_on(1, 11020607)  # Firelink Shrine flag... not in EMEVD.
    if_event_flag_on(-1, 1572)
    if_event_flag_on(-1, 1573)
    if_condition_true(1, -1)
    if_event_flag_off(1, 1574)
    if_entity_backread_enabled(1, 6590)
    if_entity_within_distance(1, 6590, CHR.Player, 20.0)
    if_event_flag_on(1, 11010000)  # New: Gargoyles must have appeared, so he can't help on your first try.
    if_condition_true(0, 1)
    message.place_summon_sign(SummonSignType.blue_eye_sign, 6590, 1012001, 11015105, 11015107)
    if_event_flag_on(0, 11015105)
    chr.set_special_effect(6590, 5450)


def event11010135():
    """ Thieves in main street kick open doors when played approaches if (a) the Capra Demon fight has been going
    long enough, or (b) if the Capra Demon is already gone on event load.
    """
    door_entity_id, thief_entity_id, area_entity_id, delay = define_args('iiif')

    header(11010135, 1)
    skip_if_this_event_slot_off(2)
    anim.end_animation(door_entity_id, 2)
    end()

    chr.disable_ai(thief_entity_id)
    skip_if_event_flag_on(3, EVENT.CapraDemonTransformed)
    if_event_flag_on(0, 11015372)
    wait(delay)
    if_player_inside_region(0, area_entity_id)
    wait_random_seconds(0.0, 1.0)
    anim.force_animation(thief_entity_id, 7001)
    chr.enable_ai(thief_entity_id)
    wait(0.1)
    anim.force_animation(door_entity_id, 2)


def event11010791():
    """ Hellkite first swoop over the bridge. Now triggered in the Taurus Demon battle as well as closer. """
    header(11010791, 0)
    end_if_this_event_on()
    if_event_flag_off(1, 11015310)  # Fire breath attack is not currently underway.
    if_event_flag_off(1, 11010782)  # Hellkite has not already flown away in this map load.
    if_entity_health_greater_than_or_equal(1, CHR.Hellkite, 0.1)
    if_player_inside_region(-1, 1012305)  # This region has moved to Taurus Demon arena.
    if_player_inside_region(-1, 1012332)  # First half of bridge.
    if_player_inside_region(-1, 1012330)  # Middle of bridge (in case you come up from below).
    if_condition_true(1, -1)
    if_all_players_outside_region(1, 1012337)  # Not sure where this is. Possibly the Altar bonfire.
    if_character_type(2, CHR.Player, CharacterType.black_phantom)
    if_condition_false(1, 2)  # Player is NOT a black ghost.
    if_condition_true(0, 1)
    flag.enable(11015310)  # Fire breath attack is underway.
    flag.enable(11010790)  # First encounter in Burg won't happen if it hasn't already.
    flag.enable(11010791)  # This initial swoop is done.
    flag.enable(11010780)  # Spire has broken (happens on first-ever swoop).
    chr.enable(CHR.Hellkite)
    warp.short_warp(CHR.Hellkite, 'region', 1012302, -1)  # Start of initial swoop (far away).
    chr.set_standby_animation_settings(CHR.Hellkite, standby_animation=7006)
    anim.force_animation(CHR.Hellkite, 7005)  # Initial swoop attack.
    wait_frames(395)
    warp.short_warp(CHR.Hellkite, 'region', 1012310, -1)  # Perch.
    flag.disable(11015310)  # Fire breath attack has ended.


def event11015302():
    """ Hellkite fire breath trigger. Now more aggressive to block progress from Taurus Demon. """
    header(11015302, 0)
    if_host(-7)
    if_character_type(-7, CHR.Player, CharacterType.white_phantom)
    if_condition_true(1, -7)
    if_event_flag_off(1, 11015310)
    if_event_flag_on(1, 11010791)
    if_event_flag_off(1, 11015311)
    if_entity_health_greater_than_or_equal(1, CHR.Hellkite, 0.1)
    if_condition_true(2, 1)
    if_condition_true(3, 1)
    if_condition_true(4, 1)
    if_condition_true(5, 1)
    if_condition_true(6, 1)
    if_condition_true(7, 1)
    if_event_flag_off(2, EVENT.CapraDemonTransformed)
    if_player_inside_region(2, 1012330)  # -> 5350   # removed ladder kicking requirement for this
    if_player_inside_region(3, 1012331)  # -> 5351
    if_event_flag_off(4, EVENT.CapraDemonTransformed)
    if_player_inside_region(4, 1012332)  # -> 5352   # removed ladder kicking requirement for this
    if_player_inside_region(5, 1012333)  # -> 5353
    if_event_flag_on(6, 11015305)  # -> 5354 (jump down due to frustration timer)
    if_event_flag_on(7, 11015317)  # -> 5354 (jump down due to being attacked)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(-1, 4)
    if_condition_true(-1, 5)
    if_condition_true(-1, 6)
    if_condition_true(-1, 7)
    if_condition_true(0, -1)

    flag.enable(11015310)
    skip_if_condition_false_finished(1, 2)
    flag.enable(11015350)
    skip_if_condition_false_finished(1, 3)
    flag.enable(11015351)
    skip_if_condition_false_finished(1, 4)
    flag.enable(11015352)
    skip_if_condition_false_finished(1, 5)
    flag.enable(11015353)
    skip_if_condition_true_finished(2, 6)
    skip_if_condition_true_finished(1, 7)
    skip(1)
    flag.enable(11015354)
    flag.disable_chunk(11015320, 11015339)
    skip_if_client(2)
    flag.enable_random_in_chunk(11015320, 11015339)
    flag.enable(11015313)
    restart()


def event11010899():
    """ Main Hellkite initialization. Controls swoop attack odds. """
    header(11010899, 0)
    chr.enable_immortality(CHR.Hellkite)
    chr.disable(CHR.Hellkite)
    chr.set_nest(CHR.Hellkite, 1012320)
    skip_if_client(2)
    chr.set_network_update_authority(CHR.Hellkite, UpdateAuthority.forced)
    flag.disable(11010782)  # Hellkite has not flown away in this load.

    # If Hellkite has swooped the bridge and is NOT down on it, move it to the perch.
    if_event_flag_on(1, 11010791)  # Hellkite has swooped the bridge.
    if_event_flag_off(1, 11015311)  # Hellkite is NOT down on the bridge.
    skip_if_condition_false(6, 1)
    flag.disable(11015310)  # Hellkite is not swooping.
    chr.enable(CHR.Hellkite)
    warp.warp_and_set_floor(CHR.Hellkite, 'region', 1012310, -1, 1013211)  # Move to perch.
    chr.set_standby_animation_settings(CHR.Hellkite, standby_animation=7006)  # Perch resting anim.
    chr.disable_collision(CHR.Hellkite)
    chr.disable_gravity(CHR.Hellkite)

    # If Hellkite has swooped the bridge and is down on it, move it to the bridge.
    if_event_flag_on(2, 11010791)
    if_event_flag_on(2, 11015311)
    skip_if_condition_false(4, 2)
    chr.enable(CHR.Hellkite)
    warp.short_warp(CHR.Hellkite, 'region', 1012320, -1)
    chr.set_standby_animation_settings_to_default(CHR.Hellkite)
    chr.set_nest(CHR.Hellkite, 1012340)  # Not sure where this nest is.

    # Swoop attack events.
    for slot, (first_flag, last_flag, attack_id, area_id) in enumerate((
            # Triggered by middle of bridge.
            (11015320, 11015325, 7004, 11015350),  # 6/20 chance
            (11015326, 11015331, 7008, 11015350),  # 6/20 chance
            (11015332, 11015333, 7009, 11015350),  # 2/20 chance
            (11015334, 11015337, 7011, 11015350),  # 4/20 chance
            (11015338, 11015339, 7006, 11015350),  # 2/20 chance (no attack)

            # Triggered by being inside the Altar. Not sure when this triggers an attack rather than leaving.
            (11015320, 11015323, 7009, 11015351),  # 4/20 chance
            (11015324, 11015339, 7006, 11015351),  # 16/20 chance (no attack)

            # Triggered by first half of bridge. Now attacks more frequently.
            (11015320, 11015333, 7011, 11015352),  # 14/20 chance
            (11015334, 11015339, 7006, 11015352),  # 6/20 chance (no attack)

            # Triggered by being at the end of the bridge (close to the Hellkite).
            (11015320, 11015321, 7004, 11015353),  # 2/20 chance
            (11015322, 11015333, 7008, 11015353),  # 12/20 chance
            (11015334, 11015335, 7009, 11015353),  # 2/20 chance
            (11015336, 11015337, 7011, 11015353))):  # 2/20 chance (remaining 2/20 causes it to land)
        run_event_with_slot(11010805, slot, args=(first_flag, last_flag, attack_id, area_id))

    # Landing attack events.
    for slot, (first_flag, last_flag, attack_id, area_id) in enumerate((
            (11015338, 11015339, 7010, 11015353),  # 2/20 chance of landing if you get close
            (11015320, 11015339, 7010, 11015354))):  # 20/20 chance of landing when frustrated or attacked
        run_event_with_slot(11010800, slot, args=(first_flag, last_flag, attack_id, area_id))


def event11015382():
    """ Taurus Demon activation (changed). """
    header(11015382, 1)
    end_if_this_event_on()
    chr.disable_ai(CHR.TaurusDemon)
    chr.disable_health_bar(CHR.TaurusDemon)
    if_player_within_distance(1, CHR.TaurusDemon, 6.0)
    if_host(2)
    if_player_inside_region(2, 1012701)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    flag.enable(11010005)  # no idea what this does, no reference in EMEVD
    skip_if_condition_true(1, 1)
    anim.force_animation(CHR.TaurusDemon, 9060, wait_for_completion=True)
    chr.enable_ai(CHR.TaurusDemon)


def event11015370():
    """ Capra Demon fog. """
    header(11015370, 0)
    if_event_flag_off(1, 11012000)
    if_event_flag_on(1, 11012001)
    if_action_button_state_and_line_segment_in_boss(
        1, 'region', 1012888, 0.0, -1, 0.0, 10010403, ReactionAttribute.human_or_hollow, 0, 1011790)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1012887)
    anim.force_animation(CHR.Player, 7410, wait_for_completion=True)
    restart()


def event11015371():
    """ Capra Demon fog (summon). """
    header(11015371, 0)
    if_event_flag_off(1, 11012000)
    if_event_flag_on(1, 11012001)
    if_event_flag_on(1, 11015373)
    if_character_type(1, CHR.Player, CharacterType.white_phantom)
    if_action_button_state_and_line_segment(
        1, 'region', 1012888, 0.0, -1, 0.0, 10010403, ReactionAttribute.human_or_hollow, 0, 1011790)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1012887)
    anim.force_animation(CHR.Player, 7410, wait_for_completion=True)
    restart()


def event11015373():
    """ Capra Demon boss trigger. """
    header(11015373, 0)
    skip_if_this_event_on(3)

    # First time trigger:
    if_client(-7)
    if_event_flag_on(-7, 11012001)
    skip_if_condition_true(16, -7)
    network.disable_sync()
    obj.disable(1011790)
    sfx.delete_map_sfx(1011791, False)
    sfx.delete_map_sfx(1011771, False)
    sfx.delete_map_sfx(1011772, False)
    sfx.delete_map_sfx(1011799, False)  # extra fog above
    if_player_inside_region(1, 1012881)  # Region at corner in middle of street.
    if_condition_true(0, 1)
    wait(0.5)
    obj.enable(1011790)
    sfx.create_map_sfx(1011791)
    sfx.create_map_sfx(1011771)
    sfx.create_map_sfx(1011772)
    sfx.create_map_sfx(1011799)
    flag.enable(11012001)  # first encounter done
    skip(3)

    # All other times:
    if_event_flag_off(1, 11012000)
    if_player_inside_region(1, 1012886)  # Region at fog entrance.
    if_condition_true(0, 1)

    network.enable_sync()
    skip_if_client(1)
    network.notify_boss_room_entry()
    chr.activate_npc_buffs(CHR.CapraDemon)
    flag.enable(11010597)


def event11015374():
    """ Start Capra Demon music. """
    header(11015374, 0)
    network.disable_sync()
    if_event_flag_off(1, 11012000)
    if_event_flag_on(1, 11015372)
    skip_if_host(1)
    if_event_flag_on(1, 11015371)
    if_player_inside_region(1, 1012880)
    if_condition_true(0, 1)
    sound.enable_map_sound(1013803)


def event11015375():
    """ Stop Capra Demon music. """
    header(11015375, 0)
    network.disable_sync()
    if_event_flag_on(1, 11015374)
    if_event_flag_on(1, 11012000)
    if_condition_true(0, 1)
    sound.disable_map_sound(1013803)


def event11012000():
    """ Capra Demon transforms into Capricious Thrall (one-off). It then waits until the Thrall disappears. """
    header(11012000, 0)
    chr.disable(CHR.CapriciousThrall)
    # If encounter is done:
    skip_if_this_event_off(4)
    chr.disable(CHR.CapraDemon)
    chr.kill(CHR.CapraDemon, False)
    flag.enable(EVENT.CapriciousThrallStableFooting)
    end()

    # If encounter is not done:
    # Disable street dog and dog in house of first thief to emerge.
    chr.disable(1010753)
    chr.disable(1010754)
    # Trigger Thrall appearance when Capra Demon gets below 25% health.
    if_entity_health_less_than_or_equal(0, CHR.CapraDemon, 0.25)
    chr.enable_invincibility(CHR.CapraDemon)
    chr.enable_invincibility(CHR.CapriciousThrall)
    chr.disable_health_bar(CHR.CapraDemon)
    chr.disable_health_bar(CHR.CapriciousThrall)
    sound.disable_map_sound(1013803)
    boss.disable_boss_health_bar(CHR.CapraDemon, TEXT.CapraDemonName)
    warp.warp_and_copy_floor(CHR.CapriciousThrall, 'character', CHR.CapraDemon, 2, CHR.CapraDemon)
    chr.disable(CHR.CapraDemon)
    chr.enable(CHR.CapriciousThrall)
    anim.force_animation(CHR.CapriciousThrall, 2083)  # stagger
    wait(2)
    anim.force_animation(CHR.CapriciousThrall, 2082)  # stagger
    wait(2)
    flag.enable(11012000)  # Thrall will be gone next time. Also makes Capra music stop.
    sound.enable_map_sound(1013804)
    boss.enable_boss_health_bar(CHR.CapriciousThrall, TEXT.CapriciousThrallName)
    anim.force_animation(CHR.CapriciousThrall, ANIM.ThrallTransformation, wait_for_completion=True)
    chr.disable_invincibility(CHR.CapriciousThrall)
    flag.enable(EVENT.CapriciousThrallActive)  # First story flag for Thrall.

    # Start battle timer.
    wait(100)

    # Thrall vanishes.
    end_if_event_flag_on(11010902)  # clean-up done already in the death event if Thrall died
    chr.enable_invincibility(CHR.CapriciousThrall)
    boss.disable_boss_health_bar(CHR.CapriciousThrall, TEXT.CapriciousThrallName)
    sound.play_sound_effect(CHR.CapriciousThrall, SoundType.s_sfx, 777777777)  # For effect.
    wait(2)  # so sound effect can build up and slightly mask the abrupt music stop
    anim.force_animation(CHR.CapriciousThrall, ANIM.ThrallRetreat)
    wait(1.4)
    chr.disable(CHR.CapriciousThrall)
    sound.disable_map_sound(1013804)
    obj.disable(1011790)
    sfx.delete_map_sfx(1011791)
    sfx.delete_map_sfx(1011771)
    sfx.delete_map_sfx(1011772)
    obj.disable(1011797)
    sfx.delete_map_sfx(1011798)
    sfx.delete_map_sfx(1011799)  # extra fog above entrance
    flag.enable(EVENT.CapriciousThrallStableFooting)
    message.status_explanation(TEXT.ThrallHasFled)
    flag.enable(11012017)  # Message won't appear when you come back.


def event11010902():
    """ Capricious Thrall death. Only gets one chance to fire - during the one-off encounter. """
    header(11010902, 0)

    # Doesn't start checking for Thrall health until it's appeared. (but why?)
    if_event_flag_on(0, 11012000)
    if_entity_health_less_than_or_equal(0, CHR.CapriciousThrall, 0.0)
    wait(1)
    sound.play_sound_effect(CHR.CapriciousThrall, SoundType.s_sfx, 777777777)
    if_entity_dead(0, CHR.CapriciousThrall)

    flag.disable(EVENT.CapriciousThrallActive)
    flag.disable(EVENT.CapriciousThrallTrapped)
    flag.enable(EVENT.CapriciousThrallDead)
    boss.kill_boss(CHR.CapriciousThrall)
    sound.disable_map_sound(1013804)
    obj.disable(1011790)
    sfx.delete_map_sfx(1011791)
    sfx.delete_map_sfx(1011771)
    sfx.delete_map_sfx(1011772)
    obj.disable(1011797)
    sfx.delete_map_sfx(1011798)
    sfx.delete_map_sfx(1011799)  # extra fog above entrance
    flag.enable(EVENT.CapriciousThrallStableFooting)


def event11015360():
    """ Host enters Haunting Semblance fog (either side). """
    header(11015360, 0)
    if_event_flag_off(1, EVENT.HauntingSemblanceDead)
    if_action_button_state_and_line_segment_in_boss(
        1, 'region', 1012878, 180.0, -1, 0.0, 10010403, ReactionAttribute.human_or_hollow, 0, 1011792)
    if_event_flag_off(2, EVENT.HauntingSemblanceDead)
    if_action_button_state_and_line_segment_in_boss(
        2, 'region', 1012879, 180.0, -1, 0.0, 10010403, ReactionAttribute.human_or_hollow, 0, 1011795)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    chr.rotate_to_face_entity(CHR.Player, 1012877)
    anim.force_animation(CHR.Player, 7410, wait_for_completion=True)
    restart()


def event11015361():
    """ Client enters Haunting Semblance fog (either side). """
    header(11015361, 0)
    if_event_flag_off(1, EVENT.HauntingSemblanceDead)
    if_event_flag_on(1, 11015363)
    if_character_type(1, CHR.Player, CharacterType.white_phantom)
    if_action_button_state_and_line_segment_in_boss(
        1, 'region', 1012878, 180.0, -1, 0.0, 10010403, ReactionAttribute.human_or_hollow, 0, 1011792)
    if_event_flag_off(2, EVENT.HauntingSemblanceDead)
    if_event_flag_on(2, 11015363)
    if_character_type(2, CHR.Player, CharacterType.white_phantom)
    if_action_button_state_and_line_segment_in_boss(
        2, 'region', 1012879, 180.0, -1, 0.0, 10010403, ReactionAttribute.human_or_hollow, 0, 1011795)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    chr.rotate_to_face_entity(CHR.Player, 1012877)
    anim.force_animation(CHR.Player, 7410, wait_for_completion=True)
    restart()


def event11015363():
    """ Notify Haunting Semblance boss battle start. """
    header(11015363, 0)
    skip_if_this_event_on(3)
    if_event_flag_off(1, EVENT.HauntingSemblanceDead)
    if_player_inside_region(1, 1012870)
    if_condition_true(0, 1)
    skip_if_client(1)
    network.notify_boss_room_entry()
    chr.activate_npc_buffs(CHR.HauntingSemblance)


def event11015362():
    """ Activate Haunting Semblance (when player approaches). """
    header(11015362, 1)
    chr.disable(CHR.ProfaneImage)
    end_if_event_flag_on(EVENT.HauntingSemblanceDead)

    skip_if_this_event_on(6)
    chr.disable_ai(CHR.HauntingSemblance)
    if_event_flag_on(1, 11015363)
    if_player_inside_region(-1, REGION.HauntingSemblanceTrigger)
    if_entity_attacked_by(-1, CHR.HauntingSemblance, CHR.Player)
    if_condition_true(1, -1)
    if_condition_true(0, 1)

    chr.enable_ai(CHR.HauntingSemblance)
    boss.enable_boss_health_bar_with_slot(CHR.HauntingSemblance, 0, TEXT.HauntingSemblance)


def event11015364():
    """ Start Haunting Semblance music. """
    header(11015364, 0)
    network.disable_sync()
    if_event_flag_off(1, EVENT.HauntingSemblanceDead)
    if_event_flag_on(1, 11015362)
    skip_if_host(1)
    if_event_flag_on(1, 11015361)
    if_condition_true(0, 1)
    sound.enable_map_sound(1013805)


def event11015365():
    """ Stop Haunting Semblance music when boss dies. """
    header(11015365, 0)
    network.disable_sync()
    if_event_flag_on(1, 11015364)
    if_event_flag_on(1, EVENT.HauntingSemblanceDead)
    if_condition_true(0, 1)
    sound.disable_map_sound(1013805)


def event11010904():
    """ Haunting Semblance dies. """
    header(11010904, 1)
    skip_if_this_event_off(4)
    chr.disable(CHR.HauntingSemblance)
    chr.disable(CHR.ProfaneImage)
    chr.kill(CHR.HauntingSemblance, False)
    end()
    if_entity_health_less_than_or_equal(0, CHR.ProfaneImage, 0.0)
    chr.kill(CHR.HauntingSemblance, False)
    wait(1)
    sound.play_sound_effect(CHR.HauntingSemblance, SoundType.s_sfx, 777777777)
    if_entity_dead(0, CHR.HauntingSemblance)
    flag.enable(11010904)
    boss.kill_boss(CHR.HauntingSemblance)
    boss.disable_boss_health_bar(CHR.HauntingSemblance, TEXT.HauntingSemblance)  # Needed to disable both health bars.
    obj.disable(1011792)
    sfx.delete_map_sfx(1011793)
    sfx.delete_map_sfx(1011794)  # this tall fog has two SFX parts
    obj.disable(1011795)
    sfx.delete_map_sfx(1011796)


def event11012002():
    """ Award achievement after Nito awakening cutscene. """
    header(11012002, 0)
    if_event_flag_on(0, EVENT.ParishNitoCutsceneWarp)
    flag.disable(EVENT.ParishNitoCutsceneWarp)
    network.save_request()
    wait(2.0)
    game.award_achievement(29)


def event11010700():
    """ Ring Bell of Awakening, and play Nito cutscene if this is the second bell. """
    header(11010700, 0)
    skip_if_this_event_off(2)
    obj.disable_activation(1011110, -1)
    end()

    if_object_activated(0, 11010700)
    network.trigger_multiplayer_event(10010)
    if_entity_health_greater_than(0, CHR.Player, 0.0)
    flag.enable(11010700)
    cutscene.play_cutscene_to_player(100100, CutsceneType.skippable, CHR.Player)
    wait_frames(1)

    # If Blighttown bell not rung, just award achievement.
    skip_if_event_flag_on(2, EVENT.BlighttownBellRung)
    game.award_achievement(29)
    end()

    # Otherwise, if Nito dead, display 'Nothing happened' and award achievement.
    skip_if_event_flag_off(3, EVENT.NitoDead)
    message.dialog(TEXT.NothingHappened, ButtonType.ok_cancel, NumberButtons.no_button, CHR.Player, 5.0)
    game.award_achievement(29)
    end()

    # Otherwise, warp to Tomb for Nito awakening cutscene. (Achievement awarded on return.)
    flag.enable(EVENT.NitoAwake)
    flag.enable(EVENT.ParishNitoCutsceneWarp)
    warp.warp_player(13, 1, 1310990)


def event11012005():
    """ Black Knight Greatsword only appears on the Watchtower if you if you have the Ring of Ash. """
    header(11012005, 1)
    chr.disable(CHR.BlackKnightGreatsword)
    skip_if_this_event_off(2)
    chr.kill(CHR.BlackKnightGreatsword, False)
    end()
    if_player_has_ring(0, RING.RingOfAsh)
    chr.enable(CHR.BlackKnightGreatsword)
    if_entity_dead(0, CHR.BlackKnightGreatsword)
    flag.enable(EVENT.BlackKnightGreatswordDead)
    item.award_item_to_host_only(27901000)  # BKGS, White Chunk
    for flag_id in (EVENT.BlackKnightSwordDead, EVENT.BlackKnightGreatswordDead,
                    EVENT.BlackKnightHalberdDead, EVENT.BlackKnightAxeDead):
        if_event_flag_on(1, flag_id)
    skip_if_condition_true(2, 1)
    message.status_explanation(TEXT.RingOfAshWarms, pad_enabled=True)
    end()
    flag.enable(EVENT.AllBlackKnightsDead)
    message.status_explanation(TEXT.RingOfAshHot, pad_enabled=True)


def event11012006():
    """ (Now always enabled.)  """
    header(11012006, 0)
    end()
    # end_if_this_event_on()
    # if_player_inside_region(0, REGION.BellCheck)
    # flag.enable(11012006)


def event11010581():
    """ Oswald now appears when you just approach the bell lever, without needing to pull it. """
    header(11010581, 0)
    end_if_this_event_on()
    if_event_flag_on(-1, 11012006)
    if_event_flag_on(-1, 11010700)
    if_condition_true(0, -1)
    chr.enable(CHR.Oswald)


def event11012007():
    """ Kill Berenike Knight on top of turret and spawn bonfire. """
    header(11012007, 1)
    skip_if_this_event_off(2)
    chr.disable(CHR.BonfireBerenikeKnight)
    end()
    if_entity_health_less_than_or_equal(0, CHR.BonfireBerenikeKnight, 0.0)
    flag.enable(11012007)
    sfx.create_oneoff_sfx('object', 1011961, -1, 90014)
    wait(2.0)
    obj.enable(1011961)
    map.register_bonfire(11010984, 1011961)


def event11012008():
    """ Darkwraiths take over the Parish. """
    header(11012008, 1)

    DARKWRAITHS = (1010875, 1010876, 1010877)
    PARISH_CHANNELERS = (1010370, 1010371)
    PARISH_HOLLOWS = range(1010675, 1010685)

    # Disable Darkwraiths before Dark Anor Londo.
    skip_if_event_flag_on(len(DARKWRAITHS) + 1, EVENT.DarkAnorLondo)
    for darkwraith in DARKWRAITHS:
        chr.disable(darkwraith)
    end()

    # Otherwise, disable Channelers and power up Parish hollows.
    for channeler in PARISH_CHANNELERS:
        chr.disable(channeler)
    for hollow in PARISH_HOLLOWS:
        chr.set_special_effect(hollow, 4957)  # +10% speed
        chr.set_special_effect(hollow, 7010)  # level 10 (~2x HP and damage)


def event11015366():
    """ Profane Image emerges when (and then whenever) Haunting Semblance reaches 60% health. """
    header(11015366)

    end_if_event_flag_on(EVENT.HauntingSemblanceDead)

    chr.disable_health_bar(CHR.ProfaneImage)

    if_event_flag_on(1, 11015362)
    if_entity_health_less_than_or_equal(1, CHR.HauntingSemblance, 0.6)
    if_condition_true(0, 1)

    warp.warp_and_copy_floor(CHR.ProfaneImage, 'character', CHR.HauntingSemblance, 4, CHR.HauntingSemblance)

    chr.enable_invincibility(CHR.HauntingSemblance)
    chr.set_ai_id(CHR.HauntingSemblance, 1)
    chr.replan_ai(CHR.HauntingSemblance)
    chr.disable_gravity(CHR.ProfaneImage)
    chr.disable_collision(CHR.ProfaneImage)
    flag.enable(11015368)  # Image is active.

    flag.disable_chunk(11015350, 11015353)
    flag.enable_random_in_chunk(11015350, 11015353)
    anim.force_animation(CHR.HauntingSemblance, 2010)
    wait(0.5)
    chr.enable(CHR.ProfaneImage)
    anim.force_animation(CHR.ProfaneImage, 2015, wait_for_completion=True)
    chr.disable(CHR.ProfaneImage)
    skip_if_event_flag_off(1, 11015350)
    warp.short_warp(CHR.ProfaneImage, 'region', 1012681, -1)
    skip_if_event_flag_off(1, 11015351)
    warp.short_warp(CHR.ProfaneImage, 'region', 1012682, -1)
    skip_if_event_flag_off(1, 11015352)
    warp.short_warp(CHR.ProfaneImage, 'region', 1012683, -1)
    skip_if_event_flag_off(1, 11015353)
    warp.short_warp(CHR.ProfaneImage, 'region', 1012684, -1)
    chr.enable(CHR.ProfaneImage)
    anim.force_animation(CHR.ProfaneImage, 3010)  # fade-in attack
    boss.disable_boss_health_bar(CHR.HauntingSemblance, TEXT.HauntingSemblance)
    boss.enable_boss_health_bar(CHR.ProfaneImage, TEXT.ProfaneImage)
    chr.disable_health_bar(CHR.HauntingSemblance)
    run_event(11015367)

    wait_random_seconds(60, 80)

    end_if_event_flag_on(EVENT.HauntingSemblanceDead)

    flag.disable(11015368)  # Image is inactive.
    anim.force_animation(CHR.ProfaneImage, 2015, wait_for_completion=True)
    chr.disable(CHR.ProfaneImage)
    chr.set_special_effect(CHR.HauntingSemblance, 3231)  # Heal Haunting Semblance.
    boss.disable_boss_health_bar(CHR.ProfaneImage, TEXT.ProfaneImage)
    boss.enable_boss_health_bar(CHR.HauntingSemblance, TEXT.HauntingSemblance)
    wait_frames(2)  # Give health time to refill.
    chr.set_ai_id(CHR.HauntingSemblance, 230003)
    chr.replan_ai(CHR.HauntingSemblance)
    chr.disable_invincibility(CHR.HauntingSemblance)
    restart()


def event11015367():
    """ Profane Image warps around. """
    header(11015367)
    if_player_within_distance(0, CHR.ProfaneImage, 4.0)
    flag.disable_chunk(11015354, 11015357)
    flag.enable_random_in_chunk(11015354, 11015357)
    if_event_flag_on(1, 11015350)
    if_event_flag_on(1, 11015354)
    if_event_flag_on(2, 11015351)
    if_event_flag_on(2, 11015355)
    if_event_flag_on(3, 11015352)
    if_event_flag_on(3, 11015356)
    if_event_flag_on(4, 11015353)
    if_event_flag_on(4, 11015357)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(-1, 4)
    skip_if_condition_false(1, -1)
    restart()

    wait_random_seconds(10, 30)

    end_if_event_flag_off(11015368)  # Profane Image has disappeared already.
    anim.force_animation(CHR.ProfaneImage, 6)  # Fade out and in.
    wait(1.0)
    flag.disable_chunk(11015350, 11015353)
    skip_if_event_flag_off(2, 11015354)
    warp.short_warp(CHR.ProfaneImage, 'region', 1012681, -1)
    flag.enable(11015350)
    skip_if_event_flag_off(2, 11015355)
    warp.short_warp(CHR.ProfaneImage, 'region', 1012682, -1)
    flag.enable(11015351)
    skip_if_event_flag_off(2, 11015356)
    warp.short_warp(CHR.ProfaneImage, 'region', 1012683, -1)
    flag.enable(11015352)
    skip_if_event_flag_off(2, 11015357)
    warp.short_warp(CHR.ProfaneImage, 'region', 1012684, -1)
    flag.enable(11015353)

    chr.rotate_to_face_entity(CHR.ProfaneImage, CHR.Player)

    restart()


def event11010150():
    """ One-way door access effect applied. """
    header(11010150)
    door_open_flag, right_side, wrong_side = define_args('iii')
    network.disable_sync()
    skip_if_event_flag_on(4, door_open_flag)
    if_player_inside_region(0, right_side)
    chr.set_special_effect(CHR.Player, 4150)
    wait(3.0)
    restart()

    if_player_inside_region(-1, right_side)
    if_player_inside_region(-1, wrong_side)
    if_condition_true(0, -1)
    chr.set_special_effect(CHR.Player, 4150)
    wait(3.0)
    restart()


def event11010140():
    """ Basic locked door with Master Key use. Can be closed again after opening. """
    header(11010140)
    objact_id, key_message, door_id, master_key_message, key_id = define_args('iiiii')
    end_if_this_event_slot_on()
    if_host(1)
    if_object_activated(1, objact_id)
    if_condition_true(0, 1)
    if_player_has_good(2, key_id)  # Overrides Master Key.
    skip_if_condition_true(3, 2)
    message.dialog(master_key_message, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)
    item.remove_items_from_player(ItemType.good, GOOD.MasterKey, 0)  # Break Master Key.
    end()
    message.dialog(key_message, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)


def event11010165():
    """ Basic locked door with Master Key use. CANNOT be closed again after opening. """
    header(11010165)
    objact_id, key_message, door_id, master_key_message, key_id = define_args('iiiii')

    skip_if_this_event_slot_off(6)
    anim.end_animation(door_id, 1)
    for idx in range(4):
        obj.deactivate_object_with_idx(door_id, -1, idx)
    end()

    if_host(1)
    if_object_activated(1, objact_id)
    if_condition_true(0, 1)
    if_player_has_good(2, key_id)  # Overrides Master Key.
    skip_if_condition_true(3, 2)
    message.dialog(master_key_message, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)
    item.remove_items_from_player(ItemType.good, GOOD.MasterKey, 0)  # Break Master Key.
    end()
    message.dialog(key_message, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)


def event11010180():
    """ Residence doors. Can't be closed after opening. """
    header(11010180)
    objact_id, key_message, door_id, master_key_message, key_id = define_args('iiiii')
    skip_if_this_event_slot_off(6)
    anim.end_animation(door_id, 0)  # Re-open door. Technically I should enable the 6... flag, but it won't matter.
    for idx in range(4):
        obj.deactivate_object_with_idx(door_id, -1, idx)
    end()

    if_host(1)
    if_object_activated(1, objact_id)
    if_condition_true(0, 1)
    flag.enable(objact_id)
    end_if_client()
    if_player_has_good(2, key_id)  # Overrides Master Key.
    skip_if_condition_true(3, 2)
    message.dialog(master_key_message, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)
    item.remove_items_from_player(ItemType.good, GOOD.MasterKey, 0)  # Break Master Key.
    skip(1)
    message.dialog(key_message, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)

    network.disable_sync()
    wait(2.0)
    for idx in range(4):
        obj.deactivate_object_with_idx(door_id, -1, idx)


def event11015130():
    """ Crystal Lizard disappears. """
    header(11015130, 1)
    chr.disable(1010400)
    end_if_event_flag_on(11010710)
    if_object_destroyed(0, 1011000)
    chr.enable(1010400)
    skip_if_this_event_on(4)
    anim.force_animation(1010400, 500, wait_for_completion=True)
    anim.force_animation(1010400, 500, wait_for_completion=True)
    anim.force_animation(1010400, 500, wait_for_completion=True)
    anim.force_animation(1010400, 500, wait_for_completion=True)
    end()


def event11015630():
    """ New NPC invasion: Depraved Apostate. """
    header(11015630)
    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11015631)
    end_if_event_flag_on(1198)  # Petrus dies (before killing Rhea).
    end_if_event_flag_on(1196)  # Petrus dies (after killing Rhea).
    # No longer requires Bell Gargoyles to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 11010810)
    if_event_flag_off(1, 1198)  # Re-checked because m10_01 may have loaded before you killed Petrus in the graveyard.
    if_event_flag_off(1, 1196)
    skip_if_this_event_on(1)
    if_player_inside_region(1, REGION.DepravedApostateTrigger)
    if_condition_true(0, 1)
    message.place_summon_sign(SummonSignType.black_eye_sign, 6850, REGION.DepravedApostateSignPoint, 11015631, 11015632)
    wait(20.0)
    restart()


def event11010810():
    """ Depraved Apostate invader dies. """
    header(11010810)
    skip_if_host(3)
    if_event_flag_on(1, 11015031)
    if_event_flag_off(1, 11015032)
    skip_if_condition_true(1, 1)
    chr.disable(CHR.DepravedApostate)
    end_if_this_event_on()
    if_entity_dead(0, CHR.DepravedApostate)
    flag.enable(11010810)


def event11012020():
    """ Lithic Bond statue interaction. """
    header(11012020)

    if_action_button_state(0, Category.character, CHR.SenLithicStatue, 180.0, -1, 2.0, TEXT.ExamineStatue)

    if_event_flag_on(1, EVENT.LithicWitness)
    if_event_flag_off(1, EVENT.LithicBondObtained)
    skip_if_condition_true(2, 1)
    message.dialog(TEXT.LithicStatue, ButtonType.ok_cancel, NumberButtons.no_button, CHR.SenLithicStatue, 4.0)
    skip(1)
    item.award_item_to_host_only(ITEMLOT.LithicBond)

    wait(3.0)
    restart()


def event11012021():
    """ Empyrean Bond statue interaction. """
    header(11012021)

    if_action_button_state(0, Category.character, CHR.SenEmpyreanStatue, 180.0, -1, 3.0, TEXT.ExamineStatue)

    if_event_flag_on(1, EVENT.EmpyreanWitness)
    if_event_flag_off(1, EVENT.EmpyreanBondObtained)
    skip_if_condition_true(2, 1)
    message.dialog(TEXT.EmpyreanStatue, ButtonType.ok_cancel, NumberButtons.no_button, CHR.SenEmpyreanStatue, 4.0)
    skip(1)
    item.award_item_to_host_only(ITEMLOT.EmpyreanBond)

    wait(3.0)
    restart()


def event11015250():
    """ Hanging Hollows climb up. Now disables gravity as well. """
    header(11015250, 1)
    enemy, trigger_entity, trigger_distance, delay = define_args('iiff')

    skip_if_this_event_slot_off(2)
    chr.set_standby_animation_settings_to_default(enemy)
    end()

    chr.disable_gravity(enemy)
    chr.disable_collision(enemy)

    if_player_within_distance(0, trigger_entity, trigger_distance)
    network.disable_sync()
    wait(delay)
    chr.enable_collision(enemy)
    chr.enable_gravity(enemy)
    chr.set_standby_animation_settings(enemy, cancel_animation=9060)


def event11015492():
    """ Horned Scourge appears (or is disabled). """
    header(11015492, 1)

    chr.disable(CHR.HornedScourge)

    if_event_flag_on(1, EVENT.TaurusDemonDead)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_off(1, EVENT.HornedScourgeDead)
    end_if_condition_false(1)

    if_player_inside_region(0, REGION.HornedScourgeTrigger)

    obj.enable(1011890)
    sfx.create_map_sfx(1011891)
    obj.enable(1011892)
    sfx.create_map_sfx(1011893)

    for killplane in range(1013200, 1013205):
        hitbox.disable_hitbox(killplane)

    chr.disable_gravity(CHR.HornedScourge)
    chr.disable_collision(CHR.HornedScourge)
    chr.enable_invincibility(CHR.HornedScourge)
    chr.enable_immortality(CHR.HornedScourge)
    wait_frames(5)
    chr.enable(CHR.HornedScourge)
    anim.force_animation(CHR.HornedScourge, 3009)
    wait(7.0)
    chr.set_nest(CHR.HornedScourge, REGION.HornedScourgeTrigger)
    chr.disable_immortality(CHR.HornedScourge)
    chr.disable_invincibility(CHR.HornedScourge)
    chr.enable_collision(CHR.HornedScourge)
    chr.enable_gravity(CHR.HornedScourge)
    chr.activate_npc_buffs(CHR.HornedScourge)
    boss.enable_boss_health_bar(CHR.HornedScourge, 2251)
    sound.enable_map_sound(1013802)
    for killplane in range(1013200, 1013205):
        hitbox.enable_hitbox(killplane)

    flag.enable(11015493)  # Battle has started.

    if_entity_health_less_than_or_equal(0, CHR.HornedScourge, 0.6)
    chr.set_special_effect(CHR.HornedScourge, 4956)  # +20% speed


def event11015494():
    """ Horned Scourge jumps back up if it falls off. """
    header(11015494)

    if_event_flag_on(1, 11015493)
    if_entity_inside_area(1, CHR.HornedScourge, REGION.HornedScourgeCatchBox)
    if_condition_true(0, 1)

    chr.disable(CHR.HornedScourge)
    wait(3.0)

    chr.disable(CHR.HornedScourge)
    for killplane in range(1013200, 1013205):
        hitbox.disable_hitbox(killplane)

    warp.warp(CHR.HornedScourge, Category.region, REGION.HornedScourgeStart, -1)
    chr.disable_gravity(CHR.HornedScourge)
    chr.disable_collision(CHR.HornedScourge)
    chr.enable_invincibility(CHR.HornedScourge)
    chr.enable_immortality(CHR.HornedScourge)
    wait_frames(5)
    chr.enable(CHR.HornedScourge)
    anim.force_animation(CHR.HornedScourge, 3009)
    wait(5.0)
    chr.disable_immortality(CHR.HornedScourge)
    chr.disable_invincibility(CHR.HornedScourge)
    chr.enable_collision(CHR.HornedScourge)
    chr.enable_gravity(CHR.HornedScourge)
    for killplane in range(1013200, 1013205):
        hitbox.enable_hitbox(killplane)

    restart()


def event11012013():
    """ Horned Scourge dies. """
    header(11012013)
    end_if_this_event_on()

    if_entity_health_less_than_or_equal(0, CHR.HornedScourge, 0.0)
    chr.cancel_special_effect(CHR.HornedScourge, 2370)
    boss.kill_boss(CHR.HornedScourge)
    item.award_item_to_host_only(ITEMLOT.HornedScourgeReward)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)
    boss.disable_boss_health_bar(CHR.HornedScourge, 2251)  # Probably redundant.
    obj.disable(1011890)
    sfx.delete_map_sfx(1011891, True)
    obj.disable(1011892)
    sfx.delete_map_sfx(1011893, True)

    flag.enable(EVENT.HornedScourgeDead)
    wait(3.0)
    sound.disable_map_sound(1013802)


def event11015482():
    """ Activate Dark Haunting Semblance (when player approaches). """
    header(11015482, 1)

    chr.disable(CHR.DarkHauntingSemblance)
    chr.disable(CHR.UnhallowedSpecter)

    if_event_flag_on(1, EVENT.HauntingSemblanceDead)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_off(1, EVENT.UnhallowedSpecterDead)
    end_if_condition_false(1)

    chr.enable(CHR.DarkHauntingSemblance)
    chr.enable_invincibility(CHR.DarkHauntingSemblance)
    chr.disable_health_bar(CHR.DarkHauntingSemblance)
    chr.disable_ai(CHR.DarkHauntingSemblance)

    if_player_inside_region(0, REGION.HauntingSemblanceTrigger)

    flag.enable(11015483)  # Battle has started.

    obj.enable(1011792)
    sfx.create_map_sfx(1011793)
    sfx.create_map_sfx(1011794)  # this tall fog has two SFX parts
    obj.enable(1011795)
    sfx.create_map_sfx(1011796)

    chr.enable_ai(CHR.DarkHauntingSemblance)
    chr.disable_invincibility(CHR.DarkHauntingSemblance)
    chr.activate_npc_buffs(CHR.DarkHauntingSemblance)
    chr.activate_npc_buffs(CHR.UnhallowedSpecter)
    boss.enable_boss_health_bar(CHR.DarkHauntingSemblance, TEXT.HauntingSemblance)
    sound.enable_map_sound(1013805)


def event11012014():
    """ Unhallowed Specter dies. """
    header(11012014)
    end_if_this_event_on()

    if_entity_health_less_than_or_equal(0, CHR.UnhallowedSpecter, 0.0)
    chr.kill(CHR.DarkHauntingSemblance, False)
    boss.kill_boss(CHR.DarkHauntingSemblance)
    item.award_item_to_host_only(ITEMLOT.UnhallowedSpecterReward)
    boss.disable_boss_health_bar(CHR.DarkHauntingSemblance, TEXT.HauntingSemblance)
    boss.disable_boss_health_bar(CHR.UnhallowedSpecter, TEXT.UnhallowedSpecter)
    sound.play_sound_effect(CHR.DarkHauntingSemblance, SoundType.s_sfx, 777777777)
    obj.disable(1011792)
    sfx.delete_map_sfx(1011793)
    sfx.delete_map_sfx(1011794)  # this tall fog has two SFX parts
    obj.disable(1011795)
    sfx.delete_map_sfx(1011796)

    flag.enable(EVENT.UnhallowedSpecterDead)
    wait(3.0)
    sound.disable_map_sound(1013805)


def event11015486():
    """ Unhallowed Specter emerges when (and then whenever) Dark Haunting Semblance reaches 80% health. """
    header(11015486)

    end_if_event_flag_on(EVENT.UnhallowedSpecterDead)

    if_event_flag_on(1, 11015483)
    if_entity_health_less_than_or_equal(1, CHR.DarkHauntingSemblance, 0.6)
    if_condition_true(0, 1)

    warp.warp_and_copy_floor(CHR.UnhallowedSpecter, 'character', CHR.DarkHauntingSemblance, 4,
                             CHR.DarkHauntingSemblance)

    skip_if_this_event_on(3)
    boss.disable_boss_health_bar(CHR.DarkHauntingSemblance, TEXT.HauntingSemblance)
    chr.disable_health_bar(CHR.DarkHauntingSemblance)
    chr.disable_health_bar(CHR.UnhallowedSpecter)

    chr.enable_invincibility(CHR.DarkHauntingSemblance)
    if_entity_health_less_than_or_equal(7, CHR.UnhallowedSpecter, 0.25)
    skip_if_condition_true(2, 7)
    chr.set_ai_id(CHR.DarkHauntingSemblance, 1)
    chr.replan_ai(CHR.DarkHauntingSemblance)
    chr.disable_gravity(CHR.UnhallowedSpecter)
    chr.disable_collision(CHR.UnhallowedSpecter)
    flag.enable(11015488)  # Specter is active.

    flag.disable_chunk(11015350, 11015353)
    flag.enable_random_in_chunk(11015350, 11015353)
    anim.force_animation(CHR.DarkHauntingSemblance, 2010)
    wait(0.5)
    chr.enable(CHR.UnhallowedSpecter)
    anim.force_animation(CHR.UnhallowedSpecter, 2015, wait_for_completion=True)
    chr.disable(CHR.UnhallowedSpecter)
    skip_if_event_flag_off(1, 11015350)
    warp.short_warp(CHR.UnhallowedSpecter, 'region', 1012681, -1)
    skip_if_event_flag_off(1, 11015351)
    warp.short_warp(CHR.UnhallowedSpecter, 'region', 1012682, -1)
    skip_if_event_flag_off(1, 11015352)
    warp.short_warp(CHR.UnhallowedSpecter, 'region', 1012683, -1)
    skip_if_event_flag_off(1, 11015353)
    warp.short_warp(CHR.UnhallowedSpecter, 'region', 1012684, -1)
    chr.enable(CHR.UnhallowedSpecter)
    anim.force_animation(CHR.UnhallowedSpecter, 3010)  # fade-in attack
    skip_if_this_event_on(1)
    boss.enable_boss_health_bar(CHR.UnhallowedSpecter, TEXT.UnhallowedSpecter)
    run_event(11015487)

    wait_random_seconds(45, 80)

    flag.disable(11015488)  # Image is inactive.
    anim.force_animation(CHR.UnhallowedSpecter, 2015, wait_for_completion=True)
    chr.disable(CHR.UnhallowedSpecter)
    chr.set_special_effect(CHR.DarkHauntingSemblance, 3231)  # Heal Haunting Semblance.
    flag.enable(11015486)  # Skip health bar swap in future.
    wait_frames(2)  # Give health time to refill.
    chr.set_ai_id(CHR.DarkHauntingSemblance, 230003)
    chr.replan_ai(CHR.DarkHauntingSemblance)
    chr.disable_invincibility(CHR.DarkHauntingSemblance)
    restart()


def event11015487():
    """ Unhallowed Specter warps around. """
    header(11015487)
    if_player_within_distance(0, CHR.UnhallowedSpecter, 4.0)
    flag.disable_chunk(11015354, 11015357)
    flag.enable_random_in_chunk(11015354, 11015357)
    if_event_flag_on(1, 11015350)
    if_event_flag_on(1, 11015354)
    if_event_flag_on(2, 11015351)
    if_event_flag_on(2, 11015355)
    if_event_flag_on(3, 11015352)
    if_event_flag_on(3, 11015356)
    if_event_flag_on(4, 11015353)
    if_event_flag_on(4, 11015357)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(-1, 4)
    restart_if_condition_true(-1)

    wait_random_seconds(5, 20)

    end_if_event_flag_off(11015488)  # Unhallowed Specter has disappeared already.
    anim.force_animation(CHR.UnhallowedSpecter, 6)  # Fade out and in.
    wait(1.0)
    flag.disable_chunk(11015350, 11015353)
    skip_if_event_flag_off(2, 11015354)
    warp.short_warp(CHR.UnhallowedSpecter, 'region', 1012681, -1)
    flag.enable(11015350)
    skip_if_event_flag_off(2, 11015355)
    warp.short_warp(CHR.UnhallowedSpecter, 'region', 1012682, -1)
    flag.enable(11015351)
    skip_if_event_flag_off(2, 11015356)
    warp.short_warp(CHR.UnhallowedSpecter, 'region', 1012683, -1)
    flag.enable(11015352)
    skip_if_event_flag_off(2, 11015357)
    warp.short_warp(CHR.UnhallowedSpecter, 'region', 1012684, -1)
    flag.enable(11015353)

    chr.rotate_to_face_entity(CHR.UnhallowedSpecter, CHR.Player)

    restart()


def event11015472():
    """ Reaper and Ransacker trigger (Black Phantom Bell Gargoyles). """
    header(11015472, 1)

    chr.disable(CHR.ReaperGargoyle)
    chr.disable(CHR.RansackerGargoyle)

    if_event_flag_on(1, EVENT.BellGargoylesDead)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_off(1, EVENT.ReaperRansackerDead)
    end_if_condition_false(1)  # No other events use this flag, so safe to end here.

    if_player_inside_region(0, 1012999)

    obj.enable(1011990)
    sfx.create_map_sfx(1011991)
    obj.enable(1011992)
    sfx.create_map_sfx(1011993)
    chr.disable(CHR.Oswald)  # for safety, re-enabled when they die

    chr.enable(CHR.ReaperGargoyle)
    chr.activate_npc_buffs(CHR.ReaperGargoyle)
    anim.force_animation(CHR.ReaperGargoyle, 3051)
    chr.enable(CHR.RansackerGargoyle)
    chr.activate_npc_buffs(CHR.RansackerGargoyle)
    anim.force_animation(CHR.RansackerGargoyle, 3051)

    wait(3.0)
    sound.disable_map_sound(1013801)  # Disable roof ambience.
    sound.enable_map_sound(1013800)

    wait(2.0)
    boss.enable_boss_health_bar_with_slot(CHR.RansackerGargoyle, 0, 5352)
    boss.enable_boss_health_bar_with_slot(CHR.ReaperGargoyle, 1, 5351)
    run_event_with_slot(11015473, 0, args=(CHR.ReaperGargoyle, CHR.RansackerGargoyle, 0.6, 0.7), arg_types='iiff')
    run_event_with_slot(11015473, 1, args=(CHR.RansackerGargoyle, CHR.ReaperGargoyle, 0.6, 0.7), arg_types='iiff')
    run_event_with_slot(11015473, 2, args=(CHR.ReaperGargoyle, CHR.RansackerGargoyle, 0.3, 0.4), arg_types='iiff')
    run_event_with_slot(11015473, 3, args=(CHR.RansackerGargoyle, CHR.ReaperGargoyle, 0.3, 0.4), arg_types='iiff')
    run_event_with_slot(11015473, 4, args=(CHR.ReaperGargoyle, CHR.RansackerGargoyle, 0.1, 0.2), arg_types='iiff')
    run_event_with_slot(11015473, 5, args=(CHR.RansackerGargoyle, CHR.ReaperGargoyle, 0.1, 0.2), arg_types='iiff')


def event11015473():
    """ One Gargoyle becomes invincible if its health falls too far below the other's. Six slots (5473-5478). """
    header(11015473)
    low_health_gargoyle, high_health_gargoyle, min_health, max_health = define_args('iiff')

    if_entity_health_less_than_or_equal(1, low_health_gargoyle, min_health)
    if_entity_health_greater_than(1, high_health_gargoyle, max_health)
    if_condition_true(0, 1)

    chr.enable_invincibility(low_health_gargoyle)

    if_entity_health_less_than_or_equal(0, high_health_gargoyle, max_health)

    chr.disable_invincibility(low_health_gargoyle)


def event11012015():
    """ Reaper and Ransacker die. """
    header(11012015)
    end_if_this_event_on()

    if_entity_health_less_than_or_equal(1, CHR.ReaperGargoyle, 0.0)
    if_entity_health_less_than_or_equal(1, CHR.RansackerGargoyle, 0.0)
    if_condition_true(0, 1)

    boss.kill_boss(CHR.ReaperGargoyle)
    item.award_item_to_host_only(ITEMLOT.ReaperRansackerReward)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)
    boss.disable_boss_health_bar_with_slot(CHR.ReaperGargoyle, 1, 5351)  # Probably redundant.
    boss.disable_boss_health_bar_with_slot(CHR.RansackerGargoyle, 0, 5352)  # Probably redundant.

    obj.disable(1011990)
    sfx.delete_map_sfx(1011991, True)
    obj.disable(1011992)
    sfx.delete_map_sfx(1011993, True)

    flag.enable(EVENT.ReaperRansackerDead)
    chr.enable(CHR.Oswald)
    wait(3.0)
    sound.disable_map_sound(1013800)
    sound.enable_map_sound(1013801)


def event11012009():
    """ Oswald stocks Velka's Rapier once you join her pact (and de-stocks it again if you break that pact). """
    header(11012009)
    skip_if_this_event_on(3)

    if_event_flag_on(0, 1910)
    flag.disable(11607030)
    flag.enable(11012009)

    if_event_flag_off(0, 1910)
    flag.enable(11012009)


def event11010001():
    """ Bell Gargoyles death. """
    header(11010001)
    if_entity_dead(1, CHR.BellGargoyleOne)
    if_entity_dead(2, CHR.BellGargoyleTwo)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    if_entity_dead(3, CHR.BellGargoyleOne)
    if_entity_dead(3, CHR.BellGargoyleTwo)
    if_condition_true(0, 3)

    flag.enable(EVENT.BellGargoylesDead)
    skip_if_condition_true_finished(3, 1)
    # Ransacker (first gargoyle) killed second.
    sound.play_sound_effect(CHR.BellGargoyleOne, SoundType.s_sfx, 777777777)
    flag.disable(51300221)  # Ransacker's Rune will appear in Catacombs.
    skip(2)
    # Reaper killed second.
    sound.play_sound_effect(CHR.BellGargoyleTwo, SoundType.s_sfx, 777777777)
    flag.disable(51300220)  # Reaper's Rune will appear in Catacombs.

    boss.kill_boss(CHR.BellGargoyleOne)
    obj.disable(1011990)
    sfx.delete_map_sfx(1011991, True)
    obj.disable(1011992)
    sfx.delete_map_sfx(1011993, True)


def event11012016():
    """ Three Thieves before Capra Demon don't respawn after all three are killed. """
    header(11012016, 1)

    skip_if_this_event_off(7)
    chr.disable(1010153)
    chr.disable(1010154)
    chr.disable(1010155)
    chr.kill(1010153, False)
    chr.kill(1010154, False)
    chr.kill(1010155, False)
    end()

    if_entity_dead(1, 1010153)
    if_entity_dead(1, 1010154)
    if_entity_dead(1, 1010155)
    if_condition_true(0, 1)
    end()


def event11010120():
    """ Rolling barrel trap. Barrel now disappears afterward. """
    header(11010120, 1)
    skip_if_this_event_off(2)
    obj.disable(OBJ.FlamingBarrel)
    end()

    chr.disable_ai(CHR.BarrelKicker)
    if_entity_attacked_by(-1, CHR.BarrelKicker, CHR.Player)
    if_player_inside_region(-1, 1012101)
    if_condition_true(0, -1)

    network.disable_sync()
    chr.reset_animation(CHR.BarrelKicker, disable_interpolation=False)
    anim.force_animation(CHR.BarrelKicker, 3006)
    wait(0.5)
    sfx.create_object_sfx(OBJ.FlamingBarrel, damipoly_id=1, sfx_id=100100)
    anim.force_animation(OBJ.FlamingBarrel, 0)
    wait(0.5)
    chr.enable_ai(CHR.BarrelKicker)
    obj.create_damaging_object(11010121, OBJ.FlamingBarrel, 1, 5020,
                               DamageTargetType.character, radius=0.6, life=3.0, repetition_time=0.0)
    wait(3.0)
    sfx.delete_object_sfx(OBJ.FlamingBarrel, erase_root=True)
    obj.disable(OBJ.FlamingBarrel)


def event11012017():
    """ Message informs you that Thrall has departed the Lower Burg when you return after dying. """
    header(11012017)
    end_if_this_event_on()
    if_event_flag_on(1, EVENT.CapriciousThrallActive)
    if_event_flag_off(1, 11015373)  # Battle not started.
    if_player_inside_region(1, 1012886)  # At fog entrance.
    if_condition_true(0, 1)
    message.status_explanation(TEXT.ThrallHasFled)


def event11012044():
    """ Monitor resting at Parish Turret bonfire. """
    header(11012044)
    if_player_within_distance(1, 1011961, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11012044)


if __name__ == '__main__':
    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event'))]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
