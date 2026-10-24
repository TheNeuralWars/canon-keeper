import argparse, json, os, sys
from . import core, report

def main(argv=None):
    p = argparse.ArgumentParser(prog="canonkeeper", description="Check a new chapter against your story canon.")
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check"); c.add_argument("canon"); c.add_argument("chapter"); c.add_argument("--html"); c.add_argument("--json", action="store_true")
    l = sub.add_parser("learn"); l.add_argument("canon"); l.add_argument("chapter")
    a = p.parse_args(argv)
    canon = core.load_canon(a.canon)
    text = open(a.chapter, encoding="utf-8").read()
    name = os.path.basename(a.chapter)
    if a.cmd == "learn":
        n = core.learn(canon, text, name)
        json.dump(canon, open(a.canon, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        print(f"learned {n} new fact(s) from {name} -> {a.canon}"); return 0
    findings = core.check(canon, text)
    if a.json:
        print(json.dumps(core.to_dicts(findings), indent=2))
    else:
        print(f"Canon Keeper · {name}: {len(findings)} issue(s)")
        for f in findings:
            print(f"  L{f.line:<3} {f.entity}.{f.attribute}: canon={f.canon_value!r} ({f.canon_source}) found={f.found_value!r}\n        \"{f.excerpt}\"")
    if a.html:
        open(a.html, "w", encoding="utf-8").write(report.render(name, text, findings)); print(f"report -> {a.html}")
    return 1 if findings else 0

if __name__ == "__main__":
    sys.exit(main())
