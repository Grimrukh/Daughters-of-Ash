--@package: m14_01_00_00.luabnd, 282000_battle.lua
--@battle_goal: 282000, Claw_Hollow282000Battle

local localScriptConfigVar1 = 3.2
local localScriptConfigVar3 = 7.5
local localScriptConfigVar7 = 1.8

--[[ Moves:

3000: Punch, right hand
3001: (cont) backhand
3002: (cont) big punch forward
3003: heavy punch, claw lower
3004: heavy punch, claw higher
3005: (cont) left hand punch
3006: leaping punch
3007: quicker leaping punch
3008: long distance leaping punch
3009: double claw thrust

Actions:

1: 3000, plus 3001, plus 3002
2: 3003, plus 3005
3: 3004, plus 3006
4: 3006 or 3007 or 3008 (depending on distance)
5: 3009 (close range)


--]]

Claw_Hollow282000Battle_Activate = function(ai, goal)
   local func1_var2 = {}
   local func1_var3 = {}
   local func1_var4 = {}
   Common_Clear_Param(func1_var2, func1_var3, func1_var4)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   if enemyDistance >= 8 then
      -- Likely to use a leap attack
      func1_var2[1] = 10
      func1_var2[2] = 5
      func1_var2[3] = 5
      func1_var2[4] = 5
      func1_var2[5] = 75
   elseif enemyDistance >= 4 then
      -- Likely to use any attack
      func1_var2[1] = 20
      func1_var2[2] = 20
      func1_var2[3] = 15
      func1_var2[4] = 15
      func1_var2[5] = 30
   else
      -- Likely to use a combo attack
      func1_var2[1] = 30
      func1_var2[2] = 20
      func1_var2[3] = 20
      func1_var2[4] = 30
      func1_var2[5] = 0
   end
   func1_var3[1] = REGIST_FUNC(ai, goal, Claw_Hollow282000_Act01)
   func1_var3[2] = REGIST_FUNC(ai, goal, Claw_Hollow282000_Act02)
   func1_var3[3] = REGIST_FUNC(ai, goal, Claw_Hollow282000_Act03)
   func1_var3[4] = REGIST_FUNC(ai, goal, Claw_Hollow282000_Act04)
   func1_var3[5] = REGIST_FUNC(ai, goal, Claw_Hollow282000_Act05)
   func1_var6 = {0, 70, 5, 5, 5, 15}
   local func1_var7 = REGIST_FUNC(ai, goal, HumanCommon_ActAfter_AdjustSpace, func1_var6)
   Common_Battle_Activate(ai, goal, func1_var2, func1_var3, func1_var7, func1_var4)
end

Claw_Hollow282000_Act01 = function(ai, goal, _)
   local random = ai:GetRandam_Int(1, 100)
   local func2_var5 = localScriptConfigVar1
   local func2_var6 = localScriptConfigVar1 + 2
   local func2_var7 = 0
   Approach_Act(ai, goal, func2_var5, func2_var6, func2_var7)
   if random <= 10 then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
   elseif random <= 30 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
   elseif random <= 80 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
   end
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

Claw_Hollow282000_Act02 = function(ai, goal, _)
   local random = ai:GetRandam_Int(1, 100)
   local func2_var5 = localScriptConfigVar1
   local func2_var6 = localScriptConfigVar1 + 2
   local func2_var7 = 0
   Approach_Act(ai, goal, func2_var5, func2_var6, func2_var7)
   if random <= 50 then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Claw_Hollow282000_Act03 = function(ai, goal, _)
   local random = ai:GetRandam_Int(1, 100)
   local func2_var5 = localScriptConfigVar1
   local func2_var6 = localScriptConfigVar1 + 2
   local func2_var7 = 0
   Approach_Act(ai, goal, func2_var5, func2_var6, func2_var7)
   if random <= 30 then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Claw_Hollow282000_Act04 = function(ai, goal, _)
   local random = ai:GetRandam_Int(1, 100)
   local func2_var5 = localScriptConfigVar1
   local func2_var6 = localScriptConfigVar1 + 2
   local func2_var7 = 0
   Approach_Act(ai, goal, func2_var5, func2_var6, func2_var7)
   if random <= 30 then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0)
   end
end

Claw_Hollow282000_Act05 = function(ai, goal, _)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local random = ai:GetRandam_Int(1, 100)
   local func3_var5 = localScriptConfigVar7
   local func3_var6 = localScriptConfigVar7 + 2
   if enemyDistance <= 6 then
      if random <= 50 then
         Approach_and_Attack_Act(ai, goal, func3_var5, func3_var6, 0, 3006, DIST_Middle)
      else
         Approach_and_Attack_Act(ai, goal, func3_var5, func3_var6, 0, 3007, DIST_Middle)
      end
   else
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3008, TARGET_ENE_0, DIST_Middle, 0)
   end
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

Claw_Hollow282000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Claw_Hollow282000Battle_Terminate = function(ai, goal)
end

Claw_Hollow282000Battle_Interupt = function(ai, goal)
   local func6_var6 = 3
   local func6_var7 = 15
   local func6_var8 = 100
   local func6_var9 = 0
   local func6_var10 = 0
   local func6_var11 = 3
   if Damaged_Step(ai, goal, func6_var6, func6_var7, func6_var8, func6_var9, func6_var10, func6_var11) then
      return true
   end
   local func6_var12 = 2.6
   local func6_var13 = 50
   local func6_var14 = ai:GetRandam_Int(1, 100)
   if GuardBreak_Act(ai, goal, func6_var12, func6_var13) then
      if func6_var14 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local func6_var15 = 9.5
   local func6_var16 = 15
   local func6_var17 = ai:GetDist(TARGET_ENE_0)
   if UseItem_Act(ai, goal, func6_var15, func6_var16) then
      if func6_var17 >= 5.5 then
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar3, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar1, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local func6_var18 = 5.5
   local func6_var19 = 18
   local func6_var20 = 20
   local func6_var21 = 30
   local func6_var22 = ai:GetRandam_Int(1, 100)
   local func6_var23 = ai:GetRandam_Int(1, 100)
   local func6_var24 = Shoot_2dist(ai, goal, func6_var18, func6_var19, func6_var20, func6_var21)
   if func6_var24 == 1 then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar1, TARGET_SELF, false, -1)
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      return true
   elseif func6_var24 == 2 then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar3, TARGET_SELF, false, -1)
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
      return true
   end
   local func6_var25 = 20
   local func6_var26 = 100
   local func6_var27 = 0
   local func6_var28 = 0
   local func6_var29 = 4
   if RebByOpGuard_Step(ai, goal, func6_var25, func6_var26, func6_var27, func6_var28, func6_var29) then
      return true
   end
   return false
end
