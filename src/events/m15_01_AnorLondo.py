
import sys
import inspect
from pydses import *


map_name = 'm15_01_00_00'  # Anor Londo
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

__REMASTERED = False

BASE_FLAG = 11510000
BASE_PART = 1510000


class DEBUG(IntEnum):
    ORNSTEIN_AND_SMOUGH_DEAD = False
    GWYNDOLIN_DEAD = False
    GET_CHTHONIC_SPARK = False
    GET_DARKMOON_SEANCE_RING = False
    DARK_ANOR_LONDO = False
    SIEGMEYER_IN_ANOR_LONDO = False
    GET_LAUTREC_BLACK_EYE_ORB = False
    CAPRICIOUS_THRALL_ACTIVE = False
    FAST_GWYN_KNIGHTS = False
    GET_BUTTERFLY_SOUL = False
    DISABLE_FOG_ARCHER = False
    JAREEL_DEAD = False


class ANIM(IntEnum):
    KnightFadeIn = 6
    KnightFadeOut = 7
    KnightBackOut = 1201
    ThrallTransformation = 4000
    ThrallRetreat = 4001
    ThrallAmbushAttack = 4002
    SummonFadeIn = 6951


class REGION(IntEnum):
    MoveArcherInDarkPalace = 1512860
    TriggerArcherBattle = 1512861
    WarpIntoSunChamber = 1512862
    JareelArena = 1512802
    CapriciousThrallTrigger = 1512863
    DarkOrnsteinAndSmoughTrigger = 1512996


class RING(IntEnum):
    RingOfAsh = 152


class ITEM(IntEnum):
    PeculiarDoll = 384
    KeyToSunChamber = 2001


class ITEMLOT(IntEnum):
    DarkOrnsteinAndSmoughReward = 2950
    DarkOrnsteinScionReward = 2960


class SPEFFECT(IntEnum):
    GwyneveresRing = 2016
    RingOfEphemera = 2370
    HealFull = 3231
    SuperDarkOrnsteinRegen = 4955
    SuperDarkSmoughSpeed = 4956


class EVENT(IntEnum):
    SensGolemDead = 11
    OrnsteinAndSmoughDead = 12
    DarkOrnsteinAndSmoughDead = 11512001
    GwyndolinDead = 11510900
    DarkAnorLondo = 11510400
    JareelDead = 11510901
    LordvesselReceived = 11512000
    GetRingOfAsh = 50000096
    CapriciousThrallActive = 11012010
    CapriciousThrallTrapped = 11012011
    CapriciousThrallDead = 11012012
    AnorLondoGwynWarp = 11802002
    PaleEyeOrbReturned = 11302002
    CathedralStableFooting = 11512501
    DarkSmoughIsSupport = 11515494
    DarkOrnsteinKilledFirst = 11515498
    DarkSmoughKilledFirst = 11515499
    DarkOrnsteinAndSmoughPhaseTwoStarted = 11515496
    DarkOrnsteinScionAtHalfHealth = 11515461
    DarkOrnsteinScionAtQuarterHealth = 11515462
    WarpOptionAtSunBonfire = 11512003  # NOT disabled by Dark Anor Londo.
    WarpAbilityAtSunBonfire = 11512006
    ObtainedChthonicSpark = 11512004  # used in common for explanation message
    ThrallAmbushOngoing = 11515379


BlackKnightActiveFlags = (11515366, 11515367, 11515368, 11515369)
BlackKnightTurnFlags = (11515362, 11515363, 11515364, 11515365)


class OBJ(IntEnum):
    ChapelChest = 1511669
    LautrecFog = 1511875
    
    
class SFX(IntEnum):
    LautrecFog = 1511876
    
    
class TEXT(IntEnum):
    DesecraterSmough = 2361
    SunEaterSmough = 2362
    ForsakenKnightOrnstein = 5275
    OrnsteinLast = 5276
    AbyssalPrinceJareelBossName = 5300
    ItsLocked = 10010163
    CannotEnterPaintedWorld = 10010166
    GwynTombSealed = 10010175
    CapriciousThrallName = 2245
    CathedralUnderSiege = 10010169
    ThrallHasFled = 10010123


class CHR(IntEnum):
    Player = 10000
    Solaire = 6003
    Siegmeyer = 6283
    Lautrec = 6302
    DarkmoonKnightess = 6010
    GiantBlacksmith = 6210
    GiantBlacksmithAngry = 6211
    DarkmoonGuardian = 6750
    AbyssalPrinceJareel = 1510170
    DarkwraithLieutenant = 1510191
    SilverKnightLowArcher = 1510327
    SilverKnightHighArcher = 1510328
    SilverKnightArcherNearThrall = 1510325
    SilverKnightArcherNearBossFog = 1510500
    Gwynevere = 1510600
    Gwyndolin = 1510650
    Ornstein = 1510800
    SuperOrnstein = 1510801
    DarkOrnsteinGiant = 1510802  # large
    DarkOrnsteinScion = 1510803  # small
    Smough = 1510810
    SuperSmough = 1510811
    DarkSmough = 1510812
    CapriciousThrall = 1510875
    CapriciousThrallBoss = 1010751
    Gwyn = 1510880
    GiantCrow = 1510881
    ChapelMimic = 1510202
    DarkwraithInBossRoom = 1510188
    DarkwraithAttackingBlacksmith = 1510175


Darkwraiths = range(1510175, 1510196)
DarkAnorLondoAllies = (1510320, 1510321, 1510323, 1510324, 1510325, 1510327, 1510328, 1510329,
                       1510300, 1510301, 1510302, 1510305, 1510402, 1510403, 1510413, 1510160)
DarkAnorLondoDisabled = (
    1510401,   # Sentinel blocking Duke's Archives
    1510412,   # Royal Sentinel closest to O&S
    1510322,   # Silver Knight before the ramparts
    1510326,   # Silver Knight near inside firelink_bonfire
    1510500,   # Silver Knight archer at O&S fog
    1510876,   # Drake near the rotating gondola
    1510877,   # Drake near the rotating gondola
    1510878,   # Drake near the cathedral ramp
    1510879,   # Drake near the cathedral ramp
)
BlackKnights = (1510882, 1510883, 1510884, 1510885)


def event0():
    """ Constructor for Anor Londo. """
    header(0, 0)

    if DEBUG.GET_CHTHONIC_SPARK:
        item.award_item_to_host_only(1600)
    if DEBUG.GET_DARKMOON_SEANCE_RING:
        item.award_item_to_host_only(1600310)
    if DEBUG.GWYNDOLIN_DEAD:
        flag.enable(EVENT.GwyndolinDead)
        item.award_item_to_host_only(2600)
    if DEBUG.ORNSTEIN_AND_SMOUGH_DEAD:
        flag.enable(EVENT.OrnsteinAndSmoughDead)
    if DEBUG.DARK_ANOR_LONDO:
        flag.enable(EVENT.OrnsteinAndSmoughDead)
        flag.enable(EVENT.GwyndolinDead)
        flag.enable(EVENT.DarkAnorLondo)
    if DEBUG.GET_LAUTREC_BLACK_EYE_ORB:
        item.award_item_to_host_only(2034)
    if DEBUG.CAPRICIOUS_THRALL_ACTIVE:
        flag.enable(EVENT.CapriciousThrallActive)
    if DEBUG.GET_BUTTERFLY_SOUL:
        item.award_item_to_host_only(2530)
        item.award_item_to_host_only(0)
    if DEBUG.DISABLE_FOG_ARCHER:
        chr.disable(CHR.SilverKnightArcherNearBossFog)
    if DEBUG.JAREEL_DEAD:
        flag.enable(EVENT.JareelDead)

    skip_if_event_flag_off(1, EVENT.OrnsteinAndSmoughDead)
    map.register_bonfire(11510920, 1511950)
    for bonfire_flag, bonfire_id, kindle_level in zip((11510992, 11510984, 11510976), (1511960, 1511961, 1511962),
                                                      (10, 0, 0)):
        map.register_bonfire(bonfire_flag, bonfire_id, initial_kindle_level=kindle_level)
    map.register_ladder(11510010, 11510011, 1511140)
    map.register_ladder(11510012, 11510013, 1511141)

    # Make elevator work immediately (and skip cutscene).
    flag.enable(11510305)

    flag.disable(11510304)
    skip_if_client(2)
    obj.disable(1511994)
    sfx.delete_map_sfx(1511995, False)
    obj.disable(1511310)
    for hitbox_id in (1513301, 1513302, 1513303):
        hitbox.disable_hitbox(hitbox_id)
    skip_if_event_flag_off(1, 11510300)
    skip_if_event_flag_off(6, 11510303)
    flag.disable(11510301)
    flag.disable(11510302)
    flag.enable(11510303)
    anim.end_animation(1511300, 53)
    hitbox.enable_hitbox(1513303)
    skip(13)
    skip_if_event_flag_off(6, 11510302)
    flag.disable(11510301)
    flag.enable(11510302)
    flag.disable(11510303)
    anim.end_animation(1511300, 50)
    hitbox.enable_hitbox(1513302)
    skip(6)
    skip_if_event_flag_off(5, 11510301)
    flag.enable(11510301)
    flag.disable(11510302)
    flag.disable(11510303)
    anim.end_animation(1511300, 51)
    hitbox.enable_hitbox(1513301)

    obj.disable(1511450)
    flag.disable(11510460)
    run_event_with_slot(11510090, 0, (1511700, 1511701, 1512600, 1512601))
    run_event_with_slot(11510090, 1, (1511702, 1511703, 1512602, 1512603))

    for event_id in (11515040, 11515041, 11515042):
        run_event(event_id)

    run_event(11510200)  # Rotating lever to open palace.
    run_event(11510205)  # (New) Rotating lever to open palace in Dark Anor Londo (Jareel must be dead).
    run_event(11510201)  # Palace locked from the outside.
    run_event(11510100)  # Break chandelier.
    run_event(11510210)  # Open one-way gate to blacksmith.
    run_event(11510211)  # Blacksmith gate is locked.
    run_event(11510220)  # First activation of gondola. (Now pre-enabled.)
    run_event(11510300)  # Main gondola activation.
    run_event(11510319)  # Gondola flags.
    run_event(11510340)  # Gondola navimesh.
    run_event(11510350)  # Gondola sync.
    run_event(11510310)  # Gondola lever can't be pushed.
    run_event(11515250)  # Painting Guardian ambush.
    run_event(11515251)  # Provoke a Silver Knight.
    run_event(11510110)  # Open door to Sun Chamber. (Now requires key.)
    run_event(11510111)  # (New) Sun Chamber is locked.
    run_event(11510400)  # Trigger Dark Anor Londo.
    run_event(11510401)  # Disable Darkmoon Tomb statue.
    run_event(11510230)  # Enter Painted World if you have the Painted Doll.
    run_event(11510240)  # Return to Sen's Fortress.
    run_event(11515050)  # Offend Pale Demon and cut off Fortress return.
    run_event(11510120)  # Enable special effect 4501 in Darkmoon Tomb.
    run_event(11510130)  # (Updated) Control Dark Anor Londo enemies.
    # (Gone) Player always respawns at 'Anor Londo' bonfire in Dark Anor Londo.
    run_event(11510460)  # Kneel to Darkmoon Covenant.
    run_event(11510462)  # Two-frame sync for above.
    run_event(11510461)  # Kneel to Darkmoon Covenant, simple version.
    run_event(11510140)  # Move your bloodstain out of endless Gwyndolin corridor when you win.
    run_event(11510150)  # Trigger flag for quivering Black Eye Orb.
    run_event(11512008)  # (New) Message that Thrall has fled higher again.

    run_event(11512043)  # (NEW) Monitor resting at Sun Chamber bonfire for warping (11512045).
    run_event(11512044)  # (NEW) Monitor resting at Gwyn's Altar bonfire for warping (11512046).

    run_event(151)
    run_event(11510215)

    # Sentinel shield parts.
    for slot, sentinel_id in zip(range(14), range(1510400, 1510414)):
        run_event_with_slot(11515060, slot, (sentinel_id,))

    # Gargoyle tails removed.

    # One-way shortcut doors.
    run_event_with_slot(11510260, 0, (11510251, 1512251, 1512250), 'iii')
    run_event_with_slot(11510260, 1, (11510257, 1512253, 1512252), 'iii')
    run_event_with_slot(11510260, 2, (11510258, 1512255, 1512254), 'iii')

    # ORNSTEIN AND SMOUGH / GWYN, LORD OF LIGHT

    sound.disable_map_sound(1513800)  # Ornstein and Smough.
    sound.disable_map_sound(1513805)  # Gwyn.

    # GWYN:
    run_event(11512200)  # Gwyn trigger.
    run_event(11512201)  # Gwyn death.
    skip_if_event_flag_on(22, EVENT.AnorLondoGwynWarp)  # Skip O&S events (light and dark). Keep an eye on length.

    skip_if_event_flag_off(10, EVENT.OrnsteinAndSmoughDead)
    # Already dead:
    anim.force_animation(1511401, 0, loop=True)  # Start elevators
    anim.force_animation(1511402, 0, loop=True)
    run_event(11515392)
    for fog_wall, fog_sfx in zip((1511990, 1511992, 1511988), (1511991, 1511993, 1511989)):
        obj.disable(fog_wall)
        sfx.delete_map_sfx(fog_sfx, False)
    skip(11)

    # Alive:
    for relative_id in (5390, 5391, 5393, 5392, 1, 5394, 5395, 5396, 5397, 5398, 5399):
        run_event(BASE_FLAG + relative_id)

    # FORSAKEN KNIGHT ORNSTEIN & SUN-EATER SMOUGH

    run_event(11515492)  # Trigger. Handles all other events within.
    run_event(11512001)  # Die.

    # DARK SUN GWYNDOLIN

    sound.disable_map_sound(1513802)
    skip_if_event_flag_off(6, EVENT.GwyndolinDead)
    # Already dead:
    run_event(11515382)
    obj.disable(1511890)
    sfx.delete_map_sfx(1511891, False)
    obj.disable(1511892)
    sfx.delete_map_sfx(1511893, False)
    skip(13)
    # Alive:
    # Disable Jareel fog (otherwise visible in boss start cutscene).
    obj.disable(1511970)
    sfx.delete_map_sfx(1511971, False)
    obj.disable(1511972)
    sfx.delete_map_sfx(1511973, False)
    for relative_id in (5380, 5381, 5383, 5382, 900, 5384, 5385, 5386, 450):
        run_event(BASE_FLAG + relative_id)

    # NEW: Abyssal King Jareel.
    sound.disable_map_sound(1513803)
    skip_if_event_flag_off(6, EVENT.JareelDead)
    # Already dead:
    run_event(11515372)
    obj.disable(1511970)
    sfx.delete_map_sfx(1511971, False)
    obj.disable(1511972)
    sfx.delete_map_sfx(1511973, False)
    skip(7)
    # Alive:
    run_event(11515370)
    run_event(11515371)
    run_event(11515373)
    run_event(11515372)
    run_event(11515374)
    run_event(11515375)
    run_event(11510901)

    # Open three doors for enemies (I think).
    for relative_door_id, base_slot in zip((251, 257, 258), (0, 20, 40)):
        run_event_with_slot(11510710, base_slot, (BASE_FLAG + relative_door_id, 6750,
                                                  1512000 + relative_door_id, 1512000 + relative_door_id - 1))
        for i, relative_enemy_id in enumerate((300, 301, 302, 305, 320, 321, 322,       # Silver Knights
                                               323, 324, 325, 326, 327, 328, 329, 500,
                                               177, 178, 179, 180, 181, 181, 182, 183,  # Darkwraiths
                                               184, 185, 186, 187, 188, 189, 190)):
            run_event_with_slot(
                11510710, base_slot + i + 1, (BASE_FLAG + relative_door_id, 1510000 + relative_enemy_id,
                                              1512000 + relative_door_id, 1512000 + relative_door_id - 1))

    # Mimic triggers.
    for slot, relative_mimic_id in enumerate(range(4)):
        run_event_with_slot(11515200, slot, (1510200 + relative_mimic_id,))
        run_event_with_slot(11515210, slot, (1510200 + relative_mimic_id,))
        run_event_with_slot(11515220, slot, (1510200 + relative_mimic_id,))
        run_event_with_slot(11515230, slot, (1510200 + relative_mimic_id,))
        run_event_with_slot(11515240, slot, (1510200 + relative_mimic_id, 1512010 + relative_mimic_id))
        run_event_with_slot(11510850, slot, (1510200 + relative_mimic_id,))
        run_event_with_slot(11515190, slot, (1510200 + relative_mimic_id,))

    # Treasure chests.
    for i in range(1, 21):
        if i == 12 or i == 19:
            continue
        run_event_with_slot(11510600, i, (1511650 + i, 11510600 + i))
    anim.end_animation(1511662, 0)   # Gwyn's chest already looted
    # Only activate chapel chest before Dark Anor Londo (replaced by Mimic).
    skip_if_event_flag_on(1, EVENT.DarkAnorLondo)
    run_event_with_slot(11510600, 19, (1511669, 11510619))

    # Non-respawning enemies.
    run_event_with_slot(11510860, 0, (1510250, 0))  # Haunting Semblance
    run_event_with_slot(11510860, 3, (6640, 0))  # Dark Anor Londo Knight 1
    run_event_with_slot(11510860, 4, (6650, 0))  # Dark Anor Londo Knight 2
    run_event_with_slot(11510870, 0, (CHR.DarkmoonGuardian,))

    # NEW: Allied Silver Knights and Sentinels stop respawning in Dark Anor Londo if killed (unless Jareel is dead).
    for slot, enemy_id in enumerate(DarkAnorLondoAllies):
        run_event_with_slot(11512050, slot, (enemy_id,))
        run_event_with_slot(11512150, slot, (enemy_id,))  # They also turn hostile again if attacked in Dark AL.

    # NEW: Darkwraiths stop respawning in Dark Anor Londo if killed (unless Jareel is alive).
    for slot, enemy_id in enumerate(Darkwraiths):
        run_event_with_slot(11512100, slot, (enemy_id,))

    # NEW: Scripted rampart battle between archers and Darkwraiths. Also disables gravity
    # for the high archer.
    run_event(11512040)

    # NEW: Scripted battle between Darkwraith and Pale Demons.
    run_event(11512041)

    # NEW: Angry Giant Blacksmith in Dark Anor Londo.
    run_event(11512042)

    # NEW: Capricious Thrall one-off attack on the rooftop.
    sound.disable_map_sound(1513804)
    obj.disable(1511974)
    sfx.delete_map_sfx(1511975, False)
    obj.disable(1511976)
    sfx.delete_map_sfx(1511977, False)
    obj.disable(1511978)
    sfx.delete_map_sfx(1511979, False)
    run_event(11512060)  # Trigger and timer.
    run_event(11512061)  # Death.


def event50():
    """ NPC pre-constructor. """
    header(50, 0)

    if DEBUG.SIEGMEYER_IN_ANOR_LONDO:
        flag.disable_chunk(1490, 1514)
        flag.enable(1493)

    # DARKMOON NPCS

    chr.humanity_registration(6640, 8258)
    chr.humanity_registration(6650, 8266)

    # KNIGHT SOLAIRE (summon)

    chr.humanity_registration(6543, 8310)
    run_event(11515030)
    run_event(11515032)
    run_event(11515033)

    # KNIGHT SOLAIRE

    chr.humanity_registration(6003, 8310)
    skip_if_event_flag_on(2, 1008)
    skip_if_event_flag_on(1, 1004)
    chr.disable(CHR.Solaire)
    run_event_with_slot(11510510, 0, args=(CHR.Solaire, 1004))  # Hostile.
    run_event_with_slot(11510520, 0, args=(CHR.Solaire, 1000, 1029, 1005))  # Dead.
    # Solaire moves from Undead Burg bridge to Anor Londo.
    run_event_with_slot(11510530, args=(CHR.Solaire, 1000, 1029, 1008))

    # DARKMOON KNIGHTESS

    chr.humanity_registration(CHR.DarkmoonKnightess, 8318)
    run_event_with_slot(11510501, args=(CHR.DarkmoonKnightess, 1033))  # Hostile.
    run_event_with_slot(11510520, 1, args=(CHR.DarkmoonKnightess, 1030, 1036, 1034))  # Dead.
    # Change state when player obtains Lordvessel.
    run_event_with_slot(11510531, args=(CHR.DarkmoonKnightess, 1030, 1036, 1036))
    # Change state when player has obtained all four Lord Souls. (Doesn't include Dark Remnant.)
    run_event_with_slot(11510532, args=(CHR.DarkmoonKnightess, 1030, 1036, 1031))
    # Enables flag 151 when she dies (maybe bonfire disabled).
    run_event_with_slot(11510533, args=(CHR.DarkmoonKnightess,))

    # (OLD) GWYNEVERE (now 'killed' when you open her door)

    # GWYNDOLIN

    chr.set_team_type(CHR.Gwyndolin, TeamType.ally)
    skip_if_event_flag_range_not_all_off(1, 1240, 1249)
    flag.enable(1240)
    run_event_with_slot(11510520, 3, args=(CHR.Gwyndolin, 1240, 1249, 1242))  # Dead.
    # Switches him to boss when you kill Gwynevere (now impossible) or enter his boss fight.
    run_event_with_slot(11510502, args=(CHR.Gwyndolin, 1241))

    # GIANT BLACKSMITH

    # Stun control.
    run_event_with_slot(11515090, args=(CHR.GiantBlacksmith,))
    run_event_with_slot(11515091, args=(CHR.GiantBlacksmith,))
    run_event_with_slot(11515092, args=(CHR.GiantBlacksmith, 1511110, 1361, 1362))  # Destroy his gear.
    run_event_with_slot(11510510, 4, args=(CHR.GiantBlacksmith, 1361))  # Hostile.
    run_event_with_slot(11510525, 0, args=(CHR.GiantBlacksmith, CHR.GiantBlacksmithAngry, 1360, 1363, 1362))  # Dead.

    # SIEGMEYER OF CATARINA

    chr.humanity_registration(CHR.Siegmeyer, 8446)
    skip_if_event_flag_on(3, 1512)
    skip_if_event_flag_on(2, 1494)
    skip_if_event_flag_on(1, 1493)
    chr.disable(CHR.Siegmeyer)
    run_event_with_slot(11510510, 5, args=(CHR.Siegmeyer, 1512))  # Hostile.
    run_event_with_slot(11510520, 5, args=(CHR.Siegmeyer, 1490, 1514, 1513))  # Dead.
    # Becomes grateful when you kill the archers.
    run_event_with_slot(11510535, args=(CHR.Siegmeyer, 1490, 1514, 1494))
    # Disappears next time he de-loads after you speak to him after killing the archers.
    run_event_with_slot(11510536, args=(CHR.Siegmeyer,))
    # (New) Dies if you trigger Dark Anor Londo while he's there.
    run_event_with_slot(11510537, args=(CHR.Siegmeyer, 1490, 1514, 1513))

    # EMBRACED KNIGHT LAUTREC

    chr.humanity_registration(CHR.Lautrec, 8462)
    chr.humanity_registration(6490, 8908)
    chr.humanity_registration(6500, 8916)
    chr.disable(CHR.Lautrec)
    chr.disable(6490)
    chr.disable(6500)
    # Control AI of Lautrec and his cronies when you invade.
    run_event_with_slot(11510541, args=(CHR.Lautrec, 1570, 1599, 1578))
    # Lautrec is killed. Enables flag 8102, which triggers Lautrec's dying words and flags invasion success.
    run_event_with_slot(11510542, args=(CHR.Lautrec, 1570, 1599, 1575))
    # Control fog, enemies, and Lautrec's dialogue when you get invade.
    run_event_with_slot(11510543, args=(CHR.Lautrec, 1570, 1599, 1572))
    # Receive rewards and enable Lautrec's corpse when you return from the invasion (and mark him as dead).
    run_event_with_slot(11510544, args=(CHR.Lautrec, 1570, 1599, 1575))


def event11510240():
    """ Return to Sen's Fortress. Now requires Sen's Stone. """
    header(11510240, 1)
    end_if_client()

    skip_if_event_flag_off(2, EVENT.PaleEyeOrbReturned)  # Pale Eye Orb must be returned.
    skip_if_event_flag_off(1, EVENT.SensGolemDead)  # Sen's Golem must be dead.
    skip(2)
    chr.disable(1510100)
    end()

    if_in_world_area(0, 15, 1)
    if_time_elapsed(0, 5.0)
    if_event_flag_off(2, 11515050)
    if_action_button_state(2, 'character', 1510100, 180.0, -1, 7.0, 10010200)
    if_condition_true(0, 2)
    skip_if_singleplayer(2)
    message.dialog(10010194, ButtonType.ok_cancel, NumberButtons.no_button, -1, 3.0)  # New message
    restart()
    skip_if_event_flag_on(2, EVENT.DarkAnorLondo)
    cutscene.play_cutscene_and_warp_player(150130, CutsceneType.skippable, 1502500, 15, 0)
    skip(1)
    cutscene.play_cutscene_and_warp_player(150132, CutsceneType.skippable, 1502500, 15, 0)
    wait_frames(1)
    restart()


def event11510150():
    """ Trigger flag for quivering Black Eye Orb. """
    header(11510150, 0)
    network.disable_sync()
    if_host(1)
    if_player_has_item(1, ItemType.good, 115)
    if_player_inside_region(1, 1512101)
    if_condition_true(0, 1)
    end()


def event11510535():
    """ Siegmeyer needs you to kill the two archers. """
    header(11510535, 0)
    npc, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1512)
    if_event_flag_on(1, 1493)
    if_entity_dead(1, CHR.SilverKnightLowArcher)
    if_entity_dead(1, CHR.SilverKnightHighArcher)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.enable(npc)


def event11510537():
    """ Siegmeyer dies if you trigger Dark Anor Londo before helping him with the archers.
    I'd do something more interesting here, but don't have the dialogue necessary. """
    header(11510537, 0)
    npc, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_on(1, 1493)  # Still stuck at the archers.
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.disable(npc)


def event11510541():
    """ Lautrec AI control. """
    header(11510541, 0)
    npc, start_flag, end_flag, new_flag = define_args('iiii')
    if DEBUG.GET_LAUTREC_BLACK_EYE_ORB:
        if_event_flag_on(-1, 1570)  # Lautrec defaults to Anor Londo.
    if_event_flag_on(-1, 1572)
    if_event_flag_on(-1, 1573)
    if_event_flag_on(-1, 1577)  # Freed himself.
    if_condition_true(1, -1)
    if_event_flag_on(1, 11510700)  # Invasion event.
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.set_team_type(6490, TeamType.white_phantom)
    chr.set_team_type(6500, TeamType.white_phantom)
    chr.disable_ai(npc)
    chr.disable_ai(6490)
    chr.disable_ai(6500)
    if_event_flag_on(-1, 11510598)
    if_entity_attacked_by(-1, npc, CHR.Player)
    if_entity_attacked_by(-1, 6490, CHR.Player)
    if_entity_attacked_by(-1, 6500, CHR.Player)
    if_condition_true(0, -1)
    chr.enable_ai(npc)
    chr.enable_ai(6490)
    chr.enable_ai(6500)


def event11510543():
    """ Lautrec entity control.  """
    header(11510543, 0)
    npc, start_flag, end_flag, new_flag = define_args('iiii')
    obj.disable(1511750)
    sfx.delete_map_sfx(1511751, False)
    obj.disable(1511752)
    sfx.delete_map_sfx(1511753, False)
    obj.disable(1511754)
    sfx.delete_map_sfx(1511755, False)
    obj.disable(OBJ.LautrecFog)
    sfx.delete_map_sfx(SFX.LautrecFog, False)
    if_event_flag_on(0, 11510700)
    obj.enable(OBJ.LautrecFog)
    sfx.create_map_sfx(SFX.LautrecFog)
    for chest in (1511654, 1511656, 1511657):
        # Open chests in the basement and disable their treasure.
        anim.end_animation(chest, 0)
        obj.disable_activation(chest, -1)
        obj.disable_treasure(chest)
    flag.disable(8104)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.disable(1510250)  # Haunting Semblance
    chr.disable(1510200)  # Mimic near stairs
    chr.enable(npc)
    chr.enable(6490)
    chr.enable(6500)
    skip_if_event_flag_on(2, 8101)
    flag.enable(8101)
    end()
    flag.enable(8100)


def event11510090():
    """ Checkpoint fog activation. (Vanilla, because I somehow screwed it up originally.) """
    header(11510090, 0)
    fog_wall, fog_sfx, intended_side_trigger_area, opposite_side_trigger_area = define_args('iiii')
    skip_if_this_event_slot_off(3)
    obj.disable(fog_wall)
    sfx.delete_map_sfx(fog_sfx, False)
    end()

    if_action_button_state_and_line_segment(1, 'region', intended_side_trigger_area, 0, 0, 0, 10010403,
                                            ReactionAttribute.human_or_hollow, 0, line_segment_endpoint_id=fog_wall)
    if_action_button_state_and_line_segment(2, 'region', opposite_side_trigger_area, 0, 0, 0, 10010407,
                                            ReactionAttribute.human_or_hollow, 0, line_segment_endpoint_id=fog_wall)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    skip_if_condition_true_finished(2, 2)
    warp.short_warp(CHR.Player, 'region', intended_side_trigger_area, -1)
    skip(1)
    warp.short_warp(CHR.Player, 'region', opposite_side_trigger_area, -1)
    anim.force_animation(CHR.Player, 7410)
    obj.disable(fog_wall)
    sfx.delete_map_sfx(fog_sfx, True)


def event11510110():
    """ Open Gwynevere's door. Requires key. """
    header(11510110, 0)
    skip_if_this_event_off(2)
    anim.end_animation(1511010, 0)
    end()
    if_player_has_item(1, ItemType.good, ITEM.KeyToSunChamber)
    if_action_button_state(1, 'object', 1511010, 60.0, 100, 1.5, 10010400, ReactionAttribute.all, pad_id=0)
    if_condition_true(0, 1)
    warp.short_warp(CHR.Player, 'object', 1511010, 120)
    anim.force_animation(CHR.Player, 7120)
    anim.force_animation(1511010, 0)


def event11510111():
    """ New: Gwynevere's door is locked. """
    header(11510111, 0)
    end_if_event_flag_on(11510110)
    if_player_does_not_have_item(1, ItemType.good, ITEM.KeyToSunChamber)
    if_action_button_state(1, 'object', 1511010, 60.0, 100, 1.5, 10010400, ReactionAttribute.all, pad_id=0)
    if_condition_true(0, 1)
    message.dialog(10010163, ButtonType.yes_no, NumberButtons.no_button, -1, 3.0)
    restart()


def event11510130():
    """ Enables and disables enemies in Dark Anor Londo. (Respawns are handled elsewhere.) """
    header(11510130, 1)

    skip_if_event_flag_off(3, EVENT.AnorLondoGwynWarp)
    chr.disable(CHR.DarkwraithInBossRoom)
    chr.disable(CHR.SilverKnightArcherNearBossFog)
    end()

    # Changes to make when Dark Anor Londo begins
    skip_if_event_flag_on(10 + 2 * len(Darkwraiths), EVENT.DarkAnorLondo)
    chr.disable(6640)
    chr.disable(6650)
    chr.disable(CHR.ChapelMimic)
    chr.disable(CHR.AbyssalPrinceJareel)
    for darkwraith in Darkwraiths:
        chr.disable(darkwraith)
    if_event_flag_on(0, EVENT.DarkAnorLondo)
    chr.enable(6640)
    chr.enable(6650)
    chr.enable(CHR.ChapelMimic)
    chr.enable(CHR.AbyssalPrinceJareel)
    chr.disable_ai(CHR.AbyssalPrinceJareel)   # maybe redundant
    for darkwraith in Darkwraiths:
        chr.enable(darkwraith)

    # Skips to here if Dark Anor Londo has already started.
    # Disable chapel chest (replaced by Mimic).
    obj.disable(OBJ.ChapelChest)
    obj.disable_activation(OBJ.ChapelChest, -1)
    for enemy_id in DarkAnorLondoAllies:
        chr.set_team_type(enemy_id, TeamType.fighting_ally)
    # Move Palace archer.
    warp.short_warp(1510301, 'region', REGION.MoveArcherInDarkPalace, -1)
    for enemy_id in DarkAnorLondoDisabled:
        chr.disable(enemy_id)
    for painting_guardian_id in range(1510150, 1510159):
        # Disable Painting Guardians on the floor (except one getting killed).
        chr.disable(painting_guardian_id)
    skip_if_event_flag_on(1, 11510861)  # Skip if Darkmoon Guardian is already dead.
    warp.warp(CHR.DarkmoonGuardian, 'region', 1512451, -1)
    end_if_event_flag_on(1034)  # Stop here if Darkmoon Knightess is already dead.
    warp.warp(CHR.DarkmoonKnightess, 'region', 1512450, -1)
    chr.set_nest(CHR.DarkmoonKnightess, 1512450)
    chr.set_standby_animation_settings_to_default(CHR.DarkmoonKnightess)


def event11510131():
    """ Removed: used to force player to respawn at 'Anor Londo' bonfire in Dark Anor Londo. """
    header(11510131, 0)
    end()


def event11510220():
    """ New unconditional activation of corkscrew elevator (since player could start at the bottom). """
    header(11510220, 0)
    anim.force_animation(1511050, 0)


def event11510230():
    """ Enter Painted World. Doesn't work if Jareel is in Anor Londo. """
    header(11510230, 0)
    if_action_button_state(0, 'region', 1512510, 0.0, -1, 0.0, 10010100)
    if_singleplayer(1)
    if_host(1)
    if_player_has_item(1, ItemType.good, ITEM.PeculiarDoll)
    if_event_flag_off(-7, EVENT.DarkAnorLondo)
    if_entity_dead(-7, 1510194)
    if_condition_true(1, -7)
    skip_if_condition_true(3, 1)
    skip_if_client(1)
    message.dialog(10010166, ButtonType.ok_cancel, NumberButtons.no_button, -1, 3.0)
    restart()
    cutscene.play_cutscene_and_warp_player(150135, CutsceneType.skippable, 1102510, 11, 0)
    wait_frames(1)
    warp.set_player_respawn_point(1102511)
    network.save_request()
    restart()


def event11510400():
    """ Trigger Dark Anor Londo by opening Gwynevere's door. """
    header(11510400, 1)
    map.disable_map_part(1513401)

    # Don't change to Dark Anor Londo if this is the Gwyn encounter.
    skip_if_event_flag_off(3, EVENT.AnorLondoGwynWarp)
    chr.disable(CHR.Gwynevere)
    sound.disable_map_sound(1513801)
    end()

    # Already Dark:
    skip_if_this_event_off(8)
    chr.disable(CHR.Gwynevere)
    sound.disable_map_sound(1513801)
    if __REMASTERED:
        light.set_area_texture_parambank_slot_index(15, 2)
    else:
        light.set_area_texture_parambank_slot_index(15, 1)
    game.set_locked_camera_slot_number(15, 1, 1)
    map.disable_map_part(1513400)
    map.enable_map_part(1513401)
    obj.disable(1511400)
    end()

    # Wait for doors to open:
    if_event_flag_on(0, 11510110)   # door opened
    sound.disable_map_sound(1513801)
    chr.disable(CHR.Gwynevere)
    flag.disable_chunk(1230, 1239)
    flag.enable(1232)  # Gwynevere 'dead'.
    wait(7)
    flag.enable(743)   # something about an NPC summon
    # Betray Princess's Guard covenant:
    if_character_type(-1, CHR.Player, CharacterType.human)
    if_character_type(-1, CHR.Player, CharacterType.hollow)
    if_condition_true(1, -1)
    if_player_covenant(1, 2)
    skip_if_condition_false(4, 1)
    game.betray_current_covenant()
    network.increment_player_pvp_sin()
    flag.enable(742)
    # Respawn at nearby bonfire:
    warp.set_player_respawn_point(1512962)
    network.save_request()
    flag.disable(120)
    cutscene.play_cutscene_to_player(150111, CutsceneType.skippable, CHR.Player)   # Gwyndolin must be dead
    wait_frames(1)
    warp.short_warp(CHR.Player, 'region', REGION.WarpIntoSunChamber, -1)
    if __REMASTERED:
        light.set_area_texture_parambank_slot_index(15, 2)
    else:
        light.set_area_texture_parambank_slot_index(15, 1)
    game.set_locked_camera_slot_number(15, 1, 1)
    map.disable_map_part(1513400)
    map.enable_map_part(1513401)
    obj.disable(1511400)
    # Close cathedral doors:
    flag.disable(11510200)
    chr.reset_animation(1511000, True)
    chr.reset_animation(1511001, True)
    event.restart_event_id(11510200)
    # Award Lordvessel if not already given:
    if_event_flag_on(2, EVENT.LordvesselReceived)
    end_if_condition_true(2)
    item.award_item_to_host_only(1090)


def event11510900():
    """ Dark Sun Gwyndolin dies. Now also enables Jareel's fog. """
    header(11510900, 0)
    if_entity_health_less_than_or_equal(0, CHR.Gwyndolin, 0.0)
    wait_frames(1)
    skip_if_client(11)
    flag.enable(11515389)
    if_event_flag_on(0, 11515389)
    # Enable Jareel fog.
    obj.enable(1511970)
    sfx.create_map_sfx(1511971)
    obj.enable(1511972)
    sfx.create_map_sfx(1511973)
    skip_if_event_flag_on(2, EVENT.DarkAnorLondo)
    cutscene.play_cutscene_and_warp_player(150152, CutsceneType.skippable, 1512897, 15, 1)
    skip(1)
    cutscene.play_cutscene_and_warp_player(150157, CutsceneType.skippable, 1512897, 15, 1)
    wait_frames(1)
    skip_if_event_flag_off(1, EVENT.OrnsteinAndSmoughDead)
    flag.enable(120)
    flag.enable(11510900)
    boss.kill_boss(CHR.Gwyndolin)
    obj.disable(1511890)
    sfx.delete_map_sfx(1511891, True)
    end_if_client()
    flag.disable(11807170)
    flag.disable(11807180)
    flag.disable(11807190)
    flag.disable(11807230)
    game.award_achievement(39)


def event11515370():
    """ Host enters Jareel fog. """
    header(11515370, 0)
    if_event_flag_off(1, EVENT.JareelDead)
    if_action_button_state_and_line_segment_in_boss(1, 'region', 1512958, 0.0, -1, 0.0, 10010403,
                                                    ReactionAttribute.human_or_hollow, 0, 1512802)
    if_condition_true(0, 1)
    skip_if_event_flag_off(3, EVENT.DarkAnorLondo)
    chr.rotate_to_face_entity(CHR.Player, 1512957)
    anim.force_animation(CHR.Player, 7410)
    skip(1)
    message.status_explanation(10010175, True)
    wait(3.0)
    restart()


def event11515371():
    """ Client enters Jareel fog. """
    header(11515371, 0)
    if_event_flag_off(1, EVENT.JareelDead)
    if_event_flag_on(1, 11515373)
    if_character_type(1, CHR.Player, CharacterType.white_phantom)
    if_action_button_state_and_line_segment(1, 'region', 1512958, 0.0, -1, 0.0, 10010403,
                                            ReactionAttribute.all, 0, 1512802)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1512957)
    anim.force_animation(CHR.Player, 7410)
    restart()


def event11515373():
    """ Notify about Jareel battle. """
    header(11515373, 0)
    skip_if_this_event_on(3)
    if_event_flag_off(1, EVENT.JareelDead)
    if_player_inside_region(1, 1512956)
    if_condition_true(0, 1)
    skip_if_client(1)
    network.notify_boss_room_entry()
    chr.activate_npc_buffs(CHR.AbyssalPrinceJareel)


def event11515374():
    """ Enable Jareel music. """
    header(11515374, 0)
    network.disable_sync()
    if_event_flag_off(1, EVENT.JareelDead)
    if_event_flag_on(1, 11515372)
    skip_if_host(1)
    if_event_flag_on(1, 11515391)
    if_player_inside_region(1, 1512802)
    if_condition_true(0, 1)
    sound.enable_map_sound(1513803)


def event11515375():
    """ Disable Jareel music. """
    header(11515375, 0)
    network.disable_sync()
    if_event_flag_on(1, EVENT.JareelDead)
    if_event_flag_on(1, 11515374)
    if_condition_true(0, 1)
    sound.disable_map_sound(1513803)


def event11515372():
    """ Jareel battle trigger. (Hopefully self-resets.) """
    header(11515372, 1)
    skip_if_event_flag_off(4, EVENT.JareelDead)
    chr.disable(CHR.AbyssalPrinceJareel)
    chr.kill(CHR.AbyssalPrinceJareel, False)
    chr.disable_backread(CHR.AbyssalPrinceJareel)
    end()
    chr.disable_ai(CHR.AbyssalPrinceJareel)
    if_event_flag_on(1, 11515373)
    if_player_inside_region(1, REGION.JareelArena)
    if_condition_true(0, 1)
    chr.enable_ai(CHR.AbyssalPrinceJareel)
    boss.enable_boss_health_bar(CHR.AbyssalPrinceJareel, TEXT.AbyssalPrinceJareelBossName)


def event11510901():
    """ Jareel's death. """
    header(11510901, 0)
    if_entity_dead(0, CHR.AbyssalPrinceJareel)
    boss.kill_boss(CHR.AbyssalPrinceJareel)  # Also disables HP bar and plays boss death sound.
    obj.disable(1511970)
    sfx.delete_map_sfx(1511971)
    obj.disable(1511972)
    sfx.delete_map_sfx(1511973)


def event11512040():
    """ Scripted event where Darkwraiths attack archers on the rampart. """
    header(11512040, 1)
    chr.disable_gravity(CHR.SilverKnightHighArcher)
    if_event_flag_on(0, EVENT.DarkAnorLondo)
    if_entity_dead(1, CHR.SilverKnightLowArcher)
    if_entity_dead(1, CHR.SilverKnightHighArcher)
    end_if_condition_true(1)
    if_entity_dead(2, 1510176)
    end_if_condition_true(2)
    chr.disable_ai(CHR.SilverKnightLowArcher)
    chr.disable_ai(CHR.SilverKnightHighArcher)
    chr.disable_ai(1510176)
    if_player_inside_region(0, REGION.TriggerArcherBattle)
    chr.enable_ai(CHR.SilverKnightLowArcher)
    chr.enable_ai(CHR.SilverKnightHighArcher)
    chr.enable_ai(1510176)


def event11512041():
    """ Scripted event where a Darkwraith takes on the Pale Demons near Duke's Archives. """
    header(11512041, 1)
    if_event_flag_on(0, EVENT.DarkAnorLondo)
    if_entity_dead(1, 1510195)
    end_if_condition_true(1)
    # Change lone Darkwraith near Pale Demons to 'charm', which is basically 'battle friend'.
    chr.set_team_type(1510195, TeamType.charm)
    if_entity_dead(2, 1510110)
    if_entity_dead(2, 1510111)
    if_entity_dead(2, 1510112)
    if_condition_true(0, 2)
    # When all three Pale Demons are dead, switch back to enemy.
    chr.set_team_type(1510195, TeamType.enemy)


def event11512042():
    """ Swaps Giant Blacksmith for an aggressive version (with no vendor behavior) as
    long as Jareel is alive in Dark Anor Londo. """
    header(11512042, 1)

    chr.disable(CHR.GiantBlacksmithAngry)

    skip_if_event_flag_off(3, EVENT.JareelDead)
    chr.disable(CHR.DarkwraithAttackingBlacksmith)
    chr.kill(CHR.DarkwraithAttackingBlacksmith, False)
    end()

    # Angry blacksmith when Dark Anor Londo starts.
    if_event_flag_on(0, EVENT.DarkAnorLondo)
    chr.disable(CHR.GiantBlacksmith)
    chr.enable(CHR.GiantBlacksmithAngry)
    chr.set_team_type(CHR.GiantBlacksmithAngry, TeamType.fighting_ally)

    # Restore blacksmith and kill his aggressor when Jareel dies (if blacksmith is alive).
    if_entity_alive(1, CHR.GiantBlacksmithAngry)
    if_event_flag_off(1, 1362)  # Only if Giant Blacksmith is not dead.
    if_event_flag_on(1, EVENT.JareelDead)
    if_condition_true(0, 1)
    chr.disable(CHR.DarkwraithAttackingBlacksmith)
    chr.kill(CHR.DarkwraithAttackingBlacksmith, False)
    chr.disable(CHR.GiantBlacksmithAngry)
    chr.enable(CHR.GiantBlacksmith)


def event11512050():
    """ Silver Knights and Sentinels stop respawning in Dark Anor Londo if Jareel is alive. """
    header(11512050, 1)
    ally, = define_args('i')

    skip_if_this_event_slot_off(3)
    chr.disable(ally)
    chr.kill(ally, False)
    end()

    if_entity_dead(1, ally)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_off(1, EVENT.JareelDead)
    if_condition_true(0, 1)
    end()


def event11512100():
    """ Darkwraiths stop respawning in Dark Anor Londo if Jareel is dead. """
    header(11512100, 1)
    darkwraith, = define_args('i')
    skip_if_this_event_slot_off(3)
    chr.disable(darkwraith)
    chr.kill(darkwraith, False)
    end()
    skip_if_equal(1, darkwraith, CHR.DarkwraithInBossRoom)  # Darkwraith in O&S room doesn't need to be killed to stop respawning
    if_entity_dead(1, darkwraith)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    skip_if_equal(1, darkwraith, 1510175)   # Darkwraith fighting the Giant Blacksmith never respawns once killed
    if_event_flag_on(1, EVENT.JareelDead)
    if_condition_true(0, 1)
    end()


def event11512150():
    """ Your allies in Dark Anor Londo will turn hostile again if you attack them. """
    header(11512150, 1)
    ally, = define_args('i')
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_entity_attacked_by(1, ally, CHR.Player)
    if_condition_true(0, 1)
    wait(1.0)  # You have to attack them twice.
    if_entity_attacked_by(0, ally, CHR.Player)
    chr.set_team_type(ally, TeamType.hostile_ally)


def event11512060():
    """ Capricious Thrall ambush (one-off). """
    header(11512060, 1)
    chr.disable(CHR.CapriciousThrall)
    end_if_this_event_on()
    end_if_event_flag_on(EVENT.CapriciousThrallDead)

    if_event_flag_on(0, EVENT.CapriciousThrallActive)
    chr.disable(CHR.SilverKnightArcherNearThrall)

    if_event_flag_on(1, EVENT.CapriciousThrallActive)
    if_host(1)
    if_player_inside_region(1, REGION.CapriciousThrallTrigger)
    if_condition_true(0, 1)

    # Ambush.
    flag.enable(EVENT.ThrallAmbushOngoing)  # Ambush is ongoing. Note this MUST be enabled before the flag below.
    flag.enable(11512060)  # One-off ambush is done.
    flag.enable(11502003)  # Thrall won't appear in Sen's.
    flag.enable(11502004)  # Thrall won't appear in Sen's.
    obj.enable(1511974)
    sfx.create_map_sfx(1511975)
    obj.enable(1511976)
    sfx.create_map_sfx(1511977)
    obj.enable(1511978)
    sfx.create_map_sfx(1511979)
    chr.enable(CHR.CapriciousThrall)
    anim.force_animation(CHR.CapriciousThrall, ANIM.ThrallAmbushAttack)
    wait(0.5)
    sound.enable_map_sound(1513804)
    boss.enable_boss_health_bar(CHR.CapriciousThrall, TEXT.CapriciousThrallName)
    wait(100.0)  # Battle timer.
    end_if_event_flag_on(11512061)  # Already dead and handled.
    boss.disable_boss_health_bar(CHR.CapriciousThrall, TEXT.CapriciousThrallName)
    sound.play_sound_effect(CHR.CapriciousThrall, SoundType.s_sfx, 777777777)  # For effect.
    wait(3.0)  # so sound effect can build up and slightly mask the abrupt music stop
    sound.disable_map_sound(1513804)
    anim.force_animation(CHR.CapriciousThrall, ANIM.ThrallRetreat)
    wait(1.4)
    chr.disable(CHR.CapriciousThrall)
    obj.disable(1511974)
    sfx.delete_map_sfx(1511975)
    obj.disable(1511976)
    sfx.delete_map_sfx(1511977)
    obj.disable(1511978)
    sfx.delete_map_sfx(1511979)
    message.status_explanation(TEXT.ThrallHasFled)
    flag.enable(11512008)  # Message won't appear when you come back.


def event11512061():
    """ Capricious Thrall dies. """
    header(11512061, 0)
    end_if_event_flag_on(EVENT.CapriciousThrallDead)

    if_entity_health_less_than_or_equal(0, CHR.CapriciousThrall, 0.0)
    wait(1.0)
    sound.play_sound_effect(CHR.CapriciousThrall, SoundType.s_sfx, 777777777)
    if_entity_dead(0, CHR.CapriciousThrall)
    boss.kill_boss(CHR.CapriciousThrallBoss)
    flag.disable(EVENT.CapriciousThrallActive)
    flag.disable(EVENT.CapriciousThrallTrapped)
    flag.enable(EVENT.CapriciousThrallDead)  # Story flag for Thrall
    boss.disable_boss_health_bar(CHR.CapriciousThrall, TEXT.CapriciousThrallName)
    sound.disable_map_sound(1513804)
    obj.disable(1511974)
    sfx.delete_map_sfx(1511975)
    obj.disable(1511976)
    sfx.delete_map_sfx(1511977)
    obj.disable(1511978)
    sfx.delete_map_sfx(1511979)


def event11512200():
    """ Gwyn, Lord of Light end-game encounter. """
    header(11512200, 1)

    skip_if_event_flag_on(7, EVENT.AnorLondoGwynWarp)
    chr.disable(CHR.Gwyn)
    chr.disable(CHR.GiantCrow)
    chr.disable(BlackKnights[0])
    chr.disable(BlackKnights[1])
    chr.disable(BlackKnights[2])
    chr.disable(BlackKnights[3])
    end()

    for boss_id in (CHR.Ornstein, CHR.SuperOrnstein, CHR.Smough, CHR.SuperSmough):
        chr.disable(boss_id)
    for knight in BlackKnights:
        chr.enable_immortality(knight)
        chr.disable_health_bar(knight)
        chr.disable(knight)

    anim.force_animation(CHR.Player, ANIM.SummonFadeIn)

    chr.enable_invincibility(CHR.GiantCrow)
    chr.disable_gravity(CHR.GiantCrow)
    chr.disable_collision(CHR.GiantCrow)
    chr.set_special_effect(CHR.Gwyn, 620)  # add light to Gwyn
    chr.set_special_effect(CHR.Gwyn, 3170)  # add lightning to Gwyn's weapon

    chr.disable_ai(CHR.Gwyn)
    anim.force_animation(CHR.Gwyn, 200, loop=True)
    wait(2.0)
    anim.force_animation(CHR.Gwyn, 200)
    chr.enable_ai(CHR.Gwyn)
    sound.enable_map_sound(1513805)
    boss.enable_boss_health_bar(CHR.Gwyn, 5375)
    flag.disable(EVENT.AnorLondoGwynWarp)

    flag.enable(11515360)

    if DEBUG.FAST_GWYN_KNIGHTS:
        wait(10.0)
    else:
        wait(135.0)  # Time it takes for Soul of Cinder music to get to piano part.

    chr.ai_instruction(CHR.Gwyn, 1, 0)
    anim.force_animation(CHR.Gwyn, 3030)
    wait(2.1)
    if __REMASTERED:
        light.set_area_texture_parambank_slot_index(15, 2)
    else:
        light.set_area_texture_parambank_slot_index(15, 1)
    wait(3.0)
    chr.rotate_to_face_entity(CHR.Gwyn, CHR.Player)

    end_if_event_flag_on(11512201)  # Gwyn already dead, no Black Knights.

    flag.enable(BlackKnightTurnFlags[0])  # Sword spawns first.
    run_event(11512202)  # Black Knight spawn manager
    for slot, (knight, knight_active_flag) in enumerate(zip(BlackKnights, BlackKnightActiveFlags)):
        run_event_with_slot(11512210, slot, args=(knight, knight_active_flag))  # Death triggers


def event11512201():
    """ Gwyn, Lord of Light dies. """
    header(11512201, 0)
    end_if_this_event_on()
    if_event_flag_on(1, 11515360)
    if_entity_health_less_than_or_equal(1, CHR.Gwyn, 0.0)
    if_condition_true(0, 1)
    boss.kill_boss(CHR.Gwyn)
    flag.enable(11512201)  # Enables pact fulfilment flag and gives reward.
    flag.enable(11512203)  # Marks return events in Kiln.

    for knight, active_flag in zip(BlackKnights, BlackKnightActiveFlags):
        skip_if_event_flag_off(4, active_flag)
        chr.disable_gravity(knight)
        chr.disable_collision(knight)
        chr.disable_ai(knight)
        chr.replan_ai(knight)

    wait(3.0)

    for knight, active_flag in zip(BlackKnights, BlackKnightActiveFlags):
        skip_if_event_flag_off(1, active_flag)
        anim.force_animation(knight, 1201, do_not_wait_for_transition=True)

    wait(1.5)  # duration of knight fade out animation
    for knight in BlackKnights:
        chr.disable(knight)

    sound.disable_map_sound(1513805)
    wait(2.0)
    message.status_explanation(10010608, True)  # Gwyn punished, pact with Velka fulfilled.
    wait(7.0)
    warp.warp_player(18, 0, 1800990)


def event11512202():
    """ Black Knights spawn on a loop during Gwyn battle. """
    header(11512202, 0)

    end_if_event_flag_on(11512201)  # End if Gwyn is dead.

    # Wait time depends on Gwyn's health.
    skip_if_event_flag_off(12, 11515361)  # No wait time on first spawn.
    if_entity_health_less_than_or_equal(1, CHR.Gwyn, 0.25)
    skip_if_condition_false(2, 1)
    wait(2.0)
    skip(8)
    if_entity_health_less_than_or_equal(2, CHR.Gwyn, 0.5)
    skip_if_condition_false(2, 2)
    wait(10.0)
    skip(4)
    if_entity_health_less_than_or_equal(3, CHR.Gwyn, 0.75)
    skip_if_condition_false(1, 3)
    wait(15.0)
    wait(20.0)  # 75-100% health

    flag.enable(11515361)  # First spawn is done.
    end_if_event_flag_on(11512201)  # End if Gwyn is dead.

    # Wait for at least one Knight to be inactive.
    if_player_has_special_effect(4, SPEFFECT.GwyneveresRing)
    if_event_flag_range_not_all_on(4, BlackKnightActiveFlags[0], BlackKnightActiveFlags[3])
    if_condition_true(0, 4)

    for knight, active_flag, turn_index in zip(BlackKnights, BlackKnightActiveFlags, range(4)):
        skip_if_event_flag_off(9, BlackKnightTurnFlags[turn_index])  # Skip if not this Knight's turn.
        skip_if_event_flag_on(8, active_flag)  # Skip if this Knight is active.
        warp.short_warp(knight, 'character', CHR.Gwyn, 237)  # seems to be best damipoly.
        wait(3.0)
        chr.enable(knight)
        flag.enable(active_flag)
        flag.disable(BlackKnightTurnFlags[turn_index])
        flag.enable(BlackKnightTurnFlags[(turn_index + 1) % 4])
        anim.force_animation(knight, ANIM.KnightFadeIn)
        restart()

    # If a Knight failed to spawn, increment turn flag.
    for turn_index in range(4):
        skip_if_event_flag_off(3, BlackKnightTurnFlags[turn_index])
        flag.disable(BlackKnightTurnFlags[turn_index])
        flag.enable(BlackKnightTurnFlags[(turn_index + 1) % 4])
        restart()


def event11512210():
    """ Slotted event that watches for Black Knight 'deaths'. """
    header(11512210, 0)
    knight, is_active = define_args('ii')
    if_event_flag_on(1, is_active)
    if_entity_health_less_than_or_equal(1, knight, 0.1)
    if_condition_true(0, 1)
    chr.disable_gravity(knight)
    chr.disable_collision(knight)
    chr.disable_ai(knight)
    chr.replan_ai(knight)
    wait(2.5)
    # Skipping the fade-out, they just get obliterated usually.
    anim.force_animation(knight, 1201, do_not_wait_for_transition=True, wait_for_completion=True)
    chr.enable_ai(knight)
    chr.disable(knight)
    chr.enable_gravity(knight)
    chr.enable_collision(knight)
    chr.set_special_effect(knight, 3231)
    flag.disable(is_active)
    restart()


def event11510450():
    """ Gwyndolin warp. Can now warp forward or backward (after first warp). """
    header(11510450, 1)
    if_does_not_have_tae_event(0, CHR.Gwyndolin, 600)
    if_has_tae_event(0, CHR.Gwyndolin, 600)

    flag.disable_chunk(11515150, 11515151)
    flag.enable_random_in_chunk(11515150, 11515151)
    chr.disable(CHR.Gwyndolin)
    wait(1.0)

    # First two warps are always forward.
    skip_if_event_flag_on(2, 11515110)
    run_event_with_slot(11515110, 0, args=(1512710, 11515110))
    restart()
    skip_if_event_flag_on(2, 11515111)
    run_event_with_slot(11515110, 1, args=(1512711, 11515111))
    restart()

    for warp_number in range(2, 40):
        skip_if_event_flag_on(7, 11515110 + warp_number)

        skip_if_event_flag_on(2, 11515151)
        # Standard forward warp.
        run_event_with_slot(11515110, warp_number, args=(1512710 + warp_number, 11515110 + warp_number))
        skip(2)
        # Backward warp.
        flag.disable(11515110 + warp_number - 1)  # Lose corridor progress.
        run_event_with_slot(11515110, warp_number - 2, args=(1512710 + warp_number - 2, 11515110 + warp_number - 2))

        chr.rotate_to_face_entity(CHR.Gwyndolin, CHR.Player)
        restart()


def event11512500():
    """ Check stable footing for cathedral. """
    header(11512500, 1)
    flag.disable(EVENT.CathedralStableFooting)

    if_event_flag_on(1, EVENT.OrnsteinAndSmoughDead)
    if_event_flag_off(1, EVENT.AnorLondoGwynWarp)
    if_condition_true(0, 1)

    flag.enable(EVENT.CathedralStableFooting)


def event11510200():
    """ Open cathedral doors before Dark Anor Londo. """
    header(11510200, 0)

    skip_if_event_flag_off(3, EVENT.DarkAnorLondo)
    obj.disable(1511001)
    obj.disable(1511000)
    end()

    skip_if_this_event_off(4)
    obj.disable_activation(1511001, -1)
    anim.end_animation(1511000, 0)
    anim.end_animation(1511001, 0)
    end()

    if_action_button_state(0, Category.object, 1511001, 60.0, 102, 1.5, 10010502, ReactionAttribute.all, 0)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_off(1, EVENT.JareelDead)
    skip_if_condition_false(3, 1)
    message.dialog(TEXT.CathedralUnderSiege, ButtonType.yes_no, NumberButtons.no_button, 1511001, 5.0)
    wait(3.0)
    restart()
    warp.short_warp(CHR.Player, Category.object, 1511001, 103)
    anim.force_animation(CHR.Player, 8021)
    anim.force_animation(1511001, 0, wait_for_completion=True)
    anim.force_animation(1511000, 0)


def event11510205():
    """ Open cathedral doors after Dark Anor Londo. """
    header(11510205, 0)

    skip_if_event_flag_on(7, EVENT.DarkAnorLondo)
    obj.disable(1511005)
    obj.disable(1511006)
    if_event_flag_on(0, EVENT.DarkAnorLondo)
    obj.enable(1511005)
    obj.enable(1511006)
    obj.disable(1511000)
    obj.disable(1511001)

    skip_if_event_flag_off(4, 11510206)
    obj.disable_activation(1511006, -1)
    anim.end_animation(1511005, 0)
    anim.end_animation(1511006, 0)
    end()

    if_action_button_state(0, Category.object, 1511006, 60.0, 102, 1.5, 10010502, ReactionAttribute.all, 0)
    skip_if_event_flag_on(3, EVENT.JareelDead)
    message.dialog(TEXT.CathedralUnderSiege, ButtonType.yes_no, NumberButtons.no_button, 1511006, 3.0)
    wait(3.0)
    restart()
    warp.short_warp(CHR.Player, Category.object, 1511006, 103)
    anim.force_animation(CHR.Player, 8021)
    anim.force_animation(1511006, 0, wait_for_completion=True)
    anim.force_animation(1511005, 0)
    flag.enable(11510206)


def event11515492():
    """ Forsaken Knight Ornstein and Sun-Eater Smough trigger. """
    header(11515492, 1)

    chr.disable(CHR.DarkOrnsteinGiant)
    chr.disable(CHR.DarkOrnsteinScion)
    chr.disable(CHR.DarkSmough)

    if_event_flag_on(1, EVENT.OrnsteinAndSmoughDead)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_on(1, EVENT.JareelDead)
    if_event_flag_off(1, EVENT.DarkOrnsteinAndSmoughDead)
    if_event_flag_off(1, EVENT.AnorLondoGwynWarp)
    end_if_condition_false(1)  # No other events use this flag, so safe to end here.

    chr.disable(CHR.DarkwraithInBossRoom)  # Disable and kill Darkwraith in O&S room.
    chr.kill(CHR.DarkwraithInBossRoom, False)

    if_event_flag_off(2, EVENT.AnorLondoGwynWarp)  # Just in case.
    if_player_inside_region(2, REGION.DarkOrnsteinAndSmoughTrigger)
    if_condition_true(0, 2)

    for fog_wall, fog_sfx in zip((1511990, 1511992, 1511988), (1511991, 1511993, 1511989)):
        obj.enable(fog_wall)
        sfx.create_map_sfx(fog_sfx)

    chr.enable(CHR.DarkSmough)
    anim.force_animation(CHR.DarkSmough, 3017)  # fade-in charge.
    wait(4.0)
    boss.enable_boss_health_bar(CHR.DarkSmough, TEXT.DesecraterSmough)
    sound.enable_map_sound(1513800)
    wait(5.0)
    chr.enable(CHR.DarkOrnsteinGiant)
    anim.force_animation(CHR.DarkOrnsteinGiant, 4011)
    boss.enable_boss_health_bar_with_slot(CHR.DarkOrnsteinGiant, 1, TEXT.ForsakenKnightOrnstein)
    chr.ai_instruction(CHR.DarkOrnsteinGiant, 1, 0)
    run_event(11515495)  # Smough in Phase 1.
    run_event(11515493)  # Main/support swapping.
    run_event(11515496)  # Monitor Phase 2 start.

    # Smough fade control.
    run_event_with_slot(11515480, 0, args=(11515470, 3010, 4000, 1.5), arg_types='iiif')  # right to left
    run_event_with_slot(11515480, 1, args=(11515471, 3011, 4001, 1.5), arg_types='iiif')  # left to right
    run_event_with_slot(11515480, 2, args=(11515472, 3012, 4002, 1.5), arg_types='iiif')  # right to left
    run_event_with_slot(11515480, 3, args=(11515473, 3013, 4003, 1.5), arg_types='iiif')  # overhead smash
    run_event_with_slot(11515480, 4, args=(11515474, 3014, 4004, 1.3), arg_types='iiif')  # fast overhead smash
    run_event_with_slot(11515480, 5, args=(11515475, 3015, 4005, 2.0), arg_types='iiif')  # left to right, more reach
    run_event_with_slot(11515480, 6, args=(11515476, 3019, 4009, 2.0), arg_types='iiif')  # short charge
    run_event_with_slot(11515480, 7, args=(11515477, 3017, 4007, 3.0), arg_types='iiif')  # long charge
    run_event_with_slot(11515480, 8, args=(11515478, 3018, 4008, 2.0), arg_types='iiif')  # butt slam
    run_event_with_slot(11515480, 9, args=(11515479, 3016, 4006, 2.0), arg_types='iiif')  # jumping hammer smash


def event11515493():
    """ Switch between Dark Ornstein and Dark Smough main/support roles in Phase 1. """
    header(11515493)

    # End if phase 1 is over.
    end_if_event_flag_on(EVENT.DarkOrnsteinAndSmoughPhaseTwoStarted)

    # SMOUGH IS MAIN.

    # Wait until Smough fades himself out.
    if_does_not_have_tae_event(0, CHR.DarkSmough, 700)
    if_has_tae_event(0, CHR.DarkSmough, 700)
    end_if_event_flag_on(EVENT.DarkOrnsteinAndSmoughPhaseTwoStarted)
    chr.disable_ai(CHR.DarkSmough)  # one-off fading attacks are handled in events.
    chr.disable(CHR.DarkSmough)
    chr.ai_instruction(CHR.DarkOrnsteinGiant, -1, 0)  # Ornstein is main.
    chr.replan_ai(CHR.DarkOrnsteinGiant)

    event.restart_event_id(11515495)
    flag.enable(EVENT.DarkSmoughIsSupport)

    # ORNSTEIN IS MAIN.

    wait_random_seconds(40, 50)  # enough time for 3-4 Smough attacks.
    flag.disable(EVENT.DarkSmoughIsSupport)  # Next Smough appearance will permanently fade him in.
    wait(5.0)

    end_if_event_flag_on(EVENT.DarkOrnsteinAndSmoughPhaseTwoStarted)
    chr.ai_instruction(CHR.DarkOrnsteinGiant, 1, 0)  # Ornstein is support.
    chr.replan_ai(CHR.DarkOrnsteinGiant)

    restart()


def event11515495():
    """ Smough does one-off fade attacks while supporting Ornstein in Phase 1. """
    header(11515495)

    if_event_flag_on(0, EVENT.DarkSmoughIsSupport)

    wait_random_seconds(12, 17)  # Time between intermittent one-off Smough attacks.

    end_if_event_flag_on(EVENT.DarkOrnsteinAndSmoughPhaseTwoStarted)

    flag.disable_chunk(11515470, 11515479)
    if_entity_health_less_than_or_equal(1, CHR.DarkOrnsteinGiant, 0.25)
    skip_if_condition_false(2, 1)
    flag.enable_random_in_chunk(11515470, 11515478)  # Maybe butt slam (3008).
    skip(1)
    flag.enable_random_in_chunk(11515470, 11515477)  # No butt slam.

    restart()


def event11515480():
    """ Ten slots for using random, intermittent Smough attacks while he is supporting in phase 1. """
    header(11515480)
    trigger_flag, fade_in_attack_id, fade_in_out_attack_id, delay = define_args('iiif')

    if_event_flag_on(0, trigger_flag)
    warp.warp(CHR.DarkSmough, Category.character, CHR.Player, 237)
    flag.disable(trigger_flag)
    wait(delay)
    chr.enable(CHR.DarkSmough)

    skip_if_event_flag_on(4, EVENT.DarkSmoughIsSupport)

    # Smough is no longer support; fade him in permanently.
    anim.force_animation(CHR.DarkSmough, fade_in_attack_id, wait_for_completion=True)
    chr.enable_ai(CHR.DarkSmough)
    chr.replan_ai(CHR.DarkSmough)
    restart()

    # Smough is still support; he fades in, attacks, and fades out immediately.
    anim.force_animation(CHR.DarkSmough, fade_in_out_attack_id)
    if_does_not_have_tae_event(0, CHR.DarkSmough, 700)
    if_has_tae_event(0, CHR.DarkSmough, 700)
    chr.disable(CHR.DarkSmough)
    restart()


def event11515496():
    """ Phase 1 ends (Ornstein or Smough dies). """
    header(11515496)

    if_entity_health_less_than_or_equal(1, CHR.DarkOrnsteinGiant, 0.0)
    if_entity_health_less_than_or_equal(2, CHR.DarkSmough, 0.0)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    flag.enable(EVENT.DarkOrnsteinAndSmoughPhaseTwoStarted)
    boss.disable_boss_health_bar_with_slot(CHR.DarkSmough, 0, TEXT.DesecraterSmough)
    boss.disable_boss_health_bar_with_slot(CHR.DarkOrnsteinGiant, 1, TEXT.ForsakenKnightOrnstein)

    skip_if_condition_false_finished(17, 1)

    # SUPER SMOUGH (if Ornstein was killed):

    flag.enable(EVENT.DarkOrnsteinKilledFirst)
    chr.disable_health_bar(CHR.DarkSmough)
    chr.set_special_effect(CHR.DarkSmough, SPEFFECT.HealFull)
    skip_if_event_flag_on(5, EVENT.DarkSmoughIsSupport)
    # Smough is main: force him to fade out with short charge.
    chr.enable_invincibility(CHR.DarkSmough)
    anim.force_animation(CHR.DarkSmough, 3029)
    if_has_tae_event(0, CHR.DarkSmough, 700)
    chr.disable(CHR.DarkSmough)
    chr.disable_invincibility(CHR.DarkSmough)
    flag.disable(EVENT.DarkSmoughIsSupport)
    wait(5.0)
    chr.ai_instruction(CHR.DarkSmough, 1, 0)  # Battle phase up.
    chr.set_special_effect(CHR.DarkSmough, SPEFFECT.SuperDarkSmoughSpeed)
    chr.set_special_effect(CHR.DarkSmough, 7610)  # 1.5x defenses
    boss.enable_boss_health_bar(CHR.DarkSmough, TEXT.SunEaterSmough)
    run_event(11515497)  # Dark Super Smough loop.
    end()

    # SUPER ORNSTEIN (if Smough was killed:).

    flag.enable(EVENT.DarkSmoughKilledFirst)
    wait(3.0)
    warp.warp(CHR.DarkOrnsteinScion, Category.character, CHR.DarkOrnsteinGiant, 3)
    anim.force_animation(CHR.DarkOrnsteinGiant, 4015)
    if_has_tae_event(0, CHR.DarkOrnsteinGiant, 700)
    chr.disable(CHR.DarkOrnsteinGiant)
    chr.enable(CHR.DarkOrnsteinScion)
    anim.force_animation(CHR.DarkOrnsteinScion, 4028, wait_for_completion=True)
    boss.enable_boss_health_bar(CHR.DarkOrnsteinScion, TEXT.OrnsteinLast)

    run_event(11515460)  # Time control.

    if_entity_health_less_than_or_equal(0, CHR.DarkOrnsteinScion, 0.5)
    flag.enable(EVENT.DarkOrnsteinScionAtHalfHealth)

    if_entity_health_less_than_or_equal(0, CHR.DarkOrnsteinScion, 0.25)
    flag.enable(EVENT.DarkOrnsteinScionAtQuarterHealth)
    chr.set_special_effect(CHR.DarkOrnsteinScion, SPEFFECT.SuperDarkOrnsteinRegen)  # One-off regen effect.


def event11515497():
    """ Super Dark Smough loop. """
    header(11515497)

    # Starts disabled.
    if_entity_health_less_than_or_equal(1, CHR.DarkSmough, 0.5)
    skip_if_condition_true(2, 1)
    wait_random_seconds(1, 2)  # longer interval (for healing) above 50% health.
    skip(1)
    wait_random_seconds(0.1, 0.5)

    # End if battle is over.
    end_if_event_flag_on(11512001)

    # Fade back in with a random attack.
    flag.disable_chunk(11515470, 11515479)
    flag.enable_random_in_chunk(11515470, 11515479)  # Any attack.

    # Wait until he fades back out naturally through AI.
    if_does_not_have_tae_event(0, CHR.DarkSmough, 700)
    if_has_tae_event(0, CHR.DarkSmough, 700)
    chr.disable(CHR.DarkSmough)

    restart()


def event11515460():
    """ Ornstein, Void Scion time fluctuation. (Started in 11515496.)

    Levels:
        4650: 5% speed boost
        4651: 10% speed boost
        4652: 15% speed boost
        4653: 20% speed boost
        4654: 25% speed boost
        4655: 20% speed boost
        4656: 15% speed boost
        4657: 10% speed boost
        4658: 5% speed boost
        4659: 0% speed boost
        4660: -5% speed boost
        4661: -10% speed boost
        4662: -15% speed boost
        4663: -20% speed boost
        4664: -25% speed boost
        4665: -20% speed boost
        4666: -15% speed boost
        4667: -10% speed boost
        4668: -5% speed boost
        4669: 0% speed boost
    """
    header(11515460)

    for effect_level in range(20):
        end_if_event_flag_on(EVENT.DarkOrnsteinAndSmoughDead)
        chr.set_special_effect(CHR.Player, 4650 + effect_level)
        chr.set_special_effect(CHR.DarkOrnsteinScion, 4650 + effect_level)

        skip_if_event_flag_on(2, EVENT.DarkOrnsteinScionAtQuarterHealth)
        wait_random_seconds(1, 5)
        skip(4)
        skip_if_event_flag_on(2, EVENT.DarkOrnsteinScionAtHalfHealth)
        wait_random_seconds(3, 7)
        skip(1)
        wait_random_seconds(5, 9)

        chr.cancel_special_effect(CHR.Player, 4650 + effect_level)
        chr.cancel_special_effect(CHR.DarkOrnsteinScion, 4650 + effect_level)

    restart()


def event11512001():
    """ (End of battle) Forsaken Knight Ornstein and Sun-Eater Smough die. """
    header(11512001)
    end_if_this_event_on()

    if_event_flag_on(1, EVENT.DarkOrnsteinKilledFirst)  # Ornstein died first.
    if_entity_health_less_than_or_equal(1, CHR.DarkSmough, 0.0)
    if_condition_true(-1, 1)
    if_event_flag_on(2, EVENT.DarkSmoughKilledFirst)  # Smough died first.
    if_entity_health_less_than_or_equal(2, CHR.DarkOrnsteinScion, 0.0)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    chr.cancel_special_effect(CHR.DarkOrnsteinScion, 4950)  # Make his death animation normal speed.

    item.award_item_to_host_only(ITEMLOT.DarkOrnsteinAndSmoughReward)
    skip_if_condition_false_finished(3, 2)
    item.award_item_to_host_only(ITEMLOT.DarkOrnsteinScionReward)
    boss.kill_boss(CHR.DarkOrnsteinScion)
    skip(1)
    boss.kill_boss(CHR.DarkSmough)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)
    boss.disable_boss_health_bar(CHR.DarkSmough, TEXT.SunEaterSmough)
    boss.disable_boss_health_bar(CHR.DarkOrnsteinGiant, TEXT.ForsakenKnightOrnstein)

    for fog_wall, fog_sfx in zip((1511990, 1511992, 1511988), (1511991, 1511993, 1511989)):
        obj.disable(fog_wall)
        sfx.delete_map_sfx(fog_sfx, True)

    flag.enable(EVENT.DarkOrnsteinAndSmoughDead)
    wait(3.0)
    sound.disable_map_sound(1513800)


def event11510531():
    """ Darkmoon Knightess changes state when you obtain the Lordvessel. """
    header(11510531)
    darkmoon_knightess, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1033)
    if_event_flag_on(1, 1030)
    if_event_flag_on(1, EVENT.LordvesselReceived)
    if_entity_alive(1, darkmoon_knightess)
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)


def event11515392():
    """ Ornstein and Smough trigger (or cleanup if dead). Now disables AI of archer outside fog. """
    header(11515392, 1)

    skip_if_event_flag_off(9, EVENT.OrnsteinAndSmoughDead)
    chr.disable(CHR.Ornstein)
    chr.disable(CHR.SuperOrnstein)
    chr.disable(CHR.Smough)
    chr.disable(CHR.SuperSmough)
    chr.kill(CHR.Ornstein, False)
    chr.kill(CHR.SuperOrnstein, False)
    chr.kill(CHR.Smough, False)
    chr.kill(CHR.SuperSmough, False)
    end()

    chr.disable(CHR.SuperOrnstein)
    chr.disable(CHR.SuperSmough)
    chr.disable_backread(CHR.SuperOrnstein)
    skip_if_event_flag_on(1, 11510000)
    chr.disable(CHR.Ornstein)  # Disable default Ornstein for cutscene.
    chr.disable_ai(CHR.Ornstein)
    chr.disable_ai(CHR.Smough)
    if_event_flag_on(1, 11515393)
    if_player_inside_region(1, 1512990)
    if_condition_true(0, 1)

    skip_if_event_flag_on(8, 11510000)
    skip_if_multiplayer(2)
    cutscene.play_cutscene_to_player(150140, CutsceneType.skippable, CHR.Player)
    skip(1)
    cutscene.play_cutscene_to_player(150140, CutsceneType.unskippable, CHR.Player)
    wait_frames(1)
    chr.enable(CHR.Ornstein)
    chr.enable(CHR.Smough)
    flag.enable(11510000)

    chr.disable_ai(CHR.SilverKnightArcherNearBossFog)
    chr.enable_ai(CHR.Ornstein)
    chr.enable_ai(CHR.Smough)
    boss.enable_boss_health_bar_with_slot(CHR.Ornstein, 1, 5270)
    boss.enable_boss_health_bar_with_slot(CHR.Smough, 0, 2360)


def event11512008():
    """ Message informs you that Thrall has climbed higher when it disappears or you return after dying. """
    header(11512008)
    end_if_this_event_on()
    if_event_flag_on(1, 11512060)  # Ambush done.
    if_event_flag_on(1, EVENT.CapriciousThrallActive)  # Thrall still active (e.g. Archive appearance not done).
    if_event_flag_off(1, EVENT.ThrallAmbushOngoing)
    if_player_inside_region(1, REGION.CapriciousThrallTrigger)
    if_condition_true(0, 1)
    message.status_explanation(TEXT.ThrallHasFled)


def event11512043():
    """ Monitor resting at Sun Chamber bonfire. """
    header(11512043)
    if_player_within_distance(1, 1511950, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11512043)


def event11512044():
    """ Monitor resting at Gwyn's Altar bonfire. """
    header(11512044)
    if_player_within_distance(1, 1511962, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11512044)


def event11510525():
    """ Giant Blacksmith dies. """
    header(11510525)
    giant_blacksmith, giant_blacksmith_angry, first_flag, last_flag, new_flag = define_args('iiiii')

    skip_if_this_event_slot_off(2)
    chr.drop_mandatory_treasure(giant_blacksmith)
    end()

    if_entity_health_less_than_or_equal(-1, giant_blacksmith, 0.0)
    if_entity_health_less_than_or_equal(-1, giant_blacksmith_angry, 0.0)
    if_condition_true(0, -1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)


def event11510870():
    """ Enemy doesn't respawn and drops mandatory loot. """
    header(11510870, 1)
    npc, = define_args('i')
    skip_if_this_event_slot_off(2)
    chr.drop_mandatory_treasure(npc)
    end()

    if_entity_dead(0, npc)
    end()


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
