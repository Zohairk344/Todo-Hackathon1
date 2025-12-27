<!--
SYNC IMPACT REPORT
Version change: 1.0.0 → 1.0.0 (Re-verification)
Modified principles: None
Added sections: None
Removed sections: None
Templates requiring updates: None
-->
# The Evolution of Todo - Phase I Constitution

## Core Principles

### I. The Golden Rule: Spec-Driven Development (SDD)
*   **Zero Manual Code:** No code shall be written by the AI unless it is explicitly defined in `speckit.tasks` and mapped to `speckit.plan`.
*   **Traceability:** Every implemented function or module must reference its originating Task ID (e.g., `# Implements: T-003`).
*   **Golden Rule:** "No Task = No Code." If a requirement is missing from the spec, the Agent must request a spec update rather than improvising.
*   **Core Philosophy:** The engineer is the System Architect; the AI is the Executor. We move from "vibe-coding" to professional Spec-Driven Engineering.

### II. Technical Stack & Environment
*   **Language:** Python 3.13+ (Strict typing required).
*   **Package Manager:** `uv` (Universal Package Manager).
*   **Environment:** Linux (Ubuntu 22.04) or WSL 2 for Windows.
*   **Persistence:** In-Memory only (Python Lists or Dictionaries). No SQL or File I/O for data storage in this phase.
*   **Framework:** Standard Library only (no external web frameworks like FastAPI yet).

### III. Architecture & Design Patterns
*   **Separation of Concerns:**
    *   **UI Layer:** Handles CLI input/output, menu rendering, and user prompts.
    *   **Service Layer:** Contains business logic (validation, ID generation).
    *   **Data Layer (Repository):** Manages in-memory storage structures.
*   **Modularity:** The application must be structured to allow replacing the "In-Memory" repository with a "Database" repository in Phase II without rewriting the UI or Service layers.
*   **Error Handling:** The app must gracefully handle invalid inputs (e.g., non-integer IDs) without crashing.

### IV. Feature Requirements (Basic Level)
The system must support the following atomic operations:
1.  **Add Task:** Create new items with Title (Req) and Description (Opt).
2.  **Delete Task:** Remove items by unique ID.
3.  **Update Task:** Modify details of existing items.
4.  **View Task List:** Display all items with status indicators.
5.  **Mark as Complete:** Toggle status between Pending and Completed.

### V. Coding Standards & Quality
*   **Style:** Follow PEP 8 guidelines.
*   **Type Hinting:** Mandatory for all function signatures (e.g., `def add_task(title: str) -> Task:`).
*   **Documentation:** All modules and public functions must have docstrings.
*   **Testing:** Basic unit tests using `unittest` or `pytest` for the Repository logic.

### VI. Deliverables
The final output must include:
*   `/src` folder containing the source code.
*   `CLAUDE.md` with context instructions.
*   `README.md` with setup instructions using `uv`.
*   `specs/` history folder containing all versions of the specifications.

## Project Identity & Scope

*   **Project Name:** The Evolution of Todo
*   **Current Phase:** Phase I (In-Memory Python Console App)
*   **Objective:** Build a robust command-line interface (CLI) task manager that stores data in memory without external database persistence.

## Governance

*   **Supremacy:** This Constitution supersedes all other technical practices or verbal instructions unless explicitly amended.
*   **Amendments:** Changes to this document require a version bump and explicit documentation in the header.
*   **Compliance:** All Pull Requests and Code Reviews must verify compliance with these principles.
*   **Guidance:** Use `GEMINI.md` (or agent equivalent) for runtime development guidance.

**Version**: 1.0.0 | **Ratified**: 2025-12-27 | **Last Amended**: 2025-12-27
