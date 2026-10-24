---
doc: prd
status: draft
---
# Canon Keeper — Product Requirements
A continuity checker for solo serial-fiction writers. Source: `scope.md > The Unique Kernel`, `scope.md > The Core Loop`.

## The Core Journey
1. Writer has `canon.json` (facts with sources) and a new `chNN.md`.
2. Runs `python3 -m canonkeeper check canon.json chNN.md --html report.html`.
3. Terminal prints each issue: line number, entity.attribute, canon value + source, found value, the line.
4. Opens `report.html`: the full chapter with offending lines highlighted and a margin note.
5. Fixes the chapter, re-runs → "0 issue(s)", exit code 0.
6. Runs `python3 -m canonkeeper learn canon.json chNN.md` → new facts (e.g. Tavi's sister Wren) are appended with source; existing facts are never overwritten.

## Screens and Layout
CLI output; one static HTML report page (header, verdict line, numbered chapter lines).

## Look and Feel
Dark (#111418) page, serif body, gold title, red highlight + note for issues, green verdict when clean.

## Features and Behavior
### Check
- [ ] Detects a changed physical trait (eyes/hair) vs canon.
- [ ] Detects a dead character acting (said/laughed/walked…).
- [ ] Consistent facts produce no findings. Exit code 1 if issues, 0 if clean (CI-friendly). `--json` for machine output.
### Learn
- [ ] Adds unknown facts with `chapter:line` source; never overwrites canon.

## States and Boundaries
- **Clean chapter** — "Canon intact ✓".
- **Unknown entity** — ignored (no false alarms).
- **Persistence** — only `canon.json`, updated by `learn`.

## Product Decisions
- Rule-based, offline extraction — reproducible for judges, free. (Assumption by agent; Nico to confirm.)

## What We're Building
check, learn, HTML report, sample world, tests.

## Deferred From the POC
LLM extraction, timelines, multi-file projects.

## Possible Later Enhancements
VS Code / Obsidian plugin; GitHub Action that blocks a chapter PR on canon breaks.

## Non-Goals
Not a grammar checker; not a writing assistant.

## Open Questions
None blocking.
