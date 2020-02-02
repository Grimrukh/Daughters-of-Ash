
import sys
import inspect
from pydses import *

map_name = 'm16_00_00_00'  # New Londo Ruins / Valley of Drakes / The Abyss
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11600000
BASE_PART = 1600000


class DEBUG(IntEnum):
    GET_RUINED_CELL_KEY = False
    NEW_LONDO_DRAINED = False
    QUELLA_DREAM = False
    GET_TRANSIENT_CURSE = False
    FOUR_KINGS_DEAD = False
    GET_BLUE_TITANITE = False
    GET_SINNERS_KEY = False


class CHR(IntEnum):
    Player = 10000
    Ingward = 6180
    Rickert = 6220
    CrestfallenWarriorHollow = 6271
    Lautrec = 6300
    Kaathe = 6340
    WitchBeatriceSummon = 6520
    ArmoredTusk = 1600622
    DrakeInside = 1600700
    ArmoredTuskInside = 1600701
    GhostGargoyle = 1600702
    GhostGargoyleTail = 1600703
    GhostDarkwraith = 1600704


class ANIM(IntEnum):
    FourKingsSpawn = 6200
    PlayerSpawn = 6950


class EVENT(IntEnum):
    QuelaagDead = 9
    SensGolemDead = 11
    FourKingsDead = 13
    QuellaPactBroken = 1904
    NewLondoDrained = 11600100
    WallCorpseAppeared = 11602002
    LedgeCorpseAppeared = 11602003
    PoolCorpseAppeared = 11602004
    GravestalkersDead = 11200901
    ArrivalFromChasm = 11212002
    LordvesselReceived = 11512000
    AbyssStableFooting = 11602501


FourKings = range(1600800, 1600804)
FourKingsActiveFlags = range(11605380, 11605384)
FourKingsDeadFlags = range(11605350, 11605354)
FourKingsLoopCount = range(11605385, 11605388)
FourKingsNames = range(5390, 5394)


class GOOD(IntEnum):
    SoulOfJareel = 718
    KeyToValley = 2008
    KeyToTheSeal = 2013
    SinnersKey = 2017
    MasterKey = 2100


class ITEMLOT(IntEnum):
    KaatheJareelGift = 1630
    GhostGargoyleTailDrop = 1710


class OBJ(IntEnum):
    WallHollowCorpse = 1601612
    LedgeHollowCorpse = 1601613
    PoolHollowCorpse = 1601614
    DeadBonfire = 1601675


class REGION(IntEnum):
    FlyingDrakeBox = 1602675


class TEXT(IntEnum):
    LightBonfire = 10010182
    FireKeeperAbsent = 10010184
    OfferSoulOfJareel = 10010198
    UsedKeyToValley = 10010867
    UsedKeyToSeal = 10010872
    UsedRuinedCellKey = 10010876
    MasterKeyShattered = 10010883


def event0():
    """ Constructor. """
    header(0, 0)

    if DEBUG.GET_RUINED_CELL_KEY:
        item.award_item_to_host_only(1010000)
    if DEBUG.NEW_LONDO_DRAINED:
        flag.enable(EVENT.NewLondoDrained)
    if DEBUG.QUELLA_DREAM:
        flag.enable(1904)
    if DEBUG.GET_TRANSIENT_CURSE:
        item.award_item_to_host_only(1600520)
    if DEBUG.FOUR_KINGS_DEAD:
        flag.enable(EVENT.FourKingsDead)
    if DEBUG.GET_BLUE_TITANITE:
        item.award_item_to_host_only(100820)  # Chunk
        item.award_item_to_host_only(100820)
        item.award_item_to_host_only(100820)
        item.award_item_to_host_only(100820)
        item.award_item_to_host_only(100820)
        item.award_item_to_host_only(100820)
        item.award_item_to_host_only(100820)
        item.award_item_to_host_only(100820)
        item.award_item_to_host_only(100820)
        item.award_item_to_host_only(1210500)  # Slab
    if DEBUG.GET_SINNERS_KEY:
        item.award_item_to_host_only(1300100)

    skip_if_event_flag_off(1, EVENT.FourKingsDead)  # Abyss bonfire.
    map.register_bonfire(11600920, 1601950)
    run_event(11602044)  # (New) Monitor resting at Abyss bonfire.
    map.register_bonfire(11600984, 1601961)  # Valley of Drakes / Darkroot Basin firelink_bonfire.
    map.register_ladder(11600010, 11600011, 1601140)
    map.register_ladder(11600012, 11600013, 1601141)
    flag.enable(11600102)

    # (New) Monitor stable footing flag for Abyss.
    run_event(11602500)

    # Summon fog.
    skip_if_client(7)
    flag.enable(404)
    for fog, sfx_id in zip((1601994, 1601996, 1601998), (1601995, 1601997, 1601999)):
        obj.disable(fog)
        sfx.delete_map_sfx(sfx_id, erase_root_only=False)

    spawner.disable_spawner(1603000)  # Four Kings spawner.

    # Checkpoint fogs.
    run_event_with_slot(11600090, 0, args=(1601700, 1601701, 1602600, 1602601))
    run_event_with_slot(11600090, 1, args=(1601702, 1601703, 1602602, 1602603))
    # Gravelording.
    run_event(11605090)
    run_event(11605091)
    run_event(11605092)

    run_event(11602000)  # (New) Arrival from Manus event battle.
    run_event(11602001)  # (New) Quella dream.
    run_event_with_slot(11605080, args=(CHR.GhostGargoyle, CHR.GhostGargoyleTail))  # (New) Ghost Gargoyle tail cut.
    run_event(11602005)  # (New) Trade Soul of Jareel to Kaathe for Ruinous Hand.
    run_event(11602006)  # (New) Inspect dead bonfire.

    run_event(11605100)  # Control enemy appearance when drained or not drained.
    run_event(11600150)  # Toggle hit-boxes and kill planes when water is drained.
    run_event(11600100)  # Draining cutscene.
    run_event_with_slot(11600101, 0, args=(1601101, 11600102, 0))  # Pull floodgate lever
    run_event_with_slot(  # Sluice seal
        11600110, 0, args=(11600110, TEXT.UsedKeyToSeal, 1601111, -1, GOOD.KeyToTheSeal))  # Can't use Master Key.
    run_event_with_slot(  # Gate to Valley of the Drakes
        11600110, 10, args=(11600120, TEXT.UsedKeyToValley, 1601110, TEXT.MasterKeyShattered, GOOD.KeyToValley))
    run_event_with_slot(  # Lautrec's cell
        11600110, 20, args=(11600130, TEXT.UsedRuinedCellKey, 1601112, TEXT.MasterKeyShattered, GOOD.SinnersKey))
    run_event(11600160)  # Kick down ladder on bridge.
    run_event(11600200)  # Activate Firelink elevator by stepping on it or pulling the lever.
    run_event(11600250)  # Display message when Firelink elevator lever can't be used.
    run_event(11600199)  # Enable two elevators below after water is drained.
    run_event(11600210)  # Cathedral elevator activation.
    run_event(11600251)  # Can't activate cathedral elevator lever.
    run_event(11600220)  # Sluice gate elevator activation.
    run_event(11600252)  # Can't activate sluice gate elevator lever.
    run_event(11600230)  # Darkroot Basin elevator.
    run_event(11600235)  # (New) Darkroot Basin top lever won't work until you ride up.
    run_event(11600253)  # Can't activate Darkroot Basin elevator lever.
    run_event(11600810)  # Undead Dragon reward and despawn.
    run_event(11600400)  # Undead Dragon wakes up.
    run_event(11605397)  # Kill planes in the Abyss.
    skip_if_event_flag_on(1, 1904)
    run_event(11605398)  # Player invincibility to survive fall into Abyss.
    # Play animation of players being dragged down into the Abyss (if they don't have the Covenant of Artorias).
    for slot, player_id in enumerate(range(10000, 10006)):
        run_event_with_slot(11605360, slot, args=(player_id,))

    # FOUR KINGS

    sound.disable_map_sound(1603800)
    skip_if_event_flag_on(1, EVENT.QuellaPactBroken)  # Kings disabled in Quella's dream.
    skip_if_event_flag_off(4, EVENT.FourKingsDead)
    run_event(11605392)
    obj.disable(1601990)
    sfx.delete_map_sfx(1601991, False)
    skip(12)
    run_event(11605390)  # Host enters fog.
    run_event(11605391)  # Summon enters fog.
    run_event(11605393)  # Notify and buff bosses.
    run_event(11605392)  # Main behavior.
    run_event(11600001)  # Death.
    run_event(11605394)  # Music on.
    run_event(11605395)  # Music off.
    run_event(11605396)  # Seems to prevent Kings from using projectiles too frequently, despite the AI timer. Leave.
    for slot in range(4):
        # Monitor individual King deaths.
        run_event_with_slot(11605350, slot, args=(1600800 + slot, 5390 + slot, 11605380 + slot))

    sound.disable_map_sound(1603801)

    """
    GHOST AREAS
    - Upper ruins, first area. Expand to include areas up to cathedral, AND the watery pool down below. (853)
        - Add Banshee to corner with petrified Hollow, and a multi-ghost trigger.
    - Main cathedral, entire building, so both upper and lower ruins. (850)
    - Bridge section, as before, but add a Banshee to end and multiple ghosts trigger. (851)
    - Ingward's house, upper, as before. Remove Banshee. (852)
    - New: ghosts in the large wall, walkway between Ingward and flood lever. Banshee at end. (New: 855)
    - New: ghosts in wooden entryway to cathedral. Large box, expands into boar area and cathedral a bit. (New: 856)
    - New: ghosts in watery pool. Large box, expands into Ingward's lower house and cathedral. (New: 857)
    - Move FK tower ghosts to the air around it, and make this box giant; they can attack you anywhere they see you,
      pretty much. (854)
    - Don't use 860 Banshee box.
    
    - I have 31 ghosts to use, and will have 3 Banshees.
        - 4 in first upper area + Banshee.
            - 0, 1, 2, 3            (853, 267040/267041) (200)
        - 3 in second upper area.
            - 4, 5, 6               (850, 267010/267011) (210)
            - 5 attacks up, 6 rises up on same trigger on bridge
        - 4 in bridge section; some ambush, some attack + Banshee.
            - 7, 8, 9, 10           (851, 267020/267021) (220)
        - 4 in upper Ingward's house.
            - 11, 12, 13, 14        (852, 267030/267031) (230)
        - 4 in the large wall + Banshee.
            - 15, 16, 17, 18        (855, 267060/267061)  NEW (240)
        - 3 in wooden entryway to cathedral.
            - 19, 20, 21            (856, 267070/267071)  NEW (250)
        - 3 in lower cathedral.
            - 22, 23, 24            (857, 267080/267081)  NEW (260)
        - 3 in watery pool.
            - 25, 26, 27            (858, 267090/267091)  NEW (270)
        - 4 airborne, attack anywhere.
            - 28, 29, 30, 31        (854, 267050) (280)
    """

    # Ghosts return home when they go outside a certain area.
    slot = 0
    for ghost_id in (200, 201, 202, 203, 302):
        run_event_with_slot(11605150, slot, args=(BASE_PART + ghost_id, 1602853))  # First upper area.
        slot += 1
    for ghost_id in (210, 211, 212):
        run_event_with_slot(11605150, slot, args=(BASE_PART + ghost_id, 1602850))  # Narrow bridge to upper cathedral.
        slot += 1
    for ghost_id in (220, 221, 222, 223, 301):
        run_event_with_slot(11605150, slot, args=(BASE_PART + ghost_id, 1602851))  # Three-level bridge section.
        slot += 1
    for ghost_id in (230, 231, 232, 233):
        run_event_with_slot(11605150, slot, args=(BASE_PART + ghost_id, 1602852))  # Ingward's house, upper.
        slot += 1
    for ghost_id in (240, 241, 242, 243, 300):
        run_event_with_slot(11605150, slot, args=(BASE_PART + ghost_id, 1602855))  # Giant wall.
        slot += 1
    for ghost_id in (250, 251, 252):
        run_event_with_slot(11605150, slot, args=(BASE_PART + ghost_id, 1602856))  # Wooden entryway in lower ruins.
        slot += 1
    for ghost_id in (260, 261, 262):
        run_event_with_slot(11605150, slot, args=(BASE_PART + ghost_id, 1602857))  # Lower/middle cathedral.
        slot += 1
    for ghost_id in (270, 271, 272):
        run_event_with_slot(11605150, slot, args=(BASE_PART + ghost_id, 1602858))  # Pool in lower ruins.
        slot += 1
    for ghost_id in (280, 281, 282, 283):
        run_event_with_slot(11605150, slot, args=(BASE_PART + ghost_id, 1602854))  # Floating above Four Kings tower.
        slot += 1

    # Ghosts rise from the deep (9060) based on distance.
    for slot, (ghost_id, delay) in enumerate(zip((200, 201, 232, 233, 243, 250, 251, 270, 271),
                                                 (5.0, 5.0, 5.0, 5.0, 3.0, 6.0, 3.0, 5.0, 5.0))):
        run_event_with_slot(11605001, slot, args=(BASE_PART + ghost_id, delay, 9060), arg_types='ifi')

    # Ghosts cancel out of standby (with an attack or rise) based on a region trigger, or just snap out of standby
    # based on being attacked or an optional distance trigger.
    for slot, (ghost_id, point_id, anim_id, use_distance, distance) in enumerate(zip(
            (202,   203,  211,  212,  220,  221,  222,  223,  240,  241,  260,  262,  272),
            (250,   250,  251,  251,  252,  253,  254,  254,  255,  255,  256,  256,  257),
            (9060, 9060, 3006, 9060, 3006, 3006, 3005, 9060, 3007, 9060, 9060, 9060, 9060),
            (0,       0,    0,    0,    1,    1,    0,    0,    0,    0,    0,    0,    0),
            (0,       0,    0,    0,  5.0,  5.0,    0,    0,    0,    0,    0,    0,    0))):
        run_event_with_slot(11605050, slot, args=(BASE_PART + ghost_id, 1602000 + point_id,
                                                  anim_id, use_distance, distance), arg_types='iiiif')

    # Wisp spawning from Mass of Souls.
    for slot, (wisp_id, i, flag_id) in enumerate(zip(range(410, 416), range(1, 7),
                                                     (100, 5200, 5201, 5202, 5203, 5204))):
        run_event_with_slot(11605200, slot, args=(1600400, BASE_PART + wisp_id, i, BASE_FLAG + flag_id))

    # Wisp self-destruct (disabling).
    for slot, wisp_id in enumerate(range(410, 416)):
        run_event_with_slot(11605250, slot, args=(BASE_PART + wisp_id,))

    # Mass of Souls doesn't respawn.
    run_event_with_slot(11600850, 0, args=(1600400,))

    # Chests.
    run_event_with_slot(11600600, 0, args=(1601650, 11600600))
    run_event_with_slot(11600600, 1, args=(1601651, 11600601))
    run_event_with_slot(11600600, 2, args=(1601652, 11600602))

    # Corpses in urns.
    run_event_with_slot(11600650, 0, args=(1601610, 1601310))
    run_event_with_slot(11600650, 1, args=(1601611, 1601311))


def event50():
    """ NPC constructor. """
    header(50, 0)

    # WITCH BEATRICE (summon)

    chr.humanity_registration(CHR.WitchBeatriceSummon, 8932)
    run_event(11605030)
    run_event(11605032)
    run_event(11605033)

    # INGWARD

    chr.humanity_registration(CHR.Ingward, 8406)
    skip_if_event_flag_on(2, 1315)
    skip_if_event_flag_on(1, 1313)
    skip(1)
    chr.disable(CHR.Ingward)
    run_event_with_slot(11600510, 0, args=(CHR.Ingward, 1314))  # Hostile.
    run_event_with_slot(11600520, args=(CHR.Ingward, 1310, 1319, 1315))  # Dead.
    # Ingward advances state when you have the Lordvessel.
    run_event_with_slot(11600530, args=(CHR.Ingward, 1310, 1319, 1311))
    # Ingward advances state when you have drained New Londo Ruins.
    run_event_with_slot(11600531, args=(CHR.Ingward, 1310, 1319, 1312))
    # Ingward move to Firelink Shrine when you talk to him enough, then de-load him.
    run_event_with_slot(11600532, args=(CHR.Ingward, 1310, 1319, 1313))

    # BLACKSMITH RICKERT

    chr.humanity_registration(CHR.Rickert, 8414)
    run_event_with_slot(11600510, 1, args=(CHR.Rickert, 1381))
    run_event_with_slot(11600520, 1, args=(CHR.Rickert, 1380, 1399, 1382))

    # CRESTFALLEN WARRIOR (Hollow)

    chr.set_team_type_and_exit_standby_animation(CHR.CrestfallenWarriorHollow, TeamType.hostile_ally)
    skip_if_event_flag_on(1, 1464)
    chr.disable(CHR.CrestfallenWarriorHollow)
    run_event_with_slot(11600520, 5, args=(CHR.CrestfallenWarriorHollow, 1460, 1489, 1462))  # Dead.
    # Spawns him when 1464 is enabled (as the map may have already loaded).
    run_event_with_slot(11600545, args=(CHR.CrestfallenWarriorHollow,))

    # DARKSEEKER KAATHE

    skip_if_event_flag_on(1, 1904)  # Disabled if this is the end of Quella's dream.
    skip_if_event_flag_off(2, 15)  # Depends on Gwyn, suggesting post-Gwyn freedom.
    chr.disable(CHR.Kaathe)
    skip_if_event_flag_on(11, 15)
    chr.enable_immortality(CHR.Kaathe)
    skip_if_event_flag_on(2, 1677)
    skip_if_event_flag_on(1, 1676)
    skip(1)
    chr.disable(CHR.Kaathe)
    # Appears when you defeat Four Kings and haven't placed the Lordvessel.
    run_event_with_slot(11600537, args=(CHR.Kaathe, 1670, 1678, 1671))
    # Advances state when you have the Lordvessel.
    run_event_with_slot(11600538, args=(CHR.Kaathe, 1670, 1678, 1672))
    # Advances state when you place the Lordvessel.
    run_event_with_slot(11600539, args=(CHR.Kaathe, 1670, 1678, 1673))
    # Departs if refuse to join him, I think, or reject him somehow.
    run_event_with_slot(11600540, args=(CHR.Kaathe, 1670, 1678, 1677))
    # Departs if you attack him or if a certain talk flag is on.
    run_event_with_slot(11600541, args=(CHR.Kaathe, 1670, 1678, 1677))
    # Kaathe takes you to Firelink Altar.
    run_event(11606200)

    # (NEW) LAUTREC OF CARIM

    chr.humanity_registration(CHR.Lautrec, 8462)
    skip_if_client(1)
    flag.disable(11010584)  # Not sure. Resets some dialogue for hosts?
    skip_if_event_flag_on(3, 11010584)  # Won't happen for hosts because of above.
    skip_if_event_flag_on(2, 1574)
    skip_if_event_flag_on(1, 1570)
    chr.disable(CHR.Lautrec)
    run_event_with_slot(11600510, 6, args=(CHR.Lautrec, 1574))  # Hostile.
    run_event_with_slot(11600520, 6, args=(CHR.Lautrec, 1570, 1599, 1575))  # Dead.
    run_event_with_slot(11600550, args=(CHR.Lautrec, 1570, 1599, 1571))  # Freed by player.
    run_event_with_slot(11600551, args=(CHR.Lautrec, 1570, 1599, 1577))  # Frees himself.
    run_event_with_slot(11600552, args=(CHR.Lautrec, 1570, 1599, 1575))  # Dies in his cell if you drain New Londo.
    run_event(11600553)  # Forces you to speak to Lautrec before you can interact with his cell door.


def event11600100():
    """ Drain New Londo. """
    header(11600100, 0)

    skip_if_event_flag_on(1, 11600101)
    skip_if_this_event_off(8)
    anim.end_animation(1601100, 10)
    hitbox.disable_hitbox(1603100)
    hitbox.disable_hitbox(1603102)
    hitbox.disable_hitbox(1603103)
    hitbox.disable_hitbox(1603104)
    obj.disable(1601120)
    flag.disable(404)
    end()

    hitbox.enable_hitbox(1603103)
    hitbox.enable_hitbox(1603104)
    light.set_area_texture_parambank_slot_index(16, 1)  # Switch to brighter light map until New Londo is drained.
    if_event_flag_on(0, 11600101)
    skip_if_multiplayer(2)
    cutscene.play_cutscene_to_player(160000, CutsceneType.skippable, CHR.Player)
    skip(1)
    cutscene.play_cutscene_to_player(160000, CutsceneType.unskippable, CHR.Player)
    wait_frames(1)
    flag.enable(EVENT.NewLondoDrained)
    light.set_area_texture_parambank_slot_index(16, 0)  # Original dark light map.
    restart()


def event11602000():
    """ Set spawn point when player comes from Manus arena. """
    header(11602000, 0)
    end_if_event_flag_off(EVENT.ArrivalFromChasm)
    flag.disable(EVENT.ArrivalFromChasm)
    warp.set_player_respawn_point(1602876)
    network.save_request()


def event11602001():
    """ Eternal condemnation in the Abyss by dying in Quella's challenge mode. """
    header(11602001)
    if_event_flag_on(0, EVENT.QuellaPactBroken)
    skip_if_this_event_on(2)
    warp.set_player_respawn_point(1602950)
    network.save_request()
    wait(5.0)
    message.status_explanation(10010209, False)


def event11600110():
    """ Open a gate (o6010) with intended key or Master Key, which breaks if used. """
    header(11600110)
    objact_id, key_message, gate_id, master_key_message, key_id = define_args('iiiii')
    skip_if_this_event_slot_off(6)
    anim.end_animation(gate_id, 0)  # Re-open door.
    for idx in range(4):
        obj.deactivate_object_with_idx(gate_id, -1, idx)
    end()

    if_host(1)
    if_object_activated(1, objact_id)
    if_condition_true(0, 1)
    flag.enable(objact_id)
    end_if_client()
    if_player_has_good(2, key_id)  # Overrides Master Key.
    skip_if_condition_true(3, 2)
    message.dialog(master_key_message, ButtonType.yes_no, NumberButtons.no_button, gate_id, 3.0)
    item.remove_items_from_player(ItemType.good, GOOD.MasterKey, 0)  # Break Master Key.
    skip(1)
    message.dialog(key_message, ButtonType.yes_no, NumberButtons.no_button, gate_id, 3.0)

    network.disable_sync()
    wait(2.0)
    for idx in range(4):
        obj.deactivate_object_with_idx(gate_id, -1, idx)


def event11600235():
    """ Controls lever at the top of Darkroot Basin elevator, which won't work until you ride up. """
    header(11600235, 0)
    end_if_event_flag_on(11600234)

    obj.disable_activation(1601231, 6101)

    if_event_flag_off(1, 11600234)
    if_action_button_state(1, Category.object, 1601231, 180.0, -1, 2.0, 10010501)
    if_event_flag_on(2, 11600234)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    skip_if_condition_true_finished(1, 2)
    message.dialog(10010170, ButtonType.yes_no, NumberButtons.no_button, 1601231, 2.0)
    wait(3.0)
    restart()

    obj.enable_activation(1601231, 6101)
    end()


def event11600230():
    """ Darkroot Basin elevator. Now, must be used from the bottom before it will work. """
    header(11600230, 0)
    skip_if_event_flag_off(3, 11600231)
    anim.end_animation(1601230, 26)  # start elevator at top
    obj.disable_activation(1601231, 6101)  # disable top lever
    skip(2)
    anim.end_animation(1601230, 21)  # start elevator at bottom
    obj.disable_activation(1601232, 6101)  # disable bottom lever

    if_event_flag_off(1, 11600231)
    if_player_inside_region(1, 1602231)  # player stands on elevator at bottom
    if_event_flag_on(2, 11600231)
    if_player_inside_region(2, 1602230)  # player stands on elevator at top
    if_event_flag_on(2, 11600234)  # (new) elevator has been activated from the bottom
    if_object_activated(3, 11600232)  # bottom lever
    if_object_activated(4, 11600233)  # top lever
    if_event_flag_on(4, 11600234)  # (new) elevator has been activated from the bottom
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(-1, 4)
    if_condition_true(0, -1)

    # Activate elevator.
    wait_for_network_approval(3.0)
    flag.enable(11605123)  # elevator is moving
    flag.enable(11600234)  # (new) elevator has been activated first time
    skip_if_condition_true_finished(10, 2)
    skip_if_condition_true_finished(9, 4)

    # Elevator going up.
    flag.enable(11600231)
    obj.disable_activation(1601231, 6101)
    anim.force_animation(1601230, 10, wait_for_completion=True)
    anim.force_animation(1601230, 6, wait_for_completion=True)
    if_all_players_outside_region(0, 1602230)
    anim.force_animation(1601230, 26, wait_for_completion=True)
    obj.enable_activation(1601232, 6101)
    flag.disable(11605123)
    restart()

    # Elevator going down.
    flag.disable(11600231)
    obj.disable_activation(1601232, 6101)
    anim.force_animation(1601230, 17, wait_for_completion=True)
    anim.force_animation(1601230, 7, wait_for_completion=True)
    if_all_players_outside_region(0, 1602231)
    anim.force_animation(1601230, 21, wait_for_completion=True)
    obj.enable_activation(1601231, 6101)
    flag.disable(11605123)
    restart()


def event11600550():
    """ Lautrec is freed by the player. """
    header(11600550, 0)
    lautrec, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1574)
    if_event_flag_on(1, 1570)
    if_event_flag_on(1, 11600130)  # Cell gate opened.
    if_entity_alive(1, lautrec)
    if_condition_true(0, 1)
    chr.set_standby_animation_settings(CHR.Lautrec, cancel_animation=7801)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    flag.enable(11010584)


def event11600553():
    """ Forces you to speak to Lautrec before you can interact with the gate. """
    header(11600553, 0)

    end_if_event_flag_off(1570)  # Lautrec must be trapped.
    end_if_event_flag_on(11010593)
    for idx in range(4):
        obj.deactivate_object_with_idx(1601112, -1, idx)
    if_event_flag_on(0, 11010593)
    obj.activate_object_with_idx(1601112, -1, 0)
    obj.activate_object_with_idx(1601112, -1, 1)


def event11600551():
    """ Lautrec frees himself if you kill Quelaag, Sen's Golem, or the Gravestalkers. """
    header(11600551, 0)
    npc, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1574)  # not hostile
    if_event_flag_on(1, 1570)  # in cell
    if_event_flag_on(-1, EVENT.QuelaagDead)
    if_event_flag_on(-1, EVENT.SensGolemDead)
    if_event_flag_on(-1, EVENT.GravestalkersDead)
    if_event_flag_on(2, 812)  # Undead Parish Humanity picked up on altar.
    if_event_flag_on(2, 813)  # Blighttown FKS picked up.
    if_condition_true(-1, 2)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.disable(npc)

    # Open and disable Lautrec's cell gate.
    skip_if_event_flag_on(7, 1570)
    anim.end_animation(1601112, 0)
    for idx in range(4):
        obj.deactivate_object_with_idx(1601112, -1, idx)
    flag.enable(11600130)  # Gate opened.


def event11600552():
    """ Lautrec dies in his cell if you drain New Londo before he is freed (by you or himself). """
    header(11600552)
    npc, start_flag, end_flag, new_flag = define_args('iiii')
    if_event_flag_on(1, 1570)  # in cell, doesn't matter if he's hostile
    if_event_flag_on(1, EVENT.NewLondoDrained)
    if_condition_true(0, 1)
    chr.kill(npc, False)  # existing Dead NPC event will take care of flags and treasure (will appear on reload)
    flag.enable(11010593)  # enables interaction with gate


def event11605360():
    """ Abyss death. Now disabled during Quella dream. """
    header(11605360)
    player_id, = define_args('i')
    network.disable_sync()
    if_event_flag_off(1, EVENT.FourKingsDead)
    if_event_flag_off(1, EVENT.QuellaPactBroken)
    if_entity_inside_area(1, player_id, 1602990)
    if_entity_does_not_have_special_effect(1, player_id, 2200)
    if_condition_true(0, 1)
    chr.reset_animation(player_id, True)
    anim.force_animation(player_id, 6084, wait_for_completion=True)
    chr.disable(player_id)
    end_if_not_equal(player_id, 10000)
    flag.enable(8120)


def event11605392():
    """ Four Kings behavior. Launches main loop 5399. Also depends on Quella's dream not having ended. """
    header(11605392, 1)

    for king in FourKings:
        chr.disable(king)
        chr.disable_health_bar(king)

    # In Quella's dream.
    skip_if_event_flag_off(2, EVENT.QuellaPactBroken)
    obj.disable(1601950)  # Abyss bonfire. (Kaathe disabled in 50.)
    end()

    # Dead.
    skip_if_event_flag_off(6, EVENT.FourKingsDead)
    obj.enable_treasure(1601600)
    for king in FourKings:
        chr.kill(king)
    end()

    if_player_inside_region(0, 1602999)
    network.disable_sync()
    run_event(11605385)  # Kick off timer so it can be restarted.
    wait(7.0)
    for king in FourKings:
        chr.enable(king)
        anim.force_animation(king, ANIM.FourKingsSpawn)
        chr.enable_ai(king)

    boss.enable_boss_health_bar(FourKings[0], FourKingsNames[0])
    flag.enable(FourKingsActiveFlags[0])
    flag.enable(FourKingsLoopCount[0])
    chr.ai_instruction(FourKings[0], 1, 1)

    run_event(11605399)
    flag.enable(11605392)

    for king in FourKings[1:]:
        anim.force_animation(king, 200, loop=True)
        wait(0.5)
        anim.force_animation(king, 200)


def event11600001():
    """ Four Kings death script. Now, they must all be dead. """
    header(11600001)
    obj.disable_treasure(1601600)  # Witch Beatrice's corpse in the Valley.
    obj.disable(1601600)
    obj.disable(1601950)

    for king_id in FourKings:
        if_entity_health_less_than_or_equal(1, king_id, 0.0)
    if_event_flag_on(1, 11605395)  # Music has stopped.
    if_condition_true(0, 1)
    skip_if_multiplayer(2)
    cutscene.play_cutscene_and_warp_specific_player(160010, CutsceneType.skippable, 1602120, 16, 0, CHR.Player)
    skip(4)
    skip_if_client(2)
    cutscene.play_cutscene_and_warp_specific_player(160010, CutsceneType.unskippable, 1602120, 16, 0, CHR.Player)
    skip(1)
    cutscene.play_cutscene_to_player(160010, CutsceneType.unskippable, CHR.Player)  # Summons aren't warped.
    wait_frames(1)

    for king_id in FourKings:
        chr.disable(king_id)
        chr.kill(king_id, True)
    boss.kill_boss(FourKings[0])
    flag.enable(EVENT.FourKingsDead)
    obj.disable(1601990)
    sfx.delete_map_sfx(1601991, True)
    obj.enable_treasure(1601600)  # Witch Beatrice's corpse in the Valley.
    obj.enable(1601600)
    end_if_client()

    game.award_achievement(37)
    sfx.create_oneoff_sfx(Category.object, 1601950, -1, 90014)
    wait(2.0)
    obj.enable(1601950)
    map.register_bonfire(11600920, 1601950)


def event11605350():
    """ Monitor individual King deaths, which removes them from the rotation. """
    header(11605350)
    king_id, king_name, active_flag = define_args('ihi')

    if_host(1)
    if_entity_health_less_than_or_equal(1, king_id, 0.0)
    if_condition_true(0, 1)

    skip_if_event_flag_off(1, active_flag)
    boss.disable_boss_health_bar(king_id, king_name)

    end()


def event11605399():
    """ Main battle loop for Four Kings. """
    header(11605399)

    end_if_event_flag_on(EVENT.FourKingsDead)

    for king_index in range(4):

        if king_index == 3:
            skip_if_event_flag_off(28, FourKingsActiveFlags[king_index])
        else:
            skip_if_event_flag_off(21, FourKingsActiveFlags[king_index])

        # Wait for rotation (due to timeout or King death).
        if_event_flag_on(-1, FourKingsDeadFlags[king_index])
        if_number_true_flags_in_range_greater_than_or_equal(7, FourKingsDeadFlags[0], FourKingsDeadFlags[3], 3)
        skip_if_condition_true(1, 7)  # Can't time out if this is the last King.
        if_time_elapsed(-1, 45.0)
        if_condition_true(0, -1)
        flag.disable(FourKingsActiveFlags[king_index])
        flag.enable(FourKingsActiveFlags[(king_index + 1) % 4])
        chr.ai_instruction(FourKings[(king_index + 1) % 4], 1, 1)  # Next King engages.

        # Delay between next King engaging and previous King disengaging.
        skip_if_event_flag_on(5, FourKingsDeadFlags[king_index])
        skip_if_event_flag_off(2, FourKingsLoopCount[2])
        wait(10.0)
        skip(2)
        skip_if_event_flag_off(1, FourKingsLoopCount[1])
        wait(5.0)

        boss.disable_boss_health_bar(FourKings[king_index], FourKingsNames[king_index])
        end_if_event_flag_on(11605395)
        skip_if_event_flag_on(1, FourKingsDeadFlags[(king_index + 1) % 4])
        boss.enable_boss_health_bar(FourKings[(king_index + 1) % 4], FourKingsNames[(king_index + 1) % 4])
        skip_if_event_flag_on(1, FourKingsDeadFlags[king_index])
        chr.ai_instruction(FourKings[king_index], -1, 1)  # Disengage.
        if king_index == 3:
            skip_if_event_flag_on(6, FourKingsLoopCount[2])
            skip_if_event_flag_on(3, FourKingsLoopCount[1])
            flag.disable(FourKingsLoopCount[0])
            flag.enable(FourKingsLoopCount[1])
            skip(2)
            flag.disable(FourKingsLoopCount[1])
            flag.enable(FourKingsLoopCount[2])

        restart()

    restart()


def event11605395():
    """ Four Kings music stops when they all die. """
    header(11605395)
    network.disable_sync()
    for king_id in FourKings:
        if_entity_health_less_than_or_equal(1, king_id, 0.0)
    if_event_flag_on(1, 11605394)
    if_condition_true(0, 1)
    sound.disable_map_sound(1603800)


def event11605396():
    """ Control Four Kings projectile use. """
    header(11605396)
    if_event_flag_on(0, 11605392)
    end_if_event_flag_on(11605395)

    for condition_slot, king_id in zip(range(1, 5), FourKings):
        if_entity_alive(condition_slot, king_id)
        skip_if_condition_false(5, condition_slot)
        chr.ai_instruction(king_id, 1, 0)
        if_entity_dead(-condition_slot, king_id)
        if_has_tae_event(-condition_slot, king_id, 500)
        if_condition_true(0, -condition_slot)
        chr.ai_instruction(king_id, -1, 0)

    restart()


def event11605100():
    """ Control enemy appearance when drained or not drained. """
    header(11605100, 1)

    FloodedOnly = range(1600600, 1600624)  # Hollows in Ruins (only 1600650 remains there)
    DrainedOnly = (
            # Drake that flies inside, moved Tusk, Gargoyle ghost/tail, Darkwraith ghost
            list(range(1600700, 1600705)) +
            # Wisps
            list(range(1600410, 1600416)) +
            # Ghosts
            list(range(1600200, 1600204)) +
            list(range(1600210, 1600213)) +
            list(range(1600220, 1600224)) +
            list(range(1600230, 1600234)) +
            list(range(1600240, 1600244)) +
            list(range(1600250, 1600253)) +
            list(range(1600260, 1600263)) +
            list(range(1600270, 1600273)) +
            list(range(1600280, 1600284)) +
            # Banshees
            list(range(1600300, 1600303)) +
            # Mass of Souls
            [1600400]
    )

    skip_if_event_flag_off(len(FloodedOnly) + 11, EVENT.NewLondoDrained)

    for enemy_id in FloodedOnly:
        chr.disable_backread(enemy_id)
    chr.set_standby_animation_settings(1600650, standby_animation=9010)  # Last Hollow in house goes more insane.

    skip_if_event_flag_on(2, EVENT.WallCorpseAppeared)
    obj.disable(OBJ.WallHollowCorpse)
    obj.disable_treasure(OBJ.WallHollowCorpse)

    skip_if_event_flag_on(2, EVENT.LedgeCorpseAppeared)
    obj.disable(OBJ.LedgeHollowCorpse)
    obj.disable_treasure(OBJ.LedgeHollowCorpse)

    skip_if_event_flag_on(2, EVENT.PoolCorpseAppeared)
    obj.disable(OBJ.PoolHollowCorpse)
    obj.disable_treasure(OBJ.PoolHollowCorpse)

    end()

    for enemy_id in DrainedOnly:
        chr.disable_backread(enemy_id)
    obj.disable(OBJ.WallHollowCorpse)
    obj.disable_treasure(OBJ.WallHollowCorpse)
    obj.disable(OBJ.LedgeHollowCorpse)
    obj.disable_treasure(OBJ.LedgeHollowCorpse)
    obj.disable(OBJ.PoolHollowCorpse)
    obj.disable_treasure(OBJ.PoolHollowCorpse)

    if_event_flag_on(0, EVENT.NewLondoDrained)

    for enemy_id in FloodedOnly:
        chr.disable_backread(enemy_id)

    for enemy_id in DrainedOnly:
        chr.enable_backread(enemy_id)

    if_entity_alive(1, 1600617)
    skip_if_condition_false(3, 1)
    obj.enable(OBJ.WallHollowCorpse)
    obj.enable_treasure(OBJ.WallHollowCorpse)
    flag.enable(EVENT.WallCorpseAppeared)

    if_entity_alive(2, 1600606)
    skip_if_condition_false(3, 2)
    obj.enable(OBJ.LedgeHollowCorpse)
    obj.enable_treasure(OBJ.LedgeHollowCorpse)
    flag.enable(EVENT.LedgeCorpseAppeared)

    if_entity_alive(3, 1600601)
    skip_if_condition_false(3, 2)
    obj.enable(OBJ.PoolHollowCorpse)
    obj.enable_treasure(OBJ.PoolHollowCorpse)
    flag.enable(EVENT.PoolCorpseAppeared)

    chr.set_standby_animation_settings(1600650, standby_animation=9010)  # Last Hollow in house goes more insane.


def event11605080():
    """ Ghost gargoyle tail cut. """
    header(11605080, 1)
    gargoyle, tail = define_args('ii')
    chr.disable(tail)

    skip_if_this_event_slot_off(5)
    chr.set_display_mask(gargoyle, 0, 0)
    chr.set_hitbox_mask(gargoyle, 1, 1)
    chr.set_special_effect(gargoyle, 5434)
    chr.ai_instruction(gargoyle, 20, 0)
    end()

    if_entity_backread_enabled(0, gargoyle)
    chr.create_multipart_npc_part(gargoyle, 5351, 1, 65, 1, 1, False, False)
    if_body_part_health_less_than_or_equal(1, gargoyle, 5351, 0)
    if_entity_health_less_than_or_equal(2, gargoyle, 0.0)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    end_if_condition_true_finished(2)  # Gargoyle is killed before tail is cut.

    chr.reset_animation(gargoyle, False)
    warp.warp_and_copy_floor(tail, Category.character, gargoyle, 110, gargoyle)
    chr.enable(tail)

    anim.force_animation(gargoyle, 8000)
    anim.force_animation(tail, 8100)
    chr.set_display_mask(gargoyle, 0, 0)
    chr.set_hitbox_mask(gargoyle, 1, 1)
    chr.set_special_effect(gargoyle, 5434)
    chr.ai_instruction(gargoyle, 20, 0)
    chr.replan_ai(gargoyle)
    if_character_human(-7, CHR.Player)
    if_character_hollow(-7, CHR.Player)
    end_if_condition_false(-7)
    item.award_item_to_host_only(ITEMLOT.GhostGargoyleTailDrop)


def event11602005():
    """ Trade Soul of Jareel to Kaathe for Ruinous Hand. """
    header(11602005)

    if_event_flag_on(1, EVENT.FourKingsDead)
    if_player_has_good(1, GOOD.SoulOfJareel)
    if_event_flag_off(1, 1676)
    if_event_flag_off(1, 1677)
    if_action_button_state(1, Category.character, CHR.Kaathe, 180.0, -1, 5.0, 10010198)
    if_condition_true(0, 1)
    item.remove_items_from_player(ItemType.good, GOOD.SoulOfJareel, 1)  # Might remove all of them.
    item.award_item_to_host_only(ITEMLOT.KaatheJareelGift)


def event11600530():
    """ Ingward responds after you've obtained the Lordvessel. """
    header(11600530)
    ingward, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, 1314)
    if_event_flag_on(1, 1310)
    if_event_flag_on(1, EVENT.LordvesselReceived)
    if_entity_alive(1, ingward)
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)


def event11600538():
    """ Kaathe responds if you have the Lordvessel. (He will have disappeared already if you talk to Frampt.) """
    header(11600538)
    kaathe, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_on(1, 1671)
    if_event_flag_on(1, EVENT.LordvesselReceived)
    if_entity_alive(1, kaathe)
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)


def event11602044():
    """ Monitor resting at Abyss bonfire. """
    header(11602044)
    if_player_within_distance(1, 1601950, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11602044)


def event11602006():
    """ Dead bonfire. """
    header(11602006)
    if_action_button_state(0, Category.object, OBJ.DeadBonfire, 180.0, -1, 2.0, TEXT.LightBonfire)
    message.dialog(TEXT.FireKeeperAbsent, ButtonType.ok_cancel, NumberButtons.no_button, OBJ.DeadBonfire, 2.0)
    wait(3.0)
    restart()


def event11602500():
    """ Stable footing for Abyss (after Four Kings or after breaking Quella pact). """
    header(11602500, 1)
    flag.disable(EVENT.AbyssStableFooting)
    if_event_flag_on(-1, EVENT.FourKingsDead)
    if_event_flag_on(-1, EVENT.QuellaPactBroken)
    if_condition_true(0, -1)
    flag.enable(EVENT.AbyssStableFooting)


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
