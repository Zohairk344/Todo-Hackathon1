# Evolution of Todo - Phase I: In-Memory Console App

A robust command-line task manager built with Python 3.13+ using a Spec-Driven Development approach.

## Features

- **Add Task**: Create tasks with titles and optional descriptions.
- **View Tasks**: List all tasks in a formatted table.
- **Update Task**: Edit task titles and descriptions.
- **Delete Task**: Remove tasks by ID.
- **Complete Task**: Toggle task status to "Completed".
- **In-Memory Storage**: Data persists only while the application is running.

## Prerequisites

- **Python**: 3.13 or higher
- **Package Manager**: `uv`

## Installation

1.  **Clone the repository**.
2.  **Sync dependencies** (creates virtual environment):
    ```bash
    uv sync
    ```

## Usage

Start the application:

```bash
uv run src/main.py
```

### Commands
- **[A]dd**: Create a new task.
- **[V]iew**: List all tasks.
- **[U]pdate**: Edit a task.
- **[D]elete**: Remove a task.
- **[C]omplete**: Mark a task as done.
- **[E]xit**: Close the application.

## Development

Run unit tests:

```bash
uv run -m unittest discover tests
```

## Project Structure

```text
src/
├── models/         # Data classes
├── repositories/   # Data storage logic
├── services/       # Business logic
├── ui/             # CLI interface
└── main.py         # Entry point
tests/              # Unit tests
specs/              # Project specifications
```
