---
name: 05-verification
description: Evidence-backed verification for time-boxed, evidence-driven AI coding hackathons.
---

# Evidence-backed verification

## Trigger
Use during the corresponding hackathon stage or when the user explicitly asks for it.

## Procedure
Run acceptance tests and integration flows; inspect runtime state where applicable. Separate pass, fail and unverified. Preserve commands, logs and artifacts.

## Deliverable
Update `.hackathon-harness/workspace/TEST_PLAN.md` and `.hackathon-harness/workspace/evidence/`. Use the corresponding template if needed; record facts separately from assumptions.

## Stop condition
Stop when the stage output is decision-ready, or time budget expires. Escalate critical ambiguity; do not invent missing facts.

## 기록 원칙
담당자 질문·답변은 QUESTIONS.md에 간단히 기록합니다. 설계 선택은 DECISIONS.md에 실제 기술적 이유로 기록하며, 담당자 답변이 실제 영향을 준 경우에만 연결합니다.
