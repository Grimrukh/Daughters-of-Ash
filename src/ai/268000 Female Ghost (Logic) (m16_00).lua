--@package: m16_00_00_00.luabnd, 268000_logic.lua
--@battle_goal: 268000, Ghost_Runaway268000_Logic

Ghost_Runaway268000_Logic = function(ai)
   local func1_var1 = ai:GetNpcThinkParamID()
   local func1_var2 = 0
   local func1_var3 = 0
   local func1_var4 = 0
   if func1_var1 == 268000 or func1_var1 == 268001 then
      func1_var3 = 1602853
      func1_var4 = 1602853
      func1_var2 = 1
   elseif func1_var1 == 268010 or func1_var1 == 268011 then
      func1_var3 = 1602851
      func1_var4 = 1602851
      func1_var2 = 1
   elseif func1_var1 == 268020 or func1_var1 == 268021 then
      func1_var3 = 1602855
      func1_var4 = 1602855
      func1_var2 = 1
   end
   if func1_var2 == 1 then
      if not ai:IsInsideTargetRegion(TARGET_SELF, func1_var3) and not ai:IsInsideTargetRegion(TARGET_SELF, func1_var4) then
         ai:AddTopGoal(GOAL_COMMON_ApproachTarget, 10, POINT_INITIAL, 2, TARGET_SELF, false, -1)
         ai:AddTopGoal(GOAL_COMMON_Wait, 2, TARGET_ENE_0, 0, 0, 0)
      else
         COMMON_EasySetup3(ai)
      end
   else
      COMMON_EasySetup3(ai)
   end
end

Ghost_Runaway268000_Interupt = function(ai, goal)
end


