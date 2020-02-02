--@package: m12_00_00_00.luabnd, 323002_battle.lua
--@battle_goal: 323002, Kagerou323002Battle

OnIf_323002 = function(ai, goal, ifSlot)
   if ifSlot == 0 then
      ai:SetTimer(0, 80) -- Time if not injured
      ai:SetTimer(1, 50) -- Time if injured (20% HP lost)
      ai:SetNumber(1, ai:GetHpRate(TARGET_SELF))
      ai:SetNumber(0, 1)
   end
end

Kagerou323002Battle_Activate = function(ai, goal)
   local selfHpRate = ai:GetHpRate(TARGET_SELF)
   local fate0 = ai:GetRandam_Int(1, 100)
   local rightMoveOdds = 0
   local leftMoveOdds = 0
   local landingOdds = 0
   local takeoffOdds = 0
   local turnaroundRightOdds = 0
   local turnaroundLeftOdds = 0
   local hoverOdds = 0
   local canLand = ai:GetNumber(0)
   if canLand == 0 then
      -- Only happens at battle start.
      goal:AddSubGoal(GOAL_COMMON_If, 10, 0)  -- Resets landing timer (shorter timer if loses 20% health).
      goal:AddSubGoal(GOAL_COMMON_Wait, 0.1, TARGET_NONE, 0, 0, 0)
   end
   if ai:IsInsideTargetRegion(TARGET_SELF, 1202210) then
      takeoffOdds = 100
   elseif (ai:IsFinishTimer(0) and canLand == 1 and not ai:IsInsideTargetRegion(TARGET_SELF, 1202226))
           or selfHpRate <= ai:GetNumber(1) - 0.2 and ai:IsFinishTimer(1) and canLand == 1 and not ai:IsInsideTargetRegion(TARGET_SELF, 1202226) then
      -- Lands if not in region 1202226 AND (Timer 0 has finished OR Timer 1 has finished and boss has lost at least
      -- 20% more health since last landing).
      landingOdds = 100
   elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202245) and (ai:IsInsideTargetRegion(TARGET_SELF, 1202225) or ai:IsInsideTargetRegion(TARGET_SELF, 1202226)) then
      turnaroundRightOdds = 100
   elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202245) and (ai:IsInsideTargetRegion(TARGET_SELF, 1202227) or ai:IsInsideTargetRegion(TARGET_SELF, 1202228) or ai:IsInsideTargetRegion(TARGET_SELF, 1202228)) then
      turnaroundLeftOdds = 100
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202220) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202240) then
         leftMoveOdds = 5
         turnaroundLeftOdds = 35
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202241) then
         leftMoveOdds = 60
         turnaroundLeftOdds = 35
         hoverOdds = 5
      else
         leftMoveOdds = 95
         turnaroundLeftOdds = 5
      end
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202221) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202240) then
         rightMoveOdds = 60
         turnaroundRightOdds = 15
         hoverOdds = 25
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202241) then
         rightMoveOdds = 20
         leftMoveOdds = 20
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202242) then
         leftMoveOdds = 60
         turnaroundLeftOdds = 15
         hoverOdds = 25
      else
         leftMoveOdds = 95
         turnaroundLeftOdds = 5
      end
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202222) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202240) then
         rightMoveOdds = 85
         turnaroundRightOdds = 15
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202241) then
         rightMoveOdds = 60
         turnaroundRightOdds = 15
         hoverOdds = 25
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202242) then
         rightMoveOdds = 20
         leftMoveOdds = 20
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202243) then
         leftMoveOdds = 60
         turnaroundLeftOdds = 15
         hoverOdds = 25
      else
         leftMoveOdds = 85
         turnaroundLeftOdds = 15
      end
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202223) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202244) then
         leftMoveOdds = 60
         turnaroundLeftOdds = 15
         hoverOdds = 25
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202243) then
         rightMoveOdds = 20
         leftMoveOdds = 20
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202242) then
         rightMoveOdds = 60
         turnaroundRightOdds = 15
         hoverOdds = 25
      else
         rightMoveOdds = 95
         turnaroundRightOdds = 5
      end
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202224) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202244) then
         rightMoveOdds = 5
         turnaroundRightOdds = 35
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202243) then
         rightMoveOdds = 60
         turnaroundRightOdds = 35
         hoverOdds = 5
      else
         rightMoveOdds = 95
         turnaroundRightOdds = 5
      end
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202225) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202240) then
         rightMoveOdds = 5
         turnaroundRightOdds = 35
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202241) then
         rightMoveOdds = 60
         turnaroundRightOdds = 35
         hoverOdds = 5
      else
         rightMoveOdds = 95
         turnaroundRightOdds = 5
      end
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202226) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202240) then
         leftMoveOdds = 60
         turnaroundLeftOdds = 15
         hoverOdds = 25
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202241) then
         rightMoveOdds = 20
         leftMoveOdds = 20
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202242) then
         rightMoveOdds = 60
         turnaroundRightOdds = 15
         hoverOdds = 25
      else
         rightMoveOdds = 95
         turnaroundRightOdds = 5
      end
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202227) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202240) then
         leftMoveOdds = 85
         turnaroundLeftOdds = 15
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202241) then
         leftMoveOdds = 60
         turnaroundLeftOdds = 15
         hoverOdds = 25
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202242) then
         rightMoveOdds = 20
         leftMoveOdds = 20
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202243) then
         rightMoveOdds = 60
         turnaroundRightOdds = 15
         hoverOdds = 25
      else
         rightMoveOdds = 85
         turnaroundRightOdds = 15
      end
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202228) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202244) then
         rightMoveOdds = 60
         turnaroundRightOdds = 15
         hoverOdds = 25
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202243) then
         rightMoveOdds = 20
         leftMoveOdds = 20
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202242) then
         leftMoveOdds = 60
         turnaroundLeftOdds = 15
         hoverOdds = 25
      else
         leftMoveOdds = 95
         turnaroundLeftOdds = 5
      end
   elseif ai:IsInsideTargetRegion(TARGET_SELF, 1202229) then
      if ai:IsInsideTargetRegion(TARGET_ENE_0, 1202244) then
         leftMoveOdds = 5
         turnaroundLeftOdds = 35
         hoverOdds = 60
      elseif ai:IsInsideTargetRegion(TARGET_ENE_0, 1202243) then
         leftMoveOdds = 60
         turnaroundLeftOdds = 35
         hoverOdds = 5
      else
         leftMoveOdds = 95
         turnaroundLeftOdds = 5
      end
   else
      ai:PrintText("ERROR Area Over")
      hoverOdds = 100
   end

   local actionFate = ai:GetRandam_Int(1, rightMoveOdds + leftMoveOdds + landingOdds + takeoffOdds
           + turnaroundRightOdds + turnaroundLeftOdds + hoverOdds)
   if actionFate <= rightMoveOdds then
      local animationID = 3010
      if fate0 <= 50 then
         animationID = 3010
      elseif fate0 <= 80 then
         animationID = 3001
      else
         animationID = 3002
      end
      ai:PrintText("Do RightMove")
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, animationID, TARGET_ENE_0, DIST_None, 0)
   elseif actionFate <= rightMoveOdds + leftMoveOdds then
      local animationID = 3011
      if fate0 <= 50 then
         animationID = 3011
      elseif fate0 <= 80 then
         animationID = 3004
      else
         animationID = 3005
      end
      ai:PrintText("Do LeftMove")
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, animationID, TARGET_ENE_0, DIST_None, 0)
   elseif actionFate <= rightMoveOdds + leftMoveOdds + landingOdds then
      ai:PrintText("Do Landing")
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3020, TARGET_ENE_0, DIST_None, 0)
   elseif actionFate <= rightMoveOdds + leftMoveOdds + landingOdds + takeoffOdds then
      -- Waits 4-8 seconds before taking off. (Now 2-4 for Mournwing.)
      ai:PrintText("Do TakeOff")
      goal:AddSubGoal(GOAL_COMMON_Wait, ai:GetRandam_Float(2, 4), TARGET_NONE, 0, 0, 0)
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3001, TARGET_ENE_0, DIST_None, 0)  -- Explosion.
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, 3000, TARGET_ENE_0, DIST_None, 0)  -- Takeoff.
      goal:AddSubGoal(GOAL_COMMON_If, 10, 0)  -- Reset landing timer.
   elseif actionFate <= rightMoveOdds + leftMoveOdds + landingOdds + takeoffOdds + turnaroundRightOdds then
      local animationID = 3013
      if fate0 <= 80 and selfHpRate <= 0.5 then
         animationID = 3013
      else
         animationID = 3024
      end
      ai:PrintText("Do Turnaround Right")
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, animationID, TARGET_ENE_0, DIST_None, 0)
   elseif actionFate <= rightMoveOdds + leftMoveOdds + landingOdds + takeoffOdds +
           turnaroundRightOdds + turnaroundLeftOdds then
      local animationID = 3012
      if fate0 <= 80 and selfHpRate <= 0.5 then
         animationID = 3012
      else
         animationID = 3022
      end
      ai:PrintText("Do Turnaround Left")
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, animationID, TARGET_ENE_0, DIST_None, 0)
   else
      -- Hover.
      local fate1 = ai:GetRandam_Int(1, 100)
      local firstAnimationID = 3014
      local secondAnimationID = 3007
      if selfHpRate <= 0.5 then
         if fate0 <= 15 then
            firstAnimationID = 3014
         elseif fate0 <= 30 then
            firstAnimationID = 3007
         elseif fate0 <= 100 then
            firstAnimationID = 3015
         else
            firstAnimationID = 3008
         end
      elseif fate0 <= 35 then
         firstAnimationID = 3014
      elseif fate0 <= 75 then
         firstAnimationID = 3007
      elseif fate0 <= 90 then
         firstAnimationID = 3015
      else
         firstAnimationID = 3008
      end
      if selfHpRate <= 0.5 then
         if fate1 <= 15 then
            secondAnimationID = 3014
         elseif fate1 <= 30 then
            secondAnimationID = 3007
         elseif fate1 <= 100 then
            secondAnimationID = 3015
         else
            secondAnimationID = 3008
         end
      elseif fate1 <= 35 then
         secondAnimationID = 3014
      elseif fate1 <= 75 then
         secondAnimationID = 3007
      elseif fate1 <= 90 then
         secondAnimationID = 3015
      else
         secondAnimationID = 3008
      end
      ai:PrintText("Do Hover")
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, firstAnimationID, TARGET_ENE_0, DIST_None, 0)
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 20, secondAnimationID, TARGET_ENE_0, DIST_None, 0)
   end
end

Kagerou323002Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Kagerou323002Battle_Terminate = function(ai, goal)
end

Kagerou323002Battle_Interupt = function(ai, goal)
   return false
end
