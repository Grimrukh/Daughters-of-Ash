import sys
import inspect
from pydses import *
    
map_name = 'm15_00_00_00'  # Sen's Fortress
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

# TODO: This switch changes the DrawParam slot for DSR.
__REMASTERED = False


class DEBUG(IntEnum):
    GET_RING_OF_ASH = False
    DARK_ANOR_LONDO = False
    THRALL_ACTIVE = False
    BOMB_GIANT_DEAD = False
    GOLEM_DEAD = False
    ANDRE_TALK_DIALOGUE = False
    GET_DIVINE_EMBER = False


class CHR(IntEnum):
    Player = 10000
    BlackKnightAxe = 1500400
    Mimic = 1500010
    SensIronGolem = 1500800
    CapriciousThrall = 1500801
    CapriciousThrallBoss = 1010751
    UndeadPrinceRicard = 6600
    BlackIronTarkusSummon = 6510
    Logan = 6030
    HollowGriggs = 6043
    Siegmeyer = 6280
    CrestfallenMerchant = 6250
    Andre = 6190
    SellswordTishana = 6860


class ANIM(IntEnum):
    ThrallTransformation = 4000
    ThrallRetreat = 4001
    ThrallAmbushAttack = 4002


Darkwraiths = (1500875, 1500876)


class EVENT(IntEnum):
    SensIronGolemDead = 11
    BlackKnightSwordDead = 11812020
    BlackKnightGreatswordDead = 11012005
    BlackKnightHalberdDead = 11202002
    BlackKnightAxeDead = 11502000
    AllBlackKnightsDead = 11802000
    AnorLondoVisited = 11100710
    DarkAnorLondo = 11510400
    JareelDead = 11510901
    CapriciousThrallActive = 11012010
    CapriciousThrallDead = 11012012
    PaleEyeOrbReturned = 11302002
    SensGolemStableFooting = 11502501
    ThrallEncounterDone = 11502502
    ScriptedBoulderDone = 11500791
    ThrallAmbushOngoing = 11505396
    # 11502020-11502023 are used for Sen's Bond witness events in other scripts


class GOOD(IntEnum):
    TortureCageKey = 2003
    MasterKey = 2100


class REGION(IntEnum):
    CapriciousThrallSoloTrigger = 1502880
    SellswordTishanaTrigger = 1502675
    SellswordTishanaSignPoint = 1502676


class RING(IntEnum):
    RingOfAsh = 152


class TEXT(IntEnum):
    RingOfAshWarms = 10010627
    RingOfAshHot = 10010628
    CapriciousThrallName = 2245
    SensIronGolemName = 2320
    AbandonedPost = 10010193
    ThrallHasFled = 10010123


def event0():
    header(0, 0)

    if DEBUG.GET_RING_OF_ASH:
        item.award_item_to_host_only(2750)
    if DEBUG.DARK_ANOR_LONDO:
        flag.enable(EVENT.DarkAnorLondo)
    if DEBUG.THRALL_ACTIVE:
        flag.enable(EVENT.CapriciousThrallActive)
    if DEBUG.BOMB_GIANT_DEAD:
        flag.enable(11500865)
    if DEBUG.GOLEM_DEAD:
        flag.enable(11)
    if DEBUG.ANDRE_TALK_DIALOGUE:
        flag.enable(11016102)
    if DEBUG.GET_DIVINE_EMBER:
        item.award_item_to_host_only(1200141)

    skip_if_event_flag_off(1, EVENT.DarkAnorLondo)
    if __REMASTERED:
        light.set_area_texture_parambank_slot_index(15, 2)
    else:
        light.set_area_texture_parambank_slot_index(15, 1)

    spawner.create_spawner(1500200)  # spawns all darts
    chr.set_network_update_rate(1500100, True, CharacterUpdateRate.always)
    map.register_bonfire(11500984, 1501961)
    map.register_ladder(11500010, 11500011, 1501140)
    map.register_ladder(11500012, 11500013, 1501141)
    map.register_ladder(11500014, 11500015, 1501142)
    map.register_ladder(11500016, 11500017, 1501143)
    skip_if_host(2)
    flag.enable(11505240)
    flag.disable(11505360)
    skip_if_client(2)
    obj.disable(1501994)
    sfx.delete_map_sfx(1501995, False)
    hitbox.disable_hitbox(1503210)
    for object_id in range(800, 808):
        obj.disable(1501000 + object_id)
    # Put boulder spawner in right place.
    skip_if_event_flag_on(1, 11500803)
    anim.end_animation(1501790, 3)
    skip_if_event_flag_off(1, 11500806)
    anim.end_animation(1501790, 0)
    skip_if_event_flag_off(1, 11500809)
    anim.end_animation(1501790, 1)
    skip_if_event_flag_off(1, 11500812)
    anim.end_animation(1501790, 2)
    # Stack up boulders in hole.
    hitbox.disable_hitbox(1503200)
    hitbox.disable_hitbox(1503201)
    hitbox.disable_hitbox(1503202)
    for boulder_flag, boulder_id, boulder_hitbox, animation_id in (
            (11500821, 1501801, 1503200, 5),
            (11500822, 1501802, 1503201, 6),
            (11500823, 1501803, 1503202, 7),
    ):
        skip_if_event_flag_off(3, boulder_flag)
        obj.enable(boulder_id)
        anim.end_animation(boulder_id, animation_id)
        hitbox.enable_hitbox(boulder_hitbox)

    # Elevator navimesh.
    skip_if_event_flag_off(21, 11500100)
    skip_if_event_flag_on(10, 11500101)
    navimesh.add_navimesh_collision_bitflags(1503100, NavimeshType.wall)
    navimesh.add_navimesh_collision_bitflags(1503110, NavimeshType.wall_touching_floor)
    navimesh.add_navimesh_collision_bitflags(1503101, NavimeshType.wall_touching_floor)
    navimesh.add_navimesh_collision_bitflags(1503111, NavimeshType.wall)
    navimesh.add_navimesh_collision_bitflags(1503102, NavimeshType.wall_touching_floor)
    navimesh.add_navimesh_collision_bitflags(1503112, NavimeshType.wall)
    navimesh.add_navimesh_collision_bitflags(1503103, NavimeshType.wall)
    navimesh.add_navimesh_collision_bitflags(1503113, NavimeshType.wall_touching_floor)
    anim.end_animation(1501011, 12)
    skip(9)
    navimesh.add_navimesh_collision_bitflags(1503100, NavimeshType.wall_touching_floor)
    navimesh.add_navimesh_collision_bitflags(1503110, NavimeshType.wall)
    navimesh.add_navimesh_collision_bitflags(1503101, NavimeshType.wall)
    navimesh.add_navimesh_collision_bitflags(1503111, NavimeshType.wall_touching_floor)
    navimesh.add_navimesh_collision_bitflags(1503102, NavimeshType.wall)
    navimesh.add_navimesh_collision_bitflags(1503112, NavimeshType.wall_touching_floor)
    navimesh.add_navimesh_collision_bitflags(1503103, NavimeshType.wall_touching_floor)
    navimesh.add_navimesh_collision_bitflags(1503113, NavimeshType.wall)
    anim.end_animation(1501011, 11)
    skip(4)
    navimesh.add_navimesh_collision_bitflags(1503100, NavimeshType.solid)
    navimesh.add_navimesh_collision_bitflags(1503101, NavimeshType.solid)
    navimesh.add_navimesh_collision_bitflags(1503102, NavimeshType.solid)
    navimesh.add_navimesh_collision_bitflags(1503103, NavimeshType.solid)

    # Checkpoint fog.
    run_event_with_slot(11500090, 0, args=(1501700, 1501701, 1502600, 1502601))
    run_event_with_slot(11500090, 1, args=(1501702, 1501703, 1502602, 1502603))

    # Gravelording.
    run_event(11505090)
    run_event(11505091)
    run_event(11505092)

    run_event(11500201)  # This opened the main gate, which is no longer necessary.
    run_event(11505300)  # Pendulums and elevator ceiling spikes.
    run_event(11500840)  # Client flag sync.
    for slot, direction_flag in enumerate((803, 806, 809, 812)):
        # Sync direction of rolling ball.
        run_event_with_slot(11500841, slot, args=(11500000 + direction_flag,))
    run_event(11500790)  # Boulder spawn control.
    run_event(11500791)  # First boulder appearance that kills the Man-Serpent outside.
    # Four directions of boulder launch. These call two sub-events that handle the launches.
    # They also detect if the player is close to the stacking pit and launch special boulders in that case.
    run_event(11500795)
    run_event(11500796)
    run_event(11500797)
    run_event(11500798)
    run_event(11500830)  # Player is present to witness boulders stacking (checked once per load).
    run_event(11500831)  # Player is crushed to death in two scenarios, probably related to above.
    run_event(11500850)  # Player rotates boulder direction lever.
    run_event(11505255)  # Boulder direction rotates automatically based on area.
    run_event(11500100)  # Cage elevator.
    run_event(11500102)  # Player opens cage elevator for the first time.
    run_event(11500103)  # Inspect elevator without Cage Key.
    run_event(11500106)  # Prison one-way door does not open.
    run_event(11500107)  # Prison one-way door opens.
    # Open other non-elevator cages with Cage Key.
    for slot in (0, 1, 2, 3, 5, 6):
        run_event_with_slot(11500110, slot, args=(1501030 + slot, 11500110 + slot))

    run_event(11505050)  # Enable battle AI of boulder-loading Giant.
    run_event(11505051)  # Boulder-loading Giant loads boulders.
    run_event(11505055)  # Bomb-throwing Giant gives up if you destroy all the bombs near him.
    run_event(11505110)  # Bomb-throwing Giant throws bombs.
    run_event(11505101)  # Bomb-throwing Giant flag sync.
    run_event(11505102)  # Bomb-throwing Giant gives up after 30 seconds out of range.
    for slot, (bomb_flag, bomb_area, bomb_instruction) in enumerate((
            (5111, 700, 1), (5112, 701, 2), (5113, 702, 3), (5114, 703, 4),
            (5115, 704, 5), (5116, 705, 6), (5117, 710, -1))):
        run_event_with_slot(11505111, slot, args=(11500000 + bomb_flag, 1502000 + bomb_area, 
                                                  bomb_instruction))
    # Giants stun themselves with frenzy attack.
    run_event_with_slot(11505060, 0, args=(1500100,))  # Bomb-throwing Giant.
    run_event_with_slot(11505060, 1, args=(1500101,))  # Boulder-loading Giant.
    run_event_with_slot(11505060, 2, args=(1500102,))  # Gate-opening Giant.
    # Giant stun ends after some duration.
    run_event_with_slot(11505070, 0, args=(1500100, 7.0), arg_types='if')  # Bomb-throwing Giant.
    run_event_with_slot(11505070, 1, args=(1500101, 7.0), arg_types='if')  # Boulder-loading Giant.
    run_event_with_slot(11505070, 2, args=(1500102, 3.0), arg_types='if')  # Gate-opening Giant.

    run_event(11505080)  # Man-Serpent sleeping against destructible wall.
    run_event(11500210)  # Warp to Anor Londo.
    run_event(11500835)  # Sync boulder trap direction for summons.
    run_event(11502000)  # (New) Black Knight Axe only appears if you have the Ashen Ring.

    # SEN'S IRON GOLEM

    sound.disable_map_sound(1503800)
    skip_if_event_flag_off(4, 11)
    run_event(11505392)
    obj.disable(1501990)
    sfx.delete_map_sfx(1501991, False)
    skip(9)
    for golem_event_id in (5390, 5391, 5393, 5392, 1, 5394, 5395):
        run_event(11500000 + golem_event_id)
    run_event(11505350)  # Golem falls off and dies.
    run_event(11505353)  # Golem switches a hitbox (probably when stunned).

    # (NEW) CAPRICIOUS THRALL (during Sen's Golem battle)
    sound.disable_map_sound(1503801)
    run_event(11502003)  # Appears during Sen's Golem battle.
    run_event(11502004)  # Appears when Sen's Golem is already dead.
    run_event(11502005)  # Death.
    run_event(11502006)  # 'Fled' message.

    # Mimic.
    for mimic_event_id in (5010, 5011, 5012, 5013, 5014, 900, 5015):
        run_event(11500000 + mimic_event_id)
    run_event(11502010)  # (New) Mimic replaces a random chest.

    # One-hole dart traps. Most have hard-coded angles inside, so the angle argument may be unused.
    for dart_trap, angle in enumerate((0, 90, 90, 270, 180, 270)):
        run_event_with_slot(11505270 + dart_trap, 0, args=(1502200 + dart_trap, 1501200 + dart_trap, 1503500,
                                                           1501210 + dart_trap, angle, 11505280 + dart_trap))

    run_event(11505260)  # Four-hole dart trap on side wall.

    # Non-respawning enemies.
    for slot, enemy_id, treasure_lot in (
            (0, 6600, 0),  # Undead Prince Ricard
            (1, 1500300, 0),  # Titanite Demons
            (2, 1500301, 0),
            (3, 1500302, 0),
            (4, 1500303, 0),
            (5, 1500100, 0),  # Bomb-throwing Giant
            (7, 1500102, 28600300)   # Gate-opening Giant (rewards Hawk Ring)
    ):
        run_event_with_slot(11500860, slot, args=(enemy_id, treasure_lot))

    # (New) Darkwraiths spawn once if Jareel is in Dark Anor Londo.
    run_event_with_slot(11502001, 0, args=(Darkwraiths[0],))
    run_event_with_slot(11502001, 1, args=(Darkwraiths[1],))
    skip_if_event_flag_off(1, EVENT.DarkAnorLondo)
    chr.disable(1500877)  # Disable Serpent Mage near second Darkwraith.

    # Five treasure chests. Mimic will replace one.
    run_event_with_slot(11500600, 0, args=(1501650, 11500600))
    run_event_with_slot(11500600, 2, args=(1501652, 11500602))
    run_event_with_slot(11500600, 4, args=(1501654, 11500604))
    run_event_with_slot(11500600, 9, args=(1501659, 11500609))
    run_event_with_slot(11500600, 10, args=(1501660, 11500610))


def event50():
    """ NPC constructor. """
    header(50, 0)

    # (NEW) SELLSWORD TISHANNA (invasion)

    # chr.humanity_registration(SellswordTishana, 8366)  # Not bothering.
    run_event(11505630)
    run_event(11500810)

    # UNDEAD PRINCE RICARD (Hollow)

    chr.humanity_registration(CHR.UndeadPrinceRicard, 8980)

    # BLACK IRON TARKUS

    chr.humanity_registration(CHR.BlackIronTarkusSummon, 8924)
    run_event(11505030)
    run_event(11505032)

    # BIG HAT LOGAN

    chr.humanity_registration(CHR.Logan, 8334)
    skip_if_event_flag_on(3, 1090)  # Logan is imprisoned.
    skip_if_event_flag_on(2, 1091)
    skip_if_event_flag_on(1, 1096)
    chr.disable(CHR.Logan)
    run_event_with_slot(11500510, 0, args=(CHR.Logan, 1096))
    run_event_with_slot(11500520, 0, args=(CHR.Logan, 1090, 1109, 1097))
    run_event(11500530)  # Can't open the cage until you talk to Logan.
    run_event_with_slot(11500531, 0, args=(CHR.Logan, 1090, 1109, 1091))  # Logan is freed.
    run_event_with_slot(11500532, 0, args=(CHR.Logan, 1090, 1109, 1092))  # Logan disappears.

    # GRIGGS OF VINHEIM (Hollow)

    chr.set_team_type_and_exit_standby_animation(CHR.HollowGriggs, TeamType.hostile_ally)
    skip_if_event_flag_on(1, 1117)
    chr.disable(CHR.HollowGriggs)
    run_event_with_slot(11500537, args=(CHR.HollowGriggs, 1110, 1119, 1117))

    # SIEGMEYER OF CATARINA

    chr.humanity_registration(CHR.Siegmeyer, 8446)
    skip_if_event_flag_on(3, 1512)
    skip_if_event_flag_on(2, 1491)
    skip_if_event_flag_on(1, 1492)
    chr.disable(CHR.Siegmeyer)  # Only enabled during 1491-1492.
    run_event_with_slot(11500510, 2, args=(CHR.Siegmeyer, 1512))
    run_event_with_slot(11500520, 2, args=(CHR.Siegmeyer, 1490, 1539, 1513))
    # (Changed) Siegmeyer appears and you didn't speak to him in Blighttown.
    run_event_with_slot(11500534, args=(CHR.Siegmeyer, 1490, 1539, 1491))
    # (Changed) Siegmeyer appears and you did speak to him in Blighttown.
    run_event_with_slot(11500535, args=(CHR.Siegmeyer, 1490, 1539, 1492))
    # Leaves second position after de-loading if you rotate the boulder switch.
    run_event_with_slot(11500536, args=(CHR.Siegmeyer, 1490, 1539, 1493))

    # CRESTFALLEN MERCHANT

    chr.humanity_registration(CHR.CrestfallenMerchant, 8422)
    skip_if_event_flag_range_not_all_off(1, 1420, 1429)
    flag.enable(1420)
    run_event_with_slot(11500510, 3, args=(CHR.CrestfallenMerchant, 1421))  # Hostile.
    run_event_with_slot(11500520, 3, args=(CHR.CrestfallenMerchant, 1420, 1429, 1422))  # Dead.

    # (NEW) ANDRE OF ASTORA

    run_event_with_slot(11500510, 4, args=(CHR.Andre, 1321))  # Hostile.
    run_event_with_slot(11500520, 4, args=(CHR.Andre, 1320, 1339, 1322))  # Dead.
    run_event_with_slot(11015090, 0, args=(1321, 1322, 1011010))  # Disable chair.


def event11500534():
    """ Siegmeyer appears in Fortress and you did speak to him in Blighttown (but didn't open the gate). """
    header(11500534)
    siegmeyer, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1512)
    if_event_flag_on(1, 1490)
    if_event_flag_on(1, 11500591)  # spoken to in Blighttown
    if_event_flag_on(1, EVENT.ScriptedBoulderDone)
    if_condition_true(0, 1)

    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.enable(siegmeyer)


def event11500535():
    """ Siegmeyer appears in Fortress and you didn't speak to him in Blighttown (or open the gate). """
    header(11500535)
    siegmeyer, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1512)
    if_event_flag_on(1, 1490)
    if_event_flag_off(1, 11500591)  # NOT spoken to in Blighttown
    if_event_flag_on(1, EVENT.ScriptedBoulderDone)
    if_condition_true(0, 1)

    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.enable(siegmeyer)


def event11500201():
    """ Main gate now opens immediately. """
    header(11500201, 0)
    flag.enable(11500200)  # Not sure where this is actually enabled.
    anim.end_animation(1501000, 0)
    if_player_inside_region(0, 1502050)
    if_player_outside_area(0, 1502050)
    restart()  # Re-opens gate if player leaves (because it might de-load).


def event11500790():
    """ Boulder trap is loaded. Now happens more frequently. """
    header(11500790, 0)
    if_event_flag_on(0, EVENT.ScriptedBoulderDone)
    if_event_flag_off(1, 11505050)
    if_entity_alive(1, 1500101)  # Boulder-loading Giant is still alive.
    if_condition_true(0, 1)
    flag.enable(11505052)
    wait(5.0)
    obj.enable(1501800)
    anim.force_animation(1501800, 0)
    wait(1.5)
    hitbox.enable_hitbox(1503210)
    wait(2.0)  # (New) Used to be 3.5 seconds.
    wait_for_network_approval(10.0)
    # Determine direction.
    skip_if_event_flag_on(2, 11505210)
    flag.enable(11505220)
    restart()
    skip_if_event_flag_on(2, 11505211)
    flag.enable(11505221)
    restart()
    skip_if_event_flag_on(2, 11505212)
    flag.enable(11505222)
    restart()
    skip_if_event_flag_on(1, 11505213)
    flag.enable(11505223)
    restart()


def event11505270():
    """ First dart trap. """
    header(11505270)
    trigger_area, trigger_object, map_sfx, projectile_id, launch_angle_y, already_triggered_flag = define_args('iiiiii')
    skip_if_event_flag_off(2, already_triggered_flag)
    anim.end_animation(trigger_object, 0)
    skip(12)

    if_player_inside_region(-1, trigger_area)
    if_object_damaged_by(-1, trigger_object, -1)
    if_condition_true(0, -1)
    flag.enable(already_triggered_flag)
    sfx.create_oneoff_sfx(Category.object, trigger_object, 101, 150005)
    sfx.delete_map_sfx(map_sfx, False)
    anim.force_animation(trigger_object, 0, wait_for_completion=True)
    skip_if_equal(5, already_triggered_flag, 11505284)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, launch_angle_y, 0)
    if_number_true_flags_in_range_greater_than_or_equal(0, 11505280, 11505285, 2)
    flag.disable(already_triggered_flag)
    anim.force_animation(trigger_object, 1, wait_for_completion=True)
    restart()


def event11505271():
    """ Second dart trap. """
    header(11505271)
    trigger_area, trigger_object, map_sfx, projectile_id, launch_angle_y, already_triggered_flag = define_args('iiiiii')
    skip_if_event_flag_off(2, already_triggered_flag)
    anim.end_animation(trigger_object, 0)
    skip(12)
    if_player_inside_region(-1, trigger_area)
    if_object_damaged_by(-1, trigger_object, -1)
    if_condition_true(0, -1)
    flag.enable(already_triggered_flag)
    sfx.create_oneoff_sfx(Category.object, trigger_object, 101, 150005)
    sfx.delete_map_sfx(map_sfx, False)
    anim.force_animation(trigger_object, 0, wait_for_completion=True)
    skip_if_equal(5, already_triggered_flag, 11505284)
    for angle in (106, 98, 90, 82, 74):
        spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, angle, 0)
        wait(0.1)
    wait(1.9)
    for angle in (106, 98, 90, 82, 74):
        spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, angle, 0)
        wait(0.1)
    if_number_true_flags_in_range_greater_than_or_equal(0, 11505280, 11505285, 2)
    flag.disable(already_triggered_flag)
    anim.force_animation(trigger_object, 1, wait_for_completion=True)
    restart()


def event11505272():
    header(11505272)
    """ Third dart trap. """
    trigger_area, trigger_object, map_sfx, projectile_id, launch_angle_y, already_triggered_flag = define_args('iiiiii')
    skip_if_event_flag_off(2, already_triggered_flag)
    anim.end_animation(trigger_object, 0)
    skip(12)
    if_player_inside_region(-1, trigger_area)
    if_object_damaged_by(-1, trigger_object, -1)
    if_condition_true(0, -1)
    flag.enable(already_triggered_flag)
    sfx.create_oneoff_sfx(Category.object, trigger_object, 101, 150005)
    sfx.delete_map_sfx(map_sfx, False)
    anim.force_animation(trigger_object, 0, wait_for_completion=True)
    skip_if_equal(5, already_triggered_flag, 11505284)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, 86, 0)
    wait(0.2)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, 90, 0)
    wait(0.2)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, 94, 0)
    if_number_true_flags_in_range_greater_than_or_equal(0, 11505280, 11505285, 2)
    flag.disable(already_triggered_flag)
    anim.force_animation(trigger_object, 1, wait_for_completion=True)
    restart()


def event11505273():
    """ Fourth dart trap. """
    header(11505273)
    trigger_area, trigger_object, map_sfx, projectile_id, launch_angle_y, already_triggered_flag = define_args('iiiiii')
    skip_if_event_flag_off(2, already_triggered_flag)
    anim.end_animation(trigger_object, 0)
    skip(12)
    if_player_inside_region(-1, trigger_area)
    if_object_damaged_by(-1, trigger_object, -1)
    if_condition_true(0, -1)
    flag.enable(already_triggered_flag)
    sfx.create_oneoff_sfx(Category.object, trigger_object, 101, 150005)
    sfx.delete_map_sfx(map_sfx, False)
    anim.force_animation(trigger_object, 0, wait_for_completion=True)
    skip_if_equal(5, already_triggered_flag, 11505284)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 7, launch_angle_y, 0)
    wait(0.1)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 8, launch_angle_y, 0)
    wait(0.1)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 9, launch_angle_y, 0)
    wait(0.1)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 10, launch_angle_y, 0)
    wait(0.1)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 11, launch_angle_y, 0)
    if_number_true_flags_in_range_greater_than_or_equal(0, 11505280, 11505285, 2)
    flag.disable(already_triggered_flag)
    anim.force_animation(trigger_object, 1, wait_for_completion=True)
    restart()


def event11505274():
    """ Fifth dart trap. """
    header(11505274)
    trigger_area, trigger_object, map_sfx, projectile_id, launch_angle_y, already_triggered_flag = define_args('iiiiii')
    skip_if_event_flag_off(2, already_triggered_flag)
    anim.end_animation(trigger_object, 0)
    skip(12)
    if_player_inside_region(-1, trigger_area)
    if_object_damaged_by(-1, trigger_object, -1)
    if_condition_true(0, -1)
    flag.enable(already_triggered_flag)
    sfx.create_oneoff_sfx(Category.object, trigger_object, 101, 150005)
    sfx.delete_map_sfx(map_sfx, False)
    anim.force_animation(trigger_object, 0, wait_for_completion=True)
    skip_if_equal(5, already_triggered_flag, 11505284)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, launch_angle_y, 0)
    wait(0.4)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, launch_angle_y, 0)
    wait(0.4)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, launch_angle_y, 0)
    if_number_true_flags_in_range_greater_than_or_equal(0, 11505280, 11505285, 2)
    flag.disable(already_triggered_flag)
    anim.force_animation(trigger_object, 1, wait_for_completion=True)
    restart()


def event11505275():
    """ Sixth dart trap. """
    header(11505275)
    trigger_area, trigger_object, map_sfx, projectile_id, launch_angle_y, already_triggered_flag = define_args('iiiiii')
    skip_if_event_flag_off(2, already_triggered_flag)
    anim.end_animation(trigger_object, 0)
    skip(12)
    if_player_inside_region(-1, trigger_area)
    if_object_damaged_by(-1, trigger_object, -1)
    if_condition_true(0, -1)
    flag.enable(already_triggered_flag)
    sfx.create_oneoff_sfx(Category.object, trigger_object, 101, 150005)
    sfx.delete_map_sfx(map_sfx, False)
    anim.force_animation(trigger_object, 0, wait_for_completion=True)
    skip_if_equal(5, already_triggered_flag, 11505284)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, launch_angle_y, 0)
    wait(1.2)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, launch_angle_y, 0)
    wait(2.4)
    spawner.shoot_projectile(1500200, projectile_id, 101, 5070, 0, launch_angle_y, 0)
    if_number_true_flags_in_range_greater_than_or_equal(0, 11505280, 11505285, 2)
    flag.disable(already_triggered_flag)
    anim.force_animation(trigger_object, 1, wait_for_completion=True)
    restart()


def event11505260():
    """ Four-hole dart trap. Now shoots in two volleys, and more rapidly. """
    header(11505260, 0)
    if_event_flag_on(0, 11505284)
    wait(0.4)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    wait(0.2)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    wait(0.2)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    wait(0.2)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    wait(0.2)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    wait(1.0)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    wait(0.2)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    wait(0.2)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    wait(0.2)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    wait(0.2)
    for dart in range(214, 218):
        spawner.shoot_projectile(1500200, 1501000 + dart, 101, 5070, 0, 180, 0)
    if_event_flag_off(0, 11505284)
    restart()


def event11502000():
    """ Black Knight Axe only appears above the gate if you if you have the Ashen Ring. """
    header(11502000, 1)
    chr.disable(CHR.BlackKnightAxe)
    skip_if_this_event_off(2)
    chr.kill(CHR.BlackKnightAxe, False)
    end()
    if_player_has_ring(0, RING.RingOfAsh)
    chr.enable(CHR.BlackKnightAxe)
    if_entity_dead(0, CHR.BlackKnightAxe)
    flag.enable(EVENT.BlackKnightAxeDead)
    item.award_item_to_host_only(27902000)  # BKA, Red Chunk
    for flag_id in (EVENT.BlackKnightSwordDead, EVENT.BlackKnightGreatswordDead,
                    EVENT.BlackKnightHalberdDead, EVENT.BlackKnightAxeDead):
        if_event_flag_on(1, flag_id)
    skip_if_condition_true(2, 1)
    message.status_explanation(TEXT.RingOfAshWarms, pad_enabled=True)
    end()
    flag.enable(EVENT.AllBlackKnightsDead)
    message.status_explanation(TEXT.RingOfAshHot, pad_enabled=True)


def event11502010():
    """ Move Mimic to replace a random chest. Uses flags 2011-2015 to remember which chest it replaced. """
    header(11502010, 1)

    # First time: choose random chest to replace.
    skip_if_this_event_on(2)
    flag.enable_random_in_chunk(11502011, 11502015)
    flag.enable(11502010)  # One-off flag chosen.
    for mimic_flag, chest, chest_warp, chest_item in (
            (11502011, 1501650, 1502875, 1500000),
            (11502012, 1501652, 1502876, 1500020),
            (11502013, 1501654, 1502877, 1500040),
            (11502014, 1501659, 1502878, 1500090),
            (11502015, 1501660, 1502879, 1500100)):
        skip_if_event_flag_off(7, mimic_flag)
        obj.disable(chest)
        obj.disable_activation(chest, -1)
        end_if_event_flag_on(11500900)  # Mimic dead.
        warp.warp(CHR.Mimic, Category.region, chest_warp, -1)
        if_entity_dead(0, CHR.Mimic)
        item.award_item_to_host_only(chest_item)
        end()


def event11505014():
    """ Mimic area control. Now checks the appropriate area for its random position. """
    header(11505014, 1)
    if_event_flag_on(0, 11502010)  # Wait for random position.
    if_singleplayer(1)
    for area in range(2011, 2016):
        skip_if_event_flag_off(1, 11500000 + area)
        if_entity_inside_area(1, CHR.Mimic, 1500000 + area)
    if_entity_backread_disabled(1, CHR.Mimic)
    if_condition_true(0, 1)
    chr.set_special_effect(CHR.Mimic, 5421)
    chr.clear_ai_target_list(CHR.Mimic)
    chr.replan_ai(CHR.Mimic)
    for area in range(2011, 2016):
        skip_if_event_flag_off(1, 11500000 + area)
        warp.short_warp(CHR.Mimic, Category.region, 1500000 + area, -1)
    if_entity_backread_enabled(0, CHR.Mimic)
    restart()


def event11502001():
    """ Darkwraiths spawn in Dark Anor Londo if Jareel is alive. Two slots, so uses 11502002 as well. """
    header(11502001, 1)
    darkwraith, = define_args('i')

    skip_if_this_event_off(3)
    chr.disable(darkwraith)
    chr.drop_mandatory_treasure(darkwraith)
    end()

    chr.disable(darkwraith)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_off(1, EVENT.JareelDead)
    if_condition_true(0, 1)
    chr.enable(darkwraith)
    if_entity_health_less_than_or_equal(0, darkwraith, 0.0)
    end()


def event11502003():
    """ Capricious Thrall appears once *during* Sen's Golem battle. """
    header(11502003, 1)
    chr.disable(CHR.CapriciousThrall)
    end_if_this_event_on()

    if_event_flag_on(1, 11505392)
    if_event_flag_off(1, 11)
    if_event_flag_on(1, EVENT.CapriciousThrallActive)
    if_condition_true(0, 1)
    wait(10.0)
    flag.enable(11502003)  # This won't happen again.
    flag.enable(11502004)  # No encounter after Sen's Golem dies, either.
    flag.enable(EVENT.ThrallAmbushOngoing)
    boss.enable_boss_health_bar_with_slot(CHR.CapriciousThrall, 1, TEXT.CapriciousThrallName)
    chr.enable(CHR.CapriciousThrall)
    anim.force_animation(CHR.CapriciousThrall, ANIM.ThrallAmbushAttack, wait_for_completion=True)

    wait(100.0)  # Battle timer.

    end_if_event_flag_on(11502005)  # Already dead and handled.
    chr.enable_invincibility(CHR.CapriciousThrall)
    sound.play_sound_effect(CHR.CapriciousThrall, SoundType.s_sfx, 777777777)  # For effect.
    wait(3.0)  # so sound effect can build up and slightly mask the abrupt music stop
    anim.force_animation(CHR.CapriciousThrall, ANIM.ThrallRetreat)
    wait(1.4)
    chr.disable(CHR.CapriciousThrall)
    flag.enable(EVENT.ThrallEncounterDone)
    flag.disable(EVENT.ThrallAmbushOngoing)  # Battle is over.
    boss.disable_boss_health_bar_with_slot(CHR.CapriciousThrall, 0, TEXT.CapriciousThrallName)
    # 'Fled' message will already be triggered, because 'ThrallAmbushOngoing' disabled above.

    skip_if_event_flag_on(2, EVENT.SensIronGolemDead)
    boss.enable_boss_health_bar(CHR.SensIronGolem, TEXT.SensIronGolemName)
    end()

    # Only disable fog, re-enable pickup ring, and instruct bomb giant if Golem is dead.
    sfx.create_map_sfx(1503010)  # Pickup ring.
    obj.disable(1501990)  # Disable fog.
    sfx.delete_map_sfx(1501991)  # Stop fog effect.
    chr.ai_instruction(1500100, 10, 0)  # Bomb-throwing giant.
    chr.replan_ai(1500100)


def event11502004():
    """ Capricious Thrall appears *once* if Sen's Golem is already dead. """
    header(11502004, 1)
    chr.disable(CHR.CapriciousThrall)
    end_if_this_event_on()

    if_this_event_off(1)  # So Thrall doesn't reappear immediately after battle.
    if_event_flag_on(1, 11)  # Sen's Golem is dead.
    if_player_inside_region(1, REGION.CapriciousThrallSoloTrigger)  # Close to pickup point.
    if_event_flag_on(1, EVENT.CapriciousThrallActive)
    if_condition_true(0, 1)

    sfx.delete_map_sfx(1503010)  # Pickup ring.
    obj.enable(1501990)  # Enable fog.
    sfx.create_map_sfx(1501991)  # Enable fog effect.
    sound.enable_map_sound(1503801)  # Enable Thrall music.
    flag.enable(11502003)  # No solo encounter.
    flag.enable(11502004)  # This won't happen again.
    flag.enable(EVENT.ThrallAmbushOngoing)  # Marks Thrall battle as ongoing.
    boss.enable_boss_health_bar_with_slot(CHR.CapriciousThrall, 0, TEXT.CapriciousThrallName)
    chr.enable(CHR.CapriciousThrall)
    anim.force_animation(CHR.CapriciousThrall, ANIM.ThrallAmbushAttack, wait_for_completion=True)

    wait(100.0)  # Battle timer.

    end_if_event_flag_on(11502005)  # Already dead and handled.
    sound.disable_map_sound(1503801)
    chr.enable_invincibility(CHR.CapriciousThrall)
    sound.play_sound_effect(CHR.CapriciousThrall, SoundType.s_sfx, 777777777)  # For effect.
    wait(2)  # so sound effect can build up and slightly mask the abrupt music stop
    anim.force_animation(CHR.CapriciousThrall, ANIM.ThrallRetreat)
    wait(1.4)
    chr.disable(CHR.CapriciousThrall)
    flag.enable(EVENT.ThrallEncounterDone)
    flag.disable(EVENT.ThrallAmbushOngoing)
    boss.disable_boss_health_bar_with_slot(CHR.CapriciousThrall, 0, TEXT.CapriciousThrallName)

    sfx.create_map_sfx(1503010)  # Pickup ring.
    obj.disable(1501990)  # Disable fog.
    sfx.delete_map_sfx(1501991)  # Stop fog effect.


def event11502005():
    """ Capricious Thrall is killed. """
    header(11502005, 0)
    end_if_event_flag_on(11502003)  # Encounter done, nothing to check.

    if_event_flag_on(1, EVENT.ThrallAmbushOngoing)
    if_entity_health_less_than_or_equal(1, CHR.CapriciousThrall, 0.0)
    if_condition_true(0, 1)
    wait(1)
    sound.play_sound_effect(CHR.CapriciousThrall, SoundType.s_sfx, 777777777)
    if_entity_dead(0, CHR.CapriciousThrall)
    boss.kill_boss(CHR.CapriciousThrallBoss)
    flag.disable(EVENT.CapriciousThrallActive)
    flag.enable(EVENT.CapriciousThrallDead)  # Story flag for Thrall
    flag.disable(EVENT.ThrallAmbushOngoing)
    flag.enable(EVENT.ThrallEncounterDone)

    skip_if_event_flag_on(2, EVENT.SensIronGolemDead)
    boss.enable_boss_health_bar(CHR.SensIronGolem, TEXT.SensIronGolemName)
    end()

    boss.disable_boss_health_bar(CHR.CapriciousThrall, TEXT.CapriciousThrallName)  # (Redundant.)
    sfx.create_map_sfx(1503010)  # Pickup ring to Anor Londo.
    sound.disable_map_sound(1503801)
    obj.disable(1501990)
    sfx.delete_map_sfx(1501991)
    chr.ai_instruction(1500100, 10, 0)  # Bomb-throwing giant.
    chr.replan_ai(1500100)


def event11505395():
    """ Sen's Golem music only turns off if Thrall is also dead. """
    header(11505395, 0)
    network.disable_sync()
    if_event_flag_on(1, 11)
    if_event_flag_on(1, 11505394)
    if_event_flag_off(1, EVENT.ThrallAmbushOngoing)
    if_condition_true(0, 1)
    sound.disable_map_sound(1503800)
    sound.play_sound_effect(1502990, SoundType.a_ambient, 150200002)


def event11500210():
    """ Demons take you to Anor Londo if you replaced the Pale Eye Orb and the Thrall isn't there. """
    header(11500210, 0)
    end_if_client()
    if_in_world_area(0, 15, 0)
    if_time_elapsed(0, 5.0)
    if_event_flag_on(0, 11)
    if_event_flag_off(1, EVENT.ThrallAmbushOngoing)
    if_action_button_state(1, Category.region, 1502505, 0.0, -1, 0.0, 10010120)
    if_condition_true(0, 1)

    if_event_flag_on(7, EVENT.PaleEyeOrbReturned)
    skip_if_condition_true(3, 7)
    message.dialog(TEXT.AbandonedPost, 1, 6, 1502505, 3.0)
    wait(3.0)
    restart()

    # Pale Demons come to pick you up.
    wait(3.0)
    chr.disable_backread(1500201)
    wait_frames(1)
    skip_if_event_flag_on(2, EVENT.DarkAnorLondo)
    cutscene.play_cutscene_and_warp_specific_player(150000, CutsceneType.skippable, 1502501, 15, 1, CHR.Player)
    skip(1)
    cutscene.play_cutscene_and_warp_specific_player(150002, CutsceneType.skippable, 1502501, 15, 1, CHR.Player)
    wait_frames(1)
    game.award_achievement(33)
    restart()


def event11015090():
    """ Andre breaks his chair when he gets up while hostile. Reset when sin is absolved. (Moved from Burg.) """
    header(11015090, 1)
    andre_hostile, andre_dead, chair = define_args('iii')
    end_if_event_flag_on(andre_hostile)
    end_if_event_flag_on(andre_dead)
    obj.enable_invulnerability(chair)
    if_event_flag_on(-1, andre_hostile)
    if_event_flag_on(-1, andre_dead)
    if_condition_true(0, -1)
    obj.disable_invulnerability(chair)
    wait_frames(1)
    obj.destroy(chair, 1)
    sound.play_sound_effect(chair, SoundType.o_object, 125200000)
    flag.enable(11015090)
    if_event_flag_on(0, 703)
    end()


def event11500510():
    """ NPC becomes hostile. Need to debug Andre. """
    header(11500510)
    npc, hostile_flag = define_args('ii')
    if_entity_health_less_than_or_equal(1, npc, 0.9)
    if_entity_health_greater_than(1, npc, 0.0)
    if_entity_attacked_by(1, npc, CHR.Player)
    if_event_flag_on(2, hostile_flag)
    if_this_event_slot_on(2)
    if_event_flag_on(3, hostile_flag)
    if_this_event_slot_off(3)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(0, -1)
    skip_if_condition_false_finished(2, 3)
    chr.disable(npc)
    if_event_flag_on(0, 703)
    flag.enable(hostile_flag)
    chr.set_team_type_and_exit_standby_animation(npc, TeamType.hostile_ally)
    network.save_request()


def event11500102():
    """ Unlock cage elevator. """
    header(11500102)
    skip_if_this_event_off(3)
    skip_if_event_flag_on(1, 11500100)
    anim.end_animation(1501011, 20)
    end()

    if_player_has_good(1, GOOD.TortureCageKey)
    if_player_has_good(-1, GOOD.MasterKey)
    if_condition_true(-1, 1)
    if_condition_true(2, -1)
    if_action_button_state(2, Category.object, 1501011, 60.0, 105, 2.0, 10010400)
    if_condition_true(0, 2)
    warp.short_warp(CHR.Player, Category.object, 1501011, 120)
    anim.force_animation(CHR.Player, 7111)
    anim.force_animation(1501011, 10)
    end_if_client()
    skip_if_condition_true_finished(3, 1)
    message.dialog(10010883, ButtonType.yes_no, NumberButtons.no_button, -1, 3.0)
    item.remove_items_from_player(ItemType.good, GOOD.MasterKey, 0)  # Break Master Key.
    end()
    message.dialog(10010862, ButtonType.yes_no, NumberButtons.no_button, -1, 3.0)


def event11500103():
    """ Inspect cage elevator without a key. """
    header(11500103)
    network.disable_sync()
    if_event_flag_off(1, 11500102)
    if_player_does_not_have_good(1, GOOD.TortureCageKey)
    if_player_does_not_have_good(1, GOOD.MasterKey)
    if_action_button_state(1, Category.object, 1501011, 60.0, 105, 2.0, 10010400)
    if_condition_true(0, 1)
    message.dialog(10010163, ButtonType.yes_no, NumberButtons.no_button, -1, 3.0)
    wait(3.0)
    restart()


def event11500110():
    """ Open other cages with Torture Cage Key or Master Key. """
    header(11500110)
    door_id, door_flag = define_args('ii')

    skip_if_this_event_slot_off(3)
    anim.end_animation(door_id, 0)
    obj.disable_activation(door_id, -1)
    end()

    if_object_activated(0, door_flag)
    flag.enable(door_flag)
    end_if_client()
    if_player_has_good(1, GOOD.TortureCageKey)
    skip_if_condition_true(3, 1)
    message.dialog(10010883, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)
    item.remove_items_from_player(ItemType.good, GOOD.MasterKey, 0)  # Break Master Key.
    end()
    message.dialog(10010862, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)


def event11502500():
    """ Checks whether stable footing should be enabled inside Golem arena. """
    header(11502500, 1)
    flag.disable(EVENT.SensGolemStableFooting)
    if_event_flag_on(1, EVENT.SensIronGolemDead)
    if_event_flag_off(-1, EVENT.CapriciousThrallActive)
    if_event_flag_on(-1, EVENT.ThrallEncounterDone)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    flag.enable(EVENT.SensGolemStableFooting)


def event11500860():
    """ Stop enemies from respawning, and drop mandatory treasure if instructed. """
    header(11500860, 1)
    entity, treasure_lot = define_args('ii')
    skip_if_this_event_slot_off(3)
    chr.disable(entity)
    chr.kill(entity, False)
    end()

    if_entity_dead(0, entity)
    skip_if_equal(1, treasure_lot, 0)
    item.award_item_to_host_only(treasure_lot)
    end()


def event11505070():
    """ Giant stun time, now variable. """
    header(11505070, 1)
    giant, stun_duration = define_args('if')
    network.disable_sync()
    if_has_tae_event(0, giant, 1400)
    wait(stun_duration)
    chr.ezstate_ai_request(giant, 1501, 0)
    restart()


def event11505630():
    """ New NPC invasion: Sellsword Tishana. """
    header(11505630)
    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11505631)
    # No longer requires Golem to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 11500810)
    skip_if_this_event_on(1)
    if_player_inside_region(1, REGION.SellswordTishanaTrigger)
    if_condition_true(0, 1)
    message.place_summon_sign(
        SummonSignType.black_eye_sign, 6860, REGION.SellswordTishanaSignPoint, 11505631, 11505632)
    wait(20.0)
    restart()


def event11500810():
    """ Sellsword Tishana invader dies. """
    header(11500810)
    skip_if_host(3)
    if_event_flag_on(1, 11505631)
    if_event_flag_off(1, 11505632)
    skip_if_condition_true(1, 1)
    chr.disable(CHR.SellswordTishana)
    end_if_this_event_on()
    if_entity_dead(0, CHR.SellswordTishana)
    flag.enable(11500810)


def event11502006():
    """ Message informs you that Thrall has departed the Lower Burg when you return after dying. """
    header(11502006)
    end_if_this_event_on()
    if_event_flag_on(1, 11502003)  # Thrall appearance here done (solo or with Golem).
    if_event_flag_on(1, EVENT.CapriciousThrallActive)
    if_event_flag_off(1, 11512060)  # Anor Londo ambush has not yet occurred.
    if_event_flag_off(1, EVENT.ThrallAmbushOngoing)
    if_player_inside_region(1, 1502990)  # Golem arena.
    if_condition_true(0, 1)
    message.status_explanation(TEXT.ThrallHasFled)


def event11500001():
    """ Sen's Golem dies. Only disables fog wall if Thrall isn't still present. """
    header(11500001)
    sfx.delete_map_sfx(1503010, False)

    if_entity_dead(0, CHR.SensIronGolem)
    flag.enable(EVENT.SensIronGolemDead)
    boss.kill_boss(CHR.SensIronGolem)

    skip_if_event_flag_on(6, EVENT.ThrallAmbushOngoing)
    obj.disable(1501990)
    sfx.delete_map_sfx(1501991, True)
    sfx.create_map_sfx(1503010)
    chr.ai_instruction(1500100, 10, 0)  # Bomb-throwing giant.
    chr.replan_ai(1500100)
    skip(1)
    boss.enable_boss_health_bar_with_slot(CHR.CapriciousThrall, 0, TEXT.CapriciousThrallName)

    # Domnhall will stock Golem armor set.
    flag.disable(11807020)
    flag.disable(11807030)
    flag.disable(11807040)
    flag.disable(11807050)

    network.disable_sync()
    wait(3.0)
    chr.disable(CHR.SensIronGolem)
    chr.disable_backread(CHR.SensIronGolem)


def event11500537():
    """ Griggs moves to Sen's Fortress and goes Hollow. """
    header(11500537)
    griggs_hollow, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1114)
    if_event_flag_off(1, 1117)
    if_event_flag_on(1, 1113)
    if_event_flag_on(1, 723)  # Griggs is sold out (including Logan's two donated spells).
    if_in_world_area(1, 15, 0)
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.enable(griggs_hollow)


def event11505030():
    """ Black Iron Tarkus summon sign (only if Anor Londo not visited already). """
    header(11505030)
    skip_if_client(1)
    chr.set_network_update_authority(CHR.BlackIronTarkusSummon, UpdateAuthority.forced)
    skip_if_event_flag_on(3, 11505033)
    if_client(2)
    if_event_flag_on(2, 11505031)
    skip_if_condition_true(1, 2)
    chr.disable(CHR.BlackIronTarkusSummon)
    end_if_event_flag_on(EVENT.SensIronGolemDead)

    if_event_flag_off(1, EVENT.AnorLondoVisited)
    if_host(1)
    if_character_human(1, CHR.Player)
    if_entity_backread_enabled(1, CHR.BlackIronTarkusSummon)
    if_player_within_distance(1, CHR.BlackIronTarkusSummon, 10.0)
    if_condition_true(0, 1)
    message.place_summon_sign(SummonSignType.blue_eye_sign, CHR.BlackIronTarkusSummon, 1502000, 11505031, 11505033)


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
