---
title: Session log
---

# Session 1 (2026-11-25)

## Map (spawn 0,0 - empty within r=40)
| Resource | Location | Notes |
|---|---|---|
| Iron ore | patch x -30..4, y -79..-49 | |
| Copper ore | patch x -43..-21, y -83..-61 | north of y=-62; borders iron |
| Coal | ~(40,-85) | 92 from spawn |
| Stone | ~(61,-54) | |
| Water | (-14, 34) | 37 from spawn |
| Trees | (-9, 47) | |

## Factory sections (all burner, hand-fed coal, hand-collected plates)
| Section | Entities | Coordinates |
|---|---|---|
| Coal outpost | 2 burner drills -> 1 wooden chest (self-accumulating, ~800+) | drills (37,-85) & (40,-86); chest (38.5,-85.5) |
| Stone outpost | 1 drill -> chest | drill (61,-54); chest (61.5,-52.5) |
| Iron line | 6 drills y=-63, x=4,2,0,-2,-4,-6 -> furnaces at y=-61 (x=5,3,1,-1,-3,-5) | |
| Iron (extra) | 4 drills y=-61 x=-28..-22 on iron patch edge -> furnaces y=-59 (x=-27,-25,-23) | accidentally iron, ok |
| Copper line | 4 drills y=-72, x=-26,-28,-30,-32 -> furnaces y=-70 (x=-25,-27,-29,-31) | confirmed copper-ore |

| Power | pump (-12.5,34.5) -> boiler (-5.5,37) -> steam engine (0.5,33.5); poles (2.5,33.5),(6.5,33.5) | built near water, hand-fed coal to boiler |
| Lab | lab (9.5,35.5) powered | science packs hand-fed |

| Red science chain (row y=35.5, east of lab) | iron chest (20.5,35.5) -> ins (19.5) -> gear asm (17.5) -> ins (15.5) -> science asm (13.5) -> ins (11.5) -> lab (9.5). Copper chest (13.5,32.5) -> ins (13.5,33.5) -> science asm. Poles at (11.5/15.5/19.5, 33.5) | chests hand-filled with plates (200 each) |

| Pole line | 26 small poles from (19.5,33.5) north to (6.5,-57.5), via connect_entities | single electricity network |
| Electric iron row | 6 units: e-drill (x=-20.5..-5.5 step 3, y=-55.5) -> stone furnace (y=-53) -> inserter (y=-51.5) -> iron chest (y=-50.5, x=-19.5..-4.5 step 3). Poles in gaps at y=-53.5 | plates accumulate in chests (~0.31/s each); furnaces still hand-fueled (20 coal each) |

| Electric copper row | 6 units: e-drill (x=-37.5..-22.5 step 3, y=-79.5) -> furnace (y=-77) -> inserter (y=-75.5) -> chest (y=-74.5, x=-36.5..-21.5). Poles y=-77.5 | furnaces hand-fueled (25 coal) |
| Power v2 | 2nd steam engine (0.5,28.5) chained to engine 1; boiler coal chest (-5.5,39.5) -> inserter (-5.5,38.5) -> boiler; pole line (2.5,29.5),(2.5,39.5),(-0.5,40.5),(-4.5,40.5) | boiler fuel slot only holds ~50 coal, so the chest+inserter is mandatory; chest holds 600 coal (~45 min) |
| Science #2 | gear asm (17.5,35.5) -> inserter (17.5,37.5) -> sci asm (17.5,39.5) -> inserter (19.5,39.5) -> lab 2 (21.5,39.5); copper chest (14.5,39.5) -> inserter (15.5,39.5) | 200 copper hand-filled |

| Power v3 | boiler 2 (-5.5,46) facing DOWN, engines (-5.5,50.5) & (-0.5,50.5); steam pipes y=47.5 x=-5.5..-0.5; water pipe x=-3.5 y=38..45; coal chest (-5.5,43.5)+inserter (-5.5,44.5); pole (-3.5,50.5) | 4 engines = 3.6MW; both coal chests hand-filled |
| Green science block | asm (recipe): cable A (14.5,49.5), gear G (18.5,49.5), belt D (22.5,49.5), circuit B (14.5,53.5), inserter C (18.5,53.5), green pack E (22.5,53.5). Flow: A->B(14.5,51.5) ; B->C(16.5,53.5) ; G->C(18.5,51.5) ; G->D(20.5,49.5) ; D->E(22.5,51.5) ; C->E(20.5,53.5) ; E->out chest (22.5,56.5) | input chests: copper (14.5,46.5); iron (18.5,46.5) gear, (22.5,46.5) belt, (11.5,53.5) circuit, (18.5,56.5) inserter. Green packs must be carried by hand to labs (21.5,39.5)/(9.5,35.5) |

Checkpoints: `bootstrap-burner-mining`, `copper-iron-lines-v1`, `power-lab-automation-done`, `red-science-automated`, `electric-iron-row`, `electric-copper-row`, `power-fix-2nd-science`, `power-3.6MW`, `green-science-built`.

## Audit 2026-11-25 (vs references/pro_ratios.md)
- Found gear chest (18.5,46.5) empty -> green block starved. Refilled; carried 80 green packs to lab chests. Engine research 84/100 left before delivery.
- Chest read gotcha: chests are `iron-chest` not wooden; use get_entities({Prototype.IronChest}, pos, r) and `.inventory`; `inspect_inventory(entity)` printed the player's inventory in my run.
- Rates: red 2 asm1 (0.5 speed, 5s) = 12/min; green 1 asm1 (6s) = 5/min theoretical; target 45 SPM needs assembler2 + more copies.
- Smelting: 12 e-drills at 0.5 ore/s feed stone furnaces at 0.3125/s: 37% idle. Steel furnaces fix it.
- Power ok per ratio; coal supply is the weak link (hand-fed).
- Checkpoint: `audit-refill-v1`.

## Phase 5 findings
- Water/trees limit building south of y~55 near x -10..28: check `can_place_entity` for all machines/chests before committing to a layout. `render` returned a blank grid (not useful).
- Boiler orientation: place with `direction=Direction.DOWN` to flip steam output; I fed 2nd engine by hand-laid pipes at y=47.5. Engines can sit side-by-side if pipes bridge top ports.
- craft_item of engines/boilers eats pipes: I ran out. Keep 40+ pipes.
- Wooden coal chest at outpost caps at 800 coal; ~800 coal/trip is only ~20 min of 2 boilers at full load. Coal automation is the top logistics problem.
- Ore row chests accumulated ~2000 plates each in ~50 min (furnaces ~0.31/s).

## Phase 4 findings
- **insert_item into a boiler/furnace fuel slot caps at one stack (~50 coal)** - my 200+300 "refills" were silently capped, and the boiler ran dry (brownout for a while). Use chest+inserter.
- Power budget: 12 e-drills (90kW) + 3 assemblers + 2 labs + inserters ~ 1.5MW > 1 engine (900kW). 1 boiler (1.8MW) supports 2 engines. Spare: 2 engines + 1 boiler in inventory for the next expansion.
- Loop placing units: the printed index in my error message was off by one; always list entities afterward to confirm what got placed.
- All red-only techs are done (Steel, FastInserter, Logistics, Electric drill, Automation, Logistic pack). Everything else needs green science (Automation2 queued, 40+40).

## Phase 4 results (partial)
- Logistics researched; Electric mining drill needed its own tech: `set_research("electric-mining-drill")` (raw string, not in enum). Steel Processing queued.
- Old burner iron/copper lines still exist; their furnaces cap at 100 plates (FULL_OUTPUT) - harvest by hand.
- Remaining manual chores: boiler coal (200 added), furnace coal, refill science chests (20.5,35.5)/(13.5,32.5) from the new iron chests.
- Electric drill (0.5 ore/s) outpaces stone furnace (0.31/s): a 2nd furnace per drill or steel furnaces would raise output.

## Phase 3 results
- Red science runs unattended while chests have plates. ~1 pack / 10s (one assembler1 is bottleneck).
- Inserter direction: `Direction.LEFT` inserter picks from east tile, drops to west tile (pickup = pos+1 on x). Direction = drop direction.
- Technology enum names: `LogisticsSciencePack`, `SteelProcessing`, `Logistics`, `Electronics`, `FastInserter`, etc. (use `dir(Technology)`).
- `get_entity(Lab)` can throw an AttributeError ('list' has no 'items') when the lab inventory is empty; use get_entities or skip.
- Boiler burns ~1 coal/few s at load; hand-feed (had 43 left after ~5 min).
- Researching: LogisticsSciencePack (75 red).

## Phase 2 results
- Automation researched (10 red packs). Assembler craftable.
- Design decision: lab at the power plant (water) and hand-carry packs, instead of ~14 poles to the ore field.
- connect_entities(pump, boiler) needed 17 pipes; craft pipes in bulk (40).
- `craft_item(Lab)` failed once on "missing gears" after partially crafting; craft gears/belts/circuits first manually.
- Wood: trees are sparse near (-9,47); `nearest(Wood)` moves; loop harvest to reach 47 wood.

## Lessons
- `fle://status` initially "Failed to connect"; `reconnect()` fixed it.
- `nearest()` is relative to player position; coordinates I assumed for copper were wrong (it was iron). Verify with `drill.resources` after placing.
- Game runs fast: sleep(15) gave a chest 800 coal. Chests at drop positions are very effective.
- Drill drop_position must land on the chest tile; shifted drill by 1 tile when it missed.
- Furnaces fill to 100 plates (FULL_OUTPUT) -> must hand-collect; automation (inserters/belts) is next step.

## Inventory at end of milestone
~200 iron plates, 400 stone, ~200 coal.
