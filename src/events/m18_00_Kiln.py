
import sys
import inspect
from pydses import *

map_name = 'm18_00_00_00'  # Kiln of the First Flame
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'


class DEBUG(IntEnum):
    WARP_TO_GWYN_IMMEDIATELY = False
    VELKA_PACT_MADE = False
    NITO_SEATH_JEREMIAH_PUNISHED = False
    ALL_BLACK_KNIGHTS_DEAD = False
    LORDVESSEL_FULL = False
    GET_ALL_LORD_SOULS = False
    ARTORIAS_SAVED = False


class ANIM(IntEnum):
    TouchBonfire = 7114


class CHR(IntEnum):
    Player = 10000
    Gwyn = 1800800
    Artorias = 1800810
    SifFirst = 1800820
    SifSecond = 1800821
    SifDeath = 1800822
    GiantCrow = 1800875
    GiantCrowFlee = 1800876
    GiantCrowInteraction = 1800877
    GiantCrowDistant = 1800878
    FirelinkAltar = 1800960


class EVENT(IntEnum):
    SifArtoriasManusDead = 5
    GwynCinderDead = 15
    FramptPresent = 830
    KaathePresent = 831
    LordvesselReceived = 11512000
    LordvesselPlaced = 11800100
    LordvesselFull = 11800210
    GwynWarpMessageDone = 11802005
    BlackKnightSwordDead = 11812020
    BlackKnightGreatswordDead = 11012005
    BlackKnightHalberdDead = 11202002
    BlackKnightAxeDead = 11502000
    AllBlackKnightsDead = 11802000
    AnorLondoGwynWarp = 11802002
    GwynLordOfLightDead = 11512201
    VelkaPactMade = 1910
    SeathPunished = 1911
    NitoPunished = 1912
    JeremiahPunished = 1913
    ReturnFromPast = 11512203
    ArtoriasTriggered = 11805396
    ArtoriasDead = 11802007  # Immediately triggers NG+.


class ITEMLOT(IntEnum):
    VelkaGift = 1650
    GwyneveresRing = 1680


class GOOD(IntEnum):
    DeathSoul = 2500
    LifeSoul = 2501
    LightSoulShardFourKings = 2502
    LightSoulShardSeath = 2503
    DarkRemnant = 2505
    Lordvessel = 2510
    ChthonicSpark = 813


class OBJ(IntEnum):
    TheFire = 1801950


class REGION(IntEnum):
    DarkLordEnding = 1802875


class RING(IntEnum):
    AshenRing = 152


class TEXT(IntEnum):
    LordvesselWarpUnlocked = 10010125
    DeathSoulFed = 10010150
    LifeSoulFed = 10010151
    LightSoulFedFourKings = 10010152
    LightSoulFedSeath = 10010153
    DarkRemnantFed = 10010154
    ReturnToFirelinkShrine = 10010409
    CrossTime = 10010602
    AshenRingCleansed = 10010629


def event0():
    """ Constructor. """
    header(0, 0)

    if DEBUG.VELKA_PACT_MADE:
        item.award_item_to_host_only(ITEMLOT.VelkaGift)
        flag.enable(EVENT.VelkaPactMade)
    if DEBUG.NITO_SEATH_JEREMIAH_PUNISHED:
        flag.enable(EVENT.NitoPunished)
        flag.enable(EVENT.SeathPunished)
        flag.enable(EVENT.JeremiahPunished)
    if DEBUG.ALL_BLACK_KNIGHTS_DEAD:
        item.award_item_to_host_only(2750)
        flag.enable(EVENT.BlackKnightSwordDead)
        flag.enable(EVENT.BlackKnightGreatswordDead)
        flag.enable(EVENT.BlackKnightAxeDead)
        flag.enable(EVENT.BlackKnightHalberdDead)
        flag.enable(EVENT.AllBlackKnightsDead)
    if DEBUG.LORDVESSEL_FULL:
        flag.enable(11800201)
        flag.enable(11800202)
        flag.enable(11800203)
        flag.enable(11800204)
        flag.enable(EVENT.LordvesselReceived)
        flag.enable(EVENT.LordvesselPlaced)
        flag.enable(EVENT.LordvesselFull)
    if DEBUG.GET_ALL_LORD_SOULS:
        item.award_item_to_host_only(1090)
        item.award_item_to_host_only(2560)
        item.award_item_to_host_only(2580)
        item.award_item_to_host_only(2630)
        item.award_item_to_host_only(2640)
        item.award_item_to_host_only(2540)
    if DEBUG.ARTORIAS_SAVED:
        flag.enable(5)

    # Firelink Altar bonfire.
    skip_if_event_flag_off(1, 11800100)
    map.register_bonfire(11800992, 1801960, initial_kindle_level=10)  # Lordvessel placed.
    skip_if_event_flag_off(1, 11800210)
    map.register_bonfire(11800992, 1801960, initial_kindle_level=30)  # All Lord Souls added.
    skip_if_client(2)
    obj.disable(1801994)
    sfx.delete_map_sfx(1801995, False)
    # Lordvessel no longer disabled if Gwyn is dead.

    # Gravelording.
    run_event(11805090)
    run_event(11805091)
    run_event(11805092)

    # Note order of these is reversed, so "link" is the default option when you approach.
    run_event(21)  # Ending: player does not link the fire.
    run_event(20)  # Ending: player links the fire.

    run_event(11800100)  # Place Lordvessel at Altar.
    run_event(11800101)  # Inspect Altar without Lordvessel.
    run_event(11800200)  # Give Lord Souls to Lordvessel.
    run_event_with_slot(11800230, 0, args=(1, 180005, 1801960))  # First soul added.
    run_event_with_slot(11800230, 1, args=(2, 180006, 1801960))  # Second soul added.
    run_event_with_slot(11800230, 2, args=(3, 180007, 1801960))  # Third soul added.
    run_event_with_slot(11800230, 3, args=(4, 180008, 1801960))  # Fourth soul added.
    run_event(11800210)  # All Lord Souls added (cutscene).
    run_event(11800220)  # Inspect Lordvessel with no Lord Souls to give.
    for slot, ghost_id in enumerate(range(6)):
        run_event_with_slot(11806100, slot, args=(1800100 + ghost_id, 1802000 + ghost_id))

    run_event(11802001)  # (New) Crow appears to take you to final encounter.
    run_event(11802004)  # (New) Black Knight Phantoms

    if DEBUG.WARP_TO_GWYN_IMMEDIATELY:
        wait(5.0)
        flag.enable(EVENT.AnorLondoGwynWarp)
        warp.warp_player(15, 1, 1510990)


def event50():
    """ NPC constructor. Includes Gwyn. No longer disables enemies when Gwyn dies. """
    header(50, 0)
    run_event(11800002)

    # GWYN, LORD OF CINDER

    sound.disable_map_sound(1803800)
    skip_if_event_flag_off(4, EVENT.GwynCinderDead)
    run_event(11805392)
    obj.disable(1801990)
    sfx.delete_map_sfx(1801991, False)
    skip(7)
    for gwyn_event_id in (5390, 5391, 5393, 5392, 1, 5394, 5395):
        run_event(11800000 + gwyn_event_id)

    # ARTORIAS, THE WOLF KNIGHT

    sound.disable_map_sound(1803801)
    run_event(11802006)
    run_event(11802007)

    # Summon Solaire if he was saved in Lost Izalith.
    chr.humanity_registration(6544, 8310)
    run_event(11805030)
    run_event(11805032)
    run_event_with_slot(11800550, 0, args=(1000, 1029, 1012))

    # Kingseeker Frampt
    chr.enable_immortality(6331)
    skip_if_event_flag_on(1, 1648)
    skip_if_event_flag_on(1, EVENT.FramptPresent)
    chr.disable(6331)
    skip_if_event_flag_on(6, EVENT.GwynCinderDead)
    run_event_with_slot(11800539, 0, args=(6331, 1640, 1647, 1647))
    run_event_with_slot(11800530, 0, args=(6331, 1640, 1647, 1644))
    run_event_with_slot(11800531, 0, args=(6331, 1640, 1647, 1645))
    run_event_with_slot(11800537, 0, args=(6331, 1640, 1647, 1649))
    run_event_with_slot(11800541, 0, args=(6331,))
    run_event(11806200)

    # Darkstalker Kaathe
    chr.enable_immortality(6341)
    skip_if_event_flag_on(1, EVENT.KaathePresent)
    chr.disable(6341)
    skip_if_event_flag_on(6, EVENT.GwynCinderDead)
    run_event_with_slot(11800540, 0, args=(6341, 1670, 1677, 1677))
    run_event_with_slot(11800533, 0, args=(6341, 1670, 1677, 1673))
    run_event_with_slot(11800534, 0, args=(6341, 1670, 1677, 1674))
    run_event_with_slot(11800538, 0, args=(6341, 1670, 1677, 1678))
    run_event_with_slot(11800542, 0, args=(6341,))
    run_event(11806201)


def event11802001():
    """ Crow appears to take you to Gwyn if you have punished Seath, Nito, and Jeremiah, and killed Lord of Cinder. """
    header(11802001, 1)
    chr.disable(CHR.GiantCrowFlee)
    chr.disable(CHR.GiantCrow)

    # Crow disappears from Kiln when pact is fulfilled.
    skip_if_event_flag_off(2, EVENT.GwynLordOfLightDead)
    chr.disable(CHR.GiantCrowDistant)
    end()

    if_event_flag_on(1, EVENT.VelkaPactMade)
    if_event_flag_on(1, EVENT.SeathPunished)
    if_event_flag_on(1, EVENT.NitoPunished)
    if_event_flag_on(1, EVENT.JeremiahPunished)
    if_event_flag_on(1, EVENT.GwynCinderDead)
    if_condition_true(0, 1)

    chr.disable(CHR.GiantCrowDistant)
    chr.enable(CHR.GiantCrow)
    chr.disable_gravity(CHR.GiantCrow)
    chr.enable_invincibility(CHR.GiantCrow)

    if_action_button_state(1, Category.character, CHR.GiantCrowInteraction, 180.0, -1, 5.0, TEXT.CrossTime)
    if_entity_health_less_than_or_equal(2, CHR.GiantCrow, 0.3)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    skip_if_condition_false_finished(5, 2)
    chr.disable(CHR.GiantCrow)
    chr.enable(CHR.GiantCrowFlee)
    anim.force_animation(CHR.GiantCrowFlee, 7000, wait_for_completion=True)
    chr.disable(CHR.GiantCrowFlee)
    end()
    flag.enable(EVENT.AnorLondoGwynWarp)
    warp.warp_player(15, 1, 1510990)


def event11800001():
    """ Gwyn, Lord of Cinder dies. Now enables a different flag to give you his soul. Flag 15 is enabled when either
    Gwyn is killed. Also gives Gwynevere's Ring if all four Black Knights are dead. """
    header(11800001)
    obj.disable(1801111)
    obj.disable(OBJ.TheFire)
    if_entity_dead(0, CHR.Gwyn)
    flag.enable(EVENT.GwynCinderDead)
    flag.enable(11800001)  # Gives rewards.
    boss.kill_boss(CHR.Gwyn)
    obj.disable(1801990)
    sfx.delete_map_sfx(1801991, True)
    skip_if_client(1)
    network.save_request()
    flag.disable(11807200)
    flag.disable(11807210)
    flag.disable(11807220)
    flag.disable(11807240)
    # Lordvessel no longer disabled here.
    sfx.create_oneoff_sfx(Category.object, OBJ.TheFire, -1, 90014)
    wait(2.0)
    obj.enable(OBJ.TheFire)

    # Disable Frampt. (No change to Kaathe.)
    chr.disable(6331)

    # Switch to rotated Black Knights.
    skip_if_event_flag_off(2, EVENT.BlackKnightSwordDead)
    chr.disable(1800200)
    chr.enable(1800210)
    chr.disable_gravity(1800210)
    chr.enable_invincibility(1800210)
    skip_if_event_flag_off(2, EVENT.BlackKnightSwordDead)
    chr.disable(1800201)
    chr.enable(1800211)
    chr.disable_gravity(1800211)
    chr.enable_invincibility(1800211)
    skip_if_event_flag_off(2, EVENT.BlackKnightSwordDead)
    chr.disable(1800202)
    chr.enable(1800212)
    chr.disable_gravity(1800212)
    chr.enable_invincibility(1800212)
    skip_if_event_flag_off(2, EVENT.BlackKnightSwordDead)
    chr.disable(1800203)
    chr.enable(1800213)
    chr.disable_gravity(1800213)
    chr.enable_invincibility(1800213)

    skip_if_event_flag_off(5, EVENT.AllBlackKnightsDead)
    wait(2.0)
    message.status_explanation(TEXT.AshenRingCleansed, True)
    wait(1.0)
    item.remove_items_from_player(ItemType.ring, RING.AshenRing, 0)
    item.award_item_to_host_only(ITEMLOT.GwyneveresRing)


def event20():
    """ Link the Fire and end the game. (You can now leave the chamber without making a decision.) """
    header(20)
    end_if_client()
    if_event_flag_on(1, EVENT.GwynCinderDead)
    if_event_flag_off(1, EVENT.ArtoriasTriggered)
    if_action_button_state(1, 'object', OBJ.TheFire, 180.0, -1, 1.5, 10010108)
    if_event_flag_off(1, 20)
    if_event_flag_off(1, 21)
    if_condition_true(0, 1)
    game.increment_new_game_plus_counter()
    # Delete Lordvessel for cutscene.
    obj.disable(1801960)
    obj.disable(1801110)
    obj.enable(1801111)
    sfx.delete_object_sfx(1801960, True)
    cutscene.play_cutscene_to_player(180000, CutsceneType.skippable, CHR.Player)
    wait_frames(1)
    game.award_achievement(1)
    flag.enable(20)
    # Re-enable Lordvessel.
    obj.enable(1801960)
    obj.enable(1801110)
    obj.disable(1801111)


def event21():
    """ Abandon the Fire and end the game. (You can now leave the chamber without making a decision.)

    If Artorias was rescued, you will fight him one last time here.
    """
    header(21)
    end_if_client()
    if_event_flag_on(1, EVENT.GwynCinderDead)
    if_event_flag_off(1, EVENT.ArtoriasTriggered)
    if_action_button_state(1, 'object', OBJ.TheFire, 180.0, -1, 1.5, 10010109)
    if_event_flag_off(1, 20)
    if_event_flag_off(1, 21)
    if_condition_true(0, 1)

    # Artorias attacks you.
    skip_if_event_flag_off(2, EVENT.SifArtoriasManusDead)
    flag.enable(EVENT.ArtoriasTriggered)
    if_event_flag_on(0, EVENT.ArtoriasDead)

    game.increment_new_game_plus_counter()
    # Delete Lordvessel for cutscene.
    obj.disable(1801960)
    obj.disable(1801110)
    obj.enable(1801111)
    sfx.delete_object_sfx(1801960, True)
    cutscene.play_cutscene_to_player(180001, CutsceneType.skippable, CHR.Player)
    wait_frames(1)
    game.award_achievement(2)
    flag.enable(21)
    # Re-enable Lordvessel.
    obj.enable(1801960)
    obj.enable(1801110)
    obj.disable(1801111)


def event11802004():
    """ Black Knights who you have defeated will appear on the final staircase until you defeat the Lord of Light. """
    header(11802004, 1)
    chr.disable(1800210)
    chr.disable(1800211)
    chr.disable(1800212)
    chr.disable(1800213)
    skip_if_event_flag_off(5, EVENT.GwynLordOfLightDead)
    chr.disable(1800200)
    chr.disable(1800201)
    chr.disable(1800202)
    chr.disable(1800203)
    end()

    for knight_flag, knight_id in zip((EVENT.BlackKnightSwordDead, EVENT.BlackKnightGreatswordDead,
                                       EVENT.BlackKnightAxeDead, EVENT.BlackKnightHalberdDead),
                                      (1800200, 1800201, 1800202, 1800203)):
        skip_if_event_flag_on(2, knight_flag)
        chr.disable(knight_id)
        skip(2)
        chr.disable_gravity(knight_id)
        chr.enable_invincibility(knight_id)


def event11800002():
    """ Disable non-phantom enemies when Gwyn dies. """
    header(11800002, 1)
    if_event_flag_on(0, EVENT.GwynCinderDead)
    for black_phantom in range(1800900, 1800905):
        chr.disable(black_phantom)
        chr.kill(black_phantom, False)
    for vagrant in range(1803900, 1803903):
        chr.disable(vagrant)
        chr.kill(vagrant, False)


def event11800200():
    """ Add Lord Souls to Lordvessel, now including Dark Remnant. Also now fed one at a time. """
    header(11800200)
    if_event_flag_on(0, 756)  # Flag enabled when feed option is selected in Lordvessel bonfire menu.
    anim.force_animation(CHR.Player, 7697)  # Feeding animation.
    wait_frames(75)

    if_event_flag_off(1, 11800201)
    if_player_has_good(1, GOOD.DeathSoul)
    if_event_flag_off(2, 11800202)
    if_player_has_good(2, GOOD.LifeSoul)
    if_event_flag_off(3, 11800203)
    if_player_has_good(3, GOOD.LightSoulShardFourKings)
    if_event_flag_off(4, 11800204)
    if_player_has_good(4, GOOD.LightSoulShardSeath)
    if_event_flag_off(5, 11800205)
    if_player_has_good(5, GOOD.DarkRemnant)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(-1, 4)
    if_condition_true(-1, 5)
    if_condition_true(0, -1)

    skip_if_condition_false_finished(4, 1)
    flag.enable(11800201)
    item.remove_items_from_player(ItemType.good, GOOD.DeathSoul, 0)
    message.dialog(TEXT.DeathSoulFed, ButtonType.ok_cancel, NumberButtons.no_button, 1801960, 3.0)
    skip(19)

    skip_if_condition_false_finished(4, 2)
    flag.enable(11800202)
    item.remove_items_from_player(ItemType.good, GOOD.LifeSoul, 0)
    message.dialog(TEXT.LifeSoulFed, ButtonType.ok_cancel, NumberButtons.no_button, 1801960, 3.0)
    skip(14)

    skip_if_condition_false_finished(4, 3)
    flag.enable(11800203)
    item.remove_items_from_player(ItemType.good, GOOD.LightSoulShardFourKings, 0)
    message.dialog(TEXT.LightSoulFedFourKings, ButtonType.ok_cancel, NumberButtons.no_button, 1801960, 3.0)
    skip(9)

    skip_if_condition_false_finished(4, 4)
    flag.enable(11800204)
    item.remove_items_from_player(ItemType.good, GOOD.LightSoulShardSeath, 0)
    message.dialog(TEXT.LightSoulFedSeath, ButtonType.ok_cancel, NumberButtons.no_button, 1801960, 3.0)
    skip(4)

    skip_if_condition_false_finished(3, 5)
    flag.enable(11800205)
    item.remove_items_from_player(ItemType.good, GOOD.DarkRemnant, 0)
    message.dialog(TEXT.DarkRemnantFed, ButtonType.ok_cancel, NumberButtons.no_button, 1801960, 3.0)

    flag.enable(11805111)  # Triggers new SFX.
    if_event_flag_off(0, 11805111)
    wait_frames(10)
    end_if_event_flag_on(11800211)
    flag.disable(756)
    restart()


def event11800210():
    """ Initialize Lordvessel SFX and play cutscene/open door when four Lord Souls are added. """
    header(11800210)
    skip_if_event_flag_on(17, EVENT.GwynCinderDead)
    if_number_true_flags_in_range_equal(2, 11800201, 11800205, 1)
    if_number_true_flags_in_range_equal(3, 11800201, 11800205, 2)
    if_number_true_flags_in_range_equal(4, 11800201, 11800205, 3)
    if_number_true_flags_in_range_equal(5, 11800201, 11800205, 4)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(-1, 4)
    if_condition_true(-1, 5)
    if_condition_true(0, -1)
    skip_if_condition_false_finished(1, 2)
    sfx.create_object_sfx(1801960, 100, 180005)
    skip_if_condition_false_finished(1, 3)
    sfx.create_object_sfx(1801960, 100, 180006)
    skip_if_condition_false_finished(1, 4)
    sfx.create_object_sfx(1801960, 100, 180007)
    skip_if_condition_false_finished(1, 5)
    sfx.create_object_sfx(1801960, 100, 180008)

    skip_if_this_event_off(2)
    anim.end_animation(1801101, 1)
    end()

    if_number_true_flags_in_range_greater_than_or_equal(0, 11800201, 11800205, 4)
    flag.enable(11800211)
    flag.disable(756)
    cutscene.play_cutscene_to_player(180010, CutsceneType.skippable, CHR.Player)
    wait_frames(1)
    anim.end_animation(1801101, 1)
    map.register_bonfire(11800992, 1801960, 2.0, 180.0, initial_kindle_level=30)
    wait(1.0)
    message.status_explanation(TEXT.LordvesselWarpUnlocked)


def event11800230():
    """ Add SFX to Lordvessel as more souls are added. """
    header(11800230)
    number_souls_added, sfx_id, lordvessel = define_args('iii')
    if_event_flag_on(1, 11805111)
    if_number_true_flags_in_range_equal(1, 11800201, 11800205, number_souls_added)
    if_condition_true(0, 1)
    sfx.delete_object_sfx(lordvessel, True)
    sfx.create_object_sfx(lordvessel, 100, sfx_id)
    wait_frames(95)
    if_number_true_flags_in_range_greater_than_or_equal(7, 11800201, 11800205, 4)
    skip_if_condition_true(1, 7)
    anim.force_animation(CHR.Player, 7701, loop=True)
    flag.disable(11805111)


def event11800100():
    """ Place Lordvessel on altar. Now doesn't play cutscene (as golden fog gates are gone). """
    header(11800100)
    end_if_this_event_on()
    obj.disable(1801110)
    if_host(1)
    if_player_has_good(1, GOOD.Lordvessel)
    if_action_button_state(1, Category.object, 1801960, 180.0, 150, 2.0, help_id=10010105)
    if_condition_true(0, 1)
    # No cutscene.
    obj.enable(1801110)
    map.register_bonfire(11800992, 1801960, initial_kindle_level=10)
    item.remove_items_from_player(ItemType.good, GOOD.Lordvessel, 0)


def event11802006():
    """ Artorias battle. """
    header(11802006, 1)

    chr.disable(CHR.Artorias)
    chr.disable(CHR.SifFirst)
    chr.disable(CHR.SifSecond)
    chr.disable(CHR.SifDeath)

    # Triggered when you try to abandon the fire, if Artorias was rescued in Darkroot.
    if_event_flag_on(0, EVENT.ArtoriasTriggered)

    # Enable fog.
    obj.enable(1801990)
    sfx.create_map_sfx(1801991)
    sound.enable_map_sound(1803801)

    chr.enable(CHR.Artorias)
    anim.force_animation(CHR.Artorias, 6, wait_for_completion=True)  # Fade in (without roar).
    boss.enable_boss_health_bar(CHR.Artorias, 4106)

    # Sif appears when Artorias is at 66% HP.
    if_entity_health_greater_than(1, CHR.Artorias, 0.0)
    if_entity_health_less_than_or_equal(1, CHR.Artorias, 0.66)
    if_condition_true(0, 1)
    anim.force_animation(CHR.Artorias, 3006)  # Roar.
    wait(2.0)
    run_event(11805397)

    # Sif appears when Artorias is at 33% HP.
    if_entity_health_greater_than(1, CHR.Artorias, 0.0)
    if_entity_health_less_than_or_equal(1, CHR.Artorias, 0.33)
    if_event_flag_on(1, 11805397)
    if_condition_true(0, 1)
    anim.force_animation(CHR.Artorias, 3006)  # Roar.
    wait(2.0)
    run_event(11805398)


def event11805397():
    """ Sif appears. Run in 11802006. """
    header(11805397)
    chr.enable(CHR.SifFirst)
    anim.force_animation(CHR.SifFirst, 7004)  # Sif appears (first time).
    if_entity_dead(0, CHR.SifFirst)
    end()


def event11805398():
    """ Sif appears again. Run in 11802006. """
    header(11805398)
    chr.enable(CHR.SifSecond)
    anim.force_animation(CHR.SifSecond, 7004)  # Sif appears (first time).
    # Doesn't end (to enable flag for second summon) until Sif is defeated.
    if_entity_dead(0, CHR.SifSecond)
    end()


def event11802007():
    """ Artorias dies, which ends the game (Dark Lord). """
    header(11802007)

    if_event_flag_on(1, EVENT.ArtoriasTriggered)
    if_entity_health_less_than_or_equal(1, CHR.Artorias, 0.0)
    if_condition_true(0, 1)

    boss.disable_boss_health_bar(CHR.Artorias, 4106)
    sound.disable_map_sound(1803801)
    sound.play_sound_effect(CHR.Artorias, SoundType.s_sfx, 777777777)

    # Find the right copy of Sif to 'die' at the end.
    skip_if_event_flag_on(3, 11805397)
    chr.enable(CHR.SifFirst)
    chr.kill(CHR.SifFirst, False)
    skip(7)
    skip_if_event_flag_on(3, 11805398)
    chr.enable(CHR.SifSecond)
    chr.kill(CHR.SifSecond, False)
    skip(3)
    warp.warp_and_copy_floor(CHR.SifDeath, Category.character, CHR.Player, 237, CHR.Player)
    chr.enable(CHR.SifDeath)
    chr.kill(CHR.SifDeath, False)

    wait(10.0)

    # If the player quits out before this point, the entire battle will be replayed.

    flag.enable(11802007)  # This will trigger the Dark Lord ending and NG+.


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
