# Encounter Generator

When invoked, generate a complete D&D 5e encounter including:
1. An encounter summary with difficulty tier and monster roster
2. Full stat blocks for each unique enemy type (using the enemy format)
3. A battle map description for ChatGPT to generate a Roll20 map

## Invocation

`/encounter [setting/location] [difficulty: easy/medium/hard/deadly/unwinnable] [any constraints: enemy types, narrative context, specific creatures to include or exclude]`

Example: `/encounter corrupted meadow in Irian, hard difficulty, twisted constructs of light, party is level 9`

---

## Party Baseline

Unless told otherwise, assume: **4 players, level 9.**

If the user specifies a different party size or level, adjust monster CR and quantity accordingly.

---

## Difficulty Tiers

Use these as guidelines for calibrating monster CR and count to party level:

**Easy** — The party will spend resources but face no serious danger. Low CR monsters or small numbers of moderate CR monsters. Likely over in 2–3 rounds.

**Medium** — A real fight that costs the party meaningful resources. Mix of CR appropriate to party level. Someone might drop to low HP.

**Hard** — A fight the party might lose if they play poorly. High CR monsters or large numbers. Multiple PCs likely drop below half HP. Resource management matters.

**Deadly** — A fight that could kill characters. Boss-tier CR, multiple dangerous abilities, or overwhelming numbers. Should feel like a genuine threat to survival.

**Unwinnable** — Not designed to be fought. Build it to be obviously unsurvivable — far beyond deadly. Always include a DM note with the intended escape route or creative solution.

---

## Monster Selection Guidelines

- Vary CR within an encounter where possible — a mix of a strong leader and weaker support is more interesting than identical enemies.
- For custom enemies with no official CR, estimate CR based on AC, HP, average damage per round, and special abilities. Note the estimated CR.
- Consider how monster abilities interact — enemies that combo well (one restrains, another attacks with advantage) make for more memorable fights.

---

## Output Format

Produce output in this order:

---

### Encounter Summary

```
Difficulty:  [Easy / Medium / Hard / Deadly / Unwinnable]
Party:       [X players, level X]

Monster Roster:
  [X]× [Monster Name] — CR [X]
  [X]× [Monster Name] — CR [X]

[1–2 sentences on what makes this encounter tactically distinctive — the key threat, the ability the DM should watch, what the monsters are trying to accomplish.]
```

---

### Stat Blocks

One complete stat block per unique enemy type, using the format from `.claude/commands/enemy.md` exactly. Do not abbreviate. Do not skip sections. If a monster has no spells, omit the Spells section entirely. Every stat block ends with a Loot entry.

---

### Battle Map Description

A description the DM can paste directly into ChatGPT to generate a Roll20 battle map.

**Perspective — state this at the very start, and repeat it at the end:**
> This map must be rendered in a strict top-down, directly overhead bird's-eye view. The camera is directly above looking straight down, as if the map were a floor plan. Not isometric. Not perspective. Not a three-quarter view. Directly overhead — the viewer is looking straight down at the ground.

**Contents:** Terrain and environment only. No creatures. No tokens. No grid.

**Map size:** State the map dimensions in feet. Scale to the encounter — a 3-monster skirmish typically needs 60×60 to 60×80 ft. A large mob fight may need 80×100 ft.

**Terrain:** Describe:
- Ground surface type and texture
- 3–5 specific terrain features that provide cover, elevation changes, or tactical variety (rocks, trees, rubble, water, walls, fallen columns, etc.)
- Environmental details that establish the location (color palette, lighting quality, any unique features of the setting)
- If relevant: any environmental hazards the encounter uses

**End the description with:**
> Style: painterly and detailed, similar to a professional tabletop RPG battle map. Rendered strictly from directly above — top-down, no perspective, no isometric angle.

---

## What NOT to do

- Do not include XP values — this campaign uses milestone leveling
- Do not put all monsters at the same CR — varied rosters are more interesting
- Do not write a battle map description that implies any viewpoint angle other than directly overhead
- Do not include creatures, tokens, or a grid in the battle map description
- Do not omit the Loot entry from any stat block
- Do not mix spells and non-spell actions in the same section
