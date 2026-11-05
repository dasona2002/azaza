---
name: 03-architecture
description: Architecture and algorithm decision for time-boxed, evidence-driven AI coding hackathons.
---

# Architecture and algorithm decision

## Trigger
Use during the corresponding hackathon stage or when the user explicitly asks for it.

## Procedure
Consult QUESTIONS.md for relevant context and constraints, but choose algorithms using technical trade-offs and human approval. Cite Q-ID only for material influence.

First confirm that organizer clarification gate is complete for P0 items and P1 assumptions are explicitly approved. Compare simple baseline and alternative(s), complexity, implementation time, risk, and observability. Flag unnecessary features. Stop for human approval.

## Deliverable
Update `.hackathon-harness/workspace/DESIGN.md` and `.hackathon-harness/workspace/DECISIONS.md`. Use the corresponding template if needed; record facts separately from assumptions.

## Stop condition
Stop when the stage output is decision-ready, or time budget expires. Escalate critical ambiguity; do not invent missing facts.

## 기록 원칙
담당자 질문·답변은 QUESTIONS.md에 간단히 기록합니다. 설계 선택은 DECISIONS.md에 실제 기술적 이유로 기록하며, 담당자 답변이 실제 영향을 준 경우에만 연결합니다.
