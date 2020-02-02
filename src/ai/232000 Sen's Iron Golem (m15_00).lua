--@package: m15_00_00_00.luabnd, 232000_battle.lua
--@battle_goal: 232000, IronGolem232000Battle

--[[

3000: smash with axe (add fire).
3001: back swipe, right to left.
3002: low swipe, left to right.
3003: uppercut.
3004: double stomp with right foot.
3005: triple stomp with left foot.
3006: grab between legs.
3007: slam with fist.
3008: big back swipe (right to left).
3009: grab between legs from right side.
3010: U-shaped swipe.
3011: diagonal back swipe.
3012: throw air projectile.
3300: grab (part one).
3301: grab recovery.

]]--

local smashMinDistance = 3.8
local backswipeMinDistance = 4.2
local uppercutMinDistance = 3.1
local grabMinDistance = 3.8
local fistSlamMinDistance = 0.4
local scoopSwipeMinDistance = 0
local airBlastMinDistance = 30

local explosionCooldown = 15  -- affects smash and fist
local grabCooldown = 10
local stompCooldown = 10
local jumpCooldown = 10

IronGolem232000Battle_Activate = function(ai, goal)
   local func1_var2 = ai:GetRandam_Int(1, 100)
   local leftAttackFate = ai:GetRandam_Int(1, 100)
   local grabFate = ai:GetRandam_Int(1, 100)
   local fistSlamFate = ai:GetRandam_Int(1, 100)
   local sideGrabFate = ai:GetRandam_Int(1, 100)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)

   local smashOdds = 0
   local swipeOdds = 0
   local uppercutOdds = 0
   local rightStompOdds = 0
   local leftStompOdds = 0
   local grabOdds = 0
   local fistSlamOdds = 0
   local sideGrabOdds = 0
   local scoopOdds = 0
   local diagonalOdds = 0
   local airBlastOdds = 0
   local firstActionOdds = 0
   local doubleSwipeOdds = 0
   local jumpOdds = 0
   ai:AddObserveChrDmySphere(0, TARGET_ENE_0, 3, 1.4)
   ai:AddObserveChrDmySphere(1, TARGET_ENE_0, 30, 1.4)
   ai:AddObserveChrDmySphere(2, TARGET_ENE_0, 4, 1.4)
   ai:AddObserveChrDmySphere(3, TARGET_ENE_0, 40, 1.4)

   local firstActionDone = ai:GetNumber(0)

   local grabOddsMultiplier = 1
   if ai:IsFinishTimer(0) == false then
      grabOddsMultiplier = 0.1
   end

   local stompOddsMultiplier = 1
   if ai:IsFinishTimer(1) == false then
      stompOddsMultiplier = 0.2
   end

   local explosionOddsMultiplier = 1
   if ai:IsFinishTimer(2) == false then
      explosionOddsMultiplier = 0
   end

   local jumpOddsMultiplier = 1
   if ai:IsFinishTimer(3) == false then
      jumpOddsMultiplier = 0
   end

   local swipeOddsMultiplier = 1
   if ai:IsInsideTargetRegion(TARGET_ENE_0, 1502730) then
      -- Never swipes if player is standing somewhere particular.
      swipeOddsMultiplier = 0
   end

   -- ODDS

   if firstActionDone == 0 then
      firstActionOdds = 100
   elseif ai:IsInsideObserve(0) or ai:IsInsideObserve(1) and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 120) and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 180) and func1_var2 <= 75 * stompOddsMultiplier then
      rightStompOdds = 100
   elseif ai:IsInsideObserve(2) or ai:IsInsideObserve(3) and leftAttackFate <= 75 * stompOddsMultiplier then
      leftStompOdds = 50
      diagonalOdds = 50
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 30) and enemyDistance >= 0 and enemyDistance <= 4 and grabFate <= 75 * grabOddsMultiplier then
      grabOdds = 100
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 30) and enemyDistance >= -1.5 and enemyDistance <= 1.5 and fistSlamFate <= 60 * explosionOddsMultiplier then
      fistSlamOdds = 100
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 50) and enemyDistance >= -1.5 and enemyDistance <= 1.5 and sideGrabFate <= 75 * grabOddsMultiplier then
      sideGrabOdds = 100
   elseif enemyDistance >= 12 then
      smashOdds = 5 * explosionOddsMultiplier
      swipeOdds = 10 * swipeOddsMultiplier
      uppercutOdds = 5
      airBlastOdds = 50
      doubleSwipeOdds = 30
   elseif enemyDistance >= 6 then
      smashOdds = 30 * explosionOddsMultiplier
      swipeOdds = 45 * swipeOddsMultiplier
      uppercutOdds = 15
      grabOdds = 10 * grabOddsMultiplier
   elseif enemyDistance >= 3 then
      smashOdds = 20 * explosionOddsMultiplier
      swipeOdds = 35 * swipeOddsMultiplier
      uppercutOdds = 10
      grabOdds = 15 * grabOddsMultiplier
      jumpOdds = 20 * jumpOddsMultiplier
   elseif enemyDistance >= 1.4 then
      smashOdds = 5 * explosionOddsMultiplier
      swipeOdds = 10 * swipeOddsMultiplier
      uppercutOdds = 10
      grabOdds = 25 * grabOddsMultiplier
      jumpOdds = 50 * jumpOddsMultiplier
   elseif enemyDistance >= -0.5 then
      if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 120) then
         grabOdds = 20 * grabOddsMultiplier
         fistSlamOdds = 15
         sideGrabOdds = 5 * grabOddsMultiplier
         scoopOdds = 10
         jumpOdds = 300 * jumpOddsMultiplier
      else
         grabOdds = 20 * grabOddsMultiplier
         fistSlamOdds = 15
         sideGrabOdds = 5 * grabOddsMultiplier
         scoopOdds = 10
         jumpOdds = 50 * jumpOddsMultiplier
      end
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 120) then
      fistSlamOdds = 10 * explosionOddsMultiplier
      sideGrabOdds = 10 * grabOddsMultiplier
      scoopOdds = 10
      jumpOdds = 300 * jumpOddsMultiplier
      rightStompOdds = 5 * stompOddsMultiplier
      leftStompOdds = 5 * stompOddsMultiplier
   else
      fistSlamOdds = 10 * explosionOddsMultiplier
      sideGrabOdds = 10 * grabOddsMultiplier
      scoopOdds = 10
      jumpOdds = 70 * jumpOddsMultiplier
      rightStompOdds = 5 * stompOddsMultiplier
      leftStompOdds = 5 * stompOddsMultiplier
   end
   if ai:IsInsideObserve(0) or ai:IsInsideObserve(1) then
      sideGrabOdds = 200
   end
   local fate = ai:GetRandam_Int(1, smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds + grabOdds + fistSlamOdds + sideGrabOdds + scoopOdds + diagonalOdds + airBlastOdds + firstActionOdds + doubleSwipeOdds + jumpOdds)
   if fate <= smashOdds then
      IronGolem232000_Act00(ai, goal)
   elseif fate <= smashOdds + swipeOdds then
      IronGolem232000_Act01(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds then
      IronGolem232000_Act02(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds then
      IronGolem232000_Act03(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds then
      IronGolem232000_Act04(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds + grabOdds then
      IronGolem232000_Act05(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds + grabOdds + fistSlamOdds then
      IronGolem232000_Act06(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds + grabOdds + fistSlamOdds + sideGrabOdds then
      IronGolem232000_Act07(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds + grabOdds + fistSlamOdds + sideGrabOdds + scoopOdds then
      IronGolem232000_Act08(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds + grabOdds + fistSlamOdds + sideGrabOdds + scoopOdds + diagonalOdds then
      IronGolem232000_Act09(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds + grabOdds + fistSlamOdds + sideGrabOdds + scoopOdds + diagonalOdds + airBlastOdds then
      IronGolem232000_Act10(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds + grabOdds + fistSlamOdds + sideGrabOdds + scoopOdds + diagonalOdds + airBlastOdds + firstActionOdds then
      IronGolem232000_Act11(ai, goal)
   elseif fate <= smashOdds + swipeOdds + uppercutOdds + rightStompOdds + leftStompOdds + grabOdds + fistSlamOdds + sideGrabOdds + scoopOdds + diagonalOdds + airBlastOdds + firstActionOdds + doubleSwipeOdds then
      IronGolem232000_Act12(ai, goal)
   else
      IronGolem232000_Act13(ai, goal)
   end
end

IronGolem232000_Act00 = function(ai, goal)
   -- Smash, maybe with one swipe.
   local fate = ai:GetRandam_Int(1, 100)
   ai:SetTimer(2, explosionCooldown)
   Approach_Act(ai, goal, smashMinDistance, smashMinDistance, 0)
   if fate <= 70 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 2, 45)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
   end
end

IronGolem232000_Act01 = function(ai, goal)
   -- Backswipes.
   local fate = ai:GetRandam_Int(1, 100)
   Approach_Act(ai, goal, backswipeMinDistance, backswipeMinDistance, 0)
   if fate <= 75 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_Far, 2, 90)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_Far, 2, 90)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3008, TARGET_ENE_0, DIST_Middle, 0)
   end
end

IronGolem232000_Act02 = function(ai, goal)
   -- Uppercut.
   Approach_Act(ai, goal, uppercutMinDistance, uppercutMinDistance, 0)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_Middle, 2, 30)
end

IronGolem232000_Act03 = function(ai, goal)
   -- Double stomp with right foot. 15 second cooldown.
   ai:SetTimer(1, stompCooldown)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3004, TARGET_ENE_0, DIST_Near, 0, 180)
end

IronGolem232000_Act04 = function(ai, goal)
   -- Triple stomp with left foot. 15 second cooldown.
   ai:SetTimer(1, stompCooldown)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3005, TARGET_ENE_0, DIST_Near, 0, 180)
end

IronGolem232000_Act05 = function(ai, goal)
   -- Grab between legs.
   Approach_Act(ai, goal, grabMinDistance, grabMinDistance, 0)
   ai:SetTimer(0, grabCooldown)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3006, TARGET_ENE_0, DIST_Middle, 2, 30)
end

IronGolem232000_Act06 = function(ai, goal)
   -- Slam with fist.
   ai:SetTimer(2, explosionCooldown)
   Approach_Act(ai, goal, fistSlamMinDistance, fistSlamMinDistance, 0)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3007, TARGET_ENE_0, DIST_Middle, 2, 30)
end

IronGolem232000_Act07 = function(ai, goal)
   -- Grab between legs from right side. 25 second cooldown.
   ai:SetTimer(0, grabCooldown)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3009, TARGET_ENE_0, DIST_Middle, 0, 180)
end

IronGolem232000_Act08 = function(ai, goal)
   -- Scooping swipe.
   Approach_Act(ai, goal, scoopSwipeMinDistance, scoopSwipeMinDistance, 0)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3010, TARGET_ENE_0, DIST_Near, 2, 90)
end

IronGolem232000_Act09 = function(ai, goal)
   -- Diagonal swipe. 15 second cooldown shared with left stomp.
   ai:SetTimer(1, stompCooldown)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3011, TARGET_ENE_0, DIST_Near, 0, 180)
end

IronGolem232000_Act10 = function(ai, goal)
   -- Air blast.
   Approach_Act(ai, goal, airBlastMinDistance, airBlastMinDistance, 0)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_None, -1, 20)
end

IronGolem232000_Act11 = function(ai, goal)
   -- Initial action: approach, use air blast, approach, backswipe.
   ai:SetNumber(0, 1)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 30, TARGET_ENE_0, airBlastMinDistance, TARGET_SELF, false, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_None, -1, 20)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, backswipeMinDistance, TARGET_SELF, false, -1)
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_Far, 2, 90)
   goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3008, TARGET_ENE_0, DIST_Middle, 0)
end

IronGolem232000_Act12 = function(ai, goal)
   -- Swipe and backswipe.
   local minDistance = 8.5
   Approach_Act(ai, goal, minDistance, minDistance, 0)
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_Far, 2, 90)
   goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3008, TARGET_ENE_0, DIST_Middle, 0)
end

IronGolem232000_Act13 = function(ai, goal)
   -- Jump backward.
   ai:SetTimer(3, jumpCooldown)
   goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 6)
end

IronGolem232000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

IronGolem232000Battle_Terminate = function(ai, goal)
end

IronGolem232000Battle_Interupt = function(ai, goal)
   local func18_var6 = 20
   local func18_var7 = 50
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   if UseItem_Act(ai, goal, func18_var6, func18_var7) then
      if enemyDistance >= 12 then
         IronGolem232000_Act10(ai, goal)
      elseif enemyDistance >= 8.5 then
         IronGolem232000_Act12(ai, goal)
      elseif enemyDistance >= 4.1 then
         IronGolem232000_Act01(ai, goal)
      elseif enemyDistance >= 0 then
         if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 120) then
            IronGolem232000_Act13(ai, goal)
         else
            IronGolem232000_Act05(ai, goal)
         end
      else
         IronGolem232000_Act13(ai, goal)
      end
      -- Tried to add an 'end' here but it's incorrect
      return true
   end
   return false
end


