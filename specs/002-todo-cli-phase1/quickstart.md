# Quickstart: Phase I Todo Console App

## Prerequisites

- **Python**: 3.13 or higher
- **Package Manager**: `uv`

## Installation

1.  **Clone the repository** (if not already done).
2.  **Navigate to the project root**.
3.  **Sync dependencies** (creates virtual environment):
    ```bash
    uv sync
    ```

## Running the Application

To start the CLI application:

```bash
uv run src/main.py
```

## Running Tests

To run the unit tests:

```bash
uv run -m unittest discover tests
```

## Usage

Once the app is running, use the following letter commands:

- **[A]dd**: Create a new task.
- **[V]iew**: List all tasks.
- **[U]pdate**: Edit a task's title or description.
- **[D]elete**: Remove a task.
- **[C]omplete**: Mark a task as done.
- **[E]xit**: Close the application (Note: Data is not saved).
