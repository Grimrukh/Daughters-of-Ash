--@package: m13_00_00_00.luabnd, 294000_battle.lua
--@battle_goal: 294000, Skeleton_baby294000Battle

local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 3

Skeleton_baby294000Battle_Activate = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_ApproachTarget, 2, TARGET_ENE_0, 2, TARGET_SELF, false, -1)
   goal:AddSubGoal(GOAL_COMMON_Attack, 10, 3000, TARGET_ENE_0, DIST_Middle)
   goal:AddSubGoal(GOAL_COMMON_Wait, ai:GetRandam_Float(0, 1.5), TARGET_SELF, 0, 0, 0)
end

Skeleton_baby294000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Skeleton_baby294000Battle_Terminate = function(ai, goal)
end

Skeleton_baby294000Battle_Interupt = function(ai, goal)
   return false
end


