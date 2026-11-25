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

## Phase 6 - Logistics overhaul (NEXT)
- [ ] Hand chores now: (1) carry green packs from (22.5,56.5) to lab chests (9.5,38.5) & (24.5,39.5); (2) refill 5 green-block input chests with plates; (3) refill science red chests; (4) refill boiler coal chests (-5.5,39.5),(-5.5,43.5); (5) refuel 12 ore furnaces
- [ ] Biggest win: coal automation (electric drills on coal + belt to boilers ~120 tiles, or move boilers; solid fuel later) and belts of plates ore->base (~100 tiles)
- [ ] Unified science: belt red+green to a lab row (labs can't be read by get_entity when empty - use chest+inserter feeding)
- [ ] Steel production (steel-processing done), research module/oil path: oil-processing, plastics, sulfur, blue science
- [ ] Find crude oil (use nearest(Resource.CrudeOil))

## Later
- Electric drills, belts, green/red science, oil, rocket silo.

## Rules reminder
- Infinite ore, peaceful, no defense needed. Radius queries <= 40.
- Update log.md every 10-15 execute() calls with coordinates.
