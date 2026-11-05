#!/usr/bin/env python3
"""Generate reproducible SHA256 manifest; does not claim functional correctness."""
from pathlib import Path
import hashlib, json, datetime
root=Path(__file__).resolve().parents[1]
base=root/'workspace'; out=base/'evidence';out.mkdir(parents=True,exist_ok=True)
entries=[]
for p in sorted(base.rglob('*')):
 if not p.is_file() or p.name == 'manifest.json' or '.git' in p.parts: continue
 entries.append({'path':str(p.relative_to(root)),'size':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest={'generated_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'note':'File inventory only; not proof of passing tests','files':entries}
path=out/'manifest.json';path.write_text(json.dumps(manifest,indent=2,ensure_ascii=False),encoding='utf-8')
print(f'Indexed {len(entries)} files: {path}')
