#!/usr/bin/env python3
# Create factual source inventory and answer-preparation documents.
import argparse, hashlib, datetime
from pathlib import Path
p=argparse.ArgumentParser()
p.add_argument('--project',default='.',help='Host project root')
a=p.parse_args()
root=Path(a.project).resolve(); harness=Path(__file__).resolve().parents[1]
if not root.is_dir(): p.error('Host project does not exist')
out=harness/'workspace';out.mkdir(exist_ok=True)
ignore={'.git','.hackathon-harness','node_modules','.venv','venv','__pycache__','dist','build','.next','coverage','.pytest_cache'}
exts={'.py','.js','.jsx','.ts','.tsx','.java','.kt','.go','.rs','.cpp','.cc','.c','.h','.hpp','.cs','.html','.css','.sql','.sh'}
files=[]
for f in sorted(root.rglob('*')):
 if not f.is_file() or any(part in ignore for part in f.relative_to(root).parts):continue
 if f.suffix.lower() not in exts:continue
 if len(files)>=300:break
 try:
  if f.stat().st_size>1_000_000:continue
  digest=hashlib.sha256(f.read_bytes()).hexdigest()[:12]
  files.append((f.relative_to(root).as_posix(),digest))
 except OSError:continue
stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
inv=out/'SOURCE_INVENTORY.md'
inv.write_text('# Source inventory (generated; not proof of correctness)\n\nGenerated UTC: '+stamp+'\n\n| File | SHA256 prefix |\n|---|---|\n'+''.join(f'| `{f}` | `{h}` |\n' for f,h in files)+'\nExcluded: dependencies, build artifacts, files over 1 MB; max 300 files.\n',encoding='utf-8')
contents={
'PROJECT_EXPLANATION.md':'''# 프로젝트 설명 — 서술형 대비
> Codex가 실제 코드와 테스트를 읽고 작성. 추측 금지. 미확인 내용은 NOT VERIFIED로 표시.

## 1. 문제 및 목표
- 문제 배경과 사용자:
- 입력 / 출력:
- 핵심 제약:
- 성공 기준:

## 2. 구현 범위와 사용자 흐름
- 구현한 기능 (요구사항 ID 연결):
- 대표 입력 → 처리 → 출력:
- 구현하지 않은 항목과 이유:

## 3. 설계와 알고리즘
- 전체 구조 (핵심 모듈 연결):
- 선택 알고리즘과 단계별 동작:
- 다른 대안과 선택 이유:
- 시간 / 공간 복잡도 및 전제:
- AI 제안 중 채택/거절한 내용과 이유:

## 3-1. 담당자 답변 → 설계 → 구현 추적
- 주요 Q-ID / R-ID / D-ID 연결과 인과 근거 (`workspace/DECISION_TRACE.md` 참조):
- 담당자가 확정한 규칙과 팀이 선택한 알고리즘 구분:
- 실제 구현 파일/함수와 테스트 근거:

## 4. 검증과 결과
- 실행 방법:
- 실제 실행한 테스트 명령과 결과 (증거 경로):
- 정상 / 경계 / 실패 사례:
- 성능 지표 및 개선 전후 (측정했을 때만):

## 5. 한계와 개선
- 알려진 문제:
- 개선 우선순위와 근거:

## 6. 예상 서술형 답변 (코드 근거 필수)
1. 왜 이 설계를 선택했는가?
2. 핵심 알고리즘은 어떻게 동작하는가?
3. 다른 접근법의 장단점은?
4. 가장 어려웠던 문제와 해결 과정은?
5. 무엇을 어떻게 검증했는가?
6. 현재 한계와 다음 개선은?
''',
'IMPLEMENTATION_DETAILS.md':'''# 구현 상세 — 코드 근거 문서
> SOURCE_INVENTORY.md는 파일 목록일 뿐임. 실제 파일을 열어 확인한 내용만 작성.

## 1. 파일별 역할
| 경로 | 역할 | 핵심 함수/클래스 | 관련 요구사항 | 확인한 코드 위치 |
|---|---|---|---|---|

## 2. 핵심 실행 흐름
- 진입점:
- 데이터 파싱 및 유효성 검사:
- 주요 처리 단계:
- 출력 / 저장:
- 오류 처리:

## 3. 핵심 구현 설명
### 기능 A
- 관련 파일 / 함수:
- 처리 로직 (순서대로):
- 자료구조 및 선택 이유:
- 입력 경계조건:
- 검증 증거:

## 4. 설계 변경 및 AI 활용
| 결정 | 대안 | 선택 근거 | 영향 | 관련 코드/로그 |
|---|---|---|---|---|

## 5. 서술형에서 주의할 점
- 코드로 확인되지 않은 주장:
- 테스트하지 못한 항목:
- 설명이 어려운 함수 (직접 재검토 필요):
'''}
for name,content in contents.items():
 target=out/name
 if not target.exists():target.write_text(content,encoding='utf-8')
 print(('EXISTS (preserved)' if target.stat().st_size!=len(content.encode()) else 'READY'),target)
print('Inventory:',inv,'files:',len(files))
