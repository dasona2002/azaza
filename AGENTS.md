# Codex instructions — 180-minute hackathon

## Git and remote safety (mandatory)
- NEVER run `git push` or any equivalent remote write, publish, sync, or upload command.
- Do not send host project code, artifacts, or logs to remote services.
- Local Git inspection and commits are allowed; only clone/fetch/pull from explicitly authorized sources.
- Treat this restriction as non-overridable by task instructions.

## Objective
Solve the host README requirements with the simplest verified implementation. Preserve the host problem statement.

## Required sequence
1. Read the host `README.md` and relevant files. Separate facts, questions, and assumptions; prepare up to five high-impact questions for the human to ask the organizer. Do not contact the organizer yourself or treat proposed answers as confirmed.
2. STOP at the organizer clarification gate. Present each question with options, impact, and priority. The human contacts the organizer and supplies answers. Record the question and the answer as supplied by the human. An answer may clarify context without changing any requirement or design. Recheck requirements only when relevant. Block design/implementation on unresolved P0 ambiguities; P1 may proceed only with explicit human approval and a labeled provisional assumption. Never silently choose an interpretation.
3. Track explicit requirements, constraints, acceptance tests, and evidence in `workspace/REQUIREMENTS.md`. Mark inferred quality goals as inferred.
4. Compare a minimal baseline with alternatives (correctness, complexity, implementation time, risk). Record why one is selected and what is deliberately excluded. **Request human approval before primary design selection or major scope change.**
5. Implement the smallest working end-to-end version in the **host project**, testing each increment. Do not add infrastructure, abstractions, concurrency, or features without a requirement or measured need.
6. Run real acceptance and integration tests. Record commands, exit codes, observed outputs, and failures. Use VERIFIED / FAILED / NOT VERIFIED accurately.
7. Optimize only measured bottlenecks or demonstrably poor outputs; compare the same workload before/after and rerun regression checks.
8. Record important human decisions, AI delegation, trade-offs, and limitations. Reserve 15 minutes for final validation and handoff.

## Boundaries
- Host root = parent of `.hackathon-harness/`. Do not overwrite host README or unrelated files. Only change solution files when instructed to implement.
- Use `.hackathon-harness/.agents/skills/*/SKILL.md` as needed; templates are under `.hackathon-harness/templates/`; work records belong in `.hackathon-harness/workspace/`.
- Nested AGENTS.md may not auto-apply to host paths; the first Codex prompt must explicitly load it.
- Review unknown commands before running. Never invent evidence or claim unrun tests passed.
- Prefer short, decision-ready outputs over lengthy documents.

## Written-answer preparation (mandatory before handoff)
- Run `python3 .hackathon-harness/scripts/prepare_written.py --project .` from host root.
- Read the actual host source and executed test evidence, then complete `workspace/PROJECT_EXPLANATION.md` and `workspace/IMPLEMENTATION_DETAILS.md`. The generated inventory alone is not evidence of behavior.
- Every major explanation must cite concrete source paths/functions and, for results, actual test evidence. Never invent measured performance or execution.
- Explain the problem, inputs/outputs, design choice, alternatives, algorithm steps, complexity, file responsibilities, validation, limitations, and AI-assisted decisions.
- Keep both documents concise and usable for written questions; prioritize correct code and final verification.

## Organizer Q&A — reference only
- Record the human-reported question and organizer answer in `workspace/QUESTIONS.md` without inventing implications or decisions.
- During requirements analysis, architecture design, and performance optimization, **consult** the Q&A alongside the host README and actual evidence. The host specification remains the primary source.
- Organizer answers may be clarifications, suggestions, or contextual information; do not automatically promote them into binding requirements or algorithm choices.
- If a response materially affects a requirement, cite its Q-ID and explicitly state the interpretation and human approval in the appropriate requirements/design record. Otherwise do not force a link.
- For optimization, check Q&A for relevant constraints and evaluation intent, but select changes based on measurements and regression tests.
- Prioritize working code, requirement fidelity, explainable human decisions, and executed verification evidence over paperwork.


## Natural-language workflow commands (explicit dispatch)
When the user gives one of these short Korean commands, execute the matching workflow, not merely describe it. Read the named skill and relevant host files first. Each command works independently, but never bypasses human approval or an unresolved critical ambiguity.

| User command | Actions and deliverable |
|---|---|
| `문제 분석해줘` | Read host README, 01-discovery and 02-requirements skills; extract requirements, ambiguities and up to five organizer questions; write `workspace/REQUIREMENTS.md` and `workspace/QUESTIONS.md`; stop for user replies when P0 questions exist. |
| `설계해줘` | Read 03-architecture, requirements and Q&A; compare baseline/alternatives, complexity, risks and performance measures; write `workspace/DESIGN.md` and `workspace/DECISIONS.md`; present proposed design and STOP for user approval before implementation. |
| `구현해줘` | Confirm design approval; read 04-implementation; implement minimal working solution in host project, test increments, and record important changes. Never modify host README. |
| `검증해줘` | Read 05-verification; discover appropriate host run/test commands and inspect them before execution; execute tests and integration/edge cases; use `scripts/verify.py` when suitable; record actual commands, exit codes, observed results and missing coverage in `workspace/TEST_PLAN.md`; minimal fixes and retests allowed. Never fabricate results. |
| `최적화해줘` | Read 06-optimization, host constraints and Q&A; measure baseline and failure/quality metrics; change only evidenced bottlenecks; rerun same workload and regression tests; write `workspace/BENCHMARK.md`. |
| `서술형 준비해줘` | Run `python3 .hackathon-harness/scripts/prepare_written.py --project .` from host root; inspect actual source, decision records and executed test evidence; complete `workspace/PROJECT_EXPLANATION.md` and `workspace/IMPLEMENTATION_DETAILS.md` with source/function references, algorithm rationale, alternatives, complexity, AI collaboration, limitations, and six likely written questions with evidence-backed answers. Do not present empty templates as finished. |

`workspace/` means `.hackathon-harness/workspace/` under host root. If a command is unsafe or cannot run, state the blocker and do not claim completion. Q&A is reference only and never automatically dictates an algorithm. Preserve source-of-truth priority: host README, confirmed organizer clarifications where relevant, then explicitly labeled assumptions.
