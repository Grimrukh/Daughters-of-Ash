--@package: m12_00_00_00.luabnd, 271101_battle.lua
--@battle_goal: 271101, CrystalAmber271101Battle

-- Boss version. Does not use 3004 (AoE), 3007, or 3008 (leaps). Only walks, except when punishing item use.

local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 1.8
local localScriptConfigVar2 = 0
local localScriptConfigVar3 = 2
local localScriptConfigVar4 = 0.5
local localScriptConfigVar5 = 2.5
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 5
local localScriptConfigVar8 = 0.5
local localScriptConfigVar9 = 2.6
local localScriptConfigVar10 = 0
local localScriptConfigVar11 = 5.1
local localScriptConfigVar12 = 4.5
local localScriptConfigVar13 = 8.3
local localScriptConfigVar14 = 7.5
local localScriptConfigVar15 = 11.5
CrystalAmber271101Battle_Activate = function(ai, goal)
--   local func1_var2 = {}
--   local func1_var3 = {}
--   local func1_var4 = {}
--   Common_Clear_Param(func1_var2, func1_var3, func1_var4)
   local oddsAct01 = 0
   local oddsAct02 = 0
   local oddsAct03 = 0
   local oddsAct04 = 0
   local oddsAct05 = 0
   local func1_var5 = ai:GetDist(TARGET_ENE_0)
   if func1_var5 >= 11.5 then
      oddsAct01 = 5    -- 3002
      oddsAct02 = 5    -- 3000, 3001
      oddsAct03 = 5    -- 3005
      oddsAct04 = 5    -- 3003
      oddsAct05 = 20   -- 3006
   elseif func1_var5 >= 8.3 then
      oddsAct01 = 5
      oddsAct02 = 5
      oddsAct03 = 5
      oddsAct04 = 5
      oddsAct05 = 30
   elseif func1_var5 >= 5.1 then
      oddsAct01 = 10
      oddsAct02 = 10
      oddsAct03 = 10
      oddsAct04 = 10
      oddsAct05 = 30
   else
      oddsAct01 = 20
      oddsAct02 = 20
      oddsAct03 = 20
      oddsAct04 = 20
      oddsAct05 = 0
   end

   CrystalAmber271101_Act01(ai, goal)

   local totalOdds = oddsAct01 + oddsAct02 + oddsAct03 + oddsAct04 + oddsAct05

   local randomRoll = ai:GetRandam_Int(1, totalOdds)

   if randomRoll <= oddsAct01 then
      CrystalAmber271101_Act01(ai, goal)
   elseif randomRoll <= oddsAct01 + oddsAct02 then
      local twoHitsOdds = ai:GetRandam_Int(0, 100)
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, 1.8, TARGET_ENE_0, true, -1)
      if twoHitsOdds <= 75 then
         goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2.5, 5)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 2.5, 5)
      else
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2.5, 5)
      end
      CrystalAmber271101_Act01(ai, goal)
   elseif randomRoll <= oddsAct01 + oddsAct02 + oddsAct03 then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, 2.5, TARGET_ENE_0, true, -1)
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3005, TARGET_ENE_0, DIST_Middle, 2.5, 5)
   elseif randomRoll <= oddsAct01 + oddsAct02 + oddsAct03 + oddsAct04 then
      CrystalAmber271101_Act04(ai, goal)
   else
      CrystalAmber271101_Act05(ai, goal)
   end

   local restRoll = ai:GetRandam_Int(0, 100)
   if restRoll <= 50 then
      CrystalAmber271101_ActAfter_AdjustSpace(ai, goal)
   end

end

CrystalAmber271101_Act01 = function(ai, goal, _)
   local func2_var5 = localScriptConfigVar3
   local func2_var6 = localScriptConfigVar3 + 2
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, func2_var5, TARGET_ENE_0, true, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_Middle, 2.5, 5)
end

CrystalAmber271101_Act04 = function(ai, goal, _)
   local func3_var5 = localScriptConfigVar5
   local func3_var6 = localScriptConfigVar5 + 2
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, func3_var5, TARGET_ENE_0, true, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_Middle, 2.5, 22)
end

CrystalAmber271101_Act05 = function(ai, goal, _)
   local func4_var5 = localScriptConfigVar11
   local func4_var6 = localScriptConfigVar11 + 2
goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, func4_var5, TARGET_ENE_0, true, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3006, TARGET_ENE_0, DIST_Middle, 2.5, 37)
end

CrystalAmber271101_ActAfter_AdjustSpace = function(ai, goal, _)
   local func7_var3 = ai:GetRandam_Int(0, 100)
   local func7_var4 = ai:GetRandam_Int(0, 1)
   local func7_var5 = ai:GetTeamRecordCount(COORDINATE_TYPE_SideWalk_L + func7_var4, TARGET_ENE_0, 2)
   if func7_var3 <= 60 then
   elseif func7_var3 <= 65 and func7_var5 < 2 then
      goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 2.5, TARGET_ENE_0, 2, TARGET_ENE_0, true, -1)
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, func7_var4, ai:GetRandam_Int(30, 45), true, true, -1)
   elseif func7_var3 <= 70 then
      goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 2.5, TARGET_ENE_0, 3, TARGET_ENE_0, true, -1)
   elseif func7_var3 <= 85 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 4)
   else
      local func7_var6 = ai:GetRandam_Int(1, 100)
      if func7_var6 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 4)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 4)
      end
   end
end

CrystalAmber271101Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

CrystalAmber271101Battle_Terminate = function(ai, goal)
end

CrystalAmber271101Battle_Interupt = function(ai, goal)
   local func10_var5 = ai:GetDist(TARGET_ENE_0)
   local func10_var6 = 2
   local func10_var7 = 30
   if GuardBreak_Act(ai, goal, func10_var6, func10_var7) then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
      return true
   end
   local func10_var8 = 8
   local func10_var9 = 25
   if UseItem_Act(ai, goal, func10_var8, func10_var9) then
      if func10_var5 <= 4.4 then
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar3, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar13, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   return false
end
