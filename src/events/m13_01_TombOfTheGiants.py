
import sys
import inspect
from pydses import *

map_name = 'm13_01_00_00'  # Tomb of the CHR.Giants
emevd_directory = 'G:\\Steam\\steamapps\\common\\Dark Souls Prepare to Die Edition\\DATA\\event'


class DEBUG(IntEnum):
    PATCHES_IN_TOMB = False
    BELLS_RUNG = False
    CEASELESS_DEAD = False
    GET_LIGHT_SOURCES = False
    CIARAN_DIED_WITH_NITO = False


class CHR(IntEnum):
    Player = 10000
    Patches = 6321
    Giant = 1310130
    FirstBonfire = 1310960
    SecondBonfire = 1310961
    NitoBonfire = 1310950
    CeaselessDischarge = 1310180
    CiaranFirstSolo = 6741
    CiaranSecondSolo = 6742
    CiaranInNitoBoss = 6743
    NitoBoss = 1310800
    NitoCovenant = 1310810
    NitoAsleep = 1310820
    NitoWithCiaranBossHP = 1310830


class OBJ(IntEnum):
    NitoCovenantCoffin = 1311300
    CiaranFog = 1311700
    NitoFog = 1311990
    NitoBonfire = 1311950


class SFX(IntEnum):
    CiaranFog = 1311701
    NitoFog = 1311991


class REGION(IntEnum):
    WarpPlane = 1312850
    WarpDestinationDecision = 1312851
    LimestoneCaveSpawn = 1312971
    RitualGrottoEntrance = 1312675


class SOUND(IntEnum):
    NitoBGM = 1313800
    CiaranBGM = 1313801
    BossDeath = 777777777
    BonfireMimic = 318011001  # voice (v)
    SkeletonAssembly = 290004002  # character_motion (c)


class SPEFFECT(IntEnum):
    CastLight = 620
    HealFull = 3231
    SunlightMaggot = 6950


class SPAWN(IntEnum):
    FirstBonfire = 1312960
    SecondBonfire = 1312961
    LimestoneCaveSpawn = 1312970


class ANIM(IntEnum):
    PlayerFadeIn = 6
    PlayerFallsOver = 2057
    PlayerSpawn = 6950
    SummonFadeIn = 6951
    TouchMimicBonfire = 7114
    WalkThroughFog = 7410
    SitAtBonfire = 7700
    SkeletonAssemble = 9061


class EVENT(IntEnum):
    PinwheelDead = 6
    NitoDead = 7
    CiaranGivenArtoriasSoul = 1862
    DeathSoulStolen = 11312006
    NitoAwake = 11310000
    SkeletonsDisturbed = 11312014
    CovenantVisit = 11310050
    CeaselessDischargeDead = 11410900
    ParishNitoCutsceneWarp = 11012003
    BlighttownNitoCutsceneWarp = 11402004
    WarpToAshLake = 11312004
    WarpToLostIzalith = 11312005
    CiaranFirstBattleStarted = 11315150
    CiaranSecondBattleStarted = 11312024
    CiaranFirstBattleDone = 11312023
    CiaranSecondBattleDone = 11312012
    LeeroyInvasionDone = 11310810
    CiaranDiedWithNito = 11312030

    PatchesHostileAgainstCleric = 1625
    PatchesHostile = 1627
    PatchesDead = 1628
    PatchesInTombBeforeKick = 1623
    PatchesInTombAfterKick = 1624
    PatchesInFirelink = 1626
    PatchesVanished = 1629  # New, happens if you steal the Death Soul before he kicks you into the pit.


class ITEMLOT(IntEnum):
    DeathSoul = 2560


class ITEM(IntEnum):
    DeathSoul = 2500


class TEXT(IntEnum):
    NitoBossName = 5220   # "Gravelord Nito"
    CiaranBossName = 5205  # "Gravedaughter Ciaran"
    CiaranAndNitoBossName = 5226  # "Gravelord Nito and Gravedaughter Ciaran"
    StealDeathSoul = 10010715
    TouchNitoBonfire = 10010742
    DeathlessAuraFades = 10010645
    DeathlessAuraSpreads = 10010646
    LightBonfire = 10010182


CliffSkeletons = (1310120, 1310121, 1310122)


def event0():
    header(0, 0)
    if DEBUG.PATCHES_IN_TOMB:
        for flag_id in [1625, 1627, 1628, 1638]:
            flag.disable(flag_id)
        flag.enable(EVENT.PinwheelDead)   # Pinwheel is "dead"
        flag.enable(EVENT.PatchesInTombBeforeKick)
    if DEBUG.BELLS_RUNG:
        flag.enable(EVENT.NitoAwake)
    if DEBUG.CEASELESS_DEAD:
        flag.enable(EVENT.CeaselessDischargeDead)
    if DEBUG.GET_LIGHT_SOURCES:
        item.award_item_to_host_only(34800100)  # Sorcerer's Catalyst
        item.award_item_to_host_only(1010514)  # Cast Light
        item.award_item_to_host_only(1310090)  # Skull Lantern
    if DEBUG.CIARAN_DIED_WITH_NITO:
        flag.enable(EVENT.CiaranDiedWithNito)

    sound.disable_map_sound(SOUND.CiaranBGM)  # Disable Ciaran's boss music.
    chr.disable(CHR.NitoWithCiaranBossHP)  # Disable Nito/Ciaran HP entity.
    for new_event in [
        11312001,  # Ceaseless Discharge visible in Demon Ruins.
        11312002,  # Disturbed Giant Skeletons block access to sleeping Nito.
        11312003,  # Player is warped to Ash Lake or Demon Ruins if they fall off a cliff while immortal.
        11312021,  # Light map is determined (depending on Ceaseless Discharge and Bells).
        11312022,  # Message that fog is blocked.
        11310098,  # Giant stuns itself.
        11310099,  # Giant wakes up.
        11312006,  # Steal Nito's Lord Soul while he sleeps.
        11312007,  # Warp out of Nito's cavern using his bonfire.
        11312008,  # Trigger first phase of Ciaran battle.
        11312009,  # Trigger second phase of Ciaran battle.
        11312011,  # Skeletons pincer you on the Ash Lake cliff during the second phase with Ciaran.
        11312012,  # Ciaran is escaped by climbing the long ladder.
        11312013,  # Ciaran's first or second phase resumes if the player respawns or reloads.
    ]:
        run_event(new_event)

    # (NEW) Bonfire mimics.
    run_event_with_slot(11312025, 0, args=(1311875, 1310875))
    run_event_with_slot(11312025, 1, args=(1311876, 1310876))

    # NOTE: Not registering Nito's bonfire at all, as there's no way to 'de-register' it when it turns out this is a
    # covenant visit. Warp prompt changed to "Touch the dead bonfire".

    # Register two bonfires.
    map.register_bonfire(11310992, 1311960, 2.0, 180.0, 0)
    map.register_bonfire(11310984, 1311961, 2.0, 180.0, 0)
    run_event(11312044)  # (NEW) Monitor warp list entry for upper bonfire.

    # Register all ladders.
    for ladder_id, ladder_on_flag, ladder_off_flag in zip(range(1311140, 1311149), range(11310010, 11310027, 2),
                                                          range(11310011, 11310028, 2)):
        map.register_ladder(ladder_on_flag, ladder_off_flag, ladder_id)

    # Two host-only event flags.
    skip_if_client(2)
    flag.disable(401)   # Wall removed by default, invasion allowed.
    flag.enable(11310095)   # Mimicking golden wall being gone already.

    # Fog barrier at start of area for other players.
    if_client(2)
    if_in_world_area(2, 13, 1)
    skip_if_condition_true(2, 2)
    obj.disable(1311994)
    sfx.delete_map_sfx(1311995, False)

    # (NEW) Ciaran's corpse appears in coffin next to Nito's if she died in Nito battle.
    skip_if_event_flag_on(3, EVENT.CiaranDiedWithNito)
    obj.disable_treasure(1311600)
    obj.disable(1311600)
    skip(2)
    obj.enable_treasure(1311600)
    run_event(11312031)  # (NEW) Helps pick up Ciaran's loot from above.

    # Gravelord events
    for gravelord_event in [11315040, 11315041, 11315042]:
        run_event(gravelord_event)

    # Light ball control
    run_event(11315100)

    # Nito's covenant (if you arrive via coffin from the Catacombs)
    for covenant_event in range(11310051, 11310055):
        run_event(covenant_event)
    run_event(11312032)  # (NEW) Disable covenant flag when player enters Ritual Grotto.

    # Illusory wall
    run_event(11310100)

    # Skeletons awoken by fighting a nearby Skeleton Beast or the Giant for too long.
    awaken_args = (
        (1310160, 1310140, 15.0, 11315300),
        (1310161, 1310141, 16.0, 11315301),
        (1310162, 1310142, 17.0, 11315302),
        (1310130, 1310143, 20.0, 11315303),   # Awoken by fighting Giant in the large coffin
        (1310164, 1310144, 14.0, 11315304),
        (1310165, 1310145, 15.0, 11315305),
    )
    for slot, args in enumerate(awaken_args):
        run_event_with_slot(11315200, slot, args=args, arg_types='IIfI')

    # Skeletons awoken because the bells are rung, the player has a light source, or Ciaran's second phase is active.
    for slot, args in enumerate(zip(range(1310140, 1310146), range(11315200, 11315206))):
        run_event_with_slot(11315300, slot, args=args, arg_types='II')
    for slot, args in enumerate(range(1310145, 1310155)):
        run_event_with_slot(11315300, slot+5, args=(args, 0), arg_types='II')

    # Bone Towers are triggered by proximity (5) only if Ciaran second phase is NOT active
    awaken_args = (
        (1310201, 1310201, 0),
        (1310202, 1310202, 0),
    )
    for slot, args in enumerate(awaken_args):
        run_event_with_slot(11315050, slot, args=args, arg_types='III')

    # Bone Towers are triggered by proximity (5) only if Ciaran second phase is active.
    awaken_args = (
        (1310200, 1310200, 0),
        (1310212, 1310212, 0),
    )
    for slot, args in enumerate(awaken_args):
        run_event_with_slot(11316050, slot, args=args, arg_types='III')

    # Bone Towers are triggered by Crystal Lizard death in pit.
    awaken_args = (
        (1310203, 11310820, 0),
        (1310204, 11310820, 0.2),
        (1310205, 11310820, 0.9),
        (1310206, 11310820, 1.0),
    )
    for slot, args in enumerate(awaken_args):
        run_event_with_slot(11315060, slot, args=args, arg_types='IIf')

    # Bone Towers are triggered by entering an area (ambush near item)
    awaken_args = (
        (1310207, 1312251, 0),
        (1310208, 1312251, 0.2),
        (1310209, 1312251, 0.4),
        (1310210, 1312251, 0.6),
        (1310211, 1312251, 0.8),
    )
    for slot, args in enumerate(awaken_args):
        run_event_with_slot(11315070, slot, args=args, arg_types='IIf')

    # Crystal Lizard doesn't respawn.
    run_event_with_slot(11310820, 0, args=(1310400, 33005000), arg_types='II')

    # GRAVELORD NITO

    sound.disable_map_sound(1313800)
    # If Nito is dead or asleep, the boss battle events aren't started.
    skip_if_event_flag_on(2, EVENT.NitoDead)
    skip_if_event_flag_off(1, EVENT.NitoAwake)
    skip(2)
    run_event(11315392)  # Fog handled inside.
    skip(9)

    # Otherwise, start his battle events.
    for nito_event in [
        11315390,  # Enter Nito's fog (host)
        11315391,  # Enter Nito's fog (summon)
        11315393,  # Start boss fight (buffs and notification)
        11315392,  # Prepare Nito for boss fight (AI, health bar)
        11310001,  # Watch for Nito's death
        11315394,  # Start music
        11315395,  # Stop music
        11315396,  # Kill skeletons that spawn off Nito - useless with 11315397 content cut.
        11315398,  # Nito's Gravelord Sword ranged attack
    ]:
        run_event(nito_event)


def event50():
    """ Preconstructor. """
    header(50)

    # (NEW) Nito awakening cutscene plays when you warp here from ringing second Bell.
    run_event(11312000)

    # PALADIN LEEROY (Invasion)

    chr.humanity_registration(6551, 8948)
    run_event(11315030)
    run_event(11310810)

    # RHEA OF THOROLUND

    chr.humanity_registration(6071, 8358)
    skip_if_event_flag_on(2, 1174)
    skip_if_event_flag_on(1, 1173)
    chr.disable(6071)
    run_event_with_slot(11310502, 0, args=(6071, 1176))
    run_event_with_slot(11310503, 0, args=(6071, 1179))
    run_event_with_slot(11310533, 0, args=(6071, 1170, 1181, 1177))
    run_event_with_slot(11310534, 0, args=(6071, 1170, 1181, 1180))
    run_event(11310530)
    run_event_with_slot(11310531, 0, args=(6071, 1170, 1181, 1174))
    run_event_with_slot(11310532, 0, args=(6071, 1170, 1181, 1175))

    # VINCE OF THOROLUND

    skip_if_event_flag_on(1, 1216)
    chr.disable(6091)
    chr.set_team_type(6091, TeamType.hostile_ally)
    run_event_with_slot(11310520, 1, args=(6091, 1210, 1219, 1214))

    # NICO OF THOROLUND

    skip_if_event_flag_on(1, 1226)
    chr.disable(6101)
    chr.set_team_type(6101, TeamType.hostile_ally)
    run_event_with_slot(11310520, 2, args=(6101, 1220, 1229, 1224))

    # TRUSTY PATCHES

    chr.humanity_registration(CHR.Patches, 8478)
    skip_if_event_flag_range_not_all_off(1, 1623, 1625)
    chr.disable(CHR.Patches)
    run_event_with_slot(11310501, 0, args=(CHR.Patches, EVENT.PatchesHostile))
    run_event_with_slot(11310543, 0, args=(CHR.Patches, EVENT.PatchesHostileAgainstCleric))
    run_event_with_slot(11310542, 0, args=(CHR.Patches, EVENT.PatchesDead))
    run_event_with_slot(11310540, 0, args=(CHR.Patches, 1620, 1631, EVENT.PatchesInTombBeforeKick))
    run_event_with_slot(11310541, 0, args=(CHR.Patches, 1620, 1631, EVENT.PatchesInTombAfterKick))
    run_event_with_slot(11310544, 0, args=(CHR.Patches, 1620, 1631, EVENT.PatchesVanished, EVENT.PatchesInFirelink))
    run_event(11310002)  # Patches kicks you into the pit (two cutscenes, depending on if you spoke to him first).


def event11312000():
    """ Nito awakening cutscene (then warp back to Parish or Quelaag). No way I can eliminate the slight glimpse of the
    player, unfortunately, but I've somewhat masked it with a brief warp. """
    header(11312000, 0)
    if_event_flag_on(-1, EVENT.ParishNitoCutsceneWarp)
    if_event_flag_on(-1, EVENT.BlighttownNitoCutsceneWarp)
    if_condition_true(0, -1)
    warp.warp(CHR.Player, 'region', 1312850, -1)
    obj.disable(OBJ.NitoBonfire)
    cutscene.play_cutscene_to_player(130100, CutsceneType.skippable, CHR.Player)
    wait_frames(1)
    skip_if_event_flag_off(2, EVENT.ParishNitoCutsceneWarp)
    warp.warp_player(10, 1, 1010990)  # Warp back to Parish.
    end()
    warp.warp_player(14, 0, 1400990)  # Warp back to Quelaag's Domain.


def event11312001():
    header(11312001, 1)
    skip_if_event_flag_off(3, EVENT.CeaselessDischargeDead)
    chr.disable(CHR.CeaselessDischarge)
    chr.kill(CHR.CeaselessDischarge)
    end()
    chr.disable_gravity(CHR.CeaselessDischarge)


def event11312002():
    """ Make Nito's boss fog appear when a Giant Skeleton is awakened. You have to leave the map to make them go back
    to sleep. Also enabled when Ciaran second encounter is done. """
    header(11312002)

    end_if_event_flag_on(EVENT.NitoAwake)
    end_if_event_flag_on(EVENT.CiaranSecondBattleDone)
    end_if_event_flag_on(EVENT.NitoDead)

    # Event only runs if Nito is asleep.

    obj.disable(OBJ.NitoFog)
    sfx.delete_map_sfx(SFX.NitoFog, False)
    if_event_flag_on(0, EVENT.SkeletonsDisturbed)
    obj.enable(OBJ.NitoFog)
    sfx.create_map_sfx(SFX.NitoFog)


def event11312021():
    """ Change to darker light map if Ceaseless Discharge is dead. """
    header(11312021)
    end_if_event_flag_off(EVENT.CeaselessDischargeDead)
    light.set_area_texture_parambank_slot_index(13, 1)


def event11312022():
    """ Show message that Nito is blocked if any giants are disturbed or Ciaran pursuit is done. """
    header(11312022)
    if_event_flag_off(1, EVENT.NitoAwake)
    if_event_flag_on(-1, EVENT.SkeletonsDisturbed)
    if_event_flag_on(-1, EVENT.CiaranSecondBattleDone)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    if_action_button_in_region(0, 1312998, 10010403, line_intersects=OBJ.NitoFog)
    message.status_explanation(10010630, True)
    restart()


def event11310098():
    header(11310098, 1)
    if_has_tae_event(0, CHR.Giant, 500)
    chr.ezstate_ai_request(CHR.Giant, 1500, 0)
    if_does_not_have_tae_event(0, CHR.Giant, 500)
    restart()


def event11310099():
    header(11310099, 1)
    if_has_tae_event(0, CHR.Giant, 1400)
    wait(10)
    chr.ezstate_ai_request(CHR.Giant, 1501, 0)
    restart()


def event11315050():
    """ Bone Towers only appear outside Ciaran battle. """
    header(11315050, 1)
    bone_tower, distance_trigger, delay = define_args('iif')
    skip_if_this_event_slot_off(2)
    chr.set_standby_animation_settings_to_default(bone_tower)
    end()
    chr.set_standby_animation_settings(bone_tower, standby_animation=9000)
    if_player_within_distance(1, distance_trigger, 5.0)
    if_event_flag_off(1, EVENT.CiaranSecondBattleStarted)
    if_condition_true(0, 1)
    wait(delay)
    chr.set_standby_animation_settings(bone_tower, cancel_animation=9060)
    chr.replan_ai(bone_tower)


def event11316050():
    """ Bone Towers only appear during Ciaran battle. """
    header(11316050, 1)
    bone_tower, distance_trigger, delay = define_args('iif')
    skip_if_this_event_slot_off(2)
    chr.set_standby_animation_settings_to_default(bone_tower)
    end()

    chr.set_standby_animation_settings(bone_tower, standby_animation=9000)
    if_entity_within_distance(1, distance_trigger, CHR.Player, 5.0)
    if_event_flag_on(1, EVENT.CiaranSecondBattleStarted)
    if_condition_true(0, 1)
    wait(delay)
    chr.set_standby_animation_settings(bone_tower, cancel_animation=9060)
    chr.replan_ai(bone_tower)


def event11315200():
    """ Skeleton assembles if a specific nearby enemy (Skeleton Beast or Giant) has been
    attacked by the player and a certain amount of time has passed. """
    header(11315200, 2)
    fighting_enemy, skeleton, delay = define_args('iif')
    if_entity_attacked_by(0, fighting_enemy, CHR.Player)
    wait(delay)
    if_entity_dead(1, fighting_enemy)
    skip_if_condition_false(1, 1)
    end()
    chr.set_standby_animation_settings(skeleton, cancel_animation=ANIM.SkeletonAssemble)
    flag.enable(EVENT.SkeletonsDisturbed)


def event11315300():
    """ Skeletons awakened by light, or if Nito is awake, or if Ciaran is in pursuit. """
    header(11315300, 2)
    skeleton, = define_args('i')
    if_entity_alive(1, skeleton)
    if_player_within_distance(1, skeleton, 5.0)
    if_event_flag_on(-1, EVENT.NitoAwake)
    if_event_flag_on(-1, EVENT.CiaranSecondBattleStarted)  # second phase of Ciaran fight
    if_entity_has_special_effect(-1, CHR.Player, SPEFFECT.CastLight)
    if_entity_has_special_effect(-1, CHR.Player, SPEFFECT.SunlightMaggot)
    if_skull_lantern_activated(-1)
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    chr.set_standby_animation_settings(skeleton, cancel_animation=ANIM.SkeletonAssemble)
    flag.enable(EVENT.SkeletonsDisturbed)


def event11315390():
    """ Nito fog interaction. """
    header(11315390, 0)
    if_event_flag_off(1, EVENT.NitoDead)
    if_entity_alive(1, CHR.NitoBoss)
    if_action_button_in_region(1, 1312998, 10010403, line_intersects=OBJ.NitoFog, boss_version=True)
    if_condition_true(0, 1)
    skip_if_event_flag_on(2, EVENT.NitoAwake)
    message.status_explanation(10010630)
    restart()
    chr.rotate_to_face_entity(CHR.Player, 1312997)
    anim.force_animation(CHR.Player, ANIM.WalkThroughFog)
    restart()


def event11312003():
    """ Warp to Ash Lake or Demon Ruins if player falls off while being chased by Ciaran. """
    # NOTE: Izalith warp disabled, as players were being taken there before defeating Quelaag, which is problematic.
    header(11312003)
    if_player_inside_region(1, REGION.WarpPlane)
    if_event_flag_on(1, EVENT.CiaranSecondBattleStarted)
    if_condition_true(0, 1)
    flag.disable(EVENT.CiaranFirstBattleStarted)
    flag.disable(EVENT.CiaranSecondBattleStarted)
    flag.enable(EVENT.CiaranSecondBattleDone)  # Ciaran encounter is over for good.
    # if_entity_within_distance(1, CHR.Player, REGION.WarpDestinationDecision, 85.0)
    # skip_if_condition_false(3, 1)
    flag.enable(EVENT.WarpToAshLake)
    warp.warp_player(13, 2, 1320990)  # Warp to Ash Lake.
    end()
    # flag.enable(EVENT.WarpToLostIzalith)
    # warp.warp_player(14, 1, 1410990)  # Warp to Lost Izalith.


def event11312006():
    """ Steal the Death Soul from Nito. """
    header(11312006)

    skip_if_event_flag_off(2, EVENT.NitoAwake)
    chr.disable(CHR.NitoAsleep)
    end()

    chr.disable_collision(CHR.NitoAsleep)
    chr.disable_gravity(CHR.NitoAsleep)
    # Sleeping Nito falls out of his coffin; warp him back in. (Not needed anymore, keeping this here just in case.)
    # if_player_inside_area(0, 1312990)
    # warp.warp(CHR.NitoAsleep, Category.region, 1312812, -1)

    # End event now if soul already stolen.
    end_if_this_event_on()

    # Steal Death Soul.
    if_event_flag_off(1, EVENT.CovenantVisit)
    if_action_button_state(1, Category.character, CHR.NitoAsleep, 180.0, -1, 7.0, TEXT.StealDeathSoul)
    if_condition_true(0, 1)
    item.award_item_to_host_only(ITEMLOT.DeathSoul)
    warp.set_player_respawn_point(SPAWN.LimestoneCaveSpawn)  # You're trapped now.
    wait(2.0)
    message.status_explanation(TEXT.DeathlessAuraSpreads)


def event11312007():
    """ Use Nito's bonfire to warp out of cave. Nito's bonfire never functions normally (as I want the game to be
    completed without the ability to warp, and this is a dead end). """
    header(11312007)

    # Wait until Nito is asleep or dead and this isn't a covenant visit.
    if_event_flag_off(1, EVENT.CovenantVisit)
    if_event_flag_on(-1, EVENT.NitoDead)
    if_event_flag_off(-1, EVENT.NitoAwake)
    if_condition_true(1, -1)
    if_action_button_state(1, Category.character, CHR.NitoBonfire, 180, -1, 2.0, TEXT.TouchNitoBonfire)
    if_condition_true(0, 1)

    chr.rotate_to_face_entity(CHR.Player, CHR.NitoBonfire)
    anim.force_animation(CHR.Player, ANIM.TouchMimicBonfire)
    wait(2.0)
    cutscene.play_cutscene_and_warp_player(-1, 0, REGION.LimestoneCaveSpawn, 13, 1)
    wait_frames(1)
    anim.force_animation(CHR.Player, ANIM.PlayerSpawn)
    restart()


def event11312008():
    """ Trigger first Ciaran battle. """
    header(11312008, 1)

    chr.disable(CHR.CiaranFirstSolo)
    obj.disable(OBJ.CiaranFog)
    sfx.delete_map_sfx(SFX.CiaranFog, False)

    end_if_event_flag_on(EVENT.NitoAwake)
    end_if_event_flag_on(EVENT.CiaranFirstBattleDone)
    end_if_event_flag_on(EVENT.CiaranGivenArtoriasSoul)

    if_player_has_good(1, ITEM.DeathSoul)
    if_entity_within_distance(1, CHR.Player, OBJ.CiaranFog, 25.0)   # Player approaches limestone exit.
    if_condition_true(0, 1)
    flag.enable(EVENT.CiaranFirstBattleStarted)  # Battle started.
    obj.enable(OBJ.CiaranFog)
    sfx.create_map_sfx(SFX.CiaranFog)
    obj.enable(OBJ.NitoFog)
    sfx.create_map_sfx(SFX.NitoFog)

    chr.enable_immortality(CHR.Player)
    for killplane in range(1313090, 1313099):
        hitbox.disable_hitbox(killplane)

    wait(3)
    sound.play_sound_effect(CHR.Player, SoundType.v_voice, 318020000)
    wait(3.4)
    sound.play_sound_effect(CHR.Player, SoundType.v_voice, 318020001)
    wait(1)

    chr.enable(CHR.CiaranFirstSolo)
    anim.force_animation(CHR.CiaranFirstSolo, ANIM.WalkThroughFog, wait_for_completion=True)
    sound.enable_map_sound(SOUND.CiaranBGM)
    boss.enable_boss_health_bar(CHR.CiaranFirstSolo, TEXT.CiaranBossName)
    chr.disable(CHR.FirstBonfire)  # Can't use either bonfire.
    chr.disable(CHR.SecondBonfire)
    run_event_with_slot(11312015, 0, args=(EVENT.CiaranFirstBattleStarted, 400, 401, 10010635))
    run_event_with_slot(11312015, 1, args=(11312015, 402, 403, 10010636))
    run_event_with_slot(11312015, 2, args=(11312016, 404, 405, 10010636))
    run_event_with_slot(11312015, 3, args=(11312017, 406, 407, 10010636))
    run_event_with_slot(11312015, 4, args=(11312018, 408, 409, 10010636))
    run_event(11312020)


def event11312009():
    """ Start second Ciaran battle when first one ends. """
    header(11312009, 1)

    chr.disable(CHR.CiaranSecondSolo)

    end_if_event_flag_on(EVENT.NitoAwake)
    end_if_event_flag_on(EVENT.CiaranSecondBattleDone)
    end_if_event_flag_on(EVENT.CiaranGivenArtoriasSoul)

    skip_if_event_flag_on(10, EVENT.CiaranFirstBattleDone)
    # FIRST TIME: Wait for first battle to end.
    if_event_flag_on(1, EVENT.CiaranFirstBattleStarted)
    if_entity_health_less_than_or_equal(1, CHR.CiaranFirstSolo, 0.0)
    if_entity_alive(1, CHR.Player)
    if_condition_true(0, 1)
    flag.enable(EVENT.CiaranFirstBattleDone)
    sound.play_sound_effect(CHR.CiaranFirstSolo, SoundType.v_voice, 318020100)  # Death gasp.
    wait(3.0)
    boss.disable_boss_health_bar(CHR.CiaranFirstSolo, TEXT.CiaranBossName)
    obj.disable(OBJ.CiaranFog)
    sfx.delete_map_sfx(SFX.CiaranFog, True)

    skip_if_event_flag_on(3, EVENT.CiaranSecondBattleStarted)
    # FIRST TIME: Player walks out of Ritual Grotto to start second battle.
    if_player_within_distance(0, CHR.CiaranSecondSolo, 5.0)
    sound.play_sound_effect(CHR.Player, SoundType.v_voice, 318020200)  # "Hm... such conceit."
    wait(1.5)

    flag.enable(EVENT.CiaranSecondBattleStarted)
    chr.enable(CHR.CiaranSecondSolo)
    chr.disable_health_bar(CHR.CiaranSecondSolo)
    chr.enable_invincibility(CHR.CiaranSecondSolo)
    chr.enable_immortality(CHR.CiaranSecondSolo)
    anim.force_animation(CHR.CiaranSecondSolo, ANIM.PlayerFadeIn)  # Fade in.
    run_event(11312010)  # Warp to player if too distant.

    end_if_event_flag_on(EVENT.CiaranFirstBattleStarted)
    # Enable music and soul-stealing events if not already set up in first battle.
    sound.enable_map_sound(SOUND.CiaranBGM)
    run_event_with_slot(11312015, 0, args=(EVENT.CiaranSecondBattleStarted, 400, 401, 10010635))
    run_event_with_slot(11312015, 1, args=(11312015, 402, 403, 10010636))
    run_event_with_slot(11312015, 2, args=(11312016, 404, 405, 10010636))
    run_event_with_slot(11312015, 3, args=(11312017, 406, 407, 10010636))
    run_event_with_slot(11312015, 4, args=(11312018, 408, 409, 10010636))
    run_event(11312020)  # Steal back Death Soul.


def event11312010():
    """ Ciaran warps behind you if you get too far away from her or she falls off. """
    header(11312010)

    # Respawn second Ciaran at the player's location if she falls off or gets too far away.
    if_event_flag_on(1, EVENT.CiaranSecondBattleStarted)
    if_event_flag_off(1, EVENT.CiaranSecondBattleDone)
    if_entity_inside_area(-1, CHR.CiaranSecondSolo, REGION.WarpPlane)  # If she falls off.
    if_player_beyond_distance(-1, CHR.CiaranSecondSolo, 30.0)  # If player gets too far away.
    if_condition_true(1, -1)
    if_condition_true(0, 1)
    chr.disable(CHR.CiaranSecondSolo)
    warp.warp_and_copy_floor(CHR.CiaranSecondSolo, Category.character, CHR.Player, 1, CHR.Player)
    wait(1.5)
    chr.enable(CHR.CiaranSecondSolo)
    anim.force_animation(CHR.CiaranSecondSolo, ANIM.PlayerFadeIn)
    restart()


def event11312011():
    """ Three skeletons triggered on cliff during Ciaran pursuit. """
    header(11312011, 1)

    for skeleton in CliffSkeletons:
        chr.disable(skeleton)

    skip_if_event_flag_off(4, EVENT.CiaranSecondBattleDone)
    for skeleton in CliffSkeletons:
        chr.kill(skeleton)
    end()

    if_event_flag_on(1, EVENT.CiaranSecondBattleStarted)
    if_player_within_distance(1, 1310120, 45.0)
    if_condition_true(0, 1)
    for skeleton in CliffSkeletons:
        chr.enable(skeleton)


def event11312012():
    """ Player escapes Ciaran by climbing the long ladder back toward Pinwheel. """
    header(11312012)
    if_event_flag_on(1, EVENT.CiaranSecondBattleStarted)
    if_player_inside_region(1, 1312991)
    if_condition_true(0, 1)

    # End boss fight and clean up boss stuff.
    warp.set_player_respawn_point(SPAWN.FirstBonfire)
    flag.enable(EVENT.CiaranSecondBattleDone)  # Marks Ciaran encounter as complete.
    for skeleton in CliffSkeletons:
        chr.disable(skeleton)
        chr.kill(skeleton)
    chr.disable_immortality(CHR.Player)
    for killplane in range(1313090, 1313099):
        hitbox.enable_hitbox(killplane)
    sound.play_sound_effect(CHR.Player, SoundType.s_sfx, SOUND.BossDeath)
    message.status_explanation(TEXT.DeathlessAuraFades, 1)   # "The Gravelord's deathless aura fades...".
    wait(2.0)
    sound.disable_map_sound(SOUND.CiaranBGM)
    chr.disable(CHR.CiaranSecondSolo)
    chr.kill(CHR.CiaranSecondSolo, False)
    flag.disable(EVENT.CiaranFirstBattleStarted)
    flag.disable(EVENT.CiaranSecondBattleStarted)
    chr.enable(CHR.FirstBonfire)
    chr.enable(CHR.SecondBonfire)


def event11312013():
    """ Sets up Ciaran second battle if player somehow reloads the map (e.g. quitting). """
    header(11312013)

    end_if_event_flag_on(EVENT.NitoAwake)
    end_if_event_flag_on(EVENT.CiaranSecondBattleDone)
    end_if_event_flag_on(EVENT.CiaranGivenArtoriasSoul)

    end_if_event_flag_off(EVENT.CiaranFirstBattleDone)  # Checked on load.

    # Warp player to spawn point, no matter where they are, forcing them to restart the chase.
    warp.warp(CHR.Player, Category.region, REGION.LimestoneCaveSpawn, -1)

    chr.enable_immortality(CHR.Player)
    obj.enable(OBJ.NitoFog)
    sfx.create_map_sfx(SFX.NitoFog)
    sound.enable_map_sound(SOUND.CiaranBGM)
    chr.disable(CHR.FirstBonfire)
    chr.disable(CHR.SecondBonfire)
    for killplane in range(1313090, 1313099):
        hitbox.disable_hitbox(killplane)
    obj.disable(OBJ.CiaranFog)
    sfx.delete_map_sfx(SFX.CiaranFog, False)

    # Ciaran 2 is set up in 11312009.


def event11312015():
    """ Ciaran 'kills' the player and takes a type of soul item from them, in increasing value. """
    header(11312015)

    required_flag, first_soul_type, second_soul_type, message_id = define_args('iiii')

    end_if_this_event_slot_on()

    if_event_flag_on(0, required_flag)
    wait(3.0)  # Allow previous heal to finish.

    if_entity_health_value_equal(0, CHR.Player, 1)
    if_condition_true(0, 1)
    anim.force_animation(CHR.Player, ANIM.PlayerFallsOver)
    item.remove_items_from_player(ItemType.good, first_soul_type, -1)  # Soul of a Lost Undead
    item.remove_items_from_player(ItemType.good, second_soul_type, -1)  # Large Soul of a Lost Undead
    message.status_explanation(message_id, True)  # "The Gravedaughter steals your souls"
    wait(1.0)
    chr.set_special_effect(CHR.Player, SPEFFECT.HealFull)  # Using Estus level 8.
    wait(1.0)  # Allow heal to finish before next soul-steal event checks.


def event11312020():
    """ Ciaran steals back the Death Soul. """
    header(11312020)
    end_if_this_event_on()
    if_event_flag_on(1, 11312019)
    if_entity_health_value_equal(1, CHR.Player, 1)
    if_condition_true(0, 1)
    anim.force_animation(CHR.Player, ANIM.PlayerFallsOver)
    item.remove_items_from_player(ItemType.good, ITEM.DeathSoul, -1)  # Death Soul
    flag.disable(50001560)  # Nito boss will re-drop it.
    wait(2.0)
    message.status_explanation(10010637, True)  # "The Gravedaughter reclaims the Death Soul"
    wait(1.0)
    chr.set_special_effect(CHR.Player, SPEFFECT.HealFull)  # Using Estus level 8.


def event11315392():
    """ Nito behavior. """
    header(11315392, 1)

    # If Nito is dead, disable basically everything except the exit bonfire, then end.
    skip_if_event_flag_off(11, EVENT.NitoDead)
    chr.disable(CHR.NitoBoss)
    chr.kill(CHR.NitoBoss)
    chr.disable(CHR.NitoCovenant)
    chr.kill(CHR.NitoCovenant)
    chr.disable(CHR.NitoAsleep)
    chr.kill(CHR.NitoAsleep)
    chr.disable(CHR.CiaranInNitoBoss)
    chr.kill(CHR.CiaranInNitoBoss)
    obj.disable(OBJ.NitoFog)
    sfx.delete_map_sfx(SFX.NitoFog, False)
    end()

    # If Nito is asleep, disable everything except sleeping Nito and exit bonfire, then end.
    skip_if_event_flag_on(5, EVENT.NitoAwake)
    chr.disable(CHR.NitoBoss)
    chr.disable(CHR.NitoCovenant)
    chr.disable(CHR.CiaranInNitoBoss)
    chr.enable(CHR.NitoAsleep)
    # Note that fog is handled in the Disturbed Skeletons event while Nito is asleep.
    end()

    # Otherwise, Nito is awake and alive and can be challenged.
    skip_if_this_event_on(1)
    skip_if_event_flag_on(1, EVENT.NitoAwake)
    chr.disable(CHR.NitoBoss)  # No need to disable Boss Nito if he's awake; no other way into the room at this point.
    chr.disable(CHR.NitoAsleep)
    chr.disable(CHR.CiaranInNitoBoss)
    chr.disable_ai(CHR.NitoBoss)

    if_host(1)
    if_event_flag_off(1, EVENT.CovenantVisit)
    if_player_inside_region(1, 1312999)
    if_condition_true(0, 1)

    # Start the boss fight.

    chr.enable_ai(CHR.NitoBoss)
    chr.set_team_type(CHR.NitoBoss, TeamType.enemy)  # So Nito doesn't hurt Ciaran. Ciaran should already be fine.

    # If Ciaran is present:
    skip_if_event_flag_on(7, EVENT.CiaranGivenArtoriasSoul)
    chr.enable(CHR.CiaranInNitoBoss)
    chr.disable_health_bar(CHR.NitoBoss)
    chr.enable_immortality(CHR.NitoBoss)
    chr.refer_damage_to_entity(CHR.NitoBoss, CHR.CiaranInNitoBoss)
    wait(3.0)
    boss.enable_boss_health_bar(CHR.CiaranInNitoBoss, TEXT.CiaranAndNitoBossName)
    skip(2)

    # Otherwise, just Nito:
    wait(2)
    boss.enable_boss_health_bar(CHR.NitoBoss, TEXT.NitoBossName)

    flag.enable(11315392)
    network.disable_sync()


def event11310001():
    """ Nito death, modified to handle end of combined Nito and Ciaran battle. This event will only run if
    Nito is alive and awake. """
    header(11310001)
    obj.disable(OBJ.NitoBonfire)

    if_entity_dead(1, CHR.NitoBoss)
    if_entity_health_less_than_or_equal(2, CHR.CiaranInNitoBoss, 0)
    if_condition_true(-1, 1)
    if_condition_true(-1, 2)
    if_condition_true(0, -1)

    # Nito and Ciaran only.
    skip_if_condition_false_finished(6, 2)
    chr.disable_immortality(CHR.NitoBoss)
    chr.kill(CHR.NitoBoss)  # In case you won by killing Ciaran.
    boss.disable_boss_health_bar(CHR.CiaranInNitoBoss, TEXT.CiaranAndNitoBossName)
    flag.disable_chunk(1860, 1869)
    flag.enable(1864)  # Sets Ciaran's NPC status to 'dead'.
    flag.enable(EVENT.CiaranDiedWithNito)

    # Either Nito fight.
    boss.kill_boss(CHR.NitoBoss)
    flag.enable(EVENT.NitoDead)  # Awards Death Soul (and a Homeward Bone).
    skip_if_client(1)
    game.award_achievement(35)
    obj.disable(OBJ.NitoFog)
    sfx.delete_map_sfx(SFX.NitoFog, True)
    chr.kill(CHR.NitoCovenant)
    chr.kill(CHR.NitoAsleep)
    sfx.create_oneoff_sfx(Category.object, OBJ.NitoBonfire, -1, 90014)  # Bonfire appearance effect.
    wait(2.0)
    obj.enable(OBJ.NitoBonfire)  # Remember bonfire only warps you out (not registered, no flame).


def event11315030():
    """ Paladin Leeroy invasion. """
    header(11315030)
    network.disable_sync()
    end_if_client()
    end_if_event_flag_on(11315031)
    # No longer requires Nito to be alive.

    if_host(1)
    if_character_human(1, CHR.Player)
    if_event_flag_off(1, EVENT.LeeroyInvasionDone)
    if_event_flag_off(1, EVENT.CiaranFirstBattleStarted)
    skip_if_this_event_on(1)
    if_player_inside_region(1, 1312001)
    if_condition_true(0, 1)
    message.place_summon_sign(SummonSignType.black_eye_sign, 6551, 1312000, 11315031, 11315032)
    wait(20)
    restart()


def event11312025():
    """ Bonfire Mimics. """
    header(11312025, 1)
    mimic_bonfire, baby_skeleton = define_args('ii')

    # Bonfire mimic killed, disable it.
    skip_if_this_event_slot_off(4)
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
    wait(2.4)
    sound.play_sound_effect(CHR.Player, SoundType.c_character_motion, SOUND.SkeletonAssembly)
    wait(0.75)
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


def event11312031():
    """ Pick up Ciaran's loot with the help of an action button. """
    header(11312031)
    end_if_event_flag_on(51310240)  # Corpse already looted.
    if_action_button_state(0, Category.object, 1311600, 180.0, -1, 2.5, 10010101)
    item.award_item_to_host_only(1310240)
    obj.disable_treasure(1311600)


def event11312032():
    """ Disable covenant visit flag when player enters Ritual Grotto. """
    header(11312032, 1)

    if_event_flag_on(1, EVENT.CovenantVisit)
    if_player_inside_region(1, REGION.RitualGrottoEntrance)
    if_condition_true(0, 1)

    flag.disable(EVENT.CovenantVisit)
    restart()


def event11310051():
    """ Entity control for Nito (covenant visit, asleep, awake). """
    header(11310051, 1)

    # Disable covenant things.
    chr.disable(CHR.NitoCovenant)
    obj.disable(OBJ.NitoCovenantCoffin)
    obj.disable_activation(OBJ.NitoCovenantCoffin, -1)

    # COVENANT NITO SETUP. Only proceeds from here if this is a Covenant visit and Nito is asleep.
    if_event_flag_on(1, EVENT.CovenantVisit)
    if_event_flag_off(1, EVENT.NitoAwake)
    if_condition_true(0, 1)

    # Disable sleeping Nito (for stealing), Boss Nito (though he shouldn't be there), Ciaran, and the exit bonfire.
    chr.disable(CHR.NitoAsleep)
    chr.disable(CHR.CiaranInNitoBoss)
    chr.disable(CHR.NitoBoss)
    obj.disable(OBJ.NitoBonfire)
    skip_if_event_flag_on(1, EVENT.NitoDead)
    chr.enable(CHR.NitoCovenant)  # Enable sleeping Covenant Nito if he's alive.
    obj.enable(OBJ.NitoCovenantCoffin)
    obj.enable_activation(OBJ.NitoCovenantCoffin, -1)

    # NOTE CovenantVisit flag will only be disabled if you leave via the coffin, not die/bone out.
    # It will be disabled when you enter the Ritual Grotto on foot in this event.
    if_event_flag_off(0, EVENT.CovenantVisit)

    # Set things back the way they were, depending on whether Nito is asleep, awake, or dead.

    # If Nito is asleep, enable sleeping Nito and the exit bonfire.
    skip_if_event_flag_on(3, EVENT.NitoAwake)
    chr.enable(CHR.NitoAsleep)
    obj.enable(OBJ.NitoBonfire)
    skip(2)
    # Otherwise, if Nito is awake and alive, enable Boss Nito.
    skip_if_event_flag_on(1, EVENT.NitoDead)
    chr.enable(CHR.NitoBoss)

    # Covenant things will be disabled on restart.
    restart()


def event11310052():
    """ Leave after covenant visit. """
    header(11310052)
    if_object_activated(0, 11315340)
    chr.set_standby_animation_settings(CHR.Player, standby_animation=7151, death_animation=6082)
    wait(3.0)
    cutscene.play_cutscene_and_warp_specific_player(130121, CutsceneType.skippable, 1302010, 13, 0, CHR.Player)
    cutscene.play_cutscene_to_player(130021, CutsceneType.skippable, CHR.Player)
    wait_frames(1)
    flag.disable(EVENT.CovenantVisit)
    chr.disable(1300281)  # Bonewheel near coffin in Catacombs.
    chr.disable(1300282)  # Bonewheel near coffin in Catacombs.
    chr.set_standby_animation_settings_to_default(CHR.Player)
    obj.enable_activation(OBJ.NitoCovenantCoffin, -1)
    restart()


def event11310544():
    """ Patches moves to Firelink (disappears from here) immediately if you steal the Death Soul. If he hasn't kicked
    you, he will simply disappear for the rest of this playthrough. """
    header(11310544)
    patches, first_flag, last_flag, vanished_flag, firelink_flag = define_args('iiiii')
    if_event_flag_off(1, 1622)
    if_event_flag_off(1, EVENT.PatchesHostileAgainstCleric)
    if_event_flag_off(1, EVENT.PatchesHostile)
    if_event_flag_off(1, EVENT.PatchesDead)
    if_event_flag_on(1, EVENT.DeathSoulStolen)
    if_event_flag_on(-1, EVENT.PatchesInTombBeforeKick)
    if_event_flag_on(-1, EVENT.PatchesInTombAfterKick)
    if_condition_true(1, -1)
    if_condition_true(0, 1)

    skip_if_event_flag_on(3, EVENT.PatchesInTombAfterKick)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(vanished_flag)
    skip(2)
    flag.disable_chunk(first_flag, last_flag)
    flag.enable(firelink_flag)

    chr.disable(patches)


def event11312044():
    """ Add bonfire to warp menu. """
    header(11312044)
    if_player_within_distance(1, 1311960, 5.0)
    if_has_tae_event(1, CHR.Player, 700)
    if_condition_true(0, 1)
    flag.enable(11312044)


if __name__ == '__main__':

    event_function_list = [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if
                           (inspect.isfunction(obj) and name.startswith('event') and name != 'event')]

    build_emevd_from_template(event_function_list, map_name, emevd_directory)
