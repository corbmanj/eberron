# Eberron Campaign — Claude Instructions

## Read Aloud Text

Whenever writing Read Aloud text blocks in any session document, always apply the rules defined in the read-aloud skill (`.claude/skills/read-aloud/SKILL.md`). This applies automatically — do not wait to be asked.

The short version:
- Visually rich and specific — enough detail for players to picture the space
- Grounded and conversational — reads naturally aloud at a table
- Concrete sensory details only — no moods, impressions, or emotional labels
- No metaphors that don't make physical sense
- Short sentences, present tense
- Never tell the players how to feel

## Encounters

Whenever building an encounter, apply the format from the encounter skill (`.claude/skills/encounter/SKILL.md`). This campaign uses milestone leveling — never include XP values. Always include a battle map description.

When writing encounters as part of a session document, split each encounter into its own file in the same session directory. Name files descriptively: `encounter_[location]_[creature].md` (e.g. `encounter_floor4_void_bats.md`). In the session document, replace the encounter block with a single reference line linking to the file. The session document handles narrative flow; the encounter file handles stat blocks, tactical notes, and battle map.

## Enemy Stat Blocks

Whenever writing enemy stat blocks in any session document, always apply the format defined in the enemy skill (`.claude/skills/enemy/SKILL.md`). This applies automatically — do not wait to be asked.

The short version:
- Speed is always its own row near the top of the stat table
- Actions and Spells are separate sections — never mix them
- Spells section includes a table with spell level, uses per day, and counterspellable (✓) indicator
- Abilities that use spell attack rolls but are not named spells stay in Actions, labeled as not counterspellable
- Every stat block ends with a Loot entry, even if it just says "None."
