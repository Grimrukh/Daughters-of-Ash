
import sys
import inspect
from pydses import *

map_name = 'm13_00_00_00'  # Catacombs
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'


class DEBUG(IntEnum):
    GET_PALE_EYE_ORB = False
    GET_EYE_OF_DEATH = False
    GET_CHTHONIC_SPARK = False
    VAMOS_GIVEN_CHTHONIC_SPARK = False


class ANIM(IntEnum):
    PlayerCrouching = 7610
    PlayerGetUp = 7801  # only approximate match to above
    TouchMimicBonfire = 7114


class CHR(IntEnum):
    Player = 10000
    Vamos = 6200
    Patches = 6320
    PaladinLeeroySummon = 6550
    Jeremiah = 6770
    DepravedApostate = 6850
    HauntingSemblance = 1300300
    SensCryptInteraction = 1300876
    ThirdPaleDemon = 1300877
    FirstPaleDemon = 1300878
    SecondPaleDemon = 1300879
    Pinwheel = 1300800
    FakePinwheel = 1300815
    GiantSkeletonNecromancer = 1300260
    GiantSkeleton = 1300265
    CowardNecromancer = 1300270  # no Skeletons; drops Skull Lantern
    MassOfSouls = 1300290


PinwheelClones = range(1300801, 1300815)


class EVENT(IntEnum):
    BellGargoylesDead = 3
    ReaperDiedSecond = 11012016
    PinwheelDead = 6
    VamosGivenChthonicSpark = 363
    VamosHostile = 1341
    VamosDead = 1342
    PatchesBeforeBridgeTrick = 1620
    PatchesHostile = 1627
    FakePinwheelDead = 11300000
    NitoAwake = 11310000
    NitoDead = 7
    CovenantVisit = 11310050

    FirstBridgeSafe = 11300402
    SecondBridgeSafe = 11300403
    FirstBridgeSafeActivation = 11300902
    FirstBridgeSpikesActivation = 11300903
    SecondBridgeSafeActivation = 11300904
    SecondBridgeSpikesActivation = 11300905
    FirstBridgeTriggerSafe = 11305035
    FirstBridgeTriggerSpikes = 11305036
    SecondBridgeTriggerSafe = 11305037
    SecondBridgeTriggerSpikes = 11305038

    PaleEyeOrbReturned = 11302002
    LeeroyInvasionDone = 11310810
    VamosNoChthonicSparkDrop = 51300992
    JeremiahNoChthonicSparkDrop = 50006771
    JeremiahStoleFromVamos = 11302007
    # 11302010 marks first-time bonerust affliction.
    # 11302050 marks BONERUST.

    JeremiahInRuins = 11412050  # he will attack you in old Firesage room, which then triggers InLostIzalith
    JeremiahImpatient = 11412051  # you can witness him killing Ceaseless (if alive) and entering Lost Izalith
    JeremiahInIzalith = 11412052  # triggered whenever Lost Izalith opens OR if player enters Demon Ruins with Spark
    JeremiahFleeingIzalith = 11412053  # triggered when he takes the Spark from you in sewers or Bed of Chaos battle
    JeremiahEscaped = 11412054  # triggered if Lost Daughter and Quelana can't kill him
    JeremiahDeadFromPlayer = 11412055  # triggered if you kill him in any of the three battles
    JeremiahDeadNearFairLady = 11412056  # triggered after FleeingIzalith if Lost Daughter is with Fair Lady
    JeremiahDeadNearQuelana = 11412057  # triggered after FleeingIzalith if above is false, and Quelana is alive
    JeremiahDeadInQuelaagArena = 11412058  # triggered after FleeingIzalith if Lost Daughter absent and D.Q. active


class REGION(IntEnum):
    PatchesBridgeTrickTrigger = 1302001
    DepravedApostateSignPoint = 1302675
    DepravedApostateTrigger = 1302676
    JeremiahTrigger = 1302677


class TEXT(IntEnum):
    PinwheelName = 3320
    Examine = 10010100
    ReturnPaleEyeOrb = 10010178
    ReturnedPaleEyeOrb = 10010179
    PaleOrbAlreadyStolen = 10010180
    LightBonfire = 10010182


class GOOD(IntEnum):
    PaleEyeOrb = 2530


class ITEMLOT(IntEnum):
    PaleEyeOrb = 6322


class SOUND(IntEnum):
    PinwheelBGM = 1303800
    BossDeath = 777777777
    BonfireMimic = 318011001  # voice (v)
    SkeletonAssembly = 290004002  # character_motion (c)


def event0():
    """ Constructor. """
    header(0, 0)

    if DEBUG.GET_PALE_EYE_ORB:
        item.award_item_to_host_only(ITEMLOT.PaleEyeOrb)
    if DEBUG.GET_CHTHONIC_SPARK:
        item.award_item_to_host_only(2510)
    if DEBUG.VAMOS_GIVEN_CHTHONIC_SPARK:
        flag.enable(EVENT.VamosGivenChthonicSpark)
    if DEBUG.GET_EYE_OF_DEATH:
        item.award_item_to_host_only(1300020)

    map.register_bonfire(11300992, 1301960)
    map.register_bonfire(11300984, 1301961)
    run_event(11302040)  # (New) Monitors when you've rested at the second bonfire, for warping.
    for ladder_flag_1, ladder_flag_2, ladder_id in zip(range(11300010, 11300029, 2),
                                                       range(11300011, 11300030, 2),
                                                       range(1301140, 1301150)):
        if ladder_id == 1301143:
            skip_if_event_flag_off(1, 6)  # Skip ladder out of Pinwheel's room if he is alive.
        map.register_ladder(ladder_flag_1, ladder_flag_2, ladder_id)

    skip_if_client(2)
    obj.disable(1301994)  # Summon fog.
    sfx.delete_map_sfx(1301995)  # Summon fog.

    # Checkpoint fog.
    run_event_with_slot(11300090, 0, args=(1301700, 1301701, 1302650, 1302651))

    # Gravelording.
    run_event(11305065)
    run_event(11305066)
    run_event(11305067)

    # Massive skeleton immortality management.
    run_event(11300800)

    run_event(11300300)  # First spike bridge damage.
    run_event(11300350)  # Second spike bridge damage.
    run_event_with_slot(11300900, 0, args=(11300900, 1301000, 1301100, 1304000))  # Open gate with lever.
    run_event_with_slot(11300900, 1, args=(11300901, 1301001, 1301101, 1304001))  # Open gate with lever.

    # Rotating bridges. 5032 toggles the event flags based on the ObjAct, and 5030 actually rotates the bridge.
    run_event_with_slot(11305032, 0, args=(EVENT.FirstBridgeSafeActivation, EVENT.FirstBridgeSpikesActivation,
                                           EVENT.FirstBridgeTriggerSafe, EVENT.FirstBridgeTriggerSpikes))
    run_event_with_slot(11305030, 0, args=(EVENT.FirstBridgeSafe, EVENT.FirstBridgeTriggerSafe,
                                           EVENT.FirstBridgeTriggerSpikes, 1301002, 1301102, 1304002))
    run_event_with_slot(11305032, 1, args=(EVENT.SecondBridgeSafeActivation, EVENT.SecondBridgeSpikesActivation,
                                           EVENT.SecondBridgeTriggerSafe, EVENT.SecondBridgeTriggerSpikes))
    run_event_with_slot(11305030, 1, args=(EVENT.SecondBridgeSafe, EVENT.SecondBridgeTriggerSafe,
                                           EVENT.SecondBridgeTriggerSpikes, 1301003, 1301103, 1304003))

    run_event(11305000)  # Coffin warp to Gravelord Nito.
    run_event(11305001)  # Toggles activations to let you get out of the coffin after you've been in for 2 sec.
    run_event(11305002)  # Converts flag 5006 (enabled above) to 5008 after five seconds. (Can't get out.)
    run_event(11305003)  # When flag 5008 is enabled, toggles activations back and restarts above three events.
    run_event(11305004)  # Stops nearby enemy (now Bonewheel) from attacking you in the coffin.
    run_event(11305005)  # (New) Stops other Bonewheel from attacking you in the coffin.
    run_event(11305009)  # Re-enables prompt two seconds after you get out of the coffin.

    # Change death animation of any player inside the coffin.
    for player_id in range(6):
        run_event_with_slot(11300420, player_id, args=(10000 + player_id,))

    run_event(11300210)  # Vamos cutscene. Only warps players into his room if you were actually there.
    run_event(11305060)  # Determines if you are actually in Vamos's room when the cutscene is triggered.
    run_event(11300200)  # Reveal ladder when Pinwheel is killed.
    run_event(11305045)  # Profane Semblance aggro.

    # Floors collapse when you walk on them.
    for slot in range(6):
        run_event_with_slot(11300100, slot, args=(11300100 + slot, 1302100 + slot, 1301010 + slot,
                                                  303000000 + slot * 100000))

    run_event(11300150)  # Ceiling breaks in Sen's Tomb. Profane Semblance now falls down.
    run_event(11300160)  # Illusory wall near second bonfire.

    # Statue spike traps.
    for slot in range(20):
        if slot == 11:
            # One statue skipped.
            continue
        run_event_with_slot(11300700, slot, args=(1301200 + slot, 11300750 + slot))

    run_event_with_slot(11302000, args=(1301875, 1300875))  # (NEW) Bonfire Mimic
    run_event(11302001)  # (NEW) Interact with Sen's crypt.
    run_event(11302003)  # (NEW) Treasure and Bonewheel near fake bonfire disabled as long as it's alive.
    run_event(11302004)  # (NEW) Vamos will drop the Chthonic Spark if it's given to him.
    run_event(11302005)  # (NEW) Jeremiah kills Vamos, takes the Spark, and has one battle with you.

    # (NEW) Paladin Leeroy's corpse only appears if he has been killed.
    skip_if_event_flag_on(2, EVENT.LeeroyInvasionDone)
    obj.disable_treasure(1301601)
    obj.disable(1301601)
    skip_if_event_flag_off(1, EVENT.LeeroyInvasionDone)
    obj.enable_treasure(1301601)

    # PINWHEEL

    run_event(11300880)  # Sets up clones: disable health bar, disable, and make immortal.
    sound.disable_map_sound(1303800)
    # Dead.
    skip_if_event_flag_off(4, EVENT.PinwheelDead)
    obj.disable(1301990)
    sfx.delete_map_sfx(1301991, False)
    run_event(11305392)
    skip(32)

    # Alive.
    run_event(11305390)
    run_event(11305391)
    run_event(11305393)
    run_event(11305392)  # Plays cutscene once per load (which seems to be always).
    run_event(11300001)  # Pinwheel dies. Makes ladder appear and kills clones by running 880 again.
    run_event(11305394)
    run_event(11305395)
    run_event(11300882)  # Synchronizes boss warp flags from below with other players (because they're random).
    run_event(11305396)  # Pinwheel warps to one of seven random locations on event 600 (animation 3008).
    run_event(11305397)  # Spawns two of fourteen random clones. Keeps trying until it finds an inactive pair.
    run_event(11305398)
    run_event(11305250)

    # Clones appear in pairs when their respective trigger flags are enabled (last arg).
    run_event_with_slot(11305350, 0, args=(11305251, 11305252, 1300801, 1300802, 1302600, 1302612, 11305300))
    run_event_with_slot(11305350, 1, args=(11305253, 11305254, 1300803, 1300804, 1302601, 1302611, 11305301))
    run_event_with_slot(11305350, 2, args=(11305255, 11305256, 1300805, 1300806, 1302602, 1302610, 11305302))
    run_event_with_slot(11305350, 3, args=(11305257, 11305258, 1300807, 1300808, 1302603, 1302609, 11305303))
    run_event_with_slot(11305350, 4, args=(11305259, 11305260, 1300809, 1300810, 1302604, 1302608, 11305304))
    run_event_with_slot(11305350, 5, args=(11305261, 11305262, 1300811, 1300812, 1302605, 1302607, 11305305))
    run_event_with_slot(11305350, 6, args=(11305263, 11305264, 1300813, 1300814, 1302606, 1302606, 11305306))

    for clone in range(14):
        run_event_with_slot(11305370, clone, args=(1300800 + clone + 1, 11305250 + clone + 1))

    # Non-respawning enemies (not including normal Necromancers).
    run_event_with_slot(11300850, 0, args=(1300100, 0))
    run_event_with_slot(11300850, 1, args=(1300120, 0))
    run_event_with_slot(11300850, 2, args=(CHR.MassOfSouls, 0))
    run_event_with_slot(11300850, 5, args=(CHR.CowardNecromancer, 0))
    run_event_with_slot(11300850, 6, args=(1300500, 33003000))  # Crystal Lizard.
    run_event_with_slot(11300850, 7, args=(1300501, 33003000))  # Crystal Lizard.
    run_event_with_slot(11300850, 8, args=(1300300, 0))  # Haunting Semblance.


def event50():
    """ NPC constructor. """
    header(50, 0)

    run_event(11302006)  # Reaper/Ransacker Rune corpse disabled if Bell Gargoyles aren't dead.

    # (NEW) DEPRAVED APOSTATE (invasion)

    chr.humanity_registration(CHR.DepravedApostate, 8366)
    run_event(11305630)
    run_event(11300810)

    # PALADIN LEEROY (Summon)

    chr.humanity_registration(CHR.PaladinLeeroySummon, 8948)
    run_event(11305025)
    run_event(11305027)

    # VAMOS

    run_event_with_slot(11300510, 0, args=(CHR.Vamos, EVENT.VamosHostile))
    run_event_with_slot(11300520, 0, args=(CHR.Vamos, 1340, 1343, EVENT.VamosDead))
    run_event_with_slot(11305061, args=(CHR.Vamos,))

    # PATCHES

    chr.humanity_registration(CHR.Patches, 8478)
    skip_if_event_flag_on(2, EVENT.PatchesHostile)
    skip_if_event_flag_range_not_all_off(1, 1620, 1621)
    chr.disable(CHR.Patches)
    run_event_with_slot(11300510, 1, args=(CHR.Patches, EVENT.PatchesHostile))
    run_event_with_slot(11300531, 0, args=(CHR.Patches, 1628))
    run_event_with_slot(11300530, 0, args=(CHR.Patches, 1620, 1631, 1621))
    # Patches moves to Tomb when Rhea does, or when Pinwheel is killed.
    run_event_with_slot(11300533, 0, args=(CHR.Patches, 1620, 1631, 1623))
    run_event(11300592)  # First bridge is rotated before Patches tricks you.
    run_event(11300593)  # Patches rotates the bridge underneath you.


def event11305004():
    header(11305004, 1)
    if_entity_targeting(1, 1300281, CHR.Player)
    if_entity_has_special_effect(1, CHR.Player, 4130)  # in coffin
    if_condition_true(0, 1)
    chr.clear_ai_target_list(1300281)
    chr.replan_ai(1300281)


def event11305005():
    header(11305005, 1)
    if_entity_targeting(1, 1300282, CHR.Player)
    if_entity_has_special_effect(1, CHR.Player, 4130)  # in coffin
    if_condition_true(0, 1)
    chr.clear_ai_target_list(1300282)
    chr.replan_ai(1300282)


def event11300150():
    """ Profane Semblance drops from the ceiling. Now also disappears. """
    header(11300150, 1)
    skip_if_this_event_off(2)
    obj.end_destruction(1301020, 1)
    end()
    chr.disable(1300300)
    chr.disable_ai(1300300)
    if_player_inside_region(0, 1302020)
    chr.enable(1300300)
    chr.enable_ai(1300300)
    obj.destroy(1301020, 1)
    sound.play_sound_effect(1301020, SoundType.a_ambient, 303600000)


def event11300800():
    """ Big Necromancer/skeleton manager. """
    header(11300800, 1)

    flag.enable(11305200)

    flag.enable(11305040)

    # Necromancer in large cave flees.
    run_event_with_slot(11305050, 1, args=(11305040, 1300120, 1302202, 1092616192))
    run_event_with_slot(11305050, 2, args=(11305051, 1300120, 1302203, 1092616192))
    run_event_with_slot(11305050, 3, args=(11305052, 1300120, 1302204, 1092616192))
    run_event_with_slot(11305050, 4, args=(11305053, 1300120, 1302205, 1092616192))

    # Prevent certain Necromancers (and their Skeletons) from respawning.
    for slot, necro in enumerate((1300100, 1300120, 1300180, 1300220)):
        run_event_with_slot(11300801, slot, args=(necro, necro + 1, necro + 2))

    SkeletonNecromancers = (1300100, 1300120, 1300140, 1300150, 1300160, 1300170,
                            1300190, 1300200, 1300210, 1300220, 1300230, 1300240)

    # Tie immortality and assembly triggers of pairs of skeletons to Necromancers.
    assembly_slot = 0
    for necro in SkeletonNecromancers:
        d = 12.0 if necro == 1300200 else 9.0  # Skeletons of Necromancer on first spiked bridge have a longer range.
        run_event_with_slot(11305070, assembly_slot, args=(necro, necro + 1, d), arg_types='iif')  # Assembly trigger
        run_event_with_slot(11305100, assembly_slot, args=(necro, necro + 1))  # Immortality
        assembly_slot += 1
        run_event_with_slot(11305070, assembly_slot, args=(necro, necro + 2, d), arg_types='iif')  # Assembly trigger
        run_event_with_slot(11305100, assembly_slot, args=(necro, necro + 2))  # Immortality
        assembly_slot += 1

    # Tie immortality of giant skeleton to a Necromancer.
    run_event_with_slot(11305070, assembly_slot, args=(CHR.GiantSkeletonNecromancer, CHR.GiantSkeleton))
    run_event_with_slot(11305100, assembly_slot, args=(CHR.GiantSkeletonNecromancer, CHR.GiantSkeleton))

    # Wisps now generated from Mass of Souls in the pit.
    Wisps = (1300291, 1300292, 1300293, 1300294, 1300295)
    run_event_with_slot(11305400, 0, args=(CHR.MassOfSouls, Wisps[0], 1, 11300800))
    run_event_with_slot(11305400, 1, args=(CHR.MassOfSouls, Wisps[1], 2, 11305400))
    run_event_with_slot(11305400, 2, args=(CHR.MassOfSouls, Wisps[2], 3, 11305401))
    run_event_with_slot(11305400, 3, args=(CHR.MassOfSouls, Wisps[3], 4, 11305402))
    run_event_with_slot(11305400, 4, args=(CHR.MassOfSouls, Wisps[4], 5, 11305403))

    # Disable Wisps after explosion.
    for slot, wisp in enumerate((291, 292, 293, 294, 295, 353, 354, 355, 356, 357, 360, 363)):
        run_event_with_slot(11305210, slot, args=(1300000 + wisp,))


def event11300801():
    """ Prevent a Necromancer and its Skeletons from respawning. """
    header(11300801, 1)
    necromancer, skeleton_1, skeleton_2 = define_args('iii')
    skip_if_this_event_slot_off(7)
    chr.disable(necromancer)
    chr.disable(skeleton_1)
    chr.disable(skeleton_2)
    chr.kill(necromancer, False)
    chr.kill(skeleton_1, False)
    chr.kill(skeleton_2, False)
    end()

    if_entity_dead(0, necromancer)
    end()


def event11305070():
    """ Skeletons animate when you approach their (living) Necromancer. """
    header(11305070, 2)
    necromancer, skeleton, distance = define_args('iif')
    skip_if_this_event_slot_off(2)
    chr.set_standby_animation_settings_to_default(skeleton)
    end()
    if_entity_alive(1, necromancer)
    if_player_within_distance(1, necromancer, distance)
    if_condition_true(0, 1)
    wait_random_seconds(0.1, 1.5)
    chr.set_standby_animation_settings(skeleton, cancel_animation=9061)


def event11305100():
    """ Skeletons now immediately die after you kill their Necromancer. """
    header(11305100, 2)
    necromancer, skeleton = define_args('ii')

    skip_if_this_event_slot_off(2)
    chr.cancel_special_effect(skeleton, 5451)
    end()

    # If Necromancer is dead already (e.g. shot from far away), disable the skeleton.
    if_entity_health_less_than_or_equal(1, necromancer, 0.0)
    skip_if_condition_false(3, 1)
    chr.disable(skeleton)
    chr.kill(skeleton, False)
    end()

    # Wait for Necromancer to die to kill immortal skeleton.
    chr.enable_immortality(skeleton)
    if_entity_health_less_than_or_equal(0, necromancer, 0.0)
    chr.cancel_special_effect(skeleton, 5451)
    chr.disable_immortality(skeleton)
    chr.kill(skeleton, False)


def event11305400():
    """ Wisps are spawned by the Mass of Souls. """
    header(11305400, 1)
    mass, wisp, command, required_flag = define_args('iiii')

    skip_if_this_event_slot_off(3)
    if_entity_backread_enabled(0, mass)
    chr.ai_instruction(mass, command, 0)
    end()

    chr.disable(wisp)
    if_entity_backread_enabled(1, mass)
    if_has_tae_event(1, mass, 300)
    if_event_flag_on(1, required_flag)
    if_condition_true(0, 1)
    chr.ai_instruction(mass, command, 0)
    chr.enable(wisp)
    warp.warp_and_copy_floor(wisp, 'character', mass, 100, copy_floor_of_entity_id=mass)
    anim.force_animation(wisp, 8300, wait_for_completion=True)
    if_does_not_have_tae_event(0, mass, 300)
    end()


def event11300592():
    """ First bridge starts rotated on map load if Patches hasn't tricked you yet. """
    header(11300592)
    if_in_world_area(1, 13, 0)  # Give Patches time to move on when map loads, if he's leaving.
    if_host(1)
    if_event_flag_on(1, EVENT.PatchesBeforeBridgeTrick)
    if_event_flag_off(1, 11300593)  # Patches hasn't tricked you yet.
    if_event_flag_off(1, EVENT.FirstBridgeSafe)  # Bridge is spike side up.
    # if_player_inside_region(1, 1302000)
    if_condition_true(0, 1)
    flag.enable(EVENT.FirstBridgeSafe)  # Bridge is rotated (e.g. if you reload now).
    flag.enable(11300592)
    obj.start_object_activation(1301002, 3011, -1)  # Patches is close enough for the ObjAct to "grab" him.


def event11300593():
    """ Patches rotates the bridge back to spikes as you cross. """
    header(11300593, 0)
    if_host(1)
    if_event_flag_on(1, EVENT.PatchesBeforeBridgeTrick)
    if_event_flag_on(1, 11300592)
    if_event_flag_on(1, EVENT.FirstBridgeSafe)
    if_player_inside_region(1, 1302001)
    if_condition_true(0, 1)
    flag.enable(11300593)  # Trick is done.
    obj.start_object_activation(1301002, 3012, -1)  # Patches is close enough for the ObjAct to "grab" him.


def event11302000():
    """ Bonfire Mimic. Hidden fairly deep, like the real bonfire. Only one slot. """
    header(11302000, 1)
    mimic_bonfire, baby_skeleton = define_args('ii')

    # NOTE: Disabled due to SFX bug.

    # Bonfire mimic killed, disable it.
    # skip_if_this_event_slot_off(4)
    obj.disable(mimic_bonfire)
    chr.disable(baby_skeleton)
    chr.kill(baby_skeleton, False)
    end()

    # Otherwise, trigger the explosion, and wait for the baby skeleton to die.
    chr.disable_gravity(baby_skeleton)
    chr.disable_collision(baby_skeleton)
    if_action_button_state(0, Category.object, mimic_bonfire, 180.0, -1, 2.0, TEXT.LightBonfire)
    chr.rotate_to_face_entity(CHR.Player, mimic_bonfire)
    anim.force_animation(CHR.Player, ANIM.TouchMimicBonfire)
    wait(2.2)
    sound.play_sound_effect(CHR.Player, SoundType.c_character_motion, SOUND.SkeletonAssembly)
    wait(0.5)
    anim.force_animation(baby_skeleton, 9060)
    wait(0.63)
    sfx.create_oneoff_sfx(Category.character, baby_skeleton, 1, 15374)
    sound.play_sound_effect(baby_skeleton, SoundType.v_voice, SOUND.BonfireMimic)
    obj.disable(mimic_bonfire)
    chr.set_standby_animation_settings_to_default(baby_skeleton)
    chr.enable_ai(baby_skeleton)
    chr.enable_gravity(baby_skeleton)
    chr.enable_collision(baby_skeleton)

    if_entity_dead(0, baby_skeleton)
    end()


def event11302001():
    """ Interact with Sen's crypt and return Pale Eye Orb. """
    header(11302001, 1)
    chr.disable(CHR.ThirdPaleDemon)

    skip_if_event_flag_off(3, EVENT.PaleEyeOrbReturned)
    chr.disable(CHR.FirstPaleDemon)
    chr.disable(CHR.SecondPaleDemon)
    end()

    # if_entity_dead(0, CHR.HauntingSemblance)  # This requirement doesn't really make sense and will confuse players.

    if_player_does_not_have_good(1, GOOD.PaleEyeOrb)
    if_action_button_state(1, 'character', CHR.SensCryptInteraction, 180.0, -1, 2.0, TEXT.Examine)
    if_condition_true(-1, 1)
    if_player_has_good(2, GOOD.PaleEyeOrb)
    if_action_button_state(2, 'character', CHR.SensCryptInteraction, 180.0, -1, 2.0, TEXT.ReturnPaleEyeOrb)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    skip_if_condition_true_finished(3, 2)
    message.dialog(TEXT.PaleOrbAlreadyStolen, ButtonType.ok_cancel, 6, CHR.SensCryptInteraction, 4.0)
    wait(3.0)
    restart()

    item.remove_items_from_player(ItemType.good, GOOD.PaleEyeOrb, 0)
    message.dialog(TEXT.ReturnedPaleEyeOrb, ButtonType.ok_cancel, 6, CHR.SensCryptInteraction, 4.0)
    flag.enable(EVENT.PaleEyeOrbReturned)
    chr.enable(CHR.ThirdPaleDemon)
    chr.set_team_type(CHR.ThirdPaleDemon, TeamType.ally)
    chr.set_team_type(CHR.FirstPaleDemon, TeamType.ally)
    chr.set_team_type(CHR.SecondPaleDemon, TeamType.ally)

    if_entity_attacked_by(-1, CHR.ThirdPaleDemon, CHR.Player)
    if_entity_attacked_by(-1, CHR.FirstPaleDemon, CHR.Player)
    if_entity_attacked_by(-1, CHR.SecondPaleDemon, CHR.Player)
    if_condition_true(0, -1)
    chr.set_team_type(CHR.ThirdPaleDemon, TeamType.enemy)
    chr.set_team_type(CHR.FirstPaleDemon, TeamType.enemy)
    chr.set_team_type(CHR.SecondPaleDemon, TeamType.enemy)


def event11305392():
    """ Pinwheel behavior. Now just kicks off troll event. """
    header(11305392, 1)

    chr.disable(CHR.FakePinwheel)
    chr.disable(CHR.Pinwheel)

    # If Pinwheel is dead, kill him and fake Pinwheel and end.
    skip_if_event_flag_off(3, EVENT.PinwheelDead)
    chr.kill(CHR.Pinwheel)
    chr.kill(CHR.FakePinwheel)
    end()

    # Player enters boss room.
    if_event_flag_off(1, EVENT.PinwheelDead)
    if_host(1)
    if_player_inside_region(1, 1302999)
    if_condition_true(0, 1)

    # Opening cutscene and 'troll' fake-out death event.
    skip_if_event_flag_on(21, EVENT.FakePinwheelDead)
    skip_if_multiplayer(2)
    cutscene.play_cutscene_to_player(130000, CutsceneType.skippable, CHR.Player)
    skip(1)
    cutscene.play_cutscene_to_player(130000, CutsceneType.unskippable, CHR.Player)
    wait_frames(1)
    chr.enable(CHR.FakePinwheel)
    flag.enable(11300005)  # Don't know what this does, but it probably means 'Pinwheel challenged' so I'll leave it.
    skip_if_client(1)
    chr.set_network_update_authority(CHR.FakePinwheel, UpdateAuthority.forced)
    boss.enable_boss_health_bar(CHR.FakePinwheel, TEXT.PinwheelName)
    flag.enable(11305392)  # To start music, etc.
    if_entity_health_less_than_or_equal(0, CHR.FakePinwheel, 0.0)
    flag.disable(11305392)  # Battle paused.
    boss.disable_boss_health_bar(CHR.FakePinwheel, TEXT.PinwheelName)
    wait(1.0)
    message.banner(TextBannerType.boss_defeated)
    sound.play_sound_effect(CHR.FakePinwheel, SoundType.s_sfx, SOUND.BossDeath)
    if_entity_dead(0, CHR.FakePinwheel)
    sound.disable_map_sound(1303800)  # Stop music manually here.
    flag.enable(EVENT.FakePinwheelDead)
    wait(5.0)  # Wait extra long for the one-time transition.

    # The real battle begins in 11305399.
    flag.enable(11305392)  # Music will begin.
    wait(5.0)
    skip_if_client(1)
    chr.set_network_update_authority(CHR.Pinwheel, UpdateAuthority.forced)
    boss.enable_boss_health_bar(CHR.Pinwheel, TEXT.PinwheelName)
    run_event(11305399)


def event11300001():
    """ Pinwheel dies (for real). """
    header(11300001)
    if_entity_health_less_than_or_equal(0, CHR.Pinwheel, 0.0)
    wait(1.0)
    sound.play_sound_effect(CHR.Pinwheel, SoundType.s_sfx, SOUND.BossDeath)
    if_entity_dead(0, CHR.Pinwheel)
    flag.enable(EVENT.PinwheelDead)
    boss.kill_boss(CHR.Pinwheel)
    obj.disable(1301990)
    sfx.delete_map_sfx(1301991, True)
    map.register_ladder(11300016, 11300017, 1301143)
    run_event(11300880)


def event11305399():
    """ Main Pinwheel battle loop. """
    header(11305399)

    # Start off by spawning eight clones *without* Pinwheel being present.
    skip_if_event_flag_on(4, 11305399)
    run_event_with_slot(11305360, 0, args=(11305251, 11305252, 1300801, 1300802, 1302602, 1302603, 11305300))
    run_event_with_slot(11305360, 1, args=(11305253, 11305254, 1300803, 1300804, 1302604, 1302605, 11305301))
    run_event_with_slot(11305360, 2, args=(11305255, 11305256, 1300805, 1300806, 1302607, 1302608, 11305302))
    run_event_with_slot(11305360, 3, args=(11305257, 11305258, 1300807, 1300808, 1302609, 1302612, 11305303))

    # You have to kill at least 5/8 clones for Pinwheel to appear.
    wait(5.0)
    if_number_true_flags_in_range_less_than_or_equal(0, 11305250, 11305258, 3)

    chr.enable(CHR.Pinwheel)
    anim.force_animation(CHR.Pinwheel, 7000, wait_for_completion=True)  # Real Pinwheel fades in.

    # Respawn all clones after 40-60 seconds.
    wait_random_seconds(40, 60)
    run_event(11305398)
    restart()


def event11305394():
    """ Enable Pinwheel music. Now triggers in fake OR real Pinwheel fights. """
    header(11305394)
    network.disable_sync()
    if_event_flag_off(1, EVENT.PinwheelDead)
    if_event_flag_on(1, 11305392)
    skip_if_host(1)
    if_event_flag_on(1, 11305391)
    if_condition_true(0, 1)
    sound.enable_map_sound(1303800)
    # If Fake Pinwheel is alive, we wait for him to die, then restart this event so the music can start again.
    end_if_event_flag_on(EVENT.FakePinwheelDead)
    if_event_flag_on(0, EVENT.FakePinwheelDead)
    restart()  #


def event11305395():
    """ Disable Pinwheel music. (Only applies to true battle.) """
    header(11305395)
    network.disable_sync()
    if_event_flag_on(1, EVENT.PinwheelDead)
    if_event_flag_on(1, 11305394)
    if_condition_true(0, 1)
    sound.disable_map_sound(1303800)


def event11305396():
    """ Pinwheel warps to one of seven random locations. """
    header(11305396)

    if_has_tae_event(0, CHR.Pinwheel, 600)  # Triggered by animation 3008.
    chr.disable(CHR.Pinwheel)
    flag.disable_chunk(11305320, 11305326)
    skip_if_client(2)
    chr.set_network_update_authority(CHR.Pinwheel, UpdateAuthority.forced)
    flag.enable_random_in_chunk(11305320, 11305326)  # Seven possible flags.
    flag.enable(11305329)  # Not sure what this does.

    # Wait for 11305329 to disable somehow, or a max of five seconds.
    if_event_flag_off(-1, 11305329)
    if_time_elapsed(-1, 5.0)
    if_condition_true(0, -1)

    wait_random_seconds(10.0, 15.0)  # Warp interval extended.
    chr.enable(CHR.Pinwheel)
    # Warp Pinwheel to whichever location was flagged.
    for warp_flag, warp_region in zip(
            range(11305320, 11305327), (1302600, 1302602, 1302604, 1302605, 1302606, 1302608, 1302612)):
        skip_if_event_flag_off(1, warp_flag)
        warp.short_warp(CHR.Pinwheel, 'region', warp_region, -1)
    wait_frames(1)
    chr.enable(CHR.Pinwheel)
    anim.force_animation(CHR.Pinwheel, 7000, wait_for_completion=True)
    restart()


def event11305397():
    """ Enable trigger flag for a pair of currently inactive clones when Pinwheel says so. """
    header(11305397)
    end_if_client()

    skip_if_event_flag_on(4, 11305310)
    if_event_flag_on(1, 11305392)
    if_event_flag_on(1, 11300000)
    if_has_tae_event(1, CHR.Pinwheel, 700)  # Clone spawn, triggered by animation 3004.
    if_condition_true(0, 1)
    flag.enable(11305310)  # Searching for location.

    flag.disable_chunk(11305300, 11305306)
    flag.enable_random_in_chunk(11305300, 11305306)
    # Clone search is terminated when it finds two clones that are both inactive.
    for clone_flag, first_clone_flag in zip(range(11305300, 11305307),
                                            range(11305251, 11305264, 2)):
        skip_if_event_flag_off(2, clone_flag)
        skip_if_event_flag_range_not_all_off(1, first_clone_flag, first_clone_flag + 1)
        flag.disable(11305310)

    # Restart and try with new random flag if search failed.
    restart_if_event_flag_on(11305310)
    if_event_flag_on(0, 11305380)  # Loop has run once.
    if_does_not_have_tae_event(0, CHR.Pinwheel, 700)  # Wait for next spawning event once trigger ends.
    restart()


def event11305398():
    """ Spawn eight Pinwheel clones at once. Now run at will by 5399, the main battle loop manager. """
    header(11305398)

    chr.ai_instruction(CHR.Pinwheel, 1, 1)
    chr.replan_ai(CHR.Pinwheel)  # Stop Pinwheel from spawning clones.

    for slot, (clone, clone_flag) in enumerate(zip(range(1300801, 1300815), range(11305251, 11305265))):
        run_event_with_slot(11305330, slot, args=(clone, clone_flag))  # Instruct all clones to disappear.
    if_event_flag_range_all_off(0, 11305251, 11305264)  # Wait for all clones to disappear.

    chr.ai_instruction(CHR.Pinwheel, 2, 1)
    chr.replan_ai(CHR.Pinwheel)  # Instruct Pinwheel to use clone spawn (3004).

    if_has_tae_event(1, CHR.Pinwheel, 700)  # During animation 3004.
    if_condition_true(0, 1)

    chr.ai_instruction(CHR.Pinwheel, 1, 1)
    chr.replan_ai(CHR.Pinwheel)  # Stop Pinwheel from spawning clones.

    # Summon eight clones.
    run_event_with_slot(11305360, 0, args=(11305251, 11305252, 1300801, 1300802, 1302602, 1302603, 11305300))
    run_event_with_slot(11305360, 1, args=(11305253, 11305254, 1300803, 1300804, 1302604, 1302605, 11305301))
    run_event_with_slot(11305360, 2, args=(11305255, 11305256, 1300805, 1300806, 1302607, 1302608, 11305302))
    run_event_with_slot(11305360, 3, args=(11305257, 11305258, 1300807, 1300808, 1302609, 1302612, 11305303))

    # Summon four more clones if Pinwheel is below 30% health.
    if_entity_health_greater_than(7, CHR.Pinwheel, 0.3)
    end_if_condition_true(7)
    run_event_with_slot(11305360, 4, args=(11305259, 11305260, 1300809, 1300810, 1302600, 1302610, 11305304))
    run_event_with_slot(11305360, 5, args=(11305261, 11305262, 1300811, 1300812, 1302601, 1302611, 11305305))


def event11305330():
    """ Instruct clone to disappear. """
    header(11305330)
    clone, clone_flag = define_args('ii')
    chr.ai_instruction(clone, 1, 1)
    chr.replan_ai(clone)
    if_event_flag_off(0, clone_flag)
    chr.ai_instruction(clone, -1, 1)
    chr.replan_ai(clone)


def event11305350():
    """ Pair of clones triggered whenever a trigger flag is enabled (by Pinwheel's instruction in 5397). """
    header(11305350)
    clone_1_flag, clone_2_flag, clone_1, clone_2, clone_1_region, clone_2_region, trigger_flag = define_args('iiiiiii')

    if_host(1)
    if_event_flag_off(1, 11305310)  # Search has ended.
    if_event_flag_on(1, trigger_flag)
    if_condition_true(0, 1)
    wait_for_network_approval(3.0)

    flag.disable(trigger_flag)
    chr.set_special_effect(clone_1, 5450)
    chr.set_special_effect(clone_2, 5450)
    warp.short_warp(clone_1, 'region', clone_1_region, -1)
    warp.short_warp(clone_2, 'region', clone_2_region, -1)
    chr.enable(clone_1)
    chr.enable(clone_2)
    chr.replan_ai(clone_1)
    chr.replan_ai(clone_2)
    anim.force_animation(clone_1, 7000)
    anim.force_animation(clone_2, 7000)
    flag.enable(clone_1_flag)
    flag.enable(clone_2_flag)
    event.restart_event_id(11305250)  # Reset AI of all Pinwheels.
    restart()


def event11305360():
    """ Pair of clones triggered once when this event is called, unconditionally. """
    header(11305360)
    clone_1_flag, clone_2_flag, clone_1, clone_2, clone_1_region, clone_2_region, trigger_flag = define_args('iiiiiii')

    flag.disable(trigger_flag)  # Doesn't actually do anything here.
    chr.set_special_effect(clone_1, 5450)
    chr.set_special_effect(clone_2, 5450)
    warp.short_warp(clone_1, 'region', clone_1_region, -1)
    warp.short_warp(clone_2, 'region', clone_2_region, -1)
    chr.enable(clone_1)
    chr.enable(clone_2)
    chr.replan_ai(clone_1)
    chr.replan_ai(clone_2)
    anim.force_animation(clone_1, 7000)
    anim.force_animation(clone_2, 7000)
    flag.enable(clone_1_flag)
    flag.enable(clone_2_flag)
    event.restart_event_id(11305250)  # Reset AI of all Pinwheels.


def event11305370():
    """ Clone disappears, or Pinwheel dies. """
    header(11305370)
    clone, clone_flag = define_args('ii')
    if_event_flag_on(1, clone_flag)
    if_has_tae_event(1, clone, 710)
    if_entity_health_less_than_or_equal(2, CHR.Pinwheel, 0.0)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)
    wait_for_network_approval(3.0)
    skip_if_condition_true_finished(3, 1)
    chr.ai_instruction(clone, 1, 1)
    chr.replan_ai(clone)
    if_has_tae_event(0, clone, 710)
    chr.set_network_update_rate(clone, True, CharacterUpdateRate.always)
    chr.reset_animation(clone, disable_interpolation=True)
    chr.disable(clone)
    flag.disable(clone_flag)
    end_if_condition_true_finished(2)
    event.restart_event_id(11305250)  # Kill all clones.
    restart_if_event_flag_off(clone_flag)


def event11305250():
    """ Reset all Pinwheel AIs (normal and clones). """
    header(11305250)
    if_event_flag_on(0, 11305392)
    for pinwheel in range(1300800, 1300815):
        chr.ai_event(pinwheel, 0, 0, 11305251, 11305264)
    for pinwheel in range(1300800, 1300815):
        chr.replan_ai(pinwheel)
    if_entity_dead(0, CHR.Pinwheel)
    end()


def event11300880():
    """ Initialize (or kill) or Pinwheel clones. """
    header(11300880, 1)
    for clone in PinwheelClones:
        chr.disable_health_bar(clone)
    for clone in PinwheelClones:
        chr.disable(clone)
    skip_if_event_flag_on(14, EVENT.PinwheelDead)
    for clone in PinwheelClones:
        chr.enable_immortality(clone)
    end_if_event_flag_off(EVENT.PinwheelDead)
    for clone in PinwheelClones:
        chr.kill(clone, False)


def event11305630():
    """ New NPC invasion: Depraved Apostate. """
    header(11305630)
    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11305631)
    end_if_event_flag_on(1198)  # Petrus dies (before killing Rhea).
    end_if_event_flag_on(1196)  # Petrus dies (after killing Rhea).
    # No longer requires Pinwheel to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 11300810)
    if_event_flag_off(1, 1198)  # Re-checked because m13_00 may have loaded before you killed Petrus in the graveyard.
    if_event_flag_off(1, 1196)
    skip_if_this_event_on(1)
    if_player_inside_region(1, REGION.DepravedApostateTrigger)
    if_condition_true(0, 1)
    message.place_summon_sign(SummonSignType.black_eye_sign, 6850, REGION.DepravedApostateSignPoint, 11305631, 11305632)
    wait(20.0)
    restart()


def event11300810():
    """ Depraved Apostate invader dies. """
    header(11300810, 1)

    skip_if_host(3)
    if_event_flag_on(1, 11305031)
    if_event_flag_off(1, 11305032)
    skip_if_condition_true(1, 1)
    chr.disable(CHR.DepravedApostate)

    end_if_this_event_on()

    if_entity_dead(0, CHR.DepravedApostate)
    flag.enable(11300810)


def event11300100():
    """ Floor pieces break. Now also broken by Crystal Lizards. """
    header(11300100)
    broken_flag, trigger_region, floor, break_sound = define_args('iiii')
    skip_if_this_event_slot_off(2)
    obj.disable(floor)
    end()

    if_event_flag_off(1, broken_flag)
    if_player_inside_region(-1, trigger_region)
    if_entity_inside_area(2, 1300500, trigger_region)
    if_player_within_distance(2, 1300500, 5.0)
    if_condition_true(-1, 2)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    obj.destroy(floor, 1)
    sfx.create_oneoff_sfx(Category.object, floor, -1, 130000)
    sound.play_sound_effect(floor, SoundType.o_object, break_sound)


def event11302003():
    """ Bonewheel near fake bonfire disabled if it's still there. """
    header(11302003, 1)
    end_if_event_flag_on(11302000)
    chr.disable(1300285)


def event11302006():
    """ Corpse near bonfire mimic disabled if Bell Gargoyles aren't dead. """
    header(11302006)
    end_if_event_flag_on(EVENT.BellGargoylesDead)
    obj.disable(1301600)
    obj.disable_treasure(1301600)


def event11300531():
    """ Patches dies in the Catacombs. Now awards Pale Eye Orb. """
    header(11300531)
    patches, new_flag = define_args('ii')
    if_event_flag_on(1, 1620)
    if_entity_health_less_than_or_equal(1, patches, 0.0)
    if_event_flag_on(2, 1621)
    if_entity_health_less_than_or_equal(2, patches, 0.0)
    if_event_flag_on(3, new_flag)
    if_this_event_on(3)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(0, -1)

    flag.disable(1627)
    flag.enable(new_flag)
    item.award_item_to_host_only(ITEMLOT.PaleEyeOrb)
    end_if_condition_false_finished(3)
    chr.drop_mandatory_treasure(patches)


def event11302004():
    """ Vamos is given the Chthonic Spark, and will drop it when killed (by the player). """
    header(11302004)
    end_if_this_event_on()

    if_event_flag_on(0, EVENT.VamosGivenChthonicSpark)
    flag.disable(EVENT.VamosNoChthonicSparkDrop)


def event11302005():
    """ Jeremiah kills Vamos for the Chthonic Spark. """
    header(11302005, 1)
    chr.disable(CHR.Jeremiah)

    if_event_flag_on(1, EVENT.VamosGivenChthonicSpark)
    if_event_flag_off(1, EVENT.VamosDead)
    if_event_flag_on(-1, EVENT.JeremiahInRuins)
    if_event_flag_on(-1, EVENT.JeremiahImpatient)
    if_event_flag_on(-1, EVENT.JeremiahInIzalith)
    if_condition_true(1, -1)
    end_if_condition_false(1)  # Only checked on load.

    chr.enable(CHR.Jeremiah)
    chr.disable_ai(CHR.Jeremiah)

    if_player_inside_region(-2, REGION.JeremiahTrigger)
    if_player_within_distance(-2, CHR.Jeremiah, 3.0)
    if_entity_attacked_by(-2, CHR.Jeremiah, CHR.Player)
    if_condition_true(0, -2)

    flag.enable(EVENT.JeremiahStoleFromVamos)
    flag.enable(EVENT.VamosNoChthonicSparkDrop)  # Vamos won't drop the Spark.
    chr.kill(CHR.Vamos)
    flag.disable_chunk(11412050, 11412059)
    flag.enable(EVENT.JeremiahEscaped)
    flag.disable(EVENT.JeremiahNoChthonicSparkDrop)
    chr.enable_ai(CHR.Jeremiah)

    if_entity_health_less_than_or_equal(0, CHR.Jeremiah, 0.0)
    flag.disable(EVENT.JeremiahEscaped)
    flag.enable(EVENT.JeremiahDeadFromPlayer)  # Will satisfy Velka.
    # Jeremiah's set, with fake crown, unlocked with Domnhall.
    flag.disable(11807230)
    flag.disable(11807240)
    flag.disable(11807250)
    flag.disable(11807260)


def event11302040():
    """ Monitors when you've rested at the bonfire for warping. """
    header(11302040)
    if_player_within_distance(1, 1301961, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11302040)


# NOTE: The coffin warp event below hasn't actually changed, but I needed to write it out.

# def event11305000():
#     """ Nito coffin warp. """
#     header(11305000)
#     network.disable_sync()
#     if_singleplayer(1)
#     if_in_world_area(1, 13, 0)
#     if_player_inside_region(1, 1302700)
#     if_event_flag_off(1, EVENT.NitoAwake)
#     if_player_owns_good(1, 109)  # Eye of Death
#     if_condition_true(0, 1)
#
#     wait(30.0)
#
#     restart_if_multiplayer()
#     if_player_inside_region(6, 1302700)
#     restart_if_condition_false(6)
#     if_entity_health_less_than_or_equal(7, CHR.Player, 0.0)
#     restart_if_condition_true(7)
#
#     # This flag is disabled when you use the exit coffin in Nito's room *or* enter the Ritual Grotto.
#     flag.enable(EVENT.CovenantVisit)
#
#     cutscene.play_cutscene_and_warp_player(130020, CutsceneType.skippable, 1312110, 13, 1)
#     cutscene.play_cutscene_to_player(130120, CutsceneType.skippable, CHR.Player)
#     wait_frames(1)
#     obj.enable_activation(1311300, -1)  # Exit coffin from Nito's room.
#     chr.set_standby_animation_settings_to_default(CHR.Player)
#     restart()


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
