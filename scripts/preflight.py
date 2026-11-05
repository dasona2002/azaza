#!/usr/bin/env python3
"""Standard-library-only repository readiness check."""
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
required = ['AGENTS.md', 'README.md', 'scripts/prepare_written.py']
required += [f'.agents/skills/{i:02d}-{name}/SKILL.md' for i, name in enumerate(['discovery','requirements','architecture','implementation','verification','optimization'], 1)]
required += [f'templates/{n}.md' for n in ['QUESTIONS','REQUIREMENTS','DESIGN','DECISIONS','TEST_PLAN','BENCHMARK','EVALUATION','IMPLEMENTATION_LOG']]
missing = [f for f in required if not (ROOT/f).is_file()]
print(f'Root: {ROOT}')
for f in missing: print(f'MISSING: {f}')
print(f'Preflight: {len(required)-len(missing)}/{len(required)} files present')
sys.exit(1 if missing else 0)
