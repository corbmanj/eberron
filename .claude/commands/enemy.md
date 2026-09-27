# Enemy Generator

When this command is invoked, create a fully formatted D&D 5e enemy stat block for use in a homebrew Eberron campaign. Use the format and rules below exactly.

## Invocation

`/enemy [description of the creature — type, role, context, approximate party level]`

Example: `/enemy a corrupted celestial construct native to Irian, guardian role, party is level 9`

---

## Stat Block Format

Use this structure in this order, every time:

---

### [Enemy Name]

*[Size] [Type], [Alignment]*

*[1-2 sentences: what this creature is, where it comes from, and why it behaves the way it does. No more.]*

| | |
|---|---|
| **AC** | X (source) |
| **HP** | X (XdX+X) |
| **Speed** | X ft [, Fly X ft (hover) / Swim X ft / Climb X ft] |
| **STR** | X (+X) |
| **DEX** | X (+X) |
| **CON** | X (+X) |
| **INT** | X (+X) |
| **WIS** | X (+X) |
| **CHA** | X (+X) |

**Saving Throws:** [omit line if none]
**Skills:** [omit line if none]
**Damage Resistances:** [omit line if none]
**Damage Immunities:** [omit line if none]
**Condition Immunities:** [omit line if none]
**Senses:** X ft, passive Perception X
**Languages:** [omit line if none]

---

**Traits:**

[Each trait on its own paragraph. Bold name, period, description.]

---

**Actions:**

[Non-spell actions only. Multiattack first if present, then attacks, then recharge abilities. If an action uses a "Melee Spell Attack" or "Ranged Spell Attack" roll but is NOT a named spell from a spell list, it stays here — label it *(Spell-like — not counterspellable)* if there's any risk of confusion.]

---

**Spells:** *(Spell save DC X, Spell attack +X)*

[Omit this entire section if the creature has no true spells.]

| Spell | Level | Uses | Counterspellable |
|-------|-------|------|-----------------|
| *Spell Name* | Xth | X/day | ✓ |
| *Spell Name* | Cantrip | At will | ✓ |

[Add a note if any spell has unusual casting conditions or is used as a reaction.]

---

**Tactics:**
- [How does it open combat?]
- [Who does it prioritize?]
- [How does it use specific abilities — which ones does it hold, which does it use immediately?]
- [Does it retreat, fight to the death, protect something, or coordinate with allies?]

---

**Loot:**

[See loot rules below.]

---

## Rules

### Speed
Always list Speed as its own row near the top of the stat table, before ability scores. If the creature can't walk, list "0 ft" followed by its actual movement type. Never omit this row.

### Spells vs. Spell-like Abilities
This distinction matters for counterspell.

**True spells (counterspellable):** Named spells from a spell list, or innate spellcasting that says "the creature can cast [spell name]." These go in the Spells section with ✓ in the Counterspellable column.

**Spell-like abilities (NOT counterspellable):** Creature-specific abilities that use a Spell Attack roll or Spell Save DC as a mechanic, but are not named spells. These stay in Actions. Examples: a construct's energy beam, a dragon's breath weapon described as a spell save. Label them *(Spell-like — not counterspellable)* if needed.

When in doubt: if the ability names a spell from a spell list, it's counterspellable. If it's a custom creature ability that just uses spell mechanics, it isn't.

### Loot
Every stat block ends with a Loot entry. Use your judgment:

- **Constructs, spirits, elementals:** Almost always `None.`
- **Undead:** Usually `None.` — exceptions for intelligent undead carrying specific items
- **Beasts:** Harvestable materials. Format: *Perception DC X to harvest [material] — [brief use or value].*
- **Humanoids:** Personal effects plus a roll on a standard table, or a specific story-relevant item if appropriate. Reference DMG Individual Treasure tables by CR range when using random tables.
- **Boss creatures:** Always something notable — a unique magic item, a story object, or exceptional materials. Never `None.` for a boss.
- **Cult members:** Usually personal effects + possibly a mission-relevant item (journal, key, sending stone, etc.)

Keep loot entries short. One to three lines maximum.

---

## What NOT to do

- Do not put spells in the Actions section
- Do not put non-spell abilities in the Spells section
- Do not omit the Speed row
- Do not omit the Loot entry
- Do not omit the Spells section header if the creature has true spells — the DM needs to see it at a glance
- Do not write more than two sentences in the flavor description
