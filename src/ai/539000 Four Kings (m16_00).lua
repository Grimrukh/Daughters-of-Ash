--@package: m16_00_00_00.luabnd, 539000_battle.lua
--@battle_goal: 539000, Ja_yearl_demon539000Battle

--[[
Moves:
3000: One handed swipe, right to left
   3001: Left to right
3002: Thrust stab
3003: Spin and swipe
3004: Diagonal downward slash, right to left
3005: Diagonal downward slash, left to right
3006: Overhead smash
3007: Spin and grab
3008: Explosion
3009: Small projectiles
3010: Homing disc

NEW:
3011: Double homing disc
3012: Triple homing disc
3014: Explosion with ten magic projectiles
3015: Explosion with three dark projectiles
3016: Dark Bead from grab animation
]]--

local localScriptConfigVar0 = 0
local localScriptConfigVar1 = 12.5
local localScriptConfigVar2 = 0
local localScriptConfigVar3 = 10.6
local localScriptConfigVar4 = 0
local localScriptConfigVar5 = 0
local localScriptConfigVar6 = 0
local localScriptConfigVar7 = 10.4
local localScriptConfigVar8 = 0
local localScriptConfigVar9 = 11.3
local localScriptConfigVar10 = 0
local localScriptConfigVar11 = 8
local localScriptConfigVar12 = 0
local localScriptConfigVar13 = 10
local localScriptConfigVar14 = 22
local localScriptConfigVar15 = 29
local localScriptConfigVar16 = 10
local localScriptConfigVar17 = 15
local BOLTARSH = 539000
local SILGORE = 539001
local GANZEYER = 539002
local RENDAIN = 539003


Ja_yearl_demon539000Battle_Activate = function(ai, goal)
   local odds1_BasicSlashes = 0
   local oddsTable2 = 0
   local oddsTable3 = 0
   local oddsTable4 = 0
   local oddsTable5 = 0
   local odds6_Grab = 0
   local odds7_Explosion = 0
   local odds8_DistantMagic = 0
   local oddsTable9 = 0
   local oddsTable10 = 0
   local oddsTable11 = 0
   local oddsTable12 = 0
   local oddsTable13 = 0
   local oddsTable14 = 0
   local oddsTable15 = 0
   local oddsTable16 = 0
   local enemyDistance = ai:GetDist(TARGET_ENE_0)
   local projectilesAllowed = ai:GetEventRequest(0)
   local isAttacker = ai:GetEventRequest(1)

   if ai:IsFinishTimer(1) == true then
      ai:SetTimer(1, 9999)
      goal:AddSubGoal(GOAL_COMMON_Wait, ai:GetRandam_Float(0, 3), TARGET_ENE_0, 0, 0, 0)
   end

   if isAttacker == 1 then
      -- Aggressive.
      local king_id = ai:GetNpcThinkParamID()
      if king_id == BOLTARSH then
         -- Standard odds.
         if projectilesAllowed == 1 and ai:IsFinishTimer(0) == true then
            if enemyDistance >= 22 then
               odds1_BasicSlashes = 8
               oddsTable2 = 8
               oddsTable4 = 8
               oddsTable5 = 8
               odds6_Grab = 3
               odds7_Explosion = 0
               odds8_DistantMagic = 25
               oddsTable9 = 40
            elseif enemyDistance >= 12.5 then
               odds1_BasicSlashes = 15
               oddsTable2 = 15
               oddsTable4 = 15
               oddsTable5 = 15
               odds6_Grab = 5
               odds7_Explosion = 0
               oddsTable9 = 35
            elseif enemyDistance >= 8 then
               odds1_BasicSlashes = 18
               oddsTable2 = 18
               oddsTable4 = 18
               oddsTable5 = 18
               odds6_Grab = 5
               odds7_Explosion = 5
               oddsTable9 = 18
            elseif enemyDistance >= 4 then
               odds1_BasicSlashes = 20
               oddsTable2 = 20
               oddsTable4 = 20
               oddsTable5 = 20
               odds6_Grab = 5
               odds7_Explosion = 5
               oddsTable9 = 10
            else
               odds1_BasicSlashes = 21
               oddsTable2 = 21
               oddsTable4 = 21
               oddsTable5 = 21
               odds6_Grab = 5
               odds7_Explosion = 11
            end
         elseif enemyDistance >= 22 then
            odds1_BasicSlashes = 25
            oddsTable2 = 25
            oddsTable4 = 25
            oddsTable5 = 20
            odds6_Grab = 5
            odds7_Explosion = 0
         elseif enemyDistance >= 13.4 then
            odds1_BasicSlashes = 24
            oddsTable2 = 24
            oddsTable4 = 24
            oddsTable5 = 24
            odds6_Grab = 4
            odds7_Explosion = 0
         elseif enemyDistance >= 8 then
            odds1_BasicSlashes = 23
            oddsTable2 = 23
            oddsTable4 = 23
            oddsTable5 = 19
            odds6_Grab = 6
            odds7_Explosion = 6
         elseif enemyDistance >= 4 then
            odds1_BasicSlashes = 22
            oddsTable2 = 22
            oddsTable4 = 22
            oddsTable5 = 22
            odds6_Grab = 5
            odds7_Explosion = 7
         else
            odds1_BasicSlashes = 21
            oddsTable2 = 21
            oddsTable4 = 21
            oddsTable5 = 21
            odds6_Grab = 5
            odds7_Explosion = 11
         end
      elseif king_id == SILGORE then
         -- Silgore. More magic.
         if projectilesAllowed == 1 and ai:IsFinishTimer(0) == true then
            if enemyDistance >= 22 then
               odds1_BasicSlashes = 10
               odds7_Explosion = 10
               odds8_DistantMagic = 20
               oddsTable9 = 60
            elseif enemyDistance >= 12.5 then
               odds1_BasicSlashes = 10
               oddsTable2 = 5
               oddsTable4 = 5
               oddsTable5 = 5
               oddsTable9 = 75
            elseif enemyDistance >= 8 then
               odds1_BasicSlashes = 13
               oddsTable2 = 12
               oddsTable4 = 12
               oddsTable5 = 13
               odds7_Explosion = 10
               oddsTable9 = 40
            elseif enemyDistance >= 4 then
               odds1_BasicSlashes = 15
               oddsTable2 = 15
               oddsTable4 = 15
               oddsTable5 = 15
               odds7_Explosion = 10
               oddsTable9 = 30
            else
               odds1_BasicSlashes = 20
               oddsTable2 = 20
               oddsTable4 = 20
               oddsTable5 = 20
               odds7_Explosion = 20
            end
         elseif enemyDistance >= 22 then
            odds1_BasicSlashes = 25
            oddsTable2 = 25
            oddsTable4 = 25
            oddsTable5 = 20
            odds7_Explosion = 5
         elseif enemyDistance >= 13.4 then
            odds1_BasicSlashes = 20
            oddsTable2 = 25
            oddsTable4 = 25
            oddsTable5 = 25
            odds7_Explosion = 5
         elseif enemyDistance >= 8 then
            odds1_BasicSlashes = 23
            oddsTable2 = 23
            oddsTable4 = 22
            oddsTable5 = 22
            odds7_Explosion = 10
         elseif enemyDistance >= 4 then
            odds1_BasicSlashes = 20
            oddsTable2 = 20
            oddsTable4 = 20
            oddsTable5 = 20
            odds7_Explosion = 20
         else
            odds1_BasicSlashes = 20
            oddsTable2 = 20
            oddsTable4 = 20
            oddsTable5 = 20
            odds7_Explosion = 20
         end
      elseif king_id == GANZEYER then
         -- Ganzeyer. Explosions conjure Dark Orbs. Loves to grab.
         if projectilesAllowed == 1 and ai:IsFinishTimer(0) == true then
            if enemyDistance >= 22 then
               odds1_BasicSlashes = 10
               oddsTable2 = 10
               oddsTable4 = 10
               oddsTable5 = 10
               odds6_Grab = 5
               odds8_DistantMagic = 50
               oddsTable9 = 5
            elseif enemyDistance >= 12.5 then
               odds1_BasicSlashes = 15
               oddsTable2 = 10
               oddsTable4 = 15
               oddsTable5 = 10
               odds6_Grab = 5
               odds7_Explosion = 5
               odds8_DistantMagic = 30
               oddsTable9 = 10
            elseif enemyDistance >= 8 then
               odds1_BasicSlashes = 15
               oddsTable2 = 15
               oddsTable4 = 15
               oddsTable5 = 15
               odds6_Grab = 15
               odds7_Explosion = 10
               oddsTable9 = 15
            elseif enemyDistance >= 4 then
               odds1_BasicSlashes = 20
               oddsTable2 = 20
               oddsTable4 = 10
               oddsTable5 = 20
               odds6_Grab = 15
               odds7_Explosion = 20
               oddsTable9 = 30
            else
               odds1_BasicSlashes = 15
               oddsTable2 = 15
               oddsTable4 = 15
               oddsTable5 = 15
               odds6_Grab = 10
               odds7_Explosion = 30
            end
         elseif enemyDistance >= 22 then
            odds1_BasicSlashes = 25
            oddsTable2 = 25
            oddsTable4 = 25
            oddsTable5 = 20
            odds6_Grab = 5
            odds7_Explosion = 4
         elseif enemyDistance >= 13.4 then
            odds1_BasicSlashes = 24
            oddsTable2 = 24
            oddsTable4 = 24
            oddsTable5 = 24
            odds6_Grab = 4
            odds7_Explosion = 3
         elseif enemyDistance >= 8 then
            odds1_BasicSlashes = 23
            oddsTable2 = 23
            oddsTable4 = 23
            oddsTable5 = 19
            odds6_Grab = 10
            odds7_Explosion = 10
         elseif enemyDistance >= 4 then
            odds1_BasicSlashes = 20
            oddsTable2 = 20
            oddsTable4 = 20
            oddsTable5 = 15
            odds6_Grab = 20
            odds7_Explosion = 10
         else
            odds1_BasicSlashes = 21
            oddsTable2 = 21
            oddsTable4 = 21
            oddsTable5 = 21
            odds6_Grab = 10
            odds7_Explosion = 11
         end
      elseif king_id == RENDAIN then
         -- Rendain. Melee beast, no magic, so no projectile timer check.
         local rendainHp = ai:GetHpRate(TARGET_SELF)
         if enemyDistance >= 22 then
            odds1_BasicSlashes = 25
            oddsTable2 = 25
            oddsTable4 = 25
            oddsTable5 = 20
            odds6_Grab = 5
         elseif enemyDistance >= 13.4 then
            odds1_BasicSlashes = 24
            oddsTable2 = 24
            oddsTable4 = 24
            oddsTable5 = 24
            odds6_Grab = 4
         elseif enemyDistance >= 8 then
            odds1_BasicSlashes = 23
            oddsTable2 = 23
            oddsTable4 = 23
            oddsTable5 = 19
            odds6_Grab = 6
         elseif enemyDistance >= 4 then
            odds1_BasicSlashes = 22
            oddsTable2 = 22
            oddsTable4 = 22
            oddsTable5 = 22
            odds6_Grab = 5
            if rendainHp <= 0.4 then
               oddsTable16 = 20
            end
         else
            odds1_BasicSlashes = 21
            oddsTable2 = 21
            oddsTable4 = 21
            oddsTable5 = 21
            odds6_Grab = 5
            if rendainHp <= 0.4 then
               oddsTable16 = 30
            end
         end
      end

   -- Not aggressive.
   elseif enemyDistance <= 3.0 then
      oddsTable10 = 50
      oddsTable12 = 13
      oddsTable13 = 13
      oddsTable14 = 12
      oddsTable15 = 12
   else
      oddsTable10 = 20
      oddsTable11 = 80
   end

   local totalOdds = odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion +
           odds8_DistantMagic + oddsTable9 + oddsTable10 + oddsTable11 + oddsTable12 + oddsTable13 + oddsTable14 +
           oddsTable15 + oddsTable16

   local randomRoll = ai:GetRandam_Int(1, totalOdds)

   local getWellSpace_Odds = 0

   if randomRoll <= odds1_BasicSlashes then
      Ja_yearl_demon539000_Act01(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 then
      Ja_yearl_demon539000_Act02(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 then
      Ja_yearl_demon539000_Act03(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 then
      Ja_yearl_demon539000_Act04(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 then
      Ja_yearl_demon539000_Act05(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab then
      Ja_yearl_demon539000_Act06(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion then
      Ja_yearl_demon539000_Act07(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion +
           odds8_DistantMagic then
      Ja_yearl_demon539000_Act08(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion +
           odds8_DistantMagic + oddsTable9 then
      Ja_yearl_demon539000_Act09(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion +
           odds8_DistantMagic + oddsTable9 + oddsTable10 then
      Ja_yearl_demon539000_Act10(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion +
           odds8_DistantMagic + oddsTable9 + oddsTable10 + oddsTable11 then
      Ja_yearl_demon539000_Act11(ai, goal)
      getWellSpace_Odds = 0
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion +
           odds8_DistantMagic + oddsTable9 + oddsTable10 + oddsTable11 + oddsTable12 then
      Ja_yearl_demon539000_Act12(ai, goal)
      getWellSpace_Odds = 100
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion +
           odds8_DistantMagic + oddsTable9 + oddsTable10 + oddsTable11 + oddsTable12 + oddsTable13 then
      Ja_yearl_demon539000_Act13(ai, goal)
      getWellSpace_Odds = 100
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion +
           odds8_DistantMagic + oddsTable9 + oddsTable10 + oddsTable11 + oddsTable12 + oddsTable13 + oddsTable14 then
      Ja_yearl_demon539000_Act14(ai, goal)
      getWellSpace_Odds = 100
   elseif randomRoll <= odds1_BasicSlashes + oddsTable2 + oddsTable3 + oddsTable4 + oddsTable5 + odds6_Grab + odds7_Explosion +
           odds8_DistantMagic + oddsTable9 + oddsTable10 + oddsTable11 + oddsTable12 + oddsTable13 + oddsTable14 +
           oddsTable15 then
      Ja_yearl_demon539000_Act15(ai, goal)
      getWellSpace_Odds = 100
   else
      Ja_yearl_demon539000_Act16(ai, goal)
      getWellSpace_Odds = 0
   end

   local func1_var29 = ai:GetRandam_Int(1, 100)
   if func1_var29 <= getWellSpace_Odds then
      Ja_yearl_demon539000_GetWellSpace_Act(ai, goal)
   end
end

Ja_yearl_demon539000_Act01 = function(ai, goal)
   -- Simple melee slashes.
   local func2_var2 = ai:GetRandam_Int(1, 100)
   local func2_var4 = localScriptConfigVar1
   local func2_var5 = localScriptConfigVar1 + 10
   local func2_var7 = ai:GetRandam_Int(1, 100)
   if func2_var2 <= 60 then
      func2_var5 = localScriptConfigVar1 + 9999
   end
   Approach_Act(ai, goal, func2_var4, func2_var5, 0)
   if func2_var7 <= 20 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 1.5, 25)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 1.5, 25)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Ja_yearl_demon539000_Act02 = function(ai, goal)
   -- Thrusting stab.
   local func3_var2 = ai:GetRandam_Int(1, 100)
   local func3_var4 = localScriptConfigVar3
   local func3_var5 = localScriptConfigVar3 + 10
   local func3_var6 = 0
   if func3_var2 <= 60 then
      func3_var5 = localScriptConfigVar3 + 9999
   end
   Approach_Act(ai, goal, func3_var4, func3_var5, func3_var6)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_Middle, 1.5, 10)
end

Ja_yearl_demon539000_Act03 = function(ai, goal)
   -- Spin and swipe.
   local func4_var3 = localScriptConfigVar5
   local func4_var4 = localScriptConfigVar5 + 0
   local func4_var5 = 0
   Approach_Act(ai, goal, func4_var3, func4_var4, func4_var5)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3003, TARGET_ENE_0, DIST_Middle, 1.5, 25)
end

Ja_yearl_demon539000_Act04 = function(ai, goal)
   -- Diagonal slashes.
   local func5_var2 = ai:GetRandam_Int(1, 100)
   local func5_var4 = localScriptConfigVar7
   local func5_var5 = localScriptConfigVar7 + 10
   local func5_var6 = 0
   local func5_var7 = ai:GetRandam_Int(1, 100)
   if func5_var2 <= 60 then
      func5_var5 = localScriptConfigVar1 + 9999
   end
   Approach_Act(ai, goal, func5_var4, func5_var5, func5_var6)
   if func5_var7 <= 40 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3004, TARGET_ENE_0, DIST_Middle, 1.5, 8)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3004, TARGET_ENE_0, DIST_Middle, 1.5, 8)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Ja_yearl_demon539000_Act05 = function(ai, goal)
   -- Overhead slam.
   local func6_var2 = ai:GetRandam_Int(1, 100)
   local func6_var3 = ai:GetDist(TARGET_ENE_0)
   local func6_var4 = localScriptConfigVar9
   local func6_var5 = localScriptConfigVar9 + 10
   local func6_var6 = 0
   local func6_var7 = ai:GetRandam_Int(1, 100)
   if func6_var2 <= 60 then
      func6_var5 = localScriptConfigVar9 + 9999
   end
   Approach_Act(ai, goal, func6_var4, func6_var5, func6_var6)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3006, TARGET_ENE_0, DIST_Middle, 1.5, 25)
end

Ja_yearl_demon539000_Act06 = function(ai, goal)
   -- Grab.
   local func7_var2 = ai:GetRandam_Int(1, 100)
   local func7_var3 = ai:GetDist(TARGET_ENE_0)
   local func7_var4 = localScriptConfigVar11
   local func7_var5 = localScriptConfigVar11 + 10
   local func7_var6 = 0
   local func7_var7 = ai:GetRandam_Int(1, 100)
   if func7_var2 <= 60 then
      func7_var5 = localScriptConfigVar11 + 9999
   end
   Approach_Act(ai, goal, func7_var4, func7_var5, func7_var6)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3007, TARGET_ENE_0, DIST_Middle, 1.5, 25)
end

Ja_yearl_demon539000_Act07 = function(ai, goal)
   -- Explosion.
   local king_id = ai:GetNpcThinkParamID()
   if king_id == SILGORE then
      -- Silgore uses explosion and spawns ten Soulmass projectiles.
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3014, TARGET_ENE_0, DIST_Middle)
   elseif king_id == GANZEYER then
      -- Ganzeyer uses explosion and spawns three dark Soulmass projectiles.
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3015, TARGET_ENE_0, DIST_Middle)
   elseif king_id == BOLTARSH then
      -- Boltarsh uses normal explosion.
      goal:AddSubGoal(GOAL_COMMON_NonspinningAttack, 10, 3008, TARGET_ENE_0, DIST_Middle)
   end
end

Ja_yearl_demon539000_Act08 = function(ai, goal)
   -- Magic projectiles used by Boltarsh and Ganzeyer. 30-60 second delay between them.
   ai:SetTimer(0, ai:GetRandam_Int(30, 60))
   goal:AddSubGoal(GOAL_COMMON_KeepDist, 10, TARGET_ENE_0, 15, 22, TARGET_ENE_0, true, -1)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3009, TARGET_ENE_0, DIST_None, -1, -1)
end

Ja_yearl_demon539000_Act09 = function(ai, goal)
   -- Homing disc (Boltarsh/Ganzeyer), double or triple homing disc (Silgore) or dark wave (Ganzeyer).
   if ai:GetNpcThinkParamID() == SILGORE then
      -- Silgore uses double or triple homing disc.
      goal:AddSubGoal(GOAL_COMMON_KeepDist, 10, TARGET_ENE_0, 15, 22, TARGET_ENE_0, true, -1)
      if ai:GetHpRate(TARGET_SELF) <= 0.4 then
         -- Triple homing disc.
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3012, TARGET_ENE_0, DIST_None, -1, -1)
      else
         goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3011, TARGET_ENE_0, DIST_None, -1, -1)
      end
      ai:SetTimer(0, ai:GetRandam_Int(10, 20))
   elseif ai:GetNpcThinkParamID() == GANZEYER and ai:GetHpRate(TARGET_SELF) <= 0.6 then
      -- Ganzeyer sprays Dark Bead (with grab animation) at close range if he's below 60% health.
      Approach_Act(ai, goal, localScriptConfigVar1, localScriptConfigVar1 + 10, 0)
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3016, TARGET_ENE_0, DIST_None, -1, -1)
      ai:SetTimer(0, ai:GetRandam_Int(25, 40))
   else
      -- Boltarsh and healthy Ganzeyer use normal homing disc.
      goal:AddSubGoal(GOAL_COMMON_KeepDist, 10, TARGET_ENE_0, 15, 22, TARGET_ENE_0, true, -1)
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3010, TARGET_ENE_0, DIST_None, -1, -1)
      ai:SetTimer(0, ai:GetRandam_Int(30, 60))
   end

   ai:SetTimer(0, ai:GetRandam_Int(25, 40))
end

Ja_yearl_demon539000_Act10 = function(ai, goal)
   -- Wait or strafe.
   local waitOdds = ai:GetRandam_Int(1, 100)
   if waitOdds <= 25 then
      goal:AddSubGoal(GOAL_COMMON_Wait, ai:GetRandam_Float(0, 3), TARGET_ENE_0, 0, 0, 0)
   else
      local direction = ai:GetRandam_Int(0, 1)
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, direction, ai:GetRandam_Int(50, 110), true, true, -1)
   end
end

Ja_yearl_demon539000_Act11 = function(ai, goal)
   -- Maintain distance.
   goal:AddSubGoal(GOAL_COMMON_KeepDist, 10, TARGET_ENE_0, 15, 22, TARGET_ENE_0, true, -1)
end

Ja_yearl_demon539000_Act12 = function(ai, goal)
   local func17_var6 = ai:GetRandam_Int(1, 100)
   if func17_var6 <= 20 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 1.5, 25)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 1.5, 25)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3001, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Ja_yearl_demon539000_Act13 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3002, TARGET_ENE_0, DIST_Middle, 1.5, 10)
end

Ja_yearl_demon539000_Act14 = function(ai, goal)
   local func19_var2 = ai:GetDist(TARGET_ENE_0)
   local func19_var3 = localScriptConfigVar7 + 2
   local func19_var4 = localScriptConfigVar7 + 12
   local func19_var5 = 0
   local func19_var6 = ai:GetRandam_Int(1, 100)
   if func19_var6 <= 40 then
      goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3004, TARGET_ENE_0, DIST_Middle, 1.5, 25)
   else
      goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3004, TARGET_ENE_0, DIST_Middle, 1.5, 25)
      goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3005, TARGET_ENE_0, DIST_Middle, 0)
   end
end

Ja_yearl_demon539000_Act15 = function(ai, goal)
   goal:AddSubGoal(GOAL_COMMON_AttackTunableSpin, 10, 3006, TARGET_ENE_0, DIST_Middle, 1.5, 25)
end

Ja_yearl_demon539000_Act16 = function(ai, goal)
   -- Rendain's super combo attack.
   local minDistance = localScriptConfigVar1
   local maxDistance = localScriptConfigVar1 + 5
   Approach_Act(ai, goal, minDistance, maxDistance, 0)
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3000, TARGET_ENE_0, DIST_Middle, 1.5, 25)
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3001, TARGET_ENE_0, DIST_Middle, 1.5, 25)
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3004, TARGET_ENE_0, DIST_Middle, 1.5, 25)
   goal:AddSubGoal(GOAL_COMMON_ComboAttackTunableSpin, 10, 3005, TARGET_ENE_0, DIST_Middle, 1.5, 25)
   goal:AddSubGoal(GOAL_COMMON_ComboFinal, 10, 3008, TARGET_ENE_0, DIST_None, 0)
end

Ja_yearl_demon539000_GetWellSpace_Act = function(ai, goal)
   local func21_var2 = ai:GetRandam_Int(0, 100)
   local func21_var3 = ai:GetRandam_Int(0, 1)
   if func21_var2 <= 50 then
   elseif func21_var2 <= 75 then
      goal:AddSubGoal(GOAL_COMMON_SidewayMove, 3, TARGET_ENE_0, func21_var3, ai:GetRandam_Int(50, 110), true, true, -1)
   else
      local func21_var5 = ai:GetRandam_Int(1, 100)
      if func21_var5 <= 50 then
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 702, TARGET_ENE_0, 0, AI_DIR_TYPE_L, 4)
      else
         goal:AddSubGoal(GOAL_COMMON_SpinStep, 5, 703, TARGET_ENE_0, 0, AI_DIR_TYPE_R, 4)
      end
   end
end

Ja_yearl_demon539000Battle_Update = function(ai, goal)
   return GOAL_RESULT_Continue
end

Ja_yearl_demon539000Battle_Terminate = function(ai, goal)
end

Ja_yearl_demon539000Battle_Interupt = function(ai, goal)
   return false
end


