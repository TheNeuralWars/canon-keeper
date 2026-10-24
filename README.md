# Canon Keeper

Catch continuity errors in serialized fiction **before** your readers do.

Canon Keeper keeps a sourced fact sheet of your story (`canon.json`) and checks every new chapter against it, giving each contradiction with its receipt:

```
$ python3 -m canonkeeper check samples/canon.json samples/ch03.md --html report.html
Canon Keeper · ch03.md: 2 issue(s)
  L4   Mira.eyes: canon='grey' (ch01:3) found='green'
  L7   Orrin.status: canon='dead' (ch02:9) found='alive'
```

## Quick start (Python 3.10+, no dependencies, no API keys)
```bash
git clone <this repo> && cd canon-keeper
python3 -m canonkeeper check samples/canon.json samples/ch03.md --html report.html   # then open report.html
python3 -m canonkeeper learn samples/canon.json samples/ch03.md                      # add new facts to canon
python3 -m canonkeeper check samples/canon.json samples/ch03.md --json               # machine output
python3 -m unittest -v tests.test_core
```
Exit code is 1 when issues are found, so it can gate a chapter in CI.

## What it detects (POC)
Eye/hair colour, age, home town, family/mentor relations, and dead characters who act again.

## How it was built
Started from an empty folder with the Devpost Learn Skill Pack (`npx skills add challengepost/learn-ai-basics --all -y`) and a coding agent. Planning docs: `devpost/scope.md`, `devpost/prd.md`, `devpost/spec.md`, `devpost/checklist.md`. No pre-existing code; the sample world ("The Lantern Coast") was written fresh for this demo.

## License
MIT
