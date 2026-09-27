# Encounter: The Ritual Chamber

---

### Encounter Summary

```
Difficulty:  Hard (with environmental urgency)
Party:       4 players, level 10

Monster Roster:
  1× Soreth, Voice of Silence — CR 10
  2× Cultist of the Severed Tongue — CR 2

The ritual is in progress when the party arrives. Soreth uses Ritual Drain on her
turn every round, advancing the ritual toward completion. At Stage 5, the rift
opens regardless of whether she is alive. This creates two parallel pressures:
stopping Soreth AND stopping the ritual before it advances too far.

The ritual circles in the center of the room are not obstacles — they are hazards.
A creature that steps INTO a circle disrupts it. This is safe for party members
(the circle releases its captive), but Soreth will attempt to maneuver the party
near the circles and use them as threat vectors. She may force a save by knocking
someone into a circle boundary with her Glyph Strike.
```

> **Ritual Stages:** The ritual has 5 stages. Soreth advances it by one stage per use of Ritual Drain. Describe each stage's environmental effect aloud as it happens — do not announce stage numbers to players.
>
> - **Stage 1:** The three circles glow brighter. The captives' postures stiffen slightly.
> - **Stage 2:** The room temperature drops noticeably. Breath becomes visible. The walls begin to sweat condensation.
> - **Stage 3:** Fragments of the captives' voices are audible even though their mouths aren't moving — half-words, names, the edges of sentences.
> - **Stage 4:** The stone floor beneath each circle develops cracks running outward like roots. The cracks are cold to the touch.
> - **Stage 5:** The ritual completes. The rift tears open (see session document). If Soreth is still alive, she does not need Final Silence. If she is at 0 HP, Final Silence fires as a reaction.

---

## Monster Stat Blocks

### Cultist of the Severed Tongue

*Refer to* [encounter_dream_four_waves.md](../session%207/encounter_dream_four_waves.md) *for the full stat block.*

```
AC 13 | HP 32 | Speed 30 ft
Severed Vow: immune to verbal-component effects, can't speak
Glyph-Marked: on hit, DC 13 CON or target silenced until end of next turn
Multiattack: shortsword (+4, 1d6+2) + curved dagger (+4, 1d4+2)
```

These two cultists function as positioning tools — they use Shove to push party members toward the ritual circles and toward Soreth. They do not use Glyph-Marked unless the opportunity is convenient.

---

### Soreth, Voice of Silence

*Medium Humanoid (human), neutral evil*

*The Severed Tongue's ritual master in Sharn, who carved the glyph into her own tongue twenty years ago and has not spoken since. She runs the ritual with the calm of someone who has prepared for this for a long time.*

| | |
|---|---|
| **AC** | 16 (glyph-inscribed robes) |
| **HP** | 143 (22d8+44) |
| **Speed** | 30 ft |
| **STR** | 10 (+0) |
| **DEX** | 14 (+2) |
| **CON** | 14 (+2) |
| **INT** | 19 (+4) |
| **WIS** | 16 (+3) |
| **CHA** | 16 (+3) |

**Saving Throws:** INT +8, WIS +7, CHA +7
**Skills:** Arcana +8, History +8, Religion +8
**Condition Immunities:** Charmed, Frightened
**Senses:** Truesight 30 ft, passive Perception 13

---

**Traits:**

**Severed Vow.** Soreth cannot speak and is immune to any effect requiring her to hear or produce a verbal component, including as a target of *Command* or similar spells.

**Voiceless Spellcasting.** Soreth can cast any spell she knows without its verbal component. She still requires somatic and material components where applicable.

**Ritual Focus.** While within 10 ft of an active ritual circle, Soreth has advantage on Constitution saving throws to maintain Concentration and adds her proficiency bonus to all spell attack rolls.

**Final Silence.** When Soreth is reduced to 0 hit points while the ritual is at Stage 3 or higher, she uses her reaction to advance the ritual to Stage 5, completing it immediately. She then falls unconscious.

---

**Actions:**

**Multiattack.** Soreth makes two Glyph Strike attacks. She may replace one of these attacks with Ritual Drain.

**Glyph Strike.** *Ranged Spell Attack:* +8 to hit, range 60 ft. *Hit:* 17 (3d8+4) necrotic damage. The target must succeed on a DC 16 Constitution saving throw or have disadvantage on their next Concentration saving throw. *(Spell-like — not counterspellable.)*

**Ritual Drain.** Soreth draws a fragment of memory from one captive within a ritual circle within 30 ft. The captive takes 11 (2d10) psychic damage and the ritual advances one stage. The captive produces an involuntary sound — a gasp, a word, a name — the only noise from them during the encounter. *(Spell-like — not counterspellable.)*

---

**Spells:** *(Spell save DC 16, Spell attack +8)*

| Spell | Level | Uses | Counterspellable |
|-------|-------|------|-----------------|
| *Counterspell* | 3rd | 3/day | ✓ |
| *Dispel Magic* | 3rd | 2/day | ✓ |
| *Synaptic Static* | 5th | 2/day | ✓ |
| *Greater Invisibility* | 4th | 1/day | ✓ |
| *Eyebite* | 6th | 1/day | ✓ |

*Counterspell: Used on party spells of 5th level or higher. She will burn all three uses.*

*Greater Invisibility: Cast on herself in the opening round if she had any warning the party was coming. Otherwise held until below half HP.*

---

**Tactics:**
- Opens with Ritual Drain on her first turn, regardless of what the party is doing. The ritual advancing is her priority — she will not sacrifice a Drain to deal damage if she has the action.
- Stays within 10 ft of the nearest ritual circle to maintain Ritual Focus as long as possible.
- Glyph Strike targets concentration-dependent party members. The follow-on disadvantage on concentration saves is the point.
- Counterspell is used on spells of 5th level or higher. She does not waste slots on lower-level spells unless a cantrip is doing exceptional damage.
- Synaptic Static (INT save DC 16, 8d6 psychic, fail = –1d6 on attack rolls and ability checks until end of next turn) when 3 or more party members cluster within 30 ft of each other.
- Greater Invisibility when she drops below 70 HP. Her ritual circles are easy to locate even invisible, so she moves away from them while maintaining the drain effect on her next turn as a ranged action.
- Eyebite on the party's highest-damage dealer: sickened condition first (disadvantage on attacks and ability checks), then incapacitated if the sickened effect holds.
- She does not retreat. She believes in what she's doing.

---

**Loot:** A sealed journal in cipher (contains the ritual's full design — its purpose, its commissioner, and what it feeds). A set of glyph tools (ritual instruments, worth 200 gp to the right buyer). A sending stone, cold and unresponsive — whoever it was keyed to is no longer answering. Roll DMG Individual Treasure (CR 11–16).

---

## Battle Map Description

> This map must be rendered in a strict top-down, directly overhead bird's-eye view. The camera is directly above looking straight down, as if the map were a floor plan. Not isometric. Not perspective. Not a three-quarter view. Directly overhead.

**Map size:** 70×70 ft. The lower chamber of the old Cannith forgeworks — but this space predates the forgeworks. The walls curve inward slightly, forming a shallow dome. The floor is older stone than anything above. Dhakaan-era carvings run along the base of the walls in vertical columns.

**Terrain:**

- **Ritual circles (3 total):** Each circle is 10 ft in diameter, carved directly into the floor and burning with pale blue-white light. Arranged in a triangle formation in the center of the room, points of the triangle facing north, southwest, and southeast. Each circle contains one captive (Savia in the north circle, Bixum in the southwest, Umberto in the southeast). The circles are 5 ft apart at their nearest points. A creature entering a circle disrupts it — the captive is released, and the circle goes dark. The light from three active circles provides dim illumination across the full center of the room; one or two active circles reduces the center to dim; all three dark = only the party's own light sources.

- **Outer ring (perimeter of the room):** 10 ft of clear stone floor between the ritual circles and the walls. This is where the cultists stand. No cover at the walls — the carvings are decorative, not structural. The floor is flat and unobstructed.

- **Staircase (north wall):** The entry point. The stairs emerge into the north section of the room, between the perimeter and the north ritual circle. The opening is 10 ft wide.

- **Standing stones (4 total):** Knee-height flat-topped stones, roughly 3×3 ft, positioned at the four cardinal points of the room — north, south, east, west. Each has a ritual ink mark on its surface. They provide no cover (too low) but serve as anchor points for the ritual — the containment fails if all four are overturned or their marks are disrupted (requires an action per stone, DC 14 Arcana to recognize this). Disrupting two standing stones reduces the ritual by one stage (it does not pause — Soreth can re-advance it, but it costs her turns).

- **Lighting:** The ritual circles provide dim light across the central third of the room. The outer ring is in darkness unless the party brings their own light. There are no installed light sources — the gas lamps stop at the upper level.

- **Ceiling:** 15 ft at the walls, 20 ft at the apex of the dome. No handholds, no fixtures, no chains. Flying creatures have full movement but no advantage from terrain — the dome curves in, not out.

**Starting positions:**
- Soreth: center of the room, between the three ritual circles, facing the staircase.
- Two cultists: one at the east perimeter, one at the west perimeter.
- Three captives: one in each ritual circle, each in a position corresponding to their circle (Savia upright, Bixum seated, Umberto kneeling).

If the party arrived stealthily enough that Soreth did not hear them (DC 15 group Stealth check coming down the stairs), Greater Invisibility is not active — she is mid-ritual, not prepared for a fight. Otherwise, assume she cast it at the top of the stairs.

> Style: ancient and deliberate — Dhakaan stone beneath Cannith construction, ritual circles older than the building above them. Strict top-down, no perspective, no isometric angle.
