
import sys
import inspect
from pydses import *

map_name = 'm14_01_00_00'  # Demon Ruins and Lost Izalith
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'

BASE_FLAG = 11410000
BASE_PART = 1410000


class DEBUG(IntEnum):
    ALL_DISABLED = False

    ELEVATOR = False
    JEREMIAH_IMPATIENT = False
    JEREMIAH_IN_IZALITH = False
    JEREMIAH_FLEEING = False
    CEASELESS_DEAD = False
    CENTIPEDE_DEMON_DEAD = False
    LOST_DAUGHTER_CENTIPEDE_BATTLE_DONE = False
    LOST_DAUGHTER_WITH_SISTER = False
    OPEN_IZALITH_DOOR = False
    GET_EINGYI_FLAME = False
    GET_XANTHOUS_CROWN = False
    BOTH_BED_ORBS_DESTROYED = False
    SIEGMEYER_IN_IZALITH = False
    SOLAIRE_IN_IZALITH = False
    GET_CHTHONIC_SPARK = False
    VELKA_PACT_MADE = False
    GET_OTHER_LORD_SOULS = False


class CHR(IntEnum):
    Player = 10000
    Solaire = 6002
    SolaireHollow = 6004
    SolaireSummon = 6542
    SiegmeyerInIzalith = 6286
    KirkOne = 6560
    KirkTwo = 6561
    LoyalDaughter = 6620
    LostDaughter = 6621
    LostDaughterFightingCentipede = 6623
    ChaosKnight = 6760
    Jeremiah = 6770
    JeremiahDummy = 6771
    JeremiahElevatorDummy = 6772
    JeremiahInSewers = 6773
    RedEyedChaosBug = 1410100
    CeaselessDischarge = 1410600
    CentipedeDemon = 1410700
    BonfireWorm = 1410460
    InsideWallWorm = 1410461  # consider smaller trigger distance
    BoundingDemon = 1410350
    SewerCapra = 1410480


TaurusDemons = (1410450, 1410451)
LavaRockworms = range(1410452, 1410456)
WallHuggers = (1410470, 1410471, 1410472)   # top of staircase, in door tunnel, just inside dome crack
SiegmeyerChaosEaters = (1410410, 1410411)


class TEXT(IntEnum):
    Locked = 10010163
    DeathlessAura = 10010645
    JeremiahBossName = 6770
    IzalithGateClosed = 10010164
    IzalithGateOpens = 10010165
    FireProtection = 10010625
    FireProtectionAlmostOver = 10010626
    OpenedWithMeltedIronKey = 10010866


class SPAWN(IntEnum):
    SanctumBonfire = 1412964
    ArrivalFromTomb = 1412970


class REGION(IntEnum):
    JeremiahFirstBattleTrigger = 1412070
    CeaselessAtLedge = 1412020
    LostDaughterFightingCentipede = 1412850
    CentipedeFightingLostDaughter = 1412851
    CentipedeDemonWaiting = 1412852
    TriggerLostDaughterCentipedeBattle = 1412853
    StopLostDaughterCentipedeBattle = 1412854
    CentipedeDemonAwakens = 1412855
    OutsideCeaselessFog = 1412856
    CentipedeDemonArena = 1412857
    JeremiahOpensIzalithDoor = 1412858
    JeremiahInSewers = 1412859
    JeremiahSewerArena = 1412860
    JeremiahSewerTrigger = 1412861
    SlidingIntoBedArena = 1412862
    JeremiahOnElevator = 1412863
    JeremiahOnElevatorTrigger = 1412864
    CentipedeDemonBattleStartsFromIzalith = 1412865
    CentipedeDemonBattleEndsOutsideDome = 1412866
    CentipedeDemonBattleEndsInIzalith = 1412867
    CentipedeDemonBattleStartsOutsideDome = 1412868
    StopLostDaughterCentipedeBattleBack = 1412870
    TriggerJeremiahOpeningLostIzalith = 1412877
    LostDaughterHidingPlace = 1412878
    CeaselessAtAltar = 1412879


class GOOD(IntEnum):
    MeltedIronKey = 2007
    ChthonicSpark = 813


class HITBOX(IntEnum):
    CeaselessDischargeFog = 1413675
    

class ITEMLOT(IntEnum):
    VelkaGift = 1650  # Ring of Condemnation.
    ChthonicSpark = 2510  # Capricious Thrall rewards.
    OrangeCharredRing = 2671  # But not Callous Chaos Mote.
    XanthousCrown = 6770
    TaurusDemonsReward = 22500200
    BoundingDemonDrop = 34200300
    FirstWallHuggerDrop = 34200400
    SecondWallHuggerDrop = 34200500
    ThirdWallHuggerDrop = 34200600


class EVENT(IntEnum):
    BedOfChaosDead = 10
    SunlightMaggotDead = 800
    QuelanaDead = 1295
    VelkaPactMade = 1910
    CeaselessDischargeDead = 11410900
    CeaselessDischargeKilledByPlayer = 11410902
    CentipedeDemonDead = 11410901
    CeaselessLavaDrained = 11410801
    ArrivalFromTomb = 11312005
    LostIzalithDoorOpened = 11410340
    BedOfChaosBattleStarted = 11415393
    DarkAnorLondo = 11510400
    QuelaagHeartDead = 11402010
    ShortcutElevatorUsuallyActive = 11410411  # unless Jeremiah is fleeing

    LostDaughterAtCeaseless = 11412020
    LostDaughterFightingCentipede = 11412021
    LostDaughterWillHide = 11412022
    LostDaughterIsHiding = 11412023
    LostDaughterWithFairLady = 11412024
    LostDaughterHostile = 11412025  # only happens near Fair Lady, sin can be forgiven
    LostDaughterDead = 11412026  # no drops to worry about

    LostDaughterCentipedeFightOngoing = 11415505
    LostDaughterCentipedeFightDone = 11412030

    JeremiahInRuins = 11412050  # he will attack you in old Firesage room, which then triggers InLostIzalith
    JeremiahImpatient = 11412051  # you can witness him killing Ceaseless (if alive) and entering Lost Izalith
    JeremiahInIzalith = 11412052  # triggered whenever Lost Izalith opens OR if player enters Demon Ruins with Spark
    JeremiahFleeingIzalith = 11412053  # triggered when he takes the Spark from you in sewers or Bed of Chaos battle
    JeremiahEscaped = 11412054  # triggered if Lost Daughter and Quelana can't kill him
    JeremiahDeadFromPlayer = 11412055  # triggered if you kill him in any of the three battles
    JeremiahDeadNearFairLady = 11412056  # triggered after FleeingIzalith if Lost Daughter is with Fair Lady
    JeremiahDeadNearQuelana = 11412057  # triggered after FleeingIzalith if above and below are false and Quelana alive
    JeremiahDeadInQuelaagArena = 11412058  # triggered after FleeingIzalith if Lost Daughter absent and D.Q. active

    JeremiahRuinsBattleDone = 11412060
    JeremiahSewerBattleStarted = 11415342
    JeremiahSewerBattleDone = 11412061
    JeremiahKilledCeaseless = 11412062
    JeremiahOpenedLostIzalith = 11412063
    JeremiahFledOnElevator = 11412064
    JeremiahInBedBattle = 11415389
    JeremiahStoleFromVamos = 11302007

    SolaireHollowInIzalith = 1002
    SolaireSavedInIzalith = 1003
    SolaireHostile = 1004
    SolaireAtSunlightAltar = 1007
    SolaireAtIzalithBonfire = 1009

    SiegmeyerWaitingInIzalith = 1503
    SiegmeyerFightingInIzalith = 1504
    SiegmeyerLeftOutOfBattle = 1505
    SiegmeyerDyingAfterBattle = 1506
    SiegmeyerSurvivedBattle = 1507
    SiegmeyerHostile = 1512
    SiegmeyerDead = 1513
    SiegmeyerVanished = 1514  # disappears after being left out of battle


class ANIM(IntEnum):
    PointUpGesture = 6802
    PointGesture = 6805
    Bow = 6808
    PlayerSpawn = 6950
    SummonFadeIn = 6951
    TouchWall = 7114
    WalkThroughFog = 7410
    LightBonfire = 7698
    GetUpFromBonfire = 7712
    CurledUp = 7816
    CurledUpGettingUp = 7817
    SittingOneKneeUp = 7825
    SittingCrossedLegged = 7830
    SittingCrossedLeggedStraight = 7835
    Crouching = 7840
    KneelingHandsCrossed = 7880
    SittingLegsToSide = 7885
    KneelingDownOneLeg = 7895
    StayKneelingDownOneLeg = 7896
    GettingUpFromKneelingDownOneLeg = 7897
    LiftHandFromKneelingDownOneLeg = 7898
    Death = 6000   # NB: this animation this will literally kill you (after the animation finishes).


def event0():
    """ Constructor. """
    header(0, 0)

    if not DEBUG.ALL_DISABLED:
        if DEBUG.VELKA_PACT_MADE:
            item.award_item_to_host_only(ITEMLOT.VelkaGift)
            flag.enable(EVENT.VelkaPactMade)

        if DEBUG.SIEGMEYER_IN_IZALITH:
            flag.disable(EVENT.SiegmeyerHostile)
            flag.enable(1502)
            flag.enable(11400590)

        if DEBUG.SOLAIRE_IN_IZALITH:
            flag.disable(1000)
            flag.enable(1007)

        if DEBUG.GET_EINGYI_FLAME:
            item.award_item_to_host_only(1290)

        if DEBUG.GET_CHTHONIC_SPARK:
            item.award_item_to_host_only(ITEMLOT.ChthonicSpark)

        if DEBUG.GET_XANTHOUS_CROWN:
            item.award_item_to_host_only(ITEMLOT.XanthousCrown)

        if DEBUG.LOST_DAUGHTER_WITH_SISTER:
            flag.enable(EVENT.LostDaughterWithFairLady)

        if DEBUG.LOST_DAUGHTER_CENTIPEDE_BATTLE_DONE:
            flag.enable(EVENT.LostDaughterCentipedeFightDone)

        if DEBUG.ELEVATOR:
            flag.enable(11410410)

        if DEBUG.OPEN_IZALITH_DOOR:
            flag.enable(11410430)

        if DEBUG.BOTH_BED_ORBS_DESTROYED:
            flag.enable_chunk(11410291, 11410292)

        if DEBUG.CEASELESS_DEAD:
            flag.enable(EVENT.CeaselessDischargeDead)
            flag.enable(EVENT.CeaselessLavaDrained)

        if DEBUG.CENTIPEDE_DEMON_DEAD:
            flag.enable(EVENT.CentipedeDemonDead)

        if DEBUG.JEREMIAH_IMPATIENT:
            flag.disable_chunk(11412050, 11412059)
            flag.enable(EVENT.JeremiahImpatient)
        elif DEBUG.JEREMIAH_IN_IZALITH:
            flag.disable_chunk(11412050, 11412059)
            flag.disable(EVENT.JeremiahFledOnElevator)
            flag.enable(EVENT.JeremiahInIzalith)
        elif DEBUG.JEREMIAH_FLEEING:
            flag.disable_chunk(11412050, 11412059)
            flag.enable(EVENT.JeremiahFleeingIzalith)

        if DEBUG.GET_OTHER_LORD_SOULS:
            item.award_item_to_host_only(2560)
            item.award_item_to_host_only(2630)
            item.award_item_to_host_only(2640)

    # Bed of Chaos bonfire removed, as you could get stuck here without the Chthonic Spark.
    run_event(11412010)  # Wait for Rockworm death to register bonfire.

    obj.disable(1411960)
    # Remaining bonfires (excluding "bonfire" created by Lost Daughter):
    for flag_id, bonfire in zip((984, 968, 960), (1411961, 1411963, 1411964)):
        map.register_bonfire(BASE_FLAG + flag_id, bonfire, 2.0, 180.0, 0)
    run_event(11412080)  # (New) Monitors resting at Sanctum of Chaos bonfire for easy warping.

    # Summon fog walls.
    skip_if_client(14)
    for wall, sfx_id in zip((994, 996, 998, 988, 986, 984, 982), (995, 997, 999, 989, 987, 985, 983)):
        obj.disable(1411000 + wall)
        sfx.delete_map_sfx(1411000 + sfx_id, False)

    # Checkpoint fog walls.
    for wall_gone_flag, wall, sfx_1, sfx_2 in zip((291, 292), (121, 122), (400, 401), (410, 411)):
        skip_if_event_flag_off(3, BASE_FLAG + wall_gone_flag)
        obj.disable(1411000 + wall)
        sfx.delete_map_sfx(1413000 + sfx_1)
        sfx.delete_map_sfx(1413000 + sfx_2)

    # Former golden light wall, now just self-destructs.
    run_event(11410095)

    # (New) Arrival from Tomb of the Giants.
    run_event(11411000)

    # Gravelording.
    for gravelord_event in (5090, 5091, 5092):
        run_event(BASE_FLAG + gravelord_event)

    run_event(11410800)  # Lava drains.
    run_event(11410400)  # Shortcut elevator operation.
    run_event(11410410)  # Enable elevator.
    run_event(11410340)  # Lost Izalith main door.
    run_event(11410341)  # Lost Izalith main door won't open.
    run_event(11410350)  # Sewer ceiling breaks, I think.
    run_event(11410360)  # Illusory wall in lava lake.
    run_event(11415399)  # Player is invincible during slide into Bed of Chaos.
    run_event(11410260)  # "Izalith death assist." Activates a killplane in Bed of Chaos fight. Loops continually.
    run_event(11410200)  # Bed of Chaos central floor destruction (now when both orbs are destroyed).
    for slot, floor_piece, break_sound in zip(range(13), range(1411210, 1411223), range(4620, 4633)):
        # Bed of Chaos surrounding floor destruction (distance <= 8).
        run_event_with_slot(11410201, slot, args=(floor_piece, break_sound * 100000))
    run_event(11410250)  # Bed of Chaos roots are invulnerable until both orbs are destroyed.

    # CEASELESS DISCHARGE

    sound.disable_map_sound(1413801)
    # Already dead:
    skip_if_event_flag_off(4, 11410900)
    run_event(11415372)
    obj.disable(1411790)
    sfx.delete_map_sfx(1411791, False)
    skip(12)
    # Alive:
    for ceaseless_event in (5370, 5371, 5373, 5372, 5374, 5375, 5376, 5377, 5378, 5379, 900, 5500):
        """Notes:
        11415370: Host enters fog.
        11415371: Summon enters fog.
        11415373: Boss entry notification.
        11415372: Enables behavior (includes altar loot trigger). Also controls Lost Daughter.
        11415374: Enables and disables boss music.
        11415375: (New) Boss moves to the ledge when you enter (if not aggressive).
        11415376: Boss clings to cliff near entrance.
        11415377: Boss pulls out its middle arm.
        11415378: Boss moves to arena entrance if already hostile (from altar loot trigger).
        11415379: Boss falls to his death.
        11410900: Boss dies.
        11415500: (New) Lost Daughter appearance. Runs 5501 loop as well.
        """
        run_event(BASE_FLAG + ceaseless_event)
    # Count five arm hits while clinging.
    for slot, check_flag in zip(range(5), (5376, 5310, 5311, 5312, 5313)):
        run_event_with_slot(11415310, slot, args=(BASE_FLAG + check_flag,))

    # XANTHOUS KING JEREMIAH

    # Jeremiah attacks you in the Demon Ruins:
    sound.disable_map_sound(1413803)
    obj.disable(1411410)
    sfx.delete_map_sfx(1411411, False)
    obj.disable(1411412)
    sfx.delete_map_sfx(1411413, False)
    run_event(11412060)
    run_event(11415345)  # Disables Fair Lady, Eingyi, and his maggots when battle begins.

    # Jeremiah attacks you in the Lost Izalith sewers:
    obj.disable(1411890)
    sfx.delete_map_sfx(1411891, False)
    obj.disable(1411892)
    sfx.delete_map_sfx(1411893, False)
    sound.disable_map_sound(1413804)
    run_event(11412061)

    # Jeremiah kills Ceaseless Discharge:
    run_event(11412062)

    # Jeremiah opens the door to Lost Izalith:
    run_event(11412063)

    # Jeremiah flees up the elevator to Quelaag's Domain:
    run_event(11412064)

    # Jeremiah attacks you in the Bed of Chaos battle:
    run_event(11412065)

    # CENTIPEDE DEMON

    run_event(11412030)  # (NEW) Scripted lava lake battle between Centipede Demon and Lost Daughter.
    run_event(11415510)  # (NEW) Lost Daughter gives you a protective flame.
    run_event(11415511)  # (NEW) Lost Daughter's protective flame gives lava resistance for two minutes.

    sound.disable_map_sound(1413802)
    skip_if_event_flag_off(2, EVENT.CentipedeDemonDead)
    run_event(11415382)
    skip(3)
    for centipede_event in (5382, 901, 5386):
        """NOTES:
        11415382: Enable boss behavior. Also loads tail and arm parts, and enables 11415383 and 11415387.
        11410901: Boss dies.
        11415386: Drop Orange Charred Ring when first part (or boss) is killed.
        """
        run_event(BASE_FLAG + centipede_event)

    # BED OF CHAOS

    sound.disable_map_sound(1413800)

    # Already dead:
    skip_if_event_flag_off(4, 10)
    run_event(11415392)
    obj.disable(1411990)
    sfx.delete_map_sfx(1411991, False)
    skip(11)
    # Alive:
    for bed_event in (5390, 5391, 5393, 5392, 1, 5394, 5395, 5396, 5397, 5398, 5300):
        """NOTES:
        11415390: Player enters boss fog.
        11415391: Summon enters boss fog.
        11415393: Boss entry notification.
        11415392: Enable boss behavior. Also loads tail and arm parts.
        11410001: Boss dies (when bug dies). Enables flag 10, which grants Life Soul reward.
        11415394: Enable boss music.
        11415395: Disable boss music.
        11415396: Cutscene played and phase flags changed whenever an orb is destroyed.
        11415397: Bug invincibility disabled when both orbs are destroyed. Also kills components when bug is killed.
        11415398: AI changes when phase changes.
        11415300: Orb destruction (map SFX deleted).
        """
        run_event(BASE_FLAG + bed_event)

    for slot, (wall_hugger, dead_flag) in enumerate(zip(WallHuggers, range(11412005, 11412008))):
        # (NEW) Parasitic Wall Hugger deaths.
        run_event_with_slot(11412000, slot, args=(wall_hugger, dead_flag))

    run_event(11412070)  # (NEW) Taurus Demons aggro together.
    run_event(11412040)  # (NEW) Random red-eyed Chaos Bug location (replaces one of the six normal bugs).
    run_event(800, args=(CHR.RedEyedChaosBug,))  # Award Sunlight Maggot directly when red-eyed Chaos Bug is killed.

    # NON-RESPAWNING ENEMIES
    # Note that slots 0-3 are used by Chaos Eaters in pre-constructor.
    run_event_with_slot(11410100, 5, args=(CHR.BonfireWorm,))
    run_event_with_slot(11410100, 6, args=(CHR.LoyalDaughter,))
    run_event_with_slot(11410100, 7, args=(1410110,))  # Crystal Lizard.
    # run_event_with_slot(11410100, 8, args=(1410150,))
    run_event_with_slot(11410100, 9, args=(CHR.BoundingDemon,))
    run_event_with_slot(11410100, 12, args=(WallHuggers[0],))
    run_event_with_slot(11410100, 13, args=(WallHuggers[1],))
    run_event_with_slot(11410100, 14, args=(WallHuggers[2],))
    run_event_with_slot(11410120, 0, args=(CHR.ChaosKnight,))

    # Egg-bearers become aggro and then despawn when Fair Lady is dead.
    for slot, egg_bearer, first_maggot in zip(range(10), range(1410201, 1410210), range(1410225, 1410266, 5)):
        args = [egg_bearer] + [maggot for maggot in range(first_maggot, first_maggot + 5)]
        run_event_with_slot(11412100, slot, args=tuple(args))

    run_event(11415210)  # Egg-bearer prayer sound stops if enough are dead (8/9) or Fair Lady is dead.

    # Vile Maggot spawning on Egg-bearer death.
    for slot, egg_bearer, first_maggot in zip(range(11), range(1410201, 1410211), range(1410225, 1410271, 5)):
        args = [egg_bearer] + [maggot for maggot in range(first_maggot, first_maggot + 5)]
        run_event_with_slot(11415250, slot, args=tuple(args))

    # Rockworm ambush based on distance (always from self).
    for slot, lava_rockworm in zip(range(0, 4), LavaRockworms):
        run_event_with_slot(11415100, slot, args=(lava_rockworm, lava_rockworm, 9060, 10.0, 0), arg_types='iiiff')
    run_event_with_slot(11415100, 4, args=(1410460, 1410460, 9060, 10.0, 0), arg_types='iiiff')  # Ground Rockworm.
    run_event_with_slot(11415100, 5, args=(1410461, 1410461, 9060, 5.0, 0), arg_types='iiiff')  # Wall Rockworm.
    run_event_with_slot(11415100, 6, args=(1410301, 1410301, 9060, 15.0, 0), arg_types='iiiff')  # Bonfire Rockworm.
    run_event_with_slot(11415100, 7, args=(1410302, 1410302, 9060, 10.0, 0), arg_types='iiiff')  # Ceiling Rockworm.

    # Quadruple Rockworm ceiling ambush based on area trigger on far landing.
    for slot, rockworm, delay in zip(range(4), range(1410303, 1410307), (0.3, 0.1, 0.0, 0.2)):
        run_event_with_slot(11415120, slot, args=(CHR.Player, rockworm, 9060, 1412302, delay), arg_types='iiiif')

    # Directly award any drops from Rockworms to host. Note slot 0 is missing.
    rockworms = list(range(1410301, 1410306)) + list(LavaRockworms) + [CHR.BonfireWorm, CHR.InsideWallWorm]
    for slot, rockworm in enumerate(rockworms):
        run_event_with_slot(11410150, slot, args=(rockworm, 33900000))

    # Capra Demon ambushes you in sewers.
    run_event(11412011)

    # Treasure chests.
    for slot, chest, obj_act, treasure_taken_flag in zip(range(4), range(1411650, 1411654), range(11410600, 11410604),
                                                         (51410500, 51410100, 51410410, 51410520)):
        run_event_with_slot(11410600, slot, args=(chest, obj_act, treasure_taken_flag))


def event50():
    """ Pre-constructor. """
    header(50)

    for slot, siegmeyer_chaos_eater in enumerate(range(1410410, 1410414)):
        run_event_with_slot(11410100, slot, args=(siegmeyer_chaos_eater,))

    chr.humanity_registration(CHR.LoyalDaughter, 8250)  # Loyal Daughter in Bed of Chaos battle.
    chr.humanity_registration(CHR.SolaireSummon, 8310)  # Solaire summon for Bed of Chaos.
    chr.humanity_registration(CHR.KirkOne, 8956)  # First Kirk invasion in Demon Ruins.
    chr.humanity_registration(CHR.KirkTwo, 8956)  # Second Kirk invasion in Lost Izalith.

    run_event(11415030)  # Solaire summon sign (now for Bed of Chaos).
    run_event(11415032)  # Solaire warps to Bed of Chaos slide when you enter.
    run_event(11415035)  # First Kirk invasion trigger.
    run_event(11415038)  # Second Kirk invasion trigger.
    run_event_with_slot(11410810, 0, args=(CHR.KirkOne, 11415036, 11415037))  # First Kirk defeated.
    run_event_with_slot(11410810, 1, args=(CHR.KirkTwo, 11415039, 11415040))  # Second Kirk defeated.

    chr.humanity_registration(CHR.Solaire, 8310)
    chr.humanity_registration(CHR.SolaireHollow, 8310)

    # SOLAIRE

    skip_if_event_flag_on(3, EVENT.SolaireAtIzalithBonfire)
    skip_if_event_flag_on(2, 1004)
    skip_if_event_flag_on(1, 1003)
    chr.disable(CHR.Solaire)
    skip_if_event_flag_on(1, 11410580)
    skip(1)
    warp.warp_and_set_floor(CHR.Solaire, Category.region, 1412500, -1, 1413000)
    skip_if_event_flag_on(1, 1002)
    chr.disable(CHR.SolaireHollow)
    chr.set_team_type_and_exit_standby_animation(CHR.SolaireHollow, TeamType.hostile_ally)
    run_event_with_slot(11410510, 0, args=(CHR.Solaire, EVENT.SolaireHostile))
    run_event_with_slot(11410520, 0, args=(CHR.Solaire, 1000, 1029, 1005))
    run_event_with_slot(11410530, args=(CHR.Solaire, 1000, 1029, EVENT.SolaireAtIzalithBonfire))
    run_event_with_slot(11410531, args=(CHR.Solaire, 1000, 1029, EVENT.SolaireHollowInIzalith))
    run_event_with_slot(11410532, args=(CHR.Solaire, 1000, 1029, EVENT.SolaireSavedInIzalith))
    run_event_with_slot(11410533, args=(6006, 1000, 1029, 1012))  # No entity 6006. Must be unused Solaire version.
    run_event_with_slot(11410534, args=(CHR.SolaireHollow, 1000, 1029, 1011))  # Hollow Solaire dies.

    # SIEGMEYER

    chr.humanity_registration(CHR.SiegmeyerInIzalith, 8446)
    skip_if_event_flag_range_not_all_off(1, 1503, 1507)
    chr.disable(CHR.SiegmeyerInIzalith)
    skip_if_event_flag_on(3, 1504)
    skip_if_event_flag_on(2, 1506)
    skip_if_event_flag_on(1, 1507)
    skip(2)
    chr.set_special_effect(CHR.SiegmeyerInIzalith, 90111)
    warp.short_warp(CHR.SiegmeyerInIzalith, Category.region, 1412360, -1)
    skip_if_event_flag_off(1, 11410593)
    chr.set_standby_animation_settings(CHR.SiegmeyerInIzalith, standby_animation=7855)
    run_event_with_slot(11410501, args=(CHR.SiegmeyerInIzalith, EVENT.SiegmeyerHostile))
    run_event_with_slot(11410546, args=(CHR.SiegmeyerInIzalith, 1490, 1514, EVENT.SiegmeyerDead))
    run_event_with_slot(11410540, args=(CHR.SiegmeyerInIzalith, 1490, 1514, EVENT.SiegmeyerWaitingInIzalith))
    run_event_with_slot(11410541, args=(CHR.SiegmeyerInIzalith, 1490, 1514, EVENT.SiegmeyerFightingInIzalith))
    run_event_with_slot(11410542, args=(CHR.SiegmeyerInIzalith, 1490, 1514, EVENT.SiegmeyerLeftOutOfBattle))
    run_event_with_slot(11410543, args=(CHR.SiegmeyerInIzalith, 1490, 1514, EVENT.SiegmeyerDyingAfterBattle))
    run_event_with_slot(11410544, args=(CHR.SiegmeyerInIzalith, 1490, 1514, EVENT.SiegmeyerSurvivedBattle))
    run_event_with_slot(11410545, args=(CHR.SiegmeyerInIzalith, 1490, 1514, EVENT.SiegmeyerDead))  # After battle.
    run_event_with_slot(11410549, args=(CHR.SiegmeyerInIzalith,))  # Siegmeyer disappears after surviving battle.
    run_event_with_slot(11410550, args=(CHR.SiegmeyerInIzalith, 1490, 1514, EVENT.SiegmeyerVanished))
    run_event_with_slot(11410547, args=(CHR.SiegmeyerInIzalith,))  # Siegmeyer wakes up when spoken to.
    run_event_with_slot(11410548, args=(CHR.SiegmeyerInIzalith,))  # Siegmeyer sleeps after surviving battle.

    # LOST DAUGHTER

    # NOTE: no humanity registration.
    skip_if_event_flag_on(1, EVENT.LostDaughterIsHiding)
    chr.disable(CHR.LostDaughter)
    
    run_event_with_slot(11412210, args=(CHR.LostDaughter, 11412020, 11412029, EVENT.LostDaughterFightingCentipede))
    run_event_with_slot(11412211, args=(CHR.LostDaughter, 11412020, 11412029, EVENT.LostDaughterWillHide))
    run_event_with_slot(11412212, args=(CHR.LostDaughter, 11412020, 11412029, EVENT.LostDaughterIsHiding))
    run_event_with_slot(11412213, args=(CHR.LostDaughter, 11412020, 11412029, EVENT.LostDaughterWithFairLady))
    run_event_with_slot(11412214, args=(CHR.LostDaughter, 11412020, 11412029, EVENT.LostDaughterDead))

    # XANTHOUS KING JEREMIAH

    # NOTE: no humanity registration.
    chr.disable(CHR.Jeremiah)
    chr.disable(CHR.JeremiahInSewers)
    chr.disable(CHR.JeremiahDummy)
    chr.disable(CHR.JeremiahElevatorDummy)

    run_event_with_slot(11412200, args=(CHR.Jeremiah, 11412050, 11412059, EVENT.JeremiahImpatient))
    run_event_with_slot(11412201, args=(CHR.Jeremiah, 11412050, 11412059, EVENT.JeremiahInIzalith))
    run_event_with_slot(11412202, args=(CHR.Jeremiah, 11412050, 11412059, EVENT.JeremiahFleeingIzalith))
    run_event_with_slot(11412203, args=(CHR.Jeremiah, 11412050, 11412059, EVENT.JeremiahEscaped))
    run_event_with_slot(11412204, args=(CHR.Jeremiah, CHR.JeremiahInSewers, 11412050, 11412059,
                                        EVENT.JeremiahDeadFromPlayer))
    run_event_with_slot(11412205, args=(CHR.Jeremiah, 11412050, 11412059, EVENT.JeremiahDeadNearFairLady))
    run_event_with_slot(11412206, args=(CHR.Jeremiah, 11412050, 11412059, EVENT.JeremiahDeadNearQuelana))
    run_event_with_slot(11412207, args=(CHR.Jeremiah, 11412050, 11412059, EVENT.JeremiahDeadInQuelaagArena))


def event11412210():
    """ Lost Daughter moves to lava lake to fight Centipede Demon. """
    header(11412210)
    lost_daughter, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(1, EVENT.LostDaughterAtCeaseless)
    if_event_flag_on(1, EVENT.CeaselessDischargeDead)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    # If player killed Ceaseless, she bows to the player.
    if_event_flag_on(1, 11415372)
    if_entity_backread_enabled(1, CHR.LostDaughter)
    if_entity_alive(1, CHR.LostDaughter)
    end_if_condition_false(1)

    chr.disable_ai(CHR.LostDaughter)
    chr.replan_ai(CHR.LostDaughter)
    chr.enable_invincibility(CHR.LostDaughter)
    chr.rotate_to_face_entity(CHR.LostDaughter, CHR.Player)
    anim.force_animation(CHR.LostDaughter, ANIM.Bow)


def event11412211():
    """ Lost Daughter decides she will hide on next load, while fighting Centipede. """
    header(11412211)
    lost_daughter, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(1, EVENT.LostDaughterFightingCentipede)
    if_event_flag_on(-2, EVENT.LostDaughterCentipedeFightOngoing)
    if_player_inside_region(-2, REGION.CentipedeDemonBattleStartsOutsideDome)  # player sneaks into Lost Izalith
    if_player_within_distance(-2, 1410964, 10.0)  # player warps to Lost Izalith bonfire
    if_condition_true(1, -2)
    if_condition_true(-1, 1)
    if_condition_true(0, -1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)


def event11412212():
    """ Lost Daughter hides in the lava lake when her Centipede Demon fight ends (reload or triggered ending). """
    header(11412212)
    lost_daughter, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(-1, EVENT.LostDaughterIsHiding)  # She's already hiding, and just needs the setup.
    if_event_flag_on(1, EVENT.LostDaughterWillHide)
    if_event_flag_off(1, EVENT.LostDaughterCentipedeFightOngoing)
    if_condition_true(-1, 1)
    if_condition_true(0, -1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    chr.set_team_type(lost_daughter, TeamType.ally)
    warp.warp(lost_daughter, Category.region, REGION.LostDaughterHidingPlace, -1)
    chr.enable(lost_daughter)
    chr.disable_ai(lost_daughter)
    chr.set_standby_animation_settings(lost_daughter, standby_animation=ANIM.StayKneelingDownOneLeg)
    chr.set_special_effect(lost_daughter, 5492)  # Reduce HP to 1.


def event11412213():
    """ Lost Daughter moves to the Fair Lady. """
    header(11412213)
    lost_daughter, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(1, EVENT.LostDaughterIsHiding)
    if_entity_dead(1, CHR.CentipedeDemon)
    if_player_within_distance(1, lost_daughter, 5.0)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    # Play thanking animation.
    wait(1.5)
    anim.force_animation(lost_daughter, ANIM.GettingUpFromKneelingDownOneLeg, wait_for_completion=True)
    anim.force_animation(lost_daughter, ANIM.Bow)
    chr.set_standby_animation_settings_to_default(lost_daughter)
    chr.set_team_type(lost_daughter, TeamType.ally)
    chr.disable_ai(lost_daughter)  # So she doesn't run off and attack the statue above (she'll die in one hit).

    # Disappears when you get far enough away.
    if_player_beyond_distance(0, lost_daughter, 20.0)
    chr.disable(lost_daughter)


def event11412214():
    """ Lost Daughter dies (at any time, by anyone's hand, except during Centipede fight). """
    header(11412214)
    lost_daughter, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(-1, EVENT.LostDaughterDead)
    if_event_flag_off(1, EVENT.LostDaughterDead)
    if_entity_health_less_than_or_equal(1, CHR.LostDaughter, 0.0)
    if_condition_true(-1, 1)
    if_condition_true(0, -1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    chr.disable(CHR.LostDaughter)
    chr.kill(CHR.LostDaughter, False)


def event11412200():
    """ Jeremiah becomes impatient."""
    header(11412200)
    jeremiah, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(1, EVENT.JeremiahInRuins)
    if_number_true_flags_in_range_greater_than_or_equal(-7, 711, 714, 3)
    if_number_true_flags_in_range_greater_than_or_equal(7, 711, 714, 2)
    if_event_flag_on(7, 5)
    if_condition_true(-7, 7)
    if_condition_true(1, -7)
    if_condition_true(0, 1)
    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)


def event11412201():
    """ Jeremiah moves into Lost Izalith when the Izalith door is opened (by himself or the player), or if the player
    enters Izalith via the dome somehow. """
    header(11412201)
    jeremiah, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(-1, EVENT.JeremiahInRuins)
    if_event_flag_on(-1, EVENT.JeremiahImpatient)
    if_event_flag_on(-2, EVENT.LostIzalithDoorOpened)
    if_player_inside_region(-2, REGION.CentipedeDemonBattleStartsOutsideDome)
    if_player_within_distance(-2, 1411964, 10.0)  # Seems redundant, but I probably had a reason.
    if_condition_true(1, -1)
    if_condition_true(1, -2)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)


def event11412202():
    """ Jeremiah flees with the Chthonic Spark. """
    header(11412202)
    jeremiah, start_flag, end_flag, new_flag = define_args('iiii')

    if_entity_health_less_than_or_equal(1, CHR.Player, 0.0)
    if_event_flag_on(1, EVENT.JeremiahInIzalith)
    if_event_flag_on(-1, EVENT.JeremiahSewerBattleStarted)
    if_event_flag_on(-1, EVENT.JeremiahInBedBattle)
    if_condition_true(1, -1)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    item.remove_items_from_player(ItemType.good, GOOD.ChthonicSpark, 0)  # Triggers stolen message in Common.
    flag.disable(50006771)  # Jeremiah will now drop the Chthonic Spark when killed (by anyone).
    warp.set_player_respawn_point(SPAWN.SanctumBonfire)  # Player will respawn at Sanctum bonfire.


def event11412203():
    """ Jeremiah escapes with the Spark, and is never seen again. """
    header(11412203)
    jeremiah, start_flag, end_flag, new_flag = define_args('iiii')

    if_not_in_world_area(-1, 14, 1)
    if_event_flag_on(-1, EVENT.JeremiahFledOnElevator)
    if_condition_true(1, -1)
    if_event_flag_off(1, EVENT.LostDaughterWithFairLady)
    if_event_flag_on(1, EVENT.QuelanaDead)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    if_entity_backread_enabled(2, 1400700)  # Should always be true, really.
    skip_if_condition_false(3, 2)
    chr.kill(1400700, False)  # Fair Lady.
    chr.kill(6160, False)  # Eingyi. Maggots will appear (freshly killed).
    skip(3)
    flag.enable(11400800)  # Fair Lady dead.
    flag.enable(140)  # Fair Lady dead.
    flag.enable(1284)  # Eingyi dead.


def event11412204():
    """ Jeremiah is killed by the player. """
    header(11412204)
    jeremiah, jeremiah_in_sewers, start_flag, end_flag, new_flag = define_args('iiiii')

    if_entity_health_less_than_or_equal(-1, jeremiah, 0.0)
    if_entity_health_less_than_or_equal(-1, jeremiah_in_sewers, 0.0)
    if_condition_true(0, -1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    # Unlock Xanthous Set with Domnhall (with fake Crown).
    flag.disable(11807230)
    flag.disable(11807240)
    flag.disable(11807250)
    flag.disable(11807260)


def event11412205():
    """ Jeremiah is killed (off-screen) by the Lost Daughter near the Fair Lady (in Blighttown). """
    header(11412205)
    jeremiah, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(1, EVENT.JeremiahFleeingIzalith)
    if_not_in_world_area(-1, 14, 1)
    if_event_flag_on(-1, EVENT.JeremiahFledOnElevator)
    if_condition_true(1, -1)
    if_event_flag_on(1, EVENT.LostDaughterWithFairLady)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    obj.disable(1401200)
    flag.enable(11400210)
    # Unlock Xanthous Set with Domnhall (with fake Crown).
    flag.disable(11807230)
    flag.disable(11807240)
    flag.disable(11807250)
    flag.disable(11807260)


def event11412206():
    """ Jeremiah is killed (off-screen) by Quelana in the Blighttown swamp. """
    header(11412206)
    jeremiah, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(1, EVENT.JeremiahFleeingIzalith)
    if_not_in_world_area(-1, 14, 1)
    if_event_flag_on(-1, EVENT.JeremiahFledOnElevator)
    if_condition_true(1, -1)
    if_event_flag_off(1, EVENT.LostDaughterWithFairLady)
    if_event_flag_off(-2, EVENT.DarkAnorLondo)
    if_event_flag_on(-2, EVENT.QuelaagHeartDead)
    if_condition_true(1, -2)
    if_event_flag_off(1, EVENT.QuelanaDead)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    obj.disable(1401200)
    flag.enable(11400210)
    if_entity_backread_enabled(2, 1400700)  # Should always be true, really.
    skip_if_condition_false(3, 2)
    chr.kill(1400700)
    chr.kill(6160)  # Eingyi. Maggots will appear (freshly killed).
    skip(3)
    flag.enable(11400800)  # Fair Lady dead.
    flag.enable(140)  # Fair Lady dead.
    flag.enable(1284)  # Eingyi dead.
    # Unlock Xanthous Set with Domnhall (with fake Crown).
    flag.disable(11807230)
    flag.disable(11807240)
    flag.disable(11807250)
    flag.disable(11807260)


def event11412207():
    """ Jeremiah is killed (off-screen) by Dark Quelaag in her arena. """
    header(11412207)
    jeremiah, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_on(1, EVENT.JeremiahFleeingIzalith)
    if_not_in_world_area(-1, 14, 1)
    if_event_flag_on(-1, EVENT.JeremiahFledOnElevator)
    if_condition_true(1, -1)
    if_event_flag_off(1, EVENT.LostDaughterWithFairLady)
    if_event_flag_on(1, EVENT.DarkAnorLondo)
    if_event_flag_off(1, EVENT.QuelaagHeartDead)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)

    obj.disable(1401200)  # Illusory wall to Fair Lady.
    flag.enable(11400210)  # Illusory wall event done.
    if_entity_backread_enabled(2, 1400700)  # Should always be true, really.
    skip_if_condition_false(3, 2)
    chr.kill(1400700)
    chr.kill(6160)  # Eingyi. Maggots will appear (freshly killed).
    skip(3)
    flag.enable(11400800)  # Fair Lady dead.
    flag.enable(140)  # Fair Lady dead.
    flag.enable(1284)  # Eingyi dead.
    # Unlock Xanthous Set with Domnhall (with fake Crown).
    flag.disable(11807230)
    flag.disable(11807240)
    flag.disable(11807250)
    flag.disable(11807260)


def event800():
    """ Directly award Sunlight Maggot when red-eyed Chaos Bug dies. """
    header(800, 1)
    chaos_bug, = define_args('i')
    skip_if_this_event_off(2)
    chr.disable(chaos_bug)
    end()
    if_entity_dead(0, chaos_bug)
    item.award_item_to_host_only(34800100)
    end()


def event11410100():
    """ Stops certain enemies from respawning, and awards Bounding Demon drop. """
    header(11410100, 1)
    enemy, = define_args('i')
    skip_if_this_event_slot_off(3)
    chr.disable(enemy)
    chr.kill(enemy, False)
    end()

    if_entity_dead(0, enemy)
    if_character_hollow(-7, CHR.Player)
    if_character_human(-7, CHR.Player)
    end_if_condition_false(-7)
    skip_if_not_equal(1, enemy, CHR.BoundingDemon)
    item.award_item_to_host_only(ITEMLOT.BoundingDemonDrop)
    skip_if_not_equal(1, enemy, 1410110)
    item.award_item_to_host_only(33002000)


def event11412040():
    """ Randomize red-eyed Chaos Bug location *once* and then warp it there on startup. """
    header(11412040, 1)

    # One-time random location choice.
    skip_if_event_flag_range_not_all_off(1, 11412041, 11412046)
    flag.enable_random_in_chunk(11412041, 11412046)

    for bug in range(1, 7):
        # Warp to appropriate normal Chaos Bug and disable that bug.
        skip_if_event_flag_off(3, 11412040 + bug)
        chr.disable(1410100 + bug)
        warp.warp(CHR.RedEyedChaosBug, Category.region, 1412870 + bug, -1)
        end()


def event11410340():
    """ Open the stone gate to Lost Izalith. """
    header(11410340, 0)

    skip_if_event_flag_on(1, EVENT.JeremiahStoleFromVamos)  # DOor opens if Jeremiah stole from Vamos.
    skip_if_this_event_off(4)
    anim.end_animation(1411340, 1)   # reopen door
    chr.disable(1410462)
    chr.kill(1410462, False)
    end()

    if_host(1)
    # Triggered by possession of Chthonic Spark or any Ascended Pyromancy Flame from Quelana
    if_player_has_good(-1, GOOD.ChthonicSpark)
    for ascended_pyromancy_flame in (1332000, 1332100, 1332200, 1332300, 1332400, 1332500):
        if_player_has_weapon(-1, ascended_pyromancy_flame)
    if_condition_true(1, -1)
    if_action_button_in_region(1, 1412201, 10010510, line_intersects=1411340)
    if_action_button_in_region(2, 1412200, 10010510, line_intersects=1411340)
    if_condition_true(-2, 1)
    if_condition_true(-2, 2)
    if_event_flag_on(-2, EVENT.JeremiahOpenedLostIzalith)
    if_condition_true(0, -2)
    end_if_event_flag_on(EVENT.JeremiahOpenedLostIzalith)
    flag.enable(EVENT.LostIzalithDoorOpened)  # animation can be skipped by reloading
    chr.rotate_to_face_entity(CHR.Player, 1411340)
    anim.force_animation(CHR.Player, 7114, wait_for_completion=True)
    anim.force_animation(1411340, 1)
    sfx.create_oneoff_sfx(Category.object, 1411340, -1, 140000)
    end_if_condition_false_finished(1)  # Don't show message if player opened it from the inside.
    message.dialog(TEXT.IzalithGateOpens, ButtonType.yes_no, NumberButtons.no_button, 1411340, 5.0)


def event11410341():
    """ Message saying Izalith door won't open. """
    header(11410341, 0)
    network.disable_sync()

    # If you're host, activating the front of the door, and don't have a required item, show the message.
    if_event_flag_off(1, EVENT.LostIzalithDoorOpened)
    if_host(1)
    if_player_has_good(-7, GOOD.ChthonicSpark)
    for ascended_pyromancy_flame in range(1332000, 1332501, 100):
        if_player_has_weapon(-7, ascended_pyromancy_flame)
    if_condition_false(1, -7)
    if_action_button_in_region(1, 1412201, 10010510, line_intersects=1411340)

    # If you're client and activating either side of the door, show the message.
    if_event_flag_off(2, EVENT.LostIzalithDoorOpened)
    if_client(2)
    if_action_button_in_region(-3, 1412201, 10010510, line_intersects=1411340)
    if_action_button_in_region(-3, 1412200, 10010510, line_intersects=1411340)
    if_condition_true(2, -3)

    # If door was already opened (by player or Jeremiah), terminate event.
    if_event_flag_on(3, EVENT.LostIzalithDoorOpened)   # terminate event if this is true.

    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(0, -1)
    end_if_condition_true_finished(3)
    message.dialog(TEXT.IzalithGateClosed, ButtonType.yes_no, NumberButtons.no_button, 1411340, 5.0)
    restart()


def event11412070():
    """ Taurus Demons aggro together. They don't respawn once both are killed, and award a Demon's Greataxe. """
    header(11412070, 1)
    skip_if_this_event_off(3)
    chr.disable(TaurusDemons[0])
    chr.disable(TaurusDemons[1])
    end()

    chr.disable_ai(TaurusDemons[0])
    chr.disable_ai(TaurusDemons[1])
    if_entity_attacked_by(-1, TaurusDemons[0], CHR.Player)
    if_entity_attacked_by(-1, TaurusDemons[1], CHR.Player)
    if_player_within_distance(-1, TaurusDemons[0], 8.0)
    if_player_within_distance(-1, TaurusDemons[1], 8.0)
    if_condition_true(0, -1)
    chr.enable_ai(TaurusDemons[0])
    chr.enable_ai(TaurusDemons[1])

    if_entity_health_less_than_or_equal(1, TaurusDemons[0], 0.0)
    if_entity_health_less_than_or_equal(1, TaurusDemons[1], 0.0)
    if_condition_true(0, 1)
    item.award_item_to_host_only(ITEMLOT.TaurusDemonsReward)


def event11415373():
    """ Ceaseless Discharge boss notification (currently vanilla). """
    header(11415373, 0)
    skip_if_this_event_on(3)
    if_event_flag_off(1, EVENT.CeaselessDischargeDead)
    if_player_inside_region(1, 1412696)
    if_condition_true(0, 1)
    skip_if_client(2)
    network.notify_boss_room_entry()
    chr.set_network_update_authority(CHR.CeaselessDischarge, UpdateAuthority.forced)
    chr.activate_npc_buffs(CHR.CeaselessDischarge)
    chr.set_network_update_rate(CHR.CeaselessDischarge, True, 0)
    chr.disable_invincibility(CHR.CeaselessDischarge)


def event11410800():
    """ Lava drains. Enables all the enemies and items hidden beneath. """
    header(11410800, 1)

    # Disable lava if already drained.
    skip_if_event_flag_off(5, EVENT.CeaselessLavaDrained)
    obj.disable(1411100)
    hitbox.disable_hitbox(1413100)
    sound.disable_map_sound(1413805)
    obj.enable_treasure(1411610)   # not sure exactly which treasure this is.
    end()

    obj.disable(1411610)
    obj.disable_treasure(1411610)
    hitbox.disable_hitbox(1413101)
    # Disable enemies in lava (four Rockworms and two Taurus Demons).
    for taurus_demon in TaurusDemons:
        chr.disable(taurus_demon)
    for lava_rockworm in LavaRockworms:
        chr.disable(lava_rockworm)
    network.disable_sync()

    if_this_event_on(0)  # rare case where this event's flag must be enabled to trigger it.
    wait(5.0)

    # End if host is dead (i.e. died at the same time as Ceaseless). Event will resume when they approach the lava.
    if_host(1)
    if_entity_health_less_than_or_equal(1, CHR.Player, 0.0)
    end_if_condition_true(1)
    end_if_client()

    if_player_inside_region(0, 1412530)
    cutscene.play_cutscene_to_player(140100, CutsceneType.skippable, CHR.Player)
    wait_frames(1)
    chr.disable(CHR.JeremiahDummy)
    chr.disable(CHR.LostDaughter)
    flag.enable(EVENT.CeaselessLavaDrained)
    obj.disable(1411100)
    hitbox.disable_hitbox(1413100)
    sound.disable_map_sound(1413805)
    hitbox.enable_hitbox(1413101)
    obj.enable(1411610)
    obj.enable_treasure(1411610)
    # Enable enemies in lava (four Rockworms and two Taurus Demons).
    for taurus_demon in TaurusDemons:
        chr.enable(taurus_demon)
    for lava_rockworm in LavaRockworms:
        chr.enable(lava_rockworm)


def event11415375():
    """ Ceaseless briefly enables AI to move toward the altar. """
    header(11415375, 1)
    # End if Ceaseless is already aggressive because you already looted the altar.
    end_if_event_flag_on(51410180)
    if_event_flag_on(0, 11415373)
    chr.set_special_effect(CHR.CeaselessDischarge, 5129)  # Makes him walk towards the altar.
    chr.enable_ai(CHR.CeaselessDischarge)
    wait(12)  # Walk towards the altar for twelve seconds (to end in the right place).
    chr.disable_ai(CHR.CeaselessDischarge)


def event11415377():
    """ Ceaseless pulls out his middle arm when you loot the altar or kill the Lost Daughter. """
    header(11415377, 1)
    skip_if_this_event_off(4)
    chr.cancel_special_effect(CHR.CeaselessDischarge, 5132)
    chr.set_special_effect(CHR.CeaselessDischarge, 5133)
    chr.ai_instruction(CHR.CeaselessDischarge, -1, 0)
    end()
    if_has_tae_event(-1, CHR.CeaselessDischarge, 300)
    if_entity_health_less_than_or_equal(-1, CHR.LostDaughter, 0)
    if_condition_true(0, -1)
    chr.cancel_special_effect(CHR.CeaselessDischarge, 5132)
    chr.set_special_effect(CHR.CeaselessDischarge, 5133)
    chr.ai_instruction(CHR.CeaselessDischarge, -1, 0)
    chr.replan_ai(CHR.CeaselessDischarge)


def event11410900():
    """ Ceaseless Discharge death. """
    header(11410900, 0)

    if_entity_dead(0, CHR.CeaselessDischarge)
    flag.enable(EVENT.CeaselessDischargeDead)
    skip_if_event_flag_on(2, EVENT.JeremiahKilledCeaseless)
    boss.kill_boss(CHR.CeaselessDischarge)  # No boss rewards if Jeremiah killed him.
    flag.enable(EVENT.CeaselessDischargeKilledByPlayer)
    chr.disable_backread(CHR.CeaselessDischarge)
    flag.enable(11410800)  # Makes lava drain.
    obj.disable(1411790)
    sfx.delete_map_sfx(1411791)


def event11415372():
    """ Ceaseless Discharge boss trigger. Also handles Lost Daughter fog entrance. """
    header(11415372, 1)

    # Remove Ceaseless if already dead.
    skip_if_event_flag_off(3, EVENT.CeaselessDischargeDead)
    chr.disable_backread(CHR.CeaselessDischarge)
    chr.kill(CHR.CeaselessDischarge)
    end()

    # Set up Ceaseless pre-battle.
    chr.disable_ai(CHR.CeaselessDischarge)
    chr.disable_health_bar(CHR.CeaselessDischarge)
    chr.enable_invincibility(CHR.CeaselessDischarge)

    # Warp Ceaseless to altar if items taken.
    if_host(7)
    skip_if_client(1)
    if_event_flag_on(7, 51410180)
    skip_if_condition_false(1, 7)
    warp.warp(CHR.CeaselessDischarge, Category.region, REGION.CeaselessAtAltar, -1)

    # Battle begins if Ceaseless is attacked or altar items taken.
    if_event_flag_on(1, 11415373)
    if_host(1)
    skip_if_client(1)
    if_event_flag_on(1, 51410180)
    if_event_flag_on(2, 11415373)
    if_entity_attacked_by(2, CHR.CeaselessDischarge, CHR.Player)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    chr.set_nest(CHR.CeaselessDischarge, REGION.CeaselessAtAltar)
    chr.cancel_special_effect(CHR.CeaselessDischarge, 5129)   # Don't approach the altar.
    chr.enable_ai(CHR.CeaselessDischarge)
    chr.replan_ai(CHR.CeaselessDischarge)
    boss.enable_boss_health_bar(CHR.CeaselessDischarge, 5250)


def event11415500():
    """ Lost Daughter trigger in Ceaseless Discharge fight. """
    header(11415500, 1)

    chr.disable(CHR.LostDaughter)
    end_if_event_flag_on(EVENT.CeaselessDischargeDead)
    end_if_event_flag_on(EVENT.CentipedeDemonDead)  # No Lost Daughter events if Centipede Demon is already dead.

    if_event_flag_on(1, 11415372)
    if_event_flag_on(1, EVENT.LostDaughterAtCeaseless)
    if_condition_true(0, 1)

    chr.enable(CHR.LostDaughter)
    warp.warp(CHR.LostDaughter, Category.region, REGION.OutsideCeaselessFog, -1)
    chr.set_standby_animation_settings_to_default(CHR.LostDaughter)

    # If player just entered, wait five seconds, then enter. Otherwise, wait for approach.
    if_player_within_distance(2, CHR.LostDaughter, 10.0)  # Ceaseless already aggressive.
    skip_if_condition_true(2, 2)
    if_player_within_distance(0, CHR.LostDaughter, 30.0)
    skip(1)
    wait(5.0)

    anim.force_animation(CHR.LostDaughter, ANIM.WalkThroughFog, wait_for_completion=True)
    chr.rotate_to_face_entity(CHR.LostDaughter, CHR.CeaselessDischarge)
    anim.force_animation(CHR.LostDaughter, ANIM.PointUpGesture)
    chr.set_team_type(CHR.LostDaughter, TeamType.hostile_ally)
    run_event(11415501)  # Main loop that makes her temporarily aggro when you approach.


def event11415501():
    """ Lost Daughter loop in Ceaseless Discharge fight. """
    header(11415501)

    # Terminate event if you kill either Lost Daughter or Ceaseless.
    end_if_event_flag_on(EVENT.LostDaughterDead)
    end_if_event_flag_on(EVENT.CeaselessDischargeDead)

    chr.disable_ai(CHR.LostDaughter)
    # She only becomes aggro if you attack her or if Ceaseless has jumped off.
    if_entity_attacked_by(-1, CHR.LostDaughter, CHR.Player)
    if_event_flag_on(-1, 11415376)   # Ceaseless is hanging onto the ledge (she punishes you for torturing him).
    if_condition_true(0, -1)
    # If Ceaseless is hanging, wait briefly, then start attacking (unless he's dead).
    skip_if_event_flag_off(5, 11415376)
    wait(5.0)
    if_entity_health_less_than_or_equal(1, CHR.CeaselessDischarge, 0.0)
    skip_if_condition_true(1, 1)
    chr.enable_ai(CHR.LostDaughter)
    end()
    # Otherwise, when attacked, enable her AI for eight seconds, then restart.
    chr.enable_ai(CHR.LostDaughter)
    wait(8.0)
    chr.rotate_to_face_entity(CHR.LostDaughter, CHR.CeaselessDischarge)
    anim.force_animation(CHR.LostDaughter, ANIM.PointUpGesture)
    restart()


def event11412060():
    """ Jeremiah ambushes you in Demon Ruins (old Firesage room) """
    header(11412060)

    chr.disable(CHR.Jeremiah)
    end_if_this_event_on()

    # Trigger Jeremiah when the player moves into his drop attack range from the stairs (without Spark).
    if_host(1)
    if_event_flag_on(1, EVENT.JeremiahInRuins)
    if_player_does_not_have_good(1, GOOD.ChthonicSpark)
    if_player_inside_region(1, REGION.JeremiahFirstBattleTrigger)
    if_condition_true(0, 1)

    flag.enable(11415340)  # allows Fair Lady and Eingyi to be disabled
    flag.enable(EVENT.JeremiahRuinsBattleDone)  # this event as done
    obj.enable(1411410)
    sfx.create_map_sfx(1411411)
    obj.enable(1411412)
    sfx.create_map_sfx(1411413)
    chr.enable(CHR.Jeremiah)
    chr.enable_invincibility(CHR.Jeremiah)
    anim.force_animation(CHR.Jeremiah, 253801, loop=True)
    wait(1.1)
    anim.force_animation(CHR.Jeremiah, 253810)
    chr.disable_invincibility(CHR.Jeremiah)   # can't seem to make him immune to fall damage with params.
    sound.enable_map_sound(1413803)
    boss.enable_boss_health_bar(CHR.Jeremiah, TEXT.JeremiahBossName)

    if_entity_health_less_than_or_equal(0, CHR.Jeremiah, 0)
    for statue_id in range(1410463, 1410467):
        chr.kill(statue_id)  # Kill the four Demonic Statues in the room so the player can relax.
    if_entity_dead(0, CHR.Jeremiah)
    boss.disable_boss_health_bar(CHR.Jeremiah, TEXT.JeremiahBossName)
    boss.kill_boss(CHR.Jeremiah)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)
    obj.disable(1411410)
    sfx.delete_map_sfx(1411411)
    obj.disable(1411412)
    sfx.delete_map_sfx(1411413)
    sound.disable_map_sound(1413803)


def event11412061():
    """ One-off battle with Jeremiah in the Lost Izalith sewers. """
    header(11412061)

    chr.disable(CHR.JeremiahInSewers)

    end_if_this_event_on()

    # Trigger Jeremiah when he is in Izalith and the player enters the sewers with the First Spark.
    if_host(1)
    if_event_flag_on(1, EVENT.JeremiahInIzalith)
    if_player_has_good(1, GOOD.ChthonicSpark)
    if_player_inside_region(1, REGION.JeremiahSewerTrigger)
    if_condition_true(0, 1)

    flag.enable(EVENT.JeremiahSewerBattleStarted)  # For Siegmeyer and Spark theft.
    flag.enable(EVENT.JeremiahSewerBattleDone)  # marks this event as done, he won't appear again
    wait(3)  # he drops in after this
    obj.enable(1411890)
    sfx.create_map_sfx(1411891)
    obj.enable(1411892)
    sfx.create_map_sfx(1411893)
    chr.enable(CHR.JeremiahInSewers)
    chr.enable_ai(CHR.JeremiahInSewers)
    sound.enable_map_sound(1413804)
    boss.enable_boss_health_bar(CHR.JeremiahInSewers, TEXT.JeremiahBossName)

    if_entity_dead(0, CHR.JeremiahInSewers)
    boss.disable_boss_health_bar(CHR.JeremiahInSewers, TEXT.JeremiahBossName)
    boss.kill_boss(CHR.JeremiahInSewers)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 777777777)
    obj.disable(1411890)
    sfx.delete_map_sfx(1411891)
    obj.disable(1411892)
    sfx.delete_map_sfx(1411893)
    sound.disable_map_sound(1413804)


def event11410410():
    """ This was originally the Firesage Demon's death, now just used to enable the shortcut elevator when the player
    enters the lower Nursery (unless Jeremiah is fleeing).
    """
    header(11410410)

    # Elevator flag must be re-checked every map load in case Jeremiah is fleeing.
    flag.disable(11410410)

    # If Jeremiah is fleeing, wait for elevator to be enabled manually or for the player to leave m14_01 another way.
    skip_if_event_flag_off(4, 11412053)
    if_event_flag_on(-1, 11410410)
    if_not_in_world_area(-1, 14, 1)
    if_condition_true(0, -1)
    end()

    # Otherwise, wait for player to enter the lower Nursery (or if they already have).
    if_event_flag_on(-2, EVENT.ShortcutElevatorUsuallyActive)
    if_player_inside_region(-2, REGION.TriggerJeremiahOpeningLostIzalith)
    if_condition_true(0, -2)
    flag.enable(EVENT.ShortcutElevatorUsuallyActive)
    end()


def event11412030():
    """ Watch Lost Daughter fight Centipede Demon from the bridge to Lost Izalith. """
    header(11412030, 1)

    chr.set_team_type(CHR.CentipedeDemon, TeamType.neutral)
    chr.disable(CHR.LostDaughterFightingCentipede)

    end_if_event_flag_on(EVENT.LostDaughterCentipedeFightDone)

    if_event_flag_on(1, EVENT.LostDaughterFightingCentipede)
    if_player_inside_region(1, REGION.TriggerLostDaughterCentipedeBattle)
    if_condition_true(0, 1)

    flag.enable(EVENT.LostDaughterCentipedeFightOngoing)
    flag.enable(EVENT.LostDaughterCentipedeFightDone)  # won't happen again

    chr.enable(CHR.CentipedeDemon)
    warp.warp(CHR.CentipedeDemon, Category.region, REGION.CentipedeFightingLostDaughter, -1)
    chr.set_team_type(CHR.CentipedeDemon, TeamType.enemy)
    chr.replan_ai(CHR.CentipedeDemon)
    chr.disable_health_bar(CHR.CentipedeDemon)
    chr.enable_invincibility(CHR.CentipedeDemon)

    chr.enable(CHR.LostDaughterFightingCentipede)
    chr.set_team_type_and_exit_standby_animation(CHR.LostDaughterFightingCentipede, TeamType.fighting_ally)
    chr.replan_ai(CHR.LostDaughterFightingCentipede)
    chr.disable_health_bar(CHR.LostDaughterFightingCentipede)
    chr.enable_invincibility(CHR.LostDaughterFightingCentipede)
    chr.enable_immortality(CHR.LostDaughterFightingCentipede)

    if_player_inside_region(-1, REGION.StopLostDaughterCentipedeBattle)
    if_player_inside_region(-1, REGION.StopLostDaughterCentipedeBattleBack)
    if_condition_true(0, -1)

    flag.disable(EVENT.LostDaughterCentipedeFightOngoing)

    # Disable temporary Lost Daughter NPC.
    chr.disable(CHR.LostDaughterFightingCentipede)

    # Reset Centipede Demon to default manually, in case player doesn't rest before going down there.
    warp.warp(CHR.CentipedeDemon, Category.region, REGION.CentipedeDemonWaiting, -1)
    chr.set_team_type(CHR.CentipedeDemon, TeamType.neutral)
    chr.replan_ai(CHR.CentipedeDemon)
    chr.disable_invincibility(CHR.CentipedeDemon)
    wait(2.0)
    chr.enable_health_bar(CHR.CentipedeDemon)


def event11415510():
    """ Lost Daughter gives you temporary lava immunity. """
    header(11415510, 1)

    end_if_event_flag_on(EVENT.CentipedeDemonDead)

    if_event_flag_on(1, EVENT.LostDaughterIsHiding)
    if_event_flag_on(1, 11410360)  # Illusory wall destroyed.
    if_player_within_distance(1, CHR.LostDaughter, 5.0)
    if_entity_alive(1, CHR.CentipedeDemon)
    if_event_flag_off(1, 11415510)
    if_condition_true(0, 1)
    wait(2.0)
    anim.force_animation(CHR.LostDaughter, ANIM.LiftHandFromKneelingDownOneLeg, wait_for_completion=True)
    event.restart_event_id(11415511)
    restart()


def event11415511():
    """ Player touches the protective flame left by the Lost Daughter. """
    header(11415511, 1)

    end_if_event_flag_on(EVENT.CentipedeDemonDead)

    if_event_flag_on(0, 11415510)
    message.status_explanation(TEXT.FireProtection)
    chr.set_special_effect(CHR.Player, 5152)
    wait(110.0)
    message.dialog(TEXT.FireProtectionAlmostOver, ButtonType.yes_no, NumberButtons.no_button, CHR.Player, 10.0)
    flag.disable(11415510)
    wait(10.0)
    chr.cancel_special_effect(CHR.Player, 5152)

    if_event_flag_on(0, EVENT.CentipedeDemonDead)
    end()


def event11415386():
    """ Orange Charred Ring awarded when any part of Centipede Demon is killed. """
    header(11415386)
    end_if_client()
    if_entity_dead(-1, CHR.CentipedeDemon)
    for centipede_part in range(1410710, 1410715):
        if_entity_dead(-1, centipede_part)
    for centipede_part in range(1410720, 1410725):
        if_entity_dead(-1, centipede_part)
    if_condition_true(0, -1)
    if_character_type(-7, CHR.Player, CharacterType.human)
    if_character_type(-7, CHR.Player, CharacterType.hollow)
    end_if_condition_false(-7)
    item.award_item_to_host_only(ITEMLOT.OrangeCharredRing)


def event11415382():
    """ Centipede Demon behavior setup. """
    header(11415382, 1)

    obj.disable(1411110)  # petrified Centipede Demon
    flag.enable(11410002)  # cutscene has "played"
    flag.enable(11415380)  # makes parts load
    skip_if_event_flag_on(1, 11415385)  # Only runs once per load.
    run_event(11415385)  # load arms and tails (checks inside if Centipede Demon is alive).

    # Remove Centipede Demon if it's dead.
    skip_if_event_flag_off(2, EVENT.CentipedeDemonDead)
    chr.disable_backread(CHR.CentipedeDemon)
    end()

    skip_if_event_flag_off(1, EVENT.LostDaughterCentipedeFightDone)
    chr.set_team_type(CHR.CentipedeDemon, TeamType.none)   # Centipede Demon won't attack unless aggravated.

    # First-time trigger: player gets close to Centipede Demon, close to Lost Daughter hiding place, or attacks it.
    if_player_inside_region(1, REGION.CentipedeDemonArena)
    if_entity_attacked_by(-2, CHR.CentipedeDemon, CHR.Player)
    if_player_within_distance(-2, CHR.CentipedeDemon, 20.0)
    if_player_within_distance(-2, 1410960, 20.0)
    if_condition_true(1, -2)
    if_condition_true(0, 1)
    chr.set_team_type(CHR.CentipedeDemon, TeamType.boss)
    boss.enable_boss_health_bar(CHR.CentipedeDemon, 5200)
    sound.enable_map_sound(1413802)
    run_event(11415387)  # Handles recurring start/stop by entering and leaving the lava lake.


def event11415387():
    """ Centipede Demon behavior/music start/stop loop. """
    header(11415387, 1)

    # End battle if Centipede Demon dies or pause if the player leaves the arena.
    if_event_flag_on(1, EVENT.CentipedeDemonDead)
    if_condition_true(-1, 1)
    if_player_inside_region(-1, REGION.CentipedeDemonBattleEndsInIzalith)
    if_player_inside_region(-1, REGION.CentipedeDemonBattleEndsOutsideDome)
    if_condition_true(0, -1)
    boss.disable_boss_health_bar(CHR.CentipedeDemon, 5200)
    sound.disable_map_sound(1413802)
    end_if_condition_true_finished(1)

    if_player_inside_region(-2, REGION.CentipedeDemonBattleStartsFromIzalith)
    if_player_inside_region(-2, REGION.CentipedeDemonBattleStartsOutsideDome)
    if_condition_true(0, -2)
    boss.enable_boss_health_bar(CHR.CentipedeDemon, 5200)
    sound.enable_map_sound(1413802)

    restart()


def event11415392():
    """ Bed of Chaos battle logic trigger. """

    header(11415392, 1)

    # Already dead:
    skip_if_event_flag_off(7, 10)
    chr.disable(1410800)
    chr.disable(1410801)
    chr.disable(1410802)
    chr.kill(1410800, False)
    chr.kill(1410801, False)
    chr.kill(1410802, False)
    skip(12)

    # Disable elemental boss if no orbs are destroyed.
    skip_if_event_flag_range_not_all_off(1, 11410291, 11410292)
    chr.disable(1410800)

    # Set tree boss to default animations if any orbs are destroyed (skip wake up).
    skip_if_event_flag_range_all_off(1, 11410291, 11410292)
    chr.set_standby_animation_settings_to_default(1410801)

    chr.enable_invincibility(1410800)
    chr.enable_invincibility(1410801)
    chr.disable_health_bar(1410800)
    chr.disable_health_bar(1410801)
    chr.disable_ai(1410801)
    chr.disable_ai(6620)
    game.set_locked_camera_slot_number(14, 1, 1)  # this happens before even triggering the fight...

    if_host(1)
    if_player_inside_region(1, 1412996)  # end of slide
    if_condition_true(0, 1)

    # Skip boss wake-up if dead.
    skip_if_event_flag_on(5, 10)
    # Skip wake up animation of tree if any orbs are destroyed.
    skip_if_event_flag_range_not_all_off(2, 11410291, 11410292)
    chr.set_standby_animation_settings_to_default(1410801)
    anim.force_animation(1410801, 9060)
    chr.enable_ai(1410801)
    boss.enable_boss_health_bar(1410802, 5400)

    # Enable Loyal Daughter (if alive) and
    if_entity_dead(7, CHR.LoyalDaughter)
    skip_if_condition_true(1, 7)
    chr.enable_ai(CHR.LoyalDaughter)


def event11412062():
    """ Witness Jeremiah killing Ceaseless Discharge. """
    header(11412062)

    chr.disable(CHR.JeremiahDummy)
    if_event_flag_off(1, EVENT.CeaselessDischargeDead)
    if_event_flag_on(1, EVENT.JeremiahImpatient)
    if_player_within_distance(1, 1410961, 15.0)  # Close to first Demon Ruins bonfire.
    if_condition_true(0, 1)

    # Make Ceaseless jump.
    chr.enable(CHR.JeremiahDummy)
    warp.short_warp(CHR.CeaselessDischarge, Category.region, 1412797, -1)
    anim.force_animation(CHR.CeaselessDischarge, 17006, wait_for_completion=True)
    warp.short_warp(CHR.CeaselessDischarge, Category.region, 1412798, -1)
    anim.force_animation(CHR.JeremiahDummy, 6409, wait_for_completion=False)
    wait(1.6)   # temp
    chr.kill(CHR.CeaselessDischarge, False)


def event11412063():
    """ Witness Jeremiah opening the door to Lost Izalith (one time). """
    header(11412063)

    end_if_this_event_on()

    if_event_flag_on(1, EVENT.JeremiahImpatient)
    if_player_inside_region(1, REGION.TriggerJeremiahOpeningLostIzalith)
    if_condition_true(0, 1)

    flag.enable(EVENT.LostIzalithDoorOpened)
    flag.enable(EVENT.CeaselessDischargeDead)
    flag.enable(EVENT.JeremiahKilledCeaseless)
    flag.enable(EVENT.JeremiahOpenedLostIzalith)

    # Kill Capra Demon guarding the door.
    chr.disable(1410462)
    chr.kill(1410462, False)

    # Move dummy Jeremiah to the door and have him open it.
    warp.warp(CHR.JeremiahDummy, Category.region, REGION.JeremiahOpensIzalithDoor, -1)
    chr.enable(CHR.JeremiahDummy)
    chr.enable_invincibility(CHR.JeremiahDummy)
    anim.force_animation(CHR.JeremiahDummy, 7114, wait_for_completion=True)

    # Open door.
    anim.force_animation(1411340, 1)
    sfx.create_oneoff_sfx(Category.object, 1411340, -1, 140000)
    wait(5)
    anim.force_animation(CHR.JeremiahDummy, ANIM.WalkThroughFog, wait_for_completion=True)  # to get through barrier
    anim.force_animation(CHR.JeremiahDummy, 510, loop=True)
    wait(5)
    anim.force_animation(CHR.JeremiahDummy, 700, wait_for_completion=True)  # breaks branch in his way
    anim.force_animation(CHR.JeremiahDummy, 510, loop=True)

    # Wait long enough for him to run out of your line of sight.
    wait(10)
    chr.disable_invincibility(CHR.JeremiahDummy)
    chr.disable(CHR.JeremiahDummy)


def event11412064():
    """ Jeremiah encounter: he escapes with the Chthonic Spark on the elevator to Quelaag's Domain. """
    header(11412064)

    chr.disable(CHR.JeremiahElevatorDummy)

    # Prepare elevator if Jeremiah is fleeing (always means player just died, so safe to check here).
    if_event_flag_on(0, EVENT.JeremiahFleeingIzalith)
    # Bring down elevator if it's at the top.
    skip_if_event_flag_on(2, 11410401)
    anim.end_animation(1410400, 3)
    flag.enable(11410401)

    # Warp and enable dummy Jeremiah when player is close. This also counts as the one-off event.
    if_player_inside_region(0, REGION.JeremiahOnElevatorTrigger)
    flag.enable(EVENT.JeremiahFledOnElevator)
    chr.enable(CHR.JeremiahElevatorDummy)
    chr.enable_invincibility(CHR.JeremiahElevatorDummy)

    # Activate elevator.
    sfx.create_object_sfx(1411400, 100, 140002)
    anim.force_animation(1411400, 1, wait_for_completion=False)

    wait(5.0)
    chr.disable(CHR.JeremiahElevatorDummy)
    flag.disable(11410401)  # only tell the game the elevator is up the top at this point, and it will send it back down
    flag.enable(11410410)  # re-enable normal elevator function
    anim.end_animation(1410400, 1)
    sfx.delete_object_sfx(1411400, erase_root=True)
    anim.force_animation(1411400, 5, wait_for_completion=True)


def event11412065():
    """ Jeremiah attacks during the Bed of Chaos battle if you have the Chthonic Spark.

    He will keep ambushing you here if you quit (one of you must die to end the event). He will also ambush you in the
    sewers (once) if you quit.
    """
    header(11412065)

    # Jeremiah or Bed must die to end this event.
    end_if_this_event_on()
    end_if_event_flag_on(EVENT.BedOfChaosDead)

    # Jeremiah attacks after one orb is destroyed or if Loyal Daughter is dead (if player has Spark).
    if_event_flag_on(1, EVENT.JeremiahInIzalith)
    if_event_flag_on(1, EVENT.BedOfChaosBattleStarted)
    if_player_has_good(1, GOOD.ChthonicSpark)
    if_entity_dead(-1, CHR.LoyalDaughter)
    if_event_flag_range_not_all_off(-1, 11410291, 11410292)
    if_condition_true(1, -1)
    if_condition_true(0, 1)

    # Spawn Jeremiah near the end of the slide.
    chr.enable_invincibility(CHR.Jeremiah)
    warp.warp(CHR.Jeremiah, Category.region, REGION.SlidingIntoBedArena, -1)
    chr.enable(CHR.Jeremiah)
    flag.enable(EVENT.JeremiahInBedBattle)
    wait(4.0)
    chr.disable_invincibility(CHR.Jeremiah)
    chr.enable_ai(CHR.Jeremiah)
    boss.enable_boss_health_bar_with_slot(CHR.Jeremiah, 1, TEXT.JeremiahBossName)

    # Wait for Jeremiah to die to end the event. Ground in front of Bed won't crumble until he's dead.
    if_entity_dead(0, CHR.Jeremiah)
    end()


def event11412000():
    """ Death of a Parasitic Wall Hugger. """
    header(11412000, 1)
    wall_hugger, dead_flag = define_args('ii')

    skip_if_event_flag_off(2, dead_flag)
    chr.disable(wall_hugger)
    end()

    if_entity_alive(1, wall_hugger)
    skip_if_condition_true(11, 1)

    # Reward depends on number of Wall Huggers killed.
    if_number_true_flags_in_range_greater_than_or_equal(2, 11412005, 11412007, 2)
    skip_if_condition_false(2, 2)
    item.award_item_to_host_only(ITEMLOT.ThirdWallHuggerDrop)
    skip(5)
    if_number_true_flags_in_range_greater_than_or_equal(3, 11412005, 11412007, 1)
    skip_if_condition_false(2, 3)
    item.award_item_to_host_only(ITEMLOT.SecondWallHuggerDrop)
    skip(1)
    item.award_item_to_host_only(ITEMLOT.FirstWallHuggerDrop)
    flag.enable(dead_flag)
    end()

    network.disable_sync()
    if_entity_health_less_than_or_equal(0, wall_hugger, 0.0)
    network.enable_sync()
    chr.ezstate_ai_request(wall_hugger, 1200, 0)
    restart()


def event11412010():
    """ Death of Bonfire Rockworm enables bonfire interaction. """
    header(11412010)
    skip_if_this_event_off(2)
    map.register_bonfire(11410976, 1411962)
    end()

    if_entity_dead(0, CHR.BonfireWorm)
    map.register_bonfire(11410976, 1411962)


def event11410095():
    """ Golden light wall always disabled. """
    header(11410095)
    flag.enable(11410096)  # Not sure what this does.
    obj.disable(1411710)
    sfx.delete_map_sfx(1411711, False)
    flag.disable(402)   # This flag prevents black phantom invasions (or Kirk, at least) when enabled.


def event11415210():
    """ Stop Egg Bearer praying sounds if eight are dead or Quelaag's Sister is dead (also make hostile). """
    header(11415210, 1)
    if_number_true_flags_in_range_greater_than_or_equal(-1, 11415250, 11415261, 8)
    if_event_flag_on(-1, 140)
    if_condition_true(0, -1)
    sound.disable_map_sound(1413806)


def event11412100():
    """ Egg Bearers don't respawn once killed if Quelaag's Sister is dead - except the one at the cliff edge. """
    header(11412100, 1)
    egg_bearer, = define_args('i')
    skip_if_this_event_slot_off(2)
    chr.disable(egg_bearer)
    end()
    if_event_flag_on(0, 140)
    chr.set_standby_animation_settings_to_default(egg_bearer)
    if_entity_dead(0, egg_bearer)
    end()


def event11411000():
    """ Arrival at Demon Ruins from Tomb of the Giants. """
    header(11411000, 0)
    end_if_event_flag_off(EVENT.ArrivalFromTomb)
    flag.enable(11410410)  # Elevator works. Jeremiah encounters are normal.
    flag.disable(EVENT.ArrivalFromTomb)
    warp.set_player_respawn_point(SPAWN.ArrivalFromTomb)
    network.save_request()
    wait(1.0)
    message.status_explanation(TEXT.DeathlessAura)


def event11410541():
    """ Siegmeyer battle trigger. He now attacks if Jeremiah attacks. """
    header(11410541, 0)
    siegmeyer, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_off(1, EVENT.SiegmeyerHostile)
    if_event_flag_on(1, 1503)
    if_entity_alive(-1, SiegmeyerChaosEaters[0])
    if_entity_alive(-1, SiegmeyerChaosEaters[1])
    if_event_flag_on(-1, EVENT.JeremiahSewerBattleStarted)
    if_condition_true(1, -1)
    if_event_flag_on(1, 11410590)  # Siegmeyer has been spoken to (woken up).

    if_event_flag_off(2, EVENT.SiegmeyerHostile)
    if_event_flag_on(2, 1504)
    if_this_event_on(2)

    if_condition_true(-2, 1)
    if_condition_true(-2, 2)
    if_condition_true(0, -2)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)
    chr.set_standby_animation_settings_to_default(siegmeyer)
    chr.enable(siegmeyer)
    chr.set_team_type_and_exit_standby_animation(siegmeyer, TeamType.fighting_ally)
    chr.set_special_effect(siegmeyer, 90111)


def event11410542():
    """ Sewer battle ended without Siegmeyer's involvement (e.g. because you sniped all the Chaos Eaters).

    Requires Jeremiah to also be dead if Siegmeyer senses an attack incoming. This means that killing the two Chaos
    Eaters before dropping down won't bother Siegmeyer - he'll still join in and wait for Jeremiah's arrival.
    """
    header(11410542, 0)
    siegmeyer, start_flag, end_flag, new_flag = define_args('iiii')

    if_event_flag_off(1, EVENT.SiegmeyerHostile)
    if_event_flag_on(1, 1503)
    if_entity_dead(1, SiegmeyerChaosEaters[0])
    if_entity_dead(1, SiegmeyerChaosEaters[1])
    if_event_flag_off(-1, EVENT.JeremiahSewerBattleStarted)
    if_entity_dead(-1, CHR.JeremiahInSewers)
    if_condition_true(1, -1)
    if_entity_alive(1, siegmeyer)
    if_condition_true(0, 1)

    flag.disable_chunk(start_flag, end_flag)
    flag.enable(new_flag)


def event11410543():
    """ End of sewer battle, but Siegmeyer's health is too low for him to continue to Ash Lake. """
    header(11410543, 0)
    siegmeyer, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, EVENT.SiegmeyerHostile)
    if_event_flag_on(1, 1504)
    if_entity_health_less_than(1, siegmeyer, 0.1)   # lowered from 50% health to 10% health
    if_entity_health_greater_than(1, siegmeyer, 0.0)
    if_entity_dead(1, SiegmeyerChaosEaters[0])
    if_entity_dead(1, SiegmeyerChaosEaters[1])
    if_event_flag_off(-1, EVENT.JeremiahSewerBattleStarted)
    if_entity_dead(-1, CHR.JeremiahInSewers)
    if_condition_true(1, -1)
    if_entity_alive(1, siegmeyer)
    if_condition_true(0, 1)

    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.set_nest(siegmeyer, 1412360)


def event11410544():
    """ End of sewer battle, and Siegmeyer is strong enough to press on. """
    header(11410544, 0)
    siegmeyer, first_flag, last_flag, new_flag = define_args('iiii')
    if_event_flag_off(1, EVENT.SiegmeyerHostile)
    if_event_flag_on(1, 1504)
    if_entity_health_greater_than_or_equal(1, siegmeyer, 0.1)  # lowered from 50% health to 10% health
    if_entity_dead(1, SiegmeyerChaosEaters[0])
    if_entity_dead(1, SiegmeyerChaosEaters[1])
    if_event_flag_off(-1, EVENT.JeremiahSewerBattleStarted)
    if_entity_dead(-1, CHR.JeremiahInSewers)
    if_condition_true(1, -1)
    if_entity_alive(1, siegmeyer)
    if_condition_true(0, 1)

    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.set_nest(siegmeyer, 1412360)


def event11410201():
    """ Bed of Chaos floor breakages. Now all breaks when one orb is destroyed AND Jeremiah is dead (if he ambushed).

    Floor also regenerates on reloads.
    """
    header(11410201, 0)
    floor, break_sound = define_args('ii')

    obj.restore(floor)
    obj.enable_invulnerability(floor)
    if_event_flag_on(1, 11415392)  # Bed battle has started.
    if_number_true_flags_in_range_greater_than_or_equal(1, 11410291, 11410292, 1)  # At least one orb destroyed.
    if_condition_true(0, 1)

    wait(3.0)  # Give Jeremiah a chance to rock up again before checking if he's there.
    if_entity_beyond_distance(2, floor, CHR.Player, 8.0)  # doesn't break under your feet
    if_event_flag_off(-1, EVENT.JeremiahInBedBattle)
    if_event_flag_on(-1, EVENT.JeremiahDeadFromPlayer)
    if_condition_true(2, -1)
    if_condition_true(0, -1)

    wait_random_seconds(0, 1.5)
    obj.disable_invulnerability(floor)
    obj.destroy(floor, 1)
    sfx.create_oneoff_sfx(Category.object, floor, -1, 140008)
    sound.play_sound_effect(floor, SoundType.o_object, break_sound)
    network.disable_sync()
    wait(10)
    obj.disable(floor)


def event11410001():
    """ Bed of Chaos dies. """
    header(11410001)

    if_entity_dead(0, 1410802)
    flag.enable(EVENT.BedOfChaosDead)
    boss.kill_boss(1410800)
    skip_if_client(1)
    game.award_achievement(36)
    game.set_locked_camera_slot_number(14, 1, 0)
    obj.disable(1411990)
    sfx.delete_map_sfx(1411991)
    network.disable_sync()
    # Bonfire disabled, as you could get stuck here without Chthonic Spark.


def event11410600():
    """ Open locked chests with Melted Iron Key. """
    header(11410600)
    chest, obj_act, treasure_taken_flag = define_args('iii')
    skip_if_event_flag_off(4, treasure_taken_flag)
    anim.end_animation(chest, 0)
    obj.disable_activation(chest, -1)
    obj.enable_treasure(chest)
    end()

    obj.disable_treasure(chest)

    if_player_has_good(1, GOOD.MeltedIronKey)
    skip_if_condition_true(5, 1)
    obj.disable_activation(chest, -1)
    if_action_button_state(0, Category.object, chest, 180.0, -1, 2.0, 10010400)
    message.dialog(TEXT.Locked, ButtonType.ok_cancel, NumberButtons.no_button, chest, 5.0)
    wait(3.0)
    restart()

    if_object_activated(0, obj_act)
    message.dialog(TEXT.OpenedWithMeltedIronKey, ButtonType.ok_cancel, NumberButtons.no_button, chest, 5.0)
    wait_frames(10)
    obj.enable_treasure(chest)


def event11415035():
    """ Knight Kirk first invasion trigger. """
    header(11415035)

    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11415036)
    # No longer requires any boss to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 11410810)
    skip_if_this_event_on(1)
    if_player_inside_region(1, 1412010)
    if_condition_true(0, 1)
    flag.disable(402)  # Just in case this was the problem. Prevents this invasion from happening, for some reason.
    message.place_summon_sign(SummonSignType.black_eye_sign, 6560, 1412001, 11415036, 11415037)
    wait(20.0)
    restart()


def event11415038():
    """ Knight Kirk second invasion trigger. """
    header(11415038)
    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11415039)
    # No longer requires any boss to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 11410811)
    skip_if_this_event_on(1)
    if_player_inside_region(1, 1412520)
    if_condition_true(0, 1)
    message.place_summon_sign(SummonSignType.black_eye_sign, 6561, 1412002, 11415039, 11415040)
    wait(20.0)
    restart()


def event11410200():
    """ Bed of Chaos central floor destruction. Jeremiah must be absent. """
    header(11410200)

    FLOOR_SECTIONS = range(1411200, 1411205)

    skip_if_this_event_off(len(FLOOR_SECTIONS) + 1)
    for floor in FLOOR_SECTIONS:
        obj.disable(floor)
    end()

    for floor in FLOOR_SECTIONS:
        obj.restore(floor)
        obj.enable_invulnerability(floor)

    if_event_flag_on(1, 11410291)
    if_event_flag_on(1, 11410292)
    if_player_inside_region(1, 1412100)
    if_event_flag_off(-1, EVENT.JeremiahInBedBattle)
    if_event_flag_on(-1, EVENT.JeremiahDeadFromPlayer)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    # flag.enable(11410200)  # Progress is no longer saved here.
    for floor in FLOOR_SECTIONS:
        obj.disable_invulnerability(floor)

    sfx.create_oneoff_sfx(Category.object, 1411202, -1, 140009)
    for floor, sound_effect, frame_delay in zip(FLOOR_SECTIONS, range(4633, 4638), (4, 3, 2, 1, None)):
        obj.destroy(floor, 1)
        sound.play_sound_effect(floor, SoundType.o_object, sound_effect * 100000)
        if frame_delay is not None:
            wait_frames(frame_delay)

    network.disable_sync()
    wait(10.0)
    obj.disable(1411200)
    obj.disable(1411203)
    obj.disable(1411204)
    # Central floor only remains broken once Bed is dead.
    if_event_flag_on(0, EVENT.BedOfChaosDead)
    end()


def event11415032():
    """ Solaire summon slides into Bed of Chaos battle right after you. """
    header(11415032)
    end_if_this_event_on()

    if_event_flag_on(1, 11415031)  # Solaire has been summoned.
    if_event_flag_on(1, 11415393)  # Bed of Chaos battle has started.
    if_condition_true(0, 1)

    wait(2.0)
    chr.enable_invincibility(CHR.SolaireSummon)
    warp.warp(CHR.SolaireSummon, Category.region, REGION.SlidingIntoBedArena, -1)
    wait(4.0)
    chr.disable_invincibility(CHR.SolaireSummon)


def event11412080():
    """ Monitors when you've rested at the Sanctum of Chaos bonfire for warping. """
    header(11412080)
    if_player_within_distance(1, 1411964, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11412080)


def event11410530():
    """ Solaire now moves to Izalith (bonfire) after you open the Izalith door. """
    header(11410530)
    solaire, first_flag, last_flag, new_flag = define_args('iiii')

    if_event_flag_off(1, 1004)  # Hostile.
    if_event_flag_on(1, 1007)  # At Sunlight Altar.
    if_event_flag_on(1, EVENT.LostIzalithDoorOpened)
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.enable(solaire)


def event11410531():
    """ Solaire goes Hollow in Izalith if you kill the Bed of Chaos before the Sunlight Maggot. """
    header(11410531)
    solaire, first_flag, last_flag, new_flag = define_args('iiii')

    if_event_flag_off(1, EVENT.SolaireHostile)
    if_event_flag_on(1, EVENT.SolaireAtIzalithBonfire)
    if_event_flag_off(1, EVENT.SunlightMaggotDead)
    if_host(1)
    if_event_flag_on(1, EVENT.BedOfChaosDead)  # Instead of area trigger.
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    chr.disable(solaire)
    chr.enable(CHR.SolaireHollow)
    chr.set_team_type_and_exit_standby_animation(CHR.SolaireHollow, TeamType.hostile_ally)
    network.save_request()


def event11410532():
    """ Solaire is saved and moves to the passage if you kill the Bed of Chaos after the Sunlight Maggot. """
    header(11410532)
    solaire, first_flag, last_flag, new_flag = define_args('iiii')

    if_event_flag_off(1, EVENT.SolaireHostile)
    if_event_flag_on(1, EVENT.SolaireAtIzalithBonfire)
    if_event_flag_on(1, EVENT.SunlightMaggotDead)
    if_host(1)
    if_event_flag_on(1, EVENT.BedOfChaosDead)  # Instead of area trigger.
    if_condition_true(0, 1)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(new_flag)
    warp.warp_and_set_floor(solaire, Category.region, 1412500, -1, hitbox_entity_id=1413000)
    flag.enable(11410580)
    if_entity_backread_enabled(0, solaire)
    chr.set_nest(solaire, 1412500)


def event11412011():
    """ Capra Demon ambushes you in sewer tunnel. """
    header(11412011, 1)

    chr.disable(CHR.SewerCapra)
    end_if_this_event_on()

    if_event_flag_on(0, 51410031)  # Sewer corpse looted.
    chr.enable(CHR.SewerCapra)


def event11410120():
    """ Enemy doesn't respawn and drops mandatory loot. """
    header(11410120, 1)
    npc, = define_args('i')
    skip_if_this_event_slot_off(2)
    chr.drop_mandatory_treasure(npc)
    end()

    if_entity_dead(0, npc)
    end()


def event11415030():
    """ Solaire summon sign for Bed of Chaos. """
    header(11415030)

    skip_if_client(1)
    chr.set_network_update_authority(CHR.SolaireSummon, UpdateAuthority.forced)

    skip_if_event_flag_on(3, 11415033)
    if_client(2)
    if_event_flag_on(2, 11415031)
    skip_if_condition_true(1, 2)
    chr.disable(CHR.SolaireSummon)

    end_if_event_flag_on(EVENT.BedOfChaosDead)

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, 1004)  # Solaire not hostile.
    if_event_flag_on(1, 1009)  # Solaire at Izalith bonfire.
    if_entity_backread_enabled(1, CHR.SolaireSummon)
    if_player_within_distance(1, CHR.SolaireSummon, 20.0)
    if_condition_true(0, 1)
    message.place_summon_sign(SummonSignType.blue_eye_sign, CHR.SolaireSummon, 1412000, 11415031, 11415033)


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
