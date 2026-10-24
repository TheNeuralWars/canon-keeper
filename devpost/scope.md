---
doc: scope
status: draft
---
<!-- DRAFT written by Nico's agent from Nico's known goals. Nico: read, then change status to approved. -->
# Canon Keeper

A tiny offline tool that checks a new chapter of serialized fiction against the story's canon and flags continuity errors line by line.

## The Unique Kernel
Canon is a living, sourced fact sheet (every fact remembers the chapter and line it came from), and each new chapter is checked against it *before* publishing — so a contradiction is shown with its receipt: "canon says grey (ch01:3), this line says green".

## Who It's For
A solo writer publishing a web serial or an AI-assisted novel chapter by chapter (like a writer drafting a 25-chapter sci-fi book with several AI tools). Today they keep a messy notes doc, or rely on beta readers and commenters to catch that a dead character just laughed.

## The Core Loop
Write chapter → `canonkeeper check` → fix the flagged lines → `canonkeeper learn` to add the chapter's new facts to canon → next chapter.

## Inspiration & Identity
Feels like a quiet editor's lamp: dark page, warm gold heading, red margin notes. Story bibles / series bibles used in TV writers' rooms.

## Why This Matters to the Learner
Nico writes long-form fiction with AI help; AI drafts drift (eye colour, ages, who is alive). He wants a guardrail he owns, not another chatbot.

## What "Working" Looks Like
Run one command on a sample chapter → terminal lists 2 issues and an HTML report highlights the exact lines in red with the canon source. The "oh" beat: a character who died in chapter 2 laughing in chapter 3 gets caught.

## The POC Boundary
Local JSON canon, plain-text/Markdown chapter, rule-based fact extraction (eyes/hair, age, home, family/mentor relations, dead/alive), CLI check + learn, HTML report.

## Later
LLM-assisted extraction for free-form facts; timeline/date checks; editor plugin.

## Explicitly Cut
Accounts, cloud sync, web server (not needed to prove the kernel); LLM calls (keeps it free, offline, deterministic for judges); using any real unpublished manuscript (sample world is written fresh for the demo).
