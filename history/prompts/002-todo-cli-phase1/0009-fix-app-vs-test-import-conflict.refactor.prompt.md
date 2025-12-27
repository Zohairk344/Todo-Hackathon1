---
id: 0009
title: Fix app vs test import conflict
stage: refactor
date: 2025-12-27
surface: agent
model: gemini-2.0-flash-exp
feature: 002-todo-cli-phase1
branch: 002-todo-cli-phase1
user: zohai
command: none
labels: [fix, imports, path, testing]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - src/main.py
tests:
 - echo "E" | uv run src/main.py (Pass)
 - unittest discover tests (Pass)
---

## Prompt

hey the tests need src in import to work but the apps not running when i use src in import

## Response snapshot

Fixed the conflict where tests required `src.` imports but running the app directly failed. Added a `sys.path` adjustment to `src/main.py` to include the project root, allowing `src.` absolute imports to resolve correctly in both environments.

## Outcome

- ✅ Impact: Resolved environment-specific import issues.
- 🧪 Tests: App execution and unit tests both passing.
- 📁 Files: Updated src/main.py.
- 🔁 Next prompts: Continue with Phase II or other tasks.
- 🧠 Reflection: Python's relative import and path handling can be tricky when entry points are inside the package. Adding the project root to `sys.path` in the main entry point is a robust way to ensure absolute imports work regardless of how the script is invoked.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): default
- Next experiment (smallest change to try): none
