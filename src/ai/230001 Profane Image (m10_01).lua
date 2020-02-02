--@package: m10_01_00_00.luabnd, 230001_battle.lua
--@battle_goal: 230001, HaikaiDemon230001

--[[ Moves:
   3000: Swipe right to left
   3001: (cont) Backhand swipe left to right
   3002: (cont) Thrust forward
   3003: Delayed swipe right to left
   3004: (cont) Spin pole and swipe left to right
   3005: (cont) Overhead smash
   3006: "Punch" hook with long wind-up
   3007: Jump smash
   3008: Jump smash with longer wind-up
   3009: Dark bead (curse)
   3300: Triple ground smash
   3301: Come out of triple ground smash
]]--

local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 3.8
local localScriptConfigVar2 = 0
local localScriptConfigVar3 = 4
local localScriptConfigVar4 = 0
local localScriptConfigVar5 = 8
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 7.5
local localScriptConfigVar8 = -1.3
local localScriptConfigVar9 = 0
local localScriptConfigVar10 = 6.5
local localScriptConfigVar11 = 8.7
local localScriptConfigVar12 = 11.8
local localScriptConfigVar13 = 13.5
local localScriptConfigVar14 = 5.5
local localScriptConfigVar15 = 25
HaikaiDemon230001Battle_Activate = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar1, TARGET_SELF, false, -1)
--[[
   local func1_var2 = ai:GetTeamOrder(ORDER_TYPE_Role)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local func1_var4 = ai:GetHpRate(TARGET_SELF)
   local func1_var6 = ai:GetRandam_Int(1, 100)
   local func1_var7 = ai:GetRandam_Int(1, 100)
   local func1_var8 = ai:GetRandam_Int(1, 100)
   local func1_var9 = 0
   local func1_var10 = 0
   local func1_var11 = 0
   local func1_var12 = 0
   local func1_var13 = 0
   local func1_var14 = 0
   local func1_var15 = 0
   local func1_var16 = 0
   local func1_var17 = 0
   local func1_var18 = 0
   local func1_var19 = 0
   local func1_var20 = 0
   local func1_var21 = 0
   local func1_var22 = 0
   local func1_var23 = 0
   local func1_var24 = 1
   local func1_var25 = 1
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 160) and enemyDistance <= 0.8 then
      -- Enemy is behind at close range.
      func1_var13 = 85
      func1_var14 = 15
   elseif enemyDistance >= 12.3 then
      -- Always shoots if enemy is far away.
      func1_var15 = 100
   elseif enemyDistance >= 7 then
      func1_var11 = 40
      func1_var12 = 5
      func1_var13 = 40
      func1_var15 = 15
   elseif enemyDistance >= 4 then
      func1_var10 = 55
      func1_var11 = 25
      func1_var12 = 20
   elseif enemyDistance >= 2.2 then
      func1_var10 = 70
      func1_var12 = 20
      func1_var14 = 10
   else
      func1_var10 = 55
      func1_var12 = 15
      func1_var14 = 30
   end

   local func1_var26 = ai:GetRandam_Int(1, func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 + func1_var15 + func1_var16)
   if func1_var26 <= func1_var10 then
      -- Act "10": 3000-3002 (standard)
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar1, TARGET_SELF, false, -1)
      if func1_var6 <= 10 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 70)
      elseif func1_var6 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 70)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 70)
         goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
      end
      func1_var9 = 100
   elseif func1_var26 <= func1_var10 + func1_var11 then
      -- Act "11": 3003-3005 (heavy standard)
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar5, TARGET_SELF, false, -1)
      if func1_var6 <= 10 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_Middle, 2, 70)
      elseif func1_var6 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_Middle, 2, 70)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_Middle, 2, 70)
         goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
      end
      func1_var9 = 100
   elseif func1_var26 <= func1_var10 + func1_var11 + func1_var12 then
      -- Act "12": 3006 (hook punch)
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar9, TARGET_SELF, false, -1)
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3006, TARGET_ENE_0, DIST_Middle, 0)
      func1_var9 = 100
   elseif func1_var26 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 then
      -- Act "13": 3007 or 3008 (jump attacks)
      if localScriptConfigVar12 <= enemyDistance and func1_var6 <= 40 and func1_var25 == 1 then
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar13, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3008, TARGET_ENE_0, DIST_Middle, 0)
         func1_var9 = 100
      else
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, localScriptConfigVar11, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3007, TARGET_ENE_0, DIST_Middle, 0)
         func1_var9 = 100
      end
   elseif func1_var26 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 then
      -- Act "14": Dodge backward
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0)
      func1_var9 = 0
   elseif func1_var26 <= func1_var10 + func1_var11 + func1_var12 + func1_var13 + func1_var14 + func1_var15 then
      -- Act "15": Shoot lightning spear
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
      func1_var9 = 0
   else
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, POINT_INITIAL, 1, TARGET_ENE_0, True, -1)
   end
   local func1_var27 = ai:GetRandam_Int(1, 100)
   if func1_var27 <= func1_var9 and func1_var24 == 1 then
      local func1_var28 = 0
      local func1_var29 = 70
      GetWellSpace_Act(ai, goal, func1_var28, func1_var29, 0, 0, 0, 0)
   end]]--
end

HaikaiDemon230001Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

HaikaiDemon230001Battle_Terminate = function(ai, goal)
end

HaikaiDemon230001Battle_Interupt = function(ai, goal)
   local func4_var6 = 3
   local func4_var7 = 15
   local func4_var8 = 100
   local func4_var9 = 0
   local func4_var10 = 0
   local func4_var11 = 6
   if Damaged_Step(ai, goal, func4_var6, func4_var7, func4_var8, func4_var9, func4_var10, func4_var11) then
      return true
   end
   local func4_var12 = 4.3
   local func4_var13 = 60
   local func4_var14 = 3000
   if GuardBreak_Attack(ai, goal, func4_var12, func4_var13, func4_var14) then
      return true
   end
   local func4_var15 = 9.5
   local func4_var16 = 15
   if UseItem_Act(ai, goal, func4_var15, func4_var16) then
      if func4_var5 >= 4.4 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3006, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local func4_var17 = 20
   local func4_var18 = 100
   local func4_var19 = 0
   local func4_var20 = 0
   local func4_var21 = 6
   if RebByOpGuard_Step(ai, goal, func4_var17, func4_var18, func4_var19, func4_var20, func4_var21) then
      return true
   end
   return false
end


