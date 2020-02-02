
import sys
import inspect
from pydses import *

map_name = 'm12_01_00_00'  # Oolacile Sanctuary / Royal Woods / Oolacile Township / Chasm of the Abyss (DLC)
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11210000
BASE_PART = 1210000

"""
New events and event flags:
0006:   EVENT   Moved Sanctuary Guardian dies.
0007:   EVENT   Twilight Vagrant dies.
2000:   EVENT   Updates your spawn point when you warp to Oolacile so you can't die/Bone to get out.
2001:   EVENT   Portal appears over Manus's grave after he dies or corrupts Artorias.
2002:   FLAG    Tells New Londo Ruins to warp you to the arrival point.
2003:   FLAG    Sif/Artorias/Manus encounter is complete.   
2004:   EVENT   Control appearance of prison fog on first arrival in Early Oolacile.
2005:   EVENT   Switch to darker light map in Early Oolacile.
2006:   FLAG    Manus is genuinely dead in Chasm (not Early Oolacile). Tells Common events to award Soul of Manus.
2007:   EVENT   Twilight Vagrant chooses its next phantom (first half).
2008:   EVENT   Twilight Vagrant chooses its next phantom (second half).
2009:   FLAG    Twilight Vagrant's Oscar phantom has been defeated once (health bar triggered).
2010:   EVENT   Twilight Vagrant might appear.
2025:   FLAG    Second half of choice sub-event has finished.
2026:   FLAG    Vagrant chance appearance sub-event has finished.

2011:   
-       FLAGS   One is randomly enabled every cycle to determine the next Twilight Vagrant phantom.
2023:   

2031:   
-       FLAGS   Record LAST phantom to appear in the Vagrant fight..
2043:

2050:   EVENT   Common event that converts various 'character dead' flags to the contiguous range below.

2051:   
-       FLAGS   Contiguous copies of 'dead' flags that allow the corresponding character in the Twilight Vagrant fight.
2063:

"""


class DEBUG(IntEnum):
    EARLY_VISIT = False
    DUSK_KIDNAPPED = False
    SANCTUARY_GUARDIAN_DEAD = False
    ARTORIAS_DEAD_GONE = False
    ALL_TWILIGHT_PHANTOMS_ON = False
    GET_LIGHT_SOURCES = False
    GET_SOUL_OF_ARTORIAS = False
    ABYSS_ARTORIAS_DEAD = False
    KALAMEET_SHOT_DOWN = False


class CHR(IntEnum):
    Player = 10000
    HawkeyeGough = 6720
    Ciaran = 6740
    YoungAlvina = 6760
    ArtoriasBoss = 1210820
    ArtoriasFighting = 1210825
    SifProtected = 1210502
    Manus = 1210840
    KalameetBridge = 1210400
    KalameetBoss = 1210401
    KalameetAirborne = 1210402
    WarpRotateEntity = 1210826
    SanctuaryGuardian = 1210800
    SanctuaryGuardianTail = 1210810
    SanctuaryGuardianTwinOne = 1210801
    SanctuaryGuardianTwinTwo = 1210802
    SanctuaryGuardianMoved = 1210803
    TwilightVagrant = 1210850
    TwilightOscar = 1210851
    TwilightGough = 1210852
    TwilightArtorias = 1210853
    TwilightLogan = 1210854
    TwilightGriggs = 1210855
    TwilightSolaire = 1210856
    TwilightLaurentius = 1210857
    TwilightCrestfallen = 1210858
    TwilightLautrec = 1210859
    TwilightShiva = 1210860
    TwilightPatches = 1210861
    TwilightHavel = 1210862
    TwilightCiaran = 1210863


TwilightPhantoms = [
    1210851,  # Oscar
    1210852,  # Logan
    1210853,  # Griggs
    1210854,  # Solaire
    1210855,  # Laurentius
    1210856,  # Crestfallen
    1210857,  # Lautrec
    1210858,  # Shiva
    1210859,  # Patches
    1210860,  # Havel
    1210861,  # Ciaran
    1210862,  # Gough
    1210863,  # Artorias
]


class ANIM(IntEnum):
    FadeIn = 6
    FadeOut = 7
    PlayerSpawn = 6950
    TouchWall = 7114
    ArtoriasLeapFade = 3105
    ArtoriasPossession = 3113
    ManusPossession = 3112
    SifDisappears = 7010


class ITEMLOT(IntEnum):
    CovenantOfArtorias = 1630


class OBJECT(IntEnum):
    EarlyFog = 1211875


class GOOD(IntEnum):
    SoulOfArtorias = 710


class SFX(IntEnum):
    EarlyFog = 1211876
    ManusPortal = 1213675


class REGION(IntEnum):
    EarlyArrival = 1212675  # Just in front of Chasm cell bonfire.
    CloseToPrisonFog = 1212676  # Tells you about prison fog ('sealed by dark').
    TwilightVagrantFirstTrigger = 1212682
    TwilightVagrantNormalTrigger = 1212683
    EarlySorcerer0Warp = 1212684
    EarlyBloathead6Warp = 1212685
    EarlyBloathead20Warp = 1212686
    EarlySorcerer9Warp = 1212687
    EarlyBloathead21Warp = 1212688
    EarlySorcerer7Warp = 1212689
    EarlyBloathead15Warp = 1212690


class TEXT(IntEnum):
    AbyssPrisonFog = 10010177


class EVENT(IntEnum):
    SanctuaryGuardianDead = 11210000
    ArtoriasDeadOrGone = 11210001  # Meaning disambiguated with Early Oolacile flag.
    ManusDeadOrGone = 11210002
    MovedSanctuaryGuardianDead = 11210006
    EarlyOolacile = 11200007  # Event from activating the tunnel portal with Broken Pendant (and not Lordvessel).
    NewLondoWarp = 11212002
    SifRescued = 11212003  # Event battle is complete.
    AwardManusSoul = 11212006  # Manus killed in Late Oolacile, awards Soul of Manus.
    TwilightVagrantDead = 11212008
    KalameetShotDown = 11210592
    KalameetDead = 11210004
    TwilightFirstEncounterDone = 11212009
    TwilightPhantomSearching = 11215502
    ReflectingPoolStableFooting = 11212501
    HippodromeStableFooting = 11212506


def event0():
    header(0, 0)

    if DEBUG.EARLY_VISIT:
        flag.enable(EVENT.EarlyOolacile)
    if DEBUG.DUSK_KIDNAPPED:
        flag.disable_chunk(1120, 1139)
        flag.enable(1127)
    if DEBUG.SANCTUARY_GUARDIAN_DEAD:
        flag.enable(11210000)
    if DEBUG.ARTORIAS_DEAD_GONE:
        flag.enable(11210001)
    if DEBUG.ALL_TWILIGHT_PHANTOMS_ON:
        flag.enable(11212051)  # Oscar (friendly, in tutorial - can't be missed)
        flag.enable(11212052)  # Big Hat Logan (any time)
        flag.enable(11212053)  # Griggs (any time)
        flag.enable(11212054)  # Solaire (any time)
        flag.enable(11212055)  # Laurentius (any time)
        flag.enable(11212056)  # Crestfallen Warrior (any time)
        flag.enable(11212057)  # Lautrec (any time, including invasion)
        flag.enable(11212058)  # Shiva (any time)
        flag.enable(11212059)  # Patches (any time)
        flag.enable(11212060)  # Havel (any time - doesn't count his disappearance at Ash Lake)
        flag.enable(11212061)  # Ciaran (in Oolacile and/or with Nito)
        flag.enable(11212062)  # Gough (any time)
        flag.enable(11212063)  # Artorias (in Darkroot)
    if DEBUG.GET_LIGHT_SOURCES:
        item.award_item_to_host_only(34800100)  # Sorcerer's Catalyst
        item.award_item_to_host_only(1010514)  # Cast Light
        item.award_item_to_host_only(1310090)  # Skull Lantern
    if DEBUG.GET_SOUL_OF_ARTORIAS:
        item.award_item_to_host_only(2540)
    if DEBUG.ABYSS_ARTORIAS_DEAD:
        flag.enable(5)
    if DEBUG.KALAMEET_SHOT_DOWN:
        flag.enable(EVENT.KalameetShotDown)
        flag.enable(11210535)

    run_event(11210700)
    skip_if_client(10)
    for fog, sfx_id in zip((988, 994, 996, 998, 986), (989, 995, 997, 999, 987)):
        obj.disable(1211000 + fog)
        sfx.delete_map_sfx(1211000 + sfx_id, False)

    run_event(11212004)  # (New) Disable "early fog" that traps you in Chasm unless early Manus encounter isn't done.
    run_event(11212005)  # (New) Switch to darker light map in Early Oolacile.
    # NOTE: Arrival script removed, spawn point simply changed when portal is touched in Darkroot (and no animation).
    run_event(11212001)  # (New) Portal after Manus fight.
    run_event(11212501)  # (New) Reflecting Pool stable footing.
    run_event(11212084)  # (New) Monitor warping to Hippodrome.

    hitbox.disable_hitbox(1213061)
    skip_if_event_flag_off(2, 11210539)
    hitbox.enable_hitbox(1213061)
    hitbox.disable_hitbox(1213060)

    # Gravelord events.
    run_event(11215090)
    run_event(11215091)
    run_event(11215092)

    # SANCTUARY GUARDIAN / TWILIGHT VAGRANT

    sound.disable_map_sound(1213800)  # Sanctuary Guardian.
    sound.disable_map_sound(1213804)  # Twilight Vagrant.

    skip_if_event_flag_off(8, EVENT.EarlyOolacile)
    run_event(11210007)
    skip_if_event_flag_on(1, EVENT.TwilightVagrantDead)
    run_event(11215080)
    obj.disable(1211790)
    sfx.delete_map_sfx(1211791, False)
    obj.disable(1211792)
    sfx.delete_map_sfx(1211793, False)
    skip(16)

    run_event(11210007)  # Disables Twilight Vagrant and all phantoms.

    skip_if_event_flag_off(6, EVENT.SanctuaryGuardianDead)
    run_event(11210000)
    obj.disable(1211790)
    sfx.delete_map_sfx(1211791, False)
    obj.disable(1211792)
    sfx.delete_map_sfx(1211793, False)
    skip(8)

    run_event(11215000)  # Host enters fog.
    run_event(11215001)  # Client enters fog.
    run_event(11215002)  # Host has started boss fight. (Note proper order of these numbers now.)
    run_event(11215003)  # Boss behavior.
    run_event(11215004)  # Music on.
    run_event(11215005)  # Music off.
    run_event(11210000)  # Boss dies.
    # Tail cut events. Note that only the first of these (the boss's) is skipped if the boss is dead.
    for slot, args in enumerate(zip((1210810, 1210811, 1210812),
                                    (1210800, 1210801, 1210802),
                                    (34720000, 34720010, 34720020))):
        run_event_with_slot(11215006, slot, args=args)
    # Two respawning lesser Sanctuary Guardians appear in the arena after Artorias dies, in Late Oolacile.

    run_event(11215007)  # Lesser Guardians reposition themselves based on your initial spawn location.
    run_event(11215008)  # Lesser Guardians are triggered when player enters the arena.
    run_event(11215009)  # Lesser Guardians update their nest depending on which side of the arena you leave.

    # KNIGHT ARTORIAS / (NEW) SANCTUARY GUARDIAN

    sound.disable_map_sound(1213801)  # Knight Artorias music.
    sound.disable_map_sound(1213805)  # Moved Sanctuary Guardian music.

    # EARLY OOLACILE (Moved Sanctuary Guardian)
    skip_if_event_flag_off(12, EVENT.EarlyOolacile)

    obj.disable(1211100)  # Bloathead thrown by Artorias...
    obj.disable(1211101)  # ...and its blood trail.

    # Moved Sanctuary Guardian already dead:
    skip_if_event_flag_off(8, EVENT.MovedSanctuaryGuardianDead)
    run_event(11210006)
    obj.disable(1211890)
    sfx.delete_map_sfx(1211891, False)
    obj.disable(1211892)
    sfx.delete_map_sfx(1211893, False)
    hitbox.disable_hitbox(1213001)
    map.register_bonfire(11210968, 1211962)  # (New) Royal Hippodrome.
    skip(21)  # Skips over all battle events.

    skip(10)  # Otherwise, skips Artorias-already-dead setup.

    # LATE OOLACILE (Knight Artorias)
    # Artorias already dead:
    chr.disable(CHR.SanctuaryGuardianMoved)
    skip_if_event_flag_off(8, EVENT.ArtoriasDeadOrGone)
    run_event(11210001)
    obj.disable(1211890)
    sfx.delete_map_sfx(1211891, False)
    obj.disable(1211892)
    sfx.delete_map_sfx(1211893, False)
    hitbox.disable_hitbox(1213001)
    map.register_bonfire(11210968, 1211962)  # (New) Royal Hippodrome.
    skip(10)

    run_event(11215010)  # Host enters fog.
    run_event(11215011)  # Client enters fog.
    run_event(11215012)  # Host has started boss fight.
    run_event(11215013)  # Boss behavior.
    run_event(11215014)  # Music on.
    run_event(11215015)  # Music off.
    skip_if_event_flag_off(2, EVENT.EarlyOolacile)
    run_event(11210006)  # Sanctuary Guardian dies.
    skip(1)
    run_event(11210001)  # Knight Artorias dies.

    # MANUS, FATHER OF THE ABYSS

    sound.disable_map_sound(1213802)
    skip_if_event_flag_off(4, EVENT.ManusDeadOrGone)
    run_event(11210002)
    obj.disable(1211990)
    sfx.delete_map_sfx(1211991, False)
    skip(8)
    run_event(11215020)  # Host enters fog.
    run_event(11215021)  # Client enters fog.
    run_event(11215022)  # Host has started boss fight. Note that this only requires you to be in the arena.
    run_event(11215027)  # Manus pulls you down into the arena.
    run_event(11215023)  # Boss behavior.
    run_event(11215024)  # Music on.
    run_event(11215025)  # Music off.
    run_event(11210002)  # Boss dies.

    run_event(11215026)  # Player is invincible while falling into the arena (only once between rests!).

    # (New) Encounter between Artorias, Sif, and Manus in early Oolacile. Takes care of itself.
    run_event(11215028)  # (New) Artorias and Sif appear in the arena.

    # BLACK DRAGON KALAMEET

    sound.disable_map_sound(1213803)
    if_event_flag_on(1, EVENT.KalameetShotDown)
    if_event_flag_off(1, EVENT.KalameetDead)
    skip_if_condition_true(3, 1)  # Fog is disabled until Kalameet is shot down by Hawkeye Gough.
    obj.disable(1211690)
    sfx.delete_map_sfx(1211691, False)
    hitbox.disable_hitbox(1213001)  # Not sure what this is. Something related to the fog.
    skip_if_event_flag_on(8, EVENT.KalameetDead)
    run_event(11215060)  # Host enters fog.
    run_event(11215061)  # Client enters fog.
    run_event(11215062)  # Host has started boss fight.
    run_event(11215063)  # Boss behavior.
    run_event(11215064)  # Music on.
    run_event(11215066)  # Some kind of delay (75f) for client music, with a duplicate fog entry activation.
    run_event(11215065)  # Music off.
    run_event(11210005)  # Boss dies. (Marked by 11210004, because you can also kill flying Kalameet.)

    skip_if_event_flag_off(1, EVENT.ManusDeadOrGone)
    map.register_bonfire(11210992, 1211950)  # Bonfire after defeating Manus.
    skip_if_event_flag_on(2, EVENT.EarlyOolacile)
    map.register_bonfire(11210984, 1211963)  # First bonfire before Sanctuary Guardian. Not enabled in Early Oolacile.
    skip(2)
    chr.disable(1210963)
    obj.disable(1211963)
    map.register_bonfire(11210976, 1211961)  # Oolacile Sanctuary (near Elizabeth).
    map.register_bonfire(11210960, 1211964)  # Prison cell bonfire before Chasm.

    map.register_ladder(11210210, 11210211, 1211110)
    map.register_ladder(11210212, 11210213, 1211111)
    map.register_ladder(11210214, 11210215, 1211112)

    run_event(11212000)  # (New) Remove a few Township enemies in early Oolacile after shortcut elevator is unlocked.

    # (New) Royal Wood enemy triggers.
    for slot, (standby_enemy, distance) in enumerate(zip(range(1210100, 1210111), [5.0] * 11)):
        # Enemies cancel out of standby animation based on distance.
        run_event_with_slot(11215100, slot, args=(standby_enemy, distance), arg_types='if')
    run_event_with_slot(11215100, 11, args=(1210154, 8.0), arg_types='if')  # Stone Guardian.

    # (New) Two Stone Guardians above flower field have their nest changed to the field when they drop in.
    run_event_with_slot(11215115, 0, args=(1210152, 1212502, 1212501))
    run_event_with_slot(11215115, 1, args=(1210153, 1212502, 1212501))

    for slot, (plowing_scarecrow, distance) in enumerate(zip(range(1210120, 1210127), [10.0] * 7)):
        # Scarecrows plow and rest until triggered by distance.
        run_event_with_slot(11215120, slot, args=(plowing_scarecrow, distance), arg_types='if')

    # Three Scarecrows cutting the trees aggroed when you pick up the item nearby (Gold Coin).
    run_event_with_slot(11215130, 0, args=(1210115, 1210116, 1210117, 51210030))
    # Stone Guardians survey their surroundings while patrolling the cliff.
    run_event_with_slot(11215140, 0, args=(1210150, 1212503))
    run_event_with_slot(11215140, 1, args=(1210151, 1212523))
    # (NEW) Stone Guardians or pairs of Stone Guardians drop pieces of Guardian set when first killed.
    run_event(11212110)  # Helm (patrol)
    run_event(11212111)  # Armor (flower field)
    run_event(11212112)  # Gauntlets (pond)
    run_event(11212113)  # Leggings (lookout, only one)

    # Kalameet logic (not directly including boss battle).
    run_event(11210050)  # Kalameet lands on the bridge.
    run_event(11210051)  # Kalameet arrives at the basin when you first get there.
    run_event(11210052)  # Outcomes of fire breathing. Including death flag (see below) at 1% health.
    run_event(11210053)  # Kalameet dies if flag 11210063 is enabled.
    run_event(11210054)  # More Kalameet animation control, related to fire breathing (flag 65 off, 64 on).
    run_event(11210055)  # "Near" version of above animation control.
    run_event(11210056)  # "Flying near forest of Kaba." More fire animations.
    run_event(11210057)  # Some kind of bizarre flag switch system for Kalameet.
    run_event(11210040)  # Kalameet "monitoring Forest" (far, host).
    run_event(11210041)  # Kalameet "monitoring Forest" (near, host).
    run_event(11210042)  # Kalameet "monitoring Forest" (far, client).
    run_event(11210043)  # Kalameet "monitoring Forest" (near, client).
    run_event(11210004)  # Kalameet dies (version 401 or 402).
    run_event(11215050)  # Kalameet "wall control". I assume this stops him screwing up near the arena wall.
    run_event(11215051)  # Kalameet tail setup.
    run_event(11215052)  # Kalameet tail cut enable/disable.

    # (New) Protected Sif has moved to the Artorias/Manus encounter, but otherwise behaves the same. There's no summon.
    run_event(11210025)  # Destroy illusory wall to secret Sif location.
    run_event(11210021)  # Control behavior of protected Sif.
    run_event(11210020)  # Sif disappears if Manus is defeated, or dies and displays a message.
    run_event(11215043)  # Sif weakens below 30% health.
    run_event(11215044)  # Sif summon sign.

    # Treasure chests (five).
    for (slot, arg1, arg2) in zip((0, 1, 2, 4, 5), (600, 601, 602, 604, 605), (600, 601, 602, 604, 605)):
        if arg1 == 600:
            skip_if_event_flag_on(1, EVENT.EarlyOolacile)  # Pond chest not present in Early Oolacile.
        run_event_with_slot(11210600, slot, args=(1211000 + arg1, 11210000 + arg2))
    # Hanging treasure corpses.
    run_event_with_slot(11210230, 0, args=(1211210, 1211650, 125, 126))

    # Non-respawning enemies (all Crystal Lizards).
    for slot, (arg1, arg2) in enumerate(zip(range(200, 205), (7200, 7000, 7100, 7300, 7100))):
        run_event_with_slot(11210350, slot, args=(1210000 + arg1, 33000000 + arg2))
    run_event_with_slot(11210350, 5, args=(1210260, 41601000))  # Bloathead Sorcerer who drops "sorry" carving.
    run_event_with_slot(11210350, 6, args=(1210691, 0))  # Chained Prisoner 1.
    run_event_with_slot(11210350, 7, args=(1210660, 0))  # Chained Prisoner 2.
    run_event_with_slot(11210350, 8, args=(1210661, 0))  # Chained Prisoner 3.

    # Elevators. Elevators 0, 2, and 3 operate in reverse in Early Oolacile.
    run_event(11210100)  # Elevator 0 (Township shortcut)
    run_event(11210103)  # Elevator 0 (Township shortcut) first activation
    run_event(11210110)  # Elevator 1 (from Royal Wood down to stadium, first to be used, fine as is).
    run_event(11210112)  # Elevator 1 (from Royal Wood down to stadium) has been used
    run_event(11210120)  # Elevator 2 (from Chester back up to first half of Royal Wood)
    run_event(11210123)  # Elevator 2 (from Chester back up to first half of Royal Wood) first activation
    run_event(11210130)  # Elevator 3 (from Chasm back to Chester)
    run_event(11210133)  # Elevator 3 (from Chasm back to Chester) first activation
    run_event(11210140)  # Elevator 4 (into Chasm prison cell, fine as is)
    run_event(11210150)  # Moves Bloathead onto the prison elevator in Late Oolacile if you haven't used it yet.
    run_event(11210151)  # (New) Moves dog onto the Wood elevator in Early Oolacile if you haven't used it yet.
    # I think this makes invisible barriers prevent enemies from reaching elevators. Leaving it.
    for slot, (arg1, arg2, arg3) in enumerate(zip(range(5), range(5), (105, 115, 125, 135, 145))):
        run_event_with_slot(11210170, slot, args=(11215220 + arg1, 1213050 + arg2, 1212000 + arg3))

    # (New) Change initial elevator positions in Early Oolacile.
    skip_if_event_flag_off(2, EVENT.EarlyOolacile)
    skip_if_event_flag_on(1, 11210103)
    flag.enable(11210101)
    skip_if_event_flag_off(2, EVENT.EarlyOolacile)
    skip_if_event_flag_on(1, 11210123)
    flag.enable(11210121)
    skip_if_event_flag_off(2, EVENT.EarlyOolacile)
    skip_if_event_flag_on(1, 11210133)
    flag.enable(11210131)

    # Light-triggered illusory wall.
    sound.disable_map_sound(1213810)
    sound.disable_map_sound(1213811)
    # Walls disappear when the player has light.
    run_event_with_slot(11210200, 0, args=(1211200, 1212200))
    run_event_with_slot(11210200, 1, args=(1211201, 1212201))
    # Play sound effects near wall.
    run_event_with_slot(11210205, 0, args=(1211200, 1212200, 11210200))
    run_event_with_slot(11210205, 1, args=(1211201, 1212201, 11210201))

    run_event(11210300)  # Unlock Hawkeye Gough's door with Crest Key (no Master Key).

    # Objects in Manus's arena are destroyed (including when he dies).
    for slot, (arg1, arg2) in enumerate(zip(range(1300, 1324), range(3160, 3184))):
        run_event_with_slot(11215250, slot, args=(1210000 + arg1, 1210000 + arg2))

    # Mimics.
    run_event_with_slot(11215160, 0, args=(1210600,))
    run_event_with_slot(11215165, 0, args=(1210600,))
    run_event_with_slot(11215170, 0, args=(1210600,))
    run_event_with_slot(11215175, 0, args=(1210600,))
    run_event_with_slot(11215180, 0, args=(1210600, 1212180))
    run_event_with_slot(11210680, 0, args=(1210600,))
    run_event_with_slot(11215185, 0, args=(1210600,))
    chr.set_network_update_rate(1210601, True, CharacterUpdateRate.always)
    run_event_with_slot(11215160, 1, args=(1210601,))
    run_event_with_slot(11215165, 1, args=(1210601,))
    run_event_with_slot(11215170, 1, args=(1210601,))
    run_event_with_slot(11215175, 1, args=(1210601,))
    run_event_with_slot(11215180, 1, args=(1210601, 1212181))
    run_event_with_slot(11210680, 1, args=(1210601,))
    run_event_with_slot(11215185, 1, args=(1210601,))
    run_event_with_slot(11215160, 2, args=(1210602,))
    run_event_with_slot(11215165, 2, args=(1210602,))
    run_event_with_slot(11215170, 2, args=(1210602,))
    run_event_with_slot(11215175, 2, args=(1210602,))
    run_event_with_slot(11215180, 2, args=(1210602, 1212182))
    run_event_with_slot(11210680, 2, args=(1210602,))
    run_event_with_slot(11215185, 2, args=(1210602,))


def event50():
    """ NPC constructor. """
    header(50, 0)

    run_event(11212100)  # (New) Control enemy appearance between early and late Oolacile.

    # MARVELLOUS CHESTER (INVASION)

    run_event_with_slot(11215030, 0, args=(6731, 11215035, 11210900, 1212080, 1212081, 1))  # Early.
    run_event_with_slot(11215030, 1, args=(6732, 11215036, 11210901, 1212082, 1212083, 0))  # Late.
    # Chester reappears as merchant after invader is killed.
    run_event_with_slot(11210900, 0, args=(6731,))
    run_event_with_slot(11210900, 1, args=(6732,))
    # Chester reappears as merchant after invader gives up.
    run_event_with_slot(11210905, 0, args=(6731, 11215035, 1212080, 1213030, 11210900))
    run_event_with_slot(11210905, 1, args=(6732, 11215036, 1212082, 1213031, 11210901))

    # HAWKEYE GOUGH

    run_event_with_slot(11210510, 0, args=(CHR.HawkeyeGough, 1822))  # Hostile
    run_event_with_slot(11210520, 0, args=(CHR.HawkeyeGough, 1820, 1839, 1823))  # Dead
    run_event_with_slot(11210530, 0, args=(CHR.HawkeyeGough, 1820, 1839, 1821))  # Crest Key open
    run_event(11210535)  # Gough shoots down Kalameet
    run_event(11210910)  # Gough hostile AI
    run_event(11210912)  # Gough detects where you are when hostile
    run_event(11210915)  # Gough returns upstairs when hostile

    # MARVELLOUS CHESTER (NPC)

    skip_if_event_flag_off(2, 1842)
    obj.disable(1211130)  # Light source gone when Chester killed.
    sfx.delete_map_sfx(1213150, False)
    run_event_with_slot(11210510, 1, args=(6730, 1841))  # Hostile
    run_event_with_slot(11210520, 1, args=(6730, 1840, 1859, 1842))  # Dead
    run_event(11210544)  # Destroy light source near Chester.

    # ELIZABETH

    run_event(11210538)  # Spawn treasure if dead.
    run_event_with_slot(11210520, 2, args=(6750, 1870, 1889, 1872))  # Dead

    # LORD'S BLADE CIARAN

    # Ciaran (and Artorias's gravestone) now appear in the Sanctuary. You can only give her the Soul of Artorias if you
    # go to Early Oolacile. Knight Artorias drops ten Humanity instead of his Soul. (If I ever figure out/bother to
    # go into her EzState and change the item IDs, I can have her accept the corrupted Soul, but it seems pointless.)

    skip_if_event_flag_on(1, 11210001)
    obj.disable(1211220)  # Artorias's gravestone.
    skip_if_event_flag_on(1, 1861)
    chr.disable(CHR.Ciaran)  # Ciaran appears only if 1861 is active.
    run_event_with_slot(11210510, 3, args=(CHR.Ciaran, 1863))  # Hostile
    run_event_with_slot(11210520, 3, args=(CHR.Ciaran, 1860, 1869, 1864))  # Dead
    # Ciaran appears if you have the Soul of Artorias.
    run_event_with_slot(11210531, 0, args=(CHR.Ciaran, 1860, 1869, 1861))
    # Player gives Ciaran the Soul of Artorias (dialogue flag 11210590).
    run_event_with_slot(11210532, 0, args=(CHR.Ciaran, 1860, 1869, 1862))
    # Player *twice* refuses to give Soul of Artorias to Ciaran (dialogue flag 11210591). She disappears on de-load.
    run_event_with_slot(11210534, 0, args=(CHR.Ciaran, 1860, 1869, 1865))
    # Ciaran nest change during battle.
    run_event(11210543)

    # DUSK OF OOLACILE

    chr.disable(6700)
    skip_if_client(3)
    run_event(11210540)  # Dusk appears after killing Manus.
    run_event(11210541)  # Dusk is killed after defeating Manus. Also kills Elizabeth.
    run_event(11210542)  # Dusk reacts to being attacked.

    # YOUNG ALVINA (Early only, before Manus event)

    skip_if_event_flag_on(1, 11210345)  # After all three appearances are done, she won't appear again.
    flag.disable_chunk(11210340, 11210345)  # She will return to first position on map reload (if not finished).
    chr.disable_gravity(CHR.YoungAlvina)
    chr.enable_immortality(CHR.YoungAlvina)
    chr.disable_health_bar(CHR.YoungAlvina)
    chr.set_special_effect(CHR.YoungAlvina, 5300)
    run_event(11210340)  # First appearance.
    run_event(11210341)  # Second appearance.
    run_event(11210345)  # Third appearance.

    # Miscellaneous
    obj.enable_invulnerability(1211250)  # Illusory ground.
    run_event(11210346)  # Player is invincible during secret fall.
    run_event(11210347)  # Ground disappears for secret fall.
    anim.end_animation(1211606, 0)  # No idea what these two are.
    anim.end_animation(1211607, 0)
    run_event(11217000)  # Switch nest of two Sanctuary Guardians "immediately after loading".
    run_event(11210015)  # Gough only loads if you're within 80 distance units of him and Artorias is dead.


def event11215010():
    """ Enter Moved Sanctuary Guardian fog. """
    header(11215010, 1)
    if_host(1)
    skip_if_event_flag_off(5, EVENT.EarlyOolacile)
    # Sanctuary Guardian: enter through Township fog.
    if_event_flag_off(0, EVENT.MovedSanctuaryGuardianDead)
    if_action_button_in_region(0, region=1212678, prompt_text=10010403, line_intersects=1211679, boss_version=True)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1212679)
    skip(4)
    # Artorias: enter through Royal Wood fog.
    if_event_flag_off(1, 11210001)
    if_action_button_in_region(1, region=1212898, prompt_text=10010403, line_intersects=1211890, boss_version=True)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1211897)

    anim.force_animation(CHR.Player, 7410, wait_for_completion=True)
    restart()


def event11215011():
    """ Enter Moved Sanctuary Guardian fog (summon). """
    header(11215011, 0)
    if_character_type(1, CHR.Player, CharacterType.white_phantom)
    if_event_flag_on(1, 11215013)
    skip_if_event_flag_off(5, EVENT.EarlyOolacile)
    # Sanctuary Guardian: enter through Township fog.
    if_event_flag_off(1, EVENT.MovedSanctuaryGuardianDead)
    if_action_button_in_region(1, 1212678, 10010403, line_intersects=1211892, boss_version=True)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1212679)
    skip(4)
    if_event_flag_off(1, 11210001)
    if_action_button_in_region(1, 1212898, 10010403, line_intersects=1211890, boss_version=True)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1212897)

    anim.force_animation(CHR.Player, 7410)
    restart()


def event11215012():
    """ Notify Artorias/Moved Sanctuary Guardian boss entry. """
    header(11215012, 0)
    skip_if_this_event_on(7)
    skip_if_event_flag_off(3, EVENT.EarlyOolacile)
    if_event_flag_off(1, EVENT.MovedSanctuaryGuardianDead)
    if_player_inside_region(1, 1212680)
    skip(2)
    if_event_flag_off(1, 11210001)
    if_player_inside_region(1, 1212896)
    if_condition_true(0, 1)
    network.notify_boss_room_entry()
    skip_if_event_flag_off(3, EVENT.EarlyOolacile)
    chr.set_network_update_authority(CHR.SanctuaryGuardianMoved, UpdateAuthority.forced)
    chr.activate_npc_buffs(CHR.SanctuaryGuardianMoved)
    end()
    chr.set_network_update_authority(CHR.ArtoriasBoss, UpdateAuthority.forced)
    chr.activate_npc_buffs(CHR.ArtoriasBoss)
    flag.enable(11210537)


def event11215013():
    """ Artorias/Sanctuary Guardian behavior. """
    header(11215013, 1)
    skip_if_event_flag_off(14, EVENT.EarlyOolacile)

    skip_if_event_flag_off(3, EVENT.MovedSanctuaryGuardianDead)
    chr.disable(CHR.SanctuaryGuardianMoved)
    chr.kill(CHR.SanctuaryGuardianMoved)
    end()

    chr.disable_ai(CHR.SanctuaryGuardianMoved)
    skip_if_this_event_on(3)
    if_event_flag_on(1, 11215012)
    if_player_inside_region(1, 1212680)
    if_condition_true(0, 1)
    chr.enable(CHR.SanctuaryGuardianMoved)
    chr.enable_ai(CHR.SanctuaryGuardianMoved)
    boss.enable_boss_health_bar(CHR.SanctuaryGuardianMoved, 3471)
    hitbox.enable_hitbox(1213001)  # No idea what this is, but assuming I need it for Guardian too.
    end()

    skip_if_event_flag_off(3, EVENT.ArtoriasDeadOrGone)
    chr.disable(CHR.ArtoriasBoss)
    chr.kill(CHR.ArtoriasBoss)
    end()

    skip_if_event_flag_on(3, 11210030)
    chr.disable(CHR.ArtoriasBoss)
    obj.disable(1211100)
    obj.disable(1211101)
    chr.disable_ai(CHR.ArtoriasBoss)
    skip_if_this_event_on(11)
    if_event_flag_on(1, 11215012)
    if_player_inside_region(1, 1212896)  # Same as 5012.
    if_condition_true(0, 1)
    skip_if_event_flag_on(9, 11210030)  # Cutscene only plays once.
    skip_if_multiplayer(2)
    cutscene.play_cutscene_to_player(120110, CutsceneType.skippable, CHR.Player)
    skip(1)
    cutscene.play_cutscene_to_player(120110, CutsceneType.unskippable, CHR.Player)
    wait_frames(1)
    obj.enable(1211100)
    obj.enable(1211101)
    chr.enable(CHR.ArtoriasBoss)
    flag.enable(11210030)
    chr.enable_ai(CHR.ArtoriasBoss)
    boss.enable_boss_health_bar(CHR.ArtoriasBoss, 4100)
    hitbox.enable_hitbox(1213001)


def event11215014():
    """ Enable music for Artorias/Sanctuary Guardian. """
    header(11215014, 0)
    network.disable_sync()
    if_event_flag_on(1, 11215013)
    skip_if_host(1)
    if_event_flag_on(1, 11215011)

    skip_if_event_flag_off(5, EVENT.EarlyOolacile)
    if_event_flag_off(1, EVENT.MovedSanctuaryGuardianDead)
    if_player_inside_region(1, 1212680)
    if_condition_true(0, 1)
    sound.enable_map_sound(1213805)
    end()

    if_event_flag_off(1, 11210001)
    if_player_inside_region(1, 1212896)
    if_condition_true(0, 1)
    sound.enable_map_sound(1213801)


def event11215015():
    """ Disable Artorias/Guardian music. """
    header(11215015, 0)
    network.disable_sync()
    if_event_flag_on(1, 11215014)
    skip_if_event_flag_off(4, EVENT.EarlyOolacile)
    if_event_flag_on(1, EVENT.MovedSanctuaryGuardianDead)
    if_condition_true(0, 1)
    sound.disable_map_sound(1213805)
    end()

    if_event_flag_on(1, 11210001)
    if_condition_true(0, 1)
    sound.disable_map_sound(1213801)


def event11210006():
    """ Moved Sanctuary Guardian dies. """
    header(11210006, 1)

    # These never appear.
    chr.disable(CHR.ArtoriasBoss)
    chr.disable_backread(CHR.ArtoriasBoss)
    chr.disable(CHR.SanctuaryGuardianTwinOne)
    chr.disable(CHR.SanctuaryGuardianTwinTwo)

    # Guardian dead.
    skip_if_this_event_off(4)
    chr.disable(CHR.SanctuaryGuardianMoved)
    chr.kill(CHR.SanctuaryGuardianMoved)
    chr.disable_backread(CHR.SanctuaryGuardianMoved)
    end()

    # Guardian is not dead.
    obj.disable(1211962)  # Disable Hippodrome bonfire.
    chr.disable_backread(CHR.HawkeyeGough)  # He'll still be disabled during the fight.
    if_entity_health_less_than_or_equal(0, CHR.SanctuaryGuardianMoved, 0.0)
    wait(1.0)
    sound.play_sound_effect(CHR.SanctuaryGuardianMoved, SoundType.s_sfx, 777777777)
    if_entity_dead(0, CHR.SanctuaryGuardianMoved)
    flag.enable(EVENT.MovedSanctuaryGuardianDead)
    flag.enable(EVENT.HippodromeStableFooting)
    flag.enable(EVENT.SanctuaryGuardianDead)  # Get Sanctuary Guardian rewards.
    boss.kill_boss(CHR.SanctuaryGuardianMoved)  # Lazy, but works. Get 30K soul reward.
    obj.disable(1211890)
    sfx.delete_map_sfx(1211891)
    obj.disable(1211892)
    sfx.delete_map_sfx(1211893)
    hitbox.disable_hitbox(1213001)
    wait(2)
    sfx.create_oneoff_sfx(Category.object, 1211962, -1, 90014)
    wait(2)
    obj.enable(1211962)
    map.register_bonfire(11210968, 1211962)  # (New) Royal Hippodrome.
    wait(12.0)
    chr.disable_backread(CHR.SanctuaryGuardianMoved)
    chr.enable_backread(CHR.HawkeyeGough)


def event11210001():
    """ Knight Artorias dies. """
    header(11210001, 1)

    # Sanctuary Guardian never appears.
    chr.disable(CHR.SanctuaryGuardianMoved)
    chr.disable_backread(CHR.SanctuaryGuardianMoved)

    # Artorias dead.
    skip_if_this_event_off(6)
    chr.disable(CHR.ArtoriasBoss)
    chr.kill(CHR.ArtoriasBoss)
    chr.disable_backread(CHR.ArtoriasBoss)
    chr.enable(CHR.SanctuaryGuardianTwinOne)
    chr.enable(CHR.SanctuaryGuardianTwinTwo)
    end()

    # Artorias is not dead.
    obj.disable(1211962)  # Disable Hippodrome bonfire.
    chr.disable_backread(CHR.HawkeyeGough)  # He'll still be disabled during the fight.
    chr.disable(CHR.SanctuaryGuardianTwinOne)
    chr.disable(CHR.SanctuaryGuardianTwinTwo)
    if_entity_health_less_than_or_equal(0, CHR.ArtoriasBoss, 0.0)
    wait(1.0)
    sound.play_sound_effect(CHR.ArtoriasBoss, SoundType.s_sfx, 777777777)
    if_entity_dead(0, CHR.ArtoriasBoss)
    flag.enable(11210001)
    flag.enable(EVENT.HippodromeStableFooting)
    flag.enable(121)
    boss.kill_boss(CHR.ArtoriasBoss)
    # NOTE: No longer unlocks Artorias Set in Domnhall's inventory. Must be defeated in Darkroot.
    obj.disable(1211890)
    sfx.delete_map_sfx(1211891)
    obj.disable(1211892)
    sfx.delete_map_sfx(1211893)
    hitbox.disable_hitbox(1213001)
    wait(2)
    sfx.create_oneoff_sfx(Category.object, 1211962, -1, 90014)
    wait(2)
    obj.enable(1211962)
    map.register_bonfire(11210968, 1211962)  # (New) Royal Hippodrome.
    wait(12.0)
    chr.disable_backread(CHR.ArtoriasBoss)
    chr.enable_backread(CHR.HawkeyeGough)
    chr.enable(CHR.SanctuaryGuardianTwinOne)
    chr.enable(CHR.SanctuaryGuardianTwinTwo)


def event11210103():
    """ First activation of Oolacile Township elevator (at the top in early Oolacile). """
    header(11210103, 0)
    if_character_type(7, CHR.Player, CharacterType.black_phantom)
    if_condition_false(1, 7)
    if_event_flag_off(2, EVENT.EarlyOolacile)
    if_player_inside_region(2, 1212104)  # activated at the bottom
    if_event_flag_on(3, EVENT.EarlyOolacile)
    if_player_inside_region(3, 1212106)  # activated at the top
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    flag.enable(11210102)
    flag.enable(11210103)


def event11210123():
    """ First activation of Chester <--> early Royal Wood elevator (at the top in early Oolacile). """
    header(11210123, 0)
    if_character_type(7, CHR.Player, CharacterType.black_phantom)
    if_condition_false(1, 7)
    if_event_flag_off(2, EVENT.EarlyOolacile)
    if_player_inside_region(2, 1212124)  # activated at the bottom
    if_event_flag_on(3, EVENT.EarlyOolacile)
    if_player_inside_region(3, 1212126)  # activated at the top
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    flag.enable(11210122)
    flag.enable(11210123)


def event11210133():
    """ First activation of Chasm <--> Chester elevator (at the top in early Oolacile). """
    header(11210133, 0)
    if_event_flag_off(1, EVENT.EarlyOolacile)
    if_player_inside_region(1, 1212134)  # activated at the bottom
    if_event_flag_on(2, EVENT.EarlyOolacile)
    if_player_inside_region(2, 1212136)  # activated at the top
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    flag.enable(11210132)
    flag.enable(11210133)


def event11212001():
    """ Departure from portal that appears after Manus fight. Takes you to New Londo Ruins. This is necessary
    because the player could get to Oolacile without the ability to warp (Primordial Spark). """
    header(11212001, 0)

    sfx.delete_map_sfx(SFX.ManusPortal, False)

    if_event_flag_on(0, EVENT.ManusDeadOrGone)
    sfx.create_map_sfx(SFX.ManusPortal)
    if_singleplayer(1)
    if_action_button_in_region(1, 1212999, 10010100)
    if_condition_true(0, 1)

    end_if_client()
    chr.rotate_to_face_entity(CHR.Player, CHR.WarpRotateEntity)
    anim.force_animation(CHR.Player, ANIM.TouchWall)
    wait(3)
    flag.enable(11212002)
    warp.warp_player(16, 0, 1600990)
    restart()


def event11212004():
    """ Control appearance of fog that locks you into Chasm on early (event) visit. """
    header(11212004, 1)

    obj.disable(OBJECT.EarlyFog)
    sfx.delete_map_sfx(SFX.EarlyFog, False)
    # Enable fog when Early Oolacile is on and event battle is not done.
    if_event_flag_on(1, EVENT.EarlyOolacile)
    if_event_flag_off(1, EVENT.SifRescued)
    if_condition_true(0, 1)
    obj.enable(OBJECT.EarlyFog)
    sfx.create_map_sfx(SFX.EarlyFog)
    if_player_inside_region(0, REGION.CloseToPrisonFog)
    message.status_explanation(TEXT.AbyssPrisonFog, True)


def event11212005():
    """ Control light bank. It's shared with the Darkroot Manus battle, so need to check player is actually here. """
    header(11212005, 0)
    if_event_flag_on(1, EVENT.EarlyOolacile)
    if_in_world_area(1, 12, 1)
    skip_if_condition_false(2, 1)
    light.set_area_texture_parambank_slot_index(12, 1)
    end()
    light.set_area_texture_parambank_slot_index(12, 0)  # Probably not necessary.


def event11215027():
    """ Manus pulls you down in the arena, but only on late visit. """
    header(11215027, 0)
    if_event_flag_off(1, EVENT.EarlyOolacile)  # (New) Player must drop down themselves if Artorias is there.
    if_event_flag_on(1, 11215020)
    if_player_inside_region(1, 1212996)
    if_host(1)
    if_condition_true(0, 1)
    skip_if_multiplayer(2)
    cutscene.play_cutscene_and_warp_player(120140, CutsceneType.skippable, 1212022, 12, 1)
    skip(4)
    skip_if_client(2)
    cutscene.play_cutscene_and_warp_player(120140, CutsceneType.unskippable, 1212022, 12, 1)
    skip(1)
    cutscene.play_cutscene_to_player(120140, CutsceneType.skippable, CHR.Player)
    wait_frames(1)
    flag.enable(11210031)  # No idea what this does, no mention in events. Could trigger dialogue.


def event11215028():
    """ Artorias and Sif are fighting Manus. Early visit only. """
    header(11215028, 1)

    chr.disable(CHR.ArtoriasFighting)
    chr.disable(CHR.SifProtected)

    # If this is early Oolacile and the event battle isn't done, start the event battle.
    if_event_flag_on(1, EVENT.EarlyOolacile)
    if_event_flag_off(1, EVENT.SifRescued)
    if_condition_true(0, 1)

    chr.enable(CHR.ArtoriasFighting)
    chr.enable(CHR.SifProtected)
    chr.disable_ai(CHR.ArtoriasFighting)
    chr.disable_ai(CHR.SifProtected)  # Shouldn't have any AI anyway.

    if_event_flag_on(0, 11215020)  # Host has entered fog.

    chr.enable_ai(CHR.Manus)
    chr.enable_invincibility(CHR.Manus)
    chr.enable_immortality(CHR.Manus)  # Manus corrupts Artorias at 10% health.
    chr.disable_health_bar(CHR.Manus)
    chr.set_team_type(CHR.ArtoriasFighting, TeamType.white_phantom)
    chr.enable_immortality(CHR.ArtoriasFighting)
    chr.disable_health_bar(CHR.ArtoriasFighting)
    chr.enable_ai(CHR.ArtoriasFighting)
    if_event_flag_on(0, 11215023)  # Host has dropped into pit.
    chr.disable_invincibility(CHR.Manus)
    chr.enable_health_bar(CHR.Manus)
    # CHR.Manus possesses Artorias at 10% health.
    if_entity_health_less_than_or_equal(0, CHR.Manus, 0.1)
    anim.force_animation(CHR.Manus, ANIM.ManusPossession)
    wait(3.0)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)
    anim.force_animation(CHR.ArtoriasFighting, 3013)
    wait(2.0)
    chr.disable(CHR.Manus)
    boss.disable_boss_health_bar(CHR.Manus, 4500)
    sound.disable_map_sound(1213802)
    wait(4.0)
    anim.force_animation(CHR.ArtoriasFighting, 3105)
    wait(2.0)
    chr.disable(CHR.ArtoriasFighting)

    # End of fight.
    flag.enable(11210001)  # Artorias 'dead'; awards Covenant of Artorias.
    flag.enable(17)
    warp.set_player_respawn_point(1212950)  # No returning to the cell now.
    flag.enable(EVENT.ManusDeadOrGone)  # Manus is "dead" and the fight is over. Activates New Londo portal.
    flag.enable(EVENT.SifRescued)

    # Disable fog, enable bonfire, and enable return portal.
    obj.disable(1211990)
    sfx.delete_map_sfx(1211991, True)
    sfx.delete_map_sfx(1213100, True)
    wait(2)
    sfx.create_oneoff_sfx(Category.object, 1211950, -1, 90014)
    wait(2)
    obj.enable(1211950)
    map.register_bonfire(11210992, 1211950)


def event11210002():
    """ Manus dies (late Oolacile only). """
    header(11210002)

    obj.disable(1211950)  # Manus bonfire.

    skip_if_this_event_off(4)
    chr.disable(CHR.Manus)
    chr.kill(CHR.Manus)
    obj.enable(1211950)
    end()

    if_event_flag_off(1, EVENT.EarlyOolacile)  # Does not trigger if you manage to 'finish' Manus with Artorias.
    if_entity_health_less_than_or_equal(1, CHR.Manus, 0.0)
    if_condition_true(0, 1)

    wait(1.0)
    sound.play_sound_effect(CHR.Manus, SoundType.s_sfx, 777777777)
    if_entity_dead(0, CHR.Manus)
    flag.enable(EVENT.ManusDeadOrGone)
    flag.enable(EVENT.AwardManusSoul)
    flag.enable(17)
    boss.kill_boss(CHR.Manus)

    obj.disable(1211990)
    sfx.delete_map_sfx(1211991, True)
    sfx.delete_map_sfx(1213100, True)
    sfx.create_oneoff_sfx(Category.object, 1211950, -1, 90014)
    wait(2.0)
    obj.enable(1211950)
    map.register_bonfire(11210992, 1211950)


def event11210021():
    """ Protected Sif disappears. """
    header(11210021, 0)

    chr.disable(CHR.SifProtected)
    obj.disable(1211230)
    sfx.delete_map_sfx(1213110, False)

    # End if this isn't early Oolacile, or Sif has already been rescued (and re-drop her treasure).
    skip_if_event_flag_off(2, EVENT.SifRescued)
    chr.drop_mandatory_treasure(CHR.SifProtected)  # Re-drop Cleansing Greatshield if this is early Oolacile.
    end()

    # If this is early Oolacile and the event battle is not done, enable Sif.
    if_event_flag_on(1, EVENT.EarlyOolacile)
    if_event_flag_off(1, EVENT.SifRescued)
    if_condition_true(0, 1)
    chr.enable(CHR.SifProtected)
    obj.enable(1211230)
    sfx.create_map_sfx(1213110)
    chr.disable_ai(CHR.SifProtected)
    # Sif sits invincible inside the protective ring until the event battle is complete.
    chr.enable_invincibility(CHR.SifProtected)
    if_event_flag_on(0, 11215028)
    wait(2)
    flag.enable(11210021)
    anim.force_animation(CHR.SifProtected, 7010, wait_for_completion=True)
    chr.disable(CHR.SifProtected)
    chr.drop_mandatory_treasure(CHR.SifProtected)
    obj.disable(1211230)
    sfx.delete_map_sfx(1213110)


def event11215003():
    """ Sanctuary Guardian behavior. Now disables Twilight Vagrant. """
    header(11215003, 1)
    skip_if_this_event_on(5)
    chr.disable_ai(CHR.SanctuaryGuardian)
    if_event_flag_on(1, 11215002)
    if_player_inside_region(1, 1212886)
    if_condition_true(0, 1)
    chr.enable_ai(CHR.SanctuaryGuardian)
    boss.enable_boss_health_bar(CHR.SanctuaryGuardian, 3471)
    anim.force_animation(CHR.SanctuaryGuardian, 3017, wait_for_completion=True)


def event11215080():
    """ Twilight Vagrant triggers in Early Oolacile if you have killed at least FIVE of the phantom characters. """
    header(11215080, 1)

    chr.disable(CHR.TwilightVagrant)
    chr.enable_invincibility(CHR.TwilightVagrant)
    chr.disable_health_bar(CHR.TwilightVagrant)
    for phantom in TwilightPhantoms:
        chr.disable(phantom)
        chr.enable_immortality(phantom)
        chr.enable_invincibility(phantom)
        chr.disable_health_bar(phantom)

    obj.disable(1211790)
    sfx.delete_map_sfx(1211791, False)
    obj.disable(1211792)
    sfx.delete_map_sfx(1211793, False)

    end_if_event_flag_off(EVENT.EarlyOolacile)
    end_if_event_flag_on(EVENT.TwilightVagrantDead)

    if_host(1)
    if_number_true_flags_in_range_greater_than_or_equal(1, 11212051, 11212063, 5)
    skip_if_event_flag_on(2, EVENT.TwilightFirstEncounterDone)
    if_player_inside_region(1, REGION.TwilightVagrantFirstTrigger)
    skip(1)
    if_player_inside_region(1, REGION.TwilightVagrantNormalTrigger)
    if_condition_true(0, 1)

    flag.disable_chunk(11212031, 11212043)  # No phantoms have appeared.
    obj.enable(1211790)
    sfx.create_map_sfx(1211791)
    obj.enable(1211792)
    sfx.create_map_sfx(1211793)

    skip_if_event_flag_on(24, EVENT.TwilightFirstEncounterDone)

    chr.enable(CHR.TwilightOscar)
    chr.disable_invincibility(CHR.TwilightOscar)
    anim.force_animation(CHR.TwilightOscar, ANIM.FadeIn, wait_for_completion=True)
    if_entity_health_less_than_or_equal(0, CHR.TwilightOscar, 0.9)
    chr.set_special_effect(CHR.TwilightOscar, 3231)  # Heal Phantom to full health.
    anim.force_animation(CHR.TwilightOscar, ANIM.FadeOut)  # two seconds
    wait(2.0)
    chr.disable(CHR.TwilightOscar)
    chr.enable_invincibility(CHR.TwilightOscar)
    flag.enable(11212031)  # Oscar appeared last.
    wait(3.0)
    sound.enable_map_sound(1213804)
    wait(1.0)
    flag.enable(EVENT.TwilightFirstEncounterDone)
    chr.enable(CHR.TwilightVagrant)
    warp.warp(CHR.TwilightVagrant, Category.character, CHR.TwilightOscar, 245)
    chr.disable_invincibility(CHR.TwilightVagrant)
    anim.force_animation(CHR.TwilightVagrant, ANIM.FadeIn, wait_for_completion=True)
    boss.enable_boss_health_bar(CHR.TwilightVagrant, 5380)
    wait(5.0)
    chr.enable_invincibility(CHR.TwilightVagrant)
    anim.force_animation(CHR.TwilightVagrant, ANIM.FadeOut, wait_for_completion=True)
    chr.disable(CHR.TwilightVagrant)
    skip(3)

    sound.enable_map_sound(1213804)
    wait(3.0)
    boss.enable_boss_health_bar(CHR.TwilightVagrant, 5380)

    flag.enable(EVENT.TwilightPhantomSearching)
    run_event(11215500)


def event11215500():
    """ Kick off looping events for Twilight Vagrant, depending on which NPCs are dead (and hence available). """
    header(11215500)

    for slot, (phantom, phantom_flag, last_flag, dead_flag) in enumerate(zip(
            TwilightPhantoms,
            range(11212011, 11212024),
            range(11212031, 11212044),
            range(11212051, 11212064))):
        skip_if_event_flag_off(1, dead_flag)
        run_event_with_slot(11215510, slot + 1, args=(phantom, phantom_flag, last_flag))

    run_event(11215501)


def event11215501():
    """ Find a Twilight phantom to spawn. """
    header(11215501)

    if_event_flag_on(-1, EVENT.TwilightPhantomSearching)
    if_event_flag_on(2, EVENT.TwilightVagrantDead)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    end_if_condition_true_finished(2)
    if_number_true_flags_in_range_greater_than_or_equal(1, 11212031, 11212043, 5)
    skip_if_condition_false(1, 1)
    flag.disable_chunk(11212031, 11212043)
    flag.disable_chunk(11212011, 11212023)
    flag.enable_random_in_chunk(11212011, 11212023)
    wait_frames(5)
    restart_if_event_flag_off(EVENT.TwilightVagrantDead)


def event11215510():
    """ Spawn a Twilight Vagrant phantom, then wait until it's defeated. """
    header(11215510)
    phantom, phantom_flag, last_flag = define_args('iii')

    if_event_flag_on(1, phantom_flag)
    if_event_flag_off(1, last_flag)
    if_condition_true(-1, 1)
    if_event_flag_on(2, EVENT.TwilightVagrantDead)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    end_if_condition_true_finished(2)

    flag.disable(EVENT.TwilightPhantomSearching)

    chr.enable(phantom)
    warp.warp(phantom, Category.character, CHR.TwilightVagrant, 230)
    anim.force_animation(phantom, ANIM.FadeIn, wait_for_completion=True)
    chr.disable_invincibility(phantom)
    flag.enable(last_flag)
    if_entity_health_less_than_or_equal(0, phantom, 0.2)
    chr.set_special_effect(phantom, 3231)  # heal
    chr.enable_invincibility(phantom)
    anim.force_animation(phantom, ANIM.FadeOut)  # two seconds
    wait(2.0)
    chr.disable(CHR.TwilightVagrant)
    chr.disable(phantom)
    flag.disable(phantom_flag)

    chr.enable(CHR.TwilightVagrant)
    warp.warp(CHR.TwilightVagrant, Category.character, phantom, 245)
    chr.disable_invincibility(CHR.TwilightVagrant)
    anim.force_animation(CHR.TwilightVagrant, ANIM.FadeIn, wait_for_completion=True)
    wait_random_seconds(2.0, 5.0)
    chr.enable_invincibility(CHR.TwilightVagrant)
    anim.force_animation(CHR.TwilightVagrant, ANIM.FadeOut)  # two seconds
    wait(2.0)
    chr.disable(CHR.TwilightVagrant)

    flag.enable(EVENT.TwilightPhantomSearching)

    restart_if_event_flag_off(EVENT.TwilightVagrantDead)


def event11210007():
    """ Twilight Vagrant dies. Also disables original Sanctuary Guardian. """
    header(11210007, 1)

    # Disable Sanctuary Guardian if this is Early Oolacile.
    skip_if_event_flag_off(3, EVENT.EarlyOolacile)
    chr.disable(CHR.SanctuaryGuardian)
    chr.disable(1210810)  # Sanctuary Guardian tail.
    chr.disable_backread(CHR.SanctuaryGuardian)

    # If Twilight Vagrant is dead, or this is Early Oolacile, disable all, enable treasure, and end.
    skip_if_event_flag_off(1, EVENT.EarlyOolacile)
    skip_if_event_flag_off(len(TwilightPhantoms) + 5, EVENT.TwilightVagrantDead)
    chr.disable(CHR.TwilightVagrant)
    for phantom in TwilightPhantoms:
        chr.disable(phantom)
    skip_if_event_flag_off(2, EVENT.EarlyOolacile)
    # Enable treasure in tunnel.
    obj.enable(1211651)
    obj.enable_treasure(1211651)
    end()

    # Wait for Twilight Vagrant to die.
    if_entity_health_less_than_or_equal(0, CHR.TwilightVagrant, 0.0)
    wait(1.0)
    sound.play_sound_effect(CHR.TwilightVagrant, SoundType.s_sfx, 777777777)
    sound.disable_map_sound(1213804)
    boss.disable_boss_health_bar(CHR.TwilightVagrant, 5380)
    if_entity_dead(0, CHR.TwilightVagrant)
    flag.enable(EVENT.TwilightVagrantDead)  # NOT the same as this event.
    flag.enable(EVENT.ReflectingPoolStableFooting)
    boss.kill_boss(CHR.TwilightVagrant)
    for phantom in TwilightPhantoms:
        chr.disable(phantom)
        chr.kill(phantom)
    obj.disable(1211790)
    sfx.delete_map_sfx(1211791)
    obj.disable(1211792)
    sfx.delete_map_sfx(1211793)
    # Enable treasure in tunnel.
    obj.enable(1211651)
    obj.enable_treasure(1211651)


def event11212100():
    """ Control enemies and items that only appear in Early Oolacile. """
    header(11212100, 1)
    early_warp = range(685, 692)
    early_only = range(1210650, 1210662)
    late_only = range(1210662, 1210668)

    # NOTE: The first time this map is pre-loaded (in Darkroot), EarlyOolacile will not be enabled, but the Chasm warp
    # event forces the player to reload the map before they can explore the rest of the DLC.

    # EARLY OOLACILE: Warp some enemies to new positions.
    skip_if_event_flag_off(len(early_warp) + len(late_only) + 15, EVENT.EarlyOolacile)
    for enemy in early_warp:
        warp.short_warp(1210000 + enemy, Category.region, 1212000 + enemy, -1)
    for enemy in late_only:
        chr.disable(enemy)
    # Disable pond chest (replaced with Mimic with the same drop).
    obj.disable(1211600)
    obj.disable_treasure(1211600)
    obj.disable_activation(1211600, -1)
    chr.disable(1210600)
    # Disable Twilight Vagrant tunnel treasure unless Vagrant is dead.
    skip_if_event_flag_on(2, EVENT.TwilightVagrantDead)
    obj.disable(1211651)
    obj.disable_treasure(1211651)
    # If Manus isn't gone, disable first group of enemies in Chasm and nearby treasure corpse.
    skip_if_event_flag_on(6, EVENT.ManusDeadOrGone)
    obj.disable(1211652)
    obj.disable_treasure(1211652)
    for enemy in range(1210750, 1210754):
        chr.disable(enemy)
    end()

    # LATE OOLACILE: Disable Sanctuary tunnel corpse, new black dogs, and new chained prisoners.
    obj.disable(1211651)  # Corpse after Twilight Vagrant; replaces first bonfire.
    obj.disable_treasure(1211651)
    chr.disable(1210602)  # Pond mimic. Same drop as chest it replaces.
    for enemy in early_only:
        chr.disable(enemy)


def event11215100():
    """ Enemies snap out of standby when you approach. """
    header(11215100, 1)
    enemy, distance = define_args('if')
    skip_if_this_event_slot_off(2)
    chr.set_standby_animation_settings_to_default(enemy)
    end()

    chr.disable_ai(enemy)
    if_entity_attacked_by(-1, enemy, CHR.Player)
    if_player_within_distance(-1, enemy, distance)
    if_condition_true(0, -1)

    chr.enable_ai(enemy)
    chr.set_standby_animation_settings(enemy, cancel_animation=9060)


def event11215120():
    """ Scarecrows randomly plow and stop until you approach. """
    header(11215120, 1)
    plowing_scarecrow, distance = define_args('if')
    chr.disable_ai(plowing_scarecrow)
    if_entity_dead(7, plowing_scarecrow)
    end_if_condition_true(7)

    anim.force_animation(plowing_scarecrow, 3003, wait_for_completion=True)

    if_entity_attacked_by(-1, plowing_scarecrow, CHR.Player)
    if_player_within_distance(-1, plowing_scarecrow, distance)
    skip_if_condition_false(2, -1)
    chr.enable_ai(plowing_scarecrow)
    end()

    wait_random_seconds(0.5, 2.5)
    anim.force_animation(plowing_scarecrow, 3003, wait_for_completion=True)

    if_entity_attacked_by(-2, plowing_scarecrow, CHR.Player)
    if_player_within_distance(-2, plowing_scarecrow, distance)
    skip_if_condition_false(2, -2)
    chr.enable_ai(plowing_scarecrow)
    end()

    wait_random_seconds(0.5, 2.5)
    anim.force_animation(plowing_scarecrow, 3006, wait_for_completion=True)

    if_entity_attacked_by(-3, plowing_scarecrow, CHR.Player)
    if_player_within_distance(-3, plowing_scarecrow, distance)
    skip_if_condition_false(2, -3)
    chr.enable_ai(plowing_scarecrow)
    end()

    wait_random_seconds(0.5, 2.5)
    restart()


def event11210150():
    """ Bloathead moves onto prison elevator in late Oolacile if you haven't used it yet. """
    header(11210150, 1)
    end_if_event_flag_on(EVENT.EarlyOolacile)
    end_if_event_flag_on(11210160)  # Prison elevator used.
    warp.warp_and_set_floor(1210350, Category.region, 1212143, -1, 1213040)
    warp.warp_and_set_floor(1210350, Category.region, 1212150, -1, 1213040)
    chr.set_nest(1210350, 1212150)


def event11210151():
    """ Dog moves onto Wood elevator in early Oolacile if you haven't used it yet. """
    header(11210151, 1)
    end_if_event_flag_off(EVENT.EarlyOolacile)
    end_if_event_flag_on(11210112)  # Elevator used.
    warp.warp(1210652, Category.region, 1212151, -1)
    chr.set_nest(1210652, 1212151)


def event11210112():
    """ Marks Wood elevator as used. """
    header(11210112)
    if_event_flag_on(0, 11215221)
    end()


def event11215130():
    """ Scarecrows stop cutting trees when a flag is enabled. """
    header(11215130, 1)
    scarecrow1, scarecrow2, scarecrow3, trigger_flag = define_args('iiii')
    skip_if_this_event_off(4)
    chr.set_standby_animation_settings_to_default(scarecrow1)
    chr.set_standby_animation_settings_to_default(scarecrow2)
    chr.set_standby_animation_settings_to_default(scarecrow3)
    end()

    chr.disable_ai(scarecrow1)
    chr.disable_ai(scarecrow2)
    chr.disable_ai(scarecrow3)
    if_host(1)
    if_entity_attacked_by(-1, scarecrow1, CHR.Player)
    if_entity_attacked_by(-1, scarecrow2, CHR.Player)
    if_entity_attacked_by(-1, scarecrow3, CHR.Player)
    skip_if_client(2)
    skip_if_event_flag_on(1, trigger_flag)
    if_event_flag_on(1, trigger_flag)
    if_condition_true(-2, -1)
    if_condition_true(-2, 1)
    if_condition_true(0, -2)
    chr.enable_ai(scarecrow1)
    chr.enable_ai(scarecrow2)
    chr.enable_ai(scarecrow3)
    chr.set_standby_animation_settings(scarecrow1, cancel_animation=9060)
    chr.set_standby_animation_settings(scarecrow2, cancel_animation=9060)
    chr.set_standby_animation_settings(scarecrow3, cancel_animation=9060)


def event11215063():
    """ Kalameet boss trigger. Now changes AI in Early Oolacile. """
    header(11215063, 1)
    chr.enable_invincibility(CHR.KalameetBoss)
    skip_if_this_event_on(11)
    chr.disable_ai(CHR.KalameetBoss)
    if_event_flag_on(1, 11215062)
    if_player_inside_region(1, 1212906)
    if_player_standing_on_hitbox(-1, 1213003)
    if_player_standing_on_hitbox(-1, 1213004)
    if_player_standing_on_hitbox(-1, 1213009)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    skip_if_event_flag_off(1, EVENT.EarlyOolacile)
    chr.set_ai_id(CHR.KalameetBoss, 451001)
    chr.enable_ai(CHR.KalameetBoss)

    chr.disable_invincibility(CHR.KalameetBoss)
    skip_if_event_flag_off(2, EVENT.EarlyOolacile)
    boss.enable_boss_health_bar(CHR.KalameetBoss, 4511)  # "Calamitous Kalameet"
    skip(1)
    boss.enable_boss_health_bar(CHR.KalameetBoss, 4510)  # "Black Dragon Kalameet"
    hitbox.enable_hitbox(1213001)


def event11215030():
    """ Marvellous Chester invades you. Different in early/late. """
    header(11215030)
    invader, is_invading, invader_dead, invader_region, trigger_region, is_early = define_args('iiiiii')
    end_if_event_flag_on(is_invading)

    chr.disable(invader)

    skip_if_equal(2, is_early, 0)
    end_if_event_flag_off(EVENT.EarlyOolacile)
    skip(1)
    end_if_event_flag_on(EVENT.EarlyOolacile)
    # No longer requires any boss to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, invader_dead)
    if_event_flag_off(1, 1842)  # Chester not dead.
    if_player_inside_region(1, trigger_region)
    if_condition_true(0, 1)

    chr.disable(6730)  # Disable Chester merchant.
    chr.enable(invader)
    message.battlefield_message(20001100, 0)
    skip_if_this_event_slot_on(3)
    sfx.create_oneoff_sfx(Category.region, invader_region, -1, 130)
    anim.force_animation(invader, 7000)
    chr.replan_ai(invader)
    flag.enable(is_invading)
    flag.enable(11210536)  # Chester will mention the invasion.


def event11210905():
    """ Marvellous Chester invader gives up.

    This caused me HOURS of pain, as I'd left an event slot argument as default (0) which caused event 0 to be enabled.
    """
    header(11210905)
    invader, is_invading, reset_region, reset_hitbox, invader_dead = define_args('iiiii')
    end_if_event_flag_on(invader_dead)

    if_host(1)
    if_event_flag_on(1, is_invading)
    if_event_flag_off(1, invader_dead)
    if_player_inside_region(-1, 1212084)
    if_player_inside_region(-1, 1212085)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    anim.force_animation(invader, 7001)
    wait_frames(80)
    warp.warp_and_set_floor(invader, Category.region, reset_region, -1, reset_hitbox)
    message.battlefield_message(20001101, 0)
    chr.enable(6730)  # Chester merchant reappears.


def event11212110():
    """ Guardian Helm. """
    header(11212110)
    end_if_this_event_on()
    if_entity_dead(1, 1210150)
    if_entity_dead(1, 1210151)
    if_condition_true(0, 1)
    item.award_item_to_host_only(41200100)


def event11212111():
    """ Guardian Armor. """
    header(11212111)
    end_if_this_event_on()
    if_entity_dead(1, 1210152)
    if_entity_dead(1, 1210153)
    if_condition_true(0, 1)
    item.award_item_to_host_only(41200200)


def event11212112():
    """ Guardian Gauntlets. """
    header(11212112)
    end_if_this_event_on()
    if_entity_dead(1, 1210155)
    if_entity_dead(1, 1210156)
    if_condition_true(0, 1)
    item.award_item_to_host_only(41200300)


def event11212113():
    """ Guardian Leggings. """
    header(11212113)
    end_if_this_event_on()
    if_entity_dead(0, 1210154)
    if_condition_true(0, 1)
    item.award_item_to_host_only(41200400)


def event11210531():
    """ Ciaran appears when you have the Soul of Artorias. """
    header(11210531)
    ciaran, start_flag, end_flag, new_flag = define_args('iiii')

    if_host(1)
    if_event_flag_on(1, 1860)
    if_player_has_good(1, GOOD.SoulOfArtorias)
    if_event_flag_on(1, EVENT.ArtoriasDeadOrGone)
    if_condition_true(0, 1)
    end_if_this_event_off()
    chr.enable(ciaran)
    obj.enable(1211220)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)


def event11210532():
    """ Ciaran is given Soul of Artorias, and will disappear on reload or backread disable (no longer goes to 1865). """
    header(11210532)
    ciaran, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1863)
    if_event_flag_on(1, 1861)
    if_event_flag_on(1, 11210590)
    if_entity_alive(1, ciaran)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    # Optional disappearance.
    if_entity_backread_disabled(0, ciaran)
    chr.disable(ciaran)


def event11210340():
    """ First Alvina appearance and warp trigger. (Early only, before Manus event.) """
    header(11210340, 1)

    # Now only appears in early Oolacile, before Artorias is possessed.
    chr.disable(CHR.YoungAlvina)
    if_event_flag_on(2, EVENT.EarlyOolacile)
    if_event_flag_off(2, EVENT.ArtoriasDeadOrGone)
    if_condition_true(0, 2)
    chr.enable(CHR.YoungAlvina)

    # No change to the rest. Regions have been changed in MSB.

    skip_if_this_event_off(3)
    end_if_event_flag_on(11210341)  # Alvina is at third position (nothing to do here).
    warp.warp_and_copy_floor(CHR.YoungAlvina, Category.region, 1212331, -1, CHR.YoungAlvina)
    end()

    if_host(1)
    if_entity_within_distance(-1, CHR.YoungAlvina, CHR.Player, 7.0)
    if_entity_attacked_by(-1, CHR.YoungAlvina, CHR.Player)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    anim.force_animation(CHR.YoungAlvina, 7003, wait_for_completion=True)
    chr.disable(CHR.YoungAlvina)
    warp.warp_and_copy_floor(CHR.YoungAlvina, Category.region, 1212331, -1, CHR.YoungAlvina)
    chr.enable(CHR.YoungAlvina)


def event11212084():
    """ Monitor resting at Hippodrome bonfire. """
    header(11212084)
    if_player_within_distance(1, 1211962, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11212084)


def event11212000():
    """ A few enemies don't spawn in early Township once you have the shortcut elevator."""
    header(11212000, 1)

    if_event_flag_on(1, EVENT.EarlyOolacile)
    if_event_flag_on(1, 11210103)  # Township shortcut elevator activated.
    if_condition_true(0, 1)
    chr.disable(1210671)  # One of the lower patrolling Bloathead Sorcerers.
    chr.kill(1210671, False)


def event11210050():
    """ Kalameet lands on the bridge. Now skipped if already encountered in arena. """
    header(11210050, 1)
    chr.disable_gravity(CHR.KalameetBridge)
    chr.enable_invincibility(CHR.KalameetBridge)
    chr.disable_collision(CHR.KalameetBridge)
    chr.disable(CHR.KalameetBridge)
    skip_if_client(1)
    chr.set_network_update_authority(CHR.KalameetBridge, UpdateAuthority.forced)
    end_if_this_event_on()
    end_if_event_flag_on(11210051)  # Kalameet has arrived at arena.

    if_player_inside_region(0, 1212050)
    flag.enable(11210050)
    chr.set_network_update_rate(CHR.KalameetBridge, is_fixed=True, frequency=CharacterUpdateRate.always)
    chr.enable(CHR.KalameetBridge)
    warp.warp_and_set_floor(CHR.KalameetBridge, Category.region, 1212051, -1, hitbox_entity_id=1213000)
    anim.force_animation(CHR.KalameetBridge, 7000)
    wait_frames(420)
    chr.disable(CHR.KalameetBridge)


def event11210000():
    """ Sanctuary Guardian (default) dies. """
    header(11210000, 1)
    skip_if_this_event_off(5)
    chr.disable(CHR.SanctuaryGuardian)
    chr.kill(CHR.SanctuaryGuardian)
    chr.disable(CHR.SanctuaryGuardianTail)
    chr.kill(CHR.SanctuaryGuardianTail)
    end()

    if_entity_health_less_than_or_equal(0, CHR.SanctuaryGuardian, 0.0)
    wait(1.0)
    sound.play_sound_effect(CHR.SanctuaryGuardian, SoundType.s_sfx, 777777777)
    if_entity_dead(0, CHR.SanctuaryGuardian)
    flag.enable(EVENT.SanctuaryGuardianDead)
    flag.enable(EVENT.ReflectingPoolStableFooting)
    boss.kill_boss(CHR.SanctuaryGuardian)
    obj.disable(1211790)
    sfx.delete_map_sfx(1211791, True)
    obj.disable(1211792)
    sfx.delete_map_sfx(1211793, True)


def event11215140():
    """ Stone Guardians survey their surroundings *without* patrolling (DSR required). """
    header(11215140, 1)
    stone_guardian, trigger_region = define_args('ii')
    if_entity_inside_area(1, stone_guardian, trigger_region)
    if_ai_state(1, stone_guardian, AIStatusType.normal)
    if_condition_true(0, 1)
    chr.reset_animation(stone_guardian, disable_interpolation=False)
    anim.force_animation(stone_guardian, 7000, do_not_wait_for_transition=True)
    wait_frames(25)
    anim.force_animation(stone_guardian, 9000, do_not_wait_for_transition=True)
    wait_frames(190)
    anim.force_animation(stone_guardian, 9060)
    wait_frames(35)
    wait_random_seconds(4, 7)  # Wait a random amount of time before restarting and triggering again.
    restart()


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
