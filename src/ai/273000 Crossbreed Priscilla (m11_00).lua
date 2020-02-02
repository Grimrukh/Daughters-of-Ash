--@package: m11_00_00_00.luabnd, 273000_battle.lua
--@battle_goal: 273000, Heroine273000Battle

-- 3000: Two-handed slash, right to left.
-- 3001: (Combo) two-handed slash, left to right.
-- 3002: Underhanded slash, right to left.
-- 3003: (Combo) underhanded slash, left to right.
-- 3004: Ice breath, straight ahead.
-- 3005: Ice breath, sweep.
-- 3006: Fast slash, right to left.
-- 3007: Turn invisible.
-- 9000: Sitting down, head on knees, turned to the right.
-- 9060: Gets up from 9000.


local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 3.1
local localScriptConfigVar2 = 0
local localScriptConfigVar3 = 1.3
local localScriptConfigVar4 = 0
local localScriptConfigVar5 = 3.9
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 1.8
local localScriptConfigVar8 = 4.7
local localScriptConfigVar9 = 5.7
local localScriptConfigVar10 = 4.3
local localScriptConfigVar11 = 5.3
local localScriptConfigVar12 = -0.2
local localScriptConfigVar13 = 0.8
Heroine273000Battle_Activate = function(ai, goal)
   local oddsTable = {}
   local actionTable = {}
   local simpleActionTable = {}
   Common_Clear_Param(oddsTable, actionTable, simpleActionTable)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local enemyVerticalDistance = ai:GetDistYSigned(TARGET_ENE_0)
   local hpRate = ai:GetHpRate(TARGET_SELF)
   local hasTurnedInvisibleOnce = ai:GetNumber(0)
   ai:AddObserveRegion(2, TARGET_ENE_0, 1102700)
   ai:AddObserveRegion(3, TARGET_ENE_0, 1102701)
   ai:AddObserveRegion(4, TARGET_ENE_0, 1102702)
   ai:AddObserveRegion(5, TARGET_ENE_0, 1102703)
   ai:AddObserveRegion(6, TARGET_ENE_0, 1102704)
   ai:AddObserveRegion(7, TARGET_ENE_0, 1102705)
   ai:AddObserveRegion(8, TARGET_ENE_0, 1102706)
   ai:AddObserveRegion(9, TARGET_ENE_0, 1102707)
   ai:AddObserveRegion(10, TARGET_ENE_0, 1102708)
   local canTurnInvisible = 0
   if ai:IsFinishTimer(0) == true then
      canTurnInvisible = 1
   end
   local invisibleMultiplier = 1
   if hpRate <= 0.5 then
      invisibleMultiplier = 2
   end
   if hasTurnedInvisibleOnce == 0 then
      oddsTable[7] = 100
   elseif enemyVerticalDistance < -2 then
      oddsTable[8] = 100
   elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1102700) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1102701) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1102702) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1102703) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1102704) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1102705) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1102706) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1102707) or ai:IsInsideTargetRegion(TARGET_ENE_0, 1102708) then
      oddsTable[8] = 100
   elseif ai:HasSpecialEffectId(TARGET_SELF, 5162) then
      if enemyDistance >= 3.6 then
         if hpRate <= 0.5 then
            oddsTable[1] = 20
            oddsTable[2] = 30
            oddsTable[3] = 20
            oddsTable[4] = 0
            oddsTable[5] = 30
            oddsTable[6] = 0
         else
            oddsTable[1] = 0
            oddsTable[2] = 50
            oddsTable[3] = 0
            oddsTable[4] = 0
            oddsTable[5] = 50
            oddsTable[6] = 0
         end
      elseif enemyDistance >= 0.8 then
         if hpRate <= 0.5 then
            oddsTable[1] = 15
            oddsTable[2] = 20
            oddsTable[3] = 15
            oddsTable[4] = 30
            oddsTable[5] = 20
            oddsTable[6] = 0
         else
            oddsTable[1] = 0
            oddsTable[2] = 30
            oddsTable[3] = 0
            oddsTable[4] = 40
            oddsTable[5] = 30
            oddsTable[6] = 0
         end
      else
         if hpRate <= 0.5 then
            oddsTable[1] = 0
            oddsTable[2] = 25
            oddsTable[3] = 0
            oddsTable[4] = 25
            oddsTable[5] = 25
            oddsTable[6] = 25
         else
            oddsTable[1] = 0
            oddsTable[2] = 0
            oddsTable[3] = 0
            oddsTable[4] = 35
            oddsTable[5] = 0
            oddsTable[6] = 65
         end
      end
   elseif enemyDistance >= 4.4 then
      oddsTable[1] = 30
      oddsTable[2] = 20
      oddsTable[3] = 30
      oddsTable[4] = 0
      oddsTable[5] = 20
      oddsTable[6] = 0
   elseif enemyDistance >= 4 then
      oddsTable[1] = 10
      oddsTable[2] = 25
      oddsTable[3] = 40
      oddsTable[4] = 0
      oddsTable[5] = 25
      oddsTable[6] = 0
   elseif enemyDistance >= 3.6 then
      oddsTable[1] = 10
      oddsTable[2] = 30
      oddsTable[3] = 10
      oddsTable[4] = 0
      oddsTable[5] = 30
      oddsTable[6] = 0
      oddsTable[7] = 20 * canTurnInvisible * invisibleMultiplier
   elseif enemyDistance >= 0.8 then
      oddsTable[1] = 5
      oddsTable[2] = 35
      oddsTable[3] = 5
      oddsTable[4] = 0
      oddsTable[5] = 35
      oddsTable[6] = 0
      oddsTable[7] = 15 * canTurnInvisible * invisibleMultiplier
   else
      oddsTable[1] = 5
      oddsTable[2] = 25
      oddsTable[3] = 5
      oddsTable[4] = 0
      oddsTable[5] = 30
      oddsTable[6] = 25
      oddsTable[7] = 15 * canTurnInvisible * invisibleMultiplier
   end
   actionTable[1] = REGIST_FUNC(ai, goal, Heroine273000_Act01)  -- Ice breath, straight ahead.
   actionTable[2] = REGIST_FUNC(ai, goal, Heroine273000_Act02)  -- One or two hit combo, high up.
   actionTable[3] = REGIST_FUNC(ai, goal, Heroine273000_Act03)  -- Ice breath, sweep right to left.
   actionTable[4] = REGIST_FUNC(ai, goal, Heroine273000_Act04)  -- Retreat.
   actionTable[5] = REGIST_FUNC(ai, goal, Heroine273000_Act05)  -- One or two hit combo, low down.
   actionTable[6] = REGIST_FUNC(ai, goal, Heroine273000_Act06)  -- Single fast slash.
   actionTable[7] = REGIST_FUNC(ai, goal, Heroine273000_Act07)  -- Turn invisible.
   actionTable[8] = REGIST_FUNC(ai, goal, Heroine273000_Act08)  -- Move to a certain point.
   local func1_var11 = {0, 70, 0, 30, 0, 0}
   local actAfterAction = REGIST_FUNC(ai, goal, HumanCommon_ActAfter_AdjustSpace, func1_var11)
   Common_Battle_Activate(ai, goal, oddsTable, actionTable, actAfterAction, simpleActionTable)
end

Heroine273000_Act01 = function(ai, goal, func2_param2)
   local func2_var4 = localScriptConfigVar9 + 100
   local func2_var5 = localScriptConfigVar9
   local func2_var6 = 0
   Approach_Act(ai, goal, func2_var5, func2_var4, func2_var6)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3004, TARGET_ENE_0, DIST_Middle, 3, 30)
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      GetWellSpace_Odds = 25
   else
      GetWellSpace_Odds = 75
   end
   return GetWellSpace_Odds
end

Heroine273000_Act02 = function(ai, goal, func3_param2)
   local func3_var4 = localScriptConfigVar1 + 100
   local func3_var5 = localScriptConfigVar1
   local func3_var6 = 0
   local func3_var7 = ai:GetRandam_Int(30, 60)
   Approach_Act(ai, goal, func3_var5, func3_var4, func3_var6)
   if func3_var7 <= 20 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 15, 3000, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 15, 3000, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 15, 3001, TARGET_ENE_0, DIST_Middle, 0)
   end
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      GetWellSpace_Odds = 25
   else
      GetWellSpace_Odds = 75
   end
   return GetWellSpace_Odds
end

Heroine273000_Act03 = function(ai, goal, func4_param2)
   local func4_var4 = localScriptConfigVar11 + 100
   local func4_var5 = localScriptConfigVar11
   local func4_var6 = 0
   Approach_Act(ai, goal, func4_var5, func4_var4, func4_var6)
   goal:AddSubGoal(GOAL_COMMON_Attack, 15, 3005, TARGET_ENE_0, DIST_Middle, 0)
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      GetWellSpace_Odds = 25
   else
      GetWellSpace_Odds = 75
   end
   return GetWellSpace_Odds
end

Heroine273000_Act04 = function(ai, goal, func5_param2)
   local func5_var4 = localScriptConfigVar11 + 0
   local func5_var5 = localScriptConfigVar11
   local func5_var6 = 0
   Approach_Act(ai, goal, func5_var5, func5_var4, func5_var6)
   goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 4, TARGET_ENE_0, 3.6, TARGET_ENE_0, true, -1)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

Heroine273000_Act05 = function(ai, goal, func6_param2)
   local func6_var4 = localScriptConfigVar5 + 100
   local func6_var5 = localScriptConfigVar5
   local func6_var6 = 0
   local func6_var7 = ai:GetRandam_Int(30, 60)
   Approach_Act(ai, goal, func6_var5, func6_var4, func6_var6)
   if func6_var7 <= 30 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 15, 3002, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 15, 3002, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 15, 3003, TARGET_ENE_0, DIST_Near, 0)
   end
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      GetWellSpace_Odds = 25
   else
      GetWellSpace_Odds = 75
   end
   return GetWellSpace_Odds
end

Heroine273000_Act06 = function(ai, goal, func7_param2)
   local func7_var4 = localScriptConfigVar13 + 100
   local func7_var5 = localScriptConfigVar13
   local func7_var6 = 0
   Approach_Act(ai, goal, func7_var5, func7_var4, func7_var6)
   goal:AddSubGoal(GOAL_COMMON_Attack, 15, 3006, TARGET_ENE_0, DIST_Middle, 0)
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      GetWellSpace_Odds = 25
   else
      GetWellSpace_Odds = 75
   end
   return GetWellSpace_Odds
end

Heroine273000_Act07 = function(ai, goal, func8_param2)
   local func8_var3 = ai:GetNumber(0)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 15, 3007, TARGET_ENE_0, DIST_Middle, 0, -1)
   ai:SetNumber(0, 1)  -- has turned invisible once.
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      GetWellSpace_Odds = 25
      ai:SetTimer(0, 40)  -- timer before she can turn invisible again; shorter below 50% health.
   else
      GetWellSpace_Odds = 75
      ai:SetTimer(0, 60)
   end
   return GetWellSpace_Odds
end

Heroine273000_Act08 = function(ai, goal, func9_param2)
   if ai:IsInsideTargetRegion(TARGET_SELF, 1102760) then
      ai:SetEventMoveTarget(1102750)
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 4, POINT_EVENT, 0, TARGET_ENE_0, True, -1)
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_ENE_0)
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1102761) then
      ai:SetEventMoveTarget(1102751)
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 4, POINT_EVENT, 0, TARGET_ENE_0, True, -1)
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_ENE_0)
   else
      ai:SetEventMoveTarget(1102752)
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 4, POINT_EVENT, 0, TARGET_ENE_0, True, -1)
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_ENE_0)
   end
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

Heroine273000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Heroine273000Battle_Terminate = function(ai, goal)
end

Heroine273000Battle_Interupt = function(ai, goal)
   local func12_var2 = ai:GetRandam_Int(1, 100)
   local func12_var3 = ai:GetNumber(0)
   if ai:IsInterupt(INTERUPT_Inside_ObserveArea) and ai:IsFinishTimer(2) == true then
      if ai:IsInsideTargetRegion(TARGET_SELF, 1102760) then
         goal:ClearSubGoal()
         ai:SetTimer(2, 1)
         ai:SetEventMoveTarget(1102750)
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 4, POINT_EVENT, 0, TARGET_ENE_0, True, -1)
         goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_ENE_0)
         return true
      elseif ai:IsInsideTargetRegion(TARGET_SELF, 1102761) then
         goal:ClearSubGoal()
         ai:SetTimer(2, 1)
         ai:SetEventMoveTarget(1102751)
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 4, POINT_EVENT, 0, TARGET_ENE_0, True, -1)
         goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_ENE_0)
         return true
      else
         goal:ClearSubGoal()
         ai:SetTimer(2, 1)
         ai:SetEventMoveTarget(1102752)
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 4, POINT_EVENT, 0, TARGET_ENE_0, True, -1)
         goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_ENE_0)
         return true
      end
   end
   if ai:IsInterupt(INTERUPT_Damaged) and ai:IsFinishTimer(0) == true then
      if func12_var2 <= 10 and not ai:HasSpecialEffectId(TARGET_SELF, 5162) then
         goal:AddSubGoal(GOAL_COMMON_Attack, 15, 3007, TARGET_ENE_0, DIST_Middle, 0)
         return true
      end
   end
   local func12_var4 = 3.6
   local func12_var5 = 40
   local func12_var6 = ai:GetDist(TARGET_ENE_0)
   if GuardBreak_Act(ai, goal, func12_var4, func12_var5) then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
   end
   local func12_var7 = 3.6
   local func12_var8 = 15
   local func12_var9 = ai:GetDist(TARGET_ENE_0)
   if UseItem_Act(ai, goal, func12_var7, func12_var8) then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
   end
   return false
end