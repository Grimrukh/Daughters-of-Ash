
import sys
import inspect
from pydses import *

map_name = 'm11_00_00_00'  # Painted World of Ariamis
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11100000
BASE_PART = 1100000


class DEBUG(IntEnum):
    COURTYARD_DOOR_OPEN = False
    ARIAMIS_WARP = False
    GET_ANNEX_KEY = False
    VELKA_PACT_MADE = False


class CHR(IntEnum):
    WickedDelys = 6840
    UnmaskedSealer = 6870
    Player = 10000
    Priscilla = 1100160
    PriscillaTail = 1100161
    FiresageDemon = 1100875
    GiantCrow = 1100876
    GiantCrowInteraction = 1100877
    GiantCrowRotate = 1100878
    BonfireEngorgedHollow = 1100879
    Ariamis = 1100880
    AriamisTail = 1100881
    SenBeyondStatue = 1100882


BerenikeTrio = (1100400, 1100401, 1100402)


class EVENT(IntEnum):
    PriscillaDead = 4
    PriscillaHostile = 1691
    VelkaPactMade = 1910
    FromBaneWarp = 11002001
    BeyondWitness = 11502023
    CrowFromPaintedWorld = 11102003
    CrowHurtInFirelink = 11022003
    AriamisWarp = 11102004
    AriamisWarpTemp = 11105350
    CiaranFirstBattleStarted = 11312008
    CiaranSecondBattleStarted = 11312009
    CiaranSecondBattleDone = 11312012
    BondBeyondObtained = 50004930


class GOOD(IntEnum):
    PeculiarDoll = 384
    AnnexKey = 2009
    MasterKey = 2100


class ITEMLOT(IntEnum):
    WingedMoteGeneric = 1540
    VelkaGift = 1650  # Ring of Condemnation.
    AriamisReward = 1690
    AriamisTailCut = 1700
    BondToBeyond = 4930
    PaintedTrioReward = 25702000


class REGION(IntEnum):
    FiresageDemonArena = 1102875
    RaftersSlimeTrigger = 1102675
    SewerSlimeTrigger1 = 1102676
    SewerSlimeTrigger2 = 1102677
    SewerSlimeTrigger3 = 1102678
    SewerSlimeTrigger4 = 1102679
    WellCollapseTrigger = 1102876


class OBJ(IntEnum):
    CliffCorpse1 = 1101675
    CliffCorpse2 = 1101676
    PhalanxCorpse = 1101677


class TEXT(IntEnum):
    ReturnToFirelinkShrine = 10010409
    MemoryFades = 10010195
    ReturnPaintedDoll = 10010196
    UsedAnnexKey = 10010868
    MasterKeyShattered = 10010883
    ExamineStatue = 10010716
    BeyondStatue = 10010720


def event0():
    header(0, 0)

    if DEBUG.COURTYARD_DOOR_OPEN:
        flag.enable(11100030)
    if DEBUG.ARIAMIS_WARP:
        flag.enable(EVENT.AriamisWarp)
    if DEBUG.GET_ANNEX_KEY:
        item.award_item_to_host_only(1100140)
    if DEBUG.VELKA_PACT_MADE:
        item.award_item_to_host_only(ITEMLOT.VelkaGift)
        flag.enable(EVENT.VelkaPactMade)

    # Setup area if this is Ariamis warp.
    run_event(11102005)  # Area setup.

    # Register bonfire. Crows will keep attacking you here until you've killed them both.
    map.register_bonfire(11100992, 1101960)

    # Register ladders. Note ladder 1101141 is only run later (in 50) if you aren't in Shiva's world.
    for ladder_flag_1, ladder_flag_2, ladder_id in zip((10, 14, 16), (11, 15, 17), (140, 142, 143)):
        map.register_ladder(BASE_FLAG + ladder_flag_1, BASE_FLAG + ladder_flag_2, 1101000 + ladder_id)

    skip_if_client(1)
    flag.disable(11100410)

    # Wicked Delys defeated (corpse with loot spawns on suspension bridge).
    skip_if_event_flag_on(2, 11100810)
    obj.disable_treasure(1101610)
    obj.disable(1101610)
    skip_if_event_flag_off(1, 11100810)
    obj.enable_treasure(1101610)

    # (New) Ariamis events and tail.
    run_event(11102006)  # Tail cut.

    # Gravelording.
    run_event(11105070)
    run_event(11105071)
    run_event(11105072)

    run_event(11102000)  # (New) Giant Crow appears at the start if you have some item and takes you to Firelink.
    run_event(11102001)  # (New) Firesage Demon only has AI inside the cylinder room (to limited height).
    run_event(11102002)  # (New) Firesage Demon dies and doesn't respawn.
    run_event(11102044)  # (New) Monitor warping to bonfire.
    # Bonfire returned to original position.
    # run_event(11102009)  # (New) Crows won't attack you at bonfire once both are killed together.

    run_event(11105399)  # Reset Priscilla events if the player goes to Anor Londo and comes back (may not reload).
    run_event(11100030)  # Shortcut door (right way).
    run_event(11100031)  # Shortcut door (wrong way).
    run_event(11100136)  # Turn sewer wheel to open door to Priscilla.
    run_event(11100135)  # Door to Priscilla is locked by some contraption.
    run_event_with_slot(11100120, 0, args=(11100120, TEXT.UsedAnnexKey, 1101250, GOOD.AnnexKey))  # Annex.
    run_event_with_slot(11100120, 1, args=(11100121, TEXT.UsedAnnexKey, 1101251, GOOD.AnnexKey))  # Sewer (new).
    run_event(11100710)  # Exit to Anor Londo.
    run_event(11100200)  # Crow Demon logic manager (many sub-events).
    run_event_with_slot(11100600, 0, args=(1101650, 11100650))  # Chest.
    # Hanging Hollows.
    for slot, enemy_id in enumerate(range(1100100, 1100103)):
        run_event_with_slot(11105150, slot, args=(enemy_id,))
    run_event_with_slot(11105160, 0, args=(1100104, 1102006))
    run_event_with_slot(11105160, 1, args=(1100105, 1102001))
    run_event_with_slot(11105170, 0, args=(1100130, 1102202, 0.2), arg_types='iif')
    run_event_with_slot(11105170, 1, args=(1100132, 1102202, 0.0), arg_types='iif')
    run_event_with_slot(11105170, 2, args=(1100135, 1102202, 0.4), arg_types='iif')
    run_event_with_slot(11105170, 3, args=(1100136, 1102202, 0.6), arg_types='iif')
    run_event_with_slot(11105170, 4, args=(1100137, 1102007, 0.3), arg_types='iif')
    run_event_with_slot(11105170, 5, args=(1100138, 1102007, 0.0), arg_types='iif')

    # Crows "flock".
    run_event(11106299)

    # Crows fly away.
    for (slot, crow_id, trigger_id, animation_id, flag_id) in (
            (0, 1101011, 1101011, 12, -1),
            (1, 1101012, 1101012, 13, 11006200),
            (2, 1101013, 1101011, 12, 11006200),
            (3, 1101014, 1101014, 13, 11006200),
            (4, 1101015, 1101016, 12, 11006205),
            (5, 1101016, 1101016, 13, -1),
            (6, 1101017, 1101016, 12, 11006205),
            (7, 1101018, 1101018, 13, -1),
            (8, 1101019, 1101019, 13, -1),
            (9, 1101020, 1101020, 12, -1),
            (13, 1101024, 1101024, 13, -1),
            (14, 1101025, 1101025, 12, -1),
            (18, 1101029, 1101029, 12, -1),
            (19, 1101030, 1101030, 13, -1),
            (24, 1101035, 1101035, 12, -1),
            (27, 1101038, 1101038, 12, -1),
            (28, 1101039, 1101039, 13, -1),
            (29, 1101040, 1101040, 12, -1),
            (30, 1101041, 1101041, 12, -1),
            (31, 1101042, 1101042, 13, -1),
            (32, 1101043, 1101043, 12, -1),
            (33, 1101044, 1101044, 12, -1)):
        run_event_with_slot(11106200, slot, args=(crow_id, trigger_id, animation_id, flag_id))

    # Treasure corpses cut from ropes.
    run_event_with_slot(11100070, 0, args=(1101120, 1101600, 120, 121))
    run_event_with_slot(11100070, 1, args=(1101121, 1101601, 125, 126))

    # Despawn Undead Dragon.
    skip_if_event_flag_off(1, 11100400)
    chr.disable(1100170)

    run_event(11105370)  # Wake up Undead Dragon.
    # Two lanterns that can be destroyed (usually by Undead Dragon presumably).
    run_event_with_slot(11100100, 0, args=(1101180, 1103000))
    run_event_with_slot(11100100, 1, args=(1101181, 1103001))
    run_event(11100400)  # Undead Dragon doesn't respawn. Also sets up legs (1100171).
    run_event(11100401)  # (New) Undead Dragon legs keep going back to standby anim.
    run_event(11105371)  # Wing falls off.

    # (New) Despawn the Sealer when killed.
    run_event(11102010)

    # (New) Slimes fall from above.
    run_event_with_slot(11005100, 0, args=(REGION.RaftersSlimeTrigger, 1100250, 1.0), arg_types='iif')
    run_event_with_slot(11005100, 1, args=(REGION.SewerSlimeTrigger1, 1100251, 0.0), arg_types='iif')
    run_event_with_slot(11005100, 2, args=(REGION.SewerSlimeTrigger2, 1100252, 0.0), arg_types='iif')
    run_event_with_slot(11005100, 3, args=(REGION.SewerSlimeTrigger3, 1100253, 0.0), arg_types='iif')
    run_event_with_slot(11005100, 4, args=(REGION.SewerSlimeTrigger4, 1100254, 0.0), arg_types='iif')

    run_event(11102011)  # (New) Disable snow on well unless this is Ariamis warp.
    run_event(11102012)  # (New) Berenike Knights all aggro together.
    run_event(11102013)  # (New) Interact with Sen's Beyond statue.
    run_event(11102015)  # (New) Marks when you received Hallowed Ember for Firelink safety chest.
    run_event(11102016)  # (New) Marks when you received Profane Ember for Firelink safety chest.
    run_event(11102017)  # (New) Changes your respawn point to bridge and heals you when you arrive from Bane warp.

    # (New) Invisible Bonewheels fade in.
    run_event_with_slot(11102020, 0, args=(1100350, 1100350, 5.0, 2.0), arg_types='iiff')
    run_event_with_slot(11102020, 1, args=(1100351, 1100350, 5.0, 6.0), arg_types='iiff')
    run_event_with_slot(11102020, 2, args=(1100352, 1100350, 5.0, 6.0), arg_types='iiff')
    run_event_with_slot(11102020, 3, args=(1100353, 1100350, 5.0, 6.0), arg_types='iiff')
    run_event_with_slot(11102020, 4, args=(1100354, 1100354, 5.0, 2.0), arg_types='iiff')
    run_event_with_slot(11102020, 5, args=(1100355, 1100354, 5.0, 2.0), arg_types='iiff')
    run_event_with_slot(11102020, 6, args=(1100356, 1100356, 5.0, 3.0), arg_types='iiff')
    run_event_with_slot(11102020, 7, args=(1100357, 1100357, 6.0, 2.0), arg_types='iiff')
    run_event_with_slot(11102020, 8, args=(1100358, 1100358, 5.0, 3.0), arg_types='iiff')

    # CROSSBREED PRISCILLA

    sound.disable_map_sound(1103800)
    obj.disable(1101992)  # Rear fog.
    sfx.delete_map_sfx(1101993, False)  # Rear fog.
    skip_if_event_flag_off(4, EVENT.PriscillaDead)
    run_event(11105392)
    obj.disable(1101990)
    sfx.delete_map_sfx(1101991, False)
    skip(9)
    run_event(11105390)
    run_event(11105391)
    run_event(11105393)
    run_event(11105392)
    run_event(11100000)
    run_event(11105394)
    run_event(11105395)
    # No tail cut.
    run_event(11105397)  # Warp Priscilla to one of ten random locations when she turns invisible and disable health.
    run_event(11105398)  # Enable health when Priscilla is staggered and turns visible.


def event50():
    """ Pre-constructor for NPC events. Aiming to restore Shiva invasion. """
    header(50, 0)
    run_event(11100420)
    run_event(11102014)  # Controls Hallowed/Profane Ember appearance based on Velka's pact.

    # WICKED DELYS (invasion)

    chr.humanity_registration(6840, 8964)
    run_event(11105030)  # She invades.
    run_event(11100810)  # She dies.

    run_event(11105010)  # Phalanx setup.

    # Priscilla starts off friendly.
    skip_if_event_flag_on(1, EVENT.PriscillaHostile)
    chr.set_team_type(1100160, TeamType.ally)
    run_event_with_slot(11100530, 0, args=(1100160, 1690, 1693, 1691))  # Priscilla hostile.
    run_event_with_slot(11100531, 0, args=(1100160, 1690, 1693, 1692))  # Priscilla dead.

    # Shiva invasion events deleted. Similar logic used for Ariamis memory.


def event11100400():
    """ Undead Dragon death script. Now disables gravity of legs. """
    header(11100400, 1)
    chr.enable_immortality(1100171)
    chr.enable_invincibility(1100171)
    chr.disable_health_bar(1100171)
    chr.disable_gravity(1100171)
    skip_if_this_event_off(2)
    chr.disable(1100170)
    end()
    chr.enable_backread(1100170)
    chr.disable_gravity(1100170)
    if_entity_dead(0, 1100170)
    flag.enable(11100400)


def event11102000():
    """ Giant Crow appears if you have the bonfire here and takes you to Firelink. """
    header(11102000, 1)
    chr.disable(CHR.GiantCrow)
    chr.disable(CHR.GiantCrowRotate)
    if_event_flag_off(0, EVENT.CrowHurtInFirelink)  # Crow has not been hurt in Firelink Shrine afterward.
    chr.enable(CHR.GiantCrow)
    chr.enable_immortality(CHR.GiantCrow)
    if_action_button_state(1, Category.character, CHR.GiantCrowInteraction, 180.0, -1, 3.0, TEXT.ReturnToFirelinkShrine)
    if_entity_health_less_than_or_equal(2, CHR.GiantCrow, 0.3)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    skip_if_condition_false_finished(5, 2)
    chr.disable(CHR.GiantCrow)
    chr.enable(CHR.GiantCrowRotate)
    anim.force_animation(CHR.GiantCrowRotate, 7000, wait_for_completion=True)
    chr.disable(CHR.GiantCrowRotate)
    end()
    flag.enable(EVENT.CrowFromPaintedWorld)  # Permanent flag for Crow position in Firelink.
    warp.warp_player(10, 2, 1020990)


def event11102001():
    """ Firesage Demon attacks only if you're in his arena. """
    header(11102001, 1)
    end_if_event_flag_on(11102002)  # Firesage Demon is dead.
    chr.disable_ai(CHR.FiresageDemon)
    if_player_inside_region(0, REGION.FiresageDemonArena)
    chr.enable_ai(CHR.FiresageDemon)
    if_player_outside_area(0, REGION.FiresageDemonArena)
    restart()


def event11102002():
    """ Firesage Demon dies and doesn't respawn (and clears fog). """
    header(11102002, 1)
    skip_if_this_event_off(4)
    chr.disable(CHR.FiresageDemon)
    obj.disable(1101702)
    sfx.delete_map_sfx(1101703, False)
    end()
    if_entity_health_less_than_or_equal(0, CHR.FiresageDemon, 0.0)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)
    obj.disable(1101702)
    sfx.delete_map_sfx(1101703)
    item.award_item_to_host_only(ITEMLOT.WingedMoteGeneric)


def event11102006():
    """ Ariamis tail. """
    header(11102006, 1)
    chr.disable(CHR.AriamisTail)

    skip_if_this_event_off(4)
    chr.set_display_mask(CHR.Ariamis, 0, 0)
    chr.set_hitbox_mask(CHR.Ariamis, 1, 1)
    chr.ai_instruction(CHR.Ariamis, 20, 0)
    end()

    if_event_flag_on(7, EVENT.AriamisWarp)
    if_entity_backread_enabled(7, CHR.Ariamis)
    if_condition_true(0, 1)

    chr.create_multipart_npc_part(CHR.Ariamis, 3451, 1, 200, 1, 1, False, False)
    if_body_part_health_less_than_or_equal(1, CHR.Ariamis, 3451, 0)
    if_entity_health_less_than_or_equal(2, CHR.Ariamis, 0.0)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    end_if_condition_true_finished(2)
    anim.force_animation(CHR.Ariamis, 8000)
    if_has_tae_event(0, CHR.Ariamis, 400)
    chr.enable(CHR.AriamisTail)
    warp.warp_and_copy_floor(CHR.AriamisTail, Category.character, CHR.Ariamis, 19, CHR.Ariamis)
    anim.force_animation(CHR.AriamisTail, 8100)
    chr.set_display_mask(CHR.Ariamis, 0, 0)
    chr.set_hitbox_mask(CHR.Ariamis, 1, 1)
    chr.ai_instruction(CHR.Ariamis, 20, 0)
    chr.replan_ai(CHR.Ariamis)
    if_character_human(-7, CHR.Player)
    if_character_hollow(-7, CHR.Player)
    end_if_condition_false(-7)
    item.award_item_to_host_only(ITEMLOT.AriamisTailCut)


def event11102005():
    """ Ariamis warp events. You're trapped in the courtyard. """
    header(11102005, 1)
    skip_if_event_flag_on(4, EVENT.AriamisWarp)
    chr.disable(CHR.Ariamis)
    obj.disable(1101750)
    sfx.delete_map_sfx(1101751, False)
    end()

    flag.enable(EVENT.AriamisWarpTemp)
    flag.disable(EVENT.AriamisWarp)

    obj.enable(1101750)
    sfx.create_map_sfx(1101751)

    # Handle possibility that the player just left the Ciaran battle.
    flag.disable(EVENT.CiaranFirstBattleStarted)
    flag.disable(EVENT.CiaranSecondBattleStarted)
    flag.enable(EVENT.CiaranSecondBattleDone)  # Ciaran encounter is over for good.

    chr.enable_immortality(CHR.Ariamis)
    chr.disable_health_bar(CHR.Ariamis)

    chr.disable(CHR.FiresageDemon)
    for phalanx_id in range(1100200, 1100214):
        chr.disable(phalanx_id)
    for cliff_enemy in range(1100400, 1100405):
        chr.disable(cliff_enemy)
    for annex_hollow in range(1100410, 1100416):
        chr.disable(annex_hollow)
    chr.disable(CHR.UnmaskedSealer)
    for treasure in (OBJ.CliffCorpse1, OBJ.CliffCorpse2, OBJ.PhalanxCorpse):
        obj.disable(treasure)
        obj.disable_treasure(treasure)

    run_event(11102007)  # Get too far away from Ariamis.
    run_event(11102008)  # Return Painted Doll.


def event11102007():
    """ Teleport back to Depths if player gets too far away from Ariamis. """
    header(11102007)
    if_player_beyond_distance(0, CHR.Ariamis, 45.0)
    message.status_explanation(TEXT.MemoryFades, True)
    wait(8.0)
    if_player_beyond_distance(1, CHR.Ariamis, 45.0)
    restart_if_condition_false(1)
    warp.warp_player(10, 0, 1000990)


def event11102008():
    """ Exchange Painted Doll with Ariamis for Mark of Stone, and lose access to the Painted World. """
    header(11102008)
    if_host(1)
    if_player_has_good(1, GOOD.PeculiarDoll)
    if_action_button_state(1, Category.character, CHR.Ariamis, 180.0, 1, 5.0, TEXT.ReturnPaintedDoll)
    if_condition_true(0, 1)
    item.remove_items_from_player(ItemType.good, GOOD.PeculiarDoll, 0)
    item.award_item_to_host_only(ITEMLOT.AriamisReward)
    wait(5.0)
    message.status_explanation(TEXT.MemoryFades, True)
    wait(5.0)
    warp.warp_player(10, 0, 1000990)


def event11100120():
    """ Unlock Annex door or new sewer exit door with Annex Key. """
    header(11100120)
    objact_id, key_message, door_id, key_id, open_flag = define_args('iiiii')
    end_if_this_event_slot_on()
    if_host(1)
    if_object_activated(1, objact_id)
    if_condition_true(0, 1)
    message.dialog(key_message, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)


def event11102009():
    """ Kill Engorged Hollow and Crow Demons on top of first building to prevent the Hollow from respawning,
    and the Crows from attacking you here. """
    header(11102009, 1)
    skip_if_this_event_off(2)
    chr.disable(CHR.BonfireEngorgedHollow)
    end()
    if_entity_health_less_than_or_equal(1, CHR.BonfireEngorgedHollow, 0.0)
    if_entity_health_less_than_or_equal(1, 1100300, 0.0)
    if_entity_health_less_than_or_equal(1, 1100301, 0.0)
    if_condition_true(0, 1)
    flag.enable(11102009)


def event11105030():
    """ Wicked Delys invasion. """
    header(11105030)
    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11105031)
    # NOTE: No longer requires Priscilla to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 11100810)
    skip_if_this_event_on(1)
    if_player_inside_region(1, 1102011)
    if_condition_true(0, 1)
    message.place_summon_sign(SummonSignType.black_eye_sign, CHR.WickedDelys, 1102010, 11105031, 11105032)
    wait(20.0)
    restart()


def event11100810():
    """ Wicked Delys dies. """
    header(11100810)
    skip_if_host(3)
    if_event_flag_on(1, 11105031)
    if_event_flag_off(1, 11105032)
    skip_if_condition_true(1, 1)
    chr.disable(CHR.WickedDelys)
    end_if_this_event_on()
    if_entity_dead(0, CHR.WickedDelys)
    flag.enable(11100810)


def event11102010():
    """ Sealer NPC dies and doesn't respawn, nor do two of the Torch Hollows. """
    header(11102010, 1)
    skip_if_this_event_off(3)
    chr.drop_mandatory_treasure(CHR.UnmaskedSealer)
    chr.disable(1100414)  # Torch Hollow at back of annex room.
    end()
    chr.disable(1100403)  # ... same Torch Hollow on cliff-side.
    if_entity_health_less_than_or_equal(0, CHR.UnmaskedSealer, 0.0)
    end()


def event11100200():
    """ Crow Demon manager.
    Demons 300 and 301 are perched on top of the left building.
    Demons 302 and 303 are already on top of the right building.
    Three more anonymous demons are at the top of the 'floating' spiral stairs in the tower.
    """
    header(11100200, 1)

    # Perched Demons triggered in region 1102040 *or* 1202021 (top of the first building) if you pick up treasure 260.
    run_event_with_slot(11105190, 0, args=(1100300, 3010, 3011, 11105230, 11105232))
    run_event_with_slot(11105190, 1, args=(1100301, 3012, 3013, 11105234, 11105236))

    # Rooftop Demons play animation 3006 when they enter battle mode or you enter region 1102050.
    run_event_with_slot(11105195, 0, args=(1100302, 11105240))
    run_event_with_slot(11105195, 1, args=(1100303, 11105244))

    # Complicated events basically change Demon nests and AI event locations in the different areas.
    """
    If Arg1 is enabled (from above), and player is inside a certain area AND the corresponding flag (see below) is off,
    then enable Arg2 (to trigger battle), restart appropriate slot of 11105220 (battle countdown), then switch based on
    the area trigger. For each of the four area flags per enemy (5230-5245), restart the corresponding slot of that
    enemy's event (5250/5260/5270/5280) if that flag is ON. 
    """
    #                                                        TRIGGER/NEST:  1102020   1102030   1102040   1102050
    run_event_with_slot(11105200, 0, args=(11105190, 11105210, 0, 11105250, 11105230, 11105231, 11105232, 11105233))
    run_event_with_slot(11105200, 1, args=(11105191, 11105211, 1, 11105260, 11105234, 11105235, 11105236, 11105237))
    run_event_with_slot(11105200, 2, args=(11105195, 11105212, 2, 11105270, 11105238, 11105239, 11105240, 11105241))
    run_event_with_slot(11105200, 3, args=(11105196, 11105213, 3, 11105280, 11105242, 11105243, 11105244, 11105245))

    # Reset AI event to default (battle) if second argument flag is enabled for an extended time.
    run_event_with_slot(11105220, 0, args=(1100300, 11105210, 10.0, 11105250), arg_types='iifi')
    run_event_with_slot(11105220, 1, args=(1100301, 11105211, 10.0, 11105260), arg_types='iifi')
    run_event_with_slot(11105220, 2, args=(1100302, 11105212, 10.0, 11105270), arg_types='iifi')
    run_event_with_slot(11105220, 3, args=(1100303, 11105213, 10.0, 11105280), arg_types='iifi')

    run_event_with_slot(11105250, 0, args=(11105210, 1100300, 1, 1102040, 11105230, 11105233, 11105232))  # 1102710
    run_event_with_slot(11105250, 1, args=(11105210, 1100300, 2, 1102020, 11105230, 11105233, 11105230))  # 1102712
    run_event_with_slot(11105250, 2, args=(11105210, 1100300, 3, 1102030, 11105230, 11105233, 11105231))  # 1102710
    run_event_with_slot(11105250, 3, args=(11105210, 1100300, 4, 1102020, 11105230, 11105233, 11105230))  # 1102711
    run_event_with_slot(11105250, 4, args=(11105210, 1100300, 5, 1102050, 11105230, 11105233, 11105233))  # 1102712
    run_event_with_slot(11105250, 5, args=(11105210, 1100300, 6, 1102040, 11105230, 11105233, 11105232))  # 1102713

    run_event_with_slot(11105260, 0, args=(11105211, 1100301, 1, 1102040, 11105234, 11105237, 11105236))
    run_event_with_slot(11105260, 1, args=(11105211, 1100301, 2, 1102020, 11105234, 11105237, 11105234))
    run_event_with_slot(11105260, 2, args=(11105211, 1100301, 3, 1102030, 11105234, 11105237, 11105235))
    run_event_with_slot(11105260, 3, args=(11105211, 1100301, 4, 1102020, 11105234, 11105237, 11105234))
    run_event_with_slot(11105260, 4, args=(11105211, 1100301, 5, 1102050, 11105234, 11105237, 11105237))
    run_event_with_slot(11105260, 5, args=(11105211, 1100301, 6, 1102040, 11105234, 11105237, 11105236))

    run_event_with_slot(11105270, 0, args=(11105212, 1100302, 1, 1102040, 11105238, 11105241, 11105240))
    run_event_with_slot(11105270, 1, args=(11105212, 1100302, 2, 1102020, 11105238, 11105241, 11105238))
    run_event_with_slot(11105270, 2, args=(11105212, 1100302, 3, 1102030, 11105238, 11105241, 11105239))
    run_event_with_slot(11105270, 3, args=(11105212, 1100302, 4, 1102020, 11105238, 11105241, 11105238))
    run_event_with_slot(11105270, 4, args=(11105212, 1100302, 5, 1102050, 11105238, 11105241, 11105241))
    run_event_with_slot(11105270, 5, args=(11105212, 1100302, 6, 1102040, 11105238, 11105241, 11105240))

    run_event_with_slot(11105280, 0, args=(11105213, 1100303, 1, 1102040, 11105242, 11105245, 11105244))
    run_event_with_slot(11105280, 1, args=(11105213, 1100303, 2, 1102020, 11105242, 11105245, 11105242))
    run_event_with_slot(11105280, 2, args=(11105213, 1100303, 3, 1102030, 11105242, 11105245, 11105243))
    run_event_with_slot(11105280, 3, args=(11105213, 1100303, 4, 1102020, 11105242, 11105245, 11105242))
    run_event_with_slot(11105280, 4, args=(11105213, 1100303, 5, 1102050, 11105242, 11105245, 11105245))
    run_event_with_slot(11105280, 5, args=(11105213, 1100303, 6, 1102040, 11105242, 11105245, 11105244))


def event11005100():
    """ Slimes fall from above. """
    header(11005100, 1)
    trigger_region, slime, delay = define_args('iif')
    skip_if_this_event_slot_on(6)
    chr.disable_gravity(slime)
    chr.disable_collision(slime)
    if_player_inside_region(-1, trigger_region)
    if_entity_attacked_by(-1, slime, CHR.Player)
    if_condition_true(0, -1)
    wait(delay)
    chr.enable_gravity(slime)
    chr.enable_collision(slime)
    chr.set_standby_animation_settings_to_default(slime)


def event11105190():
    """ First two Crow Demons ambush. They now only attack the first building if the bonfire hasn't appeared. """
    header(11105190, 2)
    crow, bonfire_swoop_animation, annex_swoop_animation, bonfire_battle_flag, annex_battle_flag = define_args('iiiii')
    skip_if_this_event_slot_off(2)
    chr.set_standby_animation_settings_to_default(crow)
    end()

    chr.disable_collision(crow)
    chr.disable_gravity(crow)
    chr.set_special_effect(crow, 4160)
    if_event_flag_off(1, 11102009)
    if_player_inside_region(1, 1202021)
    if_player_inside_region(2, 1102040)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    chr.enable_collision(crow)
    chr.enable_gravity(crow)
    chr.set_standby_animation_settings_to_default(crow)

    skip_if_condition_false_finished(5, 1)
    anim.force_animation(crow, bonfire_swoop_animation, wait_for_completion=True)
    chr.cancel_special_effect(crow, 4160)
    chr.set_nest(crow, 1102020)
    flag.enable(bonfire_battle_flag)
    restart()

    anim.force_animation(crow, annex_swoop_animation, wait_for_completion=True)
    chr.cancel_special_effect(crow, 4160)
    chr.set_nest(crow, 1102040)
    flag.enable(annex_battle_flag)
    restart()


def event11102011():
    """ Simply remove snow on well, unless this is Ariamis warp, and always disable ladder. """
    header(11102011)
    obj.disable(1101141)

    # Ariamis warp: leave snow on well and don't register ladder.
    end_if_event_flag_on(EVENT.AriamisWarp)
    end_if_event_flag_on(EVENT.AriamisWarpTemp)

    map.disable_map_part(1103100)
    hitbox.disable_hitbox(1103101)


def event11102020():
    """ Invisible Bonewheels fade in some time after you approach them (only once). """
    header(11102020, 1)
    bonewheel, trigger_entity, trigger_distance, delay = define_args('iiff')
    end_if_this_event_slot_on()
    chr.disable(bonewheel)
    if_player_within_distance(0, trigger_entity, trigger_distance)
    wait(delay)
    if_player_beyond_distance(0, bonewheel, 1.0)
    chr.enable(bonewheel)
    anim.force_animation(bonewheel, 6)


def event11102012():
    """ Berenike Knights all aggro together (then despawn). """
    header(11102012, 1)
    skip_if_this_event_off(2 * len(BerenikeTrio) + 1)
    for knight in BerenikeTrio:
        chr.disable(knight)
        chr.kill(knight, False)
    end()

    for knight in BerenikeTrio:
        chr.disable_ai(knight)

    if_event_flag_off(1, EVENT.AriamisWarp)
    if_event_flag_off(1, EVENT.AriamisWarpTemp)
    for knight in BerenikeTrio:
        if_player_within_distance(-1, knight, 8.0)
        if_entity_attacked_by(-1, knight, CHR.Player)
    if_condition_true(1, -1)
    if_condition_true(0, 1)

    chr.enable_ai(1100400)
    chr.enable_ai(1100401)
    chr.enable_ai(1100402)

    if_entity_health_less_than_or_equal(1, 1100400, 0.0)
    if_entity_health_less_than_or_equal(1, 1100401, 0.0)
    if_entity_health_less_than_or_equal(1, 1100402, 0.0)
    if_condition_true(0, 1)

    item.award_item_to_host_only(ITEMLOT.PaintedTrioReward)


def event11105392():
    """ Priscilla battle begins. """
    header(11105392, 1)
    skip_if_event_flag_off(7, EVENT.PriscillaDead)
    chr.disable(CHR.Priscilla)
    chr.disable(CHR.PriscillaTail)
    chr.kill(CHR.Priscilla, False)
    chr.kill(CHR.PriscillaTail, False)
    chr.disable_backread(CHR.Priscilla)
    chr.disable_backread(CHR.PriscillaTail)
    end()

    skip_if_event_flag_off(3, EVENT.PriscillaHostile)
    chr.set_team_type(CHR.Priscilla, TeamType.ally)
    chr.set_standby_animation_settings_to_default(CHR.Priscilla)
    skip(3)
    chr.set_standby_animation_settings(CHR.Priscilla, standby_animation=9000)
    chr.disable_gravity(CHR.Priscilla)
    chr.disable_collision(CHR.Priscilla)

    chr.disable_ai(CHR.Priscilla)
    chr.disable_health_bar(CHR.Priscilla)

    if_entity_alive(1, CHR.Priscilla)
    if_event_flag_on(1, 11105393)
    if_entity_attacked_by(1, CHR.Priscilla, CHR.Player)
    if_event_flag_on(2, 11105393)
    if_player_inside_region(2, 1102100)
    if_event_flag_on(2, EVENT.PriscillaHostile)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    skip_if_condition_false_finished(1, 1)
    chr.set_standby_animation_settings(CHR.Priscilla, cancel_animation=9060)
    chr.enable_gravity(CHR.Priscilla)
    chr.enable_collision(CHR.Priscilla)
    chr.enable_ai(CHR.Priscilla)
    chr.set_team_type(CHR.Priscilla, TeamType.boss)
    boss.enable_boss_health_bar(CHR.Priscilla, 2730)
    chr.set_special_effect(CHR.Priscilla, 2111)
    flag.enable(11105392)

    # So the event can be restarted in Anor Londo if she isn't dead:
    if_event_flag_on(0, EVENT.PriscillaDead)
    end()


def event11100030():
    """ Open one-way courtyard door. Now stays shut in Ariamis memory. """
    header(11100030)

    end_if_event_flag_on(EVENT.AriamisWarp)
    end_if_event_flag_on(EVENT.AriamisWarpTemp)

    skip_if_this_event_slot_off(3)
    anim.end_animation(1101130, 2)
    navimesh.delete_navimesh_collision_bitflags(1102040, NavimeshType.solid)
    end()

    navimesh.add_navimesh_collision_bitflags(1102040, NavimeshType.solid)
    if_action_button_state(0, Category.object, 1101130, 60.0, 100, 1.5, 10010400,
                           reaction_attribute=ReactionAttribute.all, pad_id=0)
    warp.short_warp(CHR.Player, Category.region, 1102090, -1)
    anim.force_animation(CHR.Player, 7120)
    anim.force_animation(1101130, 1, wait_for_completion=True)
    navimesh.delete_navimesh_collision_bitflags(1102040, NavimeshType.solid)


def event11102500():
    """ Determine stable footing in courtyard and cliff edge (disable during Ariamis memory). """
    header(11102500)

    flag.disable(11102501)
    if_event_flag_off(1, EVENT.AriamisWarp)
    if_event_flag_off(1, EVENT.AriamisWarpTemp)
    if_condition_true(0, 1)
    flag.enable(11102501)


def event11100710():
    """ Exit to Anor Londo. Now awards achievement if this is the first time in Anor Londo. """
    header(11100710)
    flag.disable(11105380)
    if_host(1)
    if_event_flag_off(1, 1691)
    if_player_inside_region(1, 1102500)
    if_condition_true(0, 1)
    chr.enable_immortality(CHR.Priscilla)
    end_if_client()
    chr.disable_immortality(CHR.Priscilla)
    flag.enable(11105380)
    skip_if_event_flag_on(1, EVENT.PriscillaDead)
    if_event_flag_on(0, 11105395)

    cutscene.play_cutscene_and_warp_specific_player(110035, CutsceneType.skippable, 1512500, 15, 1, CHR.Player)
    wait_frames(1)

    skip_if_this_event_on(4)
    skip_if_event_flag_off(2, 11500210)
    item.award_item_to_host_only(9030)
    skip(1)
    game.award_achievement(33)

    warp.set_player_respawn_point(1512501)
    network.save_request()
    restart()


def event11102013():
    """ Empyrean Bond statue interaction. """
    header(11102013)

    if_action_button_state(0, Category.character, CHR.SenBeyondStatue, 180.0, -1, 2.0, TEXT.ExamineStatue)

    if_event_flag_on(1, EVENT.BeyondWitness)
    if_event_flag_off(1, EVENT.BondBeyondObtained)
    skip_if_condition_true(2, 1)
    message.dialog(TEXT.BeyondStatue, ButtonType.ok_cancel, NumberButtons.no_button, CHR.SenBeyondStatue, 4.0)
    skip(1)
    item.award_item_to_host_only(ITEMLOT.BondToBeyond)

    wait(3.0)
    restart()


def event11102014():
    """ Hallowed Ember is replaced by Profane Ember if you have a pact with Velka (and reverts if pact is broken). """
    header(11102014)
    # End if statue already looted.
    if_event_flag_on(1, 51100370)
    if_event_flag_on(1, 51100371)
    end_if_condition_true(1)

    skip_if_this_event_on(4)

    if_event_flag_on(0, EVENT.VelkaPactMade)
    flag.enable(51100370)
    flag.disable(51100371)
    flag.enable(11102014)

    if_event_flag_off(0, EVENT.VelkaPactMade)
    flag.disable(51100370)
    flag.enable(51100371)


def event11102015():
    """ Flags that you received the Hallowed Ember for Firelink safety chest. """
    header(11102015)

    if_event_flag_off(1, 51100370)
    if_event_flag_on(1, 51100371)
    if_condition_true(0, 1)

    if_event_flag_on(0, 51100370)  # Only way to enable this *inside* Painted World is by picking up the item.
    end()


def event11102016():
    """ Flags that you received the Profane Ember for Firelink safety chest. """
    header(11102016)

    if_event_flag_on(1, 51100370)
    if_event_flag_off(1, 51100371)
    if_condition_true(0, 1)

    if_event_flag_on(0, 51100371)  # Only way to enable this *inside* Painted World is by picking up the item.
    end()


def event11102017():
    """ Changes your respawn point and heals you when you arrive after Bane warp. """
    header(11102017)

    if_event_flag_on(0, EVENT.FromBaneWarp)
    warp.set_player_respawn_point(1102511)
    chr.set_special_effect(CHR.Player, 3231)  # Heal to full.
    flag.disable(EVENT.FromBaneWarp)


def event11102044():
    """ Monitor resting at Painted World bonfire. """
    header(11102044)
    if_player_within_distance(1, 1101960, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11102044)
    flag.enable(11102045)  # Now on permanent Lordvessel list.


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
