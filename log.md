---
title: Run log - Vanilla 2.0 Rocket Launch
---
# 2026-11-26 - Session 1: Phase 1 complete (FLE tag `phase1_complete`)

Seed 44340. MCP needed `reconnect` at start. `render` returned an empty grid.

## Resource patches (bounding boxes)
| Resource | Left-top | Right-bottom |
|---|---|---|
| Iron | (-30.5,-79.5) | (3.5,-49.5) (irregular: x=0,y=-51 not mineable) |
| Copper | (-43.5,-83.5) | (-21.5,-61.5) |
| Coal | (34.5,-101.5) | (52.5,-82.5) |
| Stone | (55.5,-69.5) | (71.5,-54.5) |
| Water | nearest (-14,34) | - |

## Built
**Coal**: burner drill (44,-88) facing LEFT; self-fuel inserter (43.5,-86.5).
Belt: (42.5,-87.5) -> (42.5,-85.5) -> (44.5,-85.5) -> (44.5,-84.5) -> (14.5,-84.5) -> south on x=14.5,
with detours to x=12.5 at y=-43.5..-42.5 and y=-32.5..-31.5; ends (14.5,-30.5).
(One stale coal tile may remain at (14.5,-29.5).)

**Drill fuel branches**
- Iron drill: transfer inserter (13.5,-54.5), belt y=-54.5 west to -9.5, drill inserter (-9.5,-53.5).
- Copper drill: transfer inserter (13.5,-68.5), belt y=-68.5 west to -31.5, drill inserter (-31.5,-67.5).

**Iron row** (12 stone furnaces, centers x=7,5,...,-15, y=-38)
- Drill (-10,-52) DOWN; ore belt (-9.5,-50.5) -> y=-44.5 -> east to x=10.5 -> side-loads input belt.
- Input belt y=-40.5 (12.5 -> -14.5, westward); coal inserter (12.5,-41.5) DOWN.
- Input inserters (x+0.5,-39.5); output inserters (x+0.5,-36.5); output belt y=-35.5 (7.5 -> -18.5).
- Chests: wooden (-20.5,-35.5), iron (-17.5,-37.5), (-18.5,-37.5).

**Copper row** (12 furnaces, same x, y=-27)
- Drill (-32,-66) DOWN; ore belt (-31.5,-64.5) -> y=-33.5 -> east to x=10.5 -> side-loads input belt.
- Input belt y=-29.5; coal inserter (12.5,-30.5) DOWN.
- Input inserters y=-28.5; output inserters y=-25.5; output belt y=-24.5.
- Chests: wooden (-20.5,-24.5), iron (-17.5,-26.5), (-18.5,-26.5).

**Stone**: burner drill (62,-60) LEFT -> wooden chest (60.5,-59.5). HAND FUELLED.

## Verified state at end
All furnaces had worked; ~570 iron and ~570 copper plates in the main chests plus ~48 in each iron chest.
FULL_OUTPUT on 7-8 furnaces per row: chest inserters are the bottleneck.

# 2026-11-26 - Session 2: Phase 2 complete (FLE tag `phase2_complete`)
Restored from 6ba2978 (reconnect needed twice). The "Manual maintenance" section below is Session 1 history.

**Power**: pump (-13.5,33.5); pipe to boiler water port (-4.5,27.5), single pipe (2.5,27.5).
Boilers (facing UP) y=27, x=-2.5,0.5,4.5,7.5; engines same x at y=23.5 and 18.5.
Boiler burner inserters y=28.5; coal belt y=29.5 (westward) fed by x=14.5 column from y=-29.5.
Poles y=21.5 at x=-4.5,2.5,9.5; trunk north on x=9.5 up to y=-31.5, then to coal area.

**Inserters**: all output-side/chest inserters in both rows are now electric; poles in rows y=-36.5 and y=-25.5.
Input-side inserters are still burner (self-fuel from the mixed coal lane).

**Coal**: electric drills (36.5,-86.5), (40.5,-86.5), (36.5,-82.5), (40.5,-82.5), (44.5,-82.5) onto belt y=-84.5;
poles x=38.5/42.5. Old burner drill (44,-88) kept as no-power blackstart.

**Research**: lab at (20.5,10.5); `set_research("electric-mining-drill")` completed (not in Technology enum; pass string).

**Verified**: 8/8 engines and 4/4 boilers WORKING; inserters powered; belts backed up (supply >= demand).
Stone burner drill (62,-60) still hand fuelled (800 stone buffered).

## API quirks
- get_entity/get_entities fail on an empty or freshly researching lab ('list' has no 'items'); get_entities returns [].
  Feed it with insert_item on a model_copy of another entity (name='lab', position); items insert despite the parse error.
- can_place_entity / place_entity only work within ~10 tiles of the character.
- connect_entities on a long belt can report ok yet build nothing: verify the belt count.

# 2026-11-26 - Session 3: Phase 3 complete (FLE tag `phase3_complete`)
Burner drills on iron/copper/stone and both drill fuel belts (y=-54.5, y=-68.5) are removed.
Chest inserters and both end wooden chests are removed: plates now flow to science.

**Drills**
- Iron: 8 drills x=-11.5/-7.5, y=-53.5..-62.5 (step 3), belt x=-9.5 southward; poles x=-13.5/-5.5, (-9.5,-64.5).
- Copper: 8 drills x=-33.5/-29.5, y=-65.5..-74.5, belt x=-31.5 southward; poles x=-35.5/-27.5.
- Stone: 2 drills (58.5,-59.5),(62.5,-59.5) into wooden chest (60.5,-59.5).

**Red science**
- Iron: (-19.5,-35.5) west to x=-27.5, underground y=-34.5/-32.5, south to y=-17.5, west to x=-30.5, south to y=-14.5.
- Copper: (-19.5,-24.5) west to x=-22.5, south to y=-15.5.
- Gear asm (-27.5,-14.5), inputs (-27.5,-16.5),(-29.5,-14.5), output (-25.5,-14.5).
- Mixed input belt y=-14.5 eastward (copper north lane, gears south lane).
- 5 red asm y=-11.5, x=-19.5..-3.5 (step 4); output belt y=-8.5 westward, then x=-23.5 south.
- 6 labs y=-2.5, x=-20.5..-0.5, daisy chained by inserters. Next lab slot x=3.5.
- Old lab (20.5,10.5) is unfed.

**Storage** (not auto-filled): iron chests (-17.5/-18.5, -37.5 and -26.5) hold plates; (-17.5,-37.5) also 229 ore.
Wooden chests: iron (-18.5,-31.5), copper (-17.5,-20.5).

**Research done**: electric drill, automation, logistics, logistic-science-pack, steel-processing.

**Quirks**
- In `execute`, use one placement per line with uniquely named loop vars: `P(...); P(...)` inside a loop used a stale x.
- Underground exit: place with the reversed direction, then `rotate_entity` to the travel direction.
- Inventory fills up around 3000 iron + 1000 coal.

## Manual maintenance (until electric inserters)
- 30 output-side burner inserters (rows at y=-36.5 / -25.5, plus chest inserters) cannot refuel from plates.
  Loaded with ~25-30 coal each; refill about every 20 min of game time.
- Stone drill: ~48 coal loaded.
