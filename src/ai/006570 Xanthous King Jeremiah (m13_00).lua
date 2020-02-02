--@package: m13_00_00_00.luabnd, 006570_battle.lua
--@battle_goal: 6570, YellowMantle6570Battle

local l_0_0 = 0
local l_0_1 = 2.6
local l_0_2 = 0
local l_0_3 = 2.5
local l_0_4 = 0
local l_0_5 = 1.8
local l_0_6 = 0
local l_0_7 = 1
local l_0_8 = 4
local l_0_9 = 6
local l_0_10 = 4
local l_0_11 = 4
local l_0_12 = 4
local l_0_13 = 4

YellowMantle6570Battle_Activate = function(ai, goal)
   local oddsTable = {}
   local actionTable = {}
   local simpleActionTable = {}
   Common_Clear_Param(oddsTable, actionTable, simpleActionTable)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local enemyIsGuarding = 0
   if ai:IsTargetGuard(TARGET_ENE_0) == true then
      enemyIsGuarding = 1
   end
   local usesFirestorm = 0
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      usesFirestorm = 1
   end
   if enemyDistance >= 3.5 then
      -- Distant
      oddsTable[1] = 5
      oddsTable[2] = 5
      oddsTable[3] = 0
      oddsTable[18] = 30  -- Pyromancy 1 (Chaos Fireball)
      oddsTable[19] = 30 * usesFirestorm  -- Pyromancy 2 (Chaos Firestorm)
      oddsTable[20] = 30  -- Pyromancy 3 (Chaos Fire Whip)
   elseif enemyDistance >= 2 then
      -- Medium
      oddsTable[1] = 15
      oddsTable[2] = 15
      oddsTable[3] = 0
      oddsTable[18] = 29
      oddsTable[19] = 21 * usesFirestorm
      oddsTable[20] = 20
   else
      -- Close
      oddsTable[1] = 20
      oddsTable[2] = 20
      oddsTable[3] = 0
      oddsTable[5] = 10
      oddsTable[17] = 10 * enemyIsGuarding  -- Kick
      oddsTable[18] = 15
      oddsTable[19] = 15 * usesFirestorm
      oddsTable[20] = 20
   end
   actionTable[1] = REGIST_FUNC(ai, goal, YellowMantle6570_Act01)
   actionTable[2] = REGIST_FUNC(ai, goal, YellowMantle6570_Act02)
   actionTable[5] = REGIST_FUNC(ai, goal, YellowMantle6570_Act05)
   actionTable[17] = REGIST_FUNC(ai, goal, YellowMantle6570_Act17)
   actionTable[18] = REGIST_FUNC(ai, goal, YellowMantle6570_Act18)
   actionTable[19] = REGIST_FUNC(ai, goal, YellowMantle6570_Act19)
   actionTable[20] = REGIST_FUNC(ai, goal, YellowMantle6570_Act20)
   local actAfter = REGIST_FUNC(ai, goal, YellowMantle6570_ActAfter_AdjustSpace, atkAfterOddsTbl)
   Common_Battle_Activate(ai, goal, oddsTable, actionTable, actAfter, simpleActionTable)
end

YellowMantle6570_Act01 = function(ai, goal, l_2_arg2)
   -- Two or three hit whip combo
   local odds = ai:GetRandam_Int(1, 100)
   NPC_KATATE_Switch(ai, goal)
   CommonNPC_ChangeWepR1(ai, goal)
   local l_2_5 = l_0_1
   local l_2_6 = l_0_1 + 5
   local l_2_7 = 0
   NPC_Approach_Act(ai, goal, l_2_5, l_2_6, l_2_7)
   if odds <= 30 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
   elseif odds <= 60 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_LargeR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
   end
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

YellowMantle6570_Act02 = function(ai, goal, unknown)
   -- One or two hit strong whip combo
   local l_3_3 = ai:GetDist(TARGET_ENE_0)
   local l_3_4 = ai:GetRandam_Int(1, 100)
   NPC_KATATE_Switch(ai, goal)
   CommonNPC_ChangeWepR1(ai, goal)
   local l_3_5 = l_0_3
   local l_3_6 = l_0_3 + 5
   local l_3_7 = 100
   NPC_Approach_Act(ai, goal, l_3_5, l_3_6, l_3_7)
   if l_3_4 <= 30 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_LargeR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_LargeR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_LargeR, TARGET_ENE_0, DIST_Middle, 0, -1)
   end
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

YellowMantle6570_Act05 = function(ai, goal, unknown)
   -- Backstep and whip
   local l_4_3 = ai:GetDist(TARGET_ENE_0)
   local l_4_4 = ai:GetRandam_Int(1, 100)
   NPC_KATATE_Switch(ai, goal)
   CommonNPC_ChangeWepR1(ai, goal)
   local l_4_5 = l_0_5
   local l_4_6 = l_0_5 + 5
   local l_4_7 = 100
   NPC_Approach_Act(ai, goal, l_4_5, l_4_6, l_4_7)
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_BackstepB, TARGET_ENE_0, 6, 1.5, 90)
   goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
   if ai:GetHpRate(TARGET_SELF) > 0.5 then
      GetWellSpace_Odds = 100
   else
      GetWellSpace_Odds = 0
   end
   return GetWellSpace_Odds
end

YellowMantle6570_Act07 = function(ai, goal, param)
   -- Step forward and whip (unused)
   local l_5_3 = ai:GetDist(TARGET_ENE_0)
   local l_5_4 = ai:GetRandam_Int(1, 100)
   NPC_KATATE_Switch(ai, goal)
   CommonNPC_ChangeWepR1(ai, goal)
   local l_5_5 = Rolling_Atk_max
   local l_5_6 = Rolling_Atk_max + 5
   local l_5_7 = 100
   NPC_Approach_Act(ai, goal, l_5_5, l_5_6, l_5_7)
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_StepF, TARGET_ENE_0, 3, 1.5, 90)
   goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
   if ai:GetHpRate(TARGET_SELF) > 0.5 then
      GetWellSpace_Odds = 100
   else
      GetWellSpace_Odds = 0
   end
   return GetWellSpace_Odds
end

YellowMantle6570_Act09 = function(ai, goal, unknown)
   -- Two-handed whip combos I think
   local l_6_3 = ai:GetDist(TARGET_ENE_0)
   local fate = ai:GetRandam_Int(1, 100)
   CommonNPC_ChangeWepR1(ai, goal)
   NPC_RYOUTE_Switch(ai, goal)
   local l_6_5 = Whand_jyaku_max
   local l_6_6 = Whand_jyaku_max + 5
   local l_6_7 = 50
   NPC_Approach_Act(ai, goal, l_6_5, l_6_6, l_6_7)
   if fate <= 30 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
   elseif fate <= 60 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_LargeR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
   end
   if ai:GetHpRate(TARGET_SELF) > 0.5 then
      GetWellSpace_Odds = 100
   else
      GetWellSpace_Odds = 0
   end
   return GetWellSpace_Odds
end

YellowMantle6570_Act10 = function(ai, goal, unknown)
   -- Two-handed strong whip combos
   local l_7_3 = ai:GetDist(TARGET_ENE_0)
   local fate = ai:GetRandam_Int(1, 100)
   CommonNPC_ChangeWepR1(ai, goal)
   NPC_RYOUTE_Switch(ai, goal)
   local l_7_5 = Whand_kyou_max
   local l_7_6 = Whand_kyou_max + 5
   local l_7_7 = 50
   NPC_Approach_Act(ai, goal, l_7_5, l_7_6, l_7_7)
   if fate <= 30 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_LargeR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_LargeR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_LargeR, TARGET_ENE_0, DIST_Middle, 0, -1)
   end
   if ai:GetHpRate(TARGET_SELF) > 0.5 then
      GetWellSpace_Odds = 100
   else
      GetWellSpace_Odds = 0
   end
   return GetWellSpace_Odds
end

YellowMantle6570_Act13 = function(ai, goal, unknown)
   -- Backstep whip two-hand combo
   local l_8_3 = ai:GetDist(TARGET_ENE_0)
   local l_8_4 = ai:GetRandam_Int(1, 100)
   CommonNPC_ChangeWepR1(ai, goal)
   NPC_RYOUTE_Switch(ai, goal)
   local l_8_5 = Backstep_AtkW_max
   local l_8_6 = Backstep_AtkW_max + 5
   local l_8_7 = 100
   NPC_Approach_Act(ai, goal, l_8_5, l_8_6, l_8_7)
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_BackstepB, TARGET_ENE_0, 6, 1.5, 90)
   goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
   if ai:GetHpRate(TARGET_SELF) > 0.5 then
      GetWellSpace_Odds = 100
   else
      GetWellSpace_Odds = 0
   end
   return GetWellSpace_Odds
end

YellowMantle6570_Act15 = function(l_9_arg0, l_9_arg1, l_9_arg2)
   -- Forward step whip two-hand combo
   local l_9_3 = l_9_arg0:GetDist(TARGET_ENE_0)
   local l_9_4 = l_9_arg0:GetRandam_Int(1, 100)
   CommonNPC_ChangeWepR1(l_9_arg0, l_9_arg1)
   NPC_RYOUTE_Switch(l_9_arg0, l_9_arg1)
   local l_9_5 = Rolling_AtkW_max
   local l_9_6 = Rolling_AtkW_max + 5
   local l_9_7 = 100
   NPC_Approach_Act(l_9_arg0, l_9_arg1, l_9_5, l_9_6, l_9_7)
   l_9_arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_StepF, TARGET_ENE_0, 3, 1.5, 90)
   l_9_arg1:AddSubGoal(GOAL_COMMON_ComboFinal, 10, NPC_ATK_NormalR, TARGET_ENE_0, DIST_Middle, 0, -1)
   if ai:GetHpRate(TARGET_SELF) > 0.5 then
      GetWellSpace_Odds = 100
   else
      GetWellSpace_Odds = 0
   end
   return GetWellSpace_Odds
end

YellowMantle6570_Act17 = function(l_10_arg0, l_10_arg1, l_10_arg2)
   -- Kick
   local l_10_3 = l_10_arg0:GetDist(TARGET_ENE_0)
   local l_10_4 = l_10_arg0:GetRandam_Int(1, 100)
   local l_10_5 = l_0_7
   local l_10_6 = l_0_7 + 5
   local l_10_7 = 100
   NPC_Approach_Act(l_10_arg0, l_10_arg1, l_10_5, l_10_6, l_10_7)
   l_10_arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_PushR, TARGET_ENE_0, DIST_Middle, 1.5, 90)
   if ai:GetHpRate(TARGET_SELF) > 0.5 then
      GetWellSpace_Odds = 100
   else
      GetWellSpace_Odds = 0
   end
   return GetWellSpace_Odds
end

YellowMantle6570_Act18 = function(ai, goal, l_11_arg2)
   -- First pyromancy (Chaos Fireball)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local l_11_4 = ai:GetRandam_Int(1, 100)
   CommonNPC_ChangeWepR1(ai, goal)
   ai:ChangeEquipMagic(0)
   if l_0_9 <= enemyDistance then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2.5, TARGET_ENE_0, l_0_9, TARGET_SELF, false, -1)
   elseif enemyDistance <= l_0_8 then
      goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 1.5, TARGET_ENE_0, l_0_8, TARGET_ENE_0, false, -1)
   end
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_MagicL, TARGET_ENE_0, DIST_None, 1.5, 90)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

YellowMantle6570_Act19 = function(l_12_arg0, l_12_arg1, l_12_arg2)
   -- Second pyromancy (Chaos Firestorm)
   local l_12_3 = l_12_arg0:GetDist(TARGET_ENE_0)
   local l_12_4 = l_12_arg0:GetRandam_Int(1, 100)
   CommonNPC_ChangeWepR1(l_12_arg0, l_12_arg1)
   l_12_arg0:ChangeEquipMagic(1)
   if l_0_11 <= l_12_3 then
      l_12_arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 2.5, TARGET_ENE_0, l_0_11, TARGET_SELF, false, -1)
   elseif l_12_3 <= l_0_10 then
      l_12_arg1:AddSubGoal(GOAL_COMMON_LeaveTarget, 1.5, TARGET_ENE_0, l_0_10, TARGET_ENE_0, false, -1)
   end
   l_12_arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_MagicL, TARGET_ENE_0, DIST_None, 1.5, 90)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

YellowMantle6570_Act20 = function(l_13_arg0, l_13_arg1, l_13_arg2)
   -- Third pyromancy (Chaos Whip)
   local l_13_3 = l_13_arg0:GetDist(TARGET_ENE_0)
   local l_13_4 = l_13_arg0:GetRandam_Int(1, 100)
   local l_13_5 = l_13_arg0:GetDist(TARGET_ENE_0)
   local l_13_6 = l_13_arg0:GetRandam_Int(1, 100)
   local l_13_7 = l_13_arg0:GetWepCateRight(TARGET_SELF)
   CommonNPC_ChangeWepR1(l_13_arg0, l_13_arg1)
   l_13_arg0:ChangeEquipMagic(2)
   if l_0_13 <= l_13_5 then
      l_13_arg1:AddSubGoal(GOAL_COMMON_ApproachTarget, 2.5, TARGET_ENE_0, l_0_13, TARGET_SELF, false, -1)
   elseif l_13_5 <= l_0_12 then
      l_13_arg1:AddSubGoal(GOAL_COMMON_LeaveTarget, 1.5, TARGET_ENE_0, l_0_12, TARGET_ENE_0, false, -1)
   end
   l_13_arg1:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, NPC_ATK_MagicL, TARGET_ENE_0, DIST_None, 1.5, 90)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

YellowMantle6570_ActAfter_AdjustSpace = function(l_14_arg0, l_14_arg1, l_14_arg2)
   local l_14_3 = l_14_arg0:GetRandam_Int(1, 100)
   local l_14_4 = l_14_arg0:GetRandam_Int(1, 100)
   local l_14_5 = 3
   if l_14_3 <= 30 then
      l_14_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, NPC_ATK_BackstepB, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 2)
   end
end

YellowMantle6570Battle_Update = function(l_15_arg0, l_15_arg1)
   return GOAL_RESULT_Continue
end

YellowMantle6570Battle_Terminate = function(l_16_arg0, l_16_arg1)
end

YellowMantle6570Battle_Interupt = function(l_17_arg0, l_17_arg1)
   local l_17_2 = l_17_arg0:GetDist(TARGET_ENE_0)
   local l_17_3 = l_17_arg0:GetRandam_Int(1, 100)
   local l_17_4 = l_17_arg0:GetRandam_Int(1, 100)
   local l_17_5 = l_17_arg0:GetRandam_Int(1, 100)
   if l_17_arg0:IsInterupt(INTERUPT_FindAttack) then
      local l_17_6 = 3
      local l_17_7 = 10
      local l_17_8 = 3
      if l_17_2 <= l_17_6 and l_17_3 <= l_17_7 then
         l_17_arg1:ClearSubGoal()
         if l_17_3 <= 50 then
            l_17_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, NPC_ATK_StepB, TARGET_ENE_0, 0, AI_DIR_TYPE_F, 0)
         else
            l_17_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, l_17_arg0:GetRandam_Int(11, 12), TARGET_SELF, 0, AI_DIR_TYPE_F, 4)
         end
         return true
      end
   end
   if l_17_arg0:IsInterupt(INTERUPT_Damaged) then
      local l_17_6 = 3
      local l_17_7 = 10
      if l_17_2 < l_17_6 and l_17_3 <= l_17_7 then
         l_17_arg1:ClearSubGoal()
         if l_17_3 <= 50 then
            l_17_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, NPC_ATK_StepB, TARGET_ENE_0, 0, AI_DIR_TYPE_F, 0)
         else
            l_17_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, l_17_arg0:GetRandam_Int(11, 12), TARGET_SELF, 0, AI_DIR_TYPE_F, 4)
         end
      end
   end
   if l_17_arg0:IsInterupt(INTERUPT_ReboundByOpponentGuard) then
      local l_17_6 = 3
      local l_17_7 = 10
      if l_17_2 < l_17_6 then
         if l_17_3 <= l_17_7 then
            l_17_arg1:ClearSubGoal()
            if l_17_4 <= l_17_7 then
               if l_17_5 <= 50 then
                  l_17_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, NPC_ATK_StepB, TARGET_ENE_0, 0, AI_DIR_TYPE_F, 0)
               else
                  l_17_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, l_17_arg0:GetRandam_Int(11, 12), TARGET_SELF, 0, AI_DIR_TYPE_F, 4)
               end
            else
               l_17_arg0:Replaning()
               l_17_arg1:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
               return true
            end
         else
            l_17_arg1:ClearSubGoal()
            l_17_arg1:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
            l_17_arg0:Replaning()
            return true
         end
      else
         l_17_arg1:ClearSubGoal()
         l_17_arg1:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_ENE_0)
         l_17_arg0:Replaning()
         return true
      end
   end
   if l_17_arg0:IsInterupt(INTERUPT_Shoot) then
      local l_17_6 = 50
      if l_17_3 <= l_17_6 then
         l_17_arg1:ClearSubGoal()
         l_17_arg1:AddSubGoal(GOAL_COMMON_SpinStep, 10, l_17_arg0:GetRandam_Int(11, 12), TARGET_SELF, 0, AI_DIR_TYPE_F, 4)
      end
      return true
   end
   return false
end