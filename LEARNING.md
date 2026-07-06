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