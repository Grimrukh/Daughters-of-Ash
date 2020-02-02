--@package: m15_01_00_00.luabnd, 530000_battle.lua
--@battle_goal: 530000, Jareel530000Battle

local localScriptConfigVar1 = 2
local localScriptConfigVar3 = 5.6
local localScriptConfigVar5 = 2.1
local localScriptConfigVar7 = 1.6
local localScriptConfigVar9 = 1.2

-- Jareel powers up at 60% HP, by using the explosion attack. He will also use it at 40% and 20% HP, or whenever the
-- timer runs out, whichever comes first. He can continue using it after the third time but it will not power him up
-- any further. The power-up reduces his GetWellSpace_Odds for the duration of the timer.

-- REVISION NOTES:
-- Mostly works well. Some attacks do not work as combos, but are clearly intended as finishers. He also uses the
-- backstep a little too often, and one move (a grab probably) is just broken, he stands there doing nothing.



Jareel530000Battle_Activate = function(ai, goal)
   local actionChance = {}
   local action = {}
   local basicAttackConfig = {}
   Common_Clear_Param(actionChance, action, basicAttackConfig)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local bossHealth = ai:GetHpRate(TARGET_SELF)
   local bossPhase = ai:GetNumber(0)
   local readyForPowerUp = ai:IsFinishTimer(0)
   local backAttackChance = ai:GetRandam_Int(1, 100)
   local getWellSpaceOdds = 0

   -- Always open with running kick.
   if ai:GetNumber(2) == 0 then
      ai:SetNumber(2, 1)
      Jareel530000_Act03(ai, goal)
      return
   end

   if bossPhase == 0 and bossHealth <= 0.6 then
      actionChance[9] = 100  -- first power-up
   elseif bossPhase == 1 and bossHealth <= 0.4 then
      actionChance[9] = 100  -- second power-up
   elseif bossPhase == 2 and bossHealth <= 0.2 then
      actionChance[9] = 100  -- third power-up
   elseif ai:IsInsideTarget(TARGET_ENEMY, AI_DIR_TYPE_B, 160) and backAttackChance <= 70 then
      actionChance[2] = 50  -- attack player behind
      actionChance[7] = 50  -- attack player behind
   else
      -- Phase and distance dependent patterns
      if enemyDistance >= 8 then
         actionChance[1] = 0  -- melee combos
         actionChance[2] = 0  -- spin back, leap smash
         actionChance[3] = 15  -- roundhouse kick
         actionChance[4] = 5  -- grab
         actionChance[5] = 25  -- two-handed
         actionChance[6] = 30  -- running leap
         actionChance[7] = 0  -- spinning kick and backfist
         if bossPhase == 3 then
            actionChance[9] = 20  -- explosion
         else
            actionChance[9] = 0  -- explosion
         end
         if bossPhase >= 2 then
            actionChance[10] = 20  -- hyper combo
         elseif bossPhase >= 1 then
            actionChance[10] = 10  -- hyper combo
         else
            actionChance[10] = 0  -- hyper combo
         end
      elseif enemyDistance >= 5 then
         if ai:IsTargetGuard(TARGET_ENE_0) == true then
            actionChance[1] = 10  -- melee combos
            actionChance[2] = 0  -- spin back, leap smash
            actionChance[3] = 15  -- roundhouse kick
            actionChance[4] = 50  -- grab
            actionChance[5] = 15  -- two-handed
            actionChance[6] = 20  -- running leap
            actionChance[7] = 10  -- spinning kick and backfist
            if bossPhase == 3 then
               actionChance[9] = 20  -- explosion
            else
               actionChance[9] = 0  -- explosion
            end
            if bossPhase >= 2 then
               actionChance[10] = 20  -- hyper combo
            elseif bossPhase >= 1 then
               actionChance[10] = 10  -- hyper combo
            else
               actionChance[10] = 0  -- hyper combo
            end
         else
            actionChance[1] = 15  -- melee combos
            actionChance[2] = 0  -- spin back, leap smash
            actionChance[3] = 10  -- roundhouse kick
            actionChance[4] = 30  -- grab
            actionChance[5] = 10  -- two-handed
            actionChance[6] = 25  -- running leap
            actionChance[7] = 15  -- spinning kick and backfist
            if bossPhase == 3 then
               actionChance[9] = 10  -- explosion
            else
               actionChance[9] = 0  -- explosion
            end
            if bossPhase >= 2 then
               actionChance[10] = 10  -- hyper combo
            elseif bossPhase >= 1 then
               actionChance[10] = 5  -- hyper combo
            else
               actionChance[10] = 0  -- hyper combo
            end
         end
      elseif enemyDistance >= 3.5 then
         if ai:IsTargetGuard(TARGET_ENE_0) == true then
            actionChance[1] = 10  -- melee combos
            actionChance[2] = 0  -- spin back, leap smash
            actionChance[3] = 20  -- roundhouse kick
            actionChance[4] = 20  -- grab
            actionChance[5] = 15  -- two-handed
            actionChance[6] = 10  -- running leap
            actionChance[7] = 15  -- spinning kick and backfist
            if bossPhase == 3 then
               actionChance[9] = 20  -- explosion
            else
               actionChance[9] = 0  -- explosion
            end
            if bossPhase >= 2 then
               actionChance[10] = 20  -- hyper combo
            elseif bossPhase >= 1 then
               actionChance[10] = 10  -- hyper combo
            else
               actionChance[10] = 0  -- hyper combo
            end
         else
            actionChance[1] = 15  -- melee combos
            actionChance[2] = 0  -- spin back, leap smash
            actionChance[3] = 5  -- roundhouse kick
            actionChance[4] = 5  -- grab
            actionChance[5] = 10  -- two-handed
            actionChance[6] = 15  -- running leap
            actionChance[7] = 15  -- spinning kick and backfist
            if bossPhase == 3 then
               actionChance[9] = 10  -- explosion
            else
               actionChance[9] = 0  -- explosion
            end
            if bossPhase >= 2 then
               actionChance[10] = 10  -- hyper combo
            elseif bossPhase >= 1 then
               actionChance[10] = 5  -- hyper combo
            else
               actionChance[10] = 0  -- hyper combo
            end
         end
      else
         if ai:IsTargetGuard(TARGET_ENE_0) == true then
            actionChance[1] = 15  -- melee combos
            actionChance[2] = 10  -- spin back, leap smash
            actionChance[3] = 10  -- roundhouse kick
            actionChance[4] = 35  -- grab
            actionChance[5] = 20  -- two-handed
            actionChance[6] = 0  -- running leap
            actionChance[7] = 20  -- spinning kick and backfist
            if bossPhase == 3 then
               actionChance[9] = 20  -- explosion
            else
               actionChance[9] = 0  -- explosion
            end
            if bossPhase >= 2 then
               actionChance[10] = 20  -- hyper combo
            elseif bossPhase >= 1 then
               actionChance[10] = 10  -- hyper combo
            else
               actionChance[10] = 0  -- hyper combo
            end
         else
            actionChance[1] = 25  -- melee combos
            actionChance[2] = 15  -- spin back, leap smash
            actionChance[3] = 5  -- roundhouse kick
            actionChance[4] = 0  -- grab
            actionChance[5] = 10  -- two-handed
            actionChance[6] = 0  -- running leap
            actionChance[7] = 15  -- spinning kick and backfist
            if bossPhase == 3 then
               actionChance[9] = 10  -- explosion
            else
               actionChance[9] = 0  -- explosion
            end
            if bossPhase >= 2 then
               actionChance[10] = 10  -- hyper combo
            elseif bossPhase >= 1 then
               actionChance[10] = 5  -- hyper combo
            else
               actionChance[10] = 0  -- hyper combo
            end
         end
      end
   end
   local actionFate = ai:GetRandam_Int(1, actionChance[1] + actionChance[2] + actionChance[3] + actionChance[4] + actionChance[5] + actionChance[6] + actionChance[7] + actionChance[8] + actionChance[9] + actionChance[10])

   if actionFate <= actionChance[1] then
      getWellSpaceOdds = Jareel530000_Act01(ai, goal)
   elseif actionFate <= actionChance[1] + actionChance[2] then
      getWellSpaceOdds = Jareel530000_Act02(ai, goal)
   elseif actionFate <= actionChance[1] + actionChance[2] + actionChance[3] then
      getWellSpaceOdds = Jareel530000_Act03(ai, goal)
   elseif actionFate <= actionChance[1] + actionChance[2] + actionChance[3] + actionChance[4] then
      getWellSpaceOdds = Jareel530000_Act04(ai, goal)
   elseif actionFate <= actionChance[1] + actionChance[2] + actionChance[3] + actionChance[4] + actionChance[5] then
      getWellSpaceOdds = Jareel530000_Act05(ai, goal)
   elseif actionFate <= actionChance[1] + actionChance[2] + actionChance[3] + actionChance[4] + actionChance[5] + actionChance[6] then
      getWellSpaceOdds = Jareel530000_Act06(ai, goal)
   elseif actionFate <= actionChance[1] + actionChance[2] + actionChance[3] + actionChance[4] + actionChance[5] + actionChance[6] + actionChance[7] then
      getWellSpaceOdds = Jareel530000_Act07(ai, goal)
   elseif actionFate <= actionChance[1] + actionChance[2] + actionChance[3] + actionChance[4] + actionChance[5] + actionChance[6] + actionChance[7] + actionChance[8] then
      getWellSpaceOdds = Jareel530000_Act08(ai, goal)
   elseif actionFate <= actionChance[1] + actionChance[2] + actionChance[3] + actionChance[4] + actionChance[5] + actionChance[6] + actionChance[7] + actionChance[8] + actionChance[9] then
      getWellSpaceOdds = Jareel530000_Act09(ai, goal)
   else
      getWellSpaceOdds = Jareel530000_Act10(ai, goal)
   end
   getWellFate = GetRandam_Int(1, 100)
   if getWellFate <= getWellSpaceOdds then
      Jareel530000_GetWellSpace_Act(ai, goal)
   end
end

Jareel530000_Act01 = function(ai, goal, _)
   -- Basic melee combos. Rarely ends with a roundhouse kick.
   local patternRoll = ai:GetRandam_Int(1, 100)
   local approachToDistance = localScriptConfigVar1
   local minRunDistance = localScriptConfigVar1 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   if patternRoll <= 5 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 25
      else
         GetWellSpace_Odds = 5
      end
   elseif patternRoll <= 20 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 50
      else
         GetWellSpace_Odds = 15
      end
   elseif patternRoll <= 50 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 80
      else
         GetWellSpace_Odds = 20
      end
   elseif patternRoll <= 70 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 50
      else
         GetWellSpace_Odds = 15
      end
   elseif patternRoll <= 90 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 80
      else
         GetWellSpace_Odds = 20
      end
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 100
      else
         GetWellSpace_Odds = 30
      end
   end
   -- goal:AddSubGoal(GOAL_COMMON_SidewayMove, 1.8, TARGET_ENE_0, ai:GetRandam_Int(0, 1), ai:GetRandam_Int(20, 30), true, true, -1)
   return GetWellSpace_Odds
end

Jareel530000_Act02 = function(ai, goal, _)
   -- Spinning backstep attack, sometimes followed by leaping smash.
   local randomPattern = ai:GetRandam_Int(1, 100)
   local approachToDistance = localScriptConfigVar1
   local minRunDistance = localScriptConfigVar1 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   if randomPattern <= 25 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3005, TARGET_ENE_0, DIST_Middle, 2, 45)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 15
      else
         GetWellSpace_Odds = 0
      end
   elseif randomPattern <= 75 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 50
      else
         GetWellSpace_Odds = 10
      end
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 80
      else
         GetWellSpace_Odds = 20
      end
   end
   return GetWellSpace_Odds
end

Jareel530000_Act03 = function(ai, goal, _)
   -- Roundhouse kick. Close range only.
   local approachToDistance = localScriptConfigVar1
   local minRunDistance = localScriptConfigVar1 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3004, TARGET_ENE_0, DIST_Middle, 2, 45)
   if ai:IsFinishTimer(0) then
      GetWellSpace_Odds = 50
   else
      GetWellSpace_Odds = 10
   end
   return GetWellSpace_Odds
end

Jareel530000_Act04 = function(ai, goal, _)
   -- Grab attack. Close range only.
   local approachToDistance = localScriptConfigVar7
   local minRunDistance = localScriptConfigVar7 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Middle, 2, 45)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

Jareel530000_Act05 = function(ai, goal)
   -- Two-handed swings, sometimes followed by backfist.
   local randomPattern = ai:GetRandam_Int(1, 100)
   local approachToDistance = localScriptConfigVar7
   local minRunDistance = localScriptConfigVar7 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   if randomPattern <= 30 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 2, 45)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 25
      else
         GetWellSpace_Odds = 0
      end
   elseif randomPattern <= 70 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 75
      else
         GetWellSpace_Odds = 25
      end
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3010, TARGET_ENE_0, DIST_Middle, 0)
      if ai:IsFinishTimer(0) then
         GetWellSpace_Odds = 100
      else
         GetWellSpace_Odds = 25
      end
   end
   return GetWellSpace_Odds
end

Jareel530000_Act06 = function(ai, goal)
   -- Running leap, sometimes followed by spinning backstep.
   local randomPattern = ai:GetRandam_Int(1, 100)
   local approachToDistance = localScriptConfigVar7
   local minRunDistance = localScriptConfigVar7 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   if randomPattern <= 60 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3007, TARGET_ENE_0, DIST_Middle, 2, 45)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3007, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
   end
   if ai:IsFinishTimer(0) then
      GetWellSpace_Odds = 80
   else
      GetWellSpace_Odds = 20
   end
   return GetWellSpace_Odds
end

Jareel530000_Act07 = function(ai, goal)
   -- Spinning kick followed by backfist and sometimes two-handed swing or another roundhouse.
   local randomPattern = ai:GetRandam_Int(1, 100)
   local approachToDistance = localScriptConfigVar1
   local minRunDistance = localScriptConfigVar1 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   if randomPattern <= 25 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3010, TARGET_ENE_0, DIST_Middle, 2, 45)
      GetWellSpace_Odds = 50
   elseif randomPattern <= 50 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3011, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3010, TARGET_ENE_0, DIST_Middle, 0)
      GetWellSpace_Odds = 50
   elseif randomPattern <= 75 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3011, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3010, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
      GetWellSpace_Odds = 100
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3011, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3010, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      GetWellSpace_Odds = 100
   end
end

Jareel530000_Act08 = function(ai, goal)
   -- Second grab attack - not sure if this one will do anything.
   local approachToDistance = localScriptConfigVar7
   local minRunDistance = localScriptConfigVar7 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Middle, 2, 45)
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

Jareel530000_Act09 = function(ai, goal)
   -- Explosion attack. Increases boss phase and increases speed for thirty seconds.
   local approachToDistance = localScriptConfigVar1
   local minRunDistance = localScriptConfigVar1 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3013, TARGET_ENE_0, DIST_Middle, 2, 45)
   ai:SetTimer(0, 30)  -- Increase speed (reduce recovery time) for thirty seconds
   local bossPhase = ai:GetNumber(0)
   if bossPhase < 3 then
      ai:SetNumber(0, bossPhase + 1)  -- Increment boss phase
   end
   GetWellSpace_Odds = 0
   return GetWellSpace_Odds
end

Jareel530000_Act10 = function(ai, goal, something)
   -- Hyper melee combo. Second/third phase only.
   local approachToDistance = localScriptConfigVar7
   local minRunDistance = localScriptConfigVar7 + 2
   local guardOdds = 0
   Approach_Act(ai, goal, approachToDistance, minRunDistance, guardOdds)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
   goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
   goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
   GetWellSpace_Odds = 100
   return GetWellSpace_Odds
end

Jareel530000_GetWellSpace_Act = function(ai, goal)
   local evadeFate = ai:GetRandam_Int(1, 100)
   if evadeFate <= 15 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 3)
   elseif evadeFate <= 22 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 3)
   elseif evadeFate <= 30 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 3)
   else
   end
end

Jareel530000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Jareel530000Battle_Terminate = function(ai, goal)
end

Jareel530000Battle_Interupt = function(ai, goal)
   local func6_var2 = ai:GetRandam_Int(1, 100)
   local func6_var3 = ai:GetRandam_Int(1, 100)
   local func6_var4 = ai:GetRandam_Int(1, 100)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local superStepDist = 3
   local superStepPer = 15
   local backStepPer = 60
   local leftStepPer = 20
   local rightStepPer = 20
   local safetyDist = 3.5
   if FindAttack_Step(ai, goal, superStepDist, superStepPer, backStepPer, leftStepPer, rightStepPer, safetyDist) then
      return true
   end
   local distDamagedStep = 3
   local oddsDamagedStep = 25
   local bkStepPer = 60
   local leftStepPer = 20
   local rightStepPer = 20
   local safetyDist = 3.5
   if Damaged_Step(ai, goal, distDamagedStep, oddsDamagedStep, oddsStep, bkStepPer, leftStepPer, rightStepPer, safetyDist) then
      return true
   end
   local distGuardBreak_Act = 5.6
   local oddsGuardBreak_Act = 30
   if GuardBreak_Act(ai, goal, distGuardBreak_Act, oddsGuardBreak_Act) then
      if enemyDistance <= 1 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Middle, 2, 45)
      elseif enemyDistance <= 2 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      else
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar7, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3007, TARGET_ENE_0, DIST_Middle, 2, 45)
      end
      return true
   end
   local distMissSwing_Int = 5.6
   local oddsMissSwing_Int = 30
   if MissSwing_Int(ai, goal, distMissSwing_Int, oddsMissSwing_Int) then
      if enemyDistance <= 2 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      else
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar7, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3007, TARGET_ENE_0, DIST_Middle, 2, 45)
      end
      return true
   end
   local distUseItem_Act = 5.6
   local oddsUseItem_Act = 60
   if UseItem_Act(ai, goal, distUseItem_Act, oddsUseItem_Act) then
      if enemyDistance <= 1 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Middle, 2, 45)
      elseif enemyDistance <= 2 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      else
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar7, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3007, TARGET_ENE_0, DIST_Middle, 2, 45)
      end
      return true
   end
   local func6_var34 = 5.6
   local func6_var35 = 18
   local func6_var36 = 0
   local func6_var37 = 50
   local func6_var38 = Shoot_2dist(ai, goal, func6_var34, func6_var35, func6_var36, func6_var37)
   if func6_var38 == 1 then
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, ai:GetRandam_Int(0, 1), ai:GetRandam_Int(30, 45),
         true, true, -1)
      return true
   elseif func6_var38 == 2 then
      if func6_var2 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, ai:GetRandam_Int(0, 1), ai:GetRandam_Int(30, 45),
            true, true, -1)
         return true
      elseif func6_var2 <= 75 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 4)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 4)
      end
      return true
   end
   local func6_var39 = 50
   local func6_var40 = 60
   local func6_var41 = 20
   local func6_var42 = 20
   local func6_var43 = 3.5
   if RebByOpGuard_Step(ai, goal, func6_var39, func6_var40, func6_var41, func6_var42, func6_var43) then
      return true
   end
   local func6_var44 = 5.6
   local func6_var45 = 60
   if SuccessGuard_Act(ai, goal, func6_var44, func6_var45) then
      if enemyDistance <= 2 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      else
         goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar7, TARGET_SELF, false, -1)
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3007, TARGET_ENE_0, DIST_Middle, 2, 45)
      end
      return true
   end
   return false
end
