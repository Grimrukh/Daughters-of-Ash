
import sys
import inspect
from pydses import *

map_name = 'm18_01_00_00'       # Undead Asylum
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'


class DEBUG(IntEnum):
    GET_RING_OF_ASH = False
    GET_XANTHOUS_CROWN = False
    GET_FORSAKEN_KEY = False
    GET_SILVER_PENDANT = False
    RETURN_VISIT = False
    STRAY_DEMON_FREED = False
    DARK_ANOR_LONDO = False


class CHR(IntEnum):
    Player = 10000
    AsylumDemon = 1810800
    StrayDemon = 1810810
    AsylumTyrant = 1810820
    BlackKnightSword = 1810880
    Darkwraith1 = 1810675
    Darkwraith2 = 1810676
    Jareel = 1810680
    TyrantPitTorchHollow = 1810275


AsylumTyrantTorchHollows = range(1810280, 1810285)


class ANIM(IntEnum):
    KneelingDownOneLeg = 7895
    StayKneelingDownOneLeg = 7896
    GettingUpFromKneelingDownOneLeg = 7897


class SOUND(IntEnum):
    BossDeath = 777777777
    AsylumFloorCollapse = 851000000


class SPEFFECT(IntEnum):
    EtchedRing = 2190

    
class OBJ(IntEnum):
    FirstBonfire = 1810960
    AsylumDemonFog = 1811990
    AsylumDemonFrontDoor = 1811111
    Portcullis = 1811115
    CellKeyCorpse = 1811600
    StartingCellReturnCorpse = 1811650
    CorpseNearRollingBall = 1811651
    JareelLoot = 1811653
    TyrantBaitCorpse = 1811654
    
    
class SFX(IntEnum):
    AsylumDemonFogSFX = 1811991


class EVENT(IntEnum):
    AsylumDemonDead = 16
    OpeningCutsceneDone = 11810002
    TutorialComplete = 11810000
    RollingBallDone = 11810211
    PortcullisClosed = 11810312
    StrayDemonFree = 11812000
    StrayDemonDead = 11810901
    AsylumTyrantDead = 11810902
    DarkAnorLondo = 11510400
    BlackKnightSwordDead = 11812020
    BlackKnightGreatswordDead = 11012005
    BlackKnightHalberdDead = 11202002
    BlackKnightAxeDead = 11502000
    AllBlackKnightsDead = 11802000
    KremmelPact = 11812035
    ZandroePact = 11812036
    CaithaPact = 11812037
    NahrAlmaPact = 11812038
    QuellaPact = 11812039
    AsylumDemonFrontDoorClosed = 61810105
    AsylumBonfireWarpEnabled = 11812040
    FloorBroken = 11810220


class CUTSCENE(IntEnum):
    AsylumOpening = 180101


class RING(IntEnum):
    EtchedRing = 139
    RingOfAsh = 152


class TEXT(IntEnum):
    StrayDemonName = 2231
    AsylumTyrantName = 2233
    MakePactWithKremmel = 10010201
    MakePactWithZandroe = 10010202
    MakePactWithCaitha = 10010203
    MakePactWithNahrAlma = 10010204
    MakePactWithQuella = 10010205
    ExamineSymbol = 10010206
    DescribeKremmelPact = 10010211
    DescribeZandroePact = 10010212
    DescribeCaithaPact = 10010213
    DescribeNahrAlmaPact = 10010214
    DescribeQuellaPact = 10010215
    SacredPactWritten = 10010216
    RingOfAshWarms = 10010627
    RingOfAshHot = 10010628


REPEAT_DROPS = [500, 375, 374, 376, 293, 380]


SNUGGLY_DROP_TABLE = (
    # (ItemType, give_item, next_trade_flag, trade_collected_flag, get_item_lot)
    (3, 111, 11810601, 51810800, 3000),      # Cracked Red Eye Orb (-> 2x Twinkling Titanite)           # DONE
    (3, 375, 11810601, 51810800, 3000),      # Sunlight Medallion (-> 2x Twinkling Titanite)            # DONE
    (3, 374, 11810601, 51810800, 3000),      # Souvenir of Reprisal (-> 2x Twinkling Titanite)          # DONE
    (3, 270, 11810602, 51810810, 3010),      # Blood-red Moss Clump (-> 2x Scarlet Blossom)             # DONE
    (3, 271, 11810603, 51810820, 3020),      # Purple Moss Clump (-> Green Blossom)                     # DONE
    (3, 272, 11810604, 51810830, 3030),      # Blooming Purple Moss Clump (-> 2x Blue Titanite Chunk)   # DONE
    (3, 273, 11810605, 51810840, 3040),      # Green Moss Clump (-> Sunlight Elixir)                    # DONE
    (3, 376, 11810605, 51810840, 3040),      # Pendant (-> Sunlight Elixir)                             # DONE
    (3, 275, 11810606, 51810850, 3050),      # Egg Vermifuge (-> Ring of Sacrifice)                     # DONE
    (3, 370, 11810607, 51810860, 3060),      # Prism Stone (-> 3x Large Titanite Shard)                 # DONE
    (3, 293, 11810607, 51810860, 3060),      # Dung Pie (-> 3x Large Titanite Shard)                    # DONE
    (3, 350, 11810608, 51810870, 3070),      # Humanity (-> Elizabeth's Mushroom)                       # DONE
    (3, 500, 11810608, 51810870, 3070),      # Humanity (-> Elizabeth's Mushroom)                       # DONE
    (1, 560000, 11810609, 51810880, 3080),   # Sack (-> Raw Butcher Knife)                              # DONE
    (3, 380, 11810609, 51810880, 3080),      # Rubbish (-> Raw Butcher Knife)                           # DONE
    (3, 385, 11810610, 51810890, 3090),      # Dried Fingers (-> Ghost Blade)                           # DONE
    (3, 501, 11810611, 51810900, 3100),      # Twin Humanities (-> 2x White Titanite Chunk)             # DONE
    (0, 1330000, 11810612, 51810910, 3110),  # Pyromancy Flame (-> 2x Red Titanite Chunk)               # DONE
    (0, 1332000, 11810613, 51810920, 3120),  # Ascended Pyromancy Flame (-> Pyromancy: Chaos Storm)     # DONE
    (0, 1396000, 11810614, 51810930, 3130),  # Skull Lantern (-> 2x Ensouled Titanite)                  # DONE
    (1, 190000, 11810615, 51810940, 3140),   # Sunlight Maggot (-> Ring of Temptation)                  # DONE
    (2, 130, 11810616, 51810950, 3150),      # Ring of the Sun Princess (-> Sorcery: Chameleon)         # DONE
    (3, 711, 11810617, 51810960, 3160),      # Soul of Manus (-> 3x Soul of a Darkwraith)               # DONE
    (3, 220, 11810618, 51810970, 3170),      # (New) Silver Pendant (-> Broken Pendant)                 # DONE
    (1, 294000, 11810619, 51810980, 3180),   # (New) Real Xanthous Crown (-> Malevolence)               # DONE
    (3, 502, 11810620, 51810990, 3190),      # (New) Geminate Vestige (-> White Titanite Slab)          # DONE
    (2, 151, 11810621, 51811000, 3200),      # (New) Gwynevere's Ring (-> Tranquil Walk of Peace)       # DONE
)


def event0():
    """ Constructor event for Undead Asylum. """
    header(0, 0)

    if DEBUG.GET_RING_OF_ASH:
        item.award_item_to_host_only(53000000)  # Jareel's rewards.
    if DEBUG.RETURN_VISIT:
        flag.enable(EVENT.OpeningCutsceneDone)
        flag.enable(EVENT.TutorialComplete)
        flag.enable(EVENT.AsylumDemonDead)
        flag.enable(11810110)  # Cathedral back door open.
        flag.enable(11810111)  # Cathedral front door open.
    if DEBUG.STRAY_DEMON_FREED:
        flag.enable(EVENT.StrayDemonFree)
    if DEBUG.DARK_ANOR_LONDO:
        flag.enable(EVENT.DarkAnorLondo)
    if DEBUG.GET_XANTHOUS_CROWN:
        item.award_item_to_host_only(6770)
    if DEBUG.GET_FORSAKEN_KEY:
        item.award_item_to_host_only(1020210)
    if DEBUG.GET_SILVER_PENDANT:
        flag.disable(50001020)
        item.award_item_to_host_only(2020)

    map.register_bonfire(11810992, 1811960, 1.0, 180.0, 0)  # First bonfire.
    run_event(11812040)  # (New) Monitors resting at first bonfire (on return) for warping.
    skip_if_event_flag_on(2, EVENT.TutorialComplete)
    map.register_bonfire(11810984, 1811961, 1.0, 180.0, 0)  # Second bonfire.
    skip(1)
    obj.disable(1811961)
    map.register_ladder(11810010, 11810011, 1811140)  # Ladder out of Stray Demon pit.
    hitbox.disable_hitbox(1813121)  # Disable portcullis safety hitbox.
    flag.disable(11810315)  # Portcullis is open.

    # (New) Switch to second dark light map if Anor Londo is dark.
    skip_if_event_flag_off(1, EVENT.DarkAnorLondo)
    light.set_area_texture_parambank_slot_index(18, 1)

    # Play opening Asylum cutscene once.
    skip_if_outside_area(4, 18, 1)
    skip_if_event_flag_on(3, EVENT.OpeningCutsceneDone)
    cutscene.play_cutscene_and_warp_specific_player(CUTSCENE.AsylumOpening, CutsceneType.skippable_with_fade_out,
                                                    1812011, 18, 1, CHR.Player)
    flag.enable(EVENT.OpeningCutsceneDone)
    warp.set_player_respawn_point(1812900)

    # (NEW) Challenge mode signs. (Kremmel restored.)
    for slot in range(5):
        run_event_with_slot(11812030, slot, args=(1811875 + slot, 11812035 + slot))  # Control sign visibility.
        run_event_with_slot(11812035, slot, args=(1810875 + slot, 10010201 + slot, 10010211 + slot))  # Make pact.
    run_event(11812001)  # (New) Etched Ring breaks in the sunlight.

    run_event_with_slot(11810090, 0, args=(1811700, 1811701, 1812600, 1812601), arg_types='iiii')  # Fog wall.
    run_event(11810000)  # First departure from Asylum (automatic cutscene trigger).
    run_event(11810150)  # Departure from return visit (manual activation).
    run_event(11810211)  # Iron ball trap.
    run_event_with_slot(11810200, 1, args=(1811210, 1811211, 1811212), arg_types='iii')  # Ball destroys wall.
    run_event(11810310)  # Move Asylum Demon above arena and have it jump down for first encounter.
    run_event(11810311)  # Trap player in cathedral and open side portcullis.
    run_event(11810312)  # Shut portcullis behind you, set new respawn, and disable front door of cathedral.
    run_event(11810313)  # Front cathedral door is locked.
    run_event(11810120)  # Apply special effect to open shortcut gate back to courtyard from east corridor.
    run_event(11810110)  # Open rear door of cathedral.
    run_event(11810111)  # Open front door of cathedral.
    run_event(11810450)  # Estus Flask tip messages.
    run_event(11810320)  # Stray Demon invincible patrolling and turning against the fallen Asylum Demon.
    run_event(11810300)  # Control Asylum Demon drops using item lot flags.
    run_event(11812020)  # (New) Black Knight appears if you have the Ring of Ash.
    run_event(11812002)  # (New) Jareel's body appears unless Dark Anor Londo is active.
    run_event(11812003)  # (New) Change cell locks on return if Stray Demon was freed.

    # Drops for Snuggly.
    skip_if_client(len(SNUGGLY_DROP_TABLE) + 1 + len(SNUGGLY_DROP_TABLE) - len(REPEAT_DROPS))
    for slot, args in enumerate(SNUGGLY_DROP_TABLE):
        run_event_with_slot(11810641, slot, args=args[:4])
    run_event(11810600)  # Some kind of Snuggly flag management.
    for slot, args in enumerate([drop for drop in SNUGGLY_DROP_TABLE if drop[1] not in REPEAT_DROPS]):
        run_event_with_slot(11815110, slot, args=(args[2], args[4], args[3]))

    gates_table = (
        # (slot, ObjAct_execution_id, gate_id, opening_message_id)
        (0, 11810100, 1811100, 10010869),
        (1, 11810101, 1811101, 10010869),
        (2, 11810102, 1811102, 10010869),
        (3, 11810103, 1811103, 10010869),
        (4, 11810104, 1811104, 10010871),
        (5, 11810105, 1811105, 0),
        (6, 11810106, 1811106, 10010871),
        (7, 11810107, 1811107, 10010875),
        (20, 11810120, 1811120, 10010873),
        (21, 11810121, 1811121, 10010873),
        (22, 11810122, 1811122, 10010873),
        (23, 11810123, 1811123, 10010873),
    )

    for args in gates_table:
        run_event_with_slot(11810100, args[0], args=args[1:])

    run_event(11815150)  # Snuggly dialogue delay (one second).

    starting_equipment_table = (
        # (class_type, equipment_drop_1, equipment_drop_2, equipment_drop_3, tip_message_bits)
        (0, 1811601, 1811602, 1811602, 0),
        (1, 1811603, 1811604, 1811604, 0),
        (2, 1811605, 1811606, 1811606, 0),
        (3, 1811607, 1811608, 1811608, 0),
        (4, 1811609, 1811610, 1811610, 0),
        (5, 1811611, 1811612, 1811613, 65536),
        (6, 1811614, 1811615, 1811616, 1),
        (7, 1811617, 1811618, 1811619, 256),
        (8, 1811620, 1811621, 1811622, 16777216),
        (9, 1811623, 1811624, 1811624, 0),
    )
    for slot, args in enumerate(starting_equipment_table):
        run_event_with_slot(11810400, slot, args=args, arg_types='iiiii')  # Five bytes packed into last int.

    # ASYLUM DEMON

    sound.disable_map_sound(1813800)

    skip_if_event_flag_on(2, 11810312)  # Reset initial Asylum Demon jump if the player didn't escape via portcullis.
    flag.disable(11810310)
    flag.disable(11810314)

    skip_if_event_flag_off(1, EVENT.AsylumDemonFrontDoorClosed)
    obj.disable_activation(OBJ.AsylumDemonFrontDoor, -1)

    # If Asylum Demon is dead:
    skip_if_event_flag_off(7, EVENT.AsylumDemonDead)
    run_event(11815392)  # Disables Asylum Demon.
    obj.disable(1811990)
    sfx.delete_map_sfx(1811991, False)
    anim.end_animation(OBJ.Portcullis, 1)  # Open portcullis.
    anim.end_animation(OBJ.AsylumDemonFrontDoor, 1)  # Open front door of cathedral.
    obj.disable_activation(OBJ.AsylumDemonFrontDoor, -1)  # Disable front door activation.
    skip(7)
    # Else, if Asylum Demon is alive:
    run_event(11815390)  # Host enters fog.
    run_event(11815393)  # Battle begins.
    run_event(11815392)  # Boss behavior.
    run_event(11810001)  # Boss dies.
    run_event(11815394)  # Boss music starts.
    run_event(11815395)  # Boss music stops
    run_event(11812004)  # (NEW) Asylum Demon automatically dies if you traverse the Stray pit and climb the ladder

    # Stray Demon is 'freed' if the Asylum Demon falls into its pit and dies, unless you kill it immediately.
    # Otherwise, Stray Demon is disabled (tutorial only). Also handles Stray Demon death during tutorial.
    skip_if_event_flag_on(2, EVENT.TutorialComplete)
    run_event(11815396)
    run_event(11810900)

    # STRAY DEMON / ASYLUM TYRANT

    obj.disable(1811890)
    sfx.delete_map_sfx(1811891, False)
    sound.disable_map_sound(1813801)

    # End constructor here if this isn't a return visit.
    end_if_event_flag_off(EVENT.TutorialComplete)

    skip_if_event_flag_off(2, 11810900)
    run_event(11815382)
    skip(4)
    run_event(11815382)
    run_event(11810900)
    run_event(11815384)
    run_event(11815385)

    # Caution: any instructions added at the bottom here will only run on return visits.


def event50():
    """ NPC pre-constructor. """
    header(50, 0)

    if DEBUG.STRAY_DEMON_FREED:
        flag.enable(11810220)  # Floor broken.

    # New Game Plus stuff.
    skip_if_client(11)
    skip_if_event_flag_on(10, 705)
    if_new_game_count_greater_than_or_equal(1, 1)
    skip_if_condition_false(8, 1)
    flag.enable(705)
    flag.enable(50000082)
    warp.set_player_respawn_point(1812900)
    flag.disable(11807200)
    flag.disable(11807210)
    flag.disable(11807220)
    flag.disable(11807240)
    run_event(11810050)  # Enables two Anor Londo shop flags if you're in Darkmoon Covenant.

    run_event(11810350)  # Control enemies and Painted Doll in tutorial vs. return.
    run_event(11815220)  # (Updated) You or Asylum Demon breaks floor.

    # OSCAR

    chr.humanity_registration(6023, 8326)  # Dying Oscar.
    skip_if_event_flag_on(1, 1061)
    chr.disable(6024)
    chr.set_team_type(6024, TeamType.hostile_ally)  # Hollow Oscar
    run_event_with_slot(11810520, 0, args=(6023, 1060, 1074, 1073))
    run_event_with_slot(11810530, 0, args=(6023,))
    # Hollow Oscar appears on return visit.
    run_event_with_slot(11810531, 0, args=(6024, 1060, 1074, 1061))
    # Hollow Oscar dies.
    run_event_with_slot(11810532, 0, args=(6024, 1060, 1074, 1062))
    run_event(11815010)  # Control Oscar's health bar appearance while weakening him.


def event11810320():
    """ Tutorial: Stray Demon invincible patrol and one-shot battle during tutorial. """
    header(11810320, 0)

    end_if_event_flag_on(EVENT.TutorialComplete)

    chr.disable(CHR.AsylumTyrant)  # Disable Asylum Tyrant.
    map.register_ladder(11810012, 11810013, 1811141)  # Pit ladder.

    end_if_event_flag_on(EVENT.StrayDemonDead)

    # Stray Demon walks around its pit, invincible.
    chr.enable_invincibility(CHR.StrayDemon)
    if_entity_backread_enabled(0, CHR.StrayDemon)
    chr.ai_instruction(CHR.StrayDemon, 10, 0)

    # Stray Demon temporarily joins your team when you challenge the Asylum Demon (either battle).
    if_event_flag_on(0, 11815392)  # Asylum Demon fight started.
    if_entity_backread_enabled(0, CHR.StrayDemon)
    chr.ai_instruction(CHR.StrayDemon, -1, 0)
    chr.set_team_type(CHR.StrayDemon, TeamType.fighting_ally)
    chr.disable_invincibility(CHR.StrayDemon)

    # Stray Demon becomes hostile again if you fall into the pit.
    if_player_inside_region(0, 1812896)  # Player falls into the pit.
    chr.set_team_type(CHR.StrayDemon, TeamType.boss)


def event11815382():
    """ Stray Demon boss battle behavior. Now handles Asylum Tyrant variant as well. """
    header(11815382, 1)

    # Asylum Tyrant and its Hollow minions always starts disabled.
    chr.disable(CHR.AsylumTyrant)
    chr.disable(CHR.TyrantPitTorchHollow)
    for hollow in AsylumTyrantTorchHollows:
        chr.disable(hollow)
    obj.disable(OBJ.TyrantBaitCorpse)

    skip_if_event_flag_on(2, EVENT.StrayDemonDead)
    skip_if_event_flag_on(1, EVENT.AsylumTyrantDead)
    skip(3)
    chr.disable(CHR.StrayDemon)
    map.register_ladder(11810012, 11810013, 1811141)
    end()

    # Stray Demon was not freed from pit in tutorial:

    skip_if_event_flag_on(10, EVENT.StrayDemonFree)
    chr.disable_ai(CHR.StrayDemon)
    chr.enable_invincibility(CHR.StrayDemon)
    chr.disable_health_bar(CHR.StrayDemon)
    if_player_inside_region(0, 1812896)
    chr.enable_ai(CHR.StrayDemon)
    chr.disable_invincibility(CHR.StrayDemon)
    boss.enable_boss_health_bar(CHR.StrayDemon, TEXT.StrayDemonName)
    obj.enable(1811890)
    sfx.create_map_sfx(1811891)
    end()

    # Stray Demon was freed from pit in tutorial:

    # Enable Hollows that surround treasure in pit.
    chr.enable(CHR.TyrantPitTorchHollow)
    chr.disable_ai(CHR.TyrantPitTorchHollow)
    obj.enable(OBJ.TyrantBaitCorpse)
    obj.enable_treasure(OBJ.TyrantBaitCorpse)
    chr.disable(CHR.StrayDemon)
    if_player_inside_region(0, 1812896)
    # Had a game hang here. Probably an artifact of debug mode (like warping around).
    chr.enable_ai(CHR.TyrantPitTorchHollow)
    obj.enable(1811890)
    sfx.create_map_sfx(1811891)
    wait(8.0)  # Ten seconds of fighting tough Torch Hollows.
    chr.enable(CHR.AsylumTyrant)
    chr.enable_invincibility(CHR.AsylumTyrant)
    wait(4.0)
    chr.disable_invincibility(CHR.AsylumTyrant)
    boss.enable_boss_health_bar(CHR.AsylumTyrant, TEXT.AsylumTyrantName)
    flag.enable(11815382)  # For music, etc.
    for slot, (required_flag, torch_hollow) in enumerate((
            (11815382, 1810280),
            (11812010, 1810281),
            (11812011, 1810282),
            (11812012, 1810283),
            (11812013, 1810284),
            )):
        run_event_with_slot(11812010, slot, args=(required_flag, torch_hollow))


def event11812010():
    """ Ten-slot event (2010-2019) that drops in more Torch Hollows during the Asylum Tyrant fight. """
    header(11812010, 1)
    spawn_trigger_flag, hollow = define_args('ii')

    if_event_flag_on(0, spawn_trigger_flag)
    wait_random_seconds(15.0, 25.0)
    chr.enable(hollow)
    chr.enable_invincibility(hollow)
    wait(3.0)
    chr.disable_invincibility(hollow)


def event11810900():
    """ Stray Demon / Asylum Tyrant death. """
    header(11810900, 0)
    if_entity_dead(1, CHR.StrayDemon)
    if_entity_dead(2, CHR.AsylumTyrant)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    obj.disable(1811890)
    sfx.delete_map_sfx(1811891)
    map.register_ladder(11810012, 11810013, 1811141)
    skip_if_condition_false_finished(3, 2)
    boss.kill_boss(CHR.AsylumTyrant)
    flag.enable(EVENT.AsylumTyrantDead)
    end()
    boss.kill_boss(CHR.StrayDemon)
    flag.disable(EVENT.StrayDemonFree)
    flag.enable(EVENT.StrayDemonDead)


def event11815220():
    """ Floor breaks under the Asylum Demon, or by the player if it wasn't broken in the tutorial. It is repaired on
    load if the Asylum Demon is alive. """
    header(11815220, 0)

    if DEBUG.STRAY_DEMON_FREED:
        skip(2)

    # Disable floor permanently if it broke before and Asylum Demon is dead.
    skip_if_event_flag_off(5, EVENT.FloorBroken)
    skip_if_event_flag_off(4, EVENT.AsylumDemonDead)
    obj.disable(1811200)
    obj.disable(1811201)
    obj.disable(1811202)
    end()

    skip_if_this_event_on(5)
    flag.disable(EVENT.FloorBroken)  # Floor must be broken again.
    obj.restore(1811200)
    obj.restore(1811201)
    obj.restore(1811202)
    obj.disable(1811201)  # actual breaking part

    # Break floor when Asylum Demon (tutorial) or player (return) walks onto it.
    if_host(1)
    # On return, player must be inside the breaking area.
    if DEBUG.RETURN_VISIT:
        skip(1)
    skip_if_event_flag_off(2, EVENT.TutorialComplete)
    if_player_inside_region(-1, 1812400)  # trigger area for floor breaking
    skip(3)
    # In tutorial, Asylum Demon must be inside the breaking area, and player in the arena.
    if_entity_inside_area(3, CHR.AsylumDemon, 1812400)
    if_player_inside_region(3, 1812990)
    if_condition_true(-1, 3)

    if_condition_true(1, -1)
    if_condition_true(0, 1)

    flag.enable(11815220)

    # Add a 12 second delay if the Asylum Demon broke the floor.
    skip_if_event_flag_on(3, EVENT.TutorialComplete)
    wait(12.0)
    if_player_inside_region(4, 1812990)  # Player must still be in arena when it ends.
    restart_if_condition_false(4)  # Countdown needs to be triggered again, and delay checked.

    flag.enable(EVENT.FloorBroken)  # Floor is broken.
    # Break floor.
    obj.disable(1811200)
    obj.enable(1811201)
    obj.destroy(1811201, 1)
    obj.disable(1811202)
    sound.play_sound_effect(1811200, SoundType.o_object, SOUND.AsylumFloorCollapse)
    sfx.create_oneoff_sfx(0, 1811200, -1, 180100)


def event11812020():
    """ Black Knight Sword only appears if you if you have the Ring of Ash. """
    header(11812020, 1)
    chr.disable(CHR.BlackKnightSword)
    skip_if_this_event_off(2)
    chr.kill(CHR.BlackKnightSword, False)
    end()
    if_player_has_item(0, ItemType.ring, RING.RingOfAsh)
    chr.enable(CHR.BlackKnightSword)
    if_entity_dead(0, CHR.BlackKnightSword)
    flag.enable(EVENT.BlackKnightSwordDead)
    item.award_item_to_host_only(27900000)
    for flag_id in (EVENT.BlackKnightSwordDead, EVENT.BlackKnightGreatswordDead,
                    EVENT.BlackKnightHalberdDead, EVENT.BlackKnightAxeDead):
        if_event_flag_on(1, flag_id)
    skip_if_condition_true(2, 1)
    message.status_explanation(TEXT.RingOfAshWarms, pad_enabled=True)
    end()
    flag.enable(EVENT.AllBlackKnightsDead)
    message.status_explanation(TEXT.RingOfAshHot, pad_enabled=True)


def event11812001():
    """ Etched Ring turns to dust when you emerge without a pact. """
    header(11812001)
    if_event_flag_range_all_off(1, 11812035, 11812039)  # No pact made.
    if_player_has_ring(1, RING.EtchedRing)
    if_player_within_distance(1, OBJ.FirstBonfire, 10.0)
    if_condition_true(0, 1)
    message.status_explanation(10010207, True)
    item.remove_items_from_player(ItemType.ring, RING.EtchedRing, 0)


def event11812030():
    """ Gods' pact signs appear when you wear the Etched Ring. """
    header(11812030)
    sign_sfx, pact_flag = define_args('ii')
    sfx.delete_map_sfx(sign_sfx)
    end_if_event_flag_on(pact_flag)
    end_if_event_flag_on(11812001)  # Too late to make any more pacts.

    if_player_has_special_effect(1, SPEFFECT.EtchedRing)
    if_event_flag_off(1, pact_flag)
    if_event_flag_off(1, 11812001)
    skip_if_not_equal(1, sign_sfx, 1811879)
    if_entity_dead(1, 1810102)  # Hollow in water must be dead for Quella's sign.
    if_condition_true(0, 1)

    sfx.create_map_sfx(sign_sfx)

    if_player_does_not_have_special_effect(-1, SPEFFECT.EtchedRing)
    if_event_flag_on(-1, pact_flag)
    if_event_flag_on(-1, 11812001)
    if_condition_true(0, -1)
    restart()


def event11812035():
    """ Make a pact with a god or goddess. """
    header(11812035)
    sign_interaction, make_pact_prompt, pact_made_explanation = define_args('iii')

    end_if_this_event_slot_on()

    # Display name of god/goddess.
    if_host(1)
    if_player_has_special_effect(1, SPEFFECT.EtchedRing)
    if_event_flag_off(1, 11812001)
    skip_if_not_equal(1, sign_interaction, 1810879)
    if_entity_dead(1, 1810102)  # Hollow in water must be dead for Quella's sign.
    if_action_button_state(1, Category.character, sign_interaction, 180.0, -1, 2.0, TEXT.ExamineSymbol)
    if_condition_true(0, 1)

    message.status_explanation(pact_made_explanation, True)
    wait(1.0)

    # Display condition of pact.
    if_host(1)
    if_player_has_special_effect(1, SPEFFECT.EtchedRing)
    if_event_flag_off(1, 11812001)
    skip_if_not_equal(1, sign_interaction, 1810879)
    if_entity_dead(1, 1810102)  # Hollow in water must be dead for Quella's sign.
    if_action_button_state(1, Category.character, sign_interaction, 180.0, -1, 2.0, make_pact_prompt)
    if_condition_true(0, 1)

    chr.rotate_to_face_entity(CHR.Player, sign_interaction)
    anim.force_animation(CHR.Player, ANIM.KneelingDownOneLeg, wait_for_completion=True)
    anim.force_animation(CHR.Player, ANIM.StayKneelingDownOneLeg, loop=True)
    wait(2.0)
    message.status_explanation(TEXT.SacredPactWritten, True)
    wait(2.0)
    anim.force_animation(CHR.Player, ANIM.GettingUpFromKneelingDownOneLeg)


def event11810350():
    """ Toggle enemies between tutorial and return. """
    header(11810350, 1)

    skip_if_event_flag_on(41, EVENT.TutorialComplete)

    obj.disable(OBJ.StartingCellReturnCorpse)
    obj.disable(OBJ.CorpseNearRollingBall)
    obj.disable(OBJ.TyrantBaitCorpse)
    for return_enemy in range(1810200, 1810214):
        chr.disable(return_enemy)
    for tyrant_hollow in [1810275, 1810280, 1810281, 1810282, 1810283, 1810284]:
        chr.disable(tyrant_hollow)

    if_event_flag_on(0, EVENT.TutorialComplete)

    flag.disable(EVENT.RollingBallDone)

    for return_enemy in range(1810200, 1810214):
        chr.enable(return_enemy)
    obj.enable(OBJ.CorpseNearRollingBall)
    obj.enable(OBJ.StartingCellReturnCorpse)

    # Skips to here if tutorial is done on load.

    obj.enable_treasure(OBJ.CorpseNearRollingBall)
    obj.enable_treasure(OBJ.StartingCellReturnCorpse)
    obj.disable(OBJ.CellKeyCorpse)
    for tutorial_enemy in range(1810101, 1810114):
        if tutorial_enemy in (1810105, 1810109):
            continue  # unused
        chr.disable(tutorial_enemy)


def event11812002():
    """ Jareel's body control, and Darkwraiths. """
    header(11812002, 1)

    obj.disable(OBJ.JareelLoot)

    skip_if_event_flag_off(3, EVENT.DarkAnorLondo)
    chr.disable(CHR.Jareel)
    obj.enable_treasure(OBJ.JareelLoot)
    end()

    chr.disable(CHR.Darkwraith1)
    chr.disable(CHR.Darkwraith2)
    chr.disable_ai(CHR.Jareel)
    chr.enable_invincibility(CHR.Jareel)


def event11810311():
    """ Asylum Demon first encounter. Portcullis now only opens when you get your shield. """
    header(11810311)
    if_event_flag_off(1, EVENT.AsylumDemonDead)
    if_event_flag_off(1, 11815390)  # Battle not entered from top fog.
    if_event_flag_off(1, 11810315)  # Portcullis is not open.
    if_player_inside_region(1, 1812996)  # Player inside church arena.
    if_condition_true(0, 1)

    # Close church doors.
    flag.disable(11810112)
    anim.force_animation(OBJ.AsylumDemonFrontDoor, 3)

    # Wait for player to pick up shield (whichever starting class they have).
    for shield_flag in (110, 130, 150, 170, 190, 210, 240, 270, 300, 330):
        if_event_flag_on(-1, 51810000 + shield_flag)
    if_condition_true(0, -1)

    # Open portcullis.
    flag.enable(11810315)
    anim.force_animation(1811115, 1, wait_for_completion=True)


def event11812003():
    """ Control cell locks (depending on Asylum Tyrant). """
    header(11812003)

    if_event_flag_on(1, EVENT.TutorialComplete)
    if_event_flag_on(1, EVENT.StrayDemonFree)

    skip_if_condition_false(9, 1)
    # Disable original cell gates that require Asylum Cell Key.
    for gate in range(1811100, 1811104):
        obj.disable(gate)
        obj.disable_activation(gate, -1)
    end()

    # Otherwise, disable cell gates that require Asylum Tyrant's Key.
    for gate in range(1811120, 1811124):
        obj.disable(gate)
        obj.disable_activation(gate, -1)


def event11810300():
    """ Control Asylum Demon drops. """
    header(11810300)
    end_if_client()
    end_if_this_event_on()
    end_if_event_flag_on(EVENT.AsylumDemonDead)
    skip_if_event_flag_on(3, 11810301)
    # Disable Big Pilgrim's Key drops from both Asylum Demon and Oscar.
    flag.enable(50000081)
    flag.enable(50001661)
    flag.enable(11810301)
    if_event_flag_off(1, EVENT.AsylumDemonDead)
    if_event_flag_off(1, 11810090)  # Fog wall not passed yet.
    if_entity_health_less_than_or_equal(1, CHR.AsylumDemon, 0.0)
    if_condition_true(0, 1)
    # Asylum Demon killed on first try.
    flag.disable(50000081)  # Oscar will give you Big Pilgrim's Key.
    flag.enable(50001660)  # Asylum Demon won't drop Big Pilgrim's Key.

    if_entity_inside_area(2, CHR.AsylumDemon, 1812896)
    end_if_condition_true(2)
    flag.disable(50001661)  # Asylum Demon will drop Archhammer if it didn't fall into the Stray pit.


def event11815396():
    """ Stray Demon is 'freed' during the tutorial when the Asylum Demon falls in and dies. If you simply break the
    floor, it will not be freed (it's too stupid to realize the Asylum Demon has died). Also disables the Stray Demon
    if you kill it during the tutorial. """
    header(11815396, 1)

    skip_if_event_flag_off(2, EVENT.StrayDemonDead)
    chr.disable(CHR.StrayDemon)
    end()

    if_event_flag_on(1, 11815392)  # Asylum Demon battle started.
    if_entity_inside_area(1, CHR.AsylumDemon, 1812896)  # Asylum Demon is in Stray pit.
    if_condition_true(0, 1)

    if_entity_health_less_than_or_equal(0, CHR.AsylumDemon, 0.0)  # Asylum Demon dies.
    flag.enable(EVENT.StrayDemonFree)


def event11812040():
    """ Monitors when you've rested at the Undead Asylum bonfire for warping. """
    header(11812040)
    end_if_this_event_on()

    if_event_flag_on(1, 11020021)  # Crow has taken you back to Asylum.
    if_player_within_distance(1, OBJ.FirstBonfire, 10.0)  # Player is near first bonfire.
    if_has_tae_event(1, CHR.Player, 700)
    if_in_world_area(1, 18, 1)
    if_condition_true(0, 1)
    flag.enable(11812040)


def event11810313():
    """ Displays message that front cathedral door is locked. """
    header(11810313)
    network.disable_sync()
    if_event_flag_off(1, EVENT.AsylumDemonDead)
    if_event_flag_on(1, EVENT.PortcullisClosed)
    if_event_flag_on(1, 61810105)  # Cathedral door is closed.
    if_action_button_state(1, Category.object, OBJ.AsylumDemonFrontDoor, 60.0, 100, 1.5, 10010400)
    if_condition_true(0, 1)
    message.dialog(10010160, ButtonType.yes_no, NumberButtons.no_button, OBJ.AsylumDemonFrontDoor, 3.0)
    restart()


def event11812004():
    """ Just kill Asylum Demon if you start the battle, drop into the Stray pit, and somehow make it back here without
    the Asylum Demon dying on its own (e.g. if it never fell in).

    Note that there's no way for the player to get to or respawn at the first bonfire without triggering this or
    otherwise killing the Asylum Demon.
    """
    header(11812004)
    end_if_event_flag_on(EVENT.AsylumDemonDead)

    if_event_flag_on(1, 11815393)
    if_event_flag_off(1, 11810312)  # Player hasn't escaped first encounter via portcullis.
    if_event_flag_off(1, EVENT.AsylumDemonDead)
    if_player_within_distance(1, OBJ.FirstBonfire, 10.0)
    if_condition_true(0, 1)
    chr.kill(CHR.AsylumDemon)
    # Front door of arena will open when boss dies.


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
