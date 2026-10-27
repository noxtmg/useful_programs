#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

pandoc document.md \
  --from markdown+tex_math_dollars+raw_tex \
  --standalone \
  -o document.docx

pandoc document.md \
  --from markdown+tex_math_dollars+raw_tex \
  --pdf-engine=xelatex \
  --standalone \
  -o document.pdf
