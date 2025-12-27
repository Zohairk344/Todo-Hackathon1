# Feature Specification: Phase I: Todo In-Memory Console App

**Feature Branch**: `002-todo-cli-phase1`  
**Created**: 2025-12-27  
**Status**: Draft  
**Input**: User description: "Phase I: Todo In-Memory Console App..."

## Clarifications

### Session 2025-12-27
- Q: How should the system handle blank input during a task update? → A: Keep existing values (Option A).
- Q: How should the system handle empty Title during task creation? → A: Reject and retry loop (Option A).
- Q: How should the system handle navigation after an action (e.g., Task Added)? → A: Auto-return to menu (Option A).
- Q: How should the system handle non-existent IDs during Update/Delete? → A: Error message then menu (Option A).
- Q: What is the primary menu navigation style? → A: Letter commands ([A]dd, [V]iew, etc.) (Option B).

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Add a Task (Priority: P1)

As a user organizing my daily work, I want to quickly capture a new task so that I don't forget it.

**Why this priority**: Core functionality; without adding tasks, the system has no data to manage.

**Independent Test**: Can be tested by adding a task and receiving a confirmation message with the new ID.

**Acceptance Scenarios**:

1. **Given** the app is running, **When** I select "Add Task" (by entering 'A') and enter title "Buy Milk", **Then** the system should confirm "Task 'Buy Milk' added with ID 1".
2. **Given** I am adding a task, **When** I provide a Title but leave Description empty, **Then** the task is created with the Title and an empty Description.
3. **Given** I am adding a task, **When** I leave the Title blank, **Then** the system shows an error and prompts me for the Title again.

---

### User Story 2 - View Task List (Priority: P1)

As a user, I want to see all my current tasks in a list so that I can decide what to work on next.

**Why this priority**: Essential for visibility; users need to see what they have added.

**Independent Test**: Can be tested by adding multiple tasks and verifying they appear in the list output.

**Acceptance Scenarios**:

1. **Given** I have added "Buy Milk" (ID 1), **When** I list tasks (by entering 'V'), **Then** I should see a table entry like "[1] [Pending] Buy Milk".
2. **Given** no tasks have been added, **When** I list tasks, **Then** I should see a friendly message "No tasks found".

---

### User Story 3 - Mark Task as Complete (Priority: P1)

As a user, I want to mark tasks as done so that I can track my progress.

**Why this priority**: fundamental workflow step (ToDo -> Done).

**Independent Test**: Can be tested by changing a task's status and verifying the update in the list.

**Acceptance Scenarios**:

1. **Given** task 1 is "Pending", **When** I mark task 1 as complete (by entering 'C' and ID 1), **Then** the system confirms the update and the task status changes to "Completed" (or True).

---

### User Story 4 - Delete a Task (Priority: P2)

As a user, I want to remove tasks that are mistakes or no longer relevant so that my list remains clean.

**Why this priority**: Important for data hygiene but strictly secondary to creation and completion.

**Independent Test**: Can be tested by removing a known task and verifying it is no longer retrievable or visible.

**Acceptance Scenarios**:

1. **Given** task 1 exists, **When** I delete task 1 (by entering 'D' and ID 1), **Then** the system confirms removal and the task list shows it is gone.
2. **Given** task 99 does not exist, **When** I try to delete task 99, **Then** I receive a "Task ID not found" error message and return to the main menu.

---

### User Story 5 - Update Task Details (Priority: P2)

As a user, I want to correct a task's title or description so that the information is accurate.

**Why this priority**: Useful refinement, but users can often just delete and re-add in a simple system.

**Independent Test**: Can be tested by modifying a task and verifying the new details.

**Acceptance Scenarios**:

1. **Given** task 1 exists with title "Buy Milk", **When** I update task 1 title to "Buy Soy Milk" (by entering 'U' and ID 1), **Then** the system confirms the update and the new title is saved.
2. **Given** task 99 does not exist, **When** I try to update task 99, **Then** I receive a "Task ID not found" error message and return to the main menu.
3. **Given** task 1 exists, **When** I update it and press Enter for the Title (leaving it blank), **Then** the original Title is preserved.

### Edge Cases

- **Invalid Input**: What happens when user enters "abc" where an integer ID is expected? System must catch `ValueError` and prompt again (or show error) without crashing.
- **Empty Title**: What happens if user creates a task with empty/whitespace title? System MUST reject empty titles and prompt the user again until a valid title is provided.
- **Persistence**: What happens when application exits? Data is wiped (Ephemeral).

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow creating a task with a mandatory Title (1-200 chars) and optional Description (max 1000 chars).
  - Empty or whitespace-only titles MUST be rejected with a retry prompt.
- **FR-002**: System MUST assign a unique auto-incrementing integer ID to each new task.
- **FR-003**: System MUST initialize new tasks with a "Pending" status.
- **FR-004**: System MUST display all tasks in a formatted list/table showing ID, Status, and Title.
- **FR-005**: System MUST allow updating the Title and Description of an existing task identified by ID.
  - If a user provides blank input during an update for Title or Description, the system MUST preserve the existing value.
  - If the provided Task ID does not exist, the system MUST display an error message and return to the main menu.
- **FR-006**: System MUST allow deleting a task identified by ID.
  - If the provided Task ID does not exist, the system MUST display an error message and return to the main menu.
- **FR-007**: System MUST allow toggling task status from "Pending" to "Completed" (and vice versa if applicable, though requirement says toggle/mark complete).
- **FR-008**: System MUST provide a continuous command-line loop (Menu -> Action -> Result -> Menu) until "Exit" is selected.
  - After any action (Add, Update, Delete, Toggle), the system MUST automatically redisplay the main menu without requiring an explicit "Press Enter" step.
  - **Menu Navigation**: The system MUST use letter-based commands for menu selection: `[A]`dd, `[V]`iew, `[U]`pdate, `[D]`elete, `[C]`omplete, `[E]`xit. Commands SHOULD be case-insensitive.
- **FR-009**: System MUST handle invalid ID inputs (non-integer) gracefully without crashing.

### Key Entities *(include if feature involves data)*

- **Task**:
    - **ID**: Unique Integer (auto-generated).
    - **Title**: String (1-200 chars).
    - **Description**: String (optional, max 1000 chars).
    - **Status**: Boolean or Enum (Pending/Completed).

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: **Crash-Free Stability**: User can perform any sequence of 20 valid or invalid operations without the application crashing (Python exceptions unhandled).
- **SC-002**: **Input Validation**: 100% of non-integer inputs for ID prompts result in a user-friendly error message instead of a crash.
- **SC-003**: **Data Integrity**: Added tasks persist accurately within the session memory until explicitly deleted or the app exits.
- **SC-004**: **Task Completion**: User can navigate from "Add" to "Mark Complete" in under 30 seconds using the CLI menu.