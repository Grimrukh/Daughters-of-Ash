--@package: m14_01_00_00.luabnd, 525000_logic.lua
--@battle_goal: 525000, Tadare525000_Logic

Tadare525000_Logic = function(ai)
   -- Get event flag based on host entering Ceaseless fog. If it's true, then have Ceaseless approach his old starting point.
   -- Otherwise, easy setup.
   if ai:HasSpecialEffectId(TARGET_SELF, 5129) then
      ai:SetEventMoveTarget(1412707)
      local distanceToLedge = ai:GetDistAtoB(POINT_EVENT, TARGET_SELF)
      if distanceToLedge >= 2 then
         ai:AddTopGoal(GOAL_COMMON_ApproachTarget, 5, POINT_EVENT, 0.05, TARGET_SELF, false, -1)   -- walking might be more appropriate
      else
         COMMON_EasySetup3(ai)
      end
   else
      COMMON_EasySetup3(ai)
   end
end

Tadare525000_Interupt = function(ai, goal)
end
