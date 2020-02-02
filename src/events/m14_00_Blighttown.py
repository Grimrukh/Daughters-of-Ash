
import sys
import inspect
from pydses import *

map_name = 'm14_00_00_00'  # Blighttown / Quelaag's Domain
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11400000
BASE_PART = 1400000


class DEBUG(IntEnum):
    PARISH_BELL_RUNG = False
    LOST_IZALITH_OPENED = False
    GET_SEROUS_BOND = False
    DARK_ANOR_LONDO = False
    GET_XANTHOUS_CROWN = False
    QUELAAG_DEAD = False


class CHR(IntEnum):
    Player = 10000
    FairLady = 1400700
    FairLadyBug = 1400701
    Eingyi = 6160
    Quelana = 6170
    ManeaterMildredInvader = 6530
    ManeaterMildredSummon = 6531
    LostDaughter = 6622
    SellswordTishana = 6860
    Quelaag = 1400800
    QuelaagHeart = 1400801
    DeadJeremiah_FairLady = 1400875
    DeadJeremiah_Swamp = 1400876
    DeadJeremiah_Quelaag = 1400886
    Butcher = 1400880
    ButcherDog1 = 1400881
    ButcherDog2 = 1400882
    Laurentius = 6130
    LaurentiusHollow = 6132
    SiegmeyerAtDepthsGate = 6280
    Siegmeyer = 6282
    Shiva = 6311
    ShivaBodyguard = 6421
    BonfireBarbarian = 1400885


SwampDemons = (1400877, 1400878, 1400879)


class SPEFFECT(IntEnum):
    XanthousCrown = 6640  # effect granted by cursed Xanthous Crown


class EVENT(IntEnum):
    QuelaagDead = 9
    QuelaagHeartDead = 11402010
    NitoDead = 7
    ParishBellRung = 11010700
    NitoAwake = 11310000
    BlighttownNitoCutsceneWarp = 11402004
    LostDaughterWithFairLady = 11412024
    LostDaughterHostile = 11412025   # attacked by player near Fair Lady
    LostDaughterDead = 11412026   # killed by player
    JeremiahDeadNearFairLady = 11412056  # Jeremiah is killed by the Lost Daughter and the Spark can be looted nearby.
    JeremiahDeadNearQuelana = 11412057  # Jeremiah is killed by Quelana and the Spark can be looted near her.
    JeremiahDeadInQuelaagArena = 11412058  # Jeremiah is killed by Dark Quelaag and the Spark can be looted near her.
    LostIzalithDoorOpened = 11410340
    DarkAnorLondo = 11510400


class ITEMLOT(IntEnum):
    QuelaagHeartReward = 2940
    XanthousCrown = 6770


class OBJ(IntEnum):
    ButcherPot = 1401875
    LaurentiusPot = 1001250  # copied from Depths


class REGION(IntEnum):
    SellswordTishanaTrigger = 1402875
    SellswordTishanaSignPoint = 1402876
    QuelaagHeartTrigger = 1402877


class TEXT(IntEnum):
    QuelaagHeart = 5285
    NothingHappened = 10010633


def event0():
    header(0, 0)

    if DEBUG.PARISH_BELL_RUNG:
        flag.enable(EVENT.ParishBellRung)
    if DEBUG.LOST_IZALITH_OPENED:
        flag.enable(11410340)
    if DEBUG.GET_SEROUS_BOND:
        item.award_item_to_host_only(4910)
    if DEBUG.DARK_ANOR_LONDO:
        flag.enable(EVENT.DarkAnorLondo)
    if DEBUG.GET_XANTHOUS_CROWN:
        item.award_item_to_host_only(ITEMLOT.XanthousCrown)
    if DEBUG.QUELAAG_DEAD:
        flag.enable(EVENT.QuelaagDead)

    # Switch light map if Anor Londo is dark. (Both maps also have dimmer lava.)
    skip_if_event_flag_off(1, EVENT.DarkAnorLondo)
    light.set_area_texture_parambank_slot_index(14, 1)

    map.register_bonfire(11400992, 1401960, initial_kindle_level=10)  # Fair Lady
    run_event(11402044)  # (New) Monitors resting at Fair Lady bonfire for warping.
    map.register_bonfire(11400984, 1401961)  # Swamp
    run_event(11402040)  # (New) Monitors resting at swamp bonfire for warping.
    skip_if_event_flag_off(1, 11402009)
    map.register_bonfire(11400976, 1401962)  # Rampart

    # Thirty-one ladders.
    for ladder_id, ladder_flag_1, ladder_flag_2 in zip(range(40, 71), range(10, 71, 2), range(11, 72, 2)):
        map.register_ladder(BASE_FLAG + ladder_flag_1, BASE_FLAG + ladder_flag_2, 1401100 + ladder_id)

    # Summon fog.
    skip_if_client(6)
    for fog in (1401994, 1401996, 1401998):
        obj.disable(fog)
        sfx.delete_map_sfx(fog + 1, False)

    # Kirk's corpse, once all three invasions are won.
    if_event_flag_on(1, 11000810)
    if_event_flag_on(1, 11410810)
    if_event_flag_on(1, 11410811)
    skip_if_condition_true(2, 1)
    obj.disable(1401601)
    skip(1)
    obj.enable_treasure(1401601)

    # Fog checkpoint, now on your way *up* through the shanty town.
    run_event_with_slot(11400090, 1, args=(1401702, 1401703, 1402603, 1402602))

    # Gravelord.
    run_event(11405090)
    run_event(11405091)
    run_event(11405092)

    run_event(11400900)  # Parasitic Wall Hugger.
    run_event(11402000)  # (NEW) Jeremiah dies and drops the Spark.
    run_event(11402001)  # (NEW) Talk to Lost Daughter (and get no response) if she is there.
    run_event(11402002)  # (NEW) Xanthous Crown makes Fair Lady appear as a Chaos Bug.
    run_event(11402003)  # (NEW) Award achievement and Homeward Bone after Nito awakening cutscene when bell is rung.
    run_event(11402009)  # (NEW) Kill Barbarian on rampart to spawn bonfire.
    run_event(11400800)  # Fair Lady's death.
    run_event(11405000)  # Gives Fair Lady a special effect when her health falls below 100%.
    run_event(11400200)  # Ring Bell of Awakening.
    run_event(11400210)  # Illusory wall to Fair Lady.
    run_event(11400220)  # Receive special effect 4140 near CHR.Quelana.
    run_event(11400230)  # Door to the Depths is locked if not opened (or open it again, if opened).
    run_event(140)  # Fair Lady is dead and her bonfire is extinguished.
    run_event(11402008)  # (New) Butcher near Laurentius stops chopping.

    # CHAOS WITCH QUELAAG

    sound.disable_map_sound(1403800)
    skip_if_event_flag_off(6, 9)
    run_event(11405392)
    obj.disable(1401990)
    sfx.delete_map_sfx(1401991, False)
    obj.disable(1401992)
    sfx.delete_map_sfx(1401993, False)
    skip(7)
    for quelaag_event in (5390, 5391, 5393, 5392, 1, 5394, 5395):
        run_event(BASE_FLAG + quelaag_event)

    # QUELAAG, HEART OF CHAOS

    run_event(11405492)  # Trigger.
    run_event(11402010)  # Death.

    # Squeaky floor boards (short and long).
    run_event_with_slot(11405100, 0, args=(1401000, 1402000, 1402001, 1402002))
    run_event_with_slot(11405110, 0, args=(1401002, 1402020, 1402021, 1402022, 1402023, 1402024))

    # Spawn Vile Maggots from Egg Bearers.
    run_event_with_slot(11405350, 0, args=(CHR.Eingyi, 1400411, 1400412, 1400413, 1400414, 1400415, 1))
    run_event_with_slot(11405350, 3, args=(1400402, 1400426, 1400427, 1400428, 1400429, 1400430, 0))
    run_event_with_slot(11405350, 4, args=(1400403, 1400431, 1400432, 1400433, 1400434, 1400435, 0))

    # Mosquito spawners.
    run_event_with_slot(11400100, 0, args=(11405340, 1402200, 1403000))
    run_event_with_slot(11400100, 1, args=(11405341, 1402201, 1403001))
    run_event_with_slot(11400100, 2, args=(11405342, 1402202, 1403002))

    # One Infested Ghoul trapped in an urn.
    run_event_with_slot(11405200, 0, args=(1400450, 1401300))

    # Boulder parts of Barbarians, which take no damage (now two extra).
    for slot, barbarian_id in enumerate(range(1400100, 1400107)):
        run_event_with_slot(11405250, slot, args=(barbarian_id,))

    # Non-respawning enemies (all Blowdart Snipers).
    for slot, blowdart_id in enumerate(range(1400200, 1400209)):
        run_event_with_slot(11400850, slot, args=(blowdart_id, 25300200))

    # (New) Demons appear (once) if Lost Izalith is opened.
    for slot, demon in enumerate(SwampDemons):
        run_event_with_slot(11402005, slot, args=(demon,))

    # Three chests.
    for slot, (chest_id, chest_flag) in enumerate(zip(range(1401650, 1401653), range(11400600, 11400603))):
        run_event_with_slot(11400600, slot, args=(chest_id, chest_flag))


def event50():
    """ NPC constructor. """
    header(50, 0)

    # (NEW) SELLSWORD TISHANA (invasion)

    # NOTE: no humanity registration.
    run_event(11405630)
    run_event(11400810)

    # MANEATER MILDRED (invasion and summon)

    chr.humanity_registration(6531, 8940)
    chr.humanity_registration(6530, 8940)
    run_event(11405030)
    run_event(11405032)  #
    run_event(11405035)
    run_event(11400901)

    # LAURENTIUS (trapped - still uses Depths flags and urn ID)

    chr.humanity_registration(CHR.Laurentius, 8390)
    skip_if_client(1)
    flag.disable(11000580)
    skip_if_event_flag_on(3, 11000580)
    skip_if_event_flag_on(2, 1250)
    skip_if_event_flag_on(1, 1253)
    chr.disable(CHR.Laurentius)
    skip_if_event_flag_off(2, 1250)
    chr.disable_gravity(CHR.Laurentius)
    chr.disable_collision(CHR.Laurentius)
    # Free Laurentius from the urn. He will fight the dogs and Butcher if they are alive.
    run_event_with_slot(11000530, args=(CHR.Laurentius, 1250, 1255, 1251))
    # Disable Laurentius if 1253 is off and 1252 is on.
    run_event_with_slot(11000531, args=(CHR.Laurentius,))
    run_event_with_slot(11400510, 3, args=(CHR.Laurentius, 1253))  # Hostile.
    run_event_with_slot(11400520, 3, args=(CHR.Laurentius, 1250, 1255, 1254))  # Dead.
    # Make Laurentius invincible while he's in the urn.
    run_event_with_slot(11000534, args=(CHR.Laurentius,))

    # LAURENTIUS (Hollow)

    skip_if_event_flag_on(1, 1257)
    chr.disable(CHR.LaurentiusHollow)
    chr.set_team_type_and_exit_standby_animation(CHR.LaurentiusHollow, TeamType.hostile_ally)
    run_event_with_slot(11400520, 0, args=(CHR.LaurentiusHollow, 1250, 1259, 1254))
    run_event_with_slot(11400530, 0, args=(CHR.LaurentiusHollow, 1250, 1259, 1257))

    # FAIR LADY

    skip_if_event_flag_range_not_all_off(1, 1270, 1279)
    flag.enable(1270)
    run_event_with_slot(11400520, 1, args=(CHR.FairLady, 1270, 1279, 1272))

    # EINGYI

    skip_if_event_flag_on(2, 1280)
    chr.set_nest(CHR.Eingyi, 1402300)
    warp.short_warp(CHR.Eingyi, Category.region, 1402300, -1)
    run_event_with_slot(11400520, 2, args=(CHR.Eingyi, 1280, 1289, 1284))
    run_event_with_slot(11400531, args=(CHR.Eingyi, 1280, 1289, 1281))
    run_event_with_slot(11400532, args=(CHR.Eingyi, 1280, 1289, 1286))
    run_event_with_slot(11400501, args=(CHR.Eingyi, 1282))
    run_event_with_slot(11400502, args=(CHR.Eingyi, 1283))
    run_event_with_slot(11400503, args=(CHR.Eingyi, 1287))
    run_event(11400533)

    # QUELANA OF IZALITH

    chr.humanity_registration(CHR.Quelana, 8398)
    skip_if_event_flag_on(2, 1296)
    skip_if_event_flag_on(1, 1290)
    skip(1)
    chr.disable(CHR.Quelana)
    run_event_with_slot(11400510, 3, args=(CHR.Quelana, 1294))
    run_event_with_slot(11400520, 3, args=(CHR.Quelana, 1290, 1309, 1295))
    run_event_with_slot(11400536, args=(CHR.Quelana, 1290, 1309, 1291))
    run_event_with_slot(11400537, args=(CHR.Quelana, 1290, 1309, 1292))
    run_event_with_slot(11400538, args=(CHR.Quelana, 1290, 1309, 1293))
    run_event_with_slot(11400539, args=(CHR.Quelana, 1290, 1309, 1296))

    # SIEGMEYER (in swamp - requires different talk ID)

    chr.humanity_registration(CHR.Siegmeyer, 8446)
    skip_if_event_flag_on(3, 1512)
    skip_if_event_flag_on(2, 1502)
    skip_if_event_flag_on(1, 1501)
    chr.disable(CHR.Siegmeyer)
    run_event_with_slot(11400510, 4, args=(CHR.Siegmeyer, 1512))
    run_event_with_slot(11400520, 4, args=(CHR.Siegmeyer, 1490, 1514, 1513))
    run_event_with_slot(11400551, args=(CHR.Siegmeyer, 1490, 1514, 1501))
    run_event_with_slot(11400552, args=(CHR.Siegmeyer, 1490, 1514, 1502))
    run_event(11400553)
    run_event_with_slot(11400554, args=(CHR.Siegmeyer,))

    # SIEGMEYER (near Depths gate - different talk ID)

    chr.humanity_registration(CHR.SiegmeyerAtDepthsGate, 8446)
    # If you open the gate, you will next see him in Anor Londo (not Sen's Fortress).
    skip_if_event_flag_on(1, 1490)
    chr.disable(CHR.SiegmeyerAtDepthsGate)
    run_event_with_slot(11400510, 7, args=(CHR.SiegmeyerAtDepthsGate, 1512))  # Hostile.
    run_event_with_slot(11400520, 7, args=(CHR.SiegmeyerAtDepthsGate, 1490, 1514, 1513))  # Dead.
    run_event_with_slot(11400555, args=(CHR.SiegmeyerAtDepthsGate, 1490, 1514, 1493))

    # SHIVA and his bodyguard

    chr.humanity_registration(CHR.Shiva, 8470)
    chr.humanity_registration(CHR.ShivaBodyguard, 8900)
    skip_if_client(1)
    flag.disable(11405022)
    skip_if_event_flag_on(8, 11405022)
    if_host(1)
    if_player_covenant(1, 'forest hunter')
    if_event_flag_on(1, 1601)
    skip_if_condition_true(2, 1)
    chr.disable(CHR.Shiva)
    chr.disable(CHR.ShivaBodyguard)
    run_event_with_slot(11400520, 5, args=(CHR.Shiva, 1600, 1619, 1604))  # Dead
    run_event_with_slot(11400520, 6, args=(CHR.ShivaBodyguard, 1760, 1769, 1764))  # Dead
    run_event_with_slot(11400504, args=(CHR.Shiva, 1603, CHR.ShivaBodyguard))  # Hostile (both at once)
    # Shiva and his bodyguard move to Blighttown from Darkroot Garden.
    run_event_with_slot(11400560, args=(CHR.Shiva, 1600, 1619, 1601, CHR.ShivaBodyguard))
    # Shiva and his bodyguard return to Darkroot if you attack them and they kill you.
    run_event_with_slot(11400566, args=(CHR.Shiva, CHR.ShivaBodyguard))
    # Shiva and his bodyguard don't appear if you're not a Forest Hunter.
    run_event_with_slot(11400567, args=(CHR.Shiva, CHR.ShivaBodyguard))
    skip_if_condition_false(2, 1)
    wait_frames(1)
    flag.enable(11405022)
    flag.disable(1766)

    # (NEW) LOST DAUGHTER OF IZALITH

    # NOTE: no humanity registration.
    skip_if_event_flag_on(2, EVENT.LostDaughterWithFairLady)
    skip_if_event_flag_on(1, EVENT.LostDaughterHostile)
    chr.disable(CHR.LostDaughter)
    run_event_with_slot(11402210, args=(CHR.LostDaughter, EVENT.LostDaughterHostile))
    run_event_with_slot(11402211, args=(CHR.LostDaughter, 11412020, 11412029, EVENT.LostDaughterDead))


def event11400555():
    """ Siegmeyer advances to Anor Londo if you open Blighttown gate (after next de-load). """
    header(11400555)
    npc, first_flag, last_flag, new_flag = define_args('iiii')
    if_host(1)
    if_event_flag_off(1, 1512)
    if_event_flag_on(1, 1490)
    if_event_flag_on(1, 11000110)  # Depths door open.
    if_entity_backread_disabled(1, npc)
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)


def event11400800():
    """ Fair Lady's death. Now makes Lost Daughter aggravated as well. """
    header(11400800, 1)
    skip_if_this_event_off(7)
    chr.disable(CHR.FairLady)
    chr.disable(CHR.FairLadyBug)
    sound.disable_map_sound(1403801)
    hitbox.disable_hitbox(1403100)
    hitbox.disable_hitbox(1403101)
    chr.set_team_type(CHR.LostDaughter, TeamType.hostile_ally)
    end()

    if_entity_dead(-1, CHR.FairLady)
    if_entity_health_less_than_or_equal(7, CHR.FairLadyBug, 0.1)
    if_condition_true(-1, 7)
    if_condition_true(0, -1)
    skip_if_condition_false_finished(3, 7)
    chr.disable(CHR.FairLadyBug)
    chr.enable(CHR.FairLady)
    chr.kill(CHR.FairLady, True)
    flag.enable(140)
    sound.disable_map_sound(1403801)
    hitbox.disable_hitbox(1403100)
    hitbox.disable_hitbox(1403101)
    chr.set_team_type(CHR.LostDaughter, TeamType.hostile_ally)
    if_character_human(-2, CHR.Player)
    if_character_hollow(-2, CHR.Player)
    if_condition_true(1, -2)
    if_player_covenant(1, 'chaos servant')
    end_if_condition_false(1)
    game.betray_current_covenant()
    network.increment_player_pvp_sin()
    flag.enable(742)
    network.save_request()


def event11402000():
    """ Jeremiah dies (drops Spark) near Lost Daughter or Quelana. """
    header(11402000, 0)
    chr.disable(CHR.DeadJeremiah_FairLady)
    chr.disable(CHR.DeadJeremiah_Swamp)
    chr.disable(CHR.DeadJeremiah_Quelaag)
    if_event_flag_on(-1, EVENT.JeremiahDeadNearFairLady)
    if_event_flag_on(-1, EVENT.JeremiahDeadNearQuelana)
    if_event_flag_on(-1, EVENT.JeremiahDeadInQuelaagArena)
    if_condition_true(0, -1)

    skip_if_event_flag_off(3, EVENT.JeremiahDeadNearFairLady)
    chr.enable(CHR.DeadJeremiah_FairLady)
    chr.drop_mandatory_treasure(CHR.DeadJeremiah_FairLady)
    end()

    skip_if_event_flag_off(3, EVENT.JeremiahDeadInQuelaagArena)
    chr.enable(CHR.DeadJeremiah_Quelaag)
    chr.drop_mandatory_treasure(CHR.DeadJeremiah_Quelaag)
    end()

    chr.enable(CHR.DeadJeremiah_Swamp)
    chr.drop_mandatory_treasure(CHR.DeadJeremiah_Swamp)


def event11402210():
    """ Lost Daughter becomes hostile. """
    header(11402210, 1)
    lost_daughter, hostile_flag = define_args('ii')

    if_event_flag_on(-1, EVENT.LostDaughterHostile)
    if_event_flag_on(1, EVENT.LostDaughterWithFairLady)
    if_entity_attacked_by(1, lost_daughter, CHR.Player)
    if_entity_health_less_than_or_equal(1, lost_daughter, 0.9)
    if_condition_true(-1, 1)
    if_event_flag_on(-1, 140)
    if_condition_true(0, -1)

    flag.enable(hostile_flag)

    chr.set_team_type(lost_daughter, TeamType.hostile_ally)


def event11402211():
    """ Lost Daughter dies. """
    header(11402211, 1)
    lost_daughter, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(-1, EVENT.LostDaughterDead)
    if_event_flag_on(-2, EVENT.LostDaughterHostile)
    if_event_flag_on(-2, EVENT.LostDaughterWithFairLady)
    if_condition_true(1, -2)
    if_entity_dead(1, lost_daughter)
    if_condition_true(-1, 1)
    if_condition_true(0, -1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    chr.disable(lost_daughter)


def event11402002():
    """ Wearing the Xanthous Crown makes the Fair Lady appear as a Chaos Bug. """
    header(11402002, 1)
    end_if_event_flag_on(140)
    chr.enable_immortality(CHR.FairLadyBug)
    chr.disable(CHR.FairLadyBug)
    if_event_flag_off(1, 140)
    if_entity_has_special_effect(1, CHR.Player, SPEFFECT.XanthousCrown)
    if_condition_true(0, 1)
    chr.disable(CHR.FairLady)
    chr.enable(CHR.FairLadyBug)
    if_event_flag_off(2, 140)
    if_entity_does_not_have_special_effect(2, CHR.Player, SPEFFECT.XanthousCrown)
    if_condition_true(0, 2)
    chr.disable(CHR.FairLadyBug)
    chr.enable(CHR.FairLady)
    restart()


def event11400200():
    """ Ring the Bell of Awakening, which may now trigger Nito cutscene. """
    header(11400200, 0)
    skip_if_this_event_off(2)
    obj.disable_activation(1401110, -1)
    end()
    if_object_activated(0, 11400201)
    if_entity_health_greater_than(0, CHR.Player, 0.0)
    flag.enable(11400200)

    # Disable Quelaag and Fair Lady for cutscene.
    chr.disable_backread(CHR.Quelaag)
    chr.disable_backread(CHR.FairLady)
    wait_frames(1)
    cutscene.play_cutscene_to_player(140010, CutsceneType.skippable, CHR.Player)
    wait_frames(1)

    # Parish bell not yet rung. Re-enable Quelaag (if alive somehow) and Fair Lady, award achievement and Bone.
    skip_if_event_flag_on(6, EVENT.ParishBellRung)
    skip_if_event_flag_on(1, EVENT.QuelaagDead)
    chr.enable_backread(CHR.Quelaag)
    chr.enable_backread(CHR.FairLady)
    game.award_achievement(30)
    item.award_item_to_host_only(9030)  # Homeward Bone
    end()

    # Otherwise, if Nito dead, display 'Nothing happened' and award achievement.
    skip_if_event_flag_off(3, EVENT.NitoDead)
    message.dialog(TEXT.NothingHappened, ButtonType.ok_cancel, NumberButtons.no_button, CHR.Player, 5.0)
    game.award_achievement(30)
    end()

    # Otherwise, warp to Tomb for Nito awakening cutscene. Achievement and Bone awarded on return.
    flag.enable(EVENT.NitoAwake)
    flag.enable(EVENT.BlighttownNitoCutsceneWarp)
    warp.warp_player(13, 1, 1310990)


def event11402003():
    """ Award achievement and Homeward Bone after Nito awakening cutscene. """
    header(11402003, 0)
    if_event_flag_on(0, EVENT.BlighttownNitoCutsceneWarp)
    flag.disable(EVENT.BlighttownNitoCutsceneWarp)
    network.save_request()
    wait(2.0)
    game.award_achievement(30)
    item.award_item_to_host_only(9030)  # Homeward Bone


def event11000530():
    """ Free Laurentius from the urn. He will fight the dogs and Butcher. """
    header(11000530, 0)
    laurentius, start_flag, end_flag, new_flag = define_args('iiii')

    skip_if_event_flag_on(9, 11000580)
    if_event_flag_off(1, 1253)  # Not hostile.
    if_event_flag_on(1, 1250)  # Stuck in pot.
    if_entity_health_greater_than(1, laurentius, 0.0)
    if_object_destroyed(-1, OBJ.LaurentiusPot)
    if_entity_attacked_by(-1, laurentius, CHR.Player)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    # Laurentius has been freed.
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    flag.enable(11000580)  # Laurentius has been freed (shouldn't come up, as he moves on).

    obj.destroy(1001250, 1)  # Destroy urn.
    chr.enable_gravity(laurentius)
    chr.enable_collision(laurentius)
    chr.set_standby_animation_settings(0, cancel_animation=7821)
    chr.disable_invincibility(laurentius)


def event11000531():
    """ Laurentius leaves. """
    header(11000531)
    laurentius, = define_args('i')
    if_event_flag_off(1, 1253)
    if_event_flag_on(1, 1252)
    if_condition_true(0, 1)
    chr.disable(laurentius)


def event1100534():
    """ Laurentius is invincible inside the urn. """
    header(11000534)
    laurentius, = define_args('i')
    if_event_flag_on(1, 1250)
    if_event_flag_off(1, 1253)
    if_condition_true(0, 1)
    chr.enable_invincibility(laurentius)
    if_object_destroyed(0, 1001250)
    network.disable_sync()
    wait(2.0)
    chr.disable_invincibility(laurentius)


def event11402005():
    """ Capra Demons and an Asylum Demon spawn once after Lost Izalith is opened. Uses 11402006 and 11402007. """
    header(11402005, 1)
    demon, = define_args('i')

    chr.disable(demon)
    skip_if_this_event_slot_off(2)
    chr.kill(demon, False)
    end()

    if_event_flag_on(0, EVENT.LostIzalithDoorOpened)
    chr.enable(demon)
    if_entity_health_less_than_or_equal(0, demon, 0.0)
    end()


def event11402008():
    """ Butcher stops chopping into the pot. """
    header(11402008, 1)
    if_player_within_distance(-1, CHR.Butcher, 10.0)
    if_entity_attacked_by(-1, CHR.Butcher, CHR.Player)
    if_object_destroyed(-1, OBJ.ButcherPot)
    if_ai_state(-1, CHR.Butcher, AIStatusType.battle)
    if_condition_true(0, -1)
    chr.set_standby_animation_settings(CHR.Butcher, cancel_animation=9060)


def event11402009():
    """ Kill Barbarian on rampart and spawn bonfire. """
    header(11402009, 1)
    skip_if_this_event_off(2)
    chr.disable(CHR.BonfireBarbarian)
    end()
    obj.disable(1401962)
    if_entity_health_less_than_or_equal(0, CHR.BonfireBarbarian, 0.0)
    flag.enable(11402009)
    sfx.create_oneoff_sfx('object', 1401962, -1, 90014)
    wait(2.0)
    obj.enable(1401962)
    map.register_bonfire(11400976, 1401962)


def event11405630():
    """ New NPC invasion: Sellsword Tishana. """
    header(11405630)
    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11405631)
    # No longer requires Quelaag to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 11400810)
    skip_if_this_event_on(1)
    if_player_inside_region(1, REGION.SellswordTishanaTrigger)
    if_condition_true(0, 1)
    message.place_summon_sign(
        SummonSignType.black_eye_sign, 6860, REGION.SellswordTishanaSignPoint, 11405631, 11405632)
    wait(20.0)
    restart()


def event11400810():
    """ Sellsword Tishana invader dies. """
    header(11400810)
    skip_if_host(3)
    if_event_flag_on(1, 11405631)
    if_event_flag_off(1, 11405632)
    skip_if_condition_true(1, 1)
    chr.disable(CHR.SellswordTishana)
    end_if_this_event_on()
    if_entity_dead(0, CHR.SellswordTishana)
    flag.enable(11400810)


def event11402001():
    """ Talk to Lost Daughter. """
    header(11402001)

    if_event_flag_on(1, EVENT.LostDaughterWithFairLady)
    if_entity_backread_enabled(1, CHR.LostDaughter)  # Just in case.
    if_entity_alive(1, CHR.LostDaughter)  # Just in case.
    if_event_flag_off(1, EVENT.LostDaughterHostile)
    if_action_button_state(1, Category.character, CHR.LostDaughter, 180.0, -1, 2.0, 10010200)
    if_condition_true(0, 1)
    message.dialog(10010197, ButtonType.ok_cancel, NumberButtons.no_button, CHR.LostDaughter, 3.0)
    wait(3.0)
    restart()


def event11405492():
    """ Quelaag, Heart of Chaos trigger. """
    header(11405492, 1)

    chr.disable(CHR.QuelaagHeart)

    if_event_flag_on(1, EVENT.QuelaagDead)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_off(1, EVENT.QuelaagHeartDead)
    end_if_condition_false(1)  # No other events use this flag, so safe to end here.

    if_player_inside_region(0, REGION.QuelaagHeartTrigger)

    obj.enable(1401990)
    sfx.create_map_sfx(1401991)
    obj.enable(1401992)
    sfx.create_map_sfx(1401993)

    chr.enable(CHR.QuelaagHeart)
    chr.activate_npc_buffs(CHR.QuelaagHeart)
    anim.force_animation(CHR.QuelaagHeart, 3017)  # Fade-in forward slam.

    wait(2.0)
    boss.enable_boss_health_bar(CHR.QuelaagHeart, TEXT.QuelaagHeart)
    sound.enable_map_sound(1403800)


def event11402010():
    """ Quelaag, Heart of Chaos dies. """
    header(11402010)
    end_if_this_event_on()

    if_entity_health_less_than_or_equal(0, CHR.QuelaagHeart, 0.0)
    boss.kill_boss(CHR.QuelaagHeart)
    item.award_item_to_host_only(ITEMLOT.QuelaagHeartReward)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)
    boss.disable_boss_health_bar(CHR.QuelaagHeart, TEXT.QuelaagHeart)  # Probably redundant.

    obj.disable(1401990)
    sfx.delete_map_sfx(1401991, True)
    obj.disable(1401992)
    sfx.delete_map_sfx(1401993, True)

    flag.enable(EVENT.QuelaagHeartDead)
    wait(3.0)
    sound.disable_map_sound(1403800)


def event11402040():
    """ Monitors when you've rested at the Fetid Slagmire bonfire for warping. """
    header(11402040)
    if_player_within_distance(1, 1401961, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11402040)


def event11402044():
    """ Monitor resting at Parish Turret bonfire. """
    header(11402044)
    if_player_within_distance(1, 1401960, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11402044)


def event11405035():
    """ Maneater Mildred invasion. """
    header(11405035)
    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11405036)
    # No longer requires Quelaag to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 11400901)
    skip_if_this_event_on(1)
    if_player_inside_region(1, 1402061)
    if_condition_true(0, 1)

    message.place_summon_sign(SummonSignType.black_eye_sign, CHR.ManeaterMildredInvader, 1402060,
                              summon_event_flag_id=11405036, dismissal_event_flag_id=11405037)
    wait(20.0)
    restart()


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
