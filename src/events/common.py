
import sys
import inspect
from pydses import *

map_name = 'common'
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'


class DEBUG(IntEnum):
    GET_MASTER_KEY = False  # NOTE: Uses safety chest pool, so also awards other random key items.
    HAS_RUSTBONE = False
    SPEED_UP_PLAYER = False
    GET_CHTHONIC_SPARK = False


class CHR(IntEnum):
    Player = 10000


class EVENT(IntEnum):
    PriscillaDead = 4
    NitoDead = 7
    GwynCinderDead = 15
    FairLadyDead = 140
    VamosDead = 1342
    CiaranGivenSoul = 1862
    CiaranDead = 1864
    SableRuneActive = 11025350
    LustrousRuneActive = 11025351
    WraithRuneActive = 11025352
    ScintillaRuneActive = 11025353
    OmphalicRuneActive = 11025354
    PaleWhiteRuneActive = 11025355
    ReapersRuneActive = 11025356
    RansackersRuneActive = 11025357
    RhythmRuneActive = 11025358
    VelkaPactMade = 1910
    SeathPunished = 1911
    NitoPunished = 1912
    JeremiahPunished = 1913
    XanthousCrownDropped = 1921
    SkeletonsDisturbed = 11312014
    JeremiahDeadFromPlayer = 11412055  # Implies Jeremiah didn't kill the Fair Lady.
    JeremiahDeadNearFairLady = 11412056  # Jeremiah is killed by the Lost Daughter.
    InSeathTowerBattle = 11705098  # Temporarily disables Quella permanent death.
    GwynLordOfLightDead = 11512201
    KremmelPact = 11812035
    ZandroePact = 11812036
    CaithaPact = 11812037
    NahrAlmaPact = 11812038
    QuellaPact = 11812039
    CapriciousThrallActive = 11012010
    CapriciousThrallTrapped = 11012011
    CapriciousThrallDead = 11012012
    AriamisWarp = 11102004
    DarkAnorLondo = 11510400
    EarlyOolacile = 11200007
    OmphalicKillCounter = 2550  # Reserving 2550-2554.
    OmphalicDeathTrigger = 2555
    ReapersKillCounter = 11025500  # Reserving 11025500-11025510.
    RhythmHitCounter = 11025550  # Reserving 11025550-11025554.
    HasBonerust = 11302050
    RansackersRuneItemTrigger = 2560
    LithicWitness = 11502020
    SerousWitness = 11502021
    EmpyreanWitness = 11502022
    BeyondWitness = 11502023
    WarpOptionAtSunChamber = 11512003
    WarpAbilityAtSunChamber = 11512006
    ObtainedChthonicSpark = 11512004
    LordvesselReceived = 11512000
    LordvesselFull = 11800211
    JeremiahInRuins = 11412050
    JeremiahImpatient = 11412051
    JeremiahInIzalith = 11412052
    JeremiahFleeingIzalith = 11412053


class GOOD(IntEnum):
    ChthonicSpark = 813
    Lordvessel = 2510
    PaleEyeOrb = 2530
    PactOfTheChosenUndead = 2540


class RING(IntEnum):
    RingOfTemptation = 127
    RingOfCondemnation = 133
    EtchedRing = 139


class ARMOR(IntEnum):
    CrownOfGold = 294000


class SPEFFECT(IntEnum):
    Petrification = 33
    SoothingSunlight = 570
    Remedy = 1340
    BountifulSunlight = 1430
    KremmelEffect = 1900  # Weapon durability down, stamina recovery down
    ZandroeEffect = 1901  # Gained souls reduced by 80%
    CaithaEffect = 1902  # All defenses are reduced by 80%
    NahrAlmaEffect = 1903  # HP drains (1905), but kills heal (1904)
    NahrAlmaHeal = 1904
    PactPunishment = 1906  # Curses you
    SerousBond = 2022
    BondToBeyond = 2024
    BondToBeyondEffect = 2025
    BondToBeyondWitness = 2026
    RingOfTemptationEquipped = 2131
    RingOfTemptationActive = 2132
    RingOfTemptationDeath = 2133  # Ring breaks, all souls and soft humanity lost
    TwilightRingEquipped = 2111
    TwilightRingWeak = 2112
    TwilightRingMedium = 2113
    TwilightRingStrong = 2114
    RingOfCondemnationEquipped = 2150
    RingOfCondemnationActive = 2151
    RingOfTheEmbraced = 2250
    RingOfTheEmbracedRemoved = 2251  # Takes all souls
    EtchedRingEffect = 2190
    RingOfTheEvilEye = 2240
    KillTrigger = 2241  # Triggered on kills as long as player has a SpEffect with stateInfo = 199
    RingOfTheEvilEyeEffect = 2242
    SunlightElixirEffect = 3000
    AriamisSoulEffect = 3324
    ExileSoulEffect = 3326
    RunicPassive0 = 4700
    RunicPassive1 = 4701
    RunicPassive2 = 4702
    RunicPassive3 = 4703
    RunicPassive4 = 4704
    RunicPassive5 = 4705
    RunicHit0 = 4710
    RunicHit1 = 4711
    RunicHit2 = 4712
    RunicHit3 = 4713
    RunicHit4 = 4714
    RunicHit5 = 4715
    SableRune0 = 4720
    SableRune1 = 4721
    SableRune2 = 4722
    SableRune3 = 4723
    SableRune4 = 4724
    SableRune5 = 4725
    SableRuneTempTrigger = 4726
    LustrousRune0 = 4730
    LustrousRune1 = 4731
    LustrousRune2 = 4732
    LustrousRune3 = 4733
    LustrousRune4 = 4734
    LustrousRune5 = 4735
    WraithRune0 = 4740
    WraithRune1 = 4741
    WraithRune2 = 4742
    WraithRune3 = 4743
    WraithRune4 = 4744
    WraithRune5 = 4745
    WraithRune5Flip = 4746
    OmphalicRune1 = 4751
    OmphalicRune2 = 4752
    OmphalicRune3 = 4753
    OmphalicRune4 = 4754
    OmphalicRune5 = 4755
    PaleWhiteRune = 4760
    SorceryCast = 4761
    ReapersRune0 = 4770
    ReapersRune1 = 4771
    ReapersRune2 = 4772
    ReapersRune3 = 4773
    ReapersRune4 = 4774
    ReapersRune5 = 4775
    RhythmRune0 = 4780
    RhythmRune1 = 4781
    RhythmRune2 = 4782
    RhythmRune3 = 4783
    RhythmRune4 = 4784
    RhythmRune5 = 4785
    RhythmRuneWindow = 4786
    StormfireStackTrigger = 4800
    RuinousHand = 4900
    RuinousHandPayment = 4901
    BonerustHit3Percent = 4910
    BonerustHit5Percent = 4911
    BonerustHit10Percent = 4912
    BonerustHit15Percent = 4913
    BonerustHit20Percent = 4914
    Bonerust = 4920
    GreenMossUsed = 4930
    HollowPenalty = 4999


class ITEMLOT(IntEnum):
    ExileSoulReward = 1620
    GravestalkersReward = 2020
    StrayDemonReward = 2040
    AsylumTyrantReward = 2050
    AriamisReward = 2500
    ThrallReward = 2510
    CrossbreedPriscillaReward = 2520
    MoonlightButterflyReward = 2530
    AbyssArtoriasReward = 2540
    PinwheelReward = 2550
    NitoReward = 2560
    QuelaagReward = 2570
    BedOfChaosReward = 2580
    SensGolemReward = 2590
    GwyndolinReward = 2600
    OrnsteinReward = 2610
    SmoughReward = 2620
    FourKingsReward = 2630
    SeathReward = 2640
    GwynCinderReward = 2650
    AsylumDemonReward = 2660
    CentipedeDemonReward = 2670
    SanctuaryGuardianReward = 2680
    ArtoriasReward = 2690
    ManusReward = 2700
    KalameetReward = 2710
    TaurusDemonReward = 2720
    ProfaneImageReward = 2730
    CeaselessDischargeReward = 2740
    JareelReward = 2750
    BellGargoylesReward = 2760
    GwynLightReward = 2770
    TwilightVagrantReward = 2780
    JeremiahReward = 6770


class TEXT(IntEnum):
    GwynWarpUnlocked = 10010125
    EtchedRingCrumbles = 10010207
    GodOfDreamsStirs = 10010208
    TheDreamEnds = 10010195
    PaleEyeOrbQuivers = 10010737
    AfflictedWithBonerust = 10010779  # ! BONERUST !
    LordvesselWarpUnlocked = 10010124


def event0():
    """ The Great Common Constructor. """
    header(0, 0)
    end_if_client()

    if DEBUG.GET_MASTER_KEY:
        flag.disable(50004066)
        item.award_item_to_host_only(4073)
    if DEBUG.HAS_RUSTBONE:
        flag.enable(EVENT.HasBonerust)
    if DEBUG.SPEED_UP_PLAYER:
        chr.set_special_effect(CHR.Player, 2370)
    if DEBUG.GET_CHTHONIC_SPARK:
        flag.disable(50001510)  # Thrall Spark drop flag.
        item.award_item_to_host_only(ITEMLOT.ThrallReward)

    for flag_id in (760, 762, 765):
        flag.disable(flag_id)

    # Display a message after an event flag is enabled (with optional delay).
    run_event_with_slot(260, 0, args=(11810000, 10010600, 0), arg_types='iif')   # Arrival in Lordran.
    run_event_with_slot(260, 1, args=(257, 10010610, 0), arg_types='iif')   # Rite of Kindling.
    run_event_with_slot(260, 2, args=(EVENT.ObtainedChthonicSpark, 10010620, 0), arg_types='iif')  # Chthonic Spark.
    run_event_with_slot(260, 3, args=(11412053, 10010621, 0), arg_types='iif')  # Chthonic Spark stolen.
    run_event_with_slot(260, 4, args=(EVENT.LordvesselReceived, TEXT.LordvesselWarpUnlocked, 0), arg_types='iif')

    # Assorted events (see documentation). Mostly monitoring states. 710 monitors warping ability.
    for event_id in (761, 763, 290, 701, 702, 717, 718,
                     706, 740, 750, 752, 757, 758, 759,
                     754, 770, 772, 730, 731, 766, 710):
        run_event(event_id)

    # Monitor Lord Souls/Shard possession. Doesn't include Dark Remnant.
    run_event_with_slot(711, 0, args=(2500, 711))  # Gravelord Nito
    run_event_with_slot(711, 1, args=(2501, 712))  # Bed of Chaos
    run_event_with_slot(711, 2, args=(2502, 713))  # Four Kings
    run_event_with_slot(711, 3, args=(2503, 714))  # Seath the Scaleless

    run_event(715)  # Player has Gwyn's Soul.
    run_event(716)  # Player has Sunlight Spear.
    run_event(11512000)  # (New) Player has been given Lordvessel.

    # Monitor Estus upgrade level.
    for slot, args in enumerate(zip(range(202, 215, 2), range(203, 216, 2))):
        run_event_with_slot(8131, slot, args)

    run_event(819)  # Monitor repair box sync.

    run_event(2540)  # (New) Ring of the Embraced punishes you if removed.
    run_event(2541)  # (New) Ring of Temptation activates after 15 seconds.
    run_event(2542)  # (New) Ring of Temptation takes your souls and breaks if you die.
    run_event(2543)  # (New) Ring of the Evil Eye kill reward.
    run_event(2544)  # (New) Twilight Ring effect starts and ends.
    run_event(2545)  # (New) Twilight Ring effect waxes and wanes.
    run_event(2546)  # (New) Bond to Beyond has a 5% chance of giving one soft humanity.
    run_event(2547)  # (New) Contract and heal Bonerust (11302050)
    run_event(2548)  # (New) Kills heal with Nahr Alma pact.
    run_event(2549)  # (New) Ring of Condemnation recharges.
    run_event(11502020)  # (New) Lithic Witness event.
    run_event(11502023)  # (New) Beyond Witness event.

    # (New) Toggles availability of full bonfire menu based on Spark possession.
    run_event(11512005)

    # BOSS DROPS

    for slot, args in enumerate((
            # boss_dead_flag, immediate_item_lot, delayed_item_lot_1, delayed_item_lot_2
            (2,         ITEMLOT.AriamisReward,              9020, 9030),
            (11010901,  ITEMLOT.TaurusDemonReward,          9000, 9030),
            (11010904,  ITEMLOT.ProfaneImageReward,         0, 0),
            (3,         ITEMLOT.BellGargoylesReward,        9020, 0),
            (4,         ITEMLOT.CrossbreedPriscillaReward,  9020, 0),
            (11200900,  ITEMLOT.MoonlightButterflyReward,   9000, 0),
            (11200901,  ITEMLOT.GravestalkersReward,        9030, 0),
            (5,         ITEMLOT.AbyssArtoriasReward,        9000, 0),
            (6,         ITEMLOT.PinwheelReward,             9000, 9030),
            (7,         ITEMLOT.NitoReward,                 9000, 9030),
            (9,         ITEMLOT.QuelaagReward,              9020, 0),
            (11410902,  ITEMLOT.CeaselessDischargeReward,   9000, 9030),
            (11412055,  ITEMLOT.JeremiahReward,             9000, 0),
            (11410901,  ITEMLOT.CentipedeDemonReward,       9000, 9030),
            (10,        ITEMLOT.BedOfChaosReward,           9000, 9030),
            (11,        ITEMLOT.SensGolemReward,            9000, 0),
            (11510900,  ITEMLOT.GwyndolinReward,            0, 0),
            (11510901,  ITEMLOT.JareelReward,               0, 0),
            (11510902,  ITEMLOT.OrnsteinReward,             9000, 0),
            (11510903,  ITEMLOT.SmoughReward,               9000, 0),
            (11012012,  ITEMLOT.ThrallReward,               0, 0),
            (13,        ITEMLOT.FourKingsReward,            9010, 0),
            (14,        ITEMLOT.SeathReward,                9000, 0),
            (11800001,  ITEMLOT.GwynCinderReward,           0, 0),
            (16,        ITEMLOT.AsylumDemonReward,          9000, 0),
            (11810901,  ITEMLOT.StrayDemonReward,           9000, 9030),
            (11810902,  ITEMLOT.AsylumTyrantReward,         9000, 9030),
            (11210000,  ITEMLOT.SanctuaryGuardianReward,    9000, 0),
            (11210001,  ITEMLOT.ArtoriasReward,             0, 0),
            (11212006,  ITEMLOT.ManusReward,                9040, 0),
            (11210004,  ITEMLOT.KalameetReward,             0, 0),
            (11212008,  ITEMLOT.TwilightVagrantReward,      0, 0),
            (11512201,  ITEMLOT.GwynLightReward,            0, 0),
    )):
        run_event_with_slot(1950, slot, args)

    # (New) Monitor Velka's pact. (1910 is enabled in Firelink Shrine.)
    run_event(1915)  # Monitor pact breaking.
    run_event(1916)  # Monitor Seath punishment.
    run_event(1917)  # Monitor Nito punishment.
    run_event(1918)  # Monitor Jeremiah punishment.

    # (New) Monitor challenge pacts.
    run_event(1900)  # Kremmel.
    run_event(1901)  # Zandroe.
    run_event(1902)  # Caitha.
    run_event(1903)  # Nahr Alma.
    run_event(1904)  # Quella permanent Abyss warp.
    run_event(1905)  # Monitor Etched Ring removal and curse player (non-Quella).
    run_event(1906)  # Quella ring removal.

    run_event(1920)  # (New) Return Xanthous Crown on next load when dropped. Uses 1921.
    run_event(1922)  # (New) Warp to special Painted World event when Soul of Ariamis is consumed.
    run_event(1923)  # (New) Award Chaos Fire Whip when Soul of the Exile is consumed.
    run_event(1924)  # (New) Skeletons in Tomb go back to rest when you load a map other than Tomb or Catacombs.
    run_event(1925)  # (New) Manages Dark Ember damage boost stacks.
    run_event(11025400)  # (New) Manages Ruinous Hand kill charge-up.
    run_event(1926)  # (New) Trigger Ruinous Hand explosion at full charge.
    run_event(1927)  # (New) HP penalty for being hollow (25%).

    run_event(2510)  # (New) Sable Rune control.
    run_event(2511)  # (New) Lustrous Rune control.
    run_event(2512)  # (New) Wraith Rune control.
    run_event(2513)  # (New) Scintilla Rune control.
    run_event(2514)  # (New) Omphalic Rune control.
    run_event(2515)  # (New) Omphalic Rune kill counter and death trigger.
    run_event(2516)  # (New) Pale White Rune control.
    run_event(2517)  # (New) Reaper's Rune trigger.
    run_event(2518)  # (New) Reaper's Rune kill counter.
    run_event(2519)  # (New) Rhythm Rune triggers.
    run_event(2520)  # (New) Ransackers Rune trigger.
    # (New) Ransackers Rune item map checks. (2521-2530) (No Kiln, no Asylum.)
    for slot, (block, area) in enumerate(((10, 0), (10, 1), (10, 2), (11, 0), (12, 0), (12, 1),
                                          (13, 0), (13, 1), (13, 2), (14, 0), (14, 1), (15, 0),
                                          (15, 1), (16, 0), (17, 0))):
        args = tuple([block, area] + [50000 + 100 * slot + 10 * i for i in range(0, 10)])
        run_event_with_slot(2521, slot, args=args, arg_types='BBiiiiiiiiii')
        
    # Activate Runes.
    for slot, rune in enumerate(range(9)):
        run_event_with_slot(2600, slot, args=(90 + rune, 11025350 + rune))

    # Monitor availability of bonfire options
    for slot, args in enumerate(zip(range(2600, 2610), range(250, 260))):
        run_event_with_slot(250, slot, args)

    # Remove Embers from inventory when given to blacksmiths. These are removed aggressively and repeatedly!
    for slot_args in zip((0, 1, 2, 6, 7, 8, 9, 10, 12),
                         zip((350, 351, 352, 356, 357, 358, 359, 360, 362),
                             (800, 801, 802, 806, 807, 808, 809, 810, 812))):
        run_event_with_slot(350, slot_args[0], slot_args[1])

    # (NEW) Chthonic Spark version of the above event, which also requires Vamos to be alive.
    run_event_with_slot(363, 0, args=(363, 813))

    # Monitor reinforcement material possession.
    for slot, args in enumerate(zip(range(1000, 1131, 10), range(780, 794))):
        run_event_with_slot(780, slot, args)

    # Monitor covenant membership.
    for slot, args in enumerate(zip(range(0, 10), range(850, 860))):
        run_event_with_slot(870, slot, args)

    # Covenant joining events. (args = trigger_flag, player_animation, rotation_target, looping_animation)
    for slot, args in enumerate(zip(range(840, 850), (7905, 7905, 7905, 7905, 7898, 7905, 7905, 7913, 7905, 7905),
                                    (6370, 6072, 6080, 6001, 10000, 6340, 6341, 10000, 6380, 1400700),
                                    (-1, -1, -1, -1, 7896, -1, -1, 7911, -1, -1))):
        run_event_with_slot(840, slot, args)

    # Monitor NG+ level. Uses flags 690 (NG) to 705 (NG+15).
    run_event_with_slot(690, 0, args=(600, 4, 16, 1175))

    run_event(719)  # Monitor possession of any spell.
    run_event(720)  # Monitor possession of any pyromancy.

    # Monitor whether shops are sold out.
    # NOTE: This all suggests that shopkeeper flags are in the 7000 range for their area. Avoid!
    run_event(721)  # Big Hat Logan in Duke's Archives.
    run_event(722)  # Quelana of Izalith.
    run_event(723)  # Griggs at Firelink Shrine.
    run_event(724)  # Male Undead Merchant. (I don't think this does anything.)
    run_event(725)  # Checks if you've bought 2+ items from Logan in Duke's Archives.
    run_event(726)  # Checks if you've bought 2+ items from Ingward in New Londo Ruins.
    run_event(727)  # Checks flags in Ash Lake / Great Hollow. Not sure who this is.

    run_event(745)  # Cut Shiva questline I think.
    run_event(818)  # Black Eye Orb quivers in Anor Londo.
    run_event(810)  # Monitor possession of Lautrec's Black Eye Orb.
    # Lautrec frees himself from New Londo if both item flags below are enabled.
    run_event_with_slot(812, 0, args=(51400150,))  # Monitor possession of Blighttown Fire Keeper Soul (moved).
    run_event_with_slot(812, 1, args=(51010050,))  # Monitor possession of Undead Parish Humanity (still on altar).
    run_event(822)  # Disable flag 830 half a second after leaving the Kiln. (Frampt pickup.)
    run_event(823)  # Disable flag 831 half a second after leaving the Kiln. (Kaathe pickup.)

    # (New) Monitor dead NPCs for Twilight Vagrant. Counts friendly or hollow death, unless noted otherwise.
    for slot, npc_dead_flag in enumerate((
            1073,  # 2051: Oscar (friendly) (must be enabled in tutorial)
            1097,  # 2052: Big Hat Logan
            1115,  # 2053: Griggs
            1005,  # 2054: Solaire (note this won't trigger if he is killed when Hollow, unlike other NPCs)
            1254,  # 2055: Laurentius
            1462,  # 2056: Crestfallen Warrior
            1575,  # 2057: Lautrec
            1604,  # 2058: Shiva
            1628,  # 2059: Patches
            1899,  # 2060: Havel
            1864,  # 2061: Ciaran (in Oolacile and/or with Nito)
            1823,  # 2062: Hawkeye Gough
            5,     # 2063: Artorias (in Darkroot)
    )):
        run_event_with_slot(11212050, slot + 1, args=(npc_dead_flag,))

    # (New) Monitor Tomb of the Giants presence to send Giant Skeletons back to sleep.
    run_event(11310201)

    # (New) Monitor picking up Chthonic Spark for the first time to display message.
    run_event(11512004)

    # EVENT REWARDS (covenants, storylines)

    run_event_with_slot(910, 0, args=(11400591, 1280))  # Joining Chaos Servants.
    run_event_with_slot(911, 0, args=(11010591, 1000, 1), arg_types='iiB')
    run_event_with_slot(911, 1, args=(11510590, 1010, 1), arg_types='iiB')
    run_event_with_slot(911, 2, args=(11700591, 1020, 1), arg_types='iiB')
    run_event_with_slot(911, 3, args=(11000591, 1030, 1), arg_types='iiB')
    run_event_with_slot(911, 4, args=(11400590, 1040, 1), arg_types='iiB')
    run_event_with_slot(911, 5, args=(11410594, 1050, 1), arg_types='iiB')
    run_event_with_slot(911, 6, args=(11020594, 1060, 1), arg_types='iiB')
    run_event_with_slot(911, 7, args=(11020595, 1070, 1), arg_types='iiB')
    run_event_with_slot(911, 8, args=(11810590, 1082, 1), arg_types='iiB')
    run_event_with_slot(911, 9, args=(11810591, 1080, 1), arg_types='iiB')
    run_event_with_slot(911, 10, args=(11510592, 1090, 1), arg_types='iiB')
    run_event_with_slot(911, 11, args=(11600592, 1100, 1), arg_types='iiB')
    run_event_with_slot(911, 12, args=(11020602, 1110, 1), arg_types='iiB')
    run_event_with_slot(911, 13, args=(11010594, 1120, 1), arg_types='iiB')
    run_event_with_slot(911, 14, args=(11010595, 1130, 1), arg_types='iiB')
    run_event_with_slot(911, 15, args=(11020599, 1140, 1), arg_types='iiB')
    run_event_with_slot(911, 16, args=(11020607, 1150, 1), arg_types='iiB')
    run_event_with_slot(911, 17, args=(11200592, 1160, 1), arg_types='iiB')
    run_event_with_slot(911, 18, args=(11200593, 1170, 1), arg_types='iiB')
    run_event_with_slot(911, 19, args=(11200594, 1180, 1), arg_types='iiB')
    run_event_with_slot(911, 20, args=(11300590, 1190, 1), arg_types='iiB')
    run_event_with_slot(911, 21, args=(11300591, 1200, 1), arg_types='iiB')
    run_event_with_slot(911, 22, args=(11310590, 1210, 1), arg_types='iiB')
    run_event_with_slot(911, 23, args=(11310592, 1220, 1), arg_types='iiB')
    run_event_with_slot(911, 24, args=(11310593, 1230, 1), arg_types='iiB')
    run_event_with_slot(911, 25, args=(11310594, 1240, 1), arg_types='iiB')
    run_event_with_slot(911, 26, args=(11320590, 1250, 1), arg_types='iiB')
    run_event_with_slot(911, 27, args=(11320581, 1260, 1), arg_types='iiB')
    run_event_with_slot(911, 28, args=(11320593, 1270, 1), arg_types='iiB')
    run_event_with_slot(911, 29, args=(11400592, 1290, 1), arg_types='iiB')
    run_event_with_slot(911, 30, args=(11400594, 1300, 1), arg_types='iiB')
    run_event_with_slot(911, 31, args=(11400596, 1310, 1), arg_types='iiB')
    run_event_with_slot(911, 32, args=(11400597, 1320, 1), arg_types='iiB')
    run_event_with_slot(911, 33, args=(11400598, 1330, 1), arg_types='iiB')
    run_event_with_slot(911, 34, args=(11400599, 1340, 1), arg_types='iiB')
    run_event_with_slot(911, 35, args=(11510595, 1350, 1), arg_types='iiB')
    run_event_with_slot(911, 36, args=(11510596, 1360, 1), arg_types='iiB')
    run_event_with_slot(911, 37, args=(11510597, 1370, 1), arg_types='iiB')
    run_event_with_slot(911, 38, args=(11600594, 1380, 1), arg_types='iiB')
    run_event_with_slot(911, 39, args=(11600595, 1390, 1), arg_types='iiB')
    run_event_with_slot(911, 40, args=(11600596, 1400, 1), arg_types='iiB')
    run_event_with_slot(911, 41, args=(11010598, 1410, 0), arg_types='iiB')
    run_event_with_slot(911, 42, args=(11210590, 1500, 1), arg_types='iiB')
    run_event_with_slot(911, 43, args=(11210593, 1510, 1), arg_types='iiB')
    run_event_with_slot(911, 44, args=(11210594, 1520, 1), arg_types='iiB')
    run_event_with_slot(911, 45, args=(11600580, 1401, 1), arg_types='iiB')
    run_event_with_slot(911, 46, args=(11600581, 1402, 1), arg_types='iiB')
    run_event_with_slot(911, 47, args=(11600582, 1403, 1), arg_types='iiB')
    run_event_with_slot(911, 48, args=(11600583, 1404, 1), arg_types='iiB')
    run_event_with_slot(890, 0, args=(11310580, 1221, 1), arg_types='iiB')   # 911 ran out of slots (up against 960).
    run_event_with_slot(890, 1, args=(11510580, 1361, 1), arg_types='iiB')
    run_event_with_slot(890, 2, args=(11510581, 1371, 1), arg_types='iiB')
    run_event_with_slot(890, 3, args=(11320592, 1261, 1), arg_types='iiB')

    # DIRECT NPC DEATH REWARDS (960-969)
    run_event_with_slot(960, 0, args=(1315, 6180, 1100))  # Ingward (Key to the Seal)
    run_event_with_slot(960, 1, args=(1402, 6230, 6230))  # Undead Merchant (Orange Soapstone)
    # run_event_with_slot(960, 2, args=(1198, 6080, 1140))  # Petrus (Lift Chamber Key) (dies before killing Rhea)
    # run_event_with_slot(960, 3, args=(1196, 6080, 1140))  # Petrus (Lift Chamber Key) (dies after killing Rhea)

    # NEW GAME PLUS: Bring covenant ranks up to date, and prevent gifts from being re-awarded.
    run_event_with_slot(8200, 0, args=(3, 5500, 50000120, 11010594))
    run_event_with_slot(8200, 1, args=(3, 5510, 50000130, 11010595))
    run_event_with_slot(8200, 2, args=(2, 103, 50000160, 11200592))
    run_event_with_slot(8200, 3, args=(3, 240, 50000170, 11200593))
    run_event_with_slot(8200, 4, args=(2, 124, 50000180, 11200594))
    run_event_with_slot(8200, 5, args=(0, 453000, 50000220, 11310592))
    run_event_with_slot(8200, 6, args=(3, 5100, 50000225, 11310580))
    run_event_with_slot(8200, 7, args=(3, 5110, 50000230, 11310593))
    run_event_with_slot(8200, 8, args=(3, 114, 50000265, 11320581))
    run_event_with_slot(8200, 9, args=(3, 377, 50000260, 11320592))
    run_event_with_slot(8200, 10, args=(3, 378, 50000270, 11320593))
    run_event_with_slot(8200, 11, args=(3, 4500, 50000310, 11400596))
    run_event_with_slot(8200, 12, args=(3, 4520, 50000320, 11400597))
    run_event_with_slot(8200, 13, args=(3, 4510, 50000330, 11400598))
    run_event_with_slot(8200, 14, args=(2, 130, 50000350, 11510595))
    run_event_with_slot(8200, 15, args=(3, 113, 50000360, 11510596))
    run_event_with_slot(8200, 16, args=(2, 102, 50000365, 11510580))
    run_event_with_slot(8200, 17, args=(3, 5910, 50000370, 11510597))
    run_event_with_slot(8200, 18, args=(0, 1366000, 50000375, 11510581))
    run_event_with_slot(8200, 19, args=(0, 904000, 50000380, 11600594))
    run_event_with_slot(8200, 20, args=(3, 102, 50000390, 11600595))
    run_event_with_slot(8200, 21, args=(0, 210000, 50000400, 11600596))
    run_event_with_slot(8200, 22, args=(1, 40000, 50000410, 11600580))
    run_event_with_slot(8200, 23, args=(1, 41000, 50000420, 11600581))
    run_event_with_slot(8200, 24, args=(1, 42000, 50000430, 11600582))
    run_event_with_slot(8200, 25, args=(1, 43000, 50000440, 11600583))

    # Same as above, but for other special rewards.
    run_event_with_slot(8300, 0, args=(ItemType.good, 100, 50000000))  # White Sign Soapstone
    run_event_with_slot(8300, 1, args=(ItemType.good, 101, 51100330))  # Red Sign Soapstone
    run_event_with_slot(8300, 2, args=(ItemType.good, 102, 50000390))  # Red Eye Orb
    run_event_with_slot(8300, 3, args=(ItemType.good, 106, 11017020))  # Orange Guidance Soapstone
    run_event_with_slot(8300, 4, args=(ItemType.good, 108, 11607020))  # Book of the Guilty
    run_event_with_slot(8300, 5, args=(ItemType.good, 112, 11407080))  # Servant Roster
    run_event_with_slot(8300, 6, args=(ItemType.good, 2508, 11007010))  # Unknown - seems unused.
    run_event_with_slot(8300, 7, args=(ItemType.good, 2508, 11007010))  # Unknown - seems unused.
    run_event_with_slot(8300, 8, args=(ItemType.good, 2508, 11007010))  # Unknown - seems unused.
    run_event_with_slot(8300, 9, args=(ItemType.good, 2508, 11007010))  # Unknown - seems unused.

    # NOTE: Flag 8310 onwards is used for NPC humanity registration.

    # Same as above for DLC items.
    run_event_with_slot(8090, 0, args=(ItemType.good, 510, 11217010))
    run_event_with_slot(8090, 1, args=(ItemType.good, 511, 11217020))
    run_event_with_slot(8090, 2, args=(ItemType.good, 512, 11217030))
    run_event_with_slot(8090, 3, args=(ItemType.good, 513, 11217040))
    run_event_with_slot(8090, 4, args=(ItemType.good, 514, 11217050))

    # (New) Same as above, but for Runes and other new items.
    run_event_with_slot(11022100, 0, args=(ItemType.good, 900, 51010020))
    run_event_with_slot(11022100, 1, args=(ItemType.good, 901, 51510690))
    run_event_with_slot(11022100, 2, args=(ItemType.good, 902, 51200120))
    run_event_with_slot(11022100, 3, args=(ItemType.good, 903, 51410030))
    run_event_with_slot(11022100, 4, args=(ItemType.good, 904, 51810080))
    run_event_with_slot(11022100, 5, args=(ItemType.good, 905, 51700020))
    run_event_with_slot(11022100, 6, args=(ItemType.good, 906, 51300220))
    run_event_with_slot(11022100, 7, args=(ItemType.good, 907, 51300221))
    run_event_with_slot(11022100, 8, args=(ItemType.good, 908, 51210290))
    run_event_with_slot(11022100, 9, args=(ItemType.ring, 133, 50000650))  # Velka gift (Ring of Condemnation)
    run_event_with_slot(11022100, 10, args=(ItemType.ring, 124, 50001780))  # Twilight Vagrant drop (Twilight Ring)
    run_event_with_slot(11022100, 11, args=(ItemType.ring, 105, 50004900))  # Lithic Bond
    run_event_with_slot(11022100, 12, args=(ItemType.ring, 107, 50004910))  # Serous Bond
    run_event_with_slot(11022100, 13, args=(ItemType.ring, 106, 50004920))  # Empyrean Bond
    run_event_with_slot(11022100, 14, args=(ItemType.ring, 108, 50004930))  # Bond to Beyond
    # Leaving slots 11022100-11022119 dedicated to this.

    # (NEW) Remove some additional new items in NG+.
    run_event_with_slot(11022120, 0, args=(ItemType.ring, 152))  # Ashen Ring
    run_event_with_slot(11022120, 1, args=(ItemType.ring, 151))  # Gwynevere's Ring
    run_event_with_slot(11022120, 2, args=(ItemType.good, 220))  # Silver Pendant
    run_event_with_slot(11022120, 3, args=(ItemType.armor, 294000))  # Xanthous Crown (true)
    run_event_with_slot(11022120, 4, args=(ItemType.ring, 149))  # Darkmoon Seance Ring


def event50():
    """ Common pre-constructor. Mostly just initializes NPC storyline flags. """
    header(50)
    skip_if_event_flag_on(86, 909)
    for chunk_start, chunk_end, initial_flag in (
            (1000, 1029, 1000),
            (1030, 1059, 1030),
            (1060, 1089, 1060),
            (1090, 1109, 1090),
            (1110, 1119, 1110),
            (1120, 1139, 1120),
            (1140, 1169, 1140),
            (1170, 1189, 1170),
            (1190, 1209, 1202),
            (1210, 1219, 1210),
            (1220, 1229, 1220),
            (1230, 1239, 1230),
            (1240, 1249, 1240),
            (1250, 1259, 1250),
            (1270, 1279, 1270),
            (1280, 1289, 1280),
            (1290, 1309, 1290),
            (1310, 1319, 1310),
            (1320, 1339, 1320),
            (1340, 1359, 1340),
            (1360, 1379, 1360),
            (1380, 1399, 1380),
            (1400, 1409, 1400),
            (1410, 1419, 1410),
            (1420, 1429, 1420),
            (1430, 1459, 1430),
            (1460, 1489, 1460),
            (1490, 1539, 1490),
            (1540, 1569, 1540),
            (1570, 1599, 1570),
            (1600, 1619, 1600),
            (1620, 1639, 1620),  # Trusty Patches
            (1640, 1669, 1640),
            (1670, 1679, 1670),
            (1690, 1699, 1690),
            (1700, 1709, 1700),
            (1710, 1729, 1710),
            (1760, 1769, 1760),
            (1770, 1779, 1770),
            (1780, 1789, 1780),
            (1820, 1839, 1820),
            (1840, 1859, 1840),
            (1860, 1869, 1860),
            (1870, 1889, 1870),
            (1890, 1899, 1890),  # (New) Havel the Rock
            (11412020, 11412029, 11412020),  # (New) Lost Daughter of Izalith
            (11412050, 11412059, 11412050),  # (New) Xanthous King Jeremiah
    ):
        skip_if_event_flag_range_not_all_off(1, chunk_start, chunk_end)
        flag.enable(initial_flag)

    skip_if_event_flag_on(24, 909)
    for new_game_flag in range(11807020, 11807241, 10):
        if new_game_flag in (11807140, 11807150, 11807160):
            continue  # not used
        flag.enable(new_game_flag)
    for new_game_flag_dlc in range(11217060, 11217091, 10):
        flag.enable(new_game_flag_dlc)

    # Some first-time initialization of flags (once per playthrough).
    end_if_event_flag_on(909)
    flag.enable(909)  # NPC initialization is done for this playthrough.
    flag.enable(814)  # Not sure.
    flag.enable(50006071)  # Rhea won't drop Pendant.
    flag.enable(50006080)  # Petrus won't drop Ivory Talisman (because he hasn't killed Rhea).
    flag.enable(50006771)  # Jeremiah won't drop Chthonic Spark (because he didn't steal it yet).
    flag.enable(51300992)  # Vamos won't drop Chthonic Spark (because he hasn't been given it yet).
    flag.enable(11607030)  # Oswald won't sell Velka's Rapier (because you haven't made a pact with Velka yet).
    flag.enable(51100371)  # Profane Ember drop is disabled (because you haven't made a pact with Velka yet).
    flag.enable(51300220)  # Reaper's Rune won't appear.
    flag.enable(51300221)  # Ransacker's Rune won't appear.

    # Disable Etched Ring pickup in starting cell unless it is NG+ and the player doesn't have one already.
    if_new_game_count_greater_than_or_equal(7, 1)
    if_player_does_not_have_ring(7, RING.EtchedRing)
    end_if_condition_true(7)
    flag.enable(51810001)


def event706():
    """ Disable warp ABILITY in Painted World, Duke's prison, Dark Anor Londo (while Jareel is alive),
    and the Sanctum of Chaos. """
    header(706, 0)

    if_event_flag_on(-1, 710)
    if_event_flag_on(-1, EVENT.WarpAbilityAtSunChamber)
    if_condition_true(0, -1)

    flag.enable(706)  # Enable warping.

    # WARPING IS ACTIVE WHILE PENDING HERE.

    if_event_flag_on(-1, 11705170)  # Player in Archive Tower ...
    if_in_world_area(-1, 11, 0)  # OR player in Painted World ...
    if_in_world_area(7, 15, 1)  # OR (Player in Anor Londo AND Dark Anor Londo active AND Jareel not dead)
    if_event_flag_on(7, 11510400)
    if_event_flag_off(7, 11510901)
    if_condition_true(-1, 7)
    if_in_world_area(6, 14, 1)  # OR (Player in Lost Izalith AND Jeremiah present)
    if_event_flag_on(-2, EVENT.JeremiahInRuins)
    if_event_flag_on(-2, EVENT.JeremiahInIzalith)
    if_event_flag_on(-2, EVENT.JeremiahImpatient)
    if_event_flag_on(-2, EVENT.JeremiahFleeingIzalith)
    if_condition_true(6, -2)
    if_condition_true(-1, 6)
    if_condition_true(0, -1)
    flag.disable(706)

    # WARPING IS NOT ACTIVE WHILE PENDING HERE.

    if_event_flag_off(1, 11705170)  # Player not in Archive Tower ...
    if_not_in_world_area(1, 11, 0)   # AND player not in Painted World ...
    if_not_in_world_area(-7, 15, 1)  # AND (player not in AL OR not Dark Anor Londo OR Jareel dead)
    if_event_flag_off(-7, 11510400)
    if_event_flag_on(-7, 11510901)
    if_condition_true(1, -7)
    if_not_in_world_area(-6, 14, 1)  # AND (player not in Izalith OR Jeremiah gone)
    if_event_flag_off(2, EVENT.JeremiahInRuins)
    if_event_flag_off(2, EVENT.JeremiahInIzalith)
    if_event_flag_off(2, EVENT.JeremiahImpatient)
    if_event_flag_off(2, EVENT.JeremiahFleeingIzalith)
    if_condition_true(-6, 2)
    if_condition_true(1, -6)
    if_condition_true(0, 1)
    restart()


def event710():
    """ Determines appearance of warp OPTION in bonfire menu. (Continuously updates.) """
    header(710, 0)

    if_player_does_not_have_good(1, GOOD.ChthonicSpark)
    if_event_flag_off(1, EVENT.LordvesselReceived)
    if_condition_true(-1, 1)
    if_event_flag_off(-1, 710)
    if_condition_true(0, -1)
    flag.disable(710)

    if_player_has_good(-2, GOOD.ChthonicSpark)
    if_event_flag_on(-2, EVENT.LordvesselReceived)
    if_event_flag_on(-2, 710)
    if_condition_true(0, -2)
    flag.enable(710)
    restart()


def event11212050():
    """ Monitor dead NPCs for Twilight Vagrant. Just copies the 14 flags into a contiguous range. """
    npc_dead_flag, = define_args('i')
    header(11212050)
    end_if_this_event_slot_on()
    if_event_flag_on(0, npc_dead_flag)
    end()


def event1915():
    """ Monitor breaking of Velka's pact. """
    header(1915, 0)

    end_if_this_event_on()

    if_event_flag_on(1, EVENT.VelkaPactMade)
    if_event_flag_on(-1, EVENT.PriscillaDead)
    if_event_flag_on(-1, EVENT.FairLadyDead)
    if_event_flag_on(-1, EVENT.CiaranDead)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    flag.disable(EVENT.VelkaPactMade)
    item.remove_items_from_player(ItemType.good, GOOD.PactOfTheChosenUndead, 0)  # Remove Pact of the Chosen Undead.
    # Removed curse punishment. Way too annoying.
    skip_if_event_flag_off(1, EVENT.PriscillaDead)
    wait(3.0)  # Extra wait time if it was Priscilla who died (for victory banner).
    wait(1.0)
    message.status_explanation(10010604, True)


def event1916():
    """ Monitor Seath's punishment. """
    header(1916, 0)

    end_if_this_event_on()

    if_event_flag_on(-1, 1911)  # Enabled manually when you kill Seath at Ash Lake.
    if_event_flag_on(-1, 50006586)  # Pick up Havel's Ring after he kills Seath at Ash Lake.
    if_condition_true(0, -1)

    if_event_flag_on(2, EVENT.VelkaPactMade)
    if_event_flag_off(2, EVENT.PriscillaDead)
    skip_if_condition_false(2, 2)
    message.status_explanation(10010605, True)
    flag.enable(EVENT.SeathPunished)


def event1917():
    """ Monitor Nito's punishment. """
    header(1917, 0)

    end_if_this_event_on()

    if_event_flag_on(1, EVENT.NitoDead)
    if_event_flag_on(1, EVENT.CiaranGivenSoul)
    if_condition_true(0, 1)

    skip_if_event_flag_off(2, EVENT.VelkaPactMade)
    message.status_explanation(10010606, True)
    flag.enable(EVENT.NitoPunished)


def event1918():
    """ Monitor Jeremiah's punishment. """
    header(1918, 0)

    end_if_this_event_on()

    if_event_flag_on(-1, EVENT.JeremiahDeadFromPlayer)
    if_event_flag_on(1, EVENT.JeremiahDeadNearFairLady)
    if_event_flag_on(1, 50006770)  # Jeremiah looted.
    if_condition_true(-1, 1)
    if_condition_true(0, -1)

    if_event_flag_on(2, EVENT.VelkaPactMade)
    if_event_flag_off(2, EVENT.FairLadyDead)  # Fair Lady NOT dead.
    skip_if_condition_false(2, 2)
    message.status_explanation(10010607, True)
    flag.enable(EVENT.JeremiahPunished)


def event11310201():
    """ Skeletons in Tomb of the Giants stop being disturbed if you leave the area. """
    header(11310201)
    if_event_flag_on(1, EVENT.SkeletonsDisturbed)
    if_not_in_world_area(1, 13, 1)
    if_condition_true(0, 1)
    flag.disable(EVENT.SkeletonsDisturbed)


def event1900():
    """ Monitor pact with Kremmel, God of Struggles. """
    header(1900, 1)
    if_event_flag_on(0, EVENT.KremmelPact)
    chr.set_special_effect(CHR.Player, SPEFFECT.KremmelEffect)
    if_event_flag_on(0, 1905)
    flag.disable(EVENT.KremmelPact)
    end()


def event1901():
    """ Monitor pact with Zandroe, God of Greed. """
    header(1901, 1)
    if_event_flag_on(0, EVENT.ZandroePact)
    chr.set_special_effect(CHR.Player, SPEFFECT.ZandroeEffect)
    if_event_flag_on(0, 1905)
    flag.disable(EVENT.ZandroePact)
    end()


def event1902():
    """ Monitor pact with Caitha, God of Tears. """
    header(1902, 1)
    if_event_flag_on(0, EVENT.CaithaPact)
    chr.set_special_effect(CHR.Player, SPEFFECT.CaithaEffect)
    if_event_flag_on(0, 1905)
    flag.disable(EVENT.CaithaPact)
    end()


def event1903():
    """ Monitor pact with Nahr Alma, God of Blood. """
    header(1903, 1)
    if_event_flag_on(0, EVENT.NahrAlmaPact)
    chr.set_special_effect(CHR.Player, SPEFFECT.NahrAlmaEffect)
    if_event_flag_on(0, 1905)
    flag.disable(EVENT.NahrAlmaPact)
    end()


def event2548():
    """ Kills heal with Nahr Alma pact active. """
    header(2548)
    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)

    if_player_has_special_effect(1, SPEFFECT.NahrAlmaEffect)
    if_player_has_special_effect(1, SPEFFECT.KillTrigger)
    if_condition_true(0, 1)

    chr.set_special_effect(CHR.Player, SPEFFECT.NahrAlmaHeal)
    restart()


def event1904():
    """ Player dies after making pact with Quella, God of Dreams. """
    header(1904)
    end_if_this_event_on()
    if_event_flag_on(1, EVENT.QuellaPact)
    if_event_flag_off(1, EVENT.InSeathTowerBattle)
    if_event_flag_on(-1, 1906)  # Player took off ring.
    if_entity_health_less_than_or_equal(-1, CHR.Player, 0.0)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    item.remove_items_from_player(ItemType.ring, RING.EtchedRing, 0)
    flag.enable(1904)
    network.save_request()
    message.status_explanation(TEXT.TheDreamEnds, False)
    warp.warp_player(16, 0, 1600970)


def event1905():
    """ Monitor Etched Ring removal (except if you have Quella). """
    header(1905)
    end_if_this_event_on()

    if_event_flag_off(1, EVENT.QuellaPact)
    if_event_flag_on(-1, EVENT.KremmelPact)
    if_event_flag_on(-1, EVENT.ZandroePact)
    if_event_flag_on(-1, EVENT.CaithaPact)
    if_event_flag_on(-1, EVENT.NahrAlmaPact)
    if_condition_true(1, -1)
    if_player_does_not_have_special_effect(1, SPEFFECT.EtchedRingEffect)
    if_condition_true(0, 1)

    item.remove_items_from_player(ItemType.ring, RING.EtchedRing, 0)
    wait(1.0)
    chr.set_special_effect(CHR.Player, SPEFFECT.PactPunishment)
    flag.disable(EVENT.QuellaPact)
    flag.disable(EVENT.KremmelPact)
    flag.disable(EVENT.ZandroePact)
    flag.disable(EVENT.CaithaPact)
    flag.disable(EVENT.NahrAlmaPact)


def event1906():
    """ Monitor pact with Quella, God of Dreams. """
    header(1906)
    end_if_event_flag_on(1904)
    if_event_flag_on(1, EVENT.QuellaPact)
    if_player_does_not_have_special_effect(1, SPEFFECT.EtchedRingEffect)
    if_condition_true(0, 1)
    wait(5.0)
    message.status_explanation(TEXT.GodOfDreamsStirs, True)  # Won't show if you're still in the menu.
    wait(5.0)
    if_player_does_not_have_special_effect(7, SPEFFECT.EtchedRingEffect)
    restart_if_condition_false(7)
    end()


def event1920():
    """ Xanthous Crown returns to you on next load when dropped. """
    header(1920)
    end_if_event_flag_on(51810980)  # Malevolence obtained.
    end_if_event_flag_on(11810619)  # Snuggly trade event.

    skip_if_event_flag_off(4, EVENT.XanthousCrownDropped)
    wait(3.0)
    flag.disable(50006770)
    flag.disable(EVENT.XanthousCrownDropped)
    item.award_item_to_host_only(ITEMLOT.JeremiahReward)

    if_player_owns_armor(0, ARMOR.CrownOfGold)
    if_player_does_not_own_armor(1, ARMOR.CrownOfGold)
    if_event_flag_off(1, 51810980)  # Malevolence trade not picked up.
    if_condition_true(0, 1)
    flag.enable(EVENT.XanthousCrownDropped)


def event1922():
    """ Warp to Painted World when you consume the Soul of Ariamis. """
    header(1922)
    end_if_this_event_on()
    if_player_has_special_effect(0, SPEFFECT.AriamisSoulEffect)
    flag.enable(EVENT.AriamisWarp)
    warp.warp_player(11, 0, 1100990)


def event1923():
    """ Award Chaos Fire Whip when Soul of the Exile is consumed. """
    header(1923)
    end_if_this_event_on()
    if_player_has_special_effect(0, SPEFFECT.ExileSoulEffect)
    item.award_item_to_host_only(ITEMLOT.ExileSoulReward)


def event1924():
    """ Skeletons in Tomb of the Giants go back to rest. """
    header(1924)
    if_not_in_world_area(1, 13, 0)
    if_not_in_world_area(1, 13, 1)
    if_condition_true(0, 1)
    flag.disable(11310201)


def event1950():
    """ Replaces 970 due to more slots available. Note that 970-999, roughly, are now free. """
    header(1950)
    boss_dead_flag, immediate_item, delayed_item_1, delayed_item_2 = define_args('iiii')
    end_if_event_flag_on(boss_dead_flag)
    if_event_flag_on(0, boss_dead_flag)
    skip_if_equal(1, immediate_item, 0)
    item.award_item_to_host_only(immediate_item)
    network.disable_sync()
    wait(5.0)
    skip_if_equal(1, delayed_item_1, 0)
    item.award_item_to_host_only(delayed_item_1)
    skip_if_equal(1, delayed_item_2, 0)
    item.award_item_to_host_only(delayed_item_2)


def event1925():
    """ Manages Stormfire fire damage stacks. """
    header(1925)

    if_player_has_special_effect(0, SPEFFECT.StormfireStackTrigger)

    for condition, stack_id in zip(range(1, 6), range(4801, 4806)):
        if_player_has_special_effect(condition, stack_id)
        skip_if_condition_true(3, condition)
        chr.set_special_effect(CHR.Player, stack_id)
        if_player_does_not_have_special_effect(0, SPEFFECT.StormfireStackTrigger)
        restart()

    # Stacks are maxed out; do nothing this hit.
    restart()


def event11025400():
    """ Increment Ruinous Hand kills with temporary flags. """
    header(11025400)

    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)

    if_player_has_special_effect(1, SPEFFECT.RuinousHand)
    if_player_has_special_effect(1, SPEFFECT.KillTrigger)
    if_condition_true(0, 1)

    restart_if_event_flag_on(11025405)  # Already at max charge.

    for current_flag in range(11025405, 11025400, -1):
        skip_if_event_flag_off(2, current_flag)
        flag.enable(current_flag + 1)
        restart()

    # If above four increment checks fail, enable first charge.
    flag.enable(11025401)
    restart()


def event1926():
    """ Create explosion when player uses Ruinous Hand strong attack at full charge. """
    header(1926)

    if_player_has_special_effect(1, SPEFFECT.RuinousHand)
    if_has_tae_event(1, CHR.Player, 675)
    if_event_flag_on(1, 11025405)
    if_condition_true(0, 1)

    spawner.shoot_projectile(CHR.Player, projectile_entity_id=CHR.Player, damipoly_id=1, behavior_id=2000)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, 90010)  # Bonfire resting sound.
    chr.set_special_effect(CHR.Player, SPEFFECT.RuinousHandPayment)  # Lose two humanity.
    flag.disable_chunk(11025401, 11025405)
    if_does_not_have_tae_event(0, CHR.Player, 675)

    if_player_has_good(2, GOOD.PaleEyeOrb)
    if_event_flag_off(2, EVENT.BeyondWitness)
    skip_if_condition_false(2, 2)
    flag.enable(EVENT.BeyondWitness)
    message.status_explanation(TEXT.PaleEyeOrbQuivers)

    restart()


def event2510():
    """ Sable Rune control. If you have the Sable Rune active, a 10-second magic damage buff applies to your right hand
    whenever you:
        a) strike an enemy with a runic weapon in a dark outdoor area; or
        b) use dark sorcery on an enemy with a runic weapon equipped in your other hand.

    The buff times out after ten seconds, with no premature end condition (except un-equipping buffed weapon).
    """
    header(2510)

    wait(0.2)  # Wait for previous trigger effects to go away.

    if_event_flag_on(1, EVENT.SableRuneActive)

    if_player_has_special_effect(-1, SPEFFECT.RunicHit0)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit1)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit2)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit3)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit4)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit5)
    if_condition_true(2, -1)
    if_event_flag_on(3, EVENT.DarkAnorLondo)
    if_in_world_area(-2, 10, 1)
    if_in_world_area(-2, 10, 2)
    if_in_world_area(-2, 14, 0)
    if_in_world_area(-2, 15, 0)
    if_in_world_area(-2, 15, 1)
    if_in_world_area(-2, 17, 0)
    if_in_world_area(-2, 18, 1)
    if_condition_true(3, -2)
    if_condition_true(-3, 3)
    if_event_flag_on(4, EVENT.EarlyOolacile)
    if_in_world_area(4, 12, 1)
    if_condition_true(-3, 4)
    if_condition_true(2, -3)
    if_condition_true(-4, 2)

    if_player_has_special_effect(-5, SPEFFECT.RunicPassive0)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive1)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive2)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive3)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive4)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive5)
    if_condition_true(5, -5)
    if_player_has_special_effect(5, SPEFFECT.SableRuneTempTrigger)
    if_condition_true(-4, 5)

    if_condition_true(1, -4)

    if_condition_true(0, 1)

    # Cancel any previous Sable buffs.
    chr.cancel_special_effect(CHR.Player, SPEFFECT.SableRune0)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.SableRune1)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.SableRune2)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.SableRune3)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.SableRune4)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.SableRune5)

    # Apply appropriate level of Sable Rune effect, and register appropriate no-weapon condition.
    if_player_has_special_effect(5, SPEFFECT.RunicHit0)
    skip_if_condition_false(2, 5)
    chr.set_special_effect(CHR.Player, SPEFFECT.SableRune0)
    restart()

    if_player_has_special_effect(6, SPEFFECT.RunicHit1)
    skip_if_condition_false(2, 6)
    chr.set_special_effect(CHR.Player, SPEFFECT.SableRune1)
    restart()

    if_player_has_special_effect(7, SPEFFECT.RunicHit2)
    skip_if_condition_false(2, 7)
    chr.set_special_effect(CHR.Player, SPEFFECT.SableRune2)
    restart()

    if_player_has_special_effect(-5, SPEFFECT.RunicHit3)
    skip_if_condition_false(2, -5)
    chr.set_special_effect(CHR.Player, SPEFFECT.SableRune3)
    restart()

    if_player_has_special_effect(-6, SPEFFECT.RunicHit4)
    skip_if_condition_false(2, -6)
    chr.set_special_effect(CHR.Player, SPEFFECT.SableRune4)
    restart()

    if_player_has_special_effect(-7, SPEFFECT.RunicHit5)
    skip_if_condition_false(1, -7)
    chr.set_special_effect(CHR.Player, SPEFFECT.SableRune5)

    restart()


def event2511():
    """ Lustrous Rune control. If you have the Lustrous Rune active, a 7-second lightning buff applies to your right
    hand whenever you:
        a) strike an enemy with a runic weapon in a light outdoor area; or
        b) cast Bountiful Sunlight or Soothing Sunlight with a runic weapon in your other hand.

    The buff times out after seven seconds, with no premature end condition (except un-equipping buffed weapon).
    """
    header(2511)

    wait(1)  # Longer delay because Soothing Sunlight will keep triggering it.

    if_event_flag_on(1, EVENT.LustrousRuneActive)

    if_player_has_special_effect(-1, SPEFFECT.RunicHit0)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit1)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit2)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit3)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit4)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit5)
    if_condition_true(2, -1)
    if_event_flag_off(3, EVENT.DarkAnorLondo)
    if_in_world_area(-2, 10, 1)
    if_in_world_area(-2, 10, 2)
    if_in_world_area(-2, 14, 0)
    if_in_world_area(-2, 15, 0)
    if_in_world_area(-2, 15, 1)
    if_in_world_area(-2, 17, 0)
    if_in_world_area(-2, 18, 1)
    if_condition_true(3, -2)
    if_condition_true(-3, 3)
    if_event_flag_off(4, EVENT.EarlyOolacile)
    if_in_world_area(4, 12, 1)
    if_condition_true(-3, 4)
    if_condition_true(2, -3)

    if_condition_true(-4, 2)

    if_player_has_special_effect(-5, SPEFFECT.RunicPassive0)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive1)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive2)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive3)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive4)
    if_player_has_special_effect(-5, SPEFFECT.RunicPassive5)
    if_condition_true(5, -5)
    if_player_has_special_effect(-6, SPEFFECT.SoothingSunlight)
    if_player_has_special_effect(-6, SPEFFECT.SoothingSunlight.value + 1)
    if_player_has_special_effect(-6, SPEFFECT.SoothingSunlight.value + 2)
    if_player_has_special_effect(-6, SPEFFECT.SoothingSunlight.value + 3)
    if_player_has_special_effect(-6, SPEFFECT.SoothingSunlight.value + 4)
    if_player_has_special_effect(-6, SPEFFECT.BountifulSunlight)
    if_player_has_special_effect(-6, SPEFFECT.BountifulSunlight.value + 1)
    if_player_has_special_effect(-6, SPEFFECT.BountifulSunlight.value + 2)
    if_player_has_special_effect(-6, SPEFFECT.BountifulSunlight.value + 3)
    if_player_has_special_effect(-6, SPEFFECT.BountifulSunlight.value + 4)
    if_condition_true(5, -6)

    if_condition_true(-4, 5)

    if_condition_true(1, -4)

    if_condition_true(0, 1)

    # Cancel any previous Lustrous buffs.
    chr.cancel_special_effect(CHR.Player, SPEFFECT.LustrousRune0)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.LustrousRune1)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.LustrousRune2)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.LustrousRune3)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.LustrousRune4)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.LustrousRune5)

    # Apply appropriate level of Lustrous Rune effect, and register appropriate no-weapon condition.
    if_player_has_special_effect(1, SPEFFECT.RunicHit0)
    skip_if_condition_false(2, 1)
    chr.set_special_effect(CHR.Player, SPEFFECT.LustrousRune0)
    restart()

    if_player_has_special_effect(2, SPEFFECT.RunicHit1)
    skip_if_condition_false(2, 2)
    chr.set_special_effect(CHR.Player, SPEFFECT.LustrousRune1)
    restart()

    if_player_has_special_effect(3, SPEFFECT.RunicHit2)
    skip_if_condition_false(2, 3)
    chr.set_special_effect(CHR.Player, SPEFFECT.LustrousRune2)
    restart()

    if_player_has_special_effect(4, SPEFFECT.RunicHit3)
    skip_if_condition_false(2, 4)
    chr.set_special_effect(CHR.Player, SPEFFECT.LustrousRune3)
    restart()

    if_player_has_special_effect(5, SPEFFECT.RunicHit4)
    skip_if_condition_false(2, 5)
    chr.set_special_effect(CHR.Player, SPEFFECT.LustrousRune4)
    restart()

    if_player_has_special_effect(6, SPEFFECT.RunicHit5)
    skip_if_condition_false(1, 6)
    chr.set_special_effect(CHR.Player, SPEFFECT.LustrousRune5)

    restart()


def event2512():
    """ Wraith Rune control. """
    header(2512)

    if_player_has_special_effect(-1, SPEFFECT.RunicPassive0)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive1)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive2)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive3)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive4)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive5)
    if_condition_true(1, -1)

    if_event_flag_on(1, EVENT.WraithRuneActive)

    if_player_has_special_effect(1, SPEFFECT.KillTrigger)

    if_condition_true(0, 1)

    # Clear any existing Wraith Rune effects.
    chr.cancel_special_effect(CHR.Player, SPEFFECT.WraithRune0)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.WraithRune1)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.WraithRune2)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.WraithRune3)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.WraithRune4)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.WraithRune5)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.WraithRune5Flip)

    # Apply appropriate level of Wraith Rune effect. It will take care of itself after that.
    if_player_has_special_effect(2, SPEFFECT.RunicPassive0)
    skip_if_condition_false(2, 2)
    chr.set_special_effect(CHR.Player, SPEFFECT.WraithRune0)
    restart()

    if_player_has_special_effect(3, SPEFFECT.RunicPassive1)
    skip_if_condition_false(2, 3)
    chr.set_special_effect(CHR.Player, SPEFFECT.WraithRune1)
    restart()

    if_player_has_special_effect(4, SPEFFECT.RunicPassive2)
    skip_if_condition_false(2, 4)
    chr.set_special_effect(CHR.Player, SPEFFECT.WraithRune2)
    restart()

    if_player_has_special_effect(5, SPEFFECT.RunicPassive3)
    skip_if_condition_false(2, 5)
    chr.set_special_effect(CHR.Player, SPEFFECT.WraithRune3)
    restart()

    if_player_has_special_effect(6, SPEFFECT.RunicPassive4)
    skip_if_condition_false(2, 6)
    chr.set_special_effect(CHR.Player, SPEFFECT.WraithRune4)
    restart()

    if_player_has_special_effect(7, SPEFFECT.RunicPassive5)
    skip_if_condition_false(2, 7)
    chr.set_special_effect(CHR.Player, SPEFFECT.WraithRune5)
    chr.set_special_effect(CHR.Player, SPEFFECT.WraithRune5Flip)

    restart()


def event2513():
    """ Scintilla Rune trigger. Note that for reasons I can't control, the Scintilla themselves trigger the
    runic effects. Fortunately, other-hand weapons do not, and spells cast with a catalyst do not. The projectile
    just seems to inherit the hit effect somehow. This just means you'll get some cool chains sometimes. """
    header(2513)

    if_player_does_not_have_special_effect(7, SPEFFECT.RunicHit0)
    if_player_does_not_have_special_effect(7, SPEFFECT.RunicHit1)
    if_player_does_not_have_special_effect(7, SPEFFECT.RunicHit2)
    if_player_does_not_have_special_effect(7, SPEFFECT.RunicHit3)
    if_player_does_not_have_special_effect(7, SPEFFECT.RunicHit4)
    if_player_does_not_have_special_effect(7, SPEFFECT.RunicHit5)
    if_condition_true(0, 7)

    if_event_flag_on(1, EVENT.ScintillaRuneActive)

    if_player_has_special_effect(-1, SPEFFECT.RunicHit0)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit1)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit2)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit3)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit4)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit5)
    if_condition_true(1, -1)

    if_condition_true(0, 1)

    # Roll d30.
    flag.disable_chunk(970, 999)
    flag.enable_random_in_chunk(970, 999)

    # Count appropriate flag range as success and spawn Scintilla projectile.
    if_player_has_special_effect(2, SPEFFECT.RunicHit0)
    skip_if_condition_false(4, 2)
    if_at_least_one_true_flag_in_range(-2, 970, 971)  # 2/30 chance at Scintilla level 0.
    restart_if_condition_false(-2)
    spawner.shoot_projectile(CHR.Player, projectile_entity_id=CHR.Player, damipoly_id=7, behavior_id=2001)
    restart()

    if_player_has_special_effect(3, SPEFFECT.RunicHit1)
    skip_if_condition_false(4, 3)
    if_at_least_one_true_flag_in_range(-2, 970, 972)  # 3/30 chance at Scintilla level 1.
    restart_if_condition_false(-2)
    spawner.shoot_projectile(CHR.Player, projectile_entity_id=CHR.Player, damipoly_id=7, behavior_id=2001)
    restart()

    if_player_has_special_effect(4, SPEFFECT.RunicHit2)
    skip_if_condition_false(4, 4)
    if_at_least_one_true_flag_in_range(-2, 970, 973)  # 4/30 chance at Scintilla level 2.
    restart_if_condition_false(-2)
    spawner.shoot_projectile(CHR.Player, projectile_entity_id=CHR.Player, damipoly_id=7, behavior_id=2001)
    restart()

    if_player_has_special_effect(5, SPEFFECT.RunicHit3)
    skip_if_condition_false(4, 5)
    if_at_least_one_true_flag_in_range(-2, 970, 974)  # 5/30 chance at Scintilla level 3.
    restart_if_condition_false(-2)
    spawner.shoot_projectile(CHR.Player, projectile_entity_id=CHR.Player, damipoly_id=7, behavior_id=2001)
    restart()

    if_player_has_special_effect(6, SPEFFECT.RunicHit4)
    skip_if_condition_false(4, 6)
    if_at_least_one_true_flag_in_range(-2, 970, 975)  # 6/30 chance at Scintilla level 4.
    restart_if_condition_false(-2)
    spawner.shoot_projectile(CHR.Player, projectile_entity_id=CHR.Player, damipoly_id=7, behavior_id=2001)
    restart()

    if_player_has_special_effect(-3, SPEFFECT.RunicHit5)
    restart_if_condition_false(-3)  # This shouldn't happen.
    if_at_least_one_true_flag_in_range(-2, 970, 972)  # 3/30 chance of Crystal Scintilla at level 5.
    skip_if_condition_false(2, -2)
    spawner.shoot_projectile(CHR.Player, projectile_entity_id=CHR.Player, damipoly_id=7, behavior_id=2002)
    skip(2)
    if_at_least_one_true_flag_in_range(-4, 973, 976)  # 4/30 chance of normal Scintilla at level 5.
    skip_if_condition_false(1, -4)
    spawner.shoot_projectile(CHR.Player, projectile_entity_id=CHR.Player, damipoly_id=7, behavior_id=2001)
    restart()


def event2514():
    """ Omphalic Rune effect control on spawn. """
    header(2514)

    # If death trigger flag is off, reset kill counter and end.
    skip_if_event_flag_on(2, EVENT.OmphalicDeathTrigger)
    flag.clear_event_value(EVENT.OmphalicKillCounter, 4)
    end()

    # Otherwise, disable death trigger, enable appropriate Omphalic buff, and wait for end.
    flag.disable(EVENT.OmphalicDeathTrigger)

    # End if rune is deactivated, somehow.
    skip_if_event_flag_on(2, EVENT.OmphalicRuneActive)
    flag.clear_event_value(EVENT.OmphalicKillCounter, 4)
    end()

    # Determine effect strength (1 to 5) based on kill count (3, 5, 7, 9, 11+).

    if_event_value_greater_than(1, EVENT.OmphalicKillCounter, 4, 10)
    skip_if_condition_false(2, 1)
    chr.set_special_effect(CHR.Player, SPEFFECT.OmphalicRune5)
    skip(15)

    if_event_value_greater_than(2, EVENT.OmphalicKillCounter, 4, 8)
    skip_if_condition_false(2, 2)
    chr.set_special_effect(CHR.Player, SPEFFECT.OmphalicRune4)
    skip(11)

    if_event_value_greater_than(3, EVENT.OmphalicKillCounter, 4, 6)
    skip_if_condition_false(2, 3)
    chr.set_special_effect(CHR.Player, SPEFFECT.OmphalicRune3)
    skip(7)

    if_event_value_greater_than(4, EVENT.OmphalicKillCounter, 4, 4)
    skip_if_condition_false(2, 4)
    chr.set_special_effect(CHR.Player, SPEFFECT.OmphalicRune2)
    skip(3)

    if_event_value_greater_than(5, EVENT.OmphalicKillCounter, 4, 2)
    skip_if_condition_false(1, 5)
    chr.set_special_effect(CHR.Player, SPEFFECT.OmphalicRune1)

    flag.clear_event_value(EVENT.OmphalicKillCounter, 4)

    # Determine duration based on runic weapon level (note: checked immediately on spawn).

    if_player_has_special_effect(-1, SPEFFECT.RunicPassive0)
    skip_if_condition_false(2, -1)
    wait(40.0)
    skip(19)

    if_player_has_special_effect(-2, SPEFFECT.RunicPassive1)
    skip_if_condition_false(2, -2)
    wait(50.0)
    skip(15)

    if_player_has_special_effect(-3, SPEFFECT.RunicPassive2)
    skip_if_condition_false(2, -3)
    wait(60.0)
    skip(11)

    if_player_has_special_effect(-4, SPEFFECT.RunicPassive3)
    skip_if_condition_false(2, -4)
    wait(70.0)
    skip(7)

    if_player_has_special_effect(-5, SPEFFECT.RunicPassive4)
    skip_if_condition_false(2, -5)
    wait(80.0)
    skip(3)

    if_player_has_special_effect(-6, SPEFFECT.RunicPassive5)
    skip_if_condition_false(1, -6)
    wait(90.0)

    # Cancel effect.
    chr.cancel_special_effect(CHR.Player, SPEFFECT.OmphalicRune1)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.OmphalicRune2)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.OmphalicRune3)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.OmphalicRune4)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.OmphalicRune5)


def event2515():
    """ Omphalic Rune kill counter and death trigger. """
    header(2515)

    if_event_flag_on(1, EVENT.OmphalicRuneActive)

    if_player_has_special_effect(2, SPEFFECT.KillTrigger)
    if_condition_true(-2, 2)
    if_entity_health_less_than_or_equal(-2, CHR.Player, 0.0)
    if_condition_true(1, -2)

    if_player_has_special_effect(-1, SPEFFECT.RunicPassive0)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive1)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive2)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive3)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive4)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive5)
    if_condition_true(1, -1)

    if_condition_true(0, 1)

    # Kill trigger: increment kill counter and restart.
    skip_if_condition_false_finished(3, 2)
    flag.increment_event_value(EVENT.OmphalicKillCounter, 4, 15)
    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)
    restart()

    # Player death: enable trigger flag.
    flag.enable(EVENT.OmphalicDeathTrigger)


def event2516():
    """ Pale White Rune trigger. """
    header(2516)

    if_player_does_not_have_special_effect(1, SPEFFECT.PaleWhiteRune)

    if_event_flag_on(1, EVENT.PaleWhiteRuneActive)

    if_player_has_special_effect(-1, SPEFFECT.RunicHit0)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit1)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit2)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit3)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit4)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit5)
    if_condition_true(1, -1)

    if_condition_true(0, 1)

    # Random twenty-flag roll.
    flag.disable_chunk(970, 999)
    flag.enable_random_in_chunk(970, 999)

    # Count appropriate flag range as success and apply Pale White Rune effect (only one level).
    if_player_has_special_effect(2, SPEFFECT.RunicHit0)
    skip_if_condition_false(4, 2)
    if_at_least_one_true_flag_in_range(-2, 970, 972)  # 3/30 chance at Pale White level 0.
    restart_if_condition_false(-2)
    chr.set_special_effect(CHR.Player, SPEFFECT.PaleWhiteRune)
    skip(29)

    if_player_has_special_effect(3, SPEFFECT.RunicHit1)
    skip_if_condition_false(4, 3)
    if_at_least_one_true_flag_in_range(-2, 970, 973)  # 4/30 chance at Pale White level 1.
    restart_if_condition_false(-2)
    chr.set_special_effect(CHR.Player, SPEFFECT.PaleWhiteRune)
    skip(23)

    if_player_has_special_effect(4, SPEFFECT.RunicHit2)
    skip_if_condition_false(4, 4)
    if_at_least_one_true_flag_in_range(-2, 970, 974)  # 5/30 chance at Pale White level 2.
    restart_if_condition_false(-2)
    chr.set_special_effect(CHR.Player, SPEFFECT.PaleWhiteRune)
    skip(17)

    if_player_has_special_effect(5, SPEFFECT.RunicHit3)
    skip_if_condition_false(4, 5)
    if_at_least_one_true_flag_in_range(-2, 970, 975)  # 6/30 chance at Pale White level 3.
    restart_if_condition_false(-2)
    chr.set_special_effect(CHR.Player, SPEFFECT.PaleWhiteRune)
    skip(11)

    if_player_has_special_effect(6, SPEFFECT.RunicHit4)
    skip_if_condition_false(4, 6)
    if_at_least_one_true_flag_in_range(-2, 970, 976)  # 7/30 chance at Pale White level 4.
    restart_if_condition_false(-2)
    chr.set_special_effect(CHR.Player, SPEFFECT.PaleWhiteRune)
    skip(5)

    if_player_has_special_effect(7, SPEFFECT.RunicHit5)
    restart_if_condition_false(7)  # This shouldn't happen.
    if_at_least_one_true_flag_in_range(-2, 970, 977)  # 8/30 chance at Pale White level 5.
    restart_if_condition_false(-2)
    chr.set_special_effect(CHR.Player, SPEFFECT.PaleWhiteRune)

    # Watch for spell being cast to end buff. (But doesn't need rune or runic weapon to continue.)
    # Buff lasts 15 seconds otherwise.

    if_player_has_special_effect(-3, SPEFFECT.SorceryCast)  # Normal sorcery.
    if_player_has_special_effect(-3, SPEFFECT.SableRuneTempTrigger)  # Dark sorcery.
    if_player_does_not_have_special_effect(-3, SPEFFECT.PaleWhiteRune)  # Times out.
    if_condition_true(0, -3)

    wait(2.0)  # Wait for spell projectile to land. (I assume this is needed.)

    chr.cancel_special_effect(CHR.Player, SPEFFECT.PaleWhiteRune)
    restart()


def event2517():
    """ Reaper's Rune effect triggers. Note that these buffs just stack up. """
    header(2517, 1)

    # Effects reset on every load or rest.
    chr.cancel_special_effect(CHR.Player, SPEFFECT.ReapersRune0)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.ReapersRune1)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.ReapersRune2)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.ReapersRune3)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.ReapersRune4)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.ReapersRune5)

    if_event_value_greater_than(0, EVENT.ReapersKillCounter, 8, 8)
    chr.set_special_effect(CHR.Player, SPEFFECT.ReapersRune0)

    if_event_value_greater_than(0, EVENT.ReapersKillCounter, 8, 16)
    chr.set_special_effect(CHR.Player, SPEFFECT.ReapersRune1)

    if_event_value_greater_than(0, EVENT.ReapersKillCounter, 8, 24)
    chr.set_special_effect(CHR.Player, SPEFFECT.ReapersRune2)

    if_event_value_greater_than(0, EVENT.ReapersKillCounter, 8, 32)
    chr.set_special_effect(CHR.Player, SPEFFECT.ReapersRune3)

    if_event_value_greater_than(0, EVENT.ReapersKillCounter, 8, 40)
    chr.set_special_effect(CHR.Player, SPEFFECT.ReapersRune4)

    if_event_value_greater_than(0, EVENT.ReapersKillCounter, 8, 48)
    chr.set_special_effect(CHR.Player, SPEFFECT.ReapersRune5)


def event2518():
    """ Reaper's Rune kill counter. """
    header(2518)

    if_event_flag_on(1, EVENT.ReapersRuneActive)
    if_player_has_special_effect(1, SPEFFECT.KillTrigger)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive0)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive1)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive2)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive3)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive4)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive5)
    if_condition_true(1, -1)

    if_condition_true(0, 1)

    if_player_has_special_effect(2, SPEFFECT.RunicPassive0)
    skip_if_condition_false(3, 2)
    flag.increment_event_value(EVENT.ReapersKillCounter, 8, 10)
    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)
    restart()

    if_player_has_special_effect(3, SPEFFECT.RunicPassive1)
    skip_if_condition_false(3, 3)
    flag.increment_event_value(EVENT.ReapersKillCounter, 8, 20)
    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)
    restart()

    if_player_has_special_effect(4, SPEFFECT.RunicPassive2)
    skip_if_condition_false(3, 4)
    flag.increment_event_value(EVENT.ReapersKillCounter, 8, 30)
    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)
    restart()

    if_player_has_special_effect(5, SPEFFECT.RunicPassive3)
    skip_if_condition_false(3, 5)
    flag.increment_event_value(EVENT.ReapersKillCounter, 8, 40)
    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)
    restart()

    if_player_has_special_effect(6, SPEFFECT.RunicPassive4)
    skip_if_condition_false(3, 6)
    flag.increment_event_value(EVENT.ReapersKillCounter, 8, 50)
    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)
    restart()

    if_player_has_special_effect(7, SPEFFECT.RunicPassive5)
    skip_if_condition_false(3, 7)
    flag.increment_event_value(EVENT.ReapersKillCounter, 8, 60)
    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)
    restart()

    restart()  # Shouldn't happen.


def event2519():
    """ Rhythm Rune triggers. """
    header(2519)

    if_event_flag_on(1, EVENT.RhythmRuneActive)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit0)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit1)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit2)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit3)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit4)
    if_player_has_special_effect(-1, SPEFFECT.RunicHit5)
    if_condition_true(1, -1)

    if_condition_true(0, 1)

    if_player_has_special_effect(-2, SPEFFECT.RhythmRuneWindow)
    skip_if_condition_true(4, -2)
    # Reset hit counter and set new window if this window was missed.
    flag.clear_event_value(EVENT.RhythmHitCounter, 4)
    wait(2.8)
    chr.set_special_effect(CHR.Player, SPEFFECT.RhythmRuneWindow)  # Window lasts for 0.4 seconds.
    restart()

    # Otherwise, increment rhythm effect level to a maximum depending on runic level.

    if_player_has_special_effect(2, SPEFFECT.RunicHit5)
    skip_if_condition_false(2, 2)
    flag.increment_event_value(EVENT.RhythmHitCounter, 4, 7)
    skip(19)

    if_player_has_special_effect(3, SPEFFECT.RunicHit4)
    skip_if_condition_false(2, 3)
    flag.increment_event_value(EVENT.RhythmHitCounter, 4, 6)
    skip(15)

    if_player_has_special_effect(4, SPEFFECT.RunicHit3)
    skip_if_condition_false(2, 4)
    flag.increment_event_value(EVENT.RhythmHitCounter, 4, 5)
    skip(11)

    if_player_has_special_effect(5, SPEFFECT.RunicHit2)
    skip_if_condition_false(2, 5)
    flag.increment_event_value(EVENT.RhythmHitCounter, 4, 4)
    skip(7)

    if_player_has_special_effect(6, SPEFFECT.RunicHit1)
    skip_if_condition_false(2, 6)
    flag.increment_event_value(EVENT.RhythmHitCounter, 4, 3)
    skip(3)

    if_player_has_special_effect(7, SPEFFECT.RunicHit0)
    skip_if_condition_false(2, 7)
    flag.increment_event_value(EVENT.RhythmHitCounter, 4, 2)

    # Cancel all previous Rhythm bonuses and apply (or re-apply) appropriate level based on hit counter.

    chr.cancel_special_effect(CHR.Player, SPEFFECT.RhythmRune0)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.RhythmRune1)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.RhythmRune2)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.RhythmRune3)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.RhythmRune4)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.RhythmRune5)

    if_event_value_greater_than(2, EVENT.RhythmHitCounter, 4, 6)
    skip_if_condition_false(2, 2)
    chr.set_special_effect(CHR.Player, SPEFFECT.RhythmRune5)
    skip(17)

    if_event_value_greater_than(3, EVENT.RhythmHitCounter, 4, 5)
    skip_if_condition_false(2, 3)
    chr.set_special_effect(CHR.Player, SPEFFECT.RhythmRune4)
    skip(13)

    if_event_value_greater_than(4, EVENT.RhythmHitCounter, 4, 4)
    skip_if_condition_false(2, 4)
    chr.set_special_effect(CHR.Player, SPEFFECT.RhythmRune3)
    skip(9)

    if_event_value_greater_than(5, EVENT.RhythmHitCounter, 4, 3)
    skip_if_condition_false(2, 5)
    chr.set_special_effect(CHR.Player, SPEFFECT.RhythmRune2)
    skip(5)

    if_event_value_greater_than(6, EVENT.RhythmHitCounter, 4, 2)
    skip_if_condition_false(2, 6)
    chr.set_special_effect(CHR.Player, SPEFFECT.RhythmRune1)
    skip(1)

    chr.set_special_effect(CHR.Player, SPEFFECT.RhythmRune0)

    wait(2.8)
    chr.set_special_effect(CHR.Player, SPEFFECT.RhythmRuneWindow)  # Window lasts for 0.4 seconds.
    restart()


def event2520():
    """ Ransacker's Rune trigger. """
    header(2520)

    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)

    if_event_flag_on(1, EVENT.RansackersRuneActive)
    if_event_flag_off(1, EVENT.RansackersRuneItemTrigger)
    if_player_has_special_effect(1, SPEFFECT.KillTrigger)

    if_player_has_special_effect(-1, SPEFFECT.RunicPassive0)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive1)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive2)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive3)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive4)
    if_player_has_special_effect(-1, SPEFFECT.RunicPassive5)
    if_condition_true(1, -1)

    if_condition_true(0, 1)

    # Roll dice.
    flag.disable_chunk(970, 999)
    flag.enable_random_in_chunk(970, 999)

    # Count appropriate flag range as success.
    if_player_has_special_effect(-2, SPEFFECT.RunicPassive0)
    skip_if_condition_false(4, -2)
    if_at_least_one_true_flag_in_range(2, 970, 971)  # 2/30 chance at Ransackers level 0.
    restart_if_condition_false(2)
    flag.enable(EVENT.RansackersRuneItemTrigger)
    restart()

    if_player_has_special_effect(-3, SPEFFECT.RunicPassive1)
    skip_if_condition_false(4, -3)
    if_at_least_one_true_flag_in_range(2, 970, 972)  # 3/30 chance at Ransackers level 1.
    restart_if_condition_false(2)
    flag.enable(EVENT.RansackersRuneItemTrigger)
    restart()

    if_player_has_special_effect(-4, SPEFFECT.RunicPassive2)
    skip_if_condition_false(4, -4)
    if_at_least_one_true_flag_in_range(2, 970, 973)  # 4/30 chance at Ransackers level 2.
    restart_if_condition_false(2)
    flag.enable(EVENT.RansackersRuneItemTrigger)
    restart()

    if_player_has_special_effect(-5, SPEFFECT.RunicPassive3)
    skip_if_condition_false(4, -5)
    if_at_least_one_true_flag_in_range(2, 970, 974)  # 5/30 chance at Ransackers level 3.
    restart_if_condition_false(2)
    flag.enable(EVENT.RansackersRuneItemTrigger)
    restart()

    if_player_has_special_effect(-6, SPEFFECT.RunicPassive4)
    skip_if_condition_false(4, -6)
    if_at_least_one_true_flag_in_range(2, 970, 975)  # 6/30 chance at Ransackers level 4.
    restart_if_condition_false(2)
    flag.enable(EVENT.RansackersRuneItemTrigger)
    restart()

    if_player_has_special_effect(-7, SPEFFECT.RunicPassive5)
    restart_if_condition_false(-7)  # This shouldn't happen.
    if_at_least_one_true_flag_in_range(2, 970, 976)  # 7/30 chance at Ransackers level 5.
    restart_if_condition_false(2)
    flag.enable(EVENT.RansackersRuneItemTrigger)
    restart()


def event2521():
    """ Ransackers Rune items (17 slots, 2521-2537).

    970-974: common_item_1 (5/30)           16.6%
    975-979: common_item_2 (5/30)           16.6%
    980-984: common_item_3 (5/30)           16.6%
    985-987: uncommon_item_1 (3/30)         10%
    988-990: uncommon_item_2 (3/30)         10%
    991-993: uncommon_item_3 (3/30)         10%
    994-995: rare_item_1 (2/30)             6.6%
    996-997: rare_item_2 (2/30)             6.6%
    998: mythic_item_1 (1/30)               3%
    999: mythic_item_2 (1/30)               3%
    """
    header(2521)
    world_block, world_area, c1, c2, c3, u1, u2, u3, r1, r2, m1, m2 = define_args('BBiiiiiiiiii')

    if_event_flag_on(1, EVENT.RansackersRuneItemTrigger)
    if_in_world_area(1, world_block, world_area)
    if_condition_true(0, 1)

    flag.disable(EVENT.RansackersRuneItemTrigger)

    # Roll dice.
    flag.disable_chunk(970, 999)
    flag.enable_random_in_chunk(970, 999)

    harvest_table = (  # condition, item_lot, start_flag, end_flag
        (2, c1, 970, 974),
        (3, c2, 975, 979),
        (4, c3, 980, 984),
        (5, u1, 985, 987),
        (6, u1, 988, 990),
        (7, u1, 991, 993),
        (-1, r1, 994, 995),
        (-2, r2, 996, 997),
        (-3, m1, 998, 998),
        (-4, m2, 999, 999),
    )

    for condition, item_lot, start_flag, end_flag in harvest_table:
        if start_flag == end_flag:
            skip_if_event_flag_off(2, start_flag)
        else:
            if_at_least_one_true_flag_in_range(condition, start_flag, end_flag)
            skip_if_condition_false(2, condition)
        item.award_item_to_host_only(item_lot)
        restart()

    restart()  # Shouldn't happen.


def event2600():
    """ Activate a Rune. Disables all other Runes. Nine slots (2600-2608). """
    header(2600)
    rune_effect, rune_flag = define_args('ii')

    if_player_has_special_effect(0, rune_effect)
    flag.disable_chunk(EVENT.SableRuneActive, EVENT.RhythmRuneActive)
    flag.enable(rune_flag)
    if_player_does_not_have_special_effect(0, rune_effect)
    restart()


def event2540():
    """ Ring of the Embraced takes all your souls if you remove it. """
    header(2540)

    if_player_has_special_effect(0, SPEFFECT.RingOfTheEmbraced)
    if_player_does_not_have_special_effect(0, SPEFFECT.RingOfTheEmbraced)
    chr.set_special_effect(CHR.Player, SPEFFECT.RingOfTheEmbracedRemoved)
    restart()


def event2541():
    """ 15 second delay after equipping Ring of Temptation. """
    header(2541)

    if_player_has_special_effect(0, SPEFFECT.RingOfTemptationEquipped)
    wait(5.0)
    if_player_has_special_effect(1, SPEFFECT.RingOfTemptationEquipped)
    skip_if_condition_true(1, 1)
    restart()
    wait(5.0)
    if_player_has_special_effect(2, SPEFFECT.RingOfTemptationEquipped)
    skip_if_condition_true(1, 2)
    restart()
    wait(5.0)
    if_player_has_special_effect(3, SPEFFECT.RingOfTemptationEquipped)
    skip_if_condition_true(1, 3)
    restart()

    chr.set_special_effect(CHR.Player, SPEFFECT.RingOfTemptationActive)
    # NOTE: You can tell it's active from the humanity icon in your HUD.

    if_player_does_not_have_special_effect(0, SPEFFECT.RingOfTemptationEquipped)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.RingOfTemptationActive)
    restart()


def event2542():
    """ Player dies while wearing Ring of Temptation, and loses all souls. """
    header(2542)

    if_player_has_special_effect(1, SPEFFECT.RingOfTemptationEquipped)
    if_entity_health_less_than_or_equal(1, CHR.Player, 0.0)
    if_condition_true(0, 1)
    chr.set_special_effect(CHR.Player, SPEFFECT.RingOfTemptationDeath)
    restart()


def event2543():
    """ Player kills an enemy with Ring of the Evil Eye equipped. """
    header(2543)

    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)

    if_player_has_special_effect(1, SPEFFECT.RingOfTheEvilEye)
    if_player_has_special_effect(1, SPEFFECT.KillTrigger)
    if_condition_true(0, 1)

    chr.set_special_effect(CHR.Player, SPEFFECT.RingOfTheEvilEyeEffect)
    restart()


def event2544():
    """ Twilight Ring starts and ends. """
    header(2544)

    if_player_has_special_effect(0, SPEFFECT.TwilightRingEquipped)
    chr.set_special_effect(CHR.Player, SPEFFECT.TwilightRingWeak)

    if_player_does_not_have_special_effect(0, SPEFFECT.TwilightRingEquipped)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.TwilightRingWeak)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.TwilightRingMedium)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.TwilightRingStrong)

    restart()


def event2545():
    """ Twilight Ring effect waxes and wanes. """
    header(2545)

    if_player_has_special_effect(0, SPEFFECT.TwilightRingWeak)
    wait(60.0)
    if_player_has_special_effect(1, SPEFFECT.TwilightRingWeak)
    skip_if_condition_true(1, 1)
    restart()

    chr.cancel_special_effect(CHR.Player, SPEFFECT.TwilightRingWeak)
    chr.set_special_effect(CHR.Player, SPEFFECT.TwilightRingMedium)
    wait(60.0)
    if_player_has_special_effect(2, SPEFFECT.TwilightRingMedium)
    skip_if_condition_true(1, 2)
    restart()

    chr.cancel_special_effect(CHR.Player, SPEFFECT.TwilightRingMedium)
    chr.set_special_effect(CHR.Player, SPEFFECT.TwilightRingStrong)
    wait(60.0)
    if_player_has_special_effect(3, SPEFFECT.TwilightRingStrong)
    skip_if_condition_true(1, 3)
    restart()

    chr.cancel_special_effect(CHR.Player, SPEFFECT.TwilightRingStrong)
    chr.set_special_effect(CHR.Player, SPEFFECT.TwilightRingMedium)
    wait(60.0)
    if_player_has_special_effect(4, SPEFFECT.TwilightRingMedium)
    skip_if_condition_true(1, 4)
    restart()

    chr.cancel_special_effect(CHR.Player, SPEFFECT.TwilightRingMedium)
    chr.set_special_effect(CHR.Player, SPEFFECT.TwilightRingWeak)
    restart()  # Cycle restarts.


def event2546():
    """ Bond to Beyond has a 5% of giving you one soft humanity on every kill. """
    header(2546)

    if_player_does_not_have_special_effect(0, SPEFFECT.KillTrigger)

    if_player_has_special_effect(1, SPEFFECT.BondToBeyond)
    if_player_has_special_effect(1, SPEFFECT.KillTrigger)
    if_condition_true(0, 1)

    flag.disable_chunk(11025600, 11025619)
    flag.enable_random_in_chunk(11025600, 11025619)
    skip_if_event_flag_off(1, 11025600)
    chr.set_special_effect(CHR.Player, SPEFFECT.BondToBeyondEffect)
    restart()


def event11502020():
    """ Lithic Bond requirement: become petrified by a Basilisk. """
    header(11502020)
    end_if_event_flag_on(EVENT.LithicWitness)
    if_player_has_good(1, GOOD.PaleEyeOrb)
    if_player_has_special_effect(1, SPEFFECT.Petrification)
    if_condition_true(0, 1)
    flag.enable(EVENT.LithicWitness)
    message.status_explanation(TEXT.PaleEyeOrbQuivers)


# Flag 11502021: Ash Lake Hydra jumps over sandbar (m13_02)

# Flag 11502022: Kill all three Moonlight Butterflies in Crystal Cave (m17_00)


def event11502023():
    """ Bond to Beyond requirement: use Soul of Manus or Ruinous Hand blast. """
    header(11502023)
    end_if_event_flag_on(EVENT.BeyondWitness)
    if_player_has_good(1, GOOD.PaleEyeOrb)
    if_player_has_special_effect(1, SPEFFECT.BondToBeyondWitness)
    if_condition_true(0, 1)
    flag.enable(EVENT.BeyondWitness)
    message.status_explanation(TEXT.PaleEyeOrbQuivers)


def event2547():
    """ Contract Bonerust, then remove it. """
    header(2547, 1)

    skip_if_event_flag_on(38, EVENT.HasBonerust)  # Skip trigger and dice roll.

    # Wait for last hit to end.
    if_player_does_not_have_special_effect(7, SPEFFECT.BonerustHit3Percent)
    if_player_does_not_have_special_effect(7, SPEFFECT.BonerustHit5Percent)
    if_player_does_not_have_special_effect(7, SPEFFECT.BonerustHit10Percent)
    if_player_does_not_have_special_effect(7, SPEFFECT.BonerustHit15Percent)
    if_player_does_not_have_special_effect(7, SPEFFECT.BonerustHit20Percent)
    if_condition_true(0, 7)

    if_player_has_special_effect(1, SPEFFECT.BonerustHit3Percent)
    if_player_has_special_effect(2, SPEFFECT.BonerustHit5Percent)
    if_player_has_special_effect(3, SPEFFECT.BonerustHit10Percent)
    if_player_has_special_effect(4, SPEFFECT.BonerustHit15Percent)
    if_player_has_special_effect(5, SPEFFECT.BonerustHit20Percent)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(-1, 3)
    if_condition_true(-1, 4)
    if_condition_true(-1, 5)
    if_condition_true(0, -1)

    if_player_has_special_effect(6, SPEFFECT.SerousBond)
    restart_if_condition_true(6)

    # Roll dice. (11025620-11025669) 11025620 or 11025621 are hits (only first with Archwood shield).
    # Note all odds have been lowered from their stated values as of v1.2.0.
    flag.disable_chunk(11025620, 11025679)
    skip_if_condition_false_finished(2, 1)
    flag.enable_random_in_chunk(11025620, 11025679)  # 2/60
    skip(10)
    skip_if_condition_false_finished(2, 2)
    flag.enable_random_in_chunk(11025620, 11025659)  # 2/40
    skip(7)
    skip_if_condition_false_finished(2, 3)
    flag.enable_random_in_chunk(11025620, 11025649)  # 2/30
    skip(4)
    skip_if_condition_false_finished(2, 4)
    flag.enable_random_in_chunk(11025620, 11025644)  # 2/25
    skip(1)
    flag.enable_random_in_chunk(11025620, 11025635)  # 2/16

    if_event_flag_on(-2, 11025620)
    if_player_has_special_effect(6, 6890)  # Grass Crest Shield halves odds.
    skip_if_condition_true(1, 6)
    if_event_flag_on(-2, 11025621)
    restart_if_condition_false(-2)

    # Skips to here if player already has Bonerust on load.

    chr.set_special_effect(CHR.Player, SPEFFECT.Bonerust)
    flag.enable(EVENT.HasBonerust)

    # Show message on first time. Evil Eye icon also active.
    skip_if_event_flag_on(2, 11302010)
    message.status_explanation(TEXT.AfflictedWithBonerust, True)  # Dialog too easily skipped. It's only one time.
    flag.enable(11302010)

    if_player_has_special_effect(-3, SPEFFECT.GreenMossUsed)
    if_player_has_special_effect(-3, SPEFFECT.Remedy)
    if_player_has_special_effect(-3, SPEFFECT.SunlightElixirEffect)
    if_has_tae_event(-3, CHR.Player, 700)  # Sitting at bonfire.
    if_condition_true(0, -3)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.Bonerust)
    flag.disable(EVENT.HasBonerust)
    wait_frames(5)
    restart()


def event2549():
    """ Ring of Condemnation recharges. """
    header(2549)

    if_player_has_special_effect(1, SPEFFECT.RingOfCondemnationEquipped)
    if_player_does_not_have_special_effect(1, SPEFFECT.RingOfCondemnationActive)
    if_condition_true(0, 1)

    chr.set_special_effect(CHR.Player, SPEFFECT.RingOfCondemnationActive)

    if_player_does_not_have_special_effect(2, SPEFFECT.RingOfCondemnationEquipped)
    if_condition_true(-1, 2)
    if_player_does_not_have_special_effect(-1, SPEFFECT.RingOfCondemnationActive)
    if_condition_true(0, -1)

    # Recharge interval (if ring wasn't unequipped). Not so long that you're tempted to quit out and reload.
    skip_if_condition_true_finished(2, 2)
    wait_random_seconds(15.0, 25.0)
    skip(1)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.RingOfCondemnationActive)

    restart()


def event1927():
    """ 25% max HP penalty for being Hollow rather than Human. """
    header(1927, 1)

    if_character_hollow(0, CHR.Player)
    chr.set_special_effect(CHR.Player, SPEFFECT.HollowPenalty)

    if_character_hollow(1, CHR.Player)
    if_condition_false(0, 1)
    chr.cancel_special_effect(CHR.Player, SPEFFECT.HollowPenalty)
    restart()


def event11022100():
    """ Prevent items from being re-obtained in NG+. Identical to 8300 and 8090. """
    header(11022100)

    item_type, item_id, item_flag = define_args('Bii')
    end_if_event_flag_on(item_flag)
    if_new_game_count_greater_than_or_equal(1, 1)
    end_if_condition_false(1)
    if_player_owns_item(2, item_type, item_id)
    end_if_condition_false(2)
    flag.enable(item_flag)


def event11512000():
    """ Player has been given Lordvessel. """
    header(11512000)
    end_if_this_event_on()
    if_player_owns_good(0, GOOD.Lordvessel)
    flag.enable(11512000)


def event11022120():
    """ Remove items from player at start of NG+. """
    header(11022120)

    item_type, item_id = define_args('Bi')
    end_if_this_event_slot_on()
    if_new_game_count_greater_than_or_equal(1, 1)
    end_if_condition_false(1)
    item.remove_items_from_player(item_type, item_id, 0)


def event11512004():
    """ Player obtained Chthonic Spark (for message display). """
    header(11512004)
    end_if_this_event_on()
    if_player_has_good(0, GOOD.ChthonicSpark)
    end()


def event363():
    """ Vamos removes Chthonic Spark from player. """
    header(363)
    vamos_given_spark, spark_id = define_args('ii')
    end_if_this_event_slot_on()  # Now just runs once.

    if_event_flag_on(0, vamos_given_spark)
    item.remove_items_from_player(ItemType.good, spark_id, 1)


def event11512005():
    """ Toggles availability of full bonfire warp menu based on Spark possession or Gwyn death. """
    header(11512005)

    BONFIRE_FLAGS = (
        # on_warp_list, required_flag (from rest)
        (11012045, 11012044),  # Parish Turret
        (11302045, 11302040),  # Bone Chimney
        (11202045, 11202040),  # Moonlight Grove
        (11402045, 11402040),  # Fetid Slagmire
        (11002045, 11002044),  # The Sluiceworks
        (11512045, 11512043),  # Sun Chamber
        (11512046, 11512044),  # Gwyn's Altar
        (11312045, 11312044),  # The Undercrypt
        (11412085, 11412080),  # Sanctum of Chaos
        (11602045, 11602044),  # The Abyss
        (11702045, 11702044),  # The Duke's Archives
        # (11102045, 11102044),  # Cloister of Exiles (now on permanent Lordvessel list)
        (11212085, 11212084),  # Royal Hippodrome
        (11812045, 11812040),  # Undead Asylum (must be rested at on return)
    )

    # Miscellaneous: enable Chasm Cell bonfire warp flag if Early Oolacile is on.
    skip_if_event_flag_off(1, EVENT.EarlyOolacile)
    flag.enable(213)

    # Start by disabling all of them.
    for warp_list_flag, _ in BONFIRE_FLAGS:
        flag.disable(warp_list_flag)

    # Wait for Chthonic Spark possession or Gwyn to be dead.
    if_player_has_good(-1, GOOD.ChthonicSpark)
    if_event_flag_on(-1, EVENT.LordvesselFull)
    if_condition_true(0, -1)

    # Enable all bonfires that have been rested at.
    for warp_list_flag, required_flag in BONFIRE_FLAGS:
        # Note that you'll need to reload for a newly rested-at bonfire to appear in the menu.
        skip_if_event_flag_off(1, required_flag)
        flag.enable(warp_list_flag)

    # Restart if Spark is lost and Lordvessel is not full.
    if_player_does_not_have_good(1, GOOD.ChthonicSpark)
    if_event_flag_off(1, EVENT.LordvesselFull)
    if_condition_true(0, 1)
    restart()


def event723():
    """ Monitor when Griggs is sold out at Firelink. (Updated for new shop lineup.) """
    header(723)
    end_if_this_event_on()

    GRIGGS_FIRELINK_SHOP_FLAGS = [
        11027130,  # Soul Arrow
        11027140,  # Heavy Soul Arrow
        11027150,  # Great Soul Arrow
        11027160,  # Heavy Great Soul Arrow
        11027170,  # Magic Weapon
        11027180,  # Magic Shield
        11027190,  # Silence
        11027200,  # Fall Control
        # 11027210,
        # 11027220,
        11027230,  # Homing Soulmass
        11027240,  # Soul Spear
    ]

    for shop_flag in GRIGGS_FIRELINK_SHOP_FLAGS:
        if_event_flag_on(1, shop_flag)
    if_condition_true(0, 1)
    flag.enable(723)


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
