--@package: m14_00_00_00.luabnd, 224001_battle.lua
--@battle_goal: 224001, Nata224001Battle


local l_0_0 = 0
local l_0_1 = 3.5
local l_0_2 = 0
local l_0_3 = 3.5
local l_0_4 = 0
local l_0_5 = 3.5
local l_0_6 = 0
local l_0_7 = 3.5
local l_0_8 = 4
local l_0_9 = 6.5
local l_0_10 = 2
local l_0_11 = 3
Nata224001Battle_Activate = function(l_1_arg0, l_1_arg1)
   local l_1_2 = {}
   local l_1_3 = {}
   local l_1_4 = {}
   Common_Clear_Param(l_1_2, l_1_3, l_1_4)
   local l_1_5 = l_1_arg0:GetDist(TARGET_ENE_0)
   if l_1_5 >= 8 then
      l_1_2[1] = 0
      l_1_2[2] = 10
      l_1_2[3] = 0
      l_1_2[4] = 10
      l_1_2[7] = 80
      l_1_2[8] = 0
   elseif l_1_5 >= 4 then
      l_1_2[1] = 15
      l_1_2[2] = 25
      l_1_2[3] = 15
      l_1_2[4] = 25
      l_1_2[7] = 20
      l_1_2[8] = 0
   elseif l_1_5 >= 2 then
      l_1_2[1] = 20
      l_1_2[2] = 30
      l_1_2[3] = 20
      l_1_2[4] = 30
      l_1_2[7] = 0
      l_1_2[8] = 0
   else
      l_1_2[1] = 15
      l_1_2[2] = 20
      l_1_2[3] = 15
      l_1_2[4] = 20
      l_1_2[7] = 0
      l_1_2[8] = 30
   end
   l_1_3[1] = REGIST_FUNC(l_1_arg0, l_1_arg1, Nata224001_Act01)
   l_1_3[2] = REGIST_FUNC(l_1_arg0, l_1_arg1, Nata224001_Act02)
   l_1_4[3] = {l_0_5, 0, 3002, DIST_Middle}
   l_1_3[4] = REGIST_FUNC(l_1_arg0, l_1_arg1, Nata224001_Act04)
   l_1_3[7] = REGIST_FUNC(l_1_arg0, l_1_arg1, Nata224001_Act07)
   l_1_3[8] = REGIST_FUNC(l_1_arg0, l_1_arg1, Nata224001_Act08)
   local l_1_6 = REGIST_FUNC(l_1_arg0, l_1_arg1, Nata224001_ActAfter_AdjustSpace)
   Common_Battle_Activate(l_1_arg0, l_1_arg1, l_1_2, l_1_3, l_1_6, l_1_4)
end

Nata224001_Act01 = function(l_2_arg0, l_2_arg1, l_2_arg2)
   local l_2_3 = l_2_arg0:GetDist(TARGET_ENE_0)
   local l_2_4 = l_2_arg0:GetRandam_Int(1, 100)
   local l_2_5 = l_0_1
   local l_2_6 = l_0_1 + 2
   local l_2_7 = 0
   Approach_Act(l_2_arg0, l_2_arg1, l_2_5, l_2_6, l_2_7)
   if l_2_4 <= 20 then
      l_2_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
   else
      l_2_arg1:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      l_2_arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
   end
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

Nata224001_Act02 = function(l_3_arg0, l_3_arg1, l_3_arg2)
   local l_3_3 = l_3_arg0:GetDist(TARGET_ENE_0)
   local l_3_4 = l_3_arg0:GetRandam_Int(1, 100)
   local l_3_5 = l_0_11
   local l_3_6 = l_0_11 + 2
   local l_3_7 = 0
   local l_3_8 = 3005
   local l_3_9 = DIST_Middle
   Approach_and_Attack_Act(l_3_arg0, l_3_arg1, l_3_5, l_3_6, l_3_7, l_3_8, l_3_9)
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

Nata224001_Act04 = function(l_4_arg0, l_4_arg1, l_4_arg2)
   local l_4_3 = l_4_arg0:GetDist(TARGET_ENE_0)
   local l_4_4 = l_4_arg0:GetRandam_Int(1, 100)
   local l_4_5 = l_0_7
   local l_4_6 = l_0_7 + 2
   local l_4_7 = 0
   Approach_Act(l_4_arg0, l_4_arg1, l_4_5, l_4_6, l_4_7)
   if l_4_4 <= 20 then
      l_4_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
   else
      l_4_arg1:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
      l_4_arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
   end
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

Nata224001_Act07 = function(l_5_arg0, l_5_arg1, l_5_arg2)
   local l_5_3 = l_5_arg0:GetDist(TARGET_ENE_0)
   local l_5_4 = l_5_arg0:GetRandam_Int(1, 100)
   local l_5_5 = l_0_9
   local l_5_6 = l_0_9 + 2
   local l_5_7 = 0
   local l_5_8 = 3004
   local l_5_9 = DIST_Middle
   Approach_and_Attack_Act(l_5_arg0, l_5_arg1, l_5_5, l_5_6, l_5_7, l_5_8, l_5_9)
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

Nata224001_Act08 = function(l_6_arg0, l_6_arg1, l_6_arg2)
   local l_6_3 = l_6_arg0:GetDist(TARGET_ENE_0)
   local l_6_4 = l_6_arg0:GetRandam_Int(1, 100)
   l_6_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, -1, AI_DIR_TYPE_B, 4)
   l_6_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

Nata224001_ActAfter_AdjustSpace = function(l_7_arg0, l_7_arg1, l_7_arg2)
   local l_7_3 = l_7_arg0:GetDist(TARGET_ENE_0)
   local l_7_4 = l_7_arg0:GetRandam_Int(1, 100)
   local l_7_5 = l_7_arg0:GetRandam_Int(1, 100)
   if l_7_4 <= 80 then
   elseif l_7_4 <= 90 then
      l_7_arg1:AddSubGoal(GOAL_COMMON_SidewayMove, 2.5, TARGET_ENE_0, l_7_arg0:GetRandam_Int(0, 1), l_7_arg0:GetRandam_Int(15, 30), true, true, -1)
   elseif l_7_5 <= 50 then
      l_7_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 4)
   else
      l_7_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 4)
   end
end

Nata224001Battle_Update = function(l_8_arg0, l_8_arg1)
   return GOAL_RESULT_Continue
end

Nata224001Battle_Terminate = function(l_9_arg0, l_9_arg1)
end

Nata224001Battle_Interupt = function(l_10_arg0, l_10_arg1)
   local l_10_2 = l_10_arg0:GetDist(TARGET_ENE_0)
   local l_10_3 = l_10_arg0:GetRandam_Int(1, 100)
   local l_10_4 = l_10_arg0:GetRandam_Int(1, 100)
   local l_10_5 = 3
   local l_10_6 = 15
   local l_10_7 = 60
   local l_10_8 = 20
   local l_10_9 = 20
   if FindAttack_Step(l_10_arg0, l_10_arg1, l_10_5, l_10_6, l_10_7, l_10_8, l_10_9) then
      return true
   end
   local l_10_10 = 3
   local l_10_11 = 15
   local l_10_12 = 60
   local l_10_13 = 20
   local l_10_14 = 20
   local l_10_15 = 3.5
   if Damaged_Step(l_10_arg0, l_10_arg1, l_10_10, l_10_11, l_10_12, l_10_13, l_10_14, l_10_15) then
      return true
   end
   local l_10_16 = 8
   local l_10_17 = 30
   if GuardBreak_Act(l_10_arg0, l_10_arg1, l_10_16, l_10_17) then
      if l_10_2 <= 3.5 then
         if l_10_3 <= 50 then
            l_10_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
         else
            l_10_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
         end
         return true
      else
         l_10_arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, l_0_9, TARGET_SELF, false, -1)
         l_10_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local l_10_18 = 6.5
   local l_10_19 = 30
   local l_10_20 = 3003
   if MissSwing_Attack(l_10_arg0, l_10_arg1, l_10_18, l_10_19, l_10_20) then
      if l_10_2 <= 3.5 then
         l_10_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
      else
         l_10_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local l_10_21 = 9
   local l_10_22 = 60
   if UseItem_Act(l_10_arg0, l_10_arg1, l_10_21, l_10_22) then
      if l_10_2 <= 3.5 then
         l_10_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
      else
         l_10_arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, l_0_9, TARGET_SELF, false, -1)
         l_10_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local l_10_23 = 12
   local l_10_24 = 20
   local l_10_25 = 0
   local l_10_26 = 30
   local l_10_27 = Shoot_2dist(l_10_arg0, l_10_arg1, l_10_23, l_10_24, l_10_25, l_10_26)
   if l_10_27 == 1 then
      l_10_arg1:AddSubGoal(GOAL_COMMON_Attack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
   elseif l_10_27 == 2 then
      if l_10_3 <= 50 then
         l_10_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 4)
      else
         l_10_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 4)
      end
      return true
   end
   local l_10_28 = 50
   local l_10_29 = 60
   local l_10_30 = 20
   local l_10_31 = 20
   local l_10_32 = 3.5
   if RebByOpGuard_Step(l_10_arg0, l_10_arg1, l_10_28, l_10_29, l_10_30, l_10_31, l_10_32) then
      return true
   end
   return false
end


