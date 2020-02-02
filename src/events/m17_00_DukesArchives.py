
import sys
import inspect
from pydses import *

map_name = 'm17_00_00_00'  # Duke's Archives / Crystal Cave
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11700000
BASE_PART = 1700000


class DEBUG(IntEnum):
    THRALL_ACTIVE = False
    AWARD_SOUL_OF_PRISCILLA = False
    DARK_ANOR_LONDO = False
    GET_ALL_LORD_SOULS = False
    SIEGLINDE_APPEARS = False
    HAVEL_AT_ASH_LAKE = False


class EVENT(IntEnum):
    SeathDead = 14
    CapriciousThrallActive = 11012010
    CapriciousThrallTrapped = 11012011
    CapriciousThrallDead = 11012012
    DarkAnorLondo = 11510400
    HavelTrapped = 1890
    HavelFreed = 1891
    HavelInsane = 1892
    HavelRestingAtAshLake = 1893
    HavelVanished = 1895
    HavelHostile = 1896  # but not insane
    HavelDead = 1899
    EmpyreanWitness = 11502022
    SeathLeftTower = 11700000
    SeathDeparted = 11702000
    AlarmRinging = 61700105
    JeremiahEscaped = 11412054


class GOOD(IntEnum):
    SoulOfPriscilla = 707
    ArchiveCellKey = 2004
    ArchivePrisonEntranceKey = 2005
    ArchiveGiantCellKey = 2006  # For Logan's cell
    ArchiveLostCellKey = 2020  # For Havel's cell
    PaleEyeOrb = 2530


class ITEMLOT(IntEnum):
    ArchiveCellKey = 6610
    SoulOfPriscilla = 2520
    ArchiveGiantCellKey = 2080


class REGION(IntEnum):
    OutsidePrisonCell = 1702675
    BottomOfPrison = 1702676
    CapriciousThrallReset = 1702677
    TopOfPrisonLadder = 1702678
    AtBonfireCellDoor = 1702679
    BottomOfExitLadder = 1702681
    InvisibleTuskMove = 1702875
    InvisibleTuskTrigger = 1702876


class SOUND(IntEnum):
    CapriciousThrallBGM = 1703802


class TEXT(IntEnum):
    CapriciousThrallName = 2245
    SeathName = 5290
    ItsLocked = 10010163
    Open = 10010400
    PaleEyeOrbQuivers = 10010737
    UsedArchiveCellKey = 10010863


class ANIM(IntEnum):
    ThrallTransformation = 4000
    ThrallRetreat = 4001
    ThrallAmbushAttack = 4002
    SittingOneKneeUp = 7825
    KneelAndFadeOut = 8305


class CHR(IntEnum):
    Player = 10000
    Logan = 6032
    LoganHollow = 6033
    RheaHollow = 6073
    Sieglinde = 6291
    Havel = 6580
    CrystalGeneral = 6610
    ArchivesWitch = 6830
    JeremiahLoot = 6774
    SleepingGuard = 1700100
    InvisibleTusk = 1700191
    CapriciousThrall = 1700750
    CapriciousThrallBoss = 1010751
    SeathInTower = 1700700
    Seath = 1700800
    SeathTail = 1700801
    SeathAbandonedSoul = 1700802
    BonfireGolem = 1700875


def event0():
    """ Constructor. """
    header(0, 0)

    if DEBUG.THRALL_ACTIVE:
        flag.disable(EVENT.CapriciousThrallDead)
        flag.disable(EVENT.CapriciousThrallTrapped)
        flag.enable(EVENT.CapriciousThrallActive)
    if DEBUG.AWARD_SOUL_OF_PRISCILLA:
        item.award_item_to_host_only(ITEMLOT.SoulOfPriscilla)
    if DEBUG.DARK_ANOR_LONDO:
        flag.enable(EVENT.DarkAnorLondo)
    if DEBUG.GET_ALL_LORD_SOULS:
        item.award_item_to_host_only(2630)
        item.award_item_to_host_only(2640)
        item.award_item_to_host_only(2560)
        item.award_item_to_host_only(2580)
    if DEBUG.SIEGLINDE_APPEARS:
        # Sets Siegmeyer's flags.
        flag.disable_chunk(1490, 1539)
        flag.enable(1501)
    if DEBUG.HAVEL_AT_ASH_LAKE:
        flag.disable_chunk(1890, 1899)
        flag.enable(EVENT.HavelRestingAtAshLake)

    skip_if_event_flag_off(1, EVENT.DarkAnorLondo)
    light.set_area_texture_parambank_slot_index(17, 1)

    skip_if_event_flag_on(2, EVENT.SeathDeparted)
    skip_if_event_flag_on(1, EVENT.SeathDead)
    skip(1)
    map.register_bonfire(11700920, 1701950)   # Crystal Cave bonfire, only if Seath is dead or departed.
    skip_if_event_flag_off(1, 11702050)
    map.register_bonfire(11700992, 1701960)  # Bonfire before garden (warpable).
    run_event(11702044)  # (New) Monitor warping to main garden bonfire.
    map.register_bonfire(11700984, 1701961)  # Prison bonfire.
    map.register_bonfire(11700976, 1701962)  # First bonfire before elevator.
    for ladder_id, ladder_flag_1, ladder_flag_2 in zip(range(1140, 1144), range(10, 17, 2), range(11, 18, 2)):
        map.register_ladder(BASE_FLAG + ladder_flag_1, BASE_FLAG + ladder_flag_2, BASE_PART + ladder_id)
    for statue_id in range(1900, 1908):
        obj.register_statue_object(BASE_PART + statue_id, 17, 0, StatueType.crystal)

    # Disable summon-only fog.
    skip_if_client(5)
    flag.enable(405)
    obj.disable(1701994)
    sfx.delete_map_sfx(1701995, False)
    obj.disable(1701996)
    sfx.delete_map_sfx(1701997, False)

    skip_if_event_flag_off(1, 11700140)  # If prison door is open, disable tower Seath.
    flag.disable(405)

    # Check to see if prison alarm should remain ringing (host only).
    skip_if_client(9)
    skip_if_event_flag_off(8, EVENT.AlarmRinging)
    if_player_inside_region(1, 1702410)  # Inside Prison Tower.
    if_player_inside_region(-1, 1702402)
    if_player_inside_region(-1, 1702403)
    if_condition_true(1, -1)
    skip_if_condition_true(2, 1)
    flag.enable(EVENT.AlarmRinging)
    skip(1)
    flag.disable(EVENT.AlarmRinging)

    # Main prison door is open.
    skip_if_event_flag_off(1, 11700002)
    anim.end_animation(1701410, 0)

    # Prison alarm animation.
    skip_if_event_flag_off(1, EVENT.AlarmRinging)
    anim.force_animation(1701400, 1)

    # Checkpoint fog (just before garden).
    run_event_with_slot(11700083, 0, args=(1701706, 1701707, 1702606, 1702607))

    flag.enable(11700086)  # This was enabled when the golden fog was disabled. No idea what it does.

    # Gravelord.
    for gravelord_event in range(11705080, 11705083):
        run_event(gravelord_event)

    # IMMORTAL TOWER SEATH

    for tower_seath_event in (5380, 5381, 5386, 5382, 5383, 5384, 5385):
        # 5380: Host enters fog.
        # 5381: Summon enters fog.
        # 5386: Boss notification.
        # 5382: Player exits fog.
        # 5383: Enable Seath's AI.
        # 5384: Enable/disable music.
        # 5385: Enable immortality and delete boss after move.
        run_event(BASE_FLAG + tower_seath_event)

    # MOVING FURNITURE

    # Descending staircase before garden.
    run_event(11700110)
    # Moving bookshelves.
    run_event_with_slot(11700120, 0, args=(11700120, 1701120, 1701121, 0, 0))
    run_event_with_slot(11700120, 5, args=(11700125, 1701125, 1701126, 1, 1))
    # Gondola request (160) and movement (105).
    run_event_with_slot(11700160, 0, args=(11700100, 1701100, 11700210, 11700211, 11705090, 11705180, 11705181))
    run_event_with_slot(11700105, 0, args=(11700100, 1701100, 1701101, 1701102, 11705090, 11705180, 11705181))
    run_event_with_slot(11700160, 1, args=(11700102, 1701130, 11700220, 11700221, 11705091, 11705182, 11705183))
    run_event_with_slot(11700105, 2, args=(11700102, 1701130, 1701131, 1701132, 11705091, 11705182, 11705183))
    # Gondola cannot be called.
    for slot, args in enumerate(zip((11700100, 11700100, 11700102, 11700102), (0, 1, 0, 1),
                                    (1701101, 1701102, 1701131, 1701132),
                                    (11705090, 11705090, 11705091, 11705091))):
        run_event_with_slot(11700090, slot, args=args, arg_types='iBii')

    # Rotating staircase. Both are activated by the same event (5150). The others handle navimesh and hitbox.
    run_event_with_slot(11705150, 0, args=(11700205, 1701200, 1701210))  # Activated together.
    run_event_with_slot(11700200, 0, args=(11700205, 1701200, 1701201, 1703200, 1703201, 1703010, 1703011, 11705151))
    run_event_with_slot(11700200, 1, args=(11700205, 1701210, 1701211, 1703210, 1703211, 1703012, 1703013, 11705152))
    run_event(11705153)  # (New) Waits for both Channelers to die before stopping endless staircase rotation.
    # Toggles a wall hitbox if you're on an elevator.
    run_event_with_slot(11700150, 0, args=(1703100, 1702780))
    run_event_with_slot(11700150, 1, args=(1703101, 1702781))

    run_event(11705099)  # (New) Monitors presence in Seath's tower room for Quella (with 11705098).
    run_event(11705100)  # Spawn player in prison if they die in Seath's tower.
    run_event(11702015)  # (New) Crystal General opens your cell if you kill the sleeping guard.
    run_event(11702016)  # (New) Crystal General dies and directly awards the Archive Cell Keys.
    run_event(11705103)  # Activate alarm lever.
    run_event(11705108)  # 10-frame delay before alarm can be activated again.
    run_event(11705101)  # Alarm rings. Modified in template to not require Cell Key.
    run_event(11705102)  # Alarm is already ringing on map load.
    run_event(11700130)  # Disables collision and gravity for sleeping guard.
    run_event(11700132)  # This event doesn't exist - they must've just made the key a drop.
    run_event(11702050)  # (New) Killing Golem reveals bonfire before garden.
    run_event(11702001)  # (New) First Armored Tusk fades in and charges.
    run_event(11702003)  # (New) Empyrean witness; kill one Moonlight Butterfly.

    # Prison doors. (New: they can't be closed after opening, to avoid messing with Havel.)
    for slot, (door_flag, door_message, door_id) in enumerate(zip((300, 311, 302, 313, 304, 305, 320),
                                                                  (863, 863, 863, 879, 863, 863, 865),
                                                                  (500, 501, 502, 503, 504, 505, 506))):
        run_event_with_slot(11700300, slot, args=(BASE_FLAG + door_flag, 10010000 + door_message, 1701000 + door_id))

    run_event(11700140)  # Open prison exit door with Archive Tower Giant Door Key.
    run_event(11700141)  # Display message that exit door is locked.
    run_event(11705170)  # Control warp prohibition (used in common event 710).

    # CAPRICIOUS THRALL

    sound.disable_map_sound(SOUND.CapriciousThrallBGM)

    run_event(11702010)  # Trigger first Thrall appearance, which causes it to become trapped (only runs once).
    run_event(11705372)  # Trigger Thrall behavior. Restarts in case the player leaves (below).
    run_event(11705374)  # If player leaves prison, reset Thrall, stop music, disable health bar.
    run_event(11700910)  # Watch for Thrall death.

    # SEATH THE SCALELESS  (Crystal Cave)

    sound.disable_map_sound(1703800)
    # If Seath already dead or departed:
    skip_if_event_flag_on(1, EVENT.SeathDeparted)
    skip_if_event_flag_off(5, EVENT.SeathDead)
    run_event(11705392)
    obj.disable(1701800)  # Disable Primordial Crystal.
    obj.disable(1701990)  # Disable fog.
    sfx.delete_map_sfx(1701991, False)
    skip(10)
    # Alive:
    for seath_event in (0, 5390, 5391, 5393, 5392, 1, 5394, 5395, 5396, 5397):
        run_event(BASE_FLAG + seath_event)

    run_event(11705200)  # Initializes component events of Channeler warping.

    # Sleeping Man-Eater Shells wake up.
    run_event_with_slot(11705270, 0, args=(1700250, 15.0), arg_types='if')
    run_event_with_slot(11705270, 1, args=(1700251, 15.0), arg_types='if')

    # Serpent-Men run for exit.
    run_event_with_slot(11705140, 0, args=(1700102, 1702150))
    run_event_with_slot(11705140, 1, args=(1700103, 1702151))

    # Moonlight Butterfly wakes up (based on distance).
    run_event_with_slot(11705160, 0, args=(1700350, 3.0), arg_types='if')
    run_event_with_slot(11705160, 1, args=(1700351, 3.0), arg_types='if')
    run_event_with_slot(11705160, 2, args=(1700352, 10.0), arg_types='if')

    # Mimics.
    for slot, (mimic_id, mimic_region) in enumerate(zip((1700400, 1700401), (1702010, 1702011))):
        run_event_with_slot(11705010, slot, args=(mimic_id,))
        run_event_with_slot(11705020, slot, args=(mimic_id,))
        run_event_with_slot(11705030, slot, args=(mimic_id,))
        run_event_with_slot(11705040, slot, args=(mimic_id,))
        run_event_with_slot(11705050, slot, args=(mimic_id, mimic_region))
        run_event_with_slot(11700900, slot, args=(mimic_id,))
        run_event_with_slot(11705060, slot, args=(mimic_id,))

    # Non-respawning enemies.
    run_event_with_slot(11700810, 0, (6610, 0, ITEMLOT.ArchiveCellKey))  # Crystal General
    run_event_with_slot(11700810, 1, (1700450, 1, 33001000))  # Crystal Lizard
    run_event_with_slot(11700810, 2, (1700451, 1, 33001000))  # Crystal Lizard
    run_event_with_slot(11700810, 3, (1700452, 1, 33001000))  # Crystal Lizard
    run_event_with_slot(11700810, 4, (1700453, 1, 33001000))  # Crystal Lizard
    run_event_with_slot(11700810, 5, (1700190, 0, 0))  # Armored Tusk 1
    run_event_with_slot(11700810, 6, (CHR.InvisibleTusk, 0, 0))
    run_event_with_slot(11700810, 10, (1700501, 0, 0))  # Golden Crystal Golem
    run_event_with_slot(11700810, 11, (1700502, 0, 0))  # Golden Crystal Golem
    run_event_with_slot(11700810, 12, (1700150, 0, 0))  # Pisaca Handmaiden 1
    run_event_with_slot(11700810, 13, (1700151, 0, 0))  # Pisaca Handmaiden 2
    run_event_with_slot(11700820, 0, (CHR.ArchivesWitch,))

    # Moonlight Butterfly rewards.
    run_event_with_slot(11705280, 0, args=(1700350,))
    run_event_with_slot(11705280, 1, args=(1700351,))

    # Chests.
    for slot, args in enumerate(zip(range(1701651, 1701667), range(11700601, 11700617))):
        run_event_with_slot(11700600, slot + 1, args)

    # Pisaca AI control.
    for slot, pisaca_id in enumerate(range(110, 128)):
        run_event_with_slot(11705110, slot, args=(BASE_PART + pisaca_id,))
    run_event_with_slot(11705110, 18, args=(1700908,))  # Red phantom
    run_event_with_slot(11705110, 19, args=(1700909,))  # Red phantom

    # Invisible Golem control. Sieglinde's golem is handled in her events.
    for slot, golem in enumerate(range(1700675, 1700686)):
        run_event_with_slot(11700850, slot, args=(golem, 5.0, 3104), arg_types='ifi')


def event50():
    """ Pre-constructor. """
    header(50)

    # (NEW) HAVEL THE ROCK

    skip_if_event_flag_on(4, EVENT.HavelTrapped)
    skip_if_event_flag_on(3, EVENT.HavelFreed)
    skip_if_event_flag_on(2, EVENT.HavelInsane)
    skip_if_event_flag_on(1, EVENT.HavelHostile)
    chr.disable(CHR.Havel)
    run_event_with_slot(11700510, 4, args=(CHR.Havel, EVENT.HavelHostile))  # Hostile
    run_event_with_slot(11700520, 4, args=(CHR.Havel, 1890, 1899, EVENT.HavelDead))  # Dead
    run_event_with_slot(11700546, args=(CHR.Havel, 1890, 1899, EVENT.HavelFreed))  # Freed by player.
    run_event_with_slot(11700547, args=(CHR.Havel, 1890, 1899, EVENT.HavelInsane))  # Goes insane.
    run_event_with_slot(11700548, args=(CHR.Havel, 1890, 1899, EVENT.HavelRestingAtAshLake))  # Escapes to Ash Lake.
    # Dropping the idea of having him died if not immediately escorted out. Too punishing.

    # CRYSTAL GENERAL

    chr.humanity_registration(CHR.CrystalGeneral, 8988)

    # BIG HAT LOGAN (Human and Hollow)

    chr.humanity_registration(CHR.Logan, 8334)
    chr.humanity_registration(CHR.LoganHollow, 8334)
    skip_if_event_flag_range_not_all_off(1, 1093, 1096)
    chr.disable(CHR.Logan)
    skip_if_event_flag_on(1, 1099)
    chr.disable(CHR.LoganHollow)
    chr.set_team_type_and_exit_standby_animation(CHR.LoganHollow, TeamType.hostile_ally)
    # Move Logan to the library if appropriate.
    skip_if_event_flag_off(1, 11700594)
    warp.warp_and_set_floor(CHR.Logan, 'region', 1702501, -1, 1703300)
    run_event_with_slot(11700510, 0, args=(CHR.Logan, 1096))  # Hostile
    run_event_with_slot(11700520, 0, args=(CHR.Logan, 1090, 1109, 1097))  # Dead
    run_event_with_slot(11700520, 1, args=(CHR.LoganHollow, 1090, 1109, 1097))  # Dead
    run_event_with_slot(11700530, args=(CHR.Logan, 1090, 1109, 1093))  # Logan appears when you enter the prison.
    run_event_with_slot(11700531, args=(CHR.Logan, 1090, 1109, 1094))  # Logan is freed by the player. (No change.)
    run_event_with_slot(11700532, args=(CHR.Logan, 1090, 1109, 1095))  # Logan moves when you free him or kill Seath.
    run_event_with_slot(11700533, args=(CHR.Logan, 1090, 1109, 1099, CHR.LoganHollow))  # Logan goes insane.

    # SIEGLINDE OF CATARINA

    chr.humanity_registration(CHR.Sieglinde, 8454)
    skip_if_event_flag_on(2, 1547)
    skip_if_event_flag_on(1, 1542)
    chr.disable(CHR.Sieglinde)
    run_event_with_slot(11700510, 2, args=(CHR.Sieglinde, 1547))  # Hostile
    run_event_with_slot(11700520, 2, args=(CHR.Sieglinde, 1540, 1569, 1548))  # Dead
    run_event_with_slot(11700538, args=(CHR.Sieglinde, 1540, 1569, 1541))  # Makes Golden Golem appear (when close).
    run_event_with_slot(11700539, args=(CHR.Sieglinde, 1540, 1569, 1542))  # Golem is killed and Sieglinde appears.
    run_event_with_slot(11700540, args=(CHR.Sieglinde, 1540, 1569, 1543))  # Sieglinde is spoken to and leaves after.

    # RHEA OF THOROLUND (Hollow)

    chr.set_team_type_and_exit_standby_animation(CHR.RheaHollow, TeamType.hostile_ally)
    skip_if_event_flag_on(1, 1181)
    chr.disable(CHR.RheaHollow)
    run_event_with_slot(11700520, 3, args=(CHR.RheaHollow, 1170, 1189, 1177))
    run_event_with_slot(11700545, args=(CHR.RheaHollow, 1170, 1189, 1181))

    # XANTHOUS KING JEREMIAH (Loot only)

    run_event(11702004)


def event11705392():
    """ Seath behavior trigger (Crystal Cave). Also handles if he's dead or departed. """
    header(11705392, 1)

    skip_if_event_flag_off(4, EVENT.SeathDeparted)
    chr.disable(CHR.Seath)
    chr.disable(CHR.SeathTail)
    chr.drop_mandatory_treasure(CHR.SeathAbandonedSoul)
    end()

    chr.disable(CHR.SeathAbandonedSoul)

    skip_if_event_flag_off(5, EVENT.SeathDead)
    chr.disable(CHR.Seath)
    chr.kill(CHR.Seath, False)
    chr.disable(CHR.SeathTail)
    chr.kill(CHR.SeathTail, False)
    end()

    chr.disable_ai(CHR.Seath)
    if_event_flag_on(1, 11705393)
    if_player_inside_region(1, 1702990)
    if_condition_true(0, 1)
    chr.enable_ai(CHR.Seath)
    boss.enable_boss_health_bar(CHR.Seath, TEXT.SeathName)

    # Enable Seath departure flag if player has Soul of Priscilla, Priscilla's Dagger, or Lifehunt Scythe.
    if_player_has_good(-1, GOOD.SoulOfPriscilla)
    for upgrade_level in (0, 100, 200, 300, 400, 500, 600):
        if_player_has_weapon(-1, 1151000 + upgrade_level)  # Lifehunt Scythe (from any source)
    for upgrade_level in range(0, 6):
        if_player_has_weapon(-1, 104000 + upgrade_level)  # Priscilla's Dagger and upgrades.
    skip_if_condition_false(1, -1)
    flag.enable(EVENT.SeathDeparted)
    # Departed flag will be replaced with Dead flag if Seath is killed in this attempt.


def event11705100():
    """ Spawn player in prison if they die against Seath. Now also activates departure storyline. """
    header(11705100, 0)
    network.disable_sync()
    if_player_inside_region(1, 1702890)
    if_host(1)
    if_entity_dead(1, CHR.Player)
    if_condition_true(0, 1)

    # Enable Seath departure flag if player has Soul of Priscilla, Priscilla's Dagger, or Lifehunt Scythe.
    if_player_has_good(-1, GOOD.SoulOfPriscilla)
    for upgrade_level in (0, 100, 200, 300, 400, 500, 600):
        if_player_has_weapon(-1, 1151000 + upgrade_level)  # Lifehunt Scythe (from any source)
    for upgrade_level in range(0, 6):
        if_player_has_weapon(-1, 104000 + upgrade_level)  # Priscilla's Dagger and upgrades.
    skip_if_condition_false(1, -1)
    flag.enable(EVENT.SeathDeparted)
    flag.enable(EVENT.SeathLeftTower)
    warp.set_player_respawn_point(1702900)
    network.save_request()


def event11702001():
    """ First Armored Tusk before elevator fades in and charges. """
    header(11702001, 1)
    # If player spawned inside the Archives, move the Boar to the other end.
    if_in_world_area(1, 17, 0)
    skip_if_condition_false(1, 1)
    warp.short_warp(CHR.InvisibleTusk, 'region', REGION.InvisibleTuskMove, -1)
    if_player_inside_region(-1, REGION.InvisibleTuskTrigger)
    if_entity_attacked_by(-1, CHR.InvisibleTusk, CHR.Player)
    if_condition_true(0, -1)
    anim.force_animation(CHR.InvisibleTusk, 3103)
    wait(2.0)
    chr.set_standby_animation_settings_to_default(CHR.InvisibleTusk)
    anim.force_animation(CHR.InvisibleTusk, 500, loop=True)
    wait(1.7)
    anim.force_animation(CHR.InvisibleTusk, 3008, wait_for_completion=True)


def event11702010():
    """ First Thrall appearance here, which causes it to become trapped. """
    header(11702010, 1)
    end_if_this_event_on()
    chr.disable(CHR.CapriciousThrall)
    if_event_flag_on(1, EVENT.CapriciousThrallActive)
    if_player_has_good(1, GOOD.ArchivePrisonEntranceKey)
    if_player_inside_region(1, REGION.BottomOfPrison)
    if_condition_true(0, 1)
    chr.enable(CHR.CapriciousThrall)
    flag.disable(EVENT.CapriciousThrallActive)
    flag.disable(EVENT.CapriciousThrallDead)  # Just to mimic standard "disable chunk" flag changes for NPCs.
    flag.enable(EVENT.CapriciousThrallTrapped)
    # chr.rotate_to_face_entity(CHR.CapriciousThrall, CHR.Player)  # not worth the brief opacity
    anim.force_animation(CHR.CapriciousThrall, ANIM.ThrallAmbushAttack)


def event11705372():
    """ Thrall AI is enabled, music plays, and health bar is enabled. """
    header(11705372, 1)
    if_event_flag_on(1, EVENT.CapriciousThrallTrapped)
    if_event_flag_off(1, 11705372)  # Disabled when player leaves prison.
    if_player_inside_region(-1, REGION.BottomOfPrison)
    if_player_inside_region(-1, REGION.OutsidePrisonCell)
    if_player_inside_region(-1, REGION.BottomOfExitLadder)
    if_player_inside_region(-1, REGION.AtBonfireCellDoor)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    chr.enable_ai(CHR.CapriciousThrall)
    sound.enable_map_sound(SOUND.CapriciousThrallBGM)
    boss.enable_boss_health_bar(CHR.CapriciousThrall, 2245)
    restart()


def event11705374():
    """ Disables Thrall music and health, resets Thrall, and disables 5372 when player leaves prison. """
    header(11705374, 1)
    if_event_flag_on(1, 11705372)
    if_player_inside_region(1, REGION.TopOfPrisonLadder)
    if_condition_true(0, 1)
    flag.disable(11705372)
    warp.warp(CHR.CapriciousThrall, Category.region, REGION.CapriciousThrallReset, -1)
    sound.disable_map_sound(1703802)
    boss.disable_boss_health_bar(CHR.CapriciousThrall, TEXT.CapriciousThrallName)
    restart()


def event11700910():
    """ Capricious Thrall death. """
    header(11700910, 1)

    skip_if_event_flag_off(3, EVENT.CapriciousThrallDead)
    chr.disable(CHR.CapriciousThrall)
    chr.kill(CHR.CapriciousThrall, False)
    end()

    if_entity_health_less_than_or_equal(0, CHR.CapriciousThrall, 0.0)
    wait(1.0)
    sound.play_sound_effect(CHR.CapriciousThrall, SoundType.s_sfx, 777777777)
    if_entity_dead(0, CHR.CapriciousThrall)
    boss.kill_boss(CHR.CapriciousThrallBoss)
    flag.disable(EVENT.CapriciousThrallActive)
    flag.disable(EVENT.CapriciousThrallTrapped)
    flag.enable(EVENT.CapriciousThrallDead)
    boss.disable_boss_health_bar(CHR.CapriciousThrall, TEXT.CapriciousThrallName)
    sound.disable_map_sound(1703802)


def event11702015():
    """ Crystal General aggroes and opens your cell after you kill the sleeping Serpent guard. """
    header(11702015, 1)  # Can be reset on rest in case something screws up.

    # If the cell gate has been opened, the sleeping guard despawns and the Crystal General is always aggro.
    skip_if_event_flag_off(3, 11700300)
    chr.disable(CHR.SleepingGuard)
    chr.kill(CHR.SleepingGuard, False)
    end()

    # Stop here if Crystal General is dead.
    end_if_event_flag_on(11702016)

    chr.disable_ai(CHR.CrystalGeneral)
    # Crystal General triggers when sleeping guard dies, or player gets close enough, or player aggravates him.
    if_entity_dead(-1, CHR.SleepingGuard)
    if_player_within_distance(1, CHR.CrystalGeneral, 3.0)
    if_condition_true(-1, 1)
    if_entity_attacked_by(-1, CHR.CrystalGeneral, CHR.Player)
    if_condition_true(0, -1)
    chr.enable_ai(CHR.CrystalGeneral)

    # Stop here if he was triggered by distance (no way you were inside the cell).
    end_if_condition_true_finished(1)

    # When sleeping Serpent is dead, he will open the door when close.
    if_entity_dead(2, CHR.SleepingGuard)
    if_entity_inside_area(2, CHR.CrystalGeneral, REGION.AtBonfireCellDoor)
    if_condition_true(0, 2)
    warp.short_warp(CHR.CrystalGeneral, Category.region, REGION.AtBonfireCellDoor, -1)
    anim.force_animation(1701500, 0)  # open gate
    anim.force_animation(CHR.CrystalGeneral, 7111, wait_for_completion=True)
    obj.disable_activation(1701500, -1)
    flag.enable(11700300)  # Bonfire cell gate will remain open and disabled.


def event11702016():
    """ Crystal General dies, and awards Archive Cell Keys. """
    header(11702016, 1)
    skip_if_this_event_off(3)
    chr.disable(CHR.CrystalGeneral)
    chr.kill(CHR.CrystalGeneral)
    end()

    if_entity_health_less_than_or_equal(0, CHR.CrystalGeneral, 0.0)
    item.award_item_lot(ITEMLOT.ArchiveCellKey)


def event11700546():
    """ Free Havel and help him escape to Ash Lake. """
    header(11700546)
    havel, start_flag, end_flag, new_flag = define_args('iiii')

    if_player_within_distance(1, havel, 5.0)
    if_event_flag_on(-1, EVENT.HavelFreed)
    if_event_flag_on(2, EVENT.HavelTrapped)
    if_object_activated(2, 11700313)  # Havel's cell gate.
    if_condition_true(-1, 2)
    if_condition_true(1, -1)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    chr.set_standby_animation_settings(havel, cancel_animation=7801)
    chr.set_team_type(havel, TeamType.fighting_ally)
    chr.set_nest(havel, REGION.BottomOfExitLadder)  # Havel will wait at the bottom of the ladder.
    chr.replan_ai(havel)

    if_event_flag_on(0, 11700140)  # Archive entrance open.
    chr.set_nest(havel, REGION.TopOfPrisonLadder)  # Havel will climb the ladder and walk out.
    chr.replan_ai(havel)


def event11700547():
    """ Havel goes insane if left in the prison for too long (3+ Lord Souls). """
    header(11700547)
    havel, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(-1, EVENT.HavelInsane)  # Always re-triggers this.
    if_event_flag_on(1, EVENT.HavelTrapped)  # Havel in his cell.
    if_object_activated(1, 11700313)  # Havel's cell gate opened.
    if_number_true_flags_in_range_greater_than_or_equal(-2, 711, 714, 3)
    if_number_true_flags_in_range_greater_than_or_equal(2, 711, 714, 2)
    if_event_flag_on(2, 5)  # or two Lord Souls and the Dark Remnant
    if_condition_true(-2, 2)
    if_condition_true(1, -2)
    if_condition_true(-1, 1)
    if_condition_true(0, -1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    chr.enable_ai(havel)  # Redundant, but oh well.
    chr.set_team_type_and_exit_standby_animation(havel, TeamType.hostile_ally)


def event11700548():
    """ Havel escapes to Ash Lake if he escapes the prison. """
    header(11700548)
    havel, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(1, EVENT.HavelFreed)
    if_entity_inside_area(1, CHR.Havel, REGION.TopOfPrisonLadder)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    # NOTE: I encountered an inexplicable, one-off bug where Havel would just walk on the spot into the top of the
    # ladder, rather than exiting through the door and triggering his disappearance. To counteract this, Havel will be
    # considered 'escaped' as soon as he reaches the top, because otherwise this glitch breaks his entire storyline
    # (because he will die if the map reloads). He will vanish after five seconds, regardless of where he is, after
    # reaching the top. This means that the glitch will simply cause him to vanish at the top of the ladder after
    # walking on the spot for a few seconds, rather than breaking his entire quest.

    wait(5.0)
    end_if_event_flag_off(new_flag)  # Havel's state changed again (e.g. he became hostile).
    anim.force_animation(havel, ANIM.KneelAndFadeOut, wait_for_completion=True)
    chr.disable(havel)


def event11705101():
    """ Trigger prison alarm when you emerge from your cell. Now doesn't require you have the key. """
    header(11705101)

    if_host(1)
    skip_if_client(1)
    if_event_flag_off(1, 11705101)
    if_event_flag_off(1, 11700133)
    if_player_inside_region(1, 1702100)
    if_host(2)
    if_event_flag_on(2, 11705106)
    if_host(3)
    if_event_flag_on(3, 11705107)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(0, -1)

    flag.disable(11705106)
    flag.disable(11705107)

    skip_if_event_flag_on(9, 11700002)
    skip_if_condition_false_finished(8, 1)
    skip_if_multiplayer(2)
    cutscene.play_cutscene_to_player(170010, CutsceneType.skippable, CHR.Player)
    skip(1)
    cutscene.play_cutscene_to_player(170010, CutsceneType.unskippable, CHR.Player)
    wait_frames(1)
    anim.force_animation(1701410, 0)
    flag.enable(11700002)
    flag.enable(EVENT.AlarmRinging)
    skip_if_condition_true_finished(1, 1)
    skip_if_condition_true_finished(9, 3)
    skip_if_event_flag_on(2, EVENT.AlarmRinging)
    run_event(11705108)
    restart()
    sound.enable_map_sound(1703500)
    anim.force_animation(1701400, 0)
    wait_frames(150)
    anim.force_animation(1701400, 1)
    run_event(11705108)
    restart()
    skip_if_event_flag_off(2, EVENT.AlarmRinging)
    run_event(11705108)
    restart()
    sound.disable_map_sound(1703500)
    flag.enable(11700133)
    anim.force_animation(1701400, 2)
    wait_frames(50)
    run_event(11705108)
    restart()


def event11700850():
    """ Eleven-slot event that triggers the invisible Crystal Golems in the garden based on player distance. """
    header(11700850, 1)
    golem, trigger_distance, animation = define_args('ifi')
    chr.disable(golem)
    if_player_within_distance(-1, golem, trigger_distance)
    if_entity_attacked_by(-1, golem, CHR.Player)
    if_condition_true(0, -1)
    chr.enable(golem)
    anim.force_animation(golem, animation)


def event11705200():
    """ Channeler warp control. """
    header(11705200, 1)
    for slot, black_channeler in enumerate(range(1700900, 1700904)):
        # Stops Black Phantom Channelers from ever using their teleport.
        run_event_with_slot(11705240, slot, args=(black_channeler,))

    # Warp instruction: (required_flag, channeler_id, warp_destination, next_flag) (triggers when hit)

    # Channeler in first room, ground floor.
    run_event_with_slot(11705201, 0, args=(11705200, 1700300, 1702301, 11705201))
    run_event_with_slot(11705201, 1, args=(11705201, 1700300, 1702305, 11705202))
    run_event_with_slot(11705201, 2, args=(11705202, 1700300, 1702301, 11705201))

    # Channeler in first room, upper floor.
    flag.enable(11705210)
    run_event_with_slot(11705201, 10, args=(11705210, 1700301, 1702311, 11705211))
    run_event_with_slot(11705201, 11, args=(11705211, 1700301, 1702312, 11705212))
    run_event_with_slot(11705201, 12, args=(11705212, 1700301, 1702313, 11705213))
    run_event_with_slot(11705201, 13, args=(11705213, 1700301, 1702312, 11705212))  # Only last two loop.

    # Channeler in second room, upper floor.
    flag.enable(11705220)
    run_event_with_slot(11705201, 20, args=(11705220, 1700302, 1702321, 11705221))
    run_event_with_slot(11705201, 21, args=(11705221, 1700302, 1702322, 11705220))


def event11705201():
    """ Channeler warp event. """
    header(11705201, 2)
    required_flag, channeler_id, warp_destination, next_flag = define_args('iiii')
    # end_if_this_event_slot_on()  # Warps now loop.

    if_event_flag_on(1, required_flag)
    if_has_tae_event(1, channeler_id, 1000)
    if_condition_true(0, 1)

    warp.short_warp(channeler_id, 'region', warp_destination, -1)
    flag.disable(required_flag)
    chr.set_nest(channeler_id, warp_destination)
    anim.force_animation(channeler_id, 7000, wait_for_completion=True)
    skip_if_not_equal(2, next_flag, 0)
    chr.ai_instruction(channeler_id, 1, 0)
    skip(1)
    flag.enable(next_flag)
    chr.replan_ai(channeler_id)
    restart()


def event11702050():
    """ Kill Crystal Golem beneath extending staircase before the garden to reveal the bonfire. """
    header(11702050, 1)
    skip_if_this_event_off(2)
    chr.disable(CHR.BonfireGolem)
    end()
    obj.disable(1701960)
    if_entity_health_less_than_or_equal(0, CHR.BonfireGolem, 0.0)
    wait(2.0)
    flag.enable(11702050)
    sfx.create_oneoff_sfx('object', 1701960, -1, 90014)
    obj.enable(1701960)
    map.register_bonfire(11700992, 1701960)


def event11705099():
    """ Monitor presence in Seath's tower room (if he's there) for Quella. """
    header(11705099)
    flag.disable(11705098)
    if_player_inside_region(1, 1702890)
    if_event_flag_on(1, 11705386)
    if_condition_true(0, 1)
    flag.enable(11705098)
    if_player_outside_area(0, 1702890)
    restart()


def event11700200():
    """ Staircases rotate when flags activated (in 5150). Now, if both Channelers are alive, they rotate continuously
    until the Channelers are killed. """
    header(11700200)
    is_rotated, staircase, barrier, hitbox_1, hitbox_2, navimesh_1, navimesh_2, trigger = define_args('iiiiiiii')

    # Initial position.
    obj.disable(barrier)
    skip_if_event_flag_on(5, is_rotated)
    anim.end_animation(staircase, 3)
    hitbox.disable_hitbox(hitbox_2)
    navimesh.delete_navimesh_collision_bitflags(navimesh_1, 1)
    navimesh.add_navimesh_collision_bitflags(navimesh_2, 1)
    skip(4)
    anim.end_animation(staircase, 1)
    hitbox.disable_hitbox(hitbox_1)
    navimesh.add_navimesh_collision_bitflags(navimesh_1, 1)
    navimesh.delete_navimesh_collision_bitflags(navimesh_2, 1)

    if_event_flag_on(0, trigger)

    skip_if_event_flag_on(12, is_rotated)
    anim.force_animation(staircase, 1)
    hitbox.disable_hitbox(hitbox_1)
    obj.enable(barrier)
    navimesh.add_navimesh_collision_bitflags(navimesh_1, 1)
    anim.force_animation(barrier, 1)
    wait_frames(180)
    obj.disable(barrier)
    hitbox.enable_hitbox(hitbox_2)
    flag.enable(is_rotated)
    skip_if_event_flag_off(1, 11705153)  # Trigger only disabled if both Channelers are dead.
    flag.disable(trigger)
    restart()

    anim.force_animation(staircase, 3)
    hitbox.disable_hitbox(hitbox_2)
    obj.enable(barrier)
    navimesh.add_navimesh_collision_bitflags(navimesh_2, 1)
    anim.force_animation(barrier, 3)
    wait_frames(180)
    obj.disable(barrier)
    hitbox.enable_hitbox(hitbox_1)
    flag.disable(is_rotated)
    skip_if_event_flag_off(1, 11705153)  # Trigger only disabled if both Channelers are dead.
    flag.disable(trigger)
    restart()


def event11705153():
    """ Marks when both upper Channelers are dead, which stops endless staircase rotation. """
    header(11705153, 1)
    if_entity_health_less_than_or_equal(1, 1700301, 0.0)
    if_entity_health_less_than_or_equal(1, 1700302, 0.0)
    if_condition_true(0, 1)
    item.award_item_to_host_only(ITEMLOT.ArchiveGiantCellKey)
    end()


def event11700538():
    """ Triggers Sieglinde's golden golem and two others at once. """
    header(11700538, 1)
    sieglinde, start_flag, end_flag, new_flag = define_args('iiii')
    golems = (1700500, 1700686, 1700687)
    for golem in golems:
        chr.disable(golem)
    if_event_flag_off(1, 1547)
    if_event_flag_on(1, 1540)
    if_event_flag_off(1, 1512)
    if_event_flag_off(1, 1513)
    if_event_flag_range_not_all_off(1, 1501, 1511)  # Siegmeyer's story is somewhere appropriate.
    if_entity_alive(1, sieglinde)
    if_event_flag_on(2, 1541)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    # Wait for player to get close to one of the golems.
    for golem in golems:
        if_player_within_distance(-2, golem, 3.0)
    if_condition_true(0, -2)
    for golem in golems:
        chr.enable(golem)
        anim.force_animation(golem, 3104)
    chr.set_display_mask(1700500, 1, 1)


def event11705385():
    """ Controls appearance of Seath's tower room. Now enables Mimic. """
    header(11705385, 1)
    chr.enable_immortality(CHR.SeathInTower)
    chr.set_special_effect(CHR.SeathInTower, 5441)
    chr.set_special_effect(CHR.SeathInTower, 5442)
    chr.set_special_effect(CHR.SeathInTower, 5443)
    skip_if_event_flag_on(3, EVENT.SeathLeftTower)
    chr.disable(1700401)
    if_event_flag_on(0, EVENT.SeathLeftTower)
    end_if_event_flag_on(EVENT.SeathDeparted)
    chr.enable(1700401)
    chr.disable(CHR.SeathInTower)
    obj.disable(1701050)
    obj.disable(1701890)
    sfx.delete_map_sfx(1701891)


def event11702003():
    """ Kill one Moonlight Butterfly with the Pale Eye Orb. """
    header(11702003)
    end_if_event_flag_on(EVENT.EmpyreanWitness)

    if_player_has_good(1, GOOD.PaleEyeOrb)
    if_entity_dead(-1, 1700350)
    if_entity_dead(-1, 1700351)
    if_entity_dead(-1, 1700352)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    flag.enable(EVENT.EmpyreanWitness)
    message.status_explanation(TEXT.PaleEyeOrbQuivers)


def event11700900():
    """ Mimic dies and doesn't respawn. Now drops mandatory treasure. """
    header(11700900, 1)
    mimic, = define_args('i')
    skip_if_this_event_slot_off(3)
    chr.disable(mimic)
    chr.drop_mandatory_treasure(mimic)
    end()

    if_entity_dead(0, mimic)
    end()


def event11702044():
    """ Monitor resting at main Archives bonfire. """
    header(11702044)
    if_player_within_distance(1, 1701960, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11702044)


def event11700532():
    """ Logan moves to library when he is freed (or frees himself when you get Seath's soul shard). """
    header(11700532)
    logan, first_flag, last_flag, new_flag = define_args('iiii')

    # Condition 1: The player has freed Logan and left the prison tower.
    if_event_flag_off(1, 1096)  # Not hostile.
    if_event_flag_on(1, 1094)  # Logan freed.
    if_host(1)
    if_player_outside_area(1, 1702410)  # Player not in prison tower.

    # Condition 2: Logan is imprisoned and the player has Seath's Lord Soul shard.
    if_event_flag_off(2, 1096)  # Not hostile.
    if_event_flag_on(2, 1093)  # Logan in prison.
    if_event_flag_on(2, 714)  # Player has Seath's Lord Soul shard.

    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    # Logan moves to the Library.
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    flag.enable(11700594)
    chr.enable(logan)
    warp.warp_and_set_floor(logan, Category.region, 1702501, -1, 1703300)
    if_entity_backread_enabled(0, logan)
    chr.set_nest(logan, 1702501)


def event11700533():
    """ Logan goes insane. """
    header(11700533)
    logan, first_flag, last_flag, new_flag, logan_hollow = define_args('iiiii')

    # The chest containing Logan's gear (except his hat) is disabled until you reload after he goes insane.
    skip_if_event_flag_on(2, 11700595)
    obj.disable(1701664)  # Logan's chest.
    obj.disable_activation(1701664, -1)

    # Condition 1: Player has Seath's Lord Soul and Logan is fully sold out (and has been spoken to).
    if_event_flag_off(1, 1096)  # Not hostile.
    if_this_event_off(1)  # He hasn't gone insane yet.
    if_event_flag_on(1, 1095)  # Logan in library.
    if_event_flag_on(1, 714)  # Player has Seath's soul shard (either by killing him or picking it up).
    if_event_flag_on(1, 728)  # Logan fully sold out.
    if_event_flag_on(1, 11700592)  # Presumably Logan's "going insane" dialogue.

    # Condition 2: Logan has already gone insane (i.e. this event has previously finished).
    if_event_flag_off(2, 1096)
    if_event_flag_on(2, 1095)  # Logan in library.
    if_this_event_on(2)  # He's already gone insane.

    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    end_if_condition_true_finished(1)  # Wait until next map load for Logan to disappear (via condition 2).

    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.disable(logan)
    chr.enable(logan_hollow)
    flag.enable(11700595)
    obj.enable(1701664)
    obj.enable_activation(1701664, -1)


def event11700001():
    """ Seath dies (in Cave battle). Now disables Departed flag, which may be enabled when flag starts. """
    header(11700001)
    obj.disable(1701950)
    if_entity_dead(0, CHR.Seath)

    skip_if_event_flag_off(1, EVENT.SeathDeparted)
    flag.enable(1911)  # For Seath punishment.

    flag.disable(EVENT.SeathDeparted)
    flag.enable(EVENT.SeathDead)
    boss.kill_boss(CHR.Seath)
    skip_if_client(1)
    game.award_achievement(38)
    obj.disable(1701990)
    sfx.delete_map_sfx(1701991, True)
    sfx.create_oneoff_sfx(Category.object, 1701950, -1, sfx_id=90014)
    wait(2.0)
    obj.enable(1701950)
    map.register_bonfire(11700920, 1701950, 2.0, 180.0, 0)


def event11700820():
    """ Enemy doesn't respawn and drops mandatory loot. """
    header(11700820, 1)
    npc, = define_args('i')
    skip_if_this_event_slot_off(2)
    chr.drop_mandatory_treasure(npc)
    end()

    if_entity_dead(0, npc)
    end()


def event11702004():
    """ Jeremiah's loot appears at the top of the tower if Seath is gone and Jeremiah has 'vanished'. """
    header(11702004, 1)
    if_event_flag_on(1, EVENT.JeremiahEscaped)
    if_event_flag_on(1, EVENT.SeathLeftTower)
    if_condition_true(0, 1)
    chr.drop_mandatory_treasure(CHR.JeremiahLoot)


def event11700300():
    """ Open a prison gate. Now cannot be closed. """
    header(11700300)
    objact_event_flag, open_message, door_id = define_args('iii')

    end_if_client()
    skip_if_this_event_slot_off(6)
    anim.end_animation(door_id, 0)  # open gate
    for idx in range(4):
        obj.deactivate_object_with_idx(door_id, -1, idx)
    end()

    if_object_activated(0, objact_event_flag)
    flag.enable(objact_event_flag)
    message.dialog(open_message, ButtonType.yes_no, NumberButtons.no_button, door_id, 3.0)
    for idx in range(4):
        obj.deactivate_object_with_idx(door_id, -1, idx)


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
