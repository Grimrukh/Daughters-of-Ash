import sys
import inspect
from pydses import *

map_name = 'm13_02_00_00'  # Great Hollow / Ash Lake
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'


class CHR(IntEnum):
    Siegmeyer = 6288
    Sieglinde = 6290
    Havel = 6580
    SellswordTishana = 6860
    Player = 10000
    Seath = 1320875
    Hydra = 1320700
    StoneDragon = 1320800
    StoneDragonTail = 1320801


HavelGear = range(6582, 6587)


class DEBUG(IntEnum):
    VELKA_PACT_MADE = False
    SEATH_AT_ASH_LAKE = False
    HAVEL_AT_ASH_LAKE = False


class GOOD(IntEnum):
    PaleEyeOrb = 2530


class REGION(IntEnum):
    DrakeAttackArea = 1322875  # used in AI
    SellswordTishanaTrigger = 1322876
    SellswordTishanaSignPoint = 1322877


class ANIM(IntEnum):
    PlayerSpawn = 6950


class EVENT(IntEnum):
    HavelTrapped = 1890
    HavelFreed = 1891
    HavelInsane = 1892
    HavelRestingAtAshLake = 1893
    HavelVanished = 1895
    HavelDead = 1899
    VelkaPactMade = 1910
    SerousWitness = 11502021
    SeathAtAshLake = 11702000
    ArrivalFromTomb = 11312004
    StoneDragonDead = 11322009
    SeathKilledByPlayerInLake = 11322004


class ITEMLOT(IntEnum):
    VelkaGift = 1650


class TEXT(IntEnum):
    DeathlessAura = 10010645
    PaleEyeOrbQuivers = 10010737


def event0():
    header(0)

    if DEBUG.VELKA_PACT_MADE:
        item.award_item_to_host_only(ITEMLOT.VelkaGift)
        flag.enable(EVENT.VelkaPactMade)
    if DEBUG.SEATH_AT_ASH_LAKE:
        flag.enable(EVENT.SeathAtAshLake)

    map.register_bonfire(11320984, 1321961)
    map.register_bonfire(11320976, 1321962)
    map.register_ladder(11320010, 11320011, 1321140)
    map.register_ladder(11320012, 11320013, 1321141)
    map.register_ladder(11320014, 11320015, 1321142)
    map.register_ladder(11320016, 11320017, 1321143)
    for statue_id in range(1321900, 1321908):
        obj.register_statue_object(statue_id, 13, 2, StatueType.stone)
    skip_if_client(2)
    obj.disable(1321994)
    sfx.delete_map_sfx(1321995, False)
    run_event_with_slot(11320090, 0, args=(1321700, 1321701, 1322600, 1322601))

    # Stone Dragon and tail.
    run_event(11325000)
    run_event(11320800)  # Doesn't respawn.
    run_event(11325001)
    run_event_with_slot(11320200, 0, args=(1321200, 11320200))
    run_event_with_slot(11320200, 1, args=(1321201, 11320201))
    run_event(11320580)

    run_event(11322000)  # (New) Arrival from Tomb of the Giants.

    run_event(11322005)  # (New) First pair of NPCs (false floor) are replaced by Basilisks when killed.
    run_event(11322006)  # (New) Second pair of NPCs (Hollow floor) are replaced by Mushrooms when killed.
    run_event(11322007)  # (New) Trio of NPCs (second Hollow) are replaced by Mushrooms when killed.
    run_event(11322008)  # (New) Witness Hydra jump over sandbar for Serous statue.

    skip_if_event_flag_off(2, 11320100)
    run_event(11320100)
    skip(3)
    run_event(11320110)
    run_event(11320100)
    run_event(11325100)

    run_event(11320101)
    run_event_with_slot(11325150, 0, args=(1320100, 15.0), arg_types='if')
    run_event_with_slot(11325150, 1, args=(1320101, 15.0), arg_types='if')
    run_event_with_slot(11325150, 2, args=(1320102, 10.0), arg_types='if')

    run_event_with_slot(11320300, 1, args=(1320201, 11325203, 11325205, 11325203))
    run_event_with_slot(11320300, 2, args=(1320202, 11325206, 11325208, 11325206))
    run_event_with_slot(11320300, 3, args=(1320203, 11325209, 11325211, 11325209))
    run_event_with_slot(11320300, 4, args=(1320204, 11325212, 11325214, 11325212))
    run_event_with_slot(11320300, 5, args=(1320205, 11325215, 11325217, 11325215))
    run_event_with_slot(11320300, 6, args=(1320206, 11325218, 11325220, 11325218))
    run_event_with_slot(11320300, 7, args=(1320207, 11325221, 11325223, 11325221))
    run_event_with_slot(11320300, 8, args=(1320208, 11325224, 11325226, 11325224))
    run_event_with_slot(11320300, 9, args=(1320209, 11325227, 11325229, 11325227))
    run_event_with_slot(11320300, 10, args=(1320210, 11325230, 11325232, 11325230))
    run_event_with_slot(11320600, 0, args=(1321650, 11320600))

    # Dart-blower doesn't respawn.
    run_event(11320900)


def event50():
    """ NPC pre-constructor. """
    header(50)

    if DEBUG.HAVEL_AT_ASH_LAKE:
        flag.disable_chunk(1890, 1899)
        flag.enable(EVENT.HavelRestingAtAshLake)

    # SIEGMEYER

    chr.humanity_registration(CHR.Siegmeyer, 8446)
    skip_if_event_flag_on(1, 1511)
    chr.disable(CHR.Siegmeyer)
    run_event_with_slot(11320534, args=(CHR.Siegmeyer, 1490, 1539, 1511))
    run_event_with_slot(11320535, args=(CHR.Siegmeyer, 1490, 1539, 1514))

    # SIEGLINDE

    chr.humanity_registration(CHR.Sieglinde, 8454)
    skip_if_event_flag_on(2, 1547)
    skip_if_event_flag_on(1, 1546)
    chr.disable(CHR.Sieglinde)
    run_event_with_slot(11320510, 1, args=(CHR.Sieglinde, 1547))
    run_event_with_slot(11320520, 1, args=(CHR.Sieglinde, 1540, 1569, 1548))
    run_event_with_slot(11320540, args=(CHR.Sieglinde, 1540, 1569, 1546))
    run_event_with_slot(11320541, args=(CHR.Sieglinde, 1540, 1569, 1549))

    # STONE DRAGON

    skip_if_event_flag_on(2, EVENT.StoneDragonDead)
    chr.enable_immortality(CHR.StoneDragon)
    skip(2)
    chr.disable(CHR.StoneDragon)
    chr.disable(CHR.StoneDragonTail)

    # (NEW) HAVEL THE ROCK and SEATH THE SCALELESS

    skip_if_event_flag_on(1, EVENT.HavelRestingAtAshLake)
    chr.disable(CHR.Havel)
    run_event_with_slot(11320510, 2, args=(CHR.Havel, 1894))  # Hostile
    run_event_with_slot(11320520, 2, args=(CHR.Havel, 1890, 1899, 1899))  # Dead
    run_event(11322001)  # (NEW) Seath gravity, and his death to the player here..
    run_event(11322002)  # (NEW) Havel kills the Stone Dragon when he arrives (also handles bonfire).
    run_event_with_slot(11322003, args=(CHR.Havel, 1890, 1899, EVENT.HavelVanished))  # (NEW) Havel kills Seath.


def event11322000():
    """ Arrival at Ash Lake from Tomb of the Giants. """
    header(11322000, 0)
    end_if_event_flag_off(EVENT.ArrivalFromTomb)

    anim.force_animation(CHR.Player, ANIM.PlayerSpawn)
    flag.disable(EVENT.ArrivalFromTomb)
    message.status_explanation(TEXT.DeathlessAura)
    warp.set_player_respawn_point(1322963)
    network.save_request()


def event11322001():
    """ Seath appears, then is killed by the player. """
    header(11322001, 1)

    skip_if_event_flag_on(2, EVENT.SeathAtAshLake)
    chr.disable(CHR.Seath)
    end()

    chr.disable_gravity(CHR.Seath)

    if_event_flag_off(1, EVENT.HavelVanished)
    if_entity_health_less_than_or_equal(1, CHR.Seath, 0.0)
    if_condition_true(0, 1)
    flag.enable(EVENT.SeathKilledByPlayerInLake)
    flag.enable(1911)  # For Seath punishment.
    end()


def event11322002():
    """ Havel kills the Stone Dragon. """
    header(11322002, 1)

    skip_if_event_flag_off(3, EVENT.StoneDragonDead)
    chr.disable(CHR.StoneDragon)
    chr.disable(CHR.StoneDragonTail)
    end()

    if_event_flag_on(-1, EVENT.HavelRestingAtAshLake)
    if_event_flag_on(-1, EVENT.HavelVanished)
    skip_if_condition_false(4, -1)
    flag.enable(EVENT.StoneDragonDead)
    chr.disable(CHR.StoneDragon)
    chr.disable(CHR.StoneDragonTail)
    end()

    # Otherwise, register Stone Dragon's bonfire.
    map.register_bonfire(11320992, 1321960, initial_kindle_level=10)


def event11322003():
    """ Havel kills Seath and sheds his own gear, then vanishes. """
    header(11322003, 1)

    # When both Havel and Seath are at Ash Lake, and Seath is not already dead here, the flag for Havel vanishing is
    # enabled. When the map is reloaded and this event runs again, it will detect that the HavelVanished flag is
    # already enabled, and (a) disable Havel, (b) disable Seath, and (c) drop Havel's five items.

    if_event_flag_on(7, EVENT.HavelVanished)
    if_condition_true(-1, 7)
    if_event_flag_on(1, EVENT.HavelRestingAtAshLake)
    if_event_flag_on(1, EVENT.SeathAtAshLake)
    if_event_flag_off(1, EVENT.SeathKilledByPlayerInLake)
    if_condition_true(-1, 1)
    if_condition_true(0, -1)

    flag.disable_chunk(1890, 1899)
    flag.enable(EVENT.HavelVanished)
    end_if_condition_false_finished(7)  # Only continue if HavelVanished was enabled on load.

    chr.disable(CHR.Havel)
    for havel_gear_drop in HavelGear:
        chr.drop_mandatory_treasure(havel_gear_drop)
    chr.disable(CHR.Seath)
    chr.kill(CHR.Seath, False)


def event11322005():
    """ First pair of NPCs are replaced by Basilisks. """
    header(11322005)
    skip_if_this_event_off(3)
    chr.disable(6820)
    chr.disable(6821)
    end()

    chr.disable(1320400)
    chr.disable(1320401)

    if_entity_dead(1, 6820)
    if_entity_dead(1, 6821)
    if_condition_true(0, 1)
    end()


def event11322006():
    """ Second pair of NPCs are replaced by a family of Mushrooms. """
    header(11322006, 1)
    skip_if_this_event_off(3)
    chr.disable(6822)
    chr.disable(6823)
    end()

    chr.disable(1320300)
    chr.disable(1320301)
    chr.disable(1320350)
    chr.disable(1320351)
    chr.disable(1320352)

    if_entity_dead(1, 6822)
    if_entity_dead(1, 6823)
    if_condition_true(0, 1)
    end()


def event11322007():
    """ Trio of NPCs are replaced by a family of Mushrooms and a Basilisk. """
    header(11322007, 1)
    skip_if_this_event_off(5)
    chr.disable(6824)
    chr.disable(6825)
    chr.disable(6826)
    chr.disable(1320403)
    end()

    chr.disable(1320302)
    chr.disable(1320303)
    chr.disable(1320353)
    chr.disable(1320354)
    chr.disable(1320355)
    chr.disable(1320402)

    if_entity_dead(1, 6824)
    if_entity_dead(1, 6825)
    if_entity_dead(1, 6826)
    if_condition_true(0, 1)
    end()


def event11322008():
    """ Witness Hydra jump over sandbar for Serous statue. """
    header(11322008)
    end_if_event_flag_on(EVENT.SerousWitness)

    if_player_has_good(1, GOOD.PaleEyeOrb)
    if_has_tae_event(1, CHR.Hydra, 700)  # Activated ten seconds into flyover (3011)
    if_condition_true(0, 1)
    flag.enable(EVENT.SerousWitness)
    message.status_explanation(TEXT.PaleEyeOrbQuivers)


def event11320900():
    """ Dart-shooter doesn't respawn. """
    header(11320900, 1)

    skip_if_this_event_off(3)
    chr.disable(1320880)
    chr.kill(1320880, False)
    end()

    if_entity_dead(0, 1320880)
    end()


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
