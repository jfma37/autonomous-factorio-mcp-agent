---
title: Infinite-resource drill yield and API quirks
date: 2026-11-26
---
- With `sonaxaton-infinite-resources`, one burner drill delivered ~20 coal/s (200 coal in 10 s into a chest).
  A 16-slot wooden chest (800 coal) filled in well under a minute.
  So one burner drill per resource likely saturates a yellow belt (iron/copper/stone rates not yet measured).
- A drill facing into another drill fuels it (coal chain works).
- Belt lanes: an end-on inserter feeding a westward belt drops on the north lane, which blocks a north
  side-load. Fix used: inserter perpendicular from the north (drops on the south lane).
- `place_entity` fails with "something is in the way" for trees (harvest them) and for drills off the ore,
  even when `can_place_entity` returns True.
- Max placement reach is 10 tiles. Burner inserter `direction` = item flow direction.
- Starting kit: 1 burner drill, 1 stone furnace, 5 wood, 8 iron plates.
- MCP link may report "Failed to connect" at session start: call `reconnect`.
- `Prototype.X` is not subscriptable; use `Prototype.X.value[0]` for the name.
- Burner drill at integer center (x,y), facing DOWN: furnace at (x, y+2) catches ore.
  Facing LEFT: drop position (x-1.5, y+0.5).
