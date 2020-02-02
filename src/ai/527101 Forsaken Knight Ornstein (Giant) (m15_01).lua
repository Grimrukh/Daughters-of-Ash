--@package: m15_01_00_00.luabnd, 527101_battle.lua
--@battle_goal: 527101, Griffith_large527101Battle

-- When supporting, melee attacks are ONLY used when close, and he will sometimes strafe while shooting.

local localScriptConfigVar1 = 3.5
local localScriptConfigVar3 = 9.8
local localScriptConfigVar5 = 16.5
local localScriptConfigVar9 = 17
local localScriptConfigVar11 = 6.5
local localScriptConfigVar23 = 7.8
Griffith_large527101Battle_Activate = function(ai, goal)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   ai:AddObserveArea(0, TARGET_FRI_0, TARGET_SELF, AI_DIR_TYPE_F, 360, 10)
   local isSupport = ai:GetEventRequest(0)  -- 1 in support, 0 in main
   local enemyBehind = 0
   local enemyLeft = 0
   local enemyRight = 0
   local canDodge = 0
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_B, 8) then
      enemyBehind = 1
   end
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_L, 6) then
      enemyLeft = 1
   end
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_R, 6) then
      enemyRight = 1
   end
   if enemyRight == 1 or enemyLeft == 1 or enemyBehind == 1 then
      canDodge = 1
   end
   local oneHandedComboOdds = 0
   local twoHandedComboOdds = 0
   local jumpingThrustOdds = 0
   local jumpingSlamOdds = 0
   local longThrustOdds = 0
   local grabStabOdds = 0
   local lightningSpearOdds = 0
   local scoopThrustOdds = 0
   local jumpBackOdds = 0
   local buttSlamOdds = 0
   local quickLightningOdds = 0
   local drillScoopOdds = 0
   local dodgeOdds = 0
   local adjustSpaceOdds = 0
   if isSupport == 1 then
      -- SUPPORT behavior.
      if enemyDistance >= 5 then
         local shootFate = ai:GetRandam_Int(1, 100)
         if shootFate <= 40 then
            -- Just strafe.
            goal:AddSubGoal(GOAL_COMMON_SidewayMove, 2, TARGET_ENE_0, ai:GetRandam_Int(0, 1), ai:GetRandam_Int(30, 45), true, true, -1)
            return
         else
            lightningSpearOdds = 30
            quickLightningOdds = 30
         end
      elseif enemyDistance >= 3 then
         lightningSpearOdds = 40
         quickLightningOdds = 40
         buttSlamOdds = 20
      elseif enemyDistance >= 1.5 then
         oneHandedComboOdds = 15
         twoHandedComboOdds = 15
         drillScoopOdds = 15
         buttSlamOdds = 20
         dodgeOdds = 30 * canDodge
      else
         grabStabOdds = 40
         jumpBackOdds = 20
         buttSlamOdds = 20
         dodgeOdds = 20 * canDodge
      end
   else
      -- MAIN behavior.
      if enemyDistance >= 30 then
         jumpingSlamOdds = 10
         longThrustOdds = 10
         lightningSpearOdds = 10
         scoopThrustOdds = 60
         quickLightningOdds = 10
      elseif enemyDistance >= 20 then
         jumpingSlamOdds = 20
         longThrustOdds = 20
         lightningSpearOdds = 15
         scoopThrustOdds = 35
         quickLightningOdds = 10
      elseif enemyDistance >= 14.1 then
         jumpingSlamOdds = 25
         longThrustOdds = 25
         lightningSpearOdds = 25
         quickLightningOdds = 25
      elseif enemyDistance >= 7 then
         oneHandedComboOdds = 10
         twoHandedComboOdds = 10
         jumpingThrustOdds = 40
         quickLightningOdds = 20
         drillScoopOdds = 20
      elseif enemyDistance >= 5 then
         oneHandedComboOdds = 25
         twoHandedComboOdds = 25
         quickLightningOdds = 30
         drillScoopOdds = 20
      elseif enemyDistance >= 4.3 then
         oneHandedComboOdds = 35
         drillScoopOdds = 35
         dodgeOdds = 30 * canDodge
      elseif enemyDistance >= 3 then
         oneHandedComboOdds = 25
         twoHandedComboOdds = 25
         buttSlamOdds = 20
         dodgeOdds = 30 * canDodge
      elseif enemyDistance >= 1.5 then
         buttSlamOdds = 50
         dodgeOdds = 50 * canDodge
      else
         grabStabOdds = 40
         jumpBackOdds = 20
         buttSlamOdds = 20
         dodgeOdds = 20 * canDodge
      end
   end
   local fate = ai:GetRandam_Int(1, oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds + longThrustOdds + grabStabOdds +
           lightningSpearOdds + scoopThrustOdds + jumpBackOdds + buttSlamOdds + quickLightningOdds + drillScoopOdds + dodgeOdds)
   if fate <= oneHandedComboOdds then
      Griffith_large527101_Act01(ai, goal)
      adjustSpaceOdds = 50
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds then
      Griffith_large527101_Act02(ai, goal)
      adjustSpaceOdds = 50
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds then
      Griffith_large527101_Act03(ai, goal)
      adjustSpaceOdds = 50
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds then
      Griffith_large527101_Act04(ai, goal)
      adjustSpaceOdds = 50
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds + longThrustOdds then
      Griffith_large527101_Act05(ai, goal)
      adjustSpaceOdds = 50
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds + longThrustOdds + grabStabOdds then
      Griffith_large527101_Act06(ai, goal)
      adjustSpaceOdds = 50
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds + longThrustOdds + grabStabOdds + lightningSpearOdds then
      Griffith_large527101_Act07(ai, goal)
      adjustSpaceOdds = 0
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds + longThrustOdds + grabStabOdds + lightningSpearOdds
           + scoopThrustOdds then
      Griffith_large527101_Act08(ai, goal)
      adjustSpaceOdds = 100
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds + longThrustOdds + grabStabOdds + lightningSpearOdds
           + scoopThrustOdds + jumpBackOdds then
      Griffith_large527101_Act09(ai, goal)
      adjustSpaceOdds = 0
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds + longThrustOdds + grabStabOdds + lightningSpearOdds
           + scoopThrustOdds + jumpBackOdds + buttSlamOdds then
      Griffith_large527101_Act10(ai, goal)
      adjustSpaceOdds = 0
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds + longThrustOdds + grabStabOdds + lightningSpearOdds
           + scoopThrustOdds + jumpBackOdds + buttSlamOdds + quickLightningOdds then
      Griffith_large527101_Act11(ai, goal)
      adjustSpaceOdds = 0
   elseif fate <= oneHandedComboOdds + twoHandedComboOdds + jumpingThrustOdds + jumpingSlamOdds + longThrustOdds + grabStabOdds + lightningSpearOdds
           + scoopThrustOdds + jumpBackOdds + buttSlamOdds + quickLightningOdds + drillScoopOdds then
      Griffith_large527101_Act12(ai, goal)
      adjustSpaceOdds = 0
   else
      Griffith_large527101_Act13(ai, goal)
      adjustSpaceOdds = 0
   end
   local adjustSpaceFate = ai:GetRandam_Int(1, 100)
   if adjustSpaceFate <= adjustSpaceOdds then
      Griffith_large527101_ActAfter_AdjustSpace(ai, goal, paramTbl)
   end
end

Griffith_large527101_Act01 = function(ai, goal)
   -- One-handed basic combo.
   local func2_var3 = localScriptConfigVar1
   local func2_var4 = localScriptConfigVar1 + 4.5
   local func2_var5 = 0
   local comboOdds = ai:GetRandam_Int(1, 100)
   BusyApproach_Act(ai, goal, func2_var3, func2_var4, func2_var5)
   if comboOdds <= 5 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, 2, 10)
   elseif comboOdds <= 15 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, 2, 10)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
   elseif comboOdds <= 60 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, 2, 10)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3002, TARGET_ENE_0, DIST_Near, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, 2, 10)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3002, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3003, TARGET_ENE_0, DIST_Near, 0)
   end
end

Griffith_large527101_Act02 = function(ai, goal)
   -- Two-handed basic combo.
   local func3_var3 = localScriptConfigVar11
   local func3_var4 = localScriptConfigVar11 + 4.5
   local func3_var5 = 0
   local comboOdds = ai:GetRandam_Int(1, 100)
   BusyApproach_Act(ai, goal, func3_var3, func3_var4, func3_var5)
   if comboOdds <= 10 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 2, 42)
   elseif comboOdds <= 30 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 2, 42)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 2, 42)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3010, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Griffith_large527101_Act03 = function(ai, goal)
   -- Jumping thrust.
   local func4_var3 = localScriptConfigVar3
   local func4_var4 = localScriptConfigVar3 + 4.5
   local func4_var5 = 0
   BusyApproach_Act(ai, goal, func4_var3, func4_var4, func4_var5)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3004, TARGET_ENE_0, DIST_None, 2, 35)
end

Griffith_large527101_Act04 = function(ai, goal)
   -- Jumping slam.
   local func5_var3 = localScriptConfigVar5
   local func5_var4 = localScriptConfigVar5 + 4.5
   local func5_var5 = 0
   BusyApproach_Act(ai, goal, func5_var3, func5_var4, func5_var5)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3005, TARGET_ENE_0, DIST_None, 2, 45)
end

Griffith_large527101_Act05 = function(ai, goal)
   -- Approach and use long crouched right hand thrust.
   local func6_var3 = localScriptConfigVar9
   local func6_var4 = localScriptConfigVar9 + 4.5
   local func6_var5 = 0
   BusyApproach_Act(ai, goal, func6_var3, func6_var4, func6_var5)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3007, TARGET_ENE_0, DIST_Middle, 0)
end

Griffith_large527101_Act06 = function(ai, goal)
   -- Grab stab.
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_None, 2, 35)
end

Griffith_large527101_Act07 = function(ai, goal)
   -- Lightning spear.
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3011, TARGET_ENE_0, DIST_None, 0)
end

Griffith_large527101_Act08 = function(ai, goal)
   -- Scoop and thrust?
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3013, TARGET_ENE_0, DIST_None, 0)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 20, TARGET_ENE_0, 11.3, TARGET_SELF, false, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3014, TARGET_ENE_0, DIST_None, 0, -1)
end

Griffith_large527101_Act09 = function(ai, goal)
   -- Jump back and swing.
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3006, TARGET_ENE_0, DIST_Middle, 2, 37)
end

Griffith_large527101_Act10 = function(ai, goal)
   -- Butt slam.
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3015, TARGET_ENE_0, DIST_Middle, 0, -1)
end

Griffith_large527101_Act11 = function(ai, goal)
   -- Short one-handed stab.
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3016, TARGET_ENE_0, DIST_None, 0)
end

Griffith_large527101_Act12 = function(ai, goal)
   -- Drill and scoop.
   local func13_var3 = localScriptConfigVar23
   local func13_var4 = localScriptConfigVar23 + 4.5
   local func13_var5 = 0
   local scoopOdds = ai:GetRandam_Int(1, 100)
   BusyApproach_Act(ai, goal, func13_var3, func13_var4, func13_var5)
   if scoopOdds <= 50 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3017, TARGET_ENE_0, DIST_None, 2, 45)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3017, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3018, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Griffith_large527101_Act13 = function(ai, goal)
   -- Dodge.
   local dodgeOdds = ai:GetRandam_Int(1, 100)
   local enemyIsBehind = 0
   local enemyIsLeft = 0
   local enemyIsRight = 0
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_B, 8) then
      enemyIsBehind = 1
   end
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_L, 6) then
      enemyIsLeft = 1
   end
   if ai:IsOnNearMeshByPos(TARGET_SELF, AI_DIR_TYPE_R, 6) then
      enemyIsRight = 1
   end
   if enemyIsBehind == 1 or enemyIsRight == 0 and enemyIsLeft == 0 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 8)
   elseif dodgeOdds <= 50 or enemyIsLeft == 0 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 6)
   else
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 6)
   end
   return true
end

Griffith_large527101_ActAfter_AdjustSpace = function(ai, goal, func15_param2)
   local func15_var3 = ai:GetRandam_Int(0, 100)
   local func15_var4 = ai:GetRandam_Int(0, 1)
   local func15_var5 = ai:GetTeamRecordCount(COORDINATE_TYPE_SideWalk_L + func15_var4, TARGET_ENE_0, 2)
   if func15_var3 <= 30 and func15_var5 < 2 then
      goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 2.5, TARGET_ENE_0, 2, TARGET_ENE_0, true, -1)
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, func15_var4, ai:GetRandam_Int(30, 45), true, true, -1)
   elseif func15_var3 <= 60 then
      goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 2.5, TARGET_ENE_0, 3, TARGET_ENE_0, true, -1)
   elseif func15_var3 <= 80 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 4)
   else
      local func15_var6 = ai:GetRandam_Int(1, 100)
      if func15_var6 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 4)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 4)
      end
   end
end

Griffith_large527101Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Griffith_large527101Battle_Terminate = function(ai, goal)
end

Griffith_large527101Battle_Interupt = function(ai, goal)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   if GuardBreak_Act(ai, goal, 7.8, 50) then
      if enemyDistance >= 3.5 then
         -- Drill.
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3017, TARGET_ENE_0, DIST_Middle, 0)
      else
         -- One-handed swing.
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   if UseItem_Act(ai, goal, 30, 50) then
      if enemyDistance >= 9.9 then
         -- Lightning spear.
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3011, TARGET_ENE_0, DIST_Middle, 0)
      else
         -- Scoop and thrust.
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3013, TARGET_ENE_0, DIST_Middle, 0)
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 20, TARGET_ENE_0, 11.3, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3014, TARGET_ENE_0, DIST_None, 0, -1)
      end
      return true
   end
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local shootInterrupt = Shoot_2dist(ai, goal, 5, 30, 0, 60)
   if shootInterrupt == 1 then
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, ai:GetRandam_Int(0, 1), ai:GetRandam_Int(30, 45), true, true, 9910)
      return true
   elseif shootInterrupt == 2 then
      if enemyDistance >= 9.9 then
         -- Lightning spear.
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3011, TARGET_ENE_0, DIST_Middle, 0)
      else
         -- Scoop and thrust.
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3013, TARGET_ENE_0, DIST_Middle, 0)
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 20, TARGET_ENE_0, 11.3, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3014, TARGET_ENE_0, DIST_None, 0, -1)
      end
      return true
   end
   return false
end


