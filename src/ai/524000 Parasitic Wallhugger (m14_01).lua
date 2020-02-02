--@package: m14_01_00_00.luabnd, 524000_battle.lua
--@battle_goal: 524000, PrinceIzalis524000Battle

PrinceIzalis524000Battle_Activate = function(ai, goal)
   local enemyDistance = ai:GetDist(TARGET_ENEMY)
   local actRandomRoll = ai:GetRandam_Int(1, 100)
   if enemyDistance <= 5 and ai:IsInsideTarget(TARGET_ENEMY, AI_DIR_TYPE_F, 150) and ai:IsInsideTarget(TARGET_ENEMY, AI_DIR_TYPE_L, 90) then
      if actRandomRoll <= 10 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3003, TARGET_ENEMY, DIST_None, 0, -1)
      else
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3005, TARGET_ENEMY, DIST_None, 0, -1)
      end
   elseif enemyDistance <= 5 and ai:IsInsideTarget(TARGET_ENEMY, AI_DIR_TYPE_F, 55) and ai:IsInsideTarget(TARGET_ENEMY, AI_DIR_TYPE_R, 170) then
      if actRandomRoll <= 10 then
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3003, TARGET_ENEMY, DIST_None, 0, -1)
      else
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3006, TARGET_ENEMY, DIST_None, 0, -1)
      end
   elseif enemyDistance <= 5 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 5, 3003, TARGET_ENEMY, DIST_None, 0, -1)
   else
      goal:AddSubGoal(GOAL_COMMON_Wait, 1, TARGET_SELF, 0, 0, 0)
   end
end

PrinceIzalis524000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

PrinceIzalis524000Battle_Terminate = function(ai, goal)
end

PrinceIzalis524000Battle_Interupt = function(ai, goal)
   return false
end
