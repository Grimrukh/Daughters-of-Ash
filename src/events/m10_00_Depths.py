
import sys
import inspect
from pydses import *

map_name = 'm10_00_00_00'  # The Depths
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11000000
BASE_PART = 1000000


class DEBUG(IntEnum):
    ARIAMIS_DEAD = False
    GET_PECULIAR_DOLL = False
    ARIAMIS_WARP_DONE = False
    GET_GOLD_PINE_RESIN = False
    GET_LIGHTNING_SPEAR = False
    GET_WORKERS_KEY = False


class CHR(IntEnum):
    Player = 10000
    Domnhall = 6260
    SolaireSummon = 6541
    Kirk = 6562
    BaneOfLordran = 1000800
    BaneChanneler = 1000300


class GOOD(IntEnum):
    PaintedDoll = 384
    MeltedIronKey = 2007
    WorkersKey = 2018
    MasterKey = 2100


class OBJECT(IntEnum):
    CorpseInSlime = 1001675
    SlimeWithCorpse = 1001676


class SPEFFECT(IntEnum):
    StandardChannelerBuff = 5471
    BaneChannelerBuff = 4960


class TEXT(IntEnum):
    SewerKeyUsed = 10010877
    MasterKeyShattered = 10010883
    SomethingInDoor = 10010631
    RemoveItem = 10010632


class ITEMLOT(IntEnum):
    MeltedIronKey = 1660


class EVENT(IntEnum):
    BaneDead = 2
    BaneWarpDone = 11002000
    BaneStableFooting = 11002501
    PaintedWorldTraversed = 11100710


def event0():
    """ Constructor. """
    header(0, 0)

    if DEBUG.ARIAMIS_DEAD:
        flag.enable(2)
    if DEBUG.GET_PECULIAR_DOLL:
        item.award_item_to_host_only(1010490)
    if DEBUG.ARIAMIS_WARP_DONE:
        flag.enable(11002000)
    if DEBUG.GET_GOLD_PINE_RESIN:
        item.award_item_to_host_only(22700000)
    if DEBUG.GET_LIGHTNING_SPEAR:
        item.award_item_to_host_only(27800001)
    if DEBUG.GET_WORKERS_KEY:
        item.award_item_to_host_only(1000170)

    map.register_bonfire(11000992, 1001960)
    map.register_ladder(11000010, 11000011, 1001140)
    for statue_id in range(1001900, 1001908):
        obj.register_statue_object(statue_id, 10, 0, StatueType.stone)

    # Stable footing in Bane of Lordran arena.
    run_event(11502500)

    # Summon fog.
    skip_if_client(5)
    flag.disable(11000000)  # Makes Bane of Lordran cutscene play every time.
    obj.disable(1001994)
    sfx.delete_map_sfx(1001995, False)
    obj.disable(1001996)
    sfx.delete_map_sfx(1001997, False)

    # Open shortcut door.
    skip_if_event_flag_off(1, 11000100)
    anim.end_animation(1001319, 0)

    # Checkpoint fog.
    run_event_with_slot(11000090, 0, args=(1001700, 1001701, 1002600, 1002601))

    # Gravelording.
    run_event(11005080)
    run_event(11005081)
    run_event(11005082)

    # Open door toward old bonfire chamber (Master Key works, but breaks).
    run_event_with_slot(11000120, args=(11000120, TEXT.SewerKeyUsed, 1001315, TEXT.MasterKeyShattered, GOOD.WorkersKey))
    run_event(11000200)  # Basilisk runs past when you get close.
    run_event(11005050)  # Butcher stops chopping and comes for you.
    run_event(11005060)  # Visual effect on Butcher's table.
    run_event(11000110)  # Open door from Blighttown (originally *to*).
    run_event(11000111)  # Blighttown door, wrong side.
    run_event(11000112)  # (New) Inspect Blighttown door, then pull out key.
    run_event_with_slot(11000600, 0, args=(1001650, 11000600))  # Large Ember chest.
    run_event(11002044)  # (New) Monitor resting at Sluiceworks bonfire for warping.

    # BANE OF LORDRAN (GAPING DRAGON)

    sound.disable_map_sound(1003800)

    # Already dead.
    skip_if_event_flag_off(4, EVENT.BaneDead)
    run_event(11005392)
    obj.disable(1001990)
    sfx.delete_map_sfx(1001991, False)
    skip(19)
    skip_if_client(1)
    skip_if_event_flag_off(3, EVENT.BaneWarpDone)  # No fog (or fog events) on first time (for hosts).
    run_event(11005390)  # Entry fog (host).
    run_event(11005391)  # Entry fog (summon).
    skip(3)
    obj.disable(1001990)
    sfx.delete_map_sfx(1001991, False)
    flag.enable(11005390)  # Allows tail cut.
    run_event(11005393)  # Boss notification.
    run_event(11005392)  # Boss behavior.
    run_event(11000001)  # Boss death.
    run_event(11005394)  # Boss music start.
    run_event(11005395)  # Boss music stop.
    run_event(11005396)  # Tail cut.
    run_event(11005397)  # Another part - head?
    run_event(11005398)  # Behavior change after tail is cut.
    run_event(11002000)  # (New) Warps you to Painted World when killed.
    run_event(11002002)  # (New) Temporarily disable Bane's speed boost during grab.
    run_event(11002003)  # (New) Channeler buff on Bane is massively powered up.

    run_event_with_slot(11005000, 0, args=(1001000, 1001000, 1))
    run_event_with_slot(11005000, 1, args=(1001001, 1001001, 1))
    run_event_with_slot(11005000, 2, args=(1001002, 1001002, 3))

    # Groups of rats aggravated at once by certain area triggers.
    slot = 0
    for enemy_id in range(1000120, 1000126):
        run_event_with_slot(11005200, slot, args=(enemy_id, 1002020))
        slot += 1
    for enemy_id in (1000110, 1000111):
        run_event_with_slot(11005200, slot, args=(enemy_id, 1002021))
        slot += 1
    for enemy_id in (1000112, 1000113, 1000126):
        run_event_with_slot(11005200, slot, args=(enemy_id, 1002022))
        slot += 1

    # Slimes drop from the ceiling with area triggers (and optional delay).
    run_event_with_slot(11005100, 0, args=(1002100, 1002110, 1000100, 0.0), arg_types='iiif')
    run_event_with_slot(11005100, 1, args=(1002101, 1002102, 1000101, 0.0), arg_types='iiif')
    run_event_with_slot(11005100, 2, args=(1002102, 1002103, 1000102, 0.0), arg_types='iiif')
    run_event_with_slot(11005100, 3, args=(1002102, 1002103, 1000103, 0.6), arg_types='iiif')
    run_event_with_slot(11005100, 4, args=(1002103, 1002104, 1000104, 0.0), arg_types='iiif')
    run_event_with_slot(11005100, 5, args=(1002103, 1002104, 1000105, 0.2), arg_types='iiif')
    run_event_with_slot(11005100, 6, args=(1002103, 1002104, 1000106, 0.9), arg_types='iiif')
    run_event_with_slot(11005100, 7, args=(1002107, 0, 1000107, 0.0), arg_types='iiif')

    # Rats burst out of crates.
    run_event_with_slot(11005150, 0, args=(1000150, 1001100))
    run_event_with_slot(11005150, 1, args=(1000151, 1001101))
    run_event_with_slot(11005150, 2, args=(1000152, 1001102))

    # (NEW) Treasure corpse inside slime.
    run_event_with_slot(11000400, 0, args=(OBJECT.CorpseInSlime, OBJECT.SlimeWithCorpse))

    # Non-respawning enemies.
    run_event_with_slot(11000850, 0, args=(1000110,))  # Butcher's dog
    run_event_with_slot(11000850, 1, args=(1000099,))  # Butcher
    run_event_with_slot(11000860, 0, args=(CHR.BaneChanneler,))  # Channeler (respawns until Painted warp done).


def event50():
    """ NPC constructor. """
    header(50)

    # Solaire summon, Lautrec summon, Kirk invasion
    chr.humanity_registration(CHR.SolaireSummon, 8310)
    chr.humanity_registration(6591, 8462)
    chr.humanity_registration(CHR.Kirk, 8956)
    run_event(11005030)
    run_event(11005031)
    run_event(11005033)
    run_event(11005034)
    run_event(11005039)
    run_event(11000810)

    # DOMNHALL OF ZENA

    chr.humanity_registration(CHR.Domnhall, 8430)
    skip_if_event_flag_on(2, 1434)
    skip_if_event_flag_on(1, 1430)
    chr.disable(CHR.Domnhall)
    run_event_with_slot(11000532, args=(CHR.Domnhall, 1430, 1459, 1431))
    run_event_with_slot(11000510, 1, args=(CHR.Domnhall, 1434))  # Hostile.
    run_event_with_slot(11000533, args=(CHR.Domnhall, 1435))  # Dead.


def event11005393():
    """ Bane of Lordran boss entry. Now requires Peculiar Doll. """
    header(11005393, 0)
    skip_if_this_event_on(4)
    if_event_flag_off(1, 2)
    if_player_inside_region(1, 1002999)
    if_player_owns_good(1, GOOD.PaintedDoll)
    if_condition_true(0, 1)
    chr.activate_npc_buffs(CHR.BaneOfLordran)
    end_if_client()

    network.notify_boss_room_entry()
    end_if_event_flag_on(EVENT.BaneWarpDone)

    wait_frames(2)
    obj.enable(1001990)
    sfx.create_map_sfx(1001991)
    if_entity_dead(2, CHR.BaneChanneler)
    end_if_condition_true(2)
    anim.force_animation(CHR.BaneChanneler, 3007)  # buff dance


def event11000110():
    """ Open gate from Blighttown to Depths. First, tells you there's something in the door. Second, lets you pull
    out the Melted Iron Key. """
    header(11000110, 0)
    skip_if_event_flag_on(1, 590)  # Door open.
    skip_if_this_event_off(2)
    anim.end_animation(1001200, 1)
    end()

    if_player_owns_good(1, GOOD.MeltedIronKey)
    if_action_button_state(1, Category.object, 1001200, 60.0, 100, 1.5, 10010400)
    if_condition_true(0, 1)
    flag.enable(11000111)  # Not sure what this achieves.
    warp.short_warp(CHR.Player, Category.object, 1001200, 120)
    anim.force_animation(CHR.Player, 7120)
    anim.force_animation(1001200, 1)
    end_if_client()
    message.dialog(10010866, ButtonType.ok_cancel, NumberButtons.no_button, 1001200, 3.0)
    flag.enable(590)


def event11000112():
    """ Inspect door from Blighttown and pull out Melted Iron Key. """
    header(11000112, 0)
    end_if_this_event_on()  # Key obtained.

    if_player_does_not_own_good(1, GOOD.MeltedIronKey)  # In case you get it elsewhere.
    if_action_button_state(1, Category.object, 1001200, 60.0, 100, 1.5, 10010400)
    if_condition_true(0, 1)
    message.dialog(TEXT.SomethingInDoor, ButtonType.ok_cancel, NumberButtons.no_button, 1001200, 3.0)
    obj.disable_activation(1001200, -1)

    wait(1.0)

    if_player_does_not_own_good(1, GOOD.MeltedIronKey)  # In case you get it elsewhere.
    if_action_button_state(1, Category.object, 1001200, 60.0, 100, 1.5, TEXT.RemoveItem)
    if_condition_true(0, 1)

    item.award_item_to_host_only(ITEMLOT.MeltedIronKey)

    wait(2.0)

    obj.enable_activation(1001200, -1)


def event11002000():
    """ Bane of Lordran warps you to Painted World when it kills or eats you (only on eating if you've traversed it
    already). """
    header(11002000, 0)
    if_event_flag_on(0, 11005393)
    if_has_tae_event(-1, CHR.BaneOfLordran, 800)
    skip_if_event_flag_on(2, EVENT.PaintedWorldTraversed)
    chr.enable_immortality(CHR.Player)
    if_entity_health_less_than_or_equal(-1, CHR.Player, 0.01)
    if_condition_true(0, -1)
    flag.enable(11002001)  # Marks arrival script for Painted World (changes respawn point).
    warp.warp_player(11, 0, 1100991)


def event11002002():
    """ Temporarily remove Bane of Lordran buff during grab attack. """
    header(11002002)
    end_if_event_flag_on(EVENT.BaneDead)
    if_has_tae_event(0, CHR.BaneOfLordran, 700)
    chr.cancel_special_effect(CHR.BaneOfLordran, 4956)
    if_has_tae_event(0, CHR.BaneOfLordran, 710)
    chr.set_special_effect(CHR.BaneOfLordran, 4956)
    restart()


def event11000860():
    """ Channeler appears until you have been warped to Painted World. """
    header(11000860, 1)
    channeler, = define_args('i')
    end_if_event_flag_off(EVENT.BaneWarpDone)
    chr.disable(channeler)
    chr.kill(channeler, False)
    end()


def event11000120():
    """ Open a door (o1315) with intended key or Master Key, which breaks if used. """
    header(11000120, 0)
    objact_id, key_message, door_id, master_key_message, key_id = define_args('iiiii')
    skip_if_this_event_slot_off(6)
    anim.end_animation(door_id, 0)  # Re-open door.
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


def event11002500():
    """ Checks whether stable footing should be enabled inside Bane of Lordran arena. """
    header(11502500, 1)
    flag.disable(EVENT.BaneStableFooting)
    if_event_flag_on(-1, EVENT.BaneDead)
    if_player_does_not_have_good(-1, GOOD.PaintedDoll)
    if_condition_true(0, -1)
    flag.enable(EVENT.BaneStableFooting)
    end_if_event_flag_on(EVENT.BaneDead)
    if_player_has_good(0, GOOD.PaintedDoll)
    restart()  # In case Depths hasn't de-loaded when you pick up the Doll in Lower Burg.


def event11000400():
    """ Corpse in slime pile. """
    header(11000400)
    corpse, slime = define_args('ii')
    skip_if_this_event_slot_off(3)
    anim.end_animation(corpse, 101)
    obj.enable_treasure(corpse)
    end()
    obj.disable_treasure(corpse)
    anim.force_animation(corpse, 100, loop=True)
    if_object_destroyed(0, slime)
    anim.force_animation(corpse, 101, wait_for_completion=True)
    obj.enable_treasure(corpse)


def event11005100():
    """ Slime ambushes. Now takes two area triggers. """
    header(11005100, 1)
    trigger_region_1, trigger_region_2, slime_id, delay = define_args('iiif')
    skip_if_this_event_slot_on(8)
    chr.disable_gravity(slime_id)
    chr.disable_collision(slime_id)
    if_player_inside_region(-1, trigger_region_1)
    skip_if_equal(1, trigger_region_2, 0)
    if_player_inside_region(-1, trigger_region_2)
    if_entity_attacked_by(-1, slime_id, CHR.Player)
    if_condition_true(0, -1)
    wait(delay)

    chr.enable_gravity(slime_id)
    chr.enable_collision(slime_id)
    chr.set_standby_animation_settings_to_default(slime_id)


def event11005039():
    """ Kirk invasion trigger. """
    header(11005039)

    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11005040)
    # No longer requires Bane of Lordran to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 11000810)
    skip_if_this_event_on(1)
    if_player_inside_region(1, 1002005)
    if_condition_true(0, 1)

    message.place_summon_sign(SummonSignType.black_eye_sign, CHR.Kirk, 1002001,
                              summon_event_flag_id=11005040, dismissal_event_flag_id=11005041)
    wait(20.0)
    restart()


def event11002003():
    """ Bane is massively buffed from Channeler, to a one-hit kill (and tons of HP). """
    header(11002003, 1)

    if_entity_has_special_effect(0, CHR.BaneOfLordran, SPEFFECT.StandardChannelerBuff)
    chr.cancel_special_effect(CHR.BaneOfLordran, SPEFFECT.StandardChannelerBuff)
    chr.set_special_effect(CHR.BaneOfLordran, SPEFFECT.BaneChannelerBuff)


def event11002044():
    """ Monitor resting at Sluiceworks bonfire. """
    header(11002044)
    if_player_within_distance(1, 1001960, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11002044)


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
