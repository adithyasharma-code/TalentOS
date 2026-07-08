# ADR-002: Backend Technology Selection

**Status:** Accepted

**Date:** 2026-07-08

---

## Context

TalentOS is an AI-first Career Operating System that integrates LLMs, browser automation, resume parsing, workflow orchestration, and external APIs.

The backend technology should support:

- Rapid MVP development
- AI integrations
- High developer productivity
- Modern asynchronous APIs
- Long-term scalability
- Maintainability

Several backend technologies were evaluated:

- Python (FastAPI)
- TypeScript (NestJS)
- Java (Spring Boot)

---

## Decision

TalentOS will use:

- Python 3.13+
- FastAPI
- ASGI
- REST APIs
- async/await programming model
- uv for dependency management

---

## Rationale

Python provides the strongest ecosystem for:

- AI and LLM integrations
- Browser automation
- Workflow automation
- Data processing
- Rapid feature development

FastAPI offers:

- Excellent performance
- Automatic OpenAPI documentation
- Type validation
- Dependency injection
- Native async support
- Minimal boilerplate

This combination aligns with both the MVP requirements and the long-term vision of TalentOS.

---

## Consequences

### Positive

- Fast iteration
- Excellent AI ecosystem
- Easy onboarding
- Large community
- Clean architecture

### Negative

- Slightly lower raw performance than Java
- Requires discipline around typing and code quality

These trade-offs are acceptable for the expected workload and product roadmap.

---

## Alternatives Considered

### NestJS

Pros:

- Strong architecture
- Excellent TypeScript ecosystem

Cons:

- Smaller AI ecosystem

### Spring Boot

Pros:

- Enterprise-grade
- High performance

Cons:

- Slower development
- More boilerplate
