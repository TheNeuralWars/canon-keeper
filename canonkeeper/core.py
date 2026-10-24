"""Fact extraction + contradiction check. Pure stdlib, deterministic, offline."""
from __future__ import annotations
import json, re
from dataclasses import dataclass, asdict

# Each pattern yields (entity, attribute, value). Kept small and readable on purpose.
PATTERNS = [
    (re.compile(r"\b([A-Z][a-z]+)'s (eyes|hair) (?:were|was|are|is|gleamed|shone) (\w+)"), lambda m: (m[1], m[2], m[3])),
    (re.compile(r"\b([A-Z][a-z]+)(?:,)? (?:who was|was|is|turned) (\d{1,3}) years old"), lambda m: (m[1], "age", m[2])),
    (re.compile(r"\b([A-Z][a-z]+) (?:lived|lives|lived alone) in ([A-Z][a-z]+(?: [A-Z][a-z]+)?)"), lambda m: (m[1], "home", m[2])),
    (re.compile(r"\b([A-Z][a-z]+)'s (sister|brother|mother|father|mentor) ([A-Z][a-z]+)"), lambda m: (m[1], m[2], m[3])),
    (re.compile(r"\b([A-Z][a-z]+) (?:was|is) dead\b"), lambda m: (m[1], "status", "dead")),
    (re.compile(r"\b([A-Z][a-z]+) (?:said|says|shouted|whispered|smiled|walked|ran|laughed)\b"), lambda m: (m[1], "status", "alive")),
]

@dataclass
class Finding:
    line: int
    entity: str
    attribute: str
    canon_value: str
    found_value: str
    canon_source: str
    excerpt: str

def load_canon(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def extract(text: str):
    for n, line in enumerate(text.splitlines(), 1):
        for rx, fn in PATTERNS:
            for m in rx.finditer(line):
                yield n, *fn(m), line.strip()

def check(canon: dict, text: str) -> list[Finding]:
    facts = canon.get("facts", {})
    out = []
    for n, ent, attr, val, excerpt in extract(text):
        fact = facts.get(ent, {}).get(attr)
        if not fact:
            continue
        if str(fact["value"]).lower() != str(val).lower():
            out.append(Finding(n, ent, attr, str(fact["value"]), val, fact.get("source", "canon"), excerpt))
    return out

def learn(canon: dict, text: str, source: str) -> int:
    """Add facts that canon does not know yet (never overwrite). Returns count added."""
    facts = canon.setdefault("facts", {})
    added = 0
    for n, ent, attr, val, _ in extract(text):
        if attr == "status" and val == "alive":
            continue
        slot = facts.setdefault(ent, {})
        if attr not in slot:
            slot[attr] = {"value": val, "source": f"{source}:{n}"}
            added += 1
    return added

def to_dicts(findings): return [asdict(f) for f in findings]
