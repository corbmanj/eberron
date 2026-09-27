#!/bin/bash
# The encounter command reads .claude/commands/enemy.md from the working directory.
# Recreate that path inside the eval sandbox so the command sees the real enemy format.
set -e
mkdir -p .claude/commands
cp /Users/jordancorbman/Documents/eberron/.claude/commands/enemy.md .claude/commands/enemy.md
