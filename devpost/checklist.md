---
doc: checklist
status: approved
---
# Build Checklist
Build mode: fast

## Slices
- [x] **1. Check a chapter and see the issues**
  Becomes usable: CLI flags eye-colour and dead-character errors.
  Why now: It is the kernel.
  PRD ref: `prd.md > Check`
  Spec ref: `spec.md > Components`
  Build: core.extract/check + CLI.
  Verify (mechanical): `python3 -m unittest -v tests.test_core`
  Learner check: run the sample and read the 2 issues.
  Commit: `Add canon check CLI`
- [x] **2. HTML report and learn**
  Becomes usable: Highlighted report; canon grows each chapter.
  Why now: Completes the loop.
  PRD ref: `prd.md > Learn`, `prd.md > Screens and Layout`
  Spec ref: `spec.md > Data Model`
  Build: report.py, core.learn.
  Verify (mechanical): tests pass; report.html opens.
  Learner check: open the report.
  Commit: `Add report and learn`

## Hands-on Checkpoints
- [ ] Final kick-the-tires exploration and feedback completed (Nico)

## Final Review
- [ ] Final review complete — feedback resolved and learner confirms ready to ship

## Code Tour and App Map
- [ ] Learning activity complete
- [ ] Optional edit and transfer reflection addressed
- [ ] `devpost/app-map.html` generated

## Revisions
