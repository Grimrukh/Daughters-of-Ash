--@package: m10_00_00_00.luabnd, 526000_battle.lua
--@battle_goal: 526000, Donsyoku526000Battle

--[[

3000: Right side grab.
3001: Triple stomp with front left foot.
3002: Front left foot swipe.
3003: Body slam.
3004: Charge.
3005: Tail swipe.
3006: Tail swipe.
3007: Jump up.
3008: Acid.
3009: Long jump.
3010: Left side grab.
3300: Grab animation.
]]--

local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 4
local localScriptConfigVar2 = 0
local localScriptConfigVar3 = 1.5
local localScriptConfigVar4 = 0
local localScriptConfigVar5 = 4
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 6
local localScriptConfigVar8 = 0
local localScriptConfigVar9 = 8
local localScriptConfigVar10 = 0
local localScriptConfigVar11 = 8
local localScriptConfigVar12 = 0
local localScriptConfigVar13 = 5
local localScriptConfigVar14 = 0
local localScriptConfigVar15 = 25
local localScriptConfigVar16 = 8
local localScriptConfigVar17 = 14
local localScriptConfigVar18 = -6
local localScriptConfigVar19 = -3
Donsyoku526000Battle_Activate = function(ai, goal)
   local selfHpRate = ai:GetHpRate(TARGET_SELF)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local rightGrabOdds = 0
   local stompOdds = 0
   local swipeOdds = 0
   local slamChargeOdds = 0
   local tailSpinOdds = 0
   local leftGrabOdds = 0
   local jumpUpOdds = 0
   local acidOdds = 0
   local longJumpOdds = 0
   local turnSlamChargeOdds = 0
   local rightGrabMultiplier = 0
   local stompMultiplier = 0
   local swipeMultiplier = 0
   local slamChargeMultiplier = 0
   local tailSpinMultiplier = 0
   local leftGrabMultiplier = 0
   local jumpUpMultiplier = 0
   local acidMultiplier = 0
   local longJumpMultiplier = 0
   local turnSlamChargeMultiplier = 0
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 240) and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 120) and enemyDistance <= -0.5 then
      rightGrabMultiplier = 4
   end
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 120) and enemyDistance <= -3 then
      leftGrabMultiplier = 4
   end
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 45) and enemyDistance >= 0 and enemyDistance <= 2 then
      stompMultiplier = 1
   else
      stompMultiplier = 0.5
   end
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 90) and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_L, 200) and enemyDistance >= 0 and enemyDistance <= 5 then
      swipeMultiplier = 1.5
   else
      swipeMultiplier = 0.5
   end
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 45) and enemyDistance >= 0 and enemyDistance <= 5 then
      slamChargeMultiplier = 1.5
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 220) then
      slamChargeMultiplier = 0
   else
      slamChargeMultiplier = 0.5
   end
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_R, 240) and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 330) and enemyDistance >= 0 and enemyDistance <= 10 then
      tailSpinMultiplier = 2.5
   end
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 170) then
      if enemyDistance >= 2 then
         jumpUpMultiplier = 2.5
      else
         jumpUpMultiplier = 6
      end
   elseif enemyDistance <= 3 then
      jumpUpMultiplier = 1
   end
   if ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 45) and enemyDistance >= 8 and enemyDistance <= 14 then
      longJumpMultiplier = 1
   elseif enemyDistance >= 8 and enemyDistance <= 14 then
      longJumpMultiplier = 0.75
   elseif enemyDistance >= 4 and enemyDistance <= 8 then
      longJumpMultiplier = 0.25
   end
   ai:AddObserveChrDmySphere(0, TARGET_ENE_0, 120, 16)
   if ai:IsInsideObserve(0) and selfHpRate <= 0.6 and ai:IsFinishTimer(1) == true then
      acidMultiplier = 1
   end
   if enemyDistance >= 10 and enemyDistance <= 25 then
      turnSlamChargeMultiplier = 1.5
   elseif enemyDistance >= 10 then
      turnSlamChargeMultiplier = 1
   end

   if enemyDistance >= 10 then
      rightGrabOdds =      0 * rightGrabMultiplier
      stompOdds =          5 * stompMultiplier
      swipeOdds =          5 * swipeMultiplier
      slamChargeOdds =     5 * slamChargeMultiplier
      tailSpinOdds =       0 * tailSpinMultiplier
      leftGrabOdds =       0 * leftGrabMultiplier
      jumpUpOdds =         0 * jumpUpMultiplier
      acidOdds =           15 * acidMultiplier
      longJumpOdds =       15 * longJumpMultiplier
      turnSlamChargeOdds = 30 * turnSlamChargeMultiplier
   elseif enemyDistance >= 2 then
      rightGrabOdds =      0 * rightGrabMultiplier
      stompOdds =          30 * stompMultiplier
      swipeOdds =          30 * swipeMultiplier
      slamChargeOdds =     30 * slamChargeMultiplier
      tailSpinOdds =       15 * tailSpinMultiplier
      leftGrabOdds =       0 * leftGrabMultiplier
      jumpUpOdds =         15 * jumpUpMultiplier
      acidOdds =           15 * acidMultiplier
      longJumpOdds =       15 * longJumpMultiplier
      turnSlamChargeOdds = 0 * turnSlamChargeMultiplier
   else
      rightGrabOdds =      30 * rightGrabMultiplier
      stompOdds =          30 * stompMultiplier
      swipeOdds =          30 * swipeMultiplier
      slamChargeOdds =     30 * slamChargeMultiplier
      tailSpinOdds =       15 * tailSpinMultiplier
      leftGrabOdds =       30 * leftGrabMultiplier
      jumpUpOdds =         15 * jumpUpMultiplier
      acidOdds =           15 * acidMultiplier
      longJumpOdds =       0 * longJumpMultiplier
      turnSlamChargeOdds = 0 * turnSlamChargeMultiplier
   end
   local func1_var28 = ai:GetRandam_Int(1, rightGrabOdds + stompOdds + swipeOdds + slamChargeOdds + tailSpinOdds + leftGrabOdds + jumpUpOdds + acidOdds + longJumpOdds + turnSlamChargeOdds)
   if func1_var28 <= rightGrabOdds then
      Donsyoku_Act1(ai, goal)
   elseif func1_var28 <= rightGrabOdds + stompOdds then
      Donsyoku_Act2(ai, goal)
   elseif func1_var28 <= rightGrabOdds + stompOdds + swipeOdds then
      Donsyoku_Act3(ai, goal)
   elseif func1_var28 <= rightGrabOdds + stompOdds + swipeOdds + slamChargeOdds then
      -- Slam and charge (50%).
      Donsyoku_Act4(ai, goal)
   elseif func1_var28 <= rightGrabOdds + stompOdds + swipeOdds + slamChargeOdds + tailSpinOdds then
      Donsyoku_Act5(ai, goal)
   elseif func1_var28 <= rightGrabOdds + stompOdds + swipeOdds + slamChargeOdds + tailSpinOdds + leftGrabOdds then
      Donsyoku_Act6(ai, goal)
   elseif func1_var28 <= rightGrabOdds + stompOdds + swipeOdds + slamChargeOdds + tailSpinOdds + leftGrabOdds
           + jumpUpOdds then
      Donsyoku_Act7(ai, goal)
   elseif func1_var28 <= rightGrabOdds + stompOdds + swipeOdds + slamChargeOdds + tailSpinOdds + leftGrabOdds
           + jumpUpOdds + acidOdds then
      Donsyoku_Act8(ai, goal)
   elseif func1_var28 <= rightGrabOdds + stompOdds + swipeOdds + slamChargeOdds + tailSpinOdds + leftGrabOdds
           + jumpUpOdds + acidOdds + longJumpOdds then
      Donsyoku_Act9(ai, goal)
   else
      Donsyoku_Act10(ai, goal)
   end
end

Donsyoku_Act1 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 30, 3000, TARGET_ENE_0, DIST_Middle, 0)
end

Donsyoku_Act2 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar3, TARGET_SELF, true, -1)
   goal:AddSubGoal(GOAL_COMMON_Attack, 30, 3001, TARGET_ENE_0, DIST_Middle, 0)
end

Donsyoku_Act3 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar5, TARGET_SELF, true, -1)
   goal:AddSubGoal(GOAL_COMMON_Attack, 30, 3002, TARGET_ENE_0, DIST_Middle, 0)
end

Donsyoku_Act4 = function(ai, goal)
   local func5_var2 = ai:GetRandam_Int(1, 100)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, localScriptConfigVar7, TARGET_SELF, true, -1)
   if func5_var2 <= 50 then
      goal:AddSubGoal(GOAL_COMMON_Attack, 30, 3003, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttack_SuccessAngle180, 30, 3003, TARGET_ENE_0, 15, 0)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 30, 3004, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Donsyoku_Act5 = function(ai, goal)
   local func6_var2 = 0
   local func6_var3 = ai:GetPartsDmg(func6_var2)
   if func6_var3 == PARTS_DMG_FINAL then
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 30, 3006, TARGET_ENE_0, DIST_Middle, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 30, 3005, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Donsyoku_Act6 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 30, 3010, TARGET_ENE_0, DIST_Middle, 0)
end

Donsyoku_Act7 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 30, 3007, TARGET_ENE_0, DIST_Middle, 0, -1)
end

Donsyoku_Act8 = function(ai, goal)
   ai:SetTimer(1, 30)
   goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 30, 3008, TARGET_ENE_0, DIST_None, 0)
end

Donsyoku_Act9 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_Turn, 3, TARGET_ENE_0, 20, 0, 0)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 30, TARGET_ENE_0, localScriptConfigVar17, TARGET_SELF, true, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 30, 3009, TARGET_ENE_0, DIST_Middle, -1, 20)
end

Donsyoku_Act10 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_Turn, 3, TARGET_ENE_0, 20, 0, 0)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 10, TARGET_ENE_0, 25, TARGET_SELF, true, -1)
   goal:AddSubGoal(GOAL_COMMON_ComboAttack_SuccessAngle180, 30, 3003, TARGET_ENE_0, DIST_None, 0)
   goal:AddSubGoal(GOAL_COMMON_ComboFinal, 30, 3004, TARGET_ENE_0, DIST_Middle, 0)
end

Donsyoku526000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Donsyoku526000Battle_Terminate = function(ai, goal)
end

Donsyoku526000Battle_Interupt = function(ai, goal)
   local func14_var2 = ai:GetDist(TARGET_ENE_0)
   local func14_var3 = ai:GetRandam_Int(1, 100)
   local func14_var4 = ai:GetRandam_Int(1, 100)
   if ai:IsInterupt(INTERUPT_SuccessThrow) then
      goal:ClearSubGoal()
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, 0, 0, 0, 0)
      return true
   end
   if ai:IsInterupt(INTERUPT_Damaged) then
      local func14_var5 = ai:GetEventRequest(0)
      if func14_var5 == 1 and ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_F, 45) and func14_var2 <= 5
              and ai:IsFinishTimer(0) == true and func14_var3 <= 100 then
         ai:SetTimer(0, 30)
         goal:ClearSubGoal()
         if func14_var4 <= 25 then
            goal:AddSubGoal(GOAL_COMMON_Attack, 30, 3003, TARGET_ENE_0, DIST_Middle, 0)
         else
            goal:AddSubGoal(GOAL_COMMON_ComboAttack_SuccessAngle180, 30, 3003, TARGET_ENE_0, DIST_None, 0)
            goal:AddSubGoal(GOAL_COMMON_ComboFinal, 30, 3004, TARGET_ENE_0, DIST_Middle, 0)
         end
         return true
      end
   end
   return false
end


