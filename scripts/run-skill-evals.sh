#!/bin/zsh
# Run the eval suite for the campaign skills in .claude/skills/.
# Cases live in evals/<skill>/<case>/ and are tagged with their skill's name.
# The repo root is packaged as a plugin (.claude-plugin/plugin.json) so every
# skill loads together; the encounter skill needs to read the enemy skill.
#
# Usage:
#   scripts/run-skill-evals.sh                   # every skill
#   scripts/run-skill-evals.sh enemy read-aloud  # just these skills
#   scripts/run-skill-evals.sh enemy -- --runs 1 --case 'enemy-boss*'
#
# Anything after -- is passed to `claude plugin eval`.
# --judge-model sonnet: the default Haiku judge passed outputs that broke the rules.
set -e
cd "${0:A:h}/.."
tags=()
extra=()
while (( $# )); do
  if [[ "$1" == "--" ]]; then shift; extra=("$@"); break; fi
  tags+=(--tag "$1"); shift
done
claude plugin eval --trust-plugin --judge-model sonnet --no-publish -j 3 --threshold 0 "${tags[@]}" "${extra[@]}" .
