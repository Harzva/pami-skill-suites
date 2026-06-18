#!/usr/bin/env python3
from pathlib import Path
import json, re, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
PT = ROOT / 'paper_templates'
manifest = PT / 'corpus_manifest.json'
if not manifest.exists():
    print('missing corpus_manifest.json', file=sys.stderr); sys.exit(1)
data = json.loads(manifest.read_text(encoding='utf-8'))
outdir = PT / 'extracted_structure_maps'; outdir.mkdir(parents=True, exist_ok=True)
def run(cmd, timeout=40):
    try:
        return subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    except Exception as e:
        class R: pass
        r=R(); r.returncode=999; r.stdout=''; r.stderr=str(e); return r
def first_text(pdf):
    r = run(['pdftotext','-f','1','-l','5',str(pdf),'-'])
    return r.stdout if r.returncode==0 else ''
def headings(text):
    rows=[]
    for line in text.splitlines():
        line=re.sub(r'\s+',' ',line.strip())
        if not line or len(line)>110: continue
        if re.match(r'^(abstract|keywords|index terms|i\.?\s+introduction|\d+\.?\s+[A-Z][A-Za-z].*|[IVX]+\.\s+[A-Z].*)$', line, re.I):
            if line not in rows: rows.append(line)
        if len(rows)>=24: break
    return rows or ['Abstract','Introduction','Related work / Background','Method','Experiments / Results','Conclusion','References']
for e in data.get('entries',[]):
    pdf=PT/e.get('local_pdf_path','')
    txt=first_text(pdf) if pdf.exists() else ''
    hs=headings(txt)
    counts={'figure_markers':len(re.findall(r'\bFig(?:ure)?\.?\s*\d+',txt,re.I)), 'table_markers':len(re.findall(r'\bTable\s*\d+',txt,re.I))}
    content = '# Extracted Structure Map: '+e['id']+'\n\n'
    content += '## Source metadata\n\n'
    content += f"- Title: {e.get('title')}\n- Journal: {e.get('journal')}\n- Year: {e.get('year')}\n- DOI: {e.get('doi')}\n- Local PDF: `{e.get('local_pdf_path')}`\n- Source URL: {e.get('source_url')}\n- License: {e.get('license')}\n\n"
    content += '## Detected section-heading candidates\n\n' + '\n'.join(f'{i+1}. {h}' for i,h in enumerate(hs)) + '\n\n'
    content += '## Visual-evidence marker counts\n\n```json\n' + json.dumps(counts, indent=2) + '\n```\n\n'
    content += '## Mining warnings\n\n- Do not copy text, figures, tables, captions, equations, or paper-specific claims.\n- Use this map as structure guidance only.\n'
    (outdir/f"{e['id']}.md").write_text(content, encoding='utf-8')
print(json.dumps({'generated_maps': len(data.get('entries',[])), 'output': str(outdir.relative_to(ROOT))}, indent=2))
