import html
def render(chapter_name: str, text: str, findings) -> str:
    bad = {f.line: f for f in findings}
    rows = []
    for n, line in enumerate(text.splitlines(), 1):
        f = bad.get(n)
        cls = ' class="bad"' if f else ""
        note = (f'<div class="note">⚠ {html.escape(f.entity)} · {f.attribute}: canon says '
                f'<b>{html.escape(f.canon_value)}</b> ({html.escape(f.canon_source)}), this line says '
                f'<b>{html.escape(f.found_value)}</b></div>') if f else ""
        rows.append(f'<div{cls}><span class="ln">{n}</span>{html.escape(line) or "&nbsp;"}{note}</div>')
    verdict = f"{len(findings)} continuity issue(s)" if findings else "Canon intact ✓"
    return f"""<!doctype html><meta charset="utf-8"><title>Canon Keeper · {html.escape(chapter_name)}</title>
<style>body{{font:16px/1.6 Georgia,serif;background:#111418;color:#e8e2d4;max-width:820px;margin:40px auto;padding:0 20px}}
h1{{font:600 22px system-ui;color:#d9b45a}} .v{{font:600 18px system-ui;margin:8px 0 24px;color:{'#ff7a6b' if findings else '#7bd88f'}}}
.ln{{display:inline-block;width:2.5em;color:#666;font:12px monospace}} .bad{{background:#3a1d1d;border-left:3px solid #ff7a6b}}
.note{{font:13px system-ui;color:#ffb3a8;margin:2px 0 6px 2.9em}}</style>
<h1>Canon Keeper — {html.escape(chapter_name)}</h1><div class="v">{verdict}</div>{''.join(rows)}"""
