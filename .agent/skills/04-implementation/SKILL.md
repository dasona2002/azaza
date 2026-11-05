---
name: 04-implementation
description: Incremental implementation for time-boxed, evidence-driven AI coding hackathons.
---

# Incremental implementation

## Trigger
Use during the corresponding hackathon stage or when the user explicitly asks for it.

## Procedure
Implement smallest working vertical slice, then extend by priority. Run checks after each increment. Record actual commands and failures.

## Deliverable
Update `.hackathon-harness/workspace/IMPLEMENTATION_LOG.md`. Use the corresponding template if needed; record facts separately from assumptions.

## Stop condition
Stop when the stage output is decision-ready, or time budget expires. Escalate critical ambiguity; do not invent missing facts.

## 기록 원칙
담당자 질문·답변은 QUESTIONS.md에 간단히 기록합니다. 설계 선택은 DECISIONS.md에 실제 기술적 이유로 기록하며, 담당자 답변이 실제 영향을 준 경우에만 연결합니다.
