#!/bin/zsh
# Refresh the plugin's command copies from .claude/commands, then run the eval suite.
# Usage: ./run-evals.sh [extra claude plugin eval flags, e.g. --case 'enemy-*' --runs 1]
set -e
cd "${0:A:h}"
for c in enemy encounter read-aloud; do cp ../.claude/commands/$c.md commands/$c.md; done
# --scaffold: encounter cases copy enemy.md into the sandbox (see evals/encounter-*/setup.sh)
# --judge-model sonnet: the default Haiku judge passed outputs that broke the rules
claude plugin eval --trust-plugin --scaffold --judge-model sonnet "$@" .
