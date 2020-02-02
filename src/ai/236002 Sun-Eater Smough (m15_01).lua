--@package: m15_01_00_00.luabnd, 236002_battle.lua
--@battle_goal: 236002, FourKnightC_Thunder236002Battle

-- Event 0: battle phase. -1 in first, 1 in second.
-- Number 0: 0 means the fade-out timer will be reset (then set to 1). Returned to 0 when fade-out attack is queued,
--           which can't be interrupted.

local localScriptConfigVar1 = 4.8
local localScriptConfigVar3 = 1
local localScriptConfigVar5 = 1.3
local localScriptConfigVar7 = 4
local localScriptConfigVar9 = 6.7
local localScriptConfigVar11 = 18
local localScriptConfigVar15 = 10.2
local smoughPhase1Time = 40
local smoughPhase2Time = 10
local smoughPhase2TimeWeak = 5

local swing1 = 3000
local swing2 = 3001
local bigSwing = 3002
local overheadSmash = 3003
local fastSmash = 3004
local swingAfterSmash = 3005
local jumpingSmash = 3006
local longCharge = 3007
local buttSlam = 3008
local shortCharge = 3009

OnIf_236002 = function(ai, goal, if_slot)
   local dodgeDirection = ai:GetRandam_Int(1, 100)
   if if_slot == 0 then
      if ai:IsInsideTarget(TARGET_FRI_0, AI_DIR_TYPE_R, 120) then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_NONE, 0, AI_DIR_TYPE_L, 3.7)
      elseif ai:IsInsideTarget(TARGET_FRI_0, AI_DIR_TYPE_L, 120) then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_NONE, 0, AI_DIR_TYPE_R, 3.7)
      elseif ai:IsInsideTarget(TARGET_FRI_0, AI_DIR_TYPE_F, 120) then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_FRI_0, 0, AI_DIR_TYPE_B, 4)
      elseif dodgeDirection <= 50 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_NONE, 0, AI_DIR_TYPE_L, 3.7)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_NONE, 0, AI_DIR_TYPE_R, 3.7)
      end
   end
end

FourKnightC_Thunder236002Battle_Activate = function(ai, goal)
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local selfHpRate = ai:GetHpRate(TARGET_SELF)
   ai:AddObserveArea(0, TARGET_FRI_0, TARGET_SELF, AI_DIR_TYPE_F, 360, 13)
   local jumpingSmashOdds = 0
   local basicComboOdds = 0
   local buttSlamOdds = 0
   local longChargeOdds = 0
   local shortChargeOdds = 0
   local bigSwingOdds = 0
   local overheadSlamOdds = 0
   local slamSwipeOdds = 0
   local getWellSpaceOdds = 0
   local getWellSpaceMultiplier = 1
   if enemyDistance >= 12 then
      jumpingSmashOdds = 25
      basicComboOdds = 15
      buttSlamOdds = 0
      longChargeOdds = 50
      shortChargeOdds = 0
      bigSwingOdds = 0
      overheadSlamOdds = 0
      slamSwipeOdds = 10
   elseif enemyDistance >= 6.7 then
      jumpingSmashOdds = 60
      basicComboOdds = 10
      buttSlamOdds = 0
      longChargeOdds = 0
      shortChargeOdds = 20
      bigSwingOdds = 0
      overheadSlamOdds = 0
      slamSwipeOdds = 10
   elseif enemyDistance >= 3.3 then
      jumpingSmashOdds = 20
      basicComboOdds = 20
      buttSlamOdds = 0
      longChargeOdds = 0
      shortChargeOdds = 40
      bigSwingOdds = 0
      overheadSlamOdds = 0
      slamSwipeOdds = 20
   elseif enemyDistance >= 1 then
      jumpingSmashOdds = 0
      basicComboOdds = 0
      buttSlamOdds = 25
      longChargeOdds = 0
      shortChargeOdds = 0
      bigSwingOdds = 37
      overheadSlamOdds = 38
      slamSwipeOdds = 0
   elseif ai:IsInsideTarget(TARGET_ENE_0, AI_DIR_TYPE_B, 150) then
      jumpingSmashOdds = 0
      basicComboOdds = 0
      buttSlamOdds = 60
      longChargeOdds = 0
      shortChargeOdds = 0
      bigSwingOdds = 20
      overheadSlamOdds = 20
      slamSwipeOdds = 0
   else
      jumpingSmashOdds = 0
      basicComboOdds = 0
      buttSlamOdds = 50
      longChargeOdds = 0
      shortChargeOdds = 0
      bigSwingOdds = 25
      overheadSlamOdds = 25
      slamSwipeOdds = 0
   end

   local battlePhase = ai:GetEventRequest(0)  -- Set to 1 when Ornstein is killed first.
   if battlePhase == -1 then
      jumpingSmashOdds = 0
   else
      getWellSpaceMultiplier = 0.5
   end

   if battlePhase == 1 and ai:GetNumber(1) == 0 then
      -- Restart fade timer prematurely at start of second phase.
      ai:SetTimer(0, smoughPhase2Time)
      ai:SetNumber(0, 1)
      ai:SetNumber(1, 1)
   elseif ai:IsFinishTimer(0) == true and ai:GetNumber(0) == 0 then
      -- Restart fade timer.
      if battlePhase == -1 then
         ai:SetTimer(0, smoughPhase1Time)
      elseif selfHpRate < 0.5 then
         ai:SetTimer(0, smoughPhase2TimeWeak)
      else
         ai:SetTimer(0, smoughPhase2Time)
      end
      ai:SetNumber(0, 1)  -- Disabled when fade command is given out, so timer can be reset.
   end

   -- TODO: getWellSpaceOdds varies with phase/health.
   local fate = ai:GetRandam_Int(1, jumpingSmashOdds + basicComboOdds + buttSlamOdds + longChargeOdds + shortChargeOdds
           + bigSwingOdds + overheadSlamOdds + slamSwipeOdds)
   if fate <= jumpingSmashOdds then
      FourKnightC_Thunder236002_Act01(ai, goal)
      getWellSpaceOdds = 100 * getWellSpaceMultiplier
   elseif fate <= jumpingSmashOdds + basicComboOdds then
      FourKnightC_Thunder236002_Act02(ai, goal)
      getWellSpaceOdds = 100 * getWellSpaceMultiplier
   elseif fate <= jumpingSmashOdds + basicComboOdds + buttSlamOdds then
      FourKnightC_Thunder236002_Act03(ai, goal)
      getWellSpaceOdds = 0
   elseif fate <= jumpingSmashOdds + basicComboOdds + buttSlamOdds + longChargeOdds then
      FourKnightC_Thunder236002_Act04(ai, goal)
      getWellSpaceOdds = 100 * getWellSpaceMultiplier
   elseif fate <= jumpingSmashOdds + basicComboOdds + buttSlamOdds + longChargeOdds + shortChargeOdds then
      FourKnightC_Thunder236002_Act05(ai, goal)
      getWellSpaceOdds = 100 * getWellSpaceMultiplier
   elseif fate <= jumpingSmashOdds + basicComboOdds + buttSlamOdds + longChargeOdds + shortChargeOdds + bigSwingOdds then
      FourKnightC_Thunder236002_Act06(ai, goal)
      getWellSpaceOdds = 100 * getWellSpaceMultiplier
   elseif fate <= jumpingSmashOdds + basicComboOdds + buttSlamOdds + longChargeOdds + shortChargeOdds + bigSwingOdds + overheadSlamOdds then
      FourKnightC_Thunder236002_Act07(ai, goal)
      getWellSpaceOdds = 100 * getWellSpaceMultiplier
   else
      FourKnightC_Thunder236002_Act08(ai, goal)
      getWellSpaceOdds = 100 * getWellSpaceMultiplier
   end
   local getWellFate = ai:GetRandam_Int(1, 100)
   if getWellFate <= getWellSpaceOdds then
      FourKnightC_Thunder236002_GetWellSpace_Act(ai, goal)
   end
end

FourKnightC_Thunder236002_Act01 = function(ai, goal, _)
   -- Jumping slam. SECOND PHASE ONLY.
   local fadeOut = ai:IsFinishTimer(0)
   Approach_Act(ai, goal, localScriptConfigVar9, localScriptConfigVar9 + 4, 0)
   if fadeOut then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3026, TARGET_ENE_0, DIST_Middle, 0)
      ai:SetNumber(0, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3006, TARGET_ENE_0, DIST_Middle, 0)
   end
end

FourKnightC_Thunder236002_Act02 = function(ai, goal, _)
   -- One or two hit combo.
   local fate = ai:GetRandam_Int(1, 100)
   local fadeOut = ai:IsFinishTimer(0)

   Approach_Act(ai, goal,  localScriptConfigVar1, localScriptConfigVar1 + 4, 0)
   if fate <= 40 then
      if fadeOut then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3020, TARGET_ENE_0, DIST_Middle, 0)
         ai:SetNumber(0, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
      end
   else
      if fadeOut then
         goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3020, TARGET_ENE_0, DIST_Middle, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 4001, TARGET_ENE_0, DIST_Middle, 0)
         ai:SetNumber(0, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3000, TARGET_ENE_0, DIST_Middle, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
      end
   end
end

FourKnightC_Thunder236002_Act03 = function(ai, goal, _)
   -- Butt slam.
   local fadeOut = ai:IsFinishTimer(0)
   if fadeOut then
      -- No fade-out butt slam. Uses short charge instead.
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3029, TARGET_ENE_0, DIST_Middle, 0, -1)
      ai:SetNumber(0, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3008, TARGET_ENE_0, DIST_Middle, 0, -1)
   end
end

FourKnightC_Thunder236002_Act04 = function(ai, goal, _)
   -- Long charge.
   local fadeOut = ai:IsFinishTimer(0)
   Approach_Act(ai, goal, localScriptConfigVar11, localScriptConfigVar11 + 4, 0)
   if fadeOut then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3027, TARGET_ENE_0, DIST_Middle, 0)
      ai:SetNumber(0, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3007, TARGET_ENE_0, DIST_Middle, 0)
   end
end

FourKnightC_Thunder236002_Act05 = function(ai, goal, _)
   -- Short charge.
   local fadeOut = ai:IsFinishTimer(0)
   Approach_Act(ai, goal, localScriptConfigVar15, localScriptConfigVar15 + 4, 0)
   if fadeOut then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3029, TARGET_ENE_0, DIST_Middle, 0)
      ai:SetNumber(0, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3009, TARGET_ENE_0, DIST_Middle, 0)
   end
end

FourKnightC_Thunder236002_Act06 = function(ai, goal, _)
   -- Big swing, right to left.
   local fadeOut = ai:IsFinishTimer(0)
   Approach_Act(ai, goal, localScriptConfigVar3, localScriptConfigVar3 + 4, 0)
   if fadeOut then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3022, TARGET_ENE_0, DIST_Middle, 0)
      ai:SetNumber(0, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3002, TARGET_ENE_0, DIST_Middle, 0)
   end
end

FourKnightC_Thunder236002_Act07 = function(ai, goal, _)
   -- Slow overhead smash.
   local fadeOut = ai:IsFinishTimer(0)
   Approach_Act(ai, goal, localScriptConfigVar5, localScriptConfigVar5 + 4, 0)
   if fadeOut then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3023, TARGET_ENE_0, DIST_Middle, 0)
      ai:SetNumber(0, 0)
   else
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3003, TARGET_ENE_0, DIST_Middle, 0)
   end
end

FourKnightC_Thunder236002_Act08 = function(ai, goal, _)
   -- Fast overhead smash + swing.
   local fate = ai:GetRandam_Int(1, 100)
   local fadeOut = ai:IsFinishTimer(0)
   Approach_Act(ai, goal, localScriptConfigVar7, localScriptConfigVar7 + 4, 0)
   if fate <= 40 then
      if fadeOut then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3024, TARGET_ENE_0, DIST_Middle, 0)
         ai:SetNumber(0, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
      end
   else
      if fadeOut then
         goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3024, TARGET_ENE_0, DIST_Middle, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 4005, TARGET_ENE_0, DIST_Middle, 0)
         ai:SetNumber(0, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_ComboAttack, 10, 3004, TARGET_ENE_0, DIST_Middle, 0)
         goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
      end
   end
end

FourKnightC_Thunder236002_GetWellSpace_Act = function(ai, goal)
   local retreatFate = ai:GetRandam_Int(1, 100)
   local directionFate = ai:GetRandam_Int(0, 1)
   local fadeOut = ai:IsFinishTimer(0)
   ai:GetTeamRecordCount(COORDINATE_TYPE_SideWalk_L + directionFate, TARGET_ENE_0, 2)  -- Leaving; could affect state.
   -- No goals added if it's time to fade out.
   if fadeOut then
      if retreatFate <= 50 then
         -- Do nothing.
      elseif retreatFate <= 60 then
         goal:AddSubGoal(GOAL_COMMON_LeaveTarget, 2.5, TARGET_ENE_0, 6, TARGET_ENE_0, true, -1)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 701, TARGET_ENE_0, 0, AI_DIR_TYPE_B, 4)
      end
   end
end

FourKnightC_Thunder236002Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

FourKnightC_Thunder236002Battle_Terminate = function(ai, goal)
end

FourKnightC_Thunder236002Battle_Interupt = function(ai, goal)
   if ai:IsFinishTimer(0) then
      -- No interrupt if it's time to fade out. (May actually want this to be possible, in one phase at least.)
      return false
   end
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   if Damaged_Step(ai, goal, 3, 15, 60, 20, 20, 4) then
      return true
   end
   if GuardBreak_Act(ai, goal, 7, 80) then
      if enemyDistance <= 1 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, bigSwing, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, shortCharge, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   if MissSwing_Int(ai, goal, 7, 70) then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, shortCharge, TARGET_ENE_0, DIST_Middle, 0)
      return true
   end
   if UseItem_Act(ai, goal, 8, 30) then
      if enemyDistance <= 1 then
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, bigSwing, TARGET_ENE_0, DIST_Middle, 0)
      else
         goal:AddSubGoal(GOAL_COMMON_Attack, 10, shortCharge, TARGET_ENE_0, DIST_Middle, 0)
      end
      return true
   end
   local enemyShooting = Shoot_2dist(ai, goal, 3.2, 10.2, 0, 50)
   if enemyShooting == 1 then
      -- Short charge.
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, shortCharge, TARGET_ENE_0, DIST_Middle, 0)
      return true
   elseif enemyShooting == 2 then
      goal:AddSubGoal(GOAL_COMMON_Attack, 10, shortCharge, TARGET_ENE_0, DIST_Middle, 0)
      return true
   end
   return false
end


