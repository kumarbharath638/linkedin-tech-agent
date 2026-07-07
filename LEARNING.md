# AI Engineering Learning Journal

This document captures my learning journey while building the LinkedIn Tech Agent from scratch.

The goal is not only to remember **what** was done, but also **why** it was done.

---

# Session 1 – Development Environment Setup

## Objective

Set up a professional Python development environment for AI application development.

## Topics Covered

- Installing Python
- Installing Homebrew
- Installing Git
- Installing Visual Studio Code
- Opening a project from the terminal
- Installing the Python extension in VS Code

## Concepts Learned

### Python

Python is the programming language used to build this AI application.

### VS Code

VS Code is the Integrated Development Environment (IDE) used for writing, debugging, and managing the project.

### Git

Git is a distributed version control system that tracks changes made to the project over time.

### GitHub

GitHub is a cloud platform used to host Git repositories and collaborate on projects.

## Commands Learned

```bash
python3 --version
git --version
code .
```

## Reflection

Today I learned how to prepare a professional development environment for Python-based AI projects.

---

# Session 2 – Python and Virtual Environment

## Objective

Understand how Python executes programs and why virtual environments are important.

## Topics Covered

- Creating the first Python program
- Running Python scripts
- Creating a virtual environment
- Activating a virtual environment
- Selecting the Python interpreter in VS Code

## Concepts Learned

### Python Interpreter

The Python interpreter reads and executes Python code line by line.

### Virtual Environment

A virtual environment isolates project dependencies so that different Python projects do not interfere with one another.

### Why Virtual Environment?

Every project can maintain its own Python packages without affecting the system Python or other projects.

## Commands Learned

```bash
python main.py
python3 -m venv .venv
source .venv/bin/activate
which python
which pip
python --version
pip --version
```

## Reflection

I now understand why professional Python projects use isolated environments.

---

# Session 3 – Git Initialization

## Objective

Initialize the project using Git and understand version control fundamentals.

## Topics Covered

- Initializing a Git repository
- Understanding Git commits
- Creating a .gitignore file
- Creating project documentation

## Concepts Learned

### Repository

A Git repository stores the complete history of a project.

### Commit

A commit is a snapshot of the project at a specific point in time.

### .gitignore

The `.gitignore` file prevents unnecessary files and folders (such as `.venv`) from being tracked by Git.

## Reflection

A clean repository is an important part of professional software development.

---

# Session 4 – Designing a Professional AI Application Architecture

## Objective

Understand how professional AI applications are structured before implementing any AI functionality.

The focus of this session was not writing code, but learning the engineering principles that make AI applications scalable, maintainable, and production-ready.

---

## Topics Covered

* Repository vs Application
* Repository vs Package vs Module
* Python Packages
* Purpose of `__init__.py`
* Layered Architecture
* Separation of Concerns
* Single Responsibility Principle (SRP)
* Single Source of Truth (SSOT)
* Business Responsibilities vs Infrastructure Responsibilities
* Professional AI project folder structure
* Configuration Management (Introduction)

---

## Concepts Learned

### Repository

A repository contains everything required to develop and maintain a software project, including application code, documentation, tests, prompts, datasets, and configuration.

The application is only one part of the repository.

---

### Package

A package is a directory that groups related Python modules together.

Packages help organize the application into logical responsibilities and improve maintainability.

---

### Module

A module is a single Python file containing related classes, functions, or variables.

Multiple modules together form a package.

---

### Why `__init__.py`?

The `__init__.py` file explicitly identifies a directory as a Python package.

Although modern Python can work without it, using it is considered a professional best practice because it:

* Makes package boundaries explicit.
* Improves IDE and tooling support.
* Provides consistent project organization.
* Allows future package-level initialization when required.

---

### Repository vs Application

The repository contains the complete project.

The application is the executable software located under the `app/` package.

Only application code belongs inside `app/`.

Documentation, prompts, datasets, and tests belong outside the application package.

---

### Layered Architecture

Applications should be divided into layers with clear responsibilities.

Instead of every module performing every task, responsibilities are separated into dedicated components.

This improves maintainability and scalability.

---

### Separation of Concerns

Each module should have one clear responsibility.

Examples:

* Configuration
* Logging
* LLM Communication
* Business Logic
* Utilities

Keeping responsibilities separate reduces coupling and makes the application easier to extend.

---

### Single Responsibility Principle (SRP)

Every module should have one reason to change.

Instead of mixing multiple responsibilities into one file, each component should focus on one responsibility.

---

### Single Source of Truth (SSOT)

Configuration should be managed from one central location instead of being scattered throughout the application.

This simplifies maintenance, debugging, and future changes.

---

### Business Responsibilities vs Infrastructure Responsibilities

Business responsibilities represent what the application does.

Examples:

* Research technology topics
* Generate LinkedIn posts
* Retrieve supporting information

Infrastructure responsibilities support the application.

Examples:

* Configuration
* Logging
* LLM communication
* Utilities
* Validation

---

## Project Architecture Created

The application was reorganized into a scalable package structure.

```text
app/
│
├── config/
├── services/
├── llm/
├── prompts/
├── utils/
├── models/
└── main.py
```

Python packages were initialized using `__init__.py`.

Root folders for documentation, prompts, data, and tests were also created.

---

## Best Practices Learned

* Design the project architecture before implementing functionality.
* Organize projects by responsibility rather than file type.
* Separate business logic from infrastructure.
* Keep configuration centralized.
* Build incrementally instead of over-engineering.
* Make Git commits represent one meaningful architectural change.
* Write code that is maintainable by future developers, not just executable today.

---

## Connection to Data Engineering

Many architecture principles are shared between AI Engineering and Data Engineering.

Examples include:

* Separating business logic from infrastructure.
* Centralizing configuration.
* Organizing projects into logical modules.
* Building scalable and maintainable project structures.
* Using version control and documentation throughout the project lifecycle.

---

## Reflection

This session shifted my thinking from writing Python programs to designing software systems.

I learned that professional AI Engineering is not only about calling Large Language Models.

It is about building applications that remain maintainable, scalable, secure, and understandable as they grow.

Understanding why architectural decisions are made is more valuable than simply learning how to implement them.

---

## Questions for Future Revision

* Why should business logic be separated from infrastructure?
* Why is configuration centralized?
* What problem does `__init__.py` solve?
* What is the difference between a Repository, Package, and Module?
* Why should LLM communication be isolated from business logic?
* How does Layered Architecture improve maintainability?
