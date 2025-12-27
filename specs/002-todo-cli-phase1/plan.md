# Implementation Plan - Phase I: Todo In-Memory Console App

## Technical Context

**Feature:** Phase I: Todo In-Memory Console App
**Goal:** Build a robust command-line interface (CLI) task manager that stores data in memory without external database persistence.

**Existing Architecture:**
- Project is in initial phase (greenfield).
- Defined layered architecture: Domain (Models), Repository (Data Access), Service (Business Logic), Presentation (CLI).

**New Components:**
- `src/models/task.py`: Data class for Task entity.
- `src/repositories/task_repository.py`: In-memory storage implementation.
- `src/services/task_service.py`: Business logic and validation.
- `src/ui/cli.py`: User interface loop and formatting.
- `src/main.py`: Application entry point.

**Constraints:**
- Python 3.13+ only.
- `uv` package manager.
- Standard Library only (no external frameworks).
- In-memory persistence (no file I/O or DB).
- Strict Type Hinting.
- PEP 8 compliance.

**Clarifications Needed:**
- None. (Clarifications regarding menu style, update behavior, and error handling were resolved in `/sp.spec`).

## Constitution Check

**Principle I: Spec-Driven Development (SDD)**
- [ ] Plan explicitly maps to `speckit.tasks`? (Will be ensured in next step)
- [ ] Traceability enforced? (Plan will mandate `# Implements: T-XXX` comments)

**Principle II: Technical Stack & Environment**
- [x] Python 3.13+ used?
- [x] `uv` package manager used?
- [x] Standard Library only?
- [x] In-Memory persistence only?

**Principle III: Architecture & Design Patterns**
- [x] Separation of Concerns (UI/Service/Repo) respected?
- [x] Modularity for future DB swap supported?

**Principle V: Coding Standards & Quality**
- [x] Type Hinting mandatory?
- [x] PEP 8 style?
- [x] Testing (unittest/pytest) included?

## Phase 0: Research & Validation

### Research Goals
- **R1:** Confirm `dataclasses` usage for mutable models vs immutable frozen instances (Mutable is better for updates here).
- **R2:** Verify `uv` setup for a pure python project without external runtime dependencies (standard lib only).
- **R3:** Best practices for Python CLI main loops (e.g., clearing screen, handling `KeyboardInterrupt`).

### Research Output (`research.md`)
*(Self-contained in this plan due to standard stack)*

**R1 Decision:** Use mutable `@dataclass` for `Task`.
- **Rationale:** Tasks need to be updated (Title, Description, Status). Mutability simplifies the `update` operation in the repository.

**R2 Decision:** Use `uv init` and `uv run`.
- **Rationale:** Standard `uv` workflow. Even with standard lib only, `uv` manages the python version and venv isolation.

**R3 Decision:**
- Use `while True` loop.
- Use `os.system('cls' if os.name == 'nt' else 'clear')` for screen clearing (optional, but good for UX).
- Wrap loop in `try...except KeyboardInterrupt` for clean exit.

## Phase 1: Design & Contracts

### Data Model (`data-model.md`)

**Entity: Task**
- `id`: int (Unique, Auto-increment, Primary Key)
- `title`: str (Required, 1-200 chars)
- `description`: str | None (Optional, max 1000 chars)
- `status`: str (Enum-like: "Pending" | "Completed", Default: "Pending")

### API Contracts (Internal Interfaces)

**Repository Interface (`TaskRepository`)**
- `add(task: Task) -> Task`
- `get_all() -> List[Task]`
- `get_by_id(id: int) -> Optional[Task]`
- `update(task: Task) -> bool` (or return updated Task)
- `delete(id: int) -> bool`

**Service Interface (`TaskService`)**
- `create_task(title: str, description: str = "") -> Union[Task, Error]`
- `list_tasks() -> List[Task]`
- `complete_task(id: int) -> Union[Task, Error]`
- `delete_task(id: int) -> Union[bool, Error]`
- `update_task(id: int, title: str = None, description: str = None) -> Union[Task, Error]`

### Directory Structure
```text
src/
├── __init__.py
├── main.py
├── models/
│   ├── __init__.py
│   └── task.py
├── repositories/
│   ├── __init__.py
│   └── task_repository.py
├── services/
│   ├── __init__.py
│   └── task_service.py
└── ui/
    ├── __init__.py
    └── cli.py
tests/
├── __init__.py
├── test_repository.py
└── test_service.py
```

## Phase 2: Execution Strategy

### Step 1: Core Domain & Data
- Implement `Task` dataclass.
- Implement `InMemoryTaskRepository` with CRUD and ID generation.
- **Verification:** Unit tests for Repository (Add, Get, Update, Delete).

### Step 2: Service Layer
- Implement `TaskService`.
- Add validation logic (Empty title check, Max length).
- Add business logic (Status toggling).
- **Verification:** Unit tests for Service (mocking Repository if needed, or using real one for simple phase 1).

### Step 3: CLI & Integration
- Implement `CLI` class.
- Build the Menu Loop with Letter Commands (`[A]`, `[V]`, `[U]`, `[D]`, `[C]`, `[E]`).
- Connect CLI -> Service -> Repository.
- **Verification:** Manual walkthrough of User Stories.

### Step 4: Polish & Documentation
- Ensure PEP 8 compliance (`ruff check .` if available, or manual).
- Add Docstrings.
- Create `README.md` and `CLAUDE.md`.
