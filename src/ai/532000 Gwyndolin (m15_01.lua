--@package: m15_01_00_00.luabnd, 532000_battle.lua
--@battle_goal: 532000, ImperialMother532000Battle

-- 3000: Rise up and shoot arrows
-- 3001: Shoot arrows and go down
-- 3002: Teleport. Only triggered by damage or proximity (in ObserveArea).
-- 3003: Cluster of sorcery
-- 3004: Awkward hand movements
-- 3005: More awkward hand movements
-- 3006: Throws big piercing spell

ImperialMother532000Battle_Activate = function(ai, goal)
   local oddsTable = {}
   local func1_var3 = {}
   local func1_var4 = {}
   Common_Clear_Param(oddsTable, func1_var3, func1_var4)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local func1_var6 = ai:GetEventRequest()
   ai:AddObserveArea(0, TARGET_SELF, TARGET_ENE_0, AI_DIR_TYPE_F, 360, 15)
   local initialTeleportDone = ai:GetNumber(0)
   local func1_var8 = 1
   if func1_var6 == 1 then
      func1_var8 = 0
   end
   if initialTeleportDone == 0 then
      oddsTable[6] = 100
   elseif ai:HasSpecialEffectId(TARGET_SELF, 5400) then
      if enemyDistance >= 75 then
         oddsTable[5] = 100
      elseif enemyDistance >= 25 then
         oddsTable[1] = 30
         oddsTable[2] = 35
         oddsTable[3] = 35
         oddsTable[4] = 0 * func1_var8
         oddsTable[5] = 0
      elseif enemyDistance >= 12 then
         oddsTable[1] = 40
         oddsTable[2] = 35
         oddsTable[3] = 25
         oddsTable[4] = 0 * func1_var8
         oddsTable[5] = 0
      elseif enemyDistance >= 6 then
         oddsTable[1] = 30
         oddsTable[2] = 40
         oddsTable[3] = 30
         oddsTable[4] = 0 * func1_var8
         oddsTable[5] = 0
      else
         oddsTable[1] = 5
         oddsTable[2] = 35
         oddsTable[3] = 60
         oddsTable[4] = 0 * func1_var8
         oddsTable[5] = 0
      end
   elseif enemyDistance >= 75 then
      oddsTable[5] = 100
   elseif enemyDistance >= 25 then
      oddsTable[1] = 20
      oddsTable[2] = 35
      oddsTable[3] = 35
      oddsTable[4] = 0 * func1_var8
      oddsTable[5] = 0
   elseif enemyDistance >= 12 then
      oddsTable[1] = 35
      oddsTable[2] = 45
      oddsTable[3] = 20
      oddsTable[4] = 0 * func1_var8
      oddsTable[5] = 0
   elseif enemyDistance >= 6 then
      oddsTable[1] = 15
      oddsTable[2] = 55
      oddsTable[3] = 30
      oddsTable[4] = 0 * func1_var8
      oddsTable[5] = 0
   else
      oddsTable[1] = 0
      oddsTable[2] = 40
      oddsTable[3] = 60
      oddsTable[4] = 0 * func1_var8
      oddsTable[5] = 0
   end
   func1_var3[1] = REGIST_FUNC(ai, goal, ImperialMother532000_Act01)  -- Shoot arrows
   func1_var3[2] = REGIST_FUNC(ai, goal, ImperialMother532000_Act02)  -- Shoot spells
   func1_var3[3] = REGIST_FUNC(ai, goal, ImperialMother532000_Act03)  -- Shoot piercing blast
   func1_var3[4] = REGIST_FUNC(ai, goal, ImperialMother532000_Act04)  -- Teleport (unused)
   func1_var3[5] = REGIST_FUNC(ai, goal, ImperialMother532000_Act05)  -- Wait between 1 and 2 seconds
   func1_var3[6] = REGIST_FUNC(ai, goal, ImperialMother532000_Act06)  -- Teleport
   local func1_var9 = {0, 70, 0, 0, 30, 0, 0}
   local func1_var10 = REGIST_FUNC(ai, goal, HumanCommon_ActAfter_AdjustSpace_IncludeSidestep, func1_var9)
   Common_Battle_Activate(ai, goal, oddsTable, func1_var3, func1_var10, func1_var4)
end

ImperialMother532000_Act01 = function(ai, goal)
   if ai:HasSpecialEffectId(TARGET_SELF, 5401) then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3005, TARGET_ENE_0, DIST_None, 0)
   end
   local func2_var2 = 3000
   local func2_var3 = 3001
   local numberShots = ai:GetRandam_Int(1, 4)
   Shoot_Act(ai, goal, func2_var2, func2_var3, numberShots)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

ImperialMother532000_Act02 = function(ai, goal)
   if ai:HasSpecialEffectId(TARGET_SELF, 5400) then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3004, TARGET_ENE_0, DIST_None, 0)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_None, 1.5, 20)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

ImperialMother532000_Act03 = function(ai, goal)
   if ai:HasSpecialEffectId(TARGET_SELF, 5400) then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3004, TARGET_ENE_0, DIST_None, 0)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3006, TARGET_ENE_0, DIST_None, 1.5, 20)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

ImperialMother532000_Act04 = function(ai, goal)
   if ai:HasSpecialEffectId(TARGET_SELF, 5400) then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3004, TARGET_ENE_0, DIST_None, 0)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_None, 0, -1)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

ImperialMother532000_Act05 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_Wait, ai:GetRandam_Float(1, 2), TARGET_ENE_0, 0, 0, 0)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

ImperialMother532000_Act06 = function(ai, goal)
   ai:SetNumber(0, 1)
   if ai:HasSpecialEffectId(TARGET_SELF, 5400) then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3004, TARGET_ENE_0, DIST_None, 0)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_None, 0, -1)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

ImperialMother532000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

ImperialMother532000Battle_Terminate = function(ai, goal)
end

ImperialMother532000Battle_Interupt = function(ai, goal)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local func10_var6 = ai:GetEventRequest()
   if ai:IsInterupt(INTERUPT_Damaged) and enemyDistance <= 3 and func10_var6 ~= 1 then
      goal:ClearSubGoal()
      if ai:HasSpecialEffectId(TARGET_SELF, 5400) then
         goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3004, TARGET_ENE_0, DIST_None, 0)
      end
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_None, 0, -1)
      return true
   end
   if ai:IsInterupt(INTERUPT_Inside_ObserveArea) and func10_var6 ~= 1 then
      goal:ClearSubGoal()
      if ai:HasSpecialEffectId(TARGET_SELF, 5400) then
         goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3004, TARGET_ENE_0, DIST_None, 0)
      end
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_None, 0, -1)
      return true
   end
   return false
end


