#!/usr/bin/env bash
# Create a new wheel from the template.
# Usage: tools/new-wheel.sh "short name of the question"
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
name="${1:-}"
if [ -z "$name" ]; then
  echo "usage: tools/new-wheel.sh \"short name\"" >&2
  exit 1
fi

slug="$(echo "$name" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g')"
last="$(ls "$root/wheels" 2>/dev/null | grep -E '^[0-9]{3}-' | sort | tail -1 | cut -c1-3 || true)"
next="$(printf '%03d' $(( ${last:-0} + 1 )))"
dir="$root/wheels/$next-$slug"

cp -R "$root/templates/wheel" "$dir"
today="$(date +%Y-%m-%d)"
sed -i '' -e "s/^# NNN:.*/# $next: $name/" -e "s/YYYY-MM-DD/$today/" "$dir/README.md"

echo "created $dir"
echo "next: fill in README.md (question, boundary, success criteria) before anything else"
