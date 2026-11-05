#!/usr/bin/env python3
"""Run a user-specified verification command and capture truthful evidence."""
import argparse, datetime, json, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
p = argparse.ArgumentParser()
p.add_argument('--project', required=True, help='Existing project directory')
p.add_argument('--command', nargs=argparse.REMAINDER, required=True, help='Command and arguments (no shell)')
p.add_argument('--timeout', type=int, default=180)
a = p.parse_args()
project = Path(a.project).resolve()
if not project.is_dir(): p.error(f'Project directory not found: {project}')
cmd = a.command
if cmd and cmd[0] == '--': cmd = cmd[1:]
if not cmd: p.error('Supply a command after --command, e.g. --command -- python3 -m unittest discover')
evidence = ROOT/'workspace'/'evidence'; evidence.mkdir(parents=True, exist_ok=True)
stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
record = {'utc':stamp,'cwd':str(project),'command':cmd,'timeout_seconds':a.timeout}
try:
 r = subprocess.run(cmd,cwd=project,capture_output=True,text=True,timeout=a.timeout,check=False)
 record.update(exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr,status='PASS' if r.returncode == 0 else 'FAIL')
except subprocess.TimeoutExpired as e:
 record.update(exit_code=None,stdout=str(e.stdout or ''),stderr=str(e.stderr or ''),status='TIMEOUT')
except OSError as e:
 record.update(exit_code=None,stdout='',stderr=str(e),status='ERROR')
out=evidence/f'verify-{stamp}.json';out.write_text(json.dumps(record,indent=2,ensure_ascii=False),encoding='utf-8')
print(f"{record['status']} | evidence: {out}")
if record.get('stdout'): print(record['stdout'][-3000:])
if record.get('stderr'): print(record['stderr'][-1500:],file=sys.stderr)
sys.exit(0 if record['status']=='PASS' else 1)
