---
name: 06-optimization
description: Measured optimization for time-boxed, evidence-driven AI coding hackathons.
---

# Measured optimization

## Trigger
Use during the corresponding hackathon stage or when the user explicitly asks for it.

## Procedure
Before optimizing, consult QUESTIONS.md for relevant evaluation intent or constraints. Benchmark and regression results—not the Q&A alone—justify optimization.

Measure baseline first, isolate bottleneck, optimize one thing at a time, rerun identical test workloads and regression checks; revert harmful changes.

## Deliverable
Update `.hackathon-harness/workspace/BENCHMARK.md`. Use the corresponding template if needed; record facts separately from assumptions.

## Stop condition
Stop when the stage output is decision-ready, or time budget expires. Escalate critical ambiguity; do not invent missing facts.

## 기록 원칙
담당자 질문·답변은 QUESTIONS.md에 간단히 기록합니다. 설계 선택은 DECISIONS.md에 실제 기술적 이유로 기록하며, 담당자 답변이 실제 영향을 준 경우에만 연결합니다.
