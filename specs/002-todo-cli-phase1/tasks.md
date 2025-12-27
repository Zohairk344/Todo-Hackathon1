# Tasks: Phase I: Todo In-Memory Console App

**Feature Branch**: `002-todo-cli-phase1`
**Plan**: [specs/002-todo-cli-phase1/plan.md](plan.md)
**Spec**: [specs/002-todo-cli-phase1/spec.md](spec.md)

## Implementation Strategy

- **Phase 1: Setup**: Initialize the project structure and strict typing configuration.
- **Phase 2: Foundation**: Build the core Domain Model (`Task`) and In-Memory Repository, ensuring data integrity logic is separated from UI.
- **Phase 3: User Story 1 (Add)**: Implement the Service layer for creation and the CLI loop for input capture.
- **Phase 4: User Story 2 (View)**: Add listing capabilities to Repository, Service, and CLI formatting.
- **Phase 5: User Story 3 (Complete)**: Add status toggling logic and menu integration.
- **Phase 6: User Story 4 (Delete)**: Implement removal logic with error handling for non-existent IDs.
- **Phase 7: User Story 5 (Update)**: Add editing capabilities with "keep existing value" logic.
- **Phase 8: Polish**: Finalize docs and verify crash-free stability.

## Dependencies

- **US1 (Add)** depends on Foundation (Task Model, Repository).
- **US2 (View)** depends on US1 (need tasks to view).
- **US3, US4, US5** depend on US2 (need to see IDs to act on them).

## Phase 1: Setup

*Goal: Initialize project structure and environment.*

- [x] T001 Create project directories (models, repositories, services, ui, tests) in src/
- [x] T002 Create __init__.py files in all subdirectories of src/
- [x] T003 Initialize pyproject.toml with Python 3.13+ requirement

## Phase 2: Foundation (Blocking)

*Goal: Core data structures and persistence logic.*

- [x] T004 Implement Task dataclass with type hints in src/models/task.py
- [x] T005 Implement InMemoryTaskRepository class with internal storage in src/repositories/task_repository.py
- [x] T006 Implement repository add() method with ID auto-increment in src/repositories/task_repository.py
- [x] T007 Implement repository get_all() method in src/repositories/task_repository.py
- [x] T008 Implement repository get_by_id() method in src/repositories/task_repository.py
- [x] T009 Create unit tests for repository add and retrieval in tests/test_repository.py

## Phase 3: User Story 1 (Add Task)

*Goal: Users can add new tasks via CLI.*
*Independent Test: Run app, Select [A]dd, Enter Title, Verify "Task added" message.*

- [x] T010 [US1] Create TaskService class with create_task method in src/services/task_service.py
- [x] T011 [US1] Implement validation for empty titles in TaskService.create_task in src/services/task_service.py
- [x] T012 [US1] Create CLI class with display_menu method showing [A]dd option in src/ui/cli.py
- [x] T013 [US1] Implement handle_input method in CLI to process 'A' command in src/ui/cli.py
- [x] T014 [US1] Implement prompt_add_task method in CLI with retry loop for empty titles in src/ui/cli.py
- [x] T015 [US1] Wire up main.py to instantiate Repo, Service, and CLI, then start loop in src/main.py

## Phase 4: User Story 2 (View Tasks)

*Goal: Users can see a list of tasks.*
*Independent Test: Add task, Select [V]iew, Verify task appears in table.*

- [x] T016 [US2] Implement list_tasks method in TaskService in src/services/task_service.py
- [x] T017 [US2] Update CLI menu to include [V]iew option in src/ui/cli.py
- [x] T018 [US2] Implement display_tasks method in CLI with table formatting in src/ui/cli.py
- [x] T019 [US2] Add empty state message "No tasks found" to display_tasks in src/ui/cli.py

## Phase 5: User Story 3 (Mark Complete)

*Goal: Users can toggle task status.*
*Independent Test: Add task, Select [C]omplete, Enter ID, View list, Verify status is "Completed".*

- [x] T020 [US3] Implement repository update() method for status changes in src/repositories/task_repository.py
- [x] T021 [US3] Implement complete_task method in TaskService with ID validation in src/services/task_service.py
- [x] T022 [US3] Update CLI menu to include [C]omplete option in src/ui/cli.py
- [x] T023 [US3] Implement prompt_complete_task in CLI with error handling for non-integer IDs in src/ui/cli.py

## Phase 6: User Story 4 (Delete Task)

*Goal: Users can remove tasks.*
*Independent Test: Add task, Select [D]elete, Enter ID, View list, Verify task is gone.*

- [x] T024 [US4] Implement repository delete() method in src/repositories/task_repository.py
- [x] T025 [US4] Implement delete_task method in TaskService with error return if not found in src/services/task_service.py
- [x] T026 [US4] Update CLI menu to include [D]elete option in src/ui/cli.py
- [x] T027 [US4] Implement prompt_delete_task in CLI showing error if ID not found in src/ui/cli.py

## Phase 7: User Story 5 (Update Task)

*Goal: Users can edit task details.*
*Independent Test: Add task, Select [U]pdate, Enter new Title, View list, Verify change.*

- [x] T028 [US5] Implement update_task method in TaskService handling partial updates in src/services/task_service.py
- [x] T029 [US5] Update CLI menu to include [U]pdate option in src/ui/cli.py
- [x] T030 [US5] Implement prompt_update_task in CLI allowing blank inputs to preserve values in src/ui/cli.py

## Phase 8: Polish & Documentation

*Goal: Final code quality checks and documentation.*

- [x] T031 Update CLI loop to auto-return to menu after actions in src/ui/cli.py
- [x] T032 Verify [E]xit command cleanly terminates the app in src/ui/cli.py
- [x] T033 Run manual "crash test" sequence (invalid IDs, empty inputs) to ensure SC-001 in src/ui/cli.py
- [x] T034 Create final README.md with setup and usage instructions in README.md