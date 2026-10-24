---
doc: spec
status: draft
---
# Canon Keeper — Technical Spec

## How This Works, In Plain Language
Canon is a JSON file: for each character, a list of facts and where each fact came from. A small set of sentence patterns reads the chapter and pulls out facts like "Mira's eyes were green". Each pulled fact is compared with canon; a mismatch becomes a finding. `learn` adds facts canon didn't have yet. A report page shows the chapter with the bad lines in red.

## The Core Journey Through the System
chapter text → `core.extract` (regex patterns) → `core.check` (compare with `canon.facts`) → findings → CLI print + `report.render` HTML. PRD ref: `prd.md > The Core Journey`.

## Stack
Python 3.10+ standard library only (argparse, json, re, html, unittest). Docs: https://docs.python.org/3/library/re.html

## Where It Runs and How Someone Tries It
Local command line, any OS with Python 3.10+. No keys.
`python3 -m canonkeeper check samples/canon.json samples/ch03.md --html report.html` then open `report.html`. Tests: `python3 -m unittest -v tests.test_core`.

## Look and Feel
See `prd.md > Look and Feel`; implemented as inline CSS in `report.py`.

## Components
### core.py — extract / check / learn
PRD ref: `prd.md > Check`, `prd.md > Learn`.
### report.py — HTML report
PRD ref: `prd.md > Screens and Layout`.
### __main__.py — CLI
PRD ref: `prd.md > The Core Journey`.

## Data Model
`{"world": str, "facts": {Entity: {attribute: {"value": str, "source": "chNN:line"}}}}`

## File Structure
```
poc/
├── canonkeeper/{__init__,__main__,core,report}.py
├── samples/{canon.json,ch03.md}   # original sample world
├── tests/test_core.py
├── devpost/{scope,prd,spec,checklist}.md
├── .agents/skills/                # Devpost Learn skill pack
└── README.md, LICENSE
```

## External Services and Dependencies
None.

## Important Failure Modes
- **Sentence phrasing not covered by patterns** → fact silently missed (no false alarm). Fuller version: LLM extraction.

## What Was Simplified and Why
- **Regex patterns** instead of NLP/LLM — free, offline, explainable.

## Decisions and Open Issues
Learner uncertainty: whether rule-based extraction is "AI" enough — clarified: the project was planned and built with an AI coding agent via the skill pack; LLM extraction is the clear next step.
