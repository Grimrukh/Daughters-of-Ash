--@package: m12_01_00_00.luabnd, 451001_battle.lua
--@battle_goal: 451001, BlackDragon451001Battle

local localScriptConfigVar0 = 6
local localScriptConfigVar1 = 32
local localScriptConfigVar2 = 6
local localScriptConfigVar3 = 16
local localScriptConfigVar4 = -2
local localScriptConfigVar5 = 0
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 4
local localScriptConfigVar8 = 0
local localScriptConfigVar9 = 5
local localScriptConfigVar10 = 0
local localScriptConfigVar11 = 4
local localScriptConfigVar12 = 0
local localScriptConfigVar13 = 4
local localScriptConfigVar14 = -4
local localScriptConfigVar15 = 0
local localScriptConfigVar16 = -4
local localScriptConfigVar17 = 0
local localScriptConfigVar18 = 0
local localScriptConfigVar19 = 5
local localScriptConfigVar20 = 0
local localScriptConfigVar21 = 4
local localScriptConfigVar22 = 0
local localScriptConfigVar23 = 4
local localScriptConfigVar24 = 0
local localScriptConfigVar25 = 16
local localScriptConfigVar26 = 0
local localScriptConfigVar27 = 0
local localScriptConfigVar28 = 0
local localScriptConfigVar29 = 0
local localScriptConfigVar30 = 0
local localScriptConfigVar31 = 0
local localScriptConfigVar32 = 0
local localScriptConfigVar33 = 20
local localScriptConfigVar34 = 0
local localScriptConfigVar35 = 0
OnIf_451001 = function(ai, goal, func1_param2)
   if func1_param2 == 0 then
      BlackDragon451001_ActAfter(ai, goal)
   end
   if func1_param2 == 1 then
      BlackDragon451001_Turn(ai, goal)
   end
end

BlackDragon451001Battle_Activate = function(ai, goal)
   local oddsTable = {}
   local actionTable = {}
   local simpleTable = {}
   Common_Clear_Param(oddsTable, actionTable, simpleTable)
   local myHp = ai:GetHpRate(TARGET_SELF)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local fate = ai:GetRandam_Int(1, 100)
   local tailIndex = 0
   local tailGone = ai:GetPartsDmg(tailIndex)
   if ai:IsInsideTargetRegion(TARGET_ENE_0, 1212057) then
      oddsTable[18] = 100
   elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1212059) then
      oddsTable[19] = 100
   elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1212058) then
      oddsTable[18] = 100
   elseif not ai:IsRideLargeSpaceFlag(TARGET_ENE_0) then
      if enemyDistance >= 4 then
         oddsTable[1] = 50
         oddsTable[2] = 50
      else
         oddsTable[4] = 33
         oddsTable[5] = 33
         oddsTable[10] = 34
      end
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 270) then
      -- Turn around in some variable way.
      oddsTable[17] = 100
   elseif enemyDistance >= 12 then
      -- Fire/charge attacks.
      oddsTable[1] = 20
      oddsTable[2] = 10
      oddsTable[3] = 0
      oddsTable[4] = 0
      oddsTable[5] = 30
      oddsTable[6] = 0
      oddsTable[7] = 0
      oddsTable[8] = 0
      oddsTable[9] = 0
      oddsTable[10] = 0
      oddsTable[11] = 0
      oddsTable[12] = 0
      oddsTable[13] = 20
      oddsTable[14] = 0
      oddsTable[15] = 0
      oddsTable[16] = 0
      oddsTable[20] = 20
      if ai:GetNumber(0) >= 1 then
         -- Avoids too much consecutive firebreathing.
         oddsTable[1] = 0
         oddsTable[20] = 40
      end
   elseif enemyDistance >= 6 then
      oddsTable[1] = 20
      oddsTable[2] = 30
      oddsTable[3] = 0
      oddsTable[4] = 20
      oddsTable[5] = 20
      oddsTable[6] = 0
      oddsTable[7] = 0
      oddsTable[8] = 0
      oddsTable[9] = 0
      oddsTable[10] = 0
      oddsTable[11] = 0
      oddsTable[12] = 0
      oddsTable[13] = 10
      oddsTable[14] = 0
      oddsTable[15] = 0
      oddsTable[16] = 0
      if ai:GetNumber(0) >= 1 then
         -- Avoids too much consecutive firebreathing.
         oddsTable[1] = 0
         oddsTable[2] = 0
         oddsTable[4] = 0
      end
   elseif enemyDistance >= 4 then
      oddsTable[1] = 0
      oddsTable[2] = 0
      oddsTable[3] = 100
      oddsTable[4] = 30
      oddsTable[5] = 50
      oddsTable[6] = 0
      oddsTable[7] = 0
      oddsTable[8] = 0
      oddsTable[9] = 0
      oddsTable[10] = 0
      oddsTable[11] = 0
      oddsTable[12] = 0
      oddsTable[13] = 20
      oddsTable[14] = 0
      oddsTable[15] = 0
      oddsTable[16] = 0
   elseif enemyDistance >= 2 then
      oddsTable[1] = 0
      oddsTable[2] = 0
      oddsTable[3] = 100
      oddsTable[4] = 20
      oddsTable[5] = 40
      oddsTable[6] = 0
      oddsTable[7] = 0
      oddsTable[8] = 0
      oddsTable[9] = 0
      oddsTable[10] = 25
      oddsTable[11] = 15
      oddsTable[12] = 0
      oddsTable[13] = 0
      oddsTable[14] = 0
      oddsTable[15] = 0
      oddsTable[16] = 100
   elseif enemyDistance >= 0 then
      oddsTable[1] = 0
      oddsTable[2] = 0
      oddsTable[3] = 100
      oddsTable[4] = 0
      oddsTable[5] = 50
      oddsTable[6] = 0
      oddsTable[7] = 0
      oddsTable[8] = 0
      oddsTable[9] = 0
      oddsTable[10] = 25
      oddsTable[11] = 35
      oddsTable[12] = 0
      oddsTable[13] = 0
      oddsTable[14] = 0
      oddsTable[15] = 0
      oddsTable[16] = 100
   elseif enemyDistance >= -4 then
      -- Close: stomp attacks, charge and breathe fire, or flying fire attack.
      oddsTable[1] = 0
      oddsTable[2] = 0
      oddsTable[3] = 0
      oddsTable[4] = 0
      oddsTable[5] = 0
      oddsTable[6] = 0
      oddsTable[7] = 0
      oddsTable[8] = 25
      oddsTable[9] = 25
      oddsTable[10] = 0
      oddsTable[11] = 35
      oddsTable[12] = 0
      oddsTable[13] = 0
      oddsTable[14] = 15
      oddsTable[15] = 0
      oddsTable[16] = 100
      if ai:GetNumber(1) >= 2 then
         -- Avoids too many consecutive stomps.
         oddsTable[8] = 0
         oddsTable[9] = 0
      end
   else
      oddsTable[1] = 0
      oddsTable[2] = 0
      oddsTable[3] = 0
      oddsTable[4] = 0
      oddsTable[5] = 0
      oddsTable[6] = 0
      oddsTable[7] = 0
      oddsTable[8] = 0
      oddsTable[9] = 0
      oddsTable[10] = 0
      oddsTable[11] = 60
      oddsTable[12] = 0
      oddsTable[13] = 0
      oddsTable[14] = 20
      oddsTable[15] = 20
      oddsTable[16] = 100
   end
   if ai:IsFinishTimer(0) == false then
      -- Downward fire timer? Or this could be grab attack.
      oddsTable[3] = 0
   end
   if ai:IsFinishTimer(1) == false then
      -- Flying loop timer.
      oddsTable[14] = 0
   end
   if ai:IsFinishTimer(2) == false then
      -- Flying fire breath timer.
      oddsTable[16] = 0
   end
   -- 3000: Breathe fire straight ahead.
   -- 3001: Breathe fire from left to right.
   -- 3002: Mark of Calamity.
   -- 3007: front hand stomp (R, L
   -- 3005/3006: slightly faster bites? Used for Turn action.
   -- 3008: FL stomp, then BR stomp.
   -- 3009: Tail spin.
   -- 3010: Charge and breathe fire.
   -- 3011: Tail slam to back left.
   -- 3012: Flying zoom attack.
   -- 3013: Flying loop attack.
   -- 3017: Roar.
   -- 3018: Flying fire.
   -- 3020: Charge swipe (R to L).
   -- 3022: Flying, breathe fire down.
   -- 3023: Charge swipe (L to R).

   actionTable[1] = REGIST_FUNC(ai, goal, BlackDragon451001_Act01)  -- Breathe fire straight ahead (neck thrust).
   actionTable[2] = REGIST_FUNC(ai, goal, BlackDragon451001_Act02)  -- Breathe fire from left to right.
   actionTable[3] = REGIST_FUNC(ai, goal, BlackDragon451001_Act03)  -- Mark of Calamity.
   actionTable[4] = REGIST_FUNC(ai, goal, BlackDragon451001_Act04)  -- Breathe fire in front.
   actionTable[5] = REGIST_FUNC(ai, goal, BlackDragon451001_Act05)  -- One or two hit bite (R to L, L to R).
   actionTable[6] = REGIST_FUNC(ai, goal, BlackDragon451001_Act06)  -- Slightly faster R to L bite (tail-less option).
   actionTable[7] = REGIST_FUNC(ai, goal, BlackDragon451001_Act07)  -- Slightly faster L to R bite (tail-less option).
   actionTable[8] = REGIST_FUNC(ai, goal, BlackDragon451001_Act08)  -- Front hand stomp (R, L).
   actionTable[9] = REGIST_FUNC(ai, goal, BlackDragon451001_Act09)  -- FL stomp, then BR stomp.
   actionTable[10] = REGIST_FUNC(ai, goal, BlackDragon451001_Act10)  -- Tail spin (if has tail).
   actionTable[11] = REGIST_FUNC(ai, goal, BlackDragon451001_Act11)  -- Charge and breathe fire.
   actionTable[12] = REGIST_FUNC(ai, goal, BlackDragon451001_Act12)  -- Tail slam to back left (tail-less option).
   actionTable[13] = REGIST_FUNC(ai, goal, BlackDragon451001_Act13)  -- Flying zoom attack.
   actionTable[14] = REGIST_FUNC(ai, goal, BlackDragon451001_Act14)  -- Flying loop attack.
   actionTable[15] = REGIST_FUNC(ai, goal, BlackDragon451001_Act15)  -- Retreat.
   actionTable[16] = REGIST_FUNC(ai, goal, BlackDragon451001_Act16)  -- Flying, breathe fire down.
   actionTable[17] = REGIST_FUNC(ai, goal, BlackDragon451001_Act17)  -- "Turn" command, variable behavior.
   actionTable[18] = REGIST_FUNC(ai, goal, BlackDragon451001_Act18)  -- Roar.
   actionTable[19] = REGIST_FUNC(ai, goal, BlackDragon451001_Act19)  -- Hovering firebreathing to get you on waterfall.
   actionTable[20] = REGIST_FUNC(ai, goal, BlackDragon451001_Act20)  -- Charge swipe (random direction).
   local func2_var12 = REGIST_FUNC(ai, goal, BlackDragon451001_ActAfter_AdjustSpace)
   Common_Battle_Activate(ai, goal, oddsTable, actionTable, func2_var12, simpleTable)
end

BlackDragon451001_Act01 = function(ai, goal, func3_param2)
   local func3_var3 = ai:GetDist(TARGET_ENE_0)
   local func3_var4 = localScriptConfigVar1 - 1
   local func3_var5 = localScriptConfigVar1 + 2
   local func3_var6 = localScriptConfigVar1
   local func3_var7 = 0
   local func3_var8 = ai:GetRandam_Int(1, 100)
   if func3_var4 <= func3_var3 then
      Approach_Act(ai, goal, func3_var4, func3_var5, func3_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, func3_var6, 0, 45)
   ai:SetNumber(0, ai:GetNumber(0) + 1)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act02 = function(ai, goal, func4_param2)
   local func4_var3 = ai:GetDist(TARGET_ENE_0)
   local func4_var4 = localScriptConfigVar3 - 1
   local func4_var5 = localScriptConfigVar3 + 2
   local func4_var6 = localScriptConfigVar3
   local func4_var7 = 0
   local func4_var8 = ai:GetRandam_Int(1, 100)
   if func4_var4 <= func4_var3 then
      Approach_Act(ai, goal, func4_var4, func4_var5, func4_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3001, TARGET_ENE_0, func4_var6, 0, 45)
   ai:SetNumber(0, ai:GetNumber(0) + 1)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act03 = function(ai, goal, func5_param2)
   local func5_var3 = ai:GetDist(TARGET_ENE_0)
   local func5_var4 = localScriptConfigVar5 - 1
   local func5_var5 = localScriptConfigVar5 + 2
   local func5_var6 = localScriptConfigVar5
   local func5_var7 = 0
   local func5_var8 = ai:GetRandam_Int(1, 100)
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      ai:SetTimer(0, 20)
   else
      ai:SetTimer(0, 30)
   end
   if func5_var4 <= func5_var3 then
      Approach_Act(ai, goal, func5_var4, func5_var5, func5_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, func5_var6, 0, 45)
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act04 = function(ai, goal, func6_param2)
   local func6_var3 = ai:GetDist(TARGET_ENE_0)
   local func6_var4 = localScriptConfigVar7 - 0
   local func6_var5 = localScriptConfigVar7 + 2
   local func6_var6 = localScriptConfigVar7
   local func6_var7 = 0
   local func6_var8 = ai:GetRandam_Int(1, 100)
   if func6_var4 <= func6_var3 then
      Approach_Act(ai, goal, func6_var4, func6_var5, func6_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3003, TARGET_ENE_0, func6_var6, 0, 45)
   ai:SetNumber(0, ai:GetNumber(0) + 1)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act05 = function(ai, goal, func7_param2)
   local func7_var3 = ai:GetDist(TARGET_ENE_0)
   local func7_var4 = localScriptConfigVar9 - 0
   local func7_var5 = localScriptConfigVar9 + 2
   local func7_var6 = localScriptConfigVar9
   local func7_var7 = 0
   local func7_var8 = ai:GetRandam_Int(1, 100)
   if func7_var4 <= func7_var3 then
      Approach_Act(ai, goal, func7_var4, func7_var5, func7_var7, 3)
   end
   if func7_var8 <= 25 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3004, TARGET_ENE_0, func7_var6, 0, 90)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3004, TARGET_ENE_0, func7_var6, 0, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3014, TARGET_ENE_0, func7_var6, 0)
   end
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act06 = function(ai, goal, func8_param2)
   local func8_var3 = ai:GetDist(TARGET_ENE_0)
   local func8_var4 = localScriptConfigVar11 - 1
   local func8_var5 = localScriptConfigVar11 + 2
   local func8_var6 = localScriptConfigVar11
   local func8_var7 = 0
   local func8_var8 = ai:GetRandam_Int(1, 100)
   local func8_var9 = 0
   local func8_var10 = ai:GetPartsDmg(func8_var9)
   if func8_var10 ~= PARTS_DMG_FINAL then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3005, TARGET_ENE_0, func8_var6, 0, 180)
   else
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3015, TARGET_ENE_0, func8_var6, 0, 180)
   end
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act07 = function(ai, goal, func9_param2)
   local func9_var3 = ai:GetDist(TARGET_ENE_0)
   local func9_var4 = localScriptConfigVar13 - 1
   local func9_var5 = localScriptConfigVar13 + 2
   local func9_var6 = localScriptConfigVar13
   local func9_var7 = 0
   local func9_var8 = ai:GetRandam_Int(1, 100)
   local func9_var9 = 0
   local func9_var10 = ai:GetPartsDmg(func9_var9)
   if func9_var10 ~= PARTS_DMG_FINAL then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3006, TARGET_ENE_0, func9_var6, 0, 180)
   else
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3016, TARGET_ENE_0, func9_var6, 0, 180)
   end
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act08 = function(ai, goal, func10_param2)
   local func10_var3 = ai:GetDist(TARGET_ENE_0)
   local func10_var4 = localScriptConfigVar15 - 1
   local func10_var5 = localScriptConfigVar15 + 2
   local func10_var6 = localScriptConfigVar15
   local func10_var7 = 0
   local func10_var8 = ai:GetRandam_Int(1, 100)
   if func10_var4 <= func10_var3 then
      Approach_Act(ai, goal, func10_var4, func10_var5, func10_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3007, TARGET_ENE_0, func10_var6, 0, 90)
   ai:SetNumber(0, 0)
   ai:SetNumber(1, ai:GetNumber(1) + 1)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act09 = function(ai, goal, func11_param2)
   local func11_var3 = ai:GetDist(TARGET_ENE_0)
   local func11_var4 = localScriptConfigVar17 - 1
   local func11_var5 = localScriptConfigVar17 + 2
   local func11_var6 = localScriptConfigVar17
   local func11_var7 = 0
   local func11_var8 = ai:GetRandam_Int(1, 100)
   if func11_var4 <= func11_var3 then
      Approach_Act(ai, goal, func11_var4, func11_var5, func11_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3008, TARGET_ENE_0, func11_var6, 0, 90)
   ai:SetNumber(0, 0)
   ai:SetNumber(1, ai:GetNumber(1) + 1)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act10 = function(ai, goal, func12_param2)
   local func12_var3 = ai:GetDist(TARGET_ENE_0)
   local func12_var4 = localScriptConfigVar19 - 0
   local func12_var5 = localScriptConfigVar19 + 2
   local func12_var6 = localScriptConfigVar19
   local func12_var7 = 0
   local func12_var8 = ai:GetRandam_Int(1, 100)
   local func12_var9 = 0
   local func12_var10 = ai:GetPartsDmg(func12_var9)
   if func12_var10 ~= PARTS_DMG_FINAL then
      if func12_var4 <= func12_var3 then
         Approach_Act(ai, goal, func12_var4, func12_var5, func12_var7, 3)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3009, TARGET_ENE_0, func12_var6, 0, 180)
      end
   else
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 7)
   end
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

BlackDragon451001_Act11 = function(ai, goal, func13_param2)
   local func13_var3 = ai:GetDist(TARGET_ENE_0)
   local func13_var4 = localScriptConfigVar21 - 1
   local func13_var5 = localScriptConfigVar21 + 2
   local func13_var6 = localScriptConfigVar21
   local func13_var7 = 0
   local func13_var8 = ai:GetRandam_Int(1, 100)
   if func13_var4 <= func13_var3 then
      Approach_Act(ai, goal, func13_var4, func13_var5, func13_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3010, TARGET_ENE_0, func13_var6, 0, 90)
   ai:SetNumber(0, ai:GetNumber(0) + 1)
   ai:SetNumber(1, 0)
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

BlackDragon451001_Act12 = function(ai, goal, func14_param2)
   local func14_var3 = ai:GetDist(TARGET_ENE_0)
   local func14_var4 = localScriptConfigVar23 - 1
   local func14_var5 = localScriptConfigVar23 + 2
   local func14_var6 = localScriptConfigVar23
   local func14_var7 = 0
   local func14_var8 = ai:GetRandam_Int(1, 100)
   local func14_var9 = 0
   local func14_var10 = ai:GetPartsDmg(func14_var9)
   if func14_var10 ~= PARTS_DMG_FINAL then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3011, TARGET_ENE_0, func14_var6, 0, 360)
   else
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3021, TARGET_ENE_0, func14_var6, 0, 360)
   end
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, ai:GetNumber(2) + 1)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act13 = function(ai, goal, func15_param2)
   local func15_var3 = ai:GetDist(TARGET_ENE_0)
   local func15_var4 = localScriptConfigVar25 - 1
   local func15_var5 = localScriptConfigVar25 + 2
   local func15_var6 = 9999
   local func15_var7 = 0
   local func15_var8 = ai:GetRandam_Int(1, 100)
   if func15_var4 <= func15_var3 then
      Approach_Act(ai, goal, func15_var4, func15_var5, func15_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, func15_var6, 0, 90)
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act14 = function(ai, goal, func16_param2)
   local func16_var3 = ai:GetDist(TARGET_ENE_0)
   local func16_var4 = localScriptConfigVar27 - 0
   local func16_var5 = localScriptConfigVar27 + 2
   local func16_var6 = 9999
   local func16_var7 = 0
   local func16_var8 = ai:GetRandam_Int(1, 100)
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      ai:SetTimer(1, 25)
   else
      ai:SetTimer(1, 45)
   end
   if func16_var4 <= func16_var3 then
      Approach_Act(ai, goal, func16_var4, func16_var5, func16_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3013, TARGET_ENE_0, func16_var6, 0, 360)
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act15 = function(ai, goal, func17_param2)
   local func17_var3 = ai:GetDist(TARGET_ENE_0)
   local func17_var4 = ai:GetRandam_Int(1, 100)
   goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 3, TARGET_ENE_0, 3, TARGET_ENE_0, true, -1)
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

BlackDragon451001_Act16 = function(ai, goal, func18_param2)
   local func18_var3 = ai:GetDist(TARGET_ENE_0)
   local func18_var4 = localScriptConfigVar35 - 0
   local func18_var5 = localScriptConfigVar35 + 2
   local func18_var6 = 9999
   local func18_var7 = 0
   local func18_var8 = ai:GetRandam_Int(1, 100)
   if ai:GetHpRate(TARGET_SELF) <= 0.5 then
      ai:SetTimer(2, 25)
   else
      ai:SetTimer(2, 45)
   end
   if func18_var4 <= func18_var3 then
      Approach_Act(ai, goal, func18_var4, func18_var5, func18_var7, 3)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3022, TARGET_ENE_0, func18_var6, 0, 360)
   ai:SetNumber(0, ai:GetNumber(0) + 1)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_Act17 = function(ai, goal, func19_param2)
   goal:AddSubGoal(GOAL_COMMON_If, 10, 1)
end

BlackDragon451001_Turn = function(ai, goal)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local tailIndex = 0
   local tailDamage = ai:GetPartsDmg(tailIndex)
   local fate = ai:GetRandam_Int(1, 100)
   local fate2 = ai:GetRandam_Int(1, 100)
   local func20_var7 = ai:GetEventRequest()
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 30) then
      if enemyDistance >= -2 and enemyDistance <= 6 and tailDamage ~= PARTS_DMG_FINAL and ai:GetNumber(2) <= 0 and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 15) then
         BlackDragon451001_Act12(ai, goal)
      elseif enemyDistance >= 2 and enemyDistance <= 6 and fate <= 50 then
         BlackDragon451001_Act06(ai, goal)
      elseif enemyDistance >= 2 and enemyDistance <= 6 and fate <= 100 then
         BlackDragon451001_Act07(ai, goal)
      elseif fate2 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3029, TARGET_ENE_0, DIST_None, 0, 90)
      else
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3028, TARGET_ENE_0, DIST_None, 0, 90)
      end
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 90) then
      if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
         if enemyDistance >= 0 and enemyDistance <= 4 and fate <= 75 then
            BlackDragon451001_Act06(ai, goal)
         else
            goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3027, TARGET_ENE_0, DIST_None, 0, 90)
         end
      elseif enemyDistance >= 0 and enemyDistance <= 4 and fate <= 75 then
         BlackDragon451001_Act07(ai, goal)
      else
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3026, TARGET_ENE_0, DIST_None, 0, 90)
      end
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 150) then
      if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
         if enemyDistance >= 0 and enemyDistance <= 4 and fate <= 75 then
            BlackDragon451001_Act07(ai, goal)
         else
            goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3027, TARGET_ENE_0, DIST_None, 0, 90)
         end
      elseif enemyDistance >= 0 and enemyDistance <= 4 and fate <= 75 then
         BlackDragon451001_Act06(ai, goal)
      else
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3026, TARGET_ENE_0, DIST_None, 0, 90)
      end
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 210) then
      if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
         if enemyDistance >= 0 and enemyDistance <= 4 and fate <= 75 then
            BlackDragon451001_Act07(ai, goal)
         else
            goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3027, TARGET_ENE_0, DIST_None, 0, 90)
         end
      elseif enemyDistance >= 0 and enemyDistance <= 4 and fate <= 75 then
         BlackDragon451001_Act06(ai, goal)
      else
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3026, TARGET_ENE_0, DIST_None, 0, 90)
      end
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3025, TARGET_ENE_0, DIST_None, 0, 90)
   else
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 3, 3024, TARGET_ENE_0, DIST_None, 0, 90)
   end
end

BlackDragon451001_Act18 = function(ai, goal, func21_param2)
   local func21_var3 = ai:GetDist(TARGET_ENE_0)
   local func21_var4 = 9999
   local func21_var5 = 9999
   local func21_var6 = 9999
   local func21_var7 = 0
   local func21_var8 = ai:GetRandam_Int(1, 100)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 3, POINT_EVENT, 3, TARGET_SELF, false, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3017, TARGET_ENE_0, func21_var6, 0, 360)
   ai:SetNumber(0, ai:GetNumber(0) + 1)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

BlackDragon451001_Act19 = function(ai, goal, func22_param2)
   local func22_var3 = ai:GetDist(TARGET_ENE_0)
   local func22_var4 = 9999
   local func22_var5 = 9999
   local func22_var6 = 9999
   local func22_var7 = 0
   local func22_var8 = ai:GetRandam_Int(1, 100)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 3, POINT_EVENT, 3, TARGET_SELF, false, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3018, TARGET_ENE_0, func22_var6, 0, 360)
   ai:SetNumber(0, ai:GetNumber(0) + 1)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

BlackDragon451001_Act20 = function(ai, goal, func23_param2)
   local func23_var3 = ai:GetDist(TARGET_ENE_0)
   local func23_var4 = localScriptConfigVar33 - 1
   local func23_var5 = localScriptConfigVar33 + 2
   local func23_var6 = 9999
   local func23_var7 = 0
   local func23_var8 = ai:GetRandam_Int(1, 100)
   if func23_var4 <= func23_var3 then
      Approach_Act(ai, goal, func23_var4, func23_var5, func23_var7, 3)
   end
   if func23_var8 <= 50 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3020, TARGET_ENE_0, func23_var6, 0, 90)
   else
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3023, TARGET_ENE_0, func23_var6, 0, 90)
   end
   ai:SetNumber(0, 0)
   ai:SetNumber(1, 0)
   ai:SetNumber(2, 0)
   GetWellSpace_Odds = 50
   return GetWellSpace_Odds
end

BlackDragon451001_ActAfter = function(ai, goal)
   local randomRoll = ai:GetRandam_Int(1, 100)
   local randomRoll2 = ai:GetRandam_Int(1, 100)
   local randomDirection = ai:GetRandam_Int(0, 1)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 330) then
      BlackDragon451001_Turn(ai, goal)
   elseif enemyDistance <= 2 then
      if randomRoll <= 50 then
         if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 120) then
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 7)
         elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 5)
         else
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 5)
         end
      elseif randomRoll <= 100 then
         if randomRoll2 <= 50 then
            goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, randomDirection, ai:GetRandam_Int(30, 45), true, true, -1)
         else
            goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 5, TARGET_ENE_0, 3, TARGET_ENE_0, true, -1)
         end
      end
   elseif enemyDistance <= 4 then
      if randomRoll <= 25 then
         if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 120) then
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 7)
         elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 5)
         else
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 5)
         end
      elseif randomRoll <= 100 then
         if randomRoll2 <= 50 then
            goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, randomDirection, ai:GetRandam_Int(45, 60), true, true, -1)
         else
            goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 5, TARGET_ENE_0, 3, TARGET_ENE_0, true, -1)
         end
      end
   elseif enemyDistance <= 8 then
      if randomRoll <= 13 then
         if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 120) then
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 7)
         elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 5)
         else
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 5)
         end
      elseif randomRoll <= 100 then
         if randomRoll2 <= 50 then
            goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, randomDirection, ai:GetRandam_Int(60, 75), true, true, -1)
         else
            goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 5, TARGET_ENE_0, 3, TARGET_ENE_0, true, -1)
         end
      elseif randomRoll <= 0 then
         if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 120) then
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 7)
         elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) then
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 5)
         else
            goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 5)
         end
      elseif randomRoll <= 100 then
         if randomRoll2 <= 50 then
            goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, randomDirection, ai:GetRandam_Int(75, 90), true, true, -1)
         else
            goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 5, TARGET_ENE_0, 3, TARGET_ENE_0, true, -1)
         end
      end
   end
end

BlackDragon451001_ActAfter_AdjustSpace = function(ai, goal, func25_param2)
   goal:AddSubGoal(GOAL_COMMON_If, 20, 0)
end

BlackDragon451001Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

BlackDragon451001Battle_Terminate = function(ai, goal)
end

BlackDragon451001Battle_Interupt = function(ai, goal)
   local fate = ai:GetRandam_Int(1, 100)
   local fate2 = ai:GetRandam_Int(1, 100)
   local fate3 = ai:GetRandam_Int(1, 100)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   if UseItem_Act(ai, goal, 12, 40) then
      if enemyDistance >= 6 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3012, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   if ai:IsInterupt(INTERUPT_FindAttack) then
      if fate <= 80 then
         if enemyDistance >= 0 and enemyDistance <= 6 and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 90) then
            goal:ClearSubGoal()
            if fate2 <= 50 then
               goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, 3003, TARGET_ENE_0, DIST_None, 0, 45)
            else
               goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, 3004, TARGET_ENE_0, DIST_None, 0, 45)
            end
            return true
         else
            return false
         end
      else
         return false
      end
   end
   if ai:IsInterupt(INTERUPT_Shoot) then
      if fate <= 80 then
         if enemyDistance <= 4 and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 90) then
            goal:ClearSubGoal()
            if fate2 <= 50 then
               goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, 3003, TARGET_ENE_0, DIST_None, 0, 45)
            else
               goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, 3004, TARGET_ENE_0, DIST_None, 0, 45)
            end
            return true
         elseif enemyDistance <= 12 and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 120) then
            goal:ClearSubGoal()
            if fate2 <= 50 then
               goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, 3001, TARGET_ENE_0, DIST_None, 0, 45)
            else
               goal:ClearSubGoal()
               if fate3 <= 50 then
                  goal:AddSubGoal(GOAL_COMMON_SpinStep, 1, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 10)
               else
                  goal:AddSubGoal(GOAL_COMMON_SpinStep, 1, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 10)
               end
            end
            return true
         elseif enemyDistance <= 20 and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 150) then
            goal:ClearSubGoal()
            if fate2 <= 50 then
               goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 1, 3000, TARGET_ENE_0, DIST_None, 0, 45)
            else
               goal:ClearSubGoal()
               if fate3 <= 50 then
                  goal:AddSubGoal(GOAL_COMMON_SpinStep, 1, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 10)
               else
                  goal:AddSubGoal(GOAL_COMMON_SpinStep, 1, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 10)
               end
            end
            return true
         else
            return false
         end
      else
         return false
      end
   end
   return false
end


