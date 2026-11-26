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

## Manual maintenance (until electric inserters)
- 30 output-side burner inserters (rows at y=-36.5 / -25.5, plus chest inserters) cannot refuel from plates.
  Loaded with ~25-30 coal each; refill about every 20 min of game time.
- Stone drill: ~48 coal loaded.
