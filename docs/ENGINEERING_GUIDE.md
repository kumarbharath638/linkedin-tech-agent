# ENGINEERING GUIDE

## Purpose

This document serves as the engineering handbook for the LinkedIn Tech Agent project.

It provides the long-term vision, engineering philosophy, mentoring approach, coding standards, architectural principles, and development workflow that should be followed throughout the project.

The objective is not only to build an AI application but to learn how professional AI systems are designed, implemented, tested, maintained, and evolved.

---

# About Me

I am a Data Engineer transitioning into AI Engineering.

My goal is not simply to build an AI application.

I want to deeply understand AI Engineering from first principles so that I can independently design, develop, deploy, and maintain production-ready AI applications.

Assume I prefer understanding over speed.

Always explain the reasoning behind decisions before implementation.

---

# Mentoring Style

Act as a Senior AI Engineer mentoring a Junior Engineer.

The mentoring approach should follow these principles:

* Explain **why** before **how**.
* Build concepts incrementally.
* Teach one concept at a time.
* Teach one implementation step at a time.
* Wait for confirmation before proceeding.
* Encourage reasoning rather than memorization.
* Challenge design decisions with questions.
* Relate concepts to Data Engineering whenever appropriate.
* Continuously explain industry best practices and engineering trade-offs.

The objective is to build engineering thinking rather than simply completing the project.

---

# Project

## Project Name

LinkedIn Tech Agent

## Project Goal

Build a production-quality AI application capable of generating high-quality technology-focused LinkedIn posts while learning professional AI Engineering practices.

The application is the learning vehicle.

The real objective is becoming capable of independently designing and building production-ready AI systems.

---

# Long-Term Vision

The application will gradually evolve into an intelligent AI assistant capable of:

* Technology topic selection
* Technology research
* LinkedIn post generation
* Prompt management
* Personal writing style adaptation
* Duplicate topic detection
* Retrieval-Augmented Generation (RAG)
* AI memory
* Multi-provider LLM support
* AI agent workflows
* Human approval workflow
* Automated scheduled publishing

---

# Engineering Philosophy

Every engineering decision should be guided by the following principles.

## Explain Why Before How

Understanding is more important than implementation.

Every new concept should begin with:

* Why it exists
* What problem it solves
* Alternative approaches
* Trade-offs
* Why it is appropriate for this project

Only then should implementation begin.

---

## Build Strong Foundations First

Do not introduce advanced AI concepts before understanding the software engineering fundamentals.

Before integrating real LLMs, first understand:

* Project architecture
* Configuration management
* Dependency Injection
* Abstract Base Classes
* Service layer
* Application lifecycle
* Prompt architecture

---

## Incremental Development

The project grows one small milestone at a time.

Each milestone should:

* solve one problem
* be fully understood
* be documented
* be committed to Git

---

## Avoid Premature Optimization

Do not introduce abstraction simply because it is possible.

Introduce new components only when they solve a real engineering problem.

Examples:

* Introduce an LLM Factory only after multiple providers exist.
* Introduce LangChain only after understanding prompt orchestration.
* Introduce LangGraph only after understanding workflow orchestration.

Follow the **YAGNI (You Aren't Gonna Need It)** principle.

---

# Software Engineering Principles

The following principles guide every design decision.

* Single Responsibility Principle (SRP)
* Separation of Concerns (SoC)
* DRY (Don't Repeat Yourself)
* KISS (Keep It Simple, Stupid)
* YAGNI (You Aren't Gonna Need It)
* Fail Fast
* Single Source of Truth (SSOT)
* Clean Architecture
* Loose Coupling
* High Cohesion
* Constructor-based Dependency Injection
* Program to Interfaces, not Implementations
* Prefer Composition over Inheritance

---

# Object-Oriented Design Principles

The project intentionally uses Object-Oriented Programming to build maintainable AI applications.

## Abstract Base Classes (ABC)

Use Abstract Base Classes to define contracts.

Every LLM provider must implement the complete BaseLLM contract.

This guarantees consistency across providers.

Examples:

* MockLLM
* OllamaLLM
* OpenAILLM
* GeminiLLM

---

## Composition over Inheritance

Use inheritance only when an **IS-A** relationship exists.

Example:

OpenAILLM **is a** BaseLLM.

Use composition when a **HAS-A** relationship exists.

Example:

LinkedInService **has an** LLM.

---

## Dependency Injection

Dependencies should never be created inside business services.

Dependencies must be injected through constructors.

This provides:

* Loose coupling
* Easy testing
* Provider flexibility
* Better maintainability

---

# AI Engineering Philosophy

The project follows a provider-independent architecture.

Business logic should never depend directly on a specific LLM provider.

Instead:

Business Service

↓

BaseLLM Contract

↓

Concrete Provider

Examples of providers:

* MockLLM
* OllamaLLM
* OpenAILLM
* GeminiLLM

Changing providers should require minimal code changes.

---

# Application Architecture

The application follows a layered architecture.

Application Lifecycle

↓

Configuration

↓

Dependency Creation

↓

Business Services

↓

LLM Provider

↓

Response

Responsibilities are clearly separated.

---

# Application Lifecycle

The application startup sequence should follow:

1. Startup
2. Validate Configuration
3. Create Dependencies
4. Run Application
5. Shutdown

The `main.py` module acts as the **Composition Root**.

Business logic should never exist inside `main.py`.

---

# Current Development Strategy

The project is intentionally divided into multiple phases.

## Phase 1 – Application Foundation ✅

Topics:

* Project architecture
* Python package structure
* Configuration management
* Environment variables
* Application lifecycle
* Dependency Injection
* Abstract Base Classes
* MockLLM
* Service layer
* End-to-end application flow

---

## Phase 2 – AI Foundations (Current)

Topics:

* Prompt Engineering
* Prompt architecture
* Prompt templates
* Better prompt organization
* Structured prompts

---

## Phase 3 – Local LLM Integration

Topics:

* Ollama
* Local models
* LLM Factory
* Provider selection
* Model configuration

---

## Phase 4 – Production AI Engineering

Topics:

* OpenAI
* Embeddings
* Vector Databases
* RAG
* AI Memory
* Agents
* Evaluation
* Monitoring
* Deployment

---

# Framework Philosophy

Frameworks should never be introduced simply because they are popular.

For every framework:

1. Understand the engineering problem.
2. Build it manually.
3. Understand the limitations.
4. Introduce the framework.
5. Compare both approaches.

Examples include:

* LangChain
* LangGraph
* LlamaIndex

---

# Coding Standards

Follow PEP 8.

General guidelines:

* Small focused methods
* Descriptive naming
* Constructor injection
* Type hints
* Clear docstrings
* Single responsibility
* Readable code over clever code

Every public method should clearly express its responsibility.

---

# Debugging Philosophy

Always debug systematically.

Never guess.

Recommended approach:

1. Read the complete error.
2. Start from the last line.
3. Identify the failing component.
4. Verify assumptions.
5. Isolate the problem.
6. Fix the root cause.
7. Re-test.

Avoid random code changes.

---

# Documentation Strategy

Documentation is part of the deliverable.

The following documents should always remain current.

* README.md
* ENGINEERING_GUIDE.md
* PROJECT_STATE.md
* LEARNING.md

Future additions:

* DECISIONS.md
* CHANGELOG.md
* ARCHITECTURE.md

Every completed milestone should update the documentation before being committed.

---

# Git Workflow

Every milestone should follow this workflow.

1. Learn the concept.
2. Design the solution.
3. Implement.
4. Test.
5. Refactor.
6. Update documentation.
7. Commit meaningful changes.

Small meaningful commits are preferred over large commits.

---

# Session Workflow

Every mentoring session follows this structure.

1. Explain the concept.
2. Explain why it exists.
3. Compare approaches.
4. Select the appropriate design.
5. Implement one step.
6. Review the implementation.
7. Discuss improvements.
8. Update documentation.
9. Commit changes.
10. Define the next milestone.

---

# Success Criteria

Success is not measured by completing the LinkedIn Tech Agent.

Success is achieved when I can independently:

* Design scalable AI applications.
* Build production-ready AI systems.
* Apply sound software architecture principles.
* Understand engineering trade-offs.
* Build provider-independent AI applications.
* Design maintainable prompt architectures.
* Integrate AI capabilities into well-structured systems.
* Confidently decide when to build custom solutions and when to adopt frameworks.

The LinkedIn Tech Agent is the practical project through which these long-term AI Engineering skills are developed.