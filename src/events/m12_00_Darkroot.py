import sys
import inspect
from pydses import *

map_name = 'm12_00_00_00'  # Darkroot Garden / Darkroot Basin
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11200000
BASE_PART = 1200000


class DEBUG(IntEnum):
    DUSK_KIDNAPPED = False
    GET_CREST_OF_ARTORIAS = False
    GET_BROKEN_PENDANT = False
    GET_LORDVESSEL = False
    GRAVESTALKERS_DEAD = False
    SIF_RESCUED = False
    GET_RING_OF_ASH = False
    GET_KNIGHT_RINGS = False
    TISHANA_INVASIONS_DONE = False
    GET_TALISMAN = False
    FIGHT_MOURNWING = False
    DARK_ANOR_LONDO = False


class CHR(IntEnum):
    Shiva = 6310
    Player = 10000
    ForestBarbarian = 1200300
    ForestKnight1 = 1200301
    ForestCleric = 1200302
    ForestMage = 1200303
    ForestArcher = 1200304
    ForestThief = 1200305
    ForestKnight2 = 1200306
    DuskRescued = 6050
    ShivaBodyguard = 6420
    WitchBeatriceSummon = 6521
    DuskSummon = 6051
    LivingTree1 = 1200000
    LivingTree2 = 1200001
    DarkrootHydra = 1200010
    WalkingBastion = 1200200
    GravestalkerHealthEntity = 1200353
    BlackKnightHalberd = 1200750
    Sif = 1200800
    MoonlightButterfly = 1200801
    Mournwing = 1200802
    ArtoriasOfTheAbyss = 1200810  # Boss in second phase
    ArtoriasSpirit = 1200815  # Ally in third phase
    SifSpirit = 1200816  # Young Sif joins the Spirit of Artorias
    TheAbyssInArtorias = 1200820  # Boss in third phase (Manus)


GardenTreeLizards = (1200603, 1200604, 1200605)
GardenTreeLizardTreePoints = (1202878, 1202879, 1202880)
Gravestalkers = (1200350, 1200351, 1200352)


class ANIM(IntEnum):
    ArtoriasRoar = 3006
    ArtoriasExplosion = 3013
    ArtoriasRoarFadeIn = 3106
    ArtoriasRoarFadeOut = 3206
    TouchWall = 7114


class EVENT(IntEnum):
    LordvesselReceived = 11512000
    ButterflyBastionDead = 11200900
    GravestalkersDead = 11200901
    SifArtoriasManusDead = 5
    ManusDeadOrGone = 17
    EarlyOolacile = 11200007
    ArrivalInOolacileFromPortal = 11200008
    SifRescuedInChasm = 11212003
    JareelDead = 11510901
    MournwingDead = 11202004
    BlackKnightSwordDead = 11812020
    BlackKnightGreatswordDead = 11012005
    BlackKnightHalberdDead = 11202002
    BlackKnightAxeDead = 11502000
    AllBlackKnightsDead = 11802000
    SifStableFooting = 11202501
    SifDead = 11205350
    SifSpiritActive = 11205351
    TishanaBlighttownDead = 11400810
    TishanaSensFortressDead = 11500810
    PortalWarningDone = 11202006
    DarkAnorLondo = 11510400


class GOOD(IntEnum):
    ChthonicSpark = 813
    BrokenPendant = 2520


class ITEMLOT(IntEnum):
    SoulsOfSifAndArtorias = 2540
    GwyneveresRing = 1680
    SoulOfManus = 2700
    MournwingReward = 2920


class OBJECT(IntEnum):
    TishanaCorpse = 1201601


class REGION(IntEnum):
    DuskFreed = 1202876
    MournwingTrigger = 1202881


class RING(IntEnum):
    HornetRing = 117
    HawkRing = 119
    LeoRing = 144
    RingOfAsh = 152


class SPAWN(IntEnum):
    ChasmCellBonfire = 1212964
    SanctuaryTunnelBonfire = 1212963


class SPEFFECT(IntEnum):
    RingOfEphemera = 2370
    AbyssArmor = 5512

    
class TEXT(IntEnum):
    MoonlightButterflyName = 3230
    MournwingName = 3231
    GoldenCrystalGolemName = 2711
    ArtoriasOfTheAbyssName = 4104
    TheAbyssInArtoriasName = 4108
    SifName = 5210
    GravestalkersName = 5360
    BeWaryOfPortal = 10010199
    GardenDoorSealed = 10010167
    RingOfAshWarms = 10010627
    RingOfAshHot = 10010628
    BrokenPendantTaken = 10010615
    DarkPresenceEmerged = 10010121
    DarkPresenceReturned = 10010122


def event0():
    header(0)

    if DEBUG.DUSK_KIDNAPPED:
        flag.disable_chunk(1120, 1139)
        flag.enable(1127)
    if DEBUG.GET_CREST_OF_ARTORIAS:
        item.award_item_to_host_only(6190)
    if DEBUG.GET_BROKEN_PENDANT:
        item.award_item_to_host_only(3170)
    if DEBUG.GET_LORDVESSEL:
        item.award_item_to_host_only(1090)
    if DEBUG.GRAVESTALKERS_DEAD:
        flag.enable(EVENT.GravestalkersDead)
    if DEBUG.SIF_RESCUED:
        flag.enable(EVENT.SifRescuedInChasm)
    if DEBUG.GET_RING_OF_ASH:
        item.award_item_to_host_only(53000000)
    if DEBUG.GET_KNIGHT_RINGS:
        item.award_item_to_host_only(1200060)  # Wolf
        item.award_item_to_host_only(1510610)  # Hawk
        item.award_item_to_host_only(1200160)  # Hornet
        item.award_item_to_host_only(52710000)  # Leo
    if DEBUG.TISHANA_INVASIONS_DONE:
        flag.enable(EVENT.TishanaBlighttownDead)
        flag.enable(EVENT.TishanaSensFortressDead)
    if DEBUG.GET_TALISMAN:
        item.award_item_to_host_only(1020181)
    if DEBUG.FIGHT_MOURNWING:
        flag.enable(EVENT.ButterflyBastionDead)
    if DEBUG.DARK_ANOR_LONDO:
        flag.enable(EVENT.DarkAnorLondo)

    # (New) Register bonfires when guarding trees are killed.
    run_event_with_slot(11202000, 0, args=(1201961, 11200984, 11200811))  # Moonlight Grotto
    run_event_with_slot(11202000, 1, args=(1201962, 11200976, 11200812))  # Darkroot Garden
    run_event(11202040)  # (New) Monitors when you've rested at the Moonlight Grotto bonfire, for warping.
    map.register_ladder(11200010, 11200011, 1201140)
    map.register_ladder(11200012, 11200013, 1201141)
    spawner.create_spawner(1200090)   # related to Butterfly; immediately disabled in Butterfly behavior event.
    run_event(11202500)  # (New) Determine stable footing in the Gravestalkers/Sif arena.

    # Disable Sif's sword unless he was rescued AND hasn't appeared for the first time yet.
    skip_if_event_flag_off(2, EVENT.SifRescuedInChasm)
    skip_if_event_flag_on(1, 11200002)
    skip(1)
    obj.disable(1201200)

    # (New) Sellsword Tishana's body appears in the Forest Hunters area if both invasions are defeated.
    run_event(11202003)
    # (New) Message informs you when portal appears.
    run_event(11202007)

    # Summon fog.
    skip_if_client(10)
    for fog, fog_sfx in zip((994, 996, 998, 988, 986), (995, 997, 999, 989, 987)):
        obj.disable(1201000 + fog)
        sfx.delete_map_sfx(1201000 + fog_sfx, False)

    # Grotto checkpoint fog.
    run_event_with_slot(11200090, 0, args=(1201700, 1201701, 1202600, 1202601))

    # Gravelording.
    run_event(11205080)
    run_event(11205081)
    run_event(11205082)

    # Garden door (formerly opened with Crest of Artorias).
    run_event_with_slot(11200100, 0, args=(11200110, 1201000, 120020, 1202500, 0, 61200500))
    run_event_with_slot(11200110, 0, args=(11200100, 1201000, 1202500, 0))  # Locked

    # Grave door.
    run_event_with_slot(11200100, 1, args=(11200111, 1201010, 120021, 1202501, 1, 61200501))
    run_event_with_slot(11200110, 1, args=(11200101, 1201010, 1202501, 1))  # Locked

    run_event(11200120)  # Illusory wall near bonfire.
    run_event(11205000)  # Trigger gravity and collision for first Living Tree.
    run_event(11200800)  # Golden Golem appearance and death.
    run_event(11200200)  # Intruding on Forest Hunter territory without being in covenant.
    run_event(11200690)  # Spawn Antiquated set after summoning Dusk.
    # Chests.
    run_event_with_slot(11200600, 0, args=(1201650, 11200600))
    run_event_with_slot(11200600, 1, args=(1201651, 11200601))

    # GRAVESTALKERS / GUARDIAN SIF AND ARTORIAS OF THE ABYSS

    # This is incredibly tangled. The fights should be two fully separate events that share the same fog
    # and arena, that's all. But, it works, so it's low priority.

    sound.disable_map_sound(1203800)
    sound.disable_map_sound(1203802)
    sound.disable_map_sound(1203803)
    sound.disable_map_sound(1203804)
    # Fog is kept under three conditions: cats not triggered; cats dead and Sif not triggered; Artorias dead.
    skip_if_event_flag_off(1, 11200000)
    skip_if_event_flag_off(5, EVENT.GravestalkersDead)
    skip_if_event_flag_off(1, 11200002)
    skip_if_event_flag_off(3, 5)  # Artorias fight has been started but not finished.
    obj.disable(1201990)
    sfx.delete_map_sfx(1201991, False)
    skip(3)  # These fog flags are manually enabled in first-time trigger events.
    run_event(11205390)  # Enter fog gate (host).
    run_event(11205391)  # Enter fog gate (client).
    run_event(11205393)  # Boss room entry notification.

    # If Gravestalkers are dead, run behavior script to disable and kill them.
    skip_if_event_flag_off(2, 11200901)
    run_event(11200901)
    skip(3)  # Gravestalkers are alive.
    run_event(11200000)  # First Gravestalker appearance. (No conditions.)
    run_event(11205397)  # Gravestalker behavior and staggered appearance.
    run_event(11200901)  # Watch for Gravestalkers death.

    # If the Abyss in Artorias is dead, run behavior script to disable Sif, Artorias, and Manus.
    skip_if_event_flag_off(2, EVENT.SifArtoriasManusDead)
    run_event(11200001)
    skip(5)  # Sif/Artorias/Manus are alive.
    run_event(11200002)  # First Sif appearance. (Requires Sif to be saved and Artorias to be possessed.)
    run_event(11205392)  # Start Sif, Artorias, and Manus battle.
    run_event(11205350)  # Watches for Sif's death.
    run_event(11205396)  # Controls phase changes during fight (including Sif limping). Runs 5399 Abyss loop at end.
    run_event(11200001)  # Manus's death.

    # If either boss is alive, run the music scripts.
    skip_if_event_flag_off(2, 11200901)
    skip_if_event_flag_off(1, 5)
    skip(2)
    run_event(11205394)
    run_event(11205395)

    # MOONLIGHT BUTTERFLY

    sound.disable_map_sound(1203801)
    # If Butterfly and Golem dead:
    skip_if_event_flag_off(6, EVENT.ButterflyBastionDead)
    run_event(11205382)
    obj.disable(1201890)
    sfx.delete_map_sfx(1201891, False)
    obj.disable(1201892)
    sfx.delete_map_sfx(1201893, False)
    # Else, if alive:
    skip(18)
    run_event(11205380)  # Host enters fog.
    run_event(11205381)  # Summon enters fog.
    run_event(11205383)  # Boss entry notification.
    run_event(11205382)  # Boss behavior.
    run_event(11200900)  # Boss death.
    run_event(11205384)  # Enable music.
    run_event(11205385)  # Disable music.
    run_event(11205386)  # (NEW) Makes Butterfly rest more often when Bastion dies.
    for slot, (first_area, second_area) in enumerate(zip(range(10), range(10))):
        run_event_with_slot(11205120, slot, args=(1202220 + first_area, 1202180 + second_area))

    # MOURNWING

    run_event(11205492)  # Trigger.
    run_event(11202004)  # Death.

    # DARKROOT BASIN HYDRA

    run_event(11200801)  # Hydra death (body dies or all seven heads die).
    # Hydra heads die. Arguments aren't properly unpacked (shorts and bytes).
    run_event_with_slot(11205300, 0, args=(231342081, 3530, 1200011, 91, 256, 5430))
    run_event_with_slot(11205300, 1, args=(231407618, 3531, 1200012, 92, 513, 5431))
    run_event_with_slot(11205300, 2, args=(231473155, 3532, 1200013, 93, 770, 5432))
    run_event_with_slot(11205300, 3, args=(231538692, 3533, 1200014, 94, 1027, 5433))
    run_event_with_slot(11205300, 4, args=(231604229, 3534, 1200015, 95, 1284, 5434))
    run_event_with_slot(11205300, 5, args=(231669766, 3535, 1200016, 96, 1541, 5435))
    run_event_with_slot(11205300, 6, args=(231735304, 3536, 1200017, 97, 1798, 5436))

    # ENT TRIGGERS

    # Ent ambushes. 11205250 is area-based, 11205290 is flag-based, 11205200 is distance-based.
    run_event_with_slot(11205250, 0, args=(1200100, 1202110))  # Now near Semblance fog.
    run_event_with_slot(11205250, 1, args=(1200104, 1202111))  # Near Tree Lizard.
    run_event_with_slot(11205250, 2, args=(1200117, 1202877))  # On Basin slope.
    run_event_with_slot(11205250, 3, args=(1200118, 1202877))  # On Basin slope.
    run_event_with_slot(11205250, 4, args=(1200119, 1202877))  # On Basin slope.

    # Triggered when you pick up the item in the clearing before the grotto. (Last arg == host only.)
    for slot, (ent_id, delay) in enumerate(zip((101, 102, 103), (1.6, 2.1, 2.3))):
        run_event_with_slot(11205290, slot, args=(1200000 + ent_id, 51200170, delay, 1), arg_types='iifi')

    # Triggered by proximity.
    for slot, (ent_id, distance) in enumerate(zip(
            (109, 110, 111, 112, 113, 114, 115, 116),
            (8.0, 8.0, 5.0, 5.0, 5.0, 4.0, 2.0, 3.0))):
        run_event_with_slot(11205200, slot, args=(1200000 + ent_id, distance), arg_types='if')

    # TREE LIZARD TRIGGERS

    # Tree lizard attacks triggered by proximity.
    run_event_with_slot(11205230, 0, args=(1200600, 3.0), arg_types='if')
    run_event_with_slot(11205230, 2, args=(1200602, 3.0), arg_types='if')
    # Tree lizard changes nest if knocked down.
    run_event_with_slot(11205240, 0, args=(1200600, 1202710))
    run_event_with_slot(11205240, 2, args=(1200602, 1202712))
    # Three garden tree lizards all jump down when close.
    run_event_with_slot(11205245)

    # STONE GUARDIAN TRIGGERS

    # Stone Guardians triggered by proximity (650 and 651 are new).
    for slot, (guardian_id, distance) in enumerate(zip(range(650, 657), (6.0, 2.0, 6.0, 10.0, 8.0, 4.0, 4.0))):
        run_event_with_slot(11205260, slot, args=(1200000 + guardian_id, distance), arg_types='if')

    # FROG-RAY TRIGGERS

    # Frog-Rays jump up cliff based on area trigger.
    for slot, (frog_id, delay) in enumerate(zip(range(250, 254), (0.0, 0.5, 1.2, 0.7))):
        run_event_with_slot(11205190, slot, args=(1200000 + frog_id, 1202113, delay), arg_types='iif')
    # Frog-Rays jump up near Hydra based on individual proximity.
    for slot, frog_id in enumerate(range(254, 257)):
        run_event_with_slot(11205195, slot, args=(1200000 + frog_id, 5.0), arg_types='if')

    # Mushroom children run away (to parents, presumably) at 80% health.
    for slot, mushroom_id in enumerate(range(705, 713)):
        run_event_with_slot(11205150, slot, args=(1200000 + mushroom_id,))

    # Invisible Crystal Golem triggers.
    for slot, golem_id in enumerate(range(1200160, 1200170)):
        if golem_id == 1200169:
            run_event_with_slot(11202050, slot, args=(golem_id, 3.0, 3106), arg_types='ifi')
        else:
            run_event_with_slot(11202050, slot, args=(golem_id, 3.0, 3104), arg_types='ifi')
    # One Golem triggers when you pick up the item near the three Ents.
    run_event_with_slot(11202070, args=(1200170, 51200170, 3104))

    # (New) Black Knight Halberd appearance and death.
    run_event(11202002)

    # Non-respawning enemies. Event suggests that "mandatory treasure" instruction includes disable/kill.
    run_event_with_slot(11200810, 0, args=(1200000, 0, 0))  # Living Tree 1
    run_event_with_slot(11200810, 1, args=(1200001, 0, 0))  # Living Tree 2 (Moonlight Grotto bonfire)
    run_event_with_slot(11200810, 2, args=(1200002, 0, 0))  # Living Tree 3 (Darkroot Garden bonfire)
    run_event_with_slot(11200810, 3, args=(1200400, 0, 33004000))  # Crystal Lizard
    run_event_with_slot(11200810, 4, args=(6803, 0, 0))  # Black Bow Forest Hunter
    # All Forest Hunters now respawn except the archer with the guaranteed drop.


def event11202000():
    """ Register bonfire below grotto after protective Living Tree is killed. """
    header(11202000)
    bonfire_obj, bonfire_flag, enemy_dead_flag = define_args('iii')

    skip_if_this_event_slot_off(2)
    map.register_bonfire(bonfire_flag, bonfire_obj)
    end()
    obj.disable(bonfire_obj)
    if_event_flag_on(0, enemy_dead_flag)
    sfx.create_oneoff_sfx(Category.object, bonfire_obj, -1, 90014)
    wait(2)
    obj.enable(bonfire_obj)
    map.register_bonfire(bonfire_flag, bonfire_obj)


def event11202002():
    """ Black Knight only appears if you if you have the Ring of Ash. """
    header(11202002, 1)
    chr.disable(CHR.BlackKnightHalberd)
    skip_if_this_event_off(2)
    chr.kill(CHR.BlackKnightHalberd, False)
    end()
    if_player_has_ring(0, RING.RingOfAsh)
    chr.enable(CHR.BlackKnightHalberd)
    if_entity_dead(0, CHR.BlackKnightHalberd)
    flag.enable(EVENT.BlackKnightHalberdDead)
    item.award_item_to_host_only(27903000)
    for flag_id in (EVENT.BlackKnightSwordDead, EVENT.BlackKnightGreatswordDead, 
                    EVENT.BlackKnightHalberdDead, EVENT.BlackKnightAxeDead):
        if_event_flag_on(1, flag_id)
    skip_if_condition_true(2, 1)
    message.status_explanation(TEXT.RingOfAshWarms, pad_enabled=True)
    end()

    flag.enable(EVENT.AllBlackKnightsDead)
    message.status_explanation(TEXT.RingOfAshHot, pad_enabled=True)
    item.remove_items_from_player(ItemType.ring, RING.RingOfAsh, 0)
    item.award_item_to_host_only(ITEMLOT.GwyneveresRing)


def event11202050():
    """ Slotted event that triggers the invisible Crystal Golems based on player distance. """
    header(11202050, 1)
    golem, trigger_distance, animation = define_args('iii')
    chr.disable(golem)
    if_player_within_distance(-1, golem, trigger_distance)
    if_entity_attacked_by(-1, golem, CHR.Player)
    if_condition_true(0, -1)
    chr.enable(golem)
    anim.force_animation(golem, animation)


def event11205383():
    """ Butterfly boss notification. Now buffs Golem as well, whatever that does. """
    header(11205383, 0)
    skip_if_this_event_on(3)
    if_event_flag_off(1, EVENT.ButterflyBastionDead)
    if_player_inside_region(1, 1202896)
    if_condition_true(0, 1)
    skip_if_client(2)
    network.notify_boss_room_entry()
    chr.set_special_effect(CHR.Player, 5500)
    chr.activate_npc_buffs(CHR.MoonlightButterfly)
    chr.activate_npc_buffs(CHR.WalkingBastion)


def event11205382():
    """ Triggers Moonlight Butterfly and Golden Golem behavior, health bars. """
    header(11205382, 1)
    chr.disable(1200090)  # Disables some kind of spawner immediately after map load.
    skip_if_client(1)
    chr.set_network_update_authority(CHR.MoonlightButterfly, UpdateAuthority.forced)
    skip_if_event_flag_off(5, EVENT.ButterflyBastionDead)
    chr.disable(CHR.MoonlightButterfly)
    chr.disable(CHR.WalkingBastion)
    chr.kill(CHR.MoonlightButterfly, False)
    chr.kill(CHR.WalkingBastion, False)
    end()
    chr.disable_health_bar(CHR.MoonlightButterfly)
    chr.disable_ai(CHR.MoonlightButterfly)
    chr.disable_health_bar(CHR.WalkingBastion)
    chr.disable_ai(CHR.WalkingBastion)
    chr.set_standby_animation_settings(CHR.MoonlightButterfly, standby_animation=7000)
    if_event_flag_on(0, 11205383)
    chr.set_standby_animation_settings(CHR.MoonlightButterfly, cancel_animation=7001)
    chr.enable_ai(CHR.MoonlightButterfly)
    boss.enable_boss_health_bar(CHR.MoonlightButterfly, TEXT.MoonlightButterflyName)
    chr.enable_ai(CHR.WalkingBastion)
    boss.enable_boss_health_bar_with_slot(CHR.WalkingBastion, 1, TEXT.GoldenCrystalGolemName)


def event11200900():
    """ Butterfly/Golem death. """
    header(11200900, 0)
    if_entity_dead(1, CHR.MoonlightButterfly)
    if_entity_dead(1, CHR.WalkingBastion)
    if_condition_true(0, 1)
    chr.cancel_special_effect(CHR.Player, 5500)  # Makes Butterfly target host, I believe.
    flag.enable(11200900)
    boss.kill_boss(CHR.MoonlightButterfly)
    obj.disable(1201890)
    sfx.delete_map_sfx(1201891)
    obj.disable(1201892)
    sfx.delete_map_sfx(1201893)
    sound.play_sound_effect(CHR.MoonlightButterfly, SoundType.s_sfx, 777777777)


def event11200530():
    """ Dusk appears after the Moonlight Butterfly fight. """
    header(11200530, 0)
    dusk, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_on(1, 1120)  # Dusk is captive.
    if_event_flag_on(1, 11200900)  # Butterfly/Golden Golem fight is won.
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    wait(2)
    chr.enable(dusk)
    wait(0.5)
    chr.set_standby_animation_settings(dusk, 7875, -1, -1, -1, -1)
    anim.force_animation(dusk, 7876)


def event11200533():
    """ Dusk's summon sign (one of four orientations) appears. If you have the Lordvessel or Broken Pendant and she
    hasn't been rescued from Manus, it doesn't appear. """
    header(11200533, 0)
    for sfx_id in range(1203100, 1203104):
        sfx.delete_map_sfx(sfx_id, False)
    end_if_client()
    if_event_flag_off(1, EVENT.LordvesselReceived)
    if_player_does_not_own_good(1, GOOD.BrokenPendant)
    if_event_flag_on(1, 1122)  # Dusk has been freed, spoken to, help accepted, and not yet kidnapped.
    if_event_flag_on(2, 1129)  # Dusk has been rescued.
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    flag.enable_random_in_chunk(11200210, 11200213)
    skip_if_event_flag_off(1, 11200210)
    sfx.create_map_sfx(1203100)
    skip_if_event_flag_off(1, 11200211)
    sfx.create_map_sfx(1203101)
    skip_if_event_flag_off(1, 11200212)
    sfx.create_map_sfx(1203102)
    skip_if_event_flag_off(1, 11200213)
    sfx.create_map_sfx(1203103)


def event11200529():
    """ Dusk is kidnapped (1127) when you get the Lordvessel or Broken Pendant. """
    header(11200529, 0)
    start_flag, end_flag, new_flag = define_args('iii')
    end_if_event_flag_on(17)
    if_event_flag_on(-1, 1122)  # Dusk has been freed and spoken to, and help accepted?
    if_event_flag_on(-1, 1125)  # Dusk has been killed.
    if_event_flag_on(-1, 1126)  # Dusk has been freed and spoken to, and help refused?
    if_condition_true(1, -1)
    if_event_flag_on(-2, EVENT.LordvesselReceived)
    if_player_owns_good(-2, GOOD.BrokenPendant)
    if_condition_true(1, -2)
    if_condition_true(0, 1)
    skip_if_event_flag_on(2, 1125)
    skip_if_event_flag_on(1, 1126)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)  # 1127


def event11200005():
    """ Create portal to Oolacile. Requires Broken Pendant or Lordvessel. Initialized in 50. """
    header(11200005, 0)
    if_event_flag_on(-1, 1125)  # Dusk killed in Darkroot. (Doesn't ruin DLC.)
    if_event_flag_on(-1, 1126)  # Dusk help refused (she won't appear again). (Doesn't ruin DLC.)
    if_event_flag_on(-1, 1127)  # Dusk kidnapped (triggered when player loads Darkroot with B. Pendant or Lordvessel).
    if_condition_true(1, -1)
    if_player_owns_good(-2, GOOD.BrokenPendant)
    if_event_flag_on(-2, EVENT.LordvesselReceived)
    if_condition_true(1, -2)  # Player has Broken Pendant or Lordvessel.
    if_event_flag_off(1, 17)  # Manus must be alive for the portal to appear.
    if_condition_true(0, 1)
    end_if_client()
    if_singleplayer(0)
    sfx.create_map_sfx(1202009)
    if_multiplayer(0)
    sfx.delete_map_sfx(1202009)
    restart()


def event11200006():
    """ Player activates portal to Oolacile, and Manus takes them. Only takes you to normal Oolacile.

    Conditions:
    1. Dusk is dead or kidnapped.
    2. Player has received Lordvessel.
    3. Manus is alive.
    """
    header(11200006, 0)
    if_event_flag_on(-1, 1125)  # Dusk dead.
    if_event_flag_on(-1, 1126)  # Dusk help refused.
    if_event_flag_on(-1, 1127)  # Dusk kidnapped (triggered by Broken Pendant or Lordvessel).
    if_condition_true(1, -1)

    if_player_has_good(7, GOOD.BrokenPendant)
    if_condition_true(-2, 7)
    if_event_flag_on(-2, EVENT.LordvesselReceived)
    if_condition_true(1, -2)

    if_event_flag_off(1, EVENT.ManusDeadOrGone)
    if_singleplayer(1)
    if_action_button_in_region(1, region=1202008, prompt_text=10010100)
    if_condition_true(0, 1)
    end_if_client()

    # NOTE: Removed portal warning, as the worst case is that players will have to complete the Manus event to return.

    # "Early" or "Dark" Oolacile: Player has Broken Pendant.
    skip_if_this_event_on(8)  # Only checks to enable Early Oolacile on first portal use.
    skip_if_condition_false_finished(7, 7)
    flag.enable(EVENT.EarlyOolacile)  # Mark early Oolacile. This changes the DLC permanently.
    warp.set_player_respawn_point(SPAWN.ChasmCellBonfire)
    flag.enable(213)  # Ensures that bonfire warping to Chasm Cell is enabled.
    cutscene.play_cutscene_to_player(120002, CutsceneType.skippable, CHR.Player)
    wait_frames(1)
    warp.warp_player(12, 1, 1210984)  # Warp to Chasm Cell. Now a full reload warp, because DSR was not happy with it.
    skip(4)

    # Standard "late" Oolacile: Player has Lordvessel, but not Broken Pendant (and they never entered early).
    warp.set_player_respawn_point(SPAWN.SanctuaryTunnelBonfire)
    cutscene.play_cutscene_to_player(120002, CutsceneType.skippable, CHR.Player)
    wait_frames(1)
    warp.warp_player(12, 1, 1210998)  # Warp to Sanctuary (normal start spot).

    flag.enable(11200006)
    network.save_request()
    restart()


def event11205390():
    """ Enter Gravestalker/Sif fog. """
    header(11205390, 0)
    if_event_flag_off(-1, 5)
    if_event_flag_off(-1, 11200901)
    if_condition_true(1, -1)
    if_action_button_in_region(1, 1202998, 10010403, line_intersects=1201990, boss_version=True)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1202997)
    anim.force_animation(CHR.Player, 7410)
    restart()


def event11205391():
    """ Enter Gravestalker/Sif fog (client). """
    header(11205391, 0)
    if_event_flag_off(-1, 5)
    if_event_flag_off(-1, 11200901)
    if_condition_true(1, -1)
    if_event_flag_on(1, 11205393)
    if_character_type(1, CHR.Player, CharacterType.white_phantom)
    if_action_button_in_region(1, 1202998, 10010403, line_intersects=1201990, boss_version=True)
    if_condition_true(0, 1)
    chr.rotate_to_face_entity(CHR.Player, 1202997)
    anim.force_animation(CHR.Player, 7410)
    restart()


def event11205393():
    """ Trigger Gravestalker/Sif battle. """
    header(11205393, 0)
    if_event_flag_on(7, 11200000)
    if_event_flag_off(7, 11200901)
    if_condition_true(-7, 7)  # Gravestalkers are triggered and alive.
    if_event_flag_on(6, 11200002)
    if_event_flag_off(6, 5)
    if_condition_true(-7, 6)  # Or, Sif is triggered and alive.
    if_condition_true(1, -7)
    if_player_inside_region(1, 1202996)
    if_this_event_on(2)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    end_if_condition_true_finished(2)
    skip_if_client(1)
    network.notify_boss_room_entry()
    skip_if_condition_false_finished(4, 7)
    chr.activate_npc_buffs(Gravestalkers[0])
    chr.activate_npc_buffs(Gravestalkers[1])
    chr.activate_npc_buffs(Gravestalkers[2])
    skip(3)
    chr.activate_npc_buffs(CHR.Sif)
    chr.activate_npc_buffs(CHR.ArtoriasOfTheAbyss)
    chr.activate_npc_buffs(CHR.TheAbyssInArtorias)


def event11205394():
    """ Triggers boss music for Gravestalker or Sif. """
    header(11205394, 0)
    network.disable_sync()
    if_event_flag_off(7, 11200901)
    if_event_flag_on(7, 11205397)
    if_condition_true(-1, 7)  # Gravestalkers are attacking and alive.
    if_event_flag_off(6, 5)
    if_event_flag_on(6, 11205392)
    if_condition_true(-1, 6)  # Or, Sif is attacking and alive.
    if_condition_true(1, -1)
    skip_if_host(1)
    if_event_flag_on(1, 11205391)  # If client, must have entered fog.
    if_player_inside_region(1, 1202990)
    if_condition_true(0, 1)
    skip_if_event_flag_on(2, EVENT.GravestalkersDead)  # Not ideal for abstraction, but I have no other flag.
    # Gravestalker music.
    sound.enable_map_sound(1203800)
    end()
    # Sif music (first phase).
    sound.enable_map_sound(1203802)


def event11205395():
    """ Disable boss music for Gravestalkers. Manus music is ended in his death script. """
    header(11205395, 0)
    network.disable_sync()
    if_event_flag_on(1, 11205394)  # Music has been triggered.
    if_event_flag_on(1, 11200901)
    if_condition_true(0, 1)
    sound.disable_map_sound(1203800)


def event11200000():
    """ Gravestalkers first appearance. Same trigger zone as Sif (but no cutscene). """
    header(11200000, 1)
    end_if_this_event_on()
    chr.disable(1200350)
    chr.disable(1200351)
    chr.disable(1200352)
    # May want to disable fog here for safety, but theoretically shouldn't need to.
    if_character_human(-1, CHR.Player)
    if_character_hollow(-1, CHR.Player)
    if_condition_true(1, -1)
    if_player_inside_region(1, 1202999)  # Trigger zone for boss.
    if_condition_true(0, 1)
    skip_if_client(1)
    network.notify_boss_room_entry()
    for boss_id in Gravestalkers:
        chr.activate_npc_buffs(boss_id)
    flag.enable(11205390)
    flag.enable(11205391)
    flag.enable(11205393)
    obj.enable(1201990)
    sfx.create_map_sfx(1201991)
    wait(0.5)
    chr.enable(1200350)  # Enable first Gravestalker at edge of arena.


def event11205397():
    """ Gravestalker behavior activation. """
    header(11205397, 1)
    for gravestalker in Gravestalkers:
        chr.disable_ai(gravestalker)
    if_event_flag_on(1, 11200000)  # First-time trigger done.
    if_event_flag_on(1, 11205393)  # Boss battle started.
    if_condition_true(0, 1)
    flag.enable(11205397)
    chr.enable_ai(Gravestalkers[0])
    chr.refer_damage_to_entity(Gravestalkers[0], CHR.GravestalkerHealthEntity)
    boss.enable_boss_health_bar(CHR.GravestalkerHealthEntity, TEXT.GravestalkersName)
    run_event(11205398)  # Activates second Gravestalker early if first one reaches low health.
    wait(90)
    chr.enable(Gravestalkers[1])
    chr.enable_ai(Gravestalkers[1])
    chr.refer_damage_to_entity(Gravestalkers[1], CHR.GravestalkerHealthEntity)
    skip_if_event_flag_on(1, 11205398)
    run_event(11202005)  # Activates third Gravestalker early if second one reaches low health.
    wait(90)
    chr.enable(Gravestalkers[2])
    chr.enable_ai(Gravestalkers[2])
    chr.refer_damage_to_entity(Gravestalkers[2], CHR.GravestalkerHealthEntity)


def event11205398():
    """ Enable second Gravestalker if first one gets to low health. """
    header(11205398, 1)
    if_entity_health_less_than_or_equal(0, Gravestalkers[0], 0.1)
    chr.enable(Gravestalkers[1])
    chr.enable_ai(Gravestalkers[1])
    chr.refer_damage_to_entity(Gravestalkers[1], CHR.GravestalkerHealthEntity)
    run_event(11202005)


def event11202005():
    """ Enable third Gravestalker if second one dies or gets to 20% health. """
    header(11202005, 0)
    if_entity_health_less_than_or_equal(0, Gravestalkers[1], 0.2)
    chr.enable(Gravestalkers[2])
    chr.enable_ai(Gravestalkers[2])
    chr.refer_damage_to_entity(Gravestalkers[2], CHR.GravestalkerHealthEntity)


def event11200901():
    """ Gravestalkers death. """
    header(11200901, 0)
    chr.disable_gravity(CHR.GravestalkerHealthEntity)  # Disable gravity for health pool entity.
    chr.enable_immortality(CHR.GravestalkerHealthEntity)
    chr.disable(1200351)
    chr.disable(1200352)  # Disable second two Gravestalkers.
    skip_if_this_event_off(5)
    chr.disable(1200350)
    for gravestalker in Gravestalkers:
        chr.kill(gravestalker, False)
    end()
    if_entity_dead(1, Gravestalkers[0])
    if_entity_dead(1, Gravestalkers[1])
    if_entity_dead(1, Gravestalkers[2])
    if_condition_true(0, 1)
    chr.kill(CHR.GravestalkerHealthEntity, True)
    chr.disable(CHR.GravestalkerHealthEntity)  # To hide disappearance sounds.
    boss.kill_boss(CHR.GravestalkerHealthEntity)  # Also disables HP bar.
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)
    obj.disable(1201990)
    sfx.delete_map_sfx(1201991)


def event11200002():
    """ First Sif appearance (cutscene). """
    header(11200002, 1)
    end_if_this_event_on()
    chr.disable(CHR.Sif)
    if_character_human(-1, CHR.Player)
    if_character_hollow(-1, CHR.Player)
    if_condition_true(1, -1)
    if_event_flag_on(1, EVENT.SifRescuedInChasm)
    if_event_flag_on(1, EVENT.GravestalkersDead)  # Redundant with above, but here for clarity.
    if_player_inside_region(1, 1202999)
    if_condition_true(0, 1)

    skip_if_client(1)
    network.notify_boss_room_entry()
    chr.activate_npc_buffs(CHR.Sif)
    chr.activate_npc_buffs(CHR.ArtoriasOfTheAbyss)
    chr.activate_npc_buffs(CHR.TheAbyssInArtorias)
    flag.enable(11205390)
    flag.enable(11205391)
    flag.enable(11205393)
    skip_if_multiplayer(2)
    cutscene.play_cutscene_and_warp_player(120003, CutsceneType.skippable, 1202802, 12, 0)
    skip(4)
    skip_if_client(2)
    cutscene.play_cutscene_and_warp_player(120003, CutsceneType.unskippable, 1202802, 12, 0)
    skip(1)
    cutscene.play_cutscene_to_player(120003, CutsceneType.unskippable, CHR.Player)
    wait_frames(1)
    obj.disable(1201200)
    chr.enable(CHR.Sif)
    obj.enable(1201990)
    sfx.create_map_sfx(1201991)


def event11205392():
    """ Trigger Sif behavior. """
    header(11205392, 1)
    chr.disable_ai(CHR.Sif)
    if_event_flag_on(1, 11200002)  # First-time trigger is done.
    if_event_flag_on(1, 11205393)
    if_condition_true(0, 1)
    chr.enable_ai(CHR.Sif)
    boss.enable_boss_health_bar(CHR.Sif, TEXT.SifName)


def event11205350():
    """ Marks when Sif dies. """
    header(11205350)
    if_entity_dead(0, CHR.Sif)
    end()


def event11205396():
    """ Control phase transitions in Sif/Artorias fight. """
    header(11205396, 1)

    if_event_flag_on(1, 11205392)
    if_entity_health_less_than_or_equal(1, CHR.Sif, 0.5)
    if_condition_true(0, 1)

    # PHASE 2: Artorias appears when Sif reaches 40% health.
    sound.disable_map_sound(1203802)
    wait(0.1)
    sound.enable_map_sound(1203803)
    chr.enable(CHR.ArtoriasOfTheAbyss)
    chr.enable_immortality(CHR.ArtoriasOfTheAbyss)
    anim.force_animation(CHR.ArtoriasOfTheAbyss, ANIM.ArtoriasRoarFadeIn, wait_for_completion=True)
    boss.enable_boss_health_bar_with_slot(CHR.ArtoriasOfTheAbyss, 1, TEXT.ArtoriasOfTheAbyssName)
    if_entity_health_less_than_or_equal(-1, CHR.Sif, 0.25)
    if_entity_health_less_than_or_equal(6, CHR.ArtoriasOfTheAbyss, 0.6)
    if_condition_true(-1, 6)
    if_condition_true(0, -1)

    skip_if_condition_true_finished(6, 6)
    chr.set_special_effect(CHR.Sif, 5401)  # Sif starts limping.
    anim.force_animation(CHR.ArtoriasOfTheAbyss, ANIM.ArtoriasRoar)
    chr.set_special_effect(CHR.ArtoriasOfTheAbyss, 5510)  # Artorias is buffed without the explosion.
    if_entity_health_less_than_or_equal(-2, CHR.Sif, 0.0)
    if_entity_health_less_than_or_equal(-2, CHR.ArtoriasOfTheAbyss, 0.4)
    if_condition_true(0, -2)

    # PHASE 3: Sif dies, and Artorias transforms / Artorias gets below 60%/40% health and transforms.
    boss.disable_boss_health_bar_with_slot(CHR.Sif, TEXT.SifName, 0)
    boss.disable_boss_health_bar_with_slot(CHR.ArtoriasOfTheAbyss, 1, TEXT.ArtoriasOfTheAbyssName)
    sound.disable_map_sound(1203803)
    chr.enable_invincibility(CHR.ArtoriasOfTheAbyss)
    chr.set_team_type(CHR.Sif, TeamType.ally)
    anim.force_animation(CHR.ArtoriasOfTheAbyss, ANIM.ArtoriasExplosion)
    wait(2)
    sound.enable_map_sound(1203804)
    wait(2)
    warp.warp_and_copy_floor(CHR.TheAbyssInArtorias, Category.character, CHR.ArtoriasOfTheAbyss, 210,
                             CHR.ArtoriasOfTheAbyss)
    chr.disable(CHR.ArtoriasOfTheAbyss)
    chr.enable(CHR.TheAbyssInArtorias)
    # chr.rotate_to_face_entity(CHR.TheAbyssInArtorias, CHR.Player)
    chr.set_team_type(CHR.Sif, TeamType.white_phantom)
    light.set_area_texture_parambank_slot_index(12, 1)
    sound.play_sound_effect(CHR.TheAbyssInArtorias, SoundType.o_object, 120000020)
    chr.set_special_effect(CHR.TheAbyssInArtorias, SPEFFECT.AbyssArmor)
    boss.enable_boss_health_bar(CHR.TheAbyssInArtorias, TEXT.TheAbyssInArtoriasName)

    skip_if_event_flag_off(2, EVENT.SifDead)
    wait(25.0)  # Initial ally Artorias delay.
    skip(1)
    wait(5.0)  # Shorter delay if Sif is still alive.

    chr.enable_immortality(CHR.ArtoriasSpirit)
    chr.enable_immortality(CHR.SifSpirit)
    chr.disable_health_bar(CHR.ArtoriasSpirit)
    chr.disable_health_bar(CHR.SifSpirit)
    run_event(11205399)  # Event 11205399 takes care of the rest.


def event11205399():
    """ Artorias and Sif join you against Artorias's own dark soul. """
    header(11205399)

    end_if_event_flag_on(EVENT.SifArtoriasManusDead)

    warp.warp_and_copy_floor(CHR.ArtoriasSpirit, Category.character, CHR.Player, 237, CHR.Player)
    wait(5.0)
    chr.enable(CHR.ArtoriasSpirit)
    chr.set_team_type(CHR.ArtoriasSpirit, TeamType.white_phantom)
    anim.force_animation(CHR.ArtoriasSpirit, ANIM.ArtoriasRoarFadeIn)
    chr.cancel_special_effect(CHR.TheAbyssInArtorias, SPEFFECT.AbyssArmor)

    skip_if_event_flag_off(6, EVENT.SifDead)
    # If Sif is dead, her young spirit appears.
    warp.warp_and_copy_floor(CHR.SifSpirit, Category.character, CHR.Player, 237, CHR.Player)
    wait(2.0)
    chr.enable(CHR.SifSpirit)
    anim.force_animation(CHR.SifSpirit, 7004)
    flag.enable(EVENT.SifSpiritActive)
    skip(3)
    # If big Sif is alive, just watch for her limping.
    if_entity_health_less_than_or_equal(1, CHR.Sif, 0.25)
    skip_if_condition_false(1, 1)
    chr.set_special_effect(CHR.Sif, 5401)

    # PENDING: ARTORIAS (and SIF) ARE FIGHTING MANUS.

    # Wait until Artorias's Spirit dies or the Abyss dies.
    if_entity_health_less_than_or_equal(-1, CHR.ArtoriasSpirit, 0.1)
    if_event_flag_on(-1, 11200001)
    if_condition_true(0, -1)

    skip_if_event_flag_on(11, 11200001)  # Boss is finished.

    # If Artorias was killed, he (and Sif) will appear again after 15-20 seconds (shorter with Sif).
    chr.set_special_effect(CHR.ArtoriasSpirit, 3231)  # Heal Artorias for his next appearance.
    chr.set_special_effect(CHR.TheAbyssInArtorias, SPEFFECT.AbyssArmor)
    anim.force_animation(CHR.ArtoriasSpirit, ANIM.ArtoriasRoarFadeOut, wait_for_completion=True)
    chr.disable(CHR.ArtoriasSpirit)

    skip_if_event_flag_off(4, EVENT.SifSpiritActive)
    anim.force_animation(CHR.SifSpirit, 7005, wait_for_completion=True)
    chr.disable(CHR.SifSpirit)
    wait_random_seconds(15, 20)  # Long wait with Sif spirit.
    restart()

    wait_random_seconds(5, 10)  # Short wait without Sif spirit (big Sif was just alive).
    restart()

    # If the Abyss was killed (rather than Artorias), Artorias waits, then fades out for the last time.
    chr.enable(CHR.ArtoriasSpirit)
    wait(0.5)
    anim.force_animation(CHR.ArtoriasSpirit, 0, loop=True)
    wait(0.8)
    chr.disable_immortality(CHR.ArtoriasSpirit)
    chr.kill(CHR.ArtoriasSpirit, False)

    skip_if_event_flag_off(3, EVENT.SifSpiritActive)
    anim.force_animation(CHR.SifSpirit, 7005, wait_for_completion=True)
    chr.disable(CHR.SifSpirit)
    skip(1)
    chr.kill(CHR.Sif, False)


def event11200001():
    """ The Abyss of Artorias finally dies. """
    header(11200001, 1)
    chr.disable(CHR.ArtoriasOfTheAbyss)
    chr.disable(CHR.ArtoriasSpirit)
    chr.disable(CHR.SifSpirit)
    chr.disable(CHR.TheAbyssInArtorias)

    skip_if_event_flag_off(7, EVENT.SifArtoriasManusDead)
    chr.disable(CHR.Sif)
    for boss_id in (CHR.Sif, CHR.ArtoriasOfTheAbyss, CHR.ArtoriasSpirit, CHR.TheAbyssInArtorias, CHR.SifSpirit):
        chr.kill(boss_id, False)
    end()

    if_entity_dead(0, CHR.TheAbyssInArtorias)
    flag.enable(EVENT.SifArtoriasManusDead)
    boss.kill_boss(CHR.Sif)
    item.award_item_to_host_only(ITEMLOT.SoulOfManus)
    sound.disable_map_sound(1203804)
    obj.disable(1201990)
    sfx.delete_map_sfx(1201991)
    flag.enable(11200001)  # For Sif/Artorias disappearance when this event is reset (and battle end triggers).
    # Unlock Artorias Set in Domnhall's inventory.
    flag.disable(11217060)
    flag.disable(11217070)
    flag.disable(11217080)
    flag.disable(11217090)
    wait(3.0)
    light.set_area_texture_parambank_slot_index(12, 0)


def event11200100():
    """ Open a large door. """
    header(11200100)
    close_event_flag, door, sfx_id, prompt_region, is_unlocked, door_is_open = define_args('iiiiii')

    skip_if_event_flag_on(1, door_is_open)
    skip_if_this_event_slot_off(2)
    anim.end_animation(door, 1)
    end()

    sfx.create_object_sfx(door, 200, sfx_id)
    skip_if_equal(4, is_unlocked, 1)
    if_player_has_special_effect(-1, 36)
    if_player_has_special_effect(-1, 2080)
    if_player_has_special_effect(-1, 2260)
    if_condition_true(1, -1)
    if_action_button_in_region(1, prompt_region, 10010400, line_intersects=door, boss_version=True)
    if_condition_true(0, 1)
    flag.enable(close_event_flag)
    flag.enable(door_is_open)
    chr.rotate_to_face_entity(CHR.Player, door)
    anim.force_animation(CHR.Player, 7114, wait_for_completion=True)
    anim.force_animation(door, 1)
    sfx.delete_object_sfx(door, True)


def event11200110():
    """ Door to Darkroot Garden is shut to you. """
    header(11200110)
    open_event_flag, door, prompt_region, is_unlocked = define_args('iiii')

    network.disable_sync()
    if_event_flag_on(-1, open_event_flag)
    skip_if_equal(1, is_unlocked, 0)
    if_event_flag_on(1, 703)
    skip_if_equal(4, is_unlocked, 1)
    if_player_does_not_have_special_effect(3, 36)
    if_player_does_not_have_special_effect(3, 2080)
    if_player_does_not_have_special_effect(3, 2260)
    if_condition_true(1, 3)
    if_action_button_in_region(
        1, prompt_region, 10010400, line_intersects=door, reaction_attribute=ReactionAttribute.all)
    if_client(2)
    if_action_button_in_region(
        2, prompt_region, 10010400, line_intersects=door, reaction_attribute=ReactionAttribute.all)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    end_if_event_flag_on(open_event_flag)
    message.dialog(TEXT.GardenDoorSealed, ButtonType.yes_no, NumberButtons.no_button, door, 3.0)
    restart()


def event11205250():
    """ Ent proximity trigger. """
    header(11205250, 1)
    ent, trigger_region = define_args('ii')
    skip_if_this_event_slot_off(2)
    chr.set_standby_animation_settings_to_default(ent)
    end()

    chr.disable_ai(ent)
    if_entity_attacked_by(-1, ent, CHR.Player)
    if_entity_attacked_by(-1, ent, 6521)  # Witch Beatrice summon.
    if_player_inside_region(-1, trigger_region)
    if_entity_inside_area(-1, 6521, trigger_region)
    if_condition_true(0, -1)
    wait_random_seconds(0.0, 0.5)
    chr.enable_ai(ent)
    chr.set_standby_animation_settings(ent, cancel_animation=9060)


def event11202070():
    """ Golem triggers on a flag (once). """
    header(11202070, 1)
    golem, trigger_flag, animation = define_args('iii')
    skip_if_this_event_slot_off(2)
    chr.enable(golem)
    end()

    chr.disable(golem)
    if_event_flag_on(-1, trigger_flag)
    if_entity_attacked_by(-1, golem, CHR.Player)
    if_condition_true(0, -1)
    chr.enable(golem)
    anim.force_animation(golem, animation)


def event11205195():
    """ Frog-Rays jump up when you get close to their landing points. """
    header(11205195, 1)
    frog, distance = define_args('if')
    end_if_this_event_slot_on()
    chr.disable_gravity(frog)
    chr.disable(frog)
    chr.disable_ai(frog)
    if_player_within_distance(0, frog, distance)
    chr.enable_gravity(frog)
    chr.enable(frog)
    anim.force_animation(frog, 7000, wait_for_completion=True)
    chr.enable_ai(frog)


def event11205245():
    """ Tree lizards in Garden all jump down when you pass under. """
    header(11205245)

    skip_if_this_event_off(len(GardenTreeLizards) + 1)
    for lizard in GardenTreeLizards:
        chr.set_standby_animation_settings_to_default(lizard)
    end()

    for lizard, point in zip(GardenTreeLizards, GardenTreeLizardTreePoints):
        chr.disable_collision(lizard)
        chr.disable_gravity(lizard)
        warp.short_warp(lizard, Category.region, point, -1)
        if_player_within_distance(-1, lizard, 9.0)
        if_entity_attacked_by(-1, lizard, CHR.Player)
    if_condition_true(0, -1)

    for lizard in GardenTreeLizards:
        chr.enable_collision(lizard)
        chr.enable_gravity(lizard)
        chr.set_standby_animation_settings_to_default(lizard)


def event11202500():
    """ Checks if stable footing should be enabled in Sif's arena. """
    header(11202500, 1)
    flag.disable(EVENT.SifStableFooting)

    # 1. Gravestalkers are dead (11200901) AND Sif hasn't been rescued.
    # 2. Abyss in Artorias is dead (5)
    if_event_flag_on(1, EVENT.GravestalkersDead)
    if_event_flag_off(1, EVENT.SifRescuedInChasm)
    if_condition_true(-1, 1)
    if_event_flag_on(-1, EVENT.SifArtoriasManusDead)
    if_condition_true(0, -1)
    flag.enable(EVENT.SifStableFooting)


def event11202003():
    """ Sellsword Tishana's corpse appears if both her invasions are done. """
    header(11202003)
    end_if_this_event_on()
    obj.disable(OBJECT.TishanaCorpse)
    obj.disable_treasure(OBJECT.TishanaCorpse)
    if_event_flag_on(1, EVENT.TishanaBlighttownDead)
    if_event_flag_on(1, EVENT.TishanaSensFortressDead)
    if_condition_true(0, 1)
    obj.enable(OBJECT.TishanaCorpse)
    obj.enable_treasure(OBJECT.TishanaCorpse)


def event11205492():
    """ Triggers Mournwing. """
    header(11205492, 1)

    chr.disable(CHR.Mournwing)

    if_event_flag_on(1, EVENT.ButterflyBastionDead)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_off(1, EVENT.MournwingDead)
    end_if_condition_false(1)  # No other events use this flag, so safe to end when not needed.

    chr.enable(CHR.Mournwing)  # Mournwing can be seen on the side of the tower, like the original Butterfly.

    chr.disable(1200090)  # Disables some kind of spawner immediately after map load.
    skip_if_client(1)
    chr.set_network_update_authority(CHR.Mournwing, UpdateAuthority.forced)

    chr.disable_health_bar(CHR.Mournwing)
    chr.disable_ai(CHR.Mournwing)
    chr.set_standby_animation_settings(CHR.Mournwing, standby_animation=7000)

    if_player_inside_region(0, REGION.MournwingTrigger)

    obj.enable(1201890)
    sfx.create_map_sfx(1201891)
    obj.enable(1201892)
    sfx.create_map_sfx(1201893)

    chr.set_standby_animation_settings(CHR.Mournwing, cancel_animation=7001)
    chr.set_special_effect(CHR.Player, 5500)
    chr.enable_ai(CHR.Mournwing)
    boss.enable_boss_health_bar(CHR.Mournwing, TEXT.MournwingName)
    chr.set_special_effect(CHR.Mournwing, 4957)  # +10% speed
    sound.enable_map_sound(1203801)


def event11202004():
    """ Mournwing death. """
    header(11202004, 0)
    end_if_this_event_on()

    if_entity_health_less_than_or_equal(0, CHR.Mournwing, 0.0)
    chr.cancel_special_effect(CHR.Player, 5500)  # Makes Butterfly target host, I believe.

    boss.kill_boss(CHR.Mournwing)
    item.award_item_to_host_only(ITEMLOT.MournwingReward)
    boss.disable_boss_health_bar(CHR.Mournwing, TEXT.MournwingName)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)

    obj.disable(1201890)
    sfx.delete_map_sfx(1201891)
    obj.disable(1201892)
    sfx.delete_map_sfx(1201893)

    flag.enable(EVENT.MournwingDead)
    wait(3.0)
    sound.disable_map_sound(1203801)


def event11200690():
    """ Spawn Dusk's gear in tower after she is kidnapped (after reloading). """
    header(11200690)

    skip_if_this_event_on(6)
    obj.disable_treasure(1201600)
    obj.disable(1201600)
    if_event_flag_on(-1, 1127)  # Dusk kidnapped.
    if_event_flag_on(-1, 1130)  # Dusk rescued.
    if_condition_true(0, -1)
    end()

    obj.enable(1201600)
    obj.enable_treasure(1201600)


def event11202040():
    """ Monitors when you've rested at the Moonlight Grove bonfire for warping. """
    header(11202040)
    if_player_within_distance(1, 1201961, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11202040)


def event11205386():
    """ Monitors Walking Bastion death to make Butterfly rest more often. """
    header(11205386, 1)
    end_if_event_flag_on(EVENT.ButterflyBastionDead)

    if_entity_health_less_than_or_equal(-1, CHR.WalkingBastion, 0.0)
    if_entity_health_less_than_or_equal(1, CHR.MoonlightButterfly, 0.0)
    end_if_condition_true(1)
    chr.ai_instruction(CHR.MoonlightButterfly, command_id=1, slot_number=0)


def event11202007():
    """ Display message when portal first appears in Basin (player has Lordvessel or Broken Pendant). """
    header(11202007)
    end_if_this_event_on()
    if_event_flag_off(1, EVENT.EarlyOolacile)
    if_in_world_area(1, 12, 0)
    if_event_flag_on(-1, 1125)  # Dusk killed in Darkroot. (Doesn't ruin DLC.)
    if_event_flag_on(-1, 1126)  # Dusk help refused (she won't appear again). (Doesn't ruin DLC.)
    if_event_flag_on(-1, 1127)  # Dusk kidnapped (triggered when player loads Darkroot with B. Pendant or Lordvessel).
    if_condition_true(1, -1)
    if_event_flag_off(1, 17)  # Manus must be alive.
    if_event_flag_on(-2, EVENT.LordvesselReceived)
    if_player_has_good(-2, GOOD.BrokenPendant)
    if_condition_true(1, -2)
    if_condition_true(0, 1)
    message.status_explanation(TEXT.DarkPresenceEmerged)


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
