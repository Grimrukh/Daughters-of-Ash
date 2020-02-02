--@package: m15_01_00_00.luabnd, 537001_battle.lua
--@battle_goal: 537001, FirewoodKing537001Battle

-- One-handed combos
local attack3000_Dist_Min = 0
local attack3000_Dist_Max = 3.2

-- Sunlight Spear
local spear_Dist_Min = 7
local spear_Dist_Max = 10.7

-- Thrust
local attack3008_Dist_Min = 0
local attack3008_Dist_Max = 9.1

-- Strong slash
local attack3010_Dist_Min = 8
local attack3010_Dist_Max = 9.3

-- Two-handed combos
local attack3012_Dist_Min = 0
local attack3012_Dist_Max = 3.9

-- Short leap
local attack3018_Dist_Min = 11.5
local attack3018_Dist_Max = 13.7

-- Long leap
local attack3019_Dist_Min = 14
local attack3019_Dist_Max = 16

-- Spin slash TODO: restore
local attack3020_Dist_Min = 0
local attack3020_Dist_Max = 2.4

-- Kick
local attack3021_Dist_Min = 0
local attack3021_Dist_Max = 2.8

-- TODO: unused (use with explosion)
local attack3022_Dist_Min = 7
local attack3022_Dist_Max = 10.4

local Suki = 1.8


FirewoodKing537001Battle_Activate = function(ai, goal)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local selfHpRate = ai:GetHpRate(TARGET_SELF)
   local breakGuardOdds = ai:GetRandam_Int(1, 100)
   local darkPhase = ai:GetEventRequest(0)
   local act01Odds = 0  -- One-handed combos
   local act02Odds = 0  -- Sunlight Spear (single or triple) (triple is second phase only)
   local act03Odds = 0  -- Thrust
   local act04Odds = 0  -- Dashing slash
   local act05Odds = 0  -- Two-handed combos
   local act06Odds = 0  -- Short leaping slash
   local act07Odds = 0  -- Far leaping slash
   local act08Odds = 0  -- Spin slash and jump back (more often in second phase)
   local act09Odds = 0  -- Kick
   local act10Odds = 0  -- Deflect and summon Sunlight Storm (dark phase only)
   local getWellOdds = 100
   local spearOddsMultiplier = 2
   local stormOddsMultiplier = 0

   if selfHpRate <= 0.5 or darkPhase == 1 then
      spearOddsMultiplier = 3
      getWellOdds = 50
   end

   if darkPhase == 1 and ai:IsFinishTimer(0) then
      stormOddsMultiplier = 1
   end

   if ai:GetNumber(0) == 0 then
      -- Always begin battle with far leaping slash.
      act07Odds = 100
      ai:SetNumber(0, 1)
   elseif ai:IsTargetGuard(TARGET_ENE_0) == true and breakGuardOdds <= 70 and enemyDistance <= 5 then
      -- Kick to break guard, or rarely use Sunlight Spear.
      act02Odds = 10 * spearOddsMultiplier
      act09Odds = 90
   elseif enemyDistance >= 15 then
      -- Target is very far away. Use Sunlight Spear, short leap, or (most likely) far leap.
      act02Odds = 30 * spearOddsMultiplier
      act06Odds = 20
      act07Odds = 50
      act10Odds = 25 * stormOddsMultiplier
   elseif enemyDistance >= 12 then
      -- Target is quite far away. Use dashing slash, Sunlight Spear, short leap (most likely), or far leap.
      act02Odds = 25 * spearOddsMultiplier
      act04Odds = 10
      act06Odds = 45
      act07Odds = 10
      act10Odds = 50 * stormOddsMultiplier
   elseif enemyDistance >= 10 then
      -- Target is at medium range. Use Sunlight Spear, thrust, dashing slash, or short leap.
      act02Odds = 20 * spearOddsMultiplier
      act03Odds = 25
      act04Odds = 30
      act06Odds = 25
      act10Odds = 50 * stormOddsMultiplier
   elseif enemyDistance >= 7 then
      -- Target is almost in melee range. Use one-handed, thrust, dash, two-handed, or short leap.
      if selfHpRate <= 0.5 or darkPhase == 1 then
         -- (PHASE 2) Target is almost in melee range. Use one-handed, spear, thrust, dash, two-handed, or short leap.
         act01Odds = 10
         act02Odds = 10 * spearOddsMultiplier
         act03Odds = 25
         act04Odds = 15
         act05Odds = 15
         act06Odds = 25
         act08Odds = 10
         act10Odds = 50 * stormOddsMultiplier
      else
         -- (PHASE 1) No spin back or spear.
         act01Odds = 10
         act03Odds = 30
         act04Odds = 15
         act05Odds = 15
         act06Odds = 30
      end
   elseif enemyDistance >= 4 then
      if selfHpRate <= 0.5 or darkPhase == 1 then
         -- (PHASE 2) Outer melee range. Use slashes or thrust, or spin.
         act01Odds = 23
         act03Odds = 15
         act05Odds = 32
         act10Odds = 50 * stormOddsMultiplier
      else
         -- (PHASE 1) No spin.
         act01Odds = 23
         act03Odds = 15
         act05Odds = 32
      end
   else
      if selfHpRate <= 0.5 or darkPhase == 1 then
         -- (PHASE 2) Close melee range. Use slashes, spin, or deflect.
         act01Odds = 35
         act05Odds = 35
         act08Odds = 20
         act10Odds = 30 * stormOddsMultiplier
      else
         -- (PHASE 1) No spin or deflect.
         act01Odds = 50
         act05Odds = 50
      end
   end

   local fate = ai:GetRandam_Int(1, act01Odds + act02Odds + act03Odds + act04Odds + act05Odds + act06Odds + act07Odds + act08Odds + act09Odds + act10Odds)
   if fate <= act01Odds then
      FirewoodKing537001_Act01(ai, goal)
   elseif fate <= act01Odds + act02Odds then
      FirewoodKing537001_Act02(ai, goal)
   elseif fate <= act01Odds + act02Odds + act03Odds then
      FirewoodKing537001_Act03(ai, goal)
   elseif fate <= act01Odds + act02Odds + act03Odds + act04Odds then
      FirewoodKing537001_Act04(ai, goal)
   elseif fate <= act01Odds + act02Odds + act03Odds + act04Odds + act05Odds then
      FirewoodKing537001_Act05(ai, goal)
   elseif fate <= act01Odds + act02Odds + act03Odds + act04Odds + act05Odds + act06Odds then
      FirewoodKing537001_Act06(ai, goal)
   elseif fate <= act01Odds + act02Odds + act03Odds + act04Odds + act05Odds + act06Odds + act07Odds then
      FirewoodKing537001_Act07(ai, goal)
   elseif fate <= act01Odds + act02Odds + act03Odds + act04Odds + act05Odds + act06Odds + act07Odds + act08Odds then
      FirewoodKing537001_Act08(ai, goal)
   elseif fate <= act01Odds + act02Odds + act03Odds + act04Odds + act05Odds + act06Odds + act07Odds + act08Odds + act09Odds then
      FirewoodKing537001_Act09(ai, goal)
   else
      FirewoodKing537001_Act10(ai, goal)
   end

   local getWellFate = ai:GetRandam_Int(1, 100)
   if getWellFate <= getWellOdds then
      FirewoodKing537001_GetWellSpace_Act(ai, goal)
   end
end

FirewoodKing537001_Act01 = function(ai, goal, func2_param2)
   -- Various permutations of 1/2/3/4 hit one-handed sword combos.
   -- TODO: Testing combinations of one and two handed attacks.
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local selfHpRate = ai:GetHpRate(TARGET_SELF)
   local fate = 0
   local darkPhase = ai:GetEventRequest(0)
   if selfHpRate <= 0.5 or darkPhase == 1 then
      fate = ai:GetRandam_Int(1, 100)
   else
      fate = ai:GetRandam_Int(1, 60)
   end
   local dodgeDirection = ai:GetRandam_Int(0, 1)
   local distMax = attack3000_Dist_Max
   local dashDist = attack3000_Dist_Max + 0.5
   if dashDist <= enemyDistance then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, distMax, TARGET_SELF, false, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, distMax, TARGET_SELF, true, -1)
   end
   if fate <= 5 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, -1, 20)
   elseif fate <= 15 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
   elseif fate <= 25 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
   elseif fate <= 35 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
   elseif fate <= 50 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3002, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)elseif fate <= 55 then
   elseif fate <= 60 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3004, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
   -- Remaining options are phase two only.
   elseif fate <= 70 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3013, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3016, TARGET_ENE_0, DIST_Middle, 0)
   elseif fate <= 80 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3002, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3013, TARGET_ENE_0, DIST_Middle, 0)
   elseif fate <= 90 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3020, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3013, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3004, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3015, TARGET_ENE_0, DIST_Middle, 0)
   end
   goal:AddSubGoal(GOAL_COMMON_SidewayMove, Suki, TARGET_ENE_0, dodgeDirection, ai:GetRandam_Int(20, 30), true, true, -1)
   GetWellSpace_Odds = 0
end

FirewoodKing537001_Act02 = function(ai, goal, func3_param2)
   -- Sunlight Spear (single or triple)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local selfHpRate = ai:GetHpRate(TARGET_SELF)
   local fate = ai:GetRandam_Int(1, 100)
   local darkPhase = ai:GetEventRequest(0)
   local distMin = spear_Dist_Min
   if enemyDistance < distMin then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 3)
   end
   if selfHpRate <= 0.5 or darkPhase == 1 then
      if fate <= 75 then
         -- Triple Spear
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3023, TARGET_ENE_0, DIST_Middle, -1, 20)
      else
         -- Single Spear
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3006, TARGET_ENE_0, DIST_Middle, -1, 20)
      end
   else
      -- Single Spear only
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3006, TARGET_ENE_0, DIST_Middle, -1, 20)
   end
   GetWellSpace_Odds = 0
end

FirewoodKing537001_Act03 = function(ai, goal, func4_param2)
   -- One-handed thrust, with optional follow-up swipe.
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local fate = ai:GetRandam_Int(1, 100)
   local dodgeDirection = ai:GetRandam_Int(0, 1)
   local distMax = attack3008_Dist_Max
   local dastDist = attack3008_Dist_Max + 0.5
   if dastDist <= enemyDistance then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, distMax, TARGET_SELF, false, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, distMax, TARGET_SELF, true, -1)
   end
   if fate <= 60 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, -1, 20)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Near, -1, 20)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
   end
   goal:AddSubGoal(GOAL_COMMON_SidewayMove, Suki, TARGET_ENE_0, dodgeDirection, ai:GetRandam_Int(20, 30), true, true, -1)
   GetWellSpace_Odds = 0
end

FirewoodKing537001_Act04 = function(ai, goal, func5_param2)
   -- Step and slash, with optional two-handed backslash.
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local fate = ai:GetRandam_Int(1, 100)
   local dodgeDirection = ai:GetRandam_Int(0, 1)
   local distMax = attack3010_Dist_Max
   local dashDist = attack3010_Dist_Max + 0.5
   if dashDist <= enemyDistance then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, distMax, TARGET_SELF, false, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, distMax, TARGET_SELF, true, -1)
   end
   if fate <= 10 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3010, TARGET_ENE_0, DIST_Middle, -1, 25)
      GetWellSpace_Odds = 100
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3010, TARGET_ENE_0, DIST_Near, -1, 25)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3011, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, Suki, TARGET_ENE_0, dodgeDirection, ai:GetRandam_Int(20, 30), true, true, -1)
      GetWellSpace_Odds = 0
   end
end

FirewoodKing537001_Act05 = function(ai, goal, func6_param2)
   -- Various two-handed combos.
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local fate = ai:GetRandam_Int(1, 100)
   local dodgeDistance = ai:GetRandam_Int(0, 1)
   local distMax = attack3012_Dist_Max
   local dashDist = attack3012_Dist_Max + 0.5
   if dashDist <= enemyDistance then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, distMax, TARGET_SELF, false, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, distMax, TARGET_SELF, true, -1)
   end
   if fate <= 5 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Middle, -1, 40)
      GetWellSpace_Odds = 100
   elseif fate <= 10 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Near, -1, 40)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3013, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, Suki, TARGET_ENE_0, dodgeDistance, ai:GetRandam_Int(20, 30), true, true, -1)
      GetWellSpace_Odds = 0
   elseif fate <= 40 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Near, -1, 40)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3013, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3016, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, Suki, TARGET_ENE_0, dodgeDistance, ai:GetRandam_Int(20, 30), true, true, -1)
      GetWellSpace_Odds = 0
   elseif fate <= 70 then
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Near, -1, 40)
      goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3013, TARGET_ENE_0, DIST_Near, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3014, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, Suki, TARGET_ENE_0, dodgeDistance, ai:GetRandam_Int(20, 30), true, true, -1)
      GetWellSpace_Odds = 0
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Near, -1, 40)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3015, TARGET_ENE_0, DIST_Middle, 0)
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, Suki, TARGET_ENE_0, dodgeDistance, ai:GetRandam_Int(20, 30), true, true, -1)
      GetWellSpace_Odds = 0
   end
end

FirewoodKing537001_Act06 = function(ai, goal, func7_param2)
   -- Leaping slash (near version)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local dodgeDirection = ai:GetRandam_Int(0, 1)
   local distMax = attack3018_Dist_Max
   local dashDist = attack3018_Dist_Max + 0.5
   if dashDist <= enemyDistance then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, distMax, TARGET_SELF, false, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, distMax, TARGET_SELF, true, -1)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3018, TARGET_ENE_0, DIST_Middle, -1, 25)
   goal:AddSubGoal(GOAL_COMMON_SidewayMove, Suki, TARGET_ENE_0, dodgeDirection, ai:GetRandam_Int(20, 30), true, true, -1)
   GetWellSpace_Odds = 0
end

FirewoodKing537001_Act07 = function(ai, goal, func8_param2)
   -- Leaping slash (far version)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local dodgeDirection = ai:GetRandam_Int(0, 1)
   local distMax = attack3019_Dist_Max
   local dashDist = attack3019_Dist_Max + 0.5
   if dashDist <= enemyDistance then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, distMax, TARGET_SELF, false, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, distMax, TARGET_SELF, true, -1)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3019, TARGET_ENE_0, DIST_Middle, -1, 25)
   goal:AddSubGoal(GOAL_COMMON_SidewayMove, Suki, TARGET_ENE_0, dodgeDirection, ai:GetRandam_Int(20, 30), true, true, -1)
   GetWellSpace_Odds = 0
end

FirewoodKing537001_Act08 = function(ai, goal, func9_param2)
   -- Spin slash and jump back.
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local distMax = attack3020_Dist_Max
   local dashDist = attack3020_Dist_Max + 0.5
   if dashDist <= enemyDistance then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, distMax, TARGET_SELF, false, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, distMax, TARGET_SELF, true, -1)
   end
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3020, TARGET_ENE_0, DIST_Middle, 0)
   GetWellSpace_Odds = 0
end

FirewoodKing537001_Act09 = function(ai, goal, func10_param2)
   -- Kick attack.
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local distMax = attack3021_Dist_Max
   local dashDist = attack3021_Dist_Max + 0.5
   if dashDist <= enemyDistance then
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 5, TARGET_ENE_0, distMax, TARGET_SELF, false, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, distMax, TARGET_SELF, true, -1)
   end
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3021, TARGET_ENE_0, DIST_Middle, -1, 20)
   GetWellSpace_Odds = 100
end

FirewoodKing537001_Act10 = function(ai, goal, func10_param2)
   -- Deflect and Sunlight Storm (no more frequently than every 30 seconds; dark phase only).
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3017, TARGET_ENE_0, DIST_Near, -1, 20)
   ai:SetTimer(0, 30)
   GetWellSpace_Odds = 100
end

FirewoodKing537001_GetWellSpace_Act = function(ai, goal)
   local directionOdds = ai:GetRandam_Int(1, 100)
   if directionOdds <= 15 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 3)
   elseif directionOdds <= 22 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 3)
   elseif directionOdds <= 30 then
      goal:AddSubGoal(GOAL_COMMON_SpinStep, 10, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 3)
   end
end

FirewoodKing537001Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

FirewoodKing537001Battle_Terminate = function(ai, goal)
end

FirewoodKing537001Battle_Interupt = function(ai, goal)
   local fate = ai:GetRandam_Int(1, 100)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local selfHpRate = ai:GetHpRate(TARGET_SELF)
   local darkPhase = ai:GetEventRequest(0)
   local func14_var6 = 4
   local func14_var7 = 15
   local func14_var8 = 50
   local func14_var9 = 25
   local func14_var10 = 25
   local func14_var11 = 5
   if FindAttack_Step(ai, goal, func14_var6, func14_var7, func14_var8, func14_var9, func14_var10, func14_var11) then
      if selfHpRate <= 0.5 or darkPhase == 1 then
         if fate <= 40 then
            goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3017, TARGET_ENE_0, DIST_Middle, -1, 25)
         end
      end
      return true
   end
   local func14_var12 = 4
   local func14_var13 = 80
   if GuardBreak_Act(ai, goal, func14_var12, func14_var13) then
      if fate <= 40 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, -1, 25)
      elseif fate <= 65 then
         goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 25)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      elseif fate <= 85 then
         goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 25)
         goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Near, -1, 25)
         goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3001, TARGET_ENE_0, DIST_Near, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboRepeat, 10, 3002, TARGET_ENE_0, DIST_Near, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local func14_var14 = 9.3
   local func14_var15 = 80
   if MissSwing_Int(ai, goal, func14_var14, func14_var15) then
      if enemyDistance >= 8 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3010, TARGET_ENE_0, DIST_Middle, 0)
      elseif enemyDistance >= 3.9 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3008, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3012, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local func14_var16 = 9.3
   local func14_var17 = 40
   if UseItem_Act(ai, goal, func14_var16, func14_var17) then
      if enemyDistance >= 12 then
         if selfHpRate <= 0.5 or darkPhase == 1 then
            goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3023, TARGET_ENE_0, DIST_Middle, 0)
         else
            goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3006, TARGET_ENE_0, DIST_Middle, 0)
         end
      elseif enemyDistance >= 8 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3010, TARGET_ENE_0, DIST_Middle, 0)
      elseif enemyDistance >= 3.9 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3008, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_Near, -1, 40)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3013, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local func14_var18 = 0.5
   local func14_var19 = 25
   local func14_var20 = 0
   local func14_var21 = 100
   local func14_var22 = Shoot_2dist(ai, goal, func14_var18, func14_var19, func14_var20, func14_var21)
   if func14_var22 == 1 then
      if fate <= 50 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 3)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 3)
      end
      return true
   elseif func14_var22 == 2 then
      if fate <= 50 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 3)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 3)
      end
   end
   local func14_var23 = 35
   local func14_var24 = 50
   local func14_var25 = 25
   local func14_var26 = 25
   local func14_var27 = 3
   if RebByOpGuard_Step(ai, goal, func14_var23, func14_var24, func14_var25, func14_var26, func14_var27) then
      if selfHpRate <= 0.5 or darkPhase == 1 then
         if fate <= 20 then
            goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3017, TARGET_ENE_0, DIST_Middle, -1, 25)
         end
      end
      return true
   end
   return false
end


