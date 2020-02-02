
import sys
import inspect
from pydses import *

map_name = 'm10_02_00_00'  # Firelink Shrine
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11020000
BASE_PART = 1020000


class DEBUG(IntEnum):
    DARK_ANOR_LONDO = False
    ARRIVE_FROM_PAINTED_WORLD = False
    GET_NEW_WEAPONS = False
    GET_SOUL_CONSUMABLES = False
    GET_BOSS_SOULS = False
    GET_MALEVOLENCE = False
    GET_LORDVESSEL = False
    BLIGHTTOWN_BELL_RUNG = False
    GET_DEBUG_ITEMS = False
    ENABLE_RUNE = False
    ENABLE_ALL_WARPS = False
    SETUP_GRIGGS_HOLLOW = False


class CHR(IntEnum):
    Player = 10000
    Darkwraith = 1020875
    SenStatue = 1020876
    Logan = 6031
    Griggs = 6041
    Anastacia = 6060
    Rhea = 6070
    Petrus = 6080
    Vince = 6090
    Nico = 6100
    Laurentius = 6131
    Ingward = 6181
    FemaleUndeadMerchant = 6240
    Domnhall = 6261
    CrestfallenWarrior = 6270
    Siegmeyer = 6287
    Sieglinde = 6292
    Lautrec = 6301
    Patches = 6322
    Frampt = 6330
    FramptDying = 6332
    GiantCrow = 1020100
    GiantCrowVelka = 1020101
    GiantCrowVelkaFlee = 1020102


class RING(IntEnum):
    RingOfCondemnation = 133


class ANIM(IntEnum):
    KneelingDownOneLeg = 7895
    StayKneelingDownOneLeg = 7896
    GettingUpFromKneelingDownOneLeg = 7897


class EVENT(IntEnum):
    PriscillaDead = 4
    NitoDead = 7
    QuelaagDead = 9
    SensGolemDead = 11
    FairLadyDead = 140
    CiaranDead = 1864
    VelkaPactMade = 1910  # and not broken
    LordvesselReceived = 11512000
    SerousWitness = 11502021
    ProfaneImageDead = 11010904
    GravestalkersDead = 11200901
    DarkAnorLondo = 11510400
    JareelDead = 11510901
    ParishBellRung = 11010700
    BlighttownBellRung = 11400200
    CrowFromPaintedWorld = 11102003
    DeathSoulStolen = 11312006
    CrowHurtInFirelink = 11022003
    ArrivalFromPaintedWorld = 11102004
    PaleEyeOrbReturned = 11302002
    CapraDemonTransformed = 11012000
    DepthsBurgDoorOpened = 11010162
    SerousBondObtained = 50004910
    # 11022100 range is used in common for NG+ Rune pickup disabling.
    # 11025350 range is used in common for Runes.
    # 11025400 range is used in common for Ruinous Hand.
    # 11025500 range is used in common for Runes.
    # 11025600 range is used for random flags.


class ITEMLOT(IntEnum):
    VelkaGift = 1650
    SerousBond = 4910
    FramptDeath = 53300000


class REGION(IntEnum):
    PetrusFirstPosition = 1022875
    AqueductRatsTrigger = 1022876


class GOOD(IntEnum):
    Malevolence = 717
    Lordvessel = 2510
    LiftChamberKey = 2015
    MasterKey = 2100
    PaleEyeOrb = 2530


class TEXT(IntEnum):
    PrayToCrow = 10010168
    MakeVelkaPact = 10010603
    ExamineStatue = 10010716
    SerousStatue = 10010718
    UsedLiftChamberKey = 10010874
    MasterKeyShattered = 10010883
    ReturnToPaintedWorld = 10010187


def event0():
    """ Constructor. """
    header(0)

    if DEBUG.DARK_ANOR_LONDO:
        flag.enable(EVENT.DarkAnorLondo)
    if DEBUG.ARRIVE_FROM_PAINTED_WORLD:
        flag.enable(EVENT.CrowFromPaintedWorld)
    if DEBUG.GET_SOUL_CONSUMABLES:
        for soul_lot in (1400060, 100510, 100610, 100520, 1700010, 100620, 1700150, 1100090, 1210250, 1800050):
            item.award_item_to_host_only(soul_lot)
    if DEBUG.GET_BOSS_SOULS:
        for soul_lot in range(2500, 2771, 10):
            item.award_item_to_host_only(soul_lot)
        item.award_item_to_host_only(6770)
    if DEBUG.GET_MALEVOLENCE:
        item.award_item_to_host_only(3220)
    if DEBUG.GET_LORDVESSEL:
        item.award_item_to_host_only(1090)
        flag.enable(11512000)
    if DEBUG.BLIGHTTOWN_BELL_RUNG:
        flag.enable(EVENT.BlighttownBellRung)
    if DEBUG.SETUP_GRIGGS_HOLLOW:
        flag.disable_chunk(1110, 1119)
        flag.enable(1113)
    if DEBUG.GET_DEBUG_ITEMS:
        item.award_item_to_host_only(0)  # Debug items.
        chr.enable_immortality(CHR.CrestfallenWarrior)
    if DEBUG.ENABLE_RUNE:
        flag.disable_chunk(11025350, 11025359)
        flag.enable(11025352)
        item.award_item_to_host_only(0)
        chr.enable_immortality(CHR.CrestfallenWarrior)
    if DEBUG.ENABLE_ALL_WARPS:
        flag.enable_chunk(200, 219)
        flag.enable(11012044)
        flag.enable(11302040)
        flag.enable(11202040)
        flag.enable(11402040)
        flag.enable(11002044)
        flag.enable(11512043)
        flag.enable(11512044)
        flag.enable(11312044)
        flag.enable(11412080)
        flag.enable(11602044)
        flag.enable(11702044)
        flag.enable(11212084)
        flag.enable(11812040)
    if DEBUG.GET_NEW_WEAPONS:
        item.award_item_to_host_only(10)

    # (New) Switch to dark lighting if Dark Anor Londo is active.
    skip_if_event_flag_off(1, EVENT.DarkAnorLondo)
    light.set_area_texture_parambank_slot_index(10, 1)

    map.register_bonfire(11020992, 1021960, reaction_distance=1.0, initial_kindle_level=10)
    skip_if_event_flag_off(1, 11020108)
    map.register_bonfire(11020992, 1021960, reaction_distance=1.0, initial_kindle_level=30)

    # Initialize Undead Parish elevator.
    skip_if_event_flag_off(4, 11020300)
    skip_if_event_flag_on(2, 11020302)
    anim.end_animation(1021000, 11)
    skip(1)
    anim.end_animation(1021000, 12)

    run_event(11020300)  # Undead Parish elevator. Redirects to 11020301 after first use.
    run_event(11025050)  # Crow flies away if hurt.
    run_event(11020001)  # Start music and enable characters on first arrival from Asylum.
    run_event(11020020)  # Curl up in Crow's nest.
    run_event(11020021)  # Crow takes you back to Asylum when you curl up for 20 seconds.
    run_event(11020105)  # Anastacia is killed, then revived, then kindles when you give a Lord Soul.
    run_event(11020106)  # Disable Shrine firelink_bonfire if Anastasia has been killed and not revived.
    run_event(11020108)  # Wait for a soul to be placed in the Lordvessel for Anastasia to kindle.
    # Removed this door, too troublesome.
    # run_event_with_slot(11020120, 0, args=(11020120, TEXT.UsedLiftChamberKey, 1021465,
    #                                        TEXT.MasterKeyShattered, GOOD.LiftChamberKey))
    run_event(11020350)  # Open hole to Firelink Altar.
    run_event(11020351)  # Warp to Firelink Altar when you fall in the hole (kills you if 710 is off).
    run_event(11020352)  # Disable hit boxes (maybe kill planes) for Firelink Altar hole.
    run_event(11025150)  # Prevents Hollows near aqueduct from entering a certain area (1022710).
    run_event(11022000)  # (New) Darkwraith near Parish lift spawns in Dark Anor Londo if Jareel is alive.
    run_event(11022001)  # (New) Crow moves to rooftop and enables Velka covenant interaction.
    run_event(11025051)  # (New) Moved Crow flies away if hurt, and no longer appears in Painted World.
    run_event(11022005)  # (New) Rats attack you at the Firelink end of the aqueduct.
    run_event(11022006)  # (New) Interact with Sen's Serous statue.
    run_event(11022007)  # (New) Patches loots Petrus's body and will sell Elite Cleric set.
    run_event(11022009)  # (New) Giant Crow can return you to Painted World.

    # Four treasure chests (Petrus's hidden chests behind the shrine).
    for slot, (chest, flag_id) in enumerate(zip(range(1021650, 1021654), range(11020700, 11020704))):
        run_event_with_slot(11020700, slot, args=(chest, flag_id))

    # (New) Skeleton assembly now depends on item flags.
    for slot, (skeleton, trigger_flag, delay) in enumerate((
            (1020200, 51020030, 1.0),
            (1020201, 51020030, 1.4),
            (1020202, 51020030, 2.2),
            (1020203, 51020010, 0.5),
            (1020204, 51020010, 1.0),
            (1020205, 51020020, 0.3),
            (1020206, 51020020, 1.3),
            (1020209, 51020170, 3.0),
            (1020210, 51020170, 3.7),
            (1020211, 51020150, 3.3),
            (1020212, 51020150, 0.2),
            (1020213, 51020160, 0.2))):
        run_event_with_slot(11025200, slot, args=(skeleton, trigger_flag, delay), arg_types='iif')


def event50():
    header(50, 0)

    # SAFETY CHEST

    # Enable all safety drop flags (so items won't appear).
    flag.enable_chunk(50004000, 50004069)
    for slot, safety_args in enumerate((

            # flag_must_be_on, flag_must_be_off, item_type, item_id, safety_item_flag

            # Keys.
            (50001601, 703, 3, 2001, 50004000),         # Key to the Sun Chamber
            # (11017140, 703, 3, 2002, 50004001),         # (Crest removed)
            (51500440, 703, 3, 2003, 50004002),         # Torture Cage Key
            (50006610, 703, 3, 2004, 50004003),         # Archive Tower Cell Key
            (51700950, 703, 3, 2005, 50004004),         # Archive Tower Giant Door Key
            (50001080, 703, 3, 2006, 50004005),         # Archive Tower Giant Cell Key
            (50000660, 703, 3, 2007, 50004006),         # Melted Iron Key
            (51600160, 703, 3, 2008, 50004007),         # Key to the Valley
            (51100120, 703, 3, 2009, 50004008),         # Annex Key
            (51810000, 703, 3, 2010, 50004009),         # Asylum Cell Key
            (50001660, 703, 3, 2011, 50004010),         # Big Pilgrim's Key
            (50000080, 703, 3, 2012, 50004011),         # Asylum Corridor Key
            (50000100, 703, 3, 2013, 50004012),         # Key to the Seal
            (50001051, 703, 3, 2014, 50004013),         # Tyrant's Key
            # (50000140, 703, 3, 2015, 50004014),         # (Lift Chamber Key removed)
            (51510900, 703, 3, 2016, 50004015),         # Forsaken Key
            (51300100, 703, 3, 2017, 50004016),         # Sinners' Key
            (51000170, 703, 3, 2018, 50004017),         # Sewer Key
            (50001720, 703, 3, 2019, 50004018),         # Watchtower Key
            (51700210, 703, 3, 2020, 50004019),         # Lost Cell Key
            (51010460, 703, 3, 2021, 50004020),         # Burg Latchkey

            # Lord Souls.
            (7, 11800201, 3, 2500, 50004021),           # Death Soul (now requires Nito to be dead)
            (50001580, 11800202, 3, 2501, 50004022),    # Life Soul
            (50001630, 11800203, 3, 2502, 50004023),    # Bequeathed Light Soul Shard (Four Kings)
            (50001640, 11800204, 3, 2503, 50004024),    # Bequeathed Light Soul Shard (Seath)

            (50000090, 11800100, 3, 2510, 50004025),    # Lordvessel
            (50001690, 703, 2, 138, 50004026),          # Covenant of Artorias
            (50001670, 703, 2, 137, 50004027),          # Orange Charred Ring
            (50000000, 703, 3, 100, 50004028),          # White Sign Soapstone
            (11607200, 703, 3, 101, 50004029),          # Red Sign Soapstone
            (50000390, 703, 3, 102, 50004030),          # Red Eye Orb
            (200, 703, 3, 103, 50004031),               # Black Separation Crystal
            (11017020, 703, 3, 106, 50004032),          # Orange Guidance Soapstone
            (11607020, 703, 3, 108, 50004033),          # Book of the Guilty
            (11407080, 703, 3, 112, 50004034),          # Servant Roster
            (50000360, 703, 3, 113, 50004035),          # Blue Eye Orb
            (50000260, 703, 3, 114, 50004036),          # Dragon Eye
            (200, 703, 3, 117, 50004037),               # Darksign

            (50000082, 8131, 3, 200, 50004038),         # Estus Flask
            (8131, 8132, 3, 202, 50004039),             # Estus Flask +1
            (8132, 8133, 3, 204, 50004040),             # Estus Flask +2
            (8133, 8134, 3, 206, 50004041),             # Estus Flask +3
            (8134, 8135, 3, 208, 50004042),             # Estus Flask +4
            (8135, 8136, 3, 210, 50004043),             # Estus Flask +5
            (8136, 8137, 3, 212, 50004044),             # Estus Flask +6
            (8137, 703, 3, 214, 50004045),              # Estus Flask +7

            (51010490, 11102008, 3, 384, 50004046),     # Peculiar Doll
            (11017150, 703, 3, 2600, 50004047),         # Weapon Smithbox
            (11017160, 703, 3, 2601, 50004048),         # Armor Smithbox
            (11017170, 703, 3, 2602, 50004049),         # Repairbox
            (50001550, 703, 3, 2607, 50004050),         # Rite of Kindling
            (11007010, 703, 3, 2608, 50004051),         # Bottomless Box
            (50000360, 703, 2, 102, 50004052),          # Darkmoon Blade Covenant Ring
            (50000160, 703, 2, 103, 50004053),          # Cat Covenant Ring
            (50000260, 703, 3, 377, 50004054),          # Dragon Head Stone
            (50000270, 703, 3, 378, 50004055),          # Dragon Torso Stone
            (51500040, 350, 3, 800, 50004056),          # Faded Ember
            (11217200, 351, 3, 801, 50004057),          # Sen's Ember
            (51700160, 352, 3, 802, 50004058),          # Crystal Ember
            (51211000, 356, 3, 806, 50004059),          # Oolacile Ember
            (51320140, 357, 3, 807, 50004060),          # Runic Ember
            (51010540, 358, 3, 808, 50004061),          # Blessed Ember
            (11102015, 359, 3, 809, 50004062),          # Hallowed Ember
            (11102016, 360, 3, 810, 50004063),          # Profane Ember
            (51600290, 362, 3, 812, 50004064),          # Rendain's Ember
            (50001542, 11800205, 3, 2505, 50004065),    # (NEW) Dark Remnant (replacing Chthonic Spark)
            (50000670, 11302002, 3, 2530, 50004066),    # (NEW) Pale Eye Orb (replacing Master Key)
            (51210510, 703, 3, 2022, 50004067),         # Crest Key
            (51811010, 703, 3, 2520, 50004068),         # Broken Pendant
            (50001200, 703, 3, 118, 50004069),          # Purple Coward's Crystal
    )):
        run_event_with_slot(11020800, slot, args=safety_args, arg_types='iiBii')

    # Controls safety chest.
    run_event_with_slot(11020899, 0, args=(50004000, 50004069))

    # BIG HAT LOGAN

    chr.humanity_registration(CHR.Logan, 8334)
    skip_if_event_flag_on(2, 1092)
    skip_if_event_flag_on(1, 1096)
    chr.disable(CHR.Logan)
    run_event_with_slot(11020510, 0, args=(CHR.Logan, 1096))  # Hostile
    run_event_with_slot(11020530, 0, args=(CHR.Logan, 1090, 1109, 1097))  # Dead
    # Logan moves from Sen's Fortress to Firelink Shrine.
    run_event_with_slot(11020550, 0, args=(CHR.Logan, 1090, 1109, 1092))
    # Logan has sold all his spells and moves to Duke's Archives.
    run_event_with_slot(11020551, 0, args=(CHR.Logan, 1090, 1109, 1093))

    # GRIGGS OF VINHEIM

    chr.humanity_registration(CHR.Griggs, 8342)
    skip_if_event_flag_range_not_all_off(1, 1112, 1114)
    chr.disable(CHR.Griggs)  # Griggs is here from 1112 to 1114.
    run_event_with_slot(11020510, 1, args=(CHR.Griggs, 1114))
    run_event_with_slot(11020530, 1, args=(CHR.Griggs, 1110, 1119, 1115))
    # Griggs moves from Undead Burg to Firelink Shrine.
    run_event_with_slot(11020552, 0, args=(CHR.Griggs, 1110, 1119, 1112))
    # Griggs prepares to find Logan after Logan leaves.
    run_event_with_slot(11020553, 0, args=(CHR.Griggs, 1110, 1119, 1113))
    # Griggs goes Hollow and moves to Sen's Fortress.
    run_event_with_slot(11020554, 0, args=(CHR.Griggs, 1110, 1119, 1117))

    # ANASTACIA OF ASTORA

    # EzState control. I think this is used rather than disabling her when killed.
    run_event(11020110)
    # Anastacia's humanity is taken by Lautrec.
    run_event_with_slot(11020555, 0, args=(CHR.Anastacia, 1140, 1169, 1141))
    # Lautrec's Black Eye Orb is picked up.
    run_event_with_slot(11020556, 0, args=(CHR.Anastacia, 1140, 1169, 1146))
    # Anastacia is restored with her Fire Keeper Soul.
    run_event_with_slot(11020557, 0, args=(CHR.Anastacia, 1140, 1169, 1142))
    # Anastacia powers up Firelink firelink_bonfire when a Lord Soul is given.
    run_event_with_slot(11020558, 0, args=(CHR.Anastacia, 1140, 1169, 1145))

    # RHEA OF THOROLUND

    chr.humanity_registration(CHR.Rhea, 8358)
    skip_if_event_flag_on(1, 1171)
    chr.disable(CHR.Rhea)
    # Make Rhea, Petrus, Vince, and Nico all hostile when one of them is attacked.
    run_event(11020501)
    # Rhea, Vince, and Nico all appear when Profane Image is killed.
    run_event(11020559)
    # Rhea, Petrus, Vince, and Nico all move on when spoken to (and reloaded) or Pinwheel challenged.
    # (Petrus abandons them and comes back on next reload.)
    run_event(11020560)
    run_event_with_slot(11020530, 2, args=(CHR.Rhea, 1170, 1180, 1177))  # Dead.

    # PETRUS OF THOROLUND

    chr.humanity_registration(CHR.Petrus, 8366)
    skip_if_event_flag_on(1, 1192)
    skip(1)
    chr.disable(CHR.Petrus)  # Petrus only disabled initially when 1192 is on.
    # (New) Petrus moves closer to the Shrine before his comrades arrive.
    run_event_with_slot(11022004, args=(CHR.Petrus,))
    # Petrus returns on first reload after he abandons his comrades in the Catacombs.
    run_event_with_slot(11020564, args=(CHR.Petrus, 1190, 1209, 1193))
    # Petrus 'reveals his true nature' (after killing Rhea at the Parish, I think).
    run_event_with_slot(11020565, args=(CHR.Petrus, 1190, 1209, 1194))
    # Petrus becomes hostile when comrades aren't there.
    run_event_with_slot(11020502, args=(CHR.Petrus, 1197))
    # Petrus becomes hostile after 'revealing his true nature'.
    run_event_with_slot(11020503, args=(CHR.Petrus, 1195))
    # Petrus dies before killing Rhea.
    run_event_with_slot(11020569, args=(CHR.Petrus, 1190, 1209, 1198))
    # Petrus dies after killing Rhea.
    run_event_with_slot(11020567, args=(CHR.Petrus, 1190, 1209, 1196))

    # VINCE OF THOROLUND

    chr.humanity_registration(CHR.Vince, 8374)
    skip_if_event_flag_on(1, 1211)
    chr.disable(CHR.Vince)
    run_event_with_slot(11020530, 4, args=(CHR.Vince, 1210, 1219, 1214))

    # NICO OF THOROLUND

    chr.humanity_registration(CHR.Nico, 8382)
    skip_if_event_flag_on(1, 1221)
    chr.disable(CHR.Nico)
    run_event_with_slot(11020530, 5, args=(CHR.Nico, 1220, 1229, 1224))

    # LAURENTIUS OF THE GREAT SWAMP

    chr.humanity_registration(CHR.Laurentius, 8390)
    skip_if_event_flag_on(2, 1252)
    skip_if_event_flag_on(1, 1253)
    chr.disable(CHR.Laurentius)
    run_event_with_slot(11020510, 6, args=(CHR.Laurentius, 1253))
    run_event_with_slot(11020530, 6, args=(CHR.Laurentius, 1250, 1259, 1254))
    # Laurentius moves from Depths to Firelink Shrine.
    run_event_with_slot(11020574, args=(CHR.Laurentius, 1250, 1259, 1252))
    # Laurentius moves from Firelink Shrine to Blighttown swamp (Hollow) when you tell him about Chaos pyromancy.
    run_event_with_slot(11020575, args=(CHR.Laurentius, 1250, 1259, 1256))

    # INGWARD

    chr.humanity_registration(CHR.Ingward, 8406)
    skip_if_event_flag_on(2, 1314)
    skip_if_event_flag_on(1, 1313)
    chr.disable(CHR.Ingward)
    run_event_with_slot(11020510, 7, args=(CHR.Ingward, 1314))
    run_event_with_slot(11020530, 7, args=(CHR.Ingward, 1310, 1319, 1315))
    # Ingward moves from New Londo Ruins to Firelink Shrine.
    run_event_with_slot(11020576, 0, args=(CHR.Ingward, 1310, 1319, 1313))

    # DOMNHALL OF ZENA

    chr.humanity_registration(CHR.Domnhall, 8430)
    skip_if_event_flag_on(2, 1434)
    skip_if_event_flag_on(1, 1431)
    chr.disable(CHR.Domnhall)
    run_event_with_slot(11020510, 9, args=(CHR.Domnhall, 1434))  # Hostile.
    run_event_with_slot(11020413, 0, args=(CHR.Domnhall, 1435))  # Dead.
    # Domnhall moves to Firelink Shrine when the Capricious Thrall has emerged.
    run_event_with_slot(11020412, 0, args=(CHR.Domnhall, 1430, 1459, 1431))

    # CRESTFALLEN WARRIOR

    chr.humanity_registration(CHR.CrestfallenWarrior, 8438)
    skip_if_event_flag_on(2, 1464)
    skip_if_event_flag_on(1, 1462)
    skip(1)
    chr.disable(CHR.CrestfallenWarrior)
    run_event_with_slot(11020510, 10, args=(CHR.CrestfallenWarrior, 1461))
    run_event_with_slot(11020530, 10, args=(CHR.CrestfallenWarrior, 1460, 1464, 1462))
    # Crestfallen Warrior moves to New Londo Ruins (Hollow) when Frampt wakes up.
    run_event_with_slot(11020577, 0, args=(CHR.CrestfallenWarrior, 1460, 1464, 1464))

    # SIEGMEYER OF CATARINA

    chr.humanity_registration(CHR.Siegmeyer, 8446)
    skip_if_event_flag_on(2, 1512)
    skip_if_event_flag_on(1, 1497)
    chr.disable(CHR.Siegmeyer)
    run_event_with_slot(11020510, 11, args=(CHR.Siegmeyer, 1512))
    run_event_with_slot(11020530, 11, args=(CHR.Siegmeyer, 1490, 1514, 1513))
    # Siegmeyer moves from Anor Londo to Firelink Shrine. Stays here until you go to Blighttown.
    run_event_with_slot(11020579, 0, args=(CHR.Siegmeyer, 1490, 1514, 1497))

    # SIEGLINDE OF CATARINA

    chr.humanity_registration(CHR.Sieglinde, 8454)
    skip_if_event_flag_on(3, 1547)
    skip_if_event_flag_on(2, 1545)
    skip_if_event_flag_on(1, 1543)
    chr.disable(CHR.Sieglinde)
    run_event_with_slot(11020510, 12, args=(CHR.Sieglinde, 1547))
    run_event_with_slot(11020530, 12, args=(CHR.Sieglinde, 1540, 1569, 1548))
    # Sieglinde moves from Duke's Archives to Firelink Shrine when rescued.
    run_event_with_slot(11020583, args=(CHR.Sieglinde, 1540, 1569, 1543))
    # Sieglinde leaves to search for her father.
    run_event_with_slot(11020584, args=(CHR.Sieglinde, 1540, 1569, 1544))
    # Sieglinde reappears when you save Siegmeyer in Lost Izalith.
    run_event_with_slot(11020585, args=(CHR.Sieglinde, 1540, 1569, 1545))
    # Sieglinde leaves for Ash Lake to reunite with her father.
    run_event_with_slot(11020586, args=(CHR.Sieglinde,))

    # KNIGHT LAUTREC OF CARIM

    chr.humanity_registration(CHR.Lautrec, 8462)
    skip_if_event_flag_on(3, 1572)
    skip_if_event_flag_on(2, 1574)
    skip_if_event_flag_on(1, 1577)
    chr.disable(CHR.Lautrec)
    run_event_with_slot(11020510, 13, args=(CHR.Lautrec, 1574))  # Hostile
    run_event_with_slot(11020530, 13, args=(CHR.Lautrec, 1570, 1599, 1575))  # Dead
    # Lautrec moves from New Londo to Firelink Shrine when freed.
    run_event_with_slot(11020587, args=(CHR.Lautrec, 1570, 1599, 1572))
    # Lautrec has a 1/3 chance of disappearing while at Firelink Shrine (if he's appeared once).
    skip_if_event_flag_off(1, 11020690)
    run_event_with_slot(11020588, args=(CHR.Lautrec, 1570, 1599, 1573, 1572, 1577))
    # Lautrec frees himself and appears after you kill Quelaag, Sen's Golem, or the Gravestalkers.
    run_event_with_slot(11020589, args=(CHR.Lautrec, 1570, 1599, 1577))
    # Lautrec kills Anastacia if you return the Pale Eye Orb, exit the Depths, or pick up the two specific FKS.
    run_event_with_slot(11020410, args=(CHR.Lautrec, 1570, 1599, 1578))

    # TRUSTY PATCHES

    chr.humanity_registration(CHR.Patches, 8478)
    skip_if_event_flag_on(2, 1627)
    skip_if_event_flag_on(1, 1626)
    chr.disable(CHR.Patches)
    run_event_with_slot(11020510, 14, args=(CHR.Patches, 1627))  # Hostile
    run_event_with_slot(11020530, 14, args=(CHR.Patches, 1620, 1629, 1628))  # Dead
    # Patches moves to Firelink Shrine if befriended in Tomb and Nito killed, or Death Soul stolen (even if lost again).
    run_event_with_slot(11020411, args=(CHR.Patches, 1620, 1629, 1626))

    # KINGSEEKER FRAMPT

    skip_if_event_flag_off(3, 15)
    chr.disable(CHR.Frampt)  # Frampt disappears if Gwyn is dead.
    chr.disable(CHR.FramptDying)
    skip_if_event_flag_on(14, 15)
    chr.enable_immortality(CHR.Frampt)
    chr.disable_gravity(CHR.Frampt)
    skip_if_event_flag_on(3, 1648)  # Dead (from Malevolence).
    skip_if_event_flag_on(2, 1647)
    skip_if_event_flag_on(1, 1640)
    skip(1)
    chr.disable(CHR.Frampt)
    # Frampt starts snoring when you kill the Profane Image.
    run_event_with_slot(11020420, args=(CHR.Frampt, 1640, 1649, 1641))
    # Frampt appears when either Bell of Awakening is rung.
    run_event_with_slot(11020421, args=(CHR.Frampt, 1640, 1649, 1642))
    # You have the Lordvessel.
    run_event_with_slot(11020422, args=(CHR.Frampt, 1640, 1649, 1643))
    # You have placed the Lordvessel and befriended Frampt.
    run_event_with_slot(11020423, args=(CHR.Frampt, 1640, 1649, 1644))
    # Frampt leaves if you approach having befriended Kaathe.
    run_event_with_slot(11020424, args=(CHR.Frampt, 1640, 1649, 1647))
    # Frampt leaves if you attack him.
    run_event_with_slot(11020425, args=(CHR.Frampt, 1640, 1649, 1647))
    # Frampt dies if you feed him Malevolence.
    run_event_with_slot(11020426, args=(CHR.Frampt, CHR.FramptDying, 1640, 1649, 1648))

    run_event(11026200)  # Frampt takes you to Firelink Altar.
    run_event(11026210)  # Frampt falls asleep.


def event11025200():
    """ Skeletons reassemble based on flags. If the flag is already enabled on map load, uses distance (8.0). """
    header(11025200, 1)
    skeleton, trigger_flag, delay = define_args('iif')

    # All skeletons are disabled if Rhea and party are present.
    skip_if_event_flag_off(2, 1171)
    chr.disable(skeleton)
    end()

    # If trigger flag is already enabled on load, skeleton will trigger based on distance.
    if_event_flag_off(1, 1171)  # Just in case. If they appear with Rhea there, they at least won't animate.
    skip_if_event_flag_on(2, trigger_flag)
    if_event_flag_on(1, trigger_flag)
    skip(1)
    if_player_within_distance(1, skeleton, 8.0)

    if_condition_true(0, 1)
    network.disable_sync()
    wait(delay)
    chr.set_standby_animation_settings(skeleton, cancel_animation=9061)


def event11022000():
    """ Darkwraith spawns in Dark Anor Londo if Jareel is alive. """
    header(11022000, 1)
    skip_if_this_event_off(3)
    chr.disable(CHR.Darkwraith)
    chr.drop_mandatory_treasure(CHR.Darkwraith)
    end()
    chr.disable(CHR.Darkwraith)
    if_event_flag_on(0, EVENT.DarkAnorLondo)
    chr.enable(CHR.Darkwraith)
    if_entity_health_less_than_or_equal(0, CHR.Darkwraith, 0.0)
    flag.enable(11022000)


def event11022001():
    """ Giant Crow moves and can be interacted with if she has taken you from the Painted World and you haven't done
    anything to break Velka's pact in advance. """
    header(11022001, 1)
    chr.disable(CHR.GiantCrowVelka)
    chr.disable(CHR.GiantCrowVelkaFlee)

    if_event_flag_off(7, EVENT.PriscillaDead)
    if_event_flag_off(7, EVENT.FairLadyDead)
    if_event_flag_off(7, EVENT.CiaranDead)
    if_event_flag_on(7, EVENT.CrowFromPaintedWorld)
    if_condition_true(0, 7)

    chr.disable(CHR.GiantCrow)
    chr.enable(CHR.GiantCrowVelka)
    chr.enable_immortality(CHR.GiantCrowVelka)

    end_if_event_flag_on(EVENT.VelkaPactMade)

    if_host(1)
    if_event_flag_off(1, EVENT.PriscillaDead)
    if_event_flag_off(1, EVENT.FairLadyDead)
    if_event_flag_off(1, EVENT.CiaranDead)
    if_action_button_state(1, 'character', CHR.GiantCrowVelka, 180.0, -1, 4.0, TEXT.PrayToCrow)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, CHR.GiantCrowVelka)
    anim.force_animation(CHR.Player, ANIM.KneelingDownOneLeg, wait_for_completion=True)
    anim.force_animation(CHR.Player, ANIM.StayKneelingDownOneLeg, loop=True)
    wait(2.0)
    item.award_item_to_host_only(ITEMLOT.VelkaGift)
    flag.disable(1915)  # Pact not yet broken.
    flag.enable(EVENT.VelkaPactMade)
    wait(2.0)
    message.status_explanation(TEXT.MakeVelkaPact, True)
    anim.force_animation(CHR.Player, ANIM.GettingUpFromKneelingDownOneLeg)


def event11025051():
    """ Moved Crow flies away when hurt, and returns to original position, and no longer appears in Painted World. """
    header(11025051, 0)
    end_if_event_flag_off(EVENT.CrowFromPaintedWorld)
    if_entity_health_less_than_or_equal(0, CHR.GiantCrowVelka, 0.3)
    flag.disable(EVENT.CrowFromPaintedWorld)
    flag.enable(EVENT.CrowHurtInFirelink)
    chr.disable(CHR.GiantCrowVelka)
    chr.enable(CHR.GiantCrowVelkaFlee)
    anim.force_animation(CHR.GiantCrowVelkaFlee, 7000, wait_for_completion=True)
    chr.disable(CHR.GiantCrowVelkaFlee)


def event11020555():
    """ Lautrec steals Anastacia's soul. Now triggered by replacing Pale Eye Orb or finishing the Depths. """
    header(11020555)
    anastacia, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_on(1, 1140)  # Anastacia is in her cell.
    if_event_flag_off(1, 1574)  # Lautrec is not hostile or dead.
    if_event_flag_off(1, 1575)
    
    if_event_flag_on(2, 812)
    if_event_flag_on(2, 813)
    if_condition_true(-1, 2)
    if_event_flag_on(-1, EVENT.PaleEyeOrbReturned)
    if_event_flag_on(-1, EVENT.DepthsBurgDoorOpened)
    if_condition_true(1, -1)
    if_entity_alive(1, anastacia)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)


def event11020589():
    """ Lautrec frees himself if you kill Quelaag, Sen's Golem, or the Gravestalkers. """
    header(11020589)
    lautrec, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1574)
    if_event_flag_off(1, 1578)
    if_event_flag_on(-1, 1570)  # in cell
    if_event_flag_on(-1, 1577)  # already freed himself in New Londo script (so a boss must be dead)
    if_condition_true(1, -1)
    if_event_flag_on(-2, EVENT.QuelaagDead)
    if_event_flag_on(-2, EVENT.SensGolemDead)
    if_event_flag_on(-2, EVENT.GravestalkersDead)
    if_condition_true(1, -2)
    if_in_world_area(1, 10, 2)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.enable(lautrec)
    flag.enable(11020690)  # Lautrec is not off exploring.
    flag.enable(11600130)  # Lautrec's cell gate in New Londo is open.
    # flag.enable(11020120)  # Lift chamber is open.
    # flag.enable(61020120)  # Lift chamber door is open.
    # anim.end_animation(1021465, 1)


def event11020350():
    """ Frampt's hole opens. Now only requires one bell to be rung. """
    header(11020350)
    skip_if_this_event_on(7)
    obj.disable(1021481)
    hitbox.disable_hitbox(1023510)
    if_event_flag_on(-1, EVENT.ParishBellRung)
    if_event_flag_on(-1, EVENT.BlighttownBellRung)
    if_condition_true(0, -1)
    obj.enable(1021481)
    hitbox.enable_hitbox(1023510)

    obj.disable(1021480)
    hitbox.disable_hitbox(1023500)
    map.disable_map_part(1023501)
    hitbox.disable_hitbox(1023502)


def event11020559():
    """ Vince, Nico, and Rhea appear in Firelink Shrine. Now triggered by death of Profane Image. """
    header(11020559)
    if_event_flag_on(1, 1170)
    if_event_flag_on(1, EVENT.ProfaneImageDead)
    if_condition_true(0, 1)
    flag.disable_chunk(1170, 1189)
    flag.enable(1171)
    chr.enable(CHR.Rhea)
    flag.disable_chunk(1210, 1219)
    flag.enable(1211)
    chr.enable(CHR.Vince)
    flag.disable_chunk(1220, 1229)
    flag.enable(1221)
    chr.enable(CHR.Nico)


def event11020502():
    """ Petrus becomes hostile (version when comrades have left). """
    header(11020502)
    petrus, hostile_flag = define_args('ii')

    if_event_flag_off(7, EVENT.ProfaneImageDead)
    if_event_flag_off(7, 1195)
    if_event_flag_off(7, 1197)
    if_event_flag_on(7, 1202)
    if_event_flag_on(6, EVENT.ProfaneImageDead)
    if_event_flag_off(6, 1195)
    if_event_flag_off(6, 1197)
    if_event_flag_on(6, 1193)
    if_condition_true(-2, 7)
    if_condition_true(-2, 6)
    if_condition_true(1, -2)
    if_entity_health_less_than_or_equal(1, petrus, 0.9)
    if_entity_health_greater_than(1, petrus, 0.0)
    if_entity_attacked_by(1, petrus, CHR.Player)
    if_this_event_off(1)

    if_event_flag_on(2, hostile_flag)
    if_this_event_on(2)

    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    flag.enable(hostile_flag)
    chr.set_team_type(petrus, TeamType.hostile_ally)
    network.save_request()


def event11020412():
    """ Domnhall moves to Firelink when the Thrall has left Undead Burg (dead or active). """
    header(11020412)
    domnhall, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1434)
    if_event_flag_off(1, 1435)
    if_event_flag_on(1, 1430)
    if_event_flag_on(1, EVENT.CapraDemonTransformed)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.enable(domnhall)


def event11020410():
    """ Lautrec kills Anastacia and leaves when you return the Pale Eye Orb or finish the Depths. """
    header(11020410)
    lautrec, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1574)
    if_event_flag_off(1, 1578)
    if_event_flag_on(-1, 1572)
    if_event_flag_on(-1, 1573)
    if_event_flag_on(-1, 1577)
    if_condition_true(1, -1)
    if_event_flag_on(2, 812)
    if_event_flag_on(2, 813)
    if_condition_true(-2, 2)
    if_event_flag_on(-2, EVENT.PaleEyeOrbReturned)
    if_event_flag_on(-2, EVENT.DepthsBurgDoorOpened)
    if_condition_true(1, -2)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.disable(lautrec)


def event11020411():
    """ Patches moves to Firelink. Now also triggers when you steal the Death Soul (even if lost again). """
    header(11020411)
    patches, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1622)
    if_event_flag_off(1, 1625)
    if_event_flag_off(1, 1627)
    if_event_flag_off(1, 1628)
    if_event_flag_on(1, 1624)
    if_event_flag_on(-1, EVENT.NitoDead)
    if_event_flag_on(-1, EVENT.DeathSoulStolen)
    if_condition_true(1, -1)
    if_in_world_area(1, 10, 2)
    if_condition_true(0, 1)

    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.enable(patches)


def event11020420():
    """ Frampt starts snoring when you kill the Profane Image. """
    header(11020420)
    frampt, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_on(1, 1640)
    if_event_flag_on(1, EVENT.ProfaneImageDead)
    if_event_flag_on(2, 1641)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.enable(frampt)
    chr.set_standby_animation_settings(frampt, standby_animation=9000)


def event11020421():
    """ Frampt wakes up and emerges when you ring either Bell of Awakening. """
    header(11020421)
    frampt, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_on(-1, 1640)
    if_event_flag_on(-1, 1641)
    if_condition_true(1, -1)
    if_event_flag_on(-2, EVENT.ParishBellRung)
    if_event_flag_on(-2, EVENT.BlighttownBellRung)
    if_condition_true(1, -2)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.enable(frampt)
    chr.set_standby_animation_settings(frampt, standby_animation=7003)


def event11020422():
    """ Frampt responds to you having the Lordvessel. """
    header(11020422)
    frampt, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_on(1, 1642)
    if_event_flag_on(1, EVENT.LordvesselReceived)
    if_entity_alive(1, frampt)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)


def event11020426():
    """ Frampt dies when you feed him Malevolence. """
    header(11020426)
    frampt, frampt_dying, start_flag, end_flag, new_flag = define_args('iiiii')
    chr.disable(frampt_dying)

    if_event_flag_on(-1, 1642)
    if_event_flag_on(-1, 1643)
    if_event_flag_on(-1, 1644)
    if_condition_true(1, -1)
    if_player_has_good(1, GOOD.Malevolence)
    if_player_within_distance(1, frampt, 4.0)
    if_condition_true(0, 1)

    # Player either moves out of range, or pisses Frampt off, or feeds him the soul.
    if_player_beyond_distance(-2, frampt, 4.0)
    if_event_flag_on(-3, 1642)
    if_event_flag_on(-3, 1643)
    if_event_flag_on(-3, 1644)
    if_condition_false(-2, -3)
    if_player_does_not_have_good(2, GOOD.Malevolence)
    if_condition_true(-2, 2)
    if_condition_true(0, -2)

    restart_if_condition_false_finished(2)

    # Frampt is doomed; now wait for player to move away (out of menu).
    if_player_beyond_distance(0, frampt, 5.0)

    chr.disable(frampt)
    chr.enable(frampt_dying)
    chr.disable_gravity(frampt_dying)
    chr.kill(frampt_dying, True)
    item.award_item_to_host_only(ITEMLOT.FramptDeath)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)


def event11020351():
    """ Warp to Firelink Altar when you fall in the hole. Lordvessel flag required has changed. """
    header(11020351)
    skip_if_this_event_off(2)
    hitbox.disable_hitbox(0)  # Yes, this is really what the vanilla game says.
    hitbox.disable_hitbox(0)  # Ditto.
    if_player_inside_region(0, 1022111)
    if_event_flag_on(1, EVENT.LordvesselReceived)
    skip_if_condition_true(2, 1)
    chr.kill(CHR.Player, False)
    end()

    cutscene.play_cutscene_and_warp_specific_player(180060, CutsceneType.skippable, 1802110, 18, 0, CHR.Player)
    wait_frames(1)
    restart()


def event11020352():
    """ Disable kill planes if you have the Lordvessel. """
    header(11020352)
    if_event_flag_on(0, EVENT.LordvesselReceived)
    hitbox.disable_hitbox(1023600)
    hitbox.disable_hitbox(1023601)


def event11020120():
    """ Open door, and break Master Key if used. """
    header(11020120)
    objact_id, key_message, door_id, master_key_message, key_id = define_args('iiiii')

    skip_if_this_event_slot_off(7)
    anim.end_animation(door_id, 1)  # Re-open door (note it has no closing animation).
    flag.enable(61020120)  # Door is open.
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


def event11022004():
    """ Petrus moves closer to the Shrine unless his comrades have arrived. """
    header(11022004, 1)
    petrus, = define_args('i')
    if_event_flag_off(1, 1171)  # Rhea isn't at Firelink.
    if_event_flag_off(-1, 1170)
    if_event_flag_off(-1, EVENT.ProfaneImageDead)
    if_condition_true(1, -1)  # Rhea isn't about to arrive in the same load.
    if_condition_true(0, 1)
    warp.warp(petrus, Category.region, REGION.PetrusFirstPosition, -1)


def event11020587():
    """ Lautrec moves to Firelink Shrine after he is freed from New Londo by the player. Opens lift chamber gate. """
    header(11020587)
    lautrec, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1574)
    if_event_flag_off(1, 1578)
    if_event_flag_on(1, 1571)
    if_in_world_area(1, 10, 2)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.enable(lautrec)
    flag.enable(11020690)
    flag.enable(11020691)
    # flag.enable(11020120)
    # flag.enable(61020120)
    # anim.end_animation(1021465, 1)


def event11022005():
    """ Rat attack in the aqueduct. """
    header(11022005, 1)

    for rat in range(1020150, 1020153):
        chr.disable_ai(rat)

    if_player_inside_region(0, REGION.AqueductRatsTrigger)

    for rat in range(1020150, 1020153):
        chr.enable_ai(rat)


def event11022006():
    """ Sen statue interaction. """
    header(11022006)

    if_action_button_state(0, Category.character, CHR.SenStatue, 180.0, -1, 2.0, TEXT.ExamineStatue)

    if_event_flag_on(1, EVENT.SerousWitness)
    if_event_flag_off(1, EVENT.SerousBondObtained)
    skip_if_condition_true(2, 1)
    message.dialog(TEXT.SerousStatue, ButtonType.ok_cancel, NumberButtons.no_button, CHR.SenStatue, 4.0)
    skip(1)
    item.award_item_to_host_only(ITEMLOT.SerousBond)

    wait(3.0)
    restart()


def event11022007():
    """ Patches stocks Petrus's Elite Cleric set after Petrus dies (and after reloading). """
    header(11022007)
    end_if_event_flag_on(11022008)

    skip_if_this_event_on(6)

    if_event_flag_on(1, 1626)  # Patches in Firelink (not hostile).
    if_event_flag_on(-1, 1198)  # Petrus dies before killing Rhea.
    if_event_flag_on(-1, 1196)  # Petrus dies after killing Rhea.
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    end()

    flag.disable(11307030)
    flag.disable(11307040)
    flag.disable(11307050)
    flag.disable(11307060)
    flag.enable(11022008)


def event11022009():
    """ Giant Crow can take you back to Painted World if you have a covenant. """
    header(11022009)

    if_event_flag_on(1, EVENT.VelkaPactMade)
    if_entity_backread_enabled(1, CHR.GiantCrowVelka)
    if_event_flag_off(1, EVENT.CrowHurtInFirelink)
    if_event_flag_on(1, 11022001)  # Pact event done (player has gotten back up).
    if_action_button_state(1, 'character', CHR.GiantCrowVelka, 180.0, -1, 4.0, TEXT.ReturnToPaintedWorld)
    if_condition_true(0, 1)
    warp.warp_player(11, 0, 1100991)


def event11020501():
    """ Cleric NPCs in Firelink all aggro when one of them is attacked. """
    header(11020501)
    if_event_flag_on(1, EVENT.ProfaneImageDead)
    if_event_flag_off(1, 11020693)  # Something about their Tomb events.
    if_event_flag_off(1, 1176)  # Rhea not already hostile.
    if_event_flag_range_all_off(1, 1193, 1196)  # Petrus storyline not at a certain point (post-abandonment, I assume).

    if_entity_health_less_than_or_equal(2, CHR.Rhea, 0.9)
    skip_if_event_flag_on(1, 1177)
    if_entity_attacked_by(2, CHR.Rhea, CHR.Player)

    if_entity_health_less_than_or_equal(3, CHR.Petrus, 0.9)
    skip_if_event_flag_on(1, 1198)
    if_entity_attacked_by(3, CHR.Petrus, CHR.Player)

    if_entity_health_less_than_or_equal(4, CHR.Vince, 0.9)
    skip_if_event_flag_on(1, 1214)
    if_entity_attacked_by(4, CHR.Vince, CHR.Player)

    if_entity_health_less_than_or_equal(5, CHR.Nico, 0.9)
    skip_if_event_flag_on(1, 1224)
    if_entity_attacked_by(5, CHR.Nico, CHR.Player)

    if_event_flag_on(6, 1197)

    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(-1, 4)
    if_condition_true(-1, 5)
    if_condition_true(-1, 6)
    if_condition_true(1, -1)

    if_this_event_on(7)
    if_condition_true(-2, 1)
    if_condition_true(-2, 7)
    if_condition_true(0, -2)

    # Make all four Clerics hostile.
    skip_if_event_flag_on(2, 1177)  # (Skip if Rhea dead.)
    flag.enable(1176)  # Rhea hostile.
    chr.enable(CHR.Rhea)
    chr.set_team_type(CHR.Rhea, TeamType.hostile_ally)

    skip_if_event_flag_on(2, 1198)
    flag.enable(1197)  # Petrus hostile.
    chr.enable(CHR.Petrus)
    chr.set_team_type(CHR.Petrus, TeamType.hostile_ally)

    skip_if_event_flag_on(2, 1214)
    flag.enable(1213)  # Vince hostile.
    chr.enable(CHR.Vince)
    chr.set_team_type(CHR.Vince, TeamType.hostile_ally)

    skip_if_event_flag_on(2, 1224)
    flag.enable(1223)  # Nico hostile.
    chr.enable(CHR.Nico)
    chr.set_team_type(CHR.Nico, TeamType.hostile_ally)

    network.save_request()


def event11020552():
    """ Griggs moves to Firelink Shrine. Now disables him in Burg. """
    header(11020552)
    griggs, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1114)
    if_event_flag_off(1, 1117)
    if_event_flag_on(1, 1111)
    if_in_world_area(1, 10, 2)
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.enable(griggs)
    chr.disable(6040)  # Disable Griggs in Undead Burg.


def event11020554():
    """ Griggs moves to Sen's Fortress and goes Hollow. """
    # NOTE: I have no idea how this ever worked in vanilla, but it should now.
    header(11020554)
    griggs, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1114)
    if_event_flag_off(1, 1117)
    if_event_flag_on(1, 1113)
    if_event_flag_on(1, 723)  # Griggs is sold out (including Logan's two donated spells).
    # NOTE: Used to require you to be in Sen's. No idea how that would work.
    if_not_in_world_area(1, 10, 2)
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.disable(griggs)


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
