# Evolution of Todo - Phase I: In-Memory Console App

A robust command-line task manager built with Python 3.13+ using a Spec-Driven Development approach.

## Features

- **Add Task**: Create tasks with titles and optional descriptions.
- **View Tasks**: List all tasks in a formatted table.
- **Update Task**: Edit task titles and descriptions.
- **Delete Task**: Remove tasks by ID.
- **Complete Task**: Toggle task status to "Completed".
- **In-Memory Storage**: Data persists only while the application is running.

# 🚀 The Evolution of Todo: Phase I

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Package Manager](https://img.shields.io/badge/uv-Package%20Manager-orange.svg)](https://github.com/astral-sh/uv)
[![Methodology](https://img.shields.io/badge/Methodology-Spec--Driven%20Development-green.svg)](#-spec-driven-development)

Welcome to **Phase I** of the *Evolution of Todo* project. This phase delivers a robust, in-memory command-line interface (CLI) task manager designed with a strict **layered architecture** and a **Spec-Driven Development (SDD)** approach.

## 🎯 Project Goals

The objective of Phase I is to build a reliable foundation for a task management system, focusing on:
- **Clean Architecture**: Separation of concerns between UI, Business Logic, and Data Access.
- **Type Safety**: Leveraging Python 3.13's strict typing.
- **SDD Excellence**: Every line of code is mapped to a validated specification and plan.

## ✨ Features

- ✅ **Task Creation**: Capture titles (required) and detailed descriptions (optional).
- 📋 **Formatted View**: Clean, tabular display of all tasks with ID, Status, and Title.
- 🔄 **Status Toggling**: Seamlessly move tasks between `Pending` and `Completed`.
- ✏️ **Smart Updates**: Edit task details with "keep-existing" logic for empty inputs.
- 🗑️ **Deletion**: Remove tasks by unique identifier.
- 🛡️ **Robust Validation**: Graceful handling of invalid inputs and non-existent IDs.

## 🛠️ Tech Stack

- **Language**: Python 3.13+
- **Environment**: Linux / WSL 2
- **Package Manager**: [uv](https://github.com/astral-sh/uv)
- **Persistence**: Strict In-Memory (Volatile)
- **Standard Library**: Built exclusively with Python built-ins (`dataclasses`, `typing`, `unittest`).

## 🏗️ Spec-Driven Development

This project follows the **SpecKit Plus** workflow:
1.  **Constitution**: Core principles and technical non-negotiables.
2.  **Specification**: Detailed "WHAT" (User Journeys & Requirements).
3.  **Plan**: Architectural "HOW" (Design & Contracts).
4.  **Tasks**: Atomic, testable implementation work units.
5.  **Implementation**: Code execution mapped 1:1 to tasks.

You can find the full audit trail in the `specs/` and `history/` directories.

## 🚀 Quick Start

### Prerequisites
Ensure you have `uv` installed:
```bash
curl -LsSf https://astral-sh/uv/install.sh | sh
```

### Installation
1. Clone the repository and navigate to the project root.
2. Initialize the environment and sync dependencies:
```bash
uv sync
```

### Execution
Start the interactive CLI:
```bash
uv run src/main.py
```

### Running Tests
Execute the full test suite (Repository & CLI flow):
```bash
uv run -m unittest discover tests
```

## 📂 Project Structure

```text
phase1/
├── src/
│   ├── models/         # Domain Entities (Dataclasses)
│   ├── repositories/   # Data Access (In-Memory Storage)
│   ├── services/       # Business Logic & Validation
│   ├── ui/             # CLI Loop & Input Handling
│   └── main.py         # App Entry Point & Wiring
├── tests/              # Comprehensive Unit & Integration Tests
├── specs/              # Design Artifacts (Spec, Plan, Tasks)
├── history/            # Prompt History Records (Audit Trail)
├── CLAUDE.md           # Developer Context
└── pyproject.toml      # UV Project Configuration
```

## 🔄 Evolution Path

This is Phase I. Future phases will evolve this system into:
- **Phase II**: Full-Stack Web App (FastAPI + Next.js + PostgreSQL).
- **Phase III**: AI-Powered Chatbot (OpenAI SDK + MCP).
- **Phase IV**: Cloud-Native Deployment (Docker + Kubernetes).
- **Phase V**: Event-Driven Architecture (Kafka + Dapr).

---
*Developed as part of the Hackathon II: Spec-Driven Development.*
### Commands
- **[A]dd**: Create a new task.
- **[V]iew**: List all tasks.
- **[U]pdate**: Edit a task.
- **[D]elete**: Remove a task.
- **[C]omplete**: Mark a task as done.
- **[E]xit**: Close the application.
