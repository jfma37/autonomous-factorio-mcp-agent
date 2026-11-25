---
goal: Vanilla 2.0 Rocket Launch (with satellite)
updated: 2026-11-25
---

# TODO

## Phase 1 - Bootstrap (current)
- [x] Connect to FLE, read core manuals
- [x] Coal outpost (2 drills -> chest) at (38.5,-85.5)
- [x] Stone outpost (drill -> chest) at (61.5,-52.5)
- [x] Iron: 6 drill->furnace pairs around (-6..4, -63)
- [x] Copper: 4 drill->furnace pairs around (-32..-26, -72)
- [ ] Periodic maintenance: refuel drills/furnaces (coal from chest), collect plates
- [ ] Craft wooden chests / iron chests; get wood from trees at (-9,47)

## Phase 2 - Power + Research (DONE)
- [x] Power at water, lab at (9.5,35.5), Automation researched

## Phase 3 - Automate science (DONE for red)
- [x] Gear asm + science asm + lab chain at (9.5..20.5, 35.5)
- [x] LogisticsSciencePack, Logistics, electric-mining-drill researched

## Phase 4 - Scale (DONE except long-haul logistics)
- [x] Pole line to ore field (26 poles)
- [x] Electric iron row: 6 units, chests at y=-50.5 (x=-19.5..-4.5)
- [x] Electric copper row: 6 units, chests at y=-74.5 (x=-36.5..-21.5)
- [x] Boiler fed from chest (600 coal) + 2nd engine
- [x] 2nd science assembler + lab 2
- [x] All red-only research done
- [ ] Still manual: carry plates from ore chests to science chests; refill boiler coal chest (-5.5,39.5) from coal outpost (38.5,-85.5); refuel 12 furnaces

## Phase 5 - Green science (DONE, packs hand-carried)
- [x] Green pack block at (11-23, 46-57), ~7 packs/min
- [x] Second boiler + 2 engines (4 engines, 3.6MW)
- [x] Automation2 researched
- [~] Engine (100+100) in progress -> then "fluid-handling" -> OilProcessing (raw string names; enum lacks them; `fluid-handling` needs `engine` first)
- Other available green techs: advanced-material-processing (75), electric-energy-distribution-1 (120), Logistics2 (200), Solar (250), Landfill

## Audit vs references/pro_ratios.md (2026-11-25) - fixes + gaps
- [x] FIXED: green-block gear chest (18.5,46.5) was EMPTY (gear asm starved -> whole block idle). Refilled 500 iron; topped up all 5 green chests (~350-500 each), red chests (20.5,35.5)=833 Fe, (13.5,32.5)=495 Cu.
- [x] FIXED: 80 green packs carried to lab chests (9.5,38.5)/(24.5,39.5) (40 each) - Engine research (84 left) should finish.
- [ ] GAP science rate: red ~12 SPM (2 asm1), green ~7 SPM vs target 45 SPM. Upgrade to assembler2 (speed 0.75) and add copies; 6 green asm / 5 red asm for 45 SPM.
- [ ] GAP smelting: e-drill 0.5/s vs stone furnace 0.3125/s -> 37% of ore wasted. Research advanced-material-processing (steel furnace 2x) right after Engine.
- [ ] GAP power: 3.6MW ok (1 boiler:2 engines). Hand-fed coal chests: 554 + 385 coal ~ <15 min at full load. Coal needs electric drills + belt.
- [ ] GAP logistics: zero belts; every plate/pack hand-carried. Phase 6 priority 1.

## Phase 6 - Logistics overhaul (IN PROGRESS)
- [x] COAL AUTOMATED: 4 e-drills (42.5/46.5, -95.5/-92.5) -> belt x=44.5 south to y=24.5 -> west y=24.5 to x=4.5 -> south x=4.5 to y=55.5 -> west y=55.5 -> (-6.5,55.5)-(-6.5,54.5)-(-7.5,54.5) -> north x=-7.5 to y=39.5; inserters (-6.5,39.5),(-6.5,43.5) feed boiler chests. ~230 belts. Poles (44.5,-97.5),(40.5,-94),(48.5,-94) + 17-pole line from (6.5,-57.5).
- [x] GREEN PACKS AUTOMATED to lab2: green out belt (22.5,56.5)->(26.5,56.5)->north x=26.5->(26.5,39.5); inserter (25.5,39.5)->chest (24.5,39.5)->ins (23.5,39.5)->lab2. Lab3 (21.5,43.5) chained from lab2 by inserter (21.5,41.5). Lab1 (9.5,35.5) still hand-fed green (chest (9.5,38.5)).
- [x] Engine researched; fluid-handling in progress (50+50) -> then oil-processing (raw strings). advanced-material-processing (75) queued after.
- [x] FURNACE COAL AUTOMATED: coal drill (36.5,-89.5) -> belt y=-89.5 west to x=-17.5 -> south to y=-74.5 -> west along y=-74.5 (copper row) to x=-38.5 -> south x=-38.5 to y=-50.5 -> east along y=-50.5 (iron row) to x=-4.5. Fuel inserters (UP) at furnace x-0.5 (y=-75.5 copper, y=-51.5 iron). Spare coal drill (36.5,-95.5) idle (belt not built).
- [x] PLATE BELTS: long-handed inserters drop plates on y=-49.5 (iron) / y=-73.5 (copper) -> trunks x=-2.5 / x=8.5 south.
- [x] MIXED SCIENCE BUS (Fe one lane, Cu other): iron trunk east along y=22.5 -> (8.5,22.5) merges with copper (side-load from (9.5,22.5)) -> underground (8.5,23.5)->(8.5,25.5) under coal belt -> south x=8.5 to y=32.5 -> east y=32.5 to x=20.5 -> south to y=37.5 -> east to x=28.5 -> south to y=46.5 -> west (underground (27.5,46.5)->(25.5,46.5) under green belt x=26.5) along y=46.5 to x=11.5 -> south x=11.5 to y=56.5 -> east to (18.5,56.5). Old input chests removed; inserters pick straight from the belt. Only red2 copper chest (14.5,39.5) still hand-fed (holds 2541 Cu).
- [x] STEEL: 2 stone furnaces (11,30),(15,30) fed iron by inserters from bus row y=32.5, coal from chests (13.5,30),(17.5,30) (200 coal each, refill occasionally), steel out to chests (10.5,27.5),(14.5,27.5).
- [x] Lab1 retired (picked up); lab4 (17.5,43.5) chained from lab3 via inserter (19.5,43.5). Labs 2,3,4 all fed by green belt + red asm2.
- [x] Assembler2 upgrade: green pack asm (22.5,53.5) and red asm2 (17.5,39.5) are now assembling-machine-2 (needs steel). 
- [x] Spare coal drill removed. Test undergrounds picked up.
- [~] Research: oil-gathering (100+100) running, then "oil-processing" (fails to start until oil-gathering done), then plastics/sulfur/chemical science; electric-energy-distribution-1, logistics-2 next. Crude oil at (-280.5,-313.5) ~420 tiles NW.
- [ ] Next (Phase 8): oil outpost + pipeline/train-free transport (barrel? use long pipe ~420 tiles or build refinery at oil), steel furnaces (6 steel+10 brick each) replacing stone furnaces to remove the drill/furnace imbalance, more assembler2 science copies toward 45 SPM, red asm1 (13.5,35.5) is idle (no lab).
- Hand chores left: refill 5 green-block input chests (plates), red chests, furnace coal.

## Later
- Electric drills, belts, green/red science, oil, rocket silo.

## Rules reminder
- Infinite ore, peaceful, no defense needed. Radius queries <= 40.
- Update log.md every 10-15 execute() calls with coordinates.
