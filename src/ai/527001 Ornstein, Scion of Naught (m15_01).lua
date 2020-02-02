--@package: m15_01_00_00.luabnd, 527001_battle.lua
--@battle_goal: 527001, Griffith527001Battle

local localScriptConfigVar1 = 4.5
local localScriptConfigVar3 = 6.2
local localScriptConfigVar5 = 10.8
local localScriptConfigVar9 = 12.3
local localScriptConfigVar11 = 4.5
local localScriptConfigVar15 = 11.4
local localScriptConfigVar21 = 4.9

Griffith527001Battle_Activate = function(ai, goal)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local selfHpRate = ai:GetHpRate(TARGET_SELF)
   local oneHandedComboOdds = 0
   local twoHandedComboOdds = 0
   local jumpThrustOdds = 0
   local jumpSlamOdds = 0
   local longThrustOdds = 0
   local runningThrustOdds = 0
   local lightningSpearOdds = 0
   local flightOdds = 0
   local jumpBackOdds = 0
   local quickLightningOdds = 0
   local drillOdds = 0
   local adjustSpaceOdds = 0
   local adjustSpaceMultiplier = 1
   if selfHpRate < 0.5 then
      -- Evades after attacks more often when below 50% health.
      adjustSpaceMultiplier = 2
   end
   if enemyDistance >= 12.3 then
      oneHandedComboOdds = 0
      twoHandedComboOdds = 0
      jumpThrustOdds = 0
      jumpSlamOdds = 10
      longThrustOdds = 10
      runningThrustOdds = 10
      lightningSpearOdds = 10
      flightOdds = 60
      jumpBackOdds = 0
      quickLightningOdds = 0
      drillOdds = 0
   elseif enemyDistance >= 10.8 then
      oneHandedComboOdds = 0
      twoHandedComboOdds = 0
      jumpThrustOdds = 0
      jumpSlamOdds = 20
      longThrustOdds = 20
      runningThrustOdds = 20
      lightningSpearOdds = 20
      flightOdds = 20
      jumpBackOdds = 0
      quickLightningOdds = 0
      drillOdds = 0
   elseif enemyDistance >= 6.2 then
      oneHandedComboOdds = 10
      twoHandedComboOdds = 10
      jumpThrustOdds = 35
      jumpSlamOdds = 0
      longThrustOdds = 15
      runningThrustOdds = 0
      lightningSpearOdds = 10
      flightOdds = 0
      jumpBackOdds = 0
      quickLightningOdds = 10
      drillOdds = 10
   elseif enemyDistance >= 2.5 then
      oneHandedComboOdds = 25
      twoHandedComboOdds = 25
      jumpThrustOdds = 0
      jumpSlamOdds = 0
      longThrustOdds = 20
      runningThrustOdds = 0
      lightningSpearOdds = 0
      flightOdds = 0
      jumpBackOdds = 0
      quickLightningOdds = 10
      drillOdds = 20
   else
      oneHandedComboOdds = 13
      twoHandedComboOdds = 12
      jumpThrustOdds = 0
      jumpSlamOdds = 0
      longThrustOdds = 0
      runningThrustOdds = 0
      lightningSpearOdds = 0
      flightOdds = 0
      jumpBackOdds = 60
      quickLightningOdds = 5
      drillOdds = 10
   end
   local fate = ai:GetRandam_Int(1, oneHandedComboOdds + twoHandedComboOdds + jumpThrustOdds + jumpSlamOdds
           + longThrustOdds + runningThrustOdds + lightningSpearOdds + flightOdds + jumpBackOdds + quickLightningOdds
           + drillOdds)
   if fate <= oneHandedComboOdds then
      Griffith527001_Act01(ai, goal)
      adjustSpaceOdds = 50 * adjustSpaceMultiplier
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds then
      Griffith527001_Act02(ai, goal)
      adjustSpaceOdds = 50 * adjustSpaceMultiplier
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpThrustOdds then
      Griffith527001_Act03(ai, goal)
      adjustSpaceOdds = 50 * adjustSpaceMultiplier
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpThrustOdds + jumpSlamOdds then
      Griffith527001_Act04(ai, goal)
      adjustSpaceOdds = 50 * adjustSpaceMultiplier
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpThrustOdds + jumpSlamOdds + longThrustOdds then
      Griffith527001_Act05(ai, goal)
      adjustSpaceOdds = 50 * adjustSpaceMultiplier
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpThrustOdds + jumpSlamOdds + longThrustOdds
           + runningThrustOdds then
      Griffith527001_Act06(ai, goal)
      adjustSpaceOdds = 50 * adjustSpaceMultiplier
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpThrustOdds + jumpSlamOdds + longThrustOdds
           + runningThrustOdds + lightningSpearOdds then
      Griffith527001_Act07(ai, goal)
      adjustSpaceOdds = 0
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpThrustOdds + jumpSlamOdds + longThrustOdds
           + runningThrustOdds + lightningSpearOdds + flightOdds then
      Griffith527001_Act08(ai, goal)
      adjustSpaceOdds = 50 * adjustSpaceMultiplier
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpThrustOdds + jumpSlamOdds + longThrustOdds
           + runningThrustOdds + lightningSpearOdds + flightOdds + jumpBackOdds then
      Griffith527001_Act09(ai, goal)
      adjustSpaceOdds = 0
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpThrustOdds + jumpSlamOdds + longThrustOdds
           + runningThrustOdds + lightningSpearOdds + flightOdds + jumpBackOdds + quickLightningOdds then
      Griffith527001_Act10(ai, goal)
      adjustSpaceOdds = 0
   else
      Griffith527001_Act11(ai, goal)
      adjustSpaceOdds = 50 * adjustSpaceMultiplier
   end
   local adjustSpaceFate = ai:GetRandam_Int(1, 100)
   if adjustSpaceFate <= adjustSpaceOdds then
      Griffith527001_ActAfter_AdjustSpace(ai, goal, paramTbl)
   end
end

Griffith527001_Act01 = function(ai, goal)
   local func3_var3 = localScriptConfigVar1
   local func3_var4 = localScriptConfigVar1 + 2
   local func3_var5 = 0
   local func3_var6 = ai:GetRandam_Int(1, 100)
   Approach_Act(ai, goal, func3_var3, func3_var4, func3_var5)
   if func3_var6 <= 5 then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4000, TARGET_ENE_0, DIST_Middle, 0)
   elseif func3_var6 <= 15 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 4000, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 4001, TARGET_ENE_0, DIST_Middle, 0)
   elseif func3_var6 <= 60 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 4000, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 4001, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 4002, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 4000, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 4001, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 4002, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 4003, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Griffith527001_Act02 = function(ai, goal)
   local func4_var3 = localScriptConfigVar11
   local func4_var4 = localScriptConfigVar11 + 2
   local func4_var5 = 0
   local func4_var6 = ai:GetRandam_Int(1, 100)
   Approach_Act(ai, goal, func4_var3, func4_var4, func4_var5)
   if func4_var6 <= 10 then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4008, TARGET_ENE_0, DIST_Middle, 0)
   elseif func4_var6 <= 30 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 4008, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 4009, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 4008, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 4009, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 4010, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Griffith527001_Act03 = function(ai, goal)
   local func5_var3 = localScriptConfigVar3
   local func5_var4 = localScriptConfigVar3 + 2
   local func5_var5 = 0
   Approach_Act(ai, goal, func5_var3, func5_var4, func5_var5)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4004, TARGET_ENE_0, DIST_Middle, 0)
end

Griffith527001_Act04 = function(ai, goal)
   local func6_var3 = localScriptConfigVar5
   local func6_var4 = localScriptConfigVar5 + 2
   local func6_var5 = 0
   Approach_Act(ai, goal, func6_var3, func6_var4, func6_var5)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4005, TARGET_ENE_0, DIST_Middle, 0)
end

Griffith527001_Act05 = function(ai, goal)
   local func7_var3 = localScriptConfigVar9
   local func7_var4 = localScriptConfigVar9 + 2
   local func7_var5 = 0
   Approach_Act(ai, goal, func7_var3, func7_var4, func7_var5)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4007, TARGET_ENE_0, DIST_Middle, 0)
end

Griffith527001_Act06 = function(ai, goal)
   local func8_var3 = localScriptConfigVar15
   local func8_var4 = localScriptConfigVar15 + 2
   local func8_var5 = 0
   Approach_Act(ai, goal, func8_var3, func8_var4, func8_var5)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4012, TARGET_ENE_0, DIST_Middle, 0)
end

Griffith527001_Act07 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4011, TARGET_ENE_0, DIST_None, 0)
end

Griffith527001_Act08 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4013, TARGET_ENE_0, DIST_None, 0)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 20, TARGET_ENE_0, 5.5, TARGET_SELF, false, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 4014, TARGET_ENE_0, DIST_None, 0, -1)
end

Griffith527001_Act09 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4006, TARGET_ENE_0, DIST_Middle, 0)
end

Griffith527001_Act10 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4016, TARGET_ENE_0, DIST_None, 0)
end

Griffith527001_Act11 = function(ai, goal)
   local func13_var3 = localScriptConfigVar21
   local func13_var4 = localScriptConfigVar21 + 2
   local func13_var5 = 0
   local func13_var6 = ai:GetRandam_Int(1, 100)
   Approach_Act(ai, goal, func13_var3, func13_var4, func13_var5)
   if func13_var6 <= 50 then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4017, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 4017, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 4018, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Griffith527001_ActAfter_AdjustSpace = function(ai, goal, func14_param2)
   local fate = ai:GetRandam_Int(0, 100)
   local directionFate = ai:GetRandam_Int(0, 1)
   local func14_var5 = ai:GetTeamRecordCount(COORDINATE_TYPE_SideWalk_L + directionFate, TARGET_ENE_0, 2)
   if fate <= 30 and func14_var5 < 2 then
      goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 2.5, TARGET_ENE_0, 2, TARGET_ENE_0, true, -1)
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, directionFate, ai:GetRandam_Int(30, 45), true, true, -1)
   elseif fate <= 60 then
      goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 2.5, TARGET_ENE_0, 3, TARGET_ENE_0, true, -1)
   elseif fate <= 80 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 4)
   else
      local dodgeDirectionFate = ai:GetRandam_Int(1, 100)
      if dodgeDirectionFate <= 50 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 4)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 4)
      end
   end
end

Griffith527001Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Griffith527001Battle_Terminate = function(ai, goal)
end

Griffith527001Battle_Interupt = function(ai, goal)
   local func17_var6 = 3
   local func17_var7 = 25
   local func17_var8 = 40
   local func17_var9 = 30
   local func17_var10 = 30
   local func17_var11 = 4
   if Damaged_Step(ai, goal, func17_var6, func17_var7, func17_var8, func17_var9, func17_var10, func17_var11) then
      return true
   end
   local func17_var12 = 6.2
   local func17_var13 = 70
   local func17_var15 = ai:GetDist(TARGET_ENE_0)
   if GuardBreak_Act(ai, goal, func17_var12, func17_var13) then
      if func17_var15 >= 4.5 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4004, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4008, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local func17_var16 = 6.2
   local func17_var17 = 50
   local func17_var18 = ai:GetDist(TARGET_ENE_0)
   if MissSwing_Int(ai, goal, func17_var16, func17_var17) then
      if func17_var18 >= 4.5 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4004, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4008, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local func17_var19 = 12.3
   local func17_var20 = 30
   if UseItem_Act(ai, goal, func17_var19, func17_var20) then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 4011, TARGET_ENE_0, DIST_Middle, 0)
      return true
   end
   local func17_var22 = 35
   local func17_var23 = 40
   local func17_var24 = 30
   local func17_var25 = 30
   local func17_var26 = 4
   if RebByOpGuard_Step(ai, goal, func17_var22, func17_var23, func17_var24, func17_var25, func17_var26) then
      return true
   end
   local func17_var27 = 3
   local func17_var28 = 18
   local func17_var29 = 0
   local func17_var30 = 60
   local dodgeLeftOdds = ai:GetRandam_Int(1, 100)
   local shootInterrupt = Shoot_2dist(ai, goal, func17_var27, func17_var28, func17_var29, func17_var30)
   if shootInterrupt == 1 then
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, ai:GetRandam_Int(0, 1), ai:GetRandam_Int(30, 45), true, true, 9910)
      return true
   elseif shootInterrupt == 2 then
      if dodgeLeftOdds <= 75 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 4)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 4)
      end
      return true
   end
   return false
end


