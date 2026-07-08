# TalentOS Technology Stack

**Document ID:** TOS-009  
**Status:** Draft  
**Version:** 1.0  
**Last Updated:** 2026-07-08

---

# Purpose

This document defines the official technology stack for TalentOS.

Each technology has been selected based on:

- Alignment with the system architecture
- MVP requirements
- Long-term scalability
- Maintainability
- Developer productivity
- AI-first product vision

This document serves as the single source of truth for technology decisions throughout the project.

---

# Technology Stack

## 1. Backend

| Category | Technology | Version | Rationale |
|----------|------------|---------|-----------|
| Language | Python | 3.13+ | Excellent AI ecosystem, rapid development, strong community support |
| Framework | FastAPI | Latest Stable | High performance, async support, automatic OpenAPI documentation |
| API Style | REST | - | Simple, widely adopted, suitable for MVP |
| Runtime | ASGI | - | Supports asynchronous request handling |
| Package Manager | uv | Latest Stable | Fast dependency management and reproducible environments |
| Dependency Management | pyproject.toml | PEP 621 | Modern Python project standard |
| Testing | pytest | Latest Stable | Industry-standard Python testing framework |

## 2. Database

### Decision

**PostgreSQL**

### Why

- Excellent support for relational data.
- ACID-compliant transactions.
- JSONB support for semi-structured AI outputs.
- Mature ecosystem and strong community.
- Easy migration to managed cloud services.
- Well supported by SQLAlchemy and FastAPI.

### Alternatives Considered

| Technology | Reason Not Selected |
|------------|---------------------|
| MySQL | Fewer advanced features for our use case. |
| SQLite | Suitable for prototypes but not for concurrent production workloads. |
| MongoDB | Less suitable for the highly relational TalentOS data model. |

## 3. Frontend

### Decision

- **Framework:** React
- **Language:** TypeScript
- **Build Tool:** Vite
- **Styling:** Tailwind CSS
- **UI Components:** shadcn/ui
- **Routing:** React Router
- **Server State:** TanStack Query

### Why

- React has a mature ecosystem and a large community.
- TypeScript improves code quality and maintainability.
- Vite provides a fast development experience and optimized builds.
- Tailwind CSS enables rapid, consistent UI development.
- shadcn/ui offers accessible, customizable, production-ready components.
- React Router is the standard routing solution for React applications.
- TanStack Query simplifies server-state management, caching, and synchronization.

### Alternatives Considered

| Technology | Reason Not Selected |
|------------|---------------------|
| Angular | Powerful but adds unnecessary complexity for the MVP. |
| Vue | Excellent framework, but React has a larger ecosystem and aligns better with our long-term goals. |

## 4. Authentication

### Decision

- **Strategy:** JWT Access Token + Refresh Token
- **Password Hashing:** bcrypt
- **Future Support:** Google OAuth, GitHub OAuth

### Why

- Complete control over authentication and authorization.
- No dependency on third-party authentication providers.
- Well supported by FastAPI and modern web applications.
- Easy to extend with OAuth providers in future releases.

### Alternatives Considered

| Technology | Reason Not Selected |
|------------|---------------------|
| Clerk | Excellent developer experience, but introduces vendor lock-in and recurring costs. |
| Auth0 | Powerful enterprise solution, but unnecessary for the MVP. |
| OAuth Only | Does not support traditional email/password authentication on its own. |

## 5. AI Integration

### Decision

- **Architecture:** Provider Abstraction Layer
- **Initial Provider:** OpenAI
- **Future Providers:** Anthropic, Google Gemini, Ollama, Azure OpenAI

### Why

- Keeps the application independent of any single AI provider.
- Makes it easy to switch providers or use multiple providers.
- Simplifies testing and future feature development.
- Supports cost optimization by allowing provider selection based on workload.

### Design Principle

The application should never call an LLM provider directly. All AI interactions must go through a centralized AI Service Layer.

### Alternatives Considered

| Approach | Reason Not Selected |
|----------|---------------------|
| Direct OpenAI Integration | Creates vendor lock-in and makes future migration difficult. |
| Multiple Provider Integrations Everywhere | Increases complexity and duplicates logic across the codebase. |

## 6. Background Processing

### Decision

- **Task Queue:** Celery
- **Message Broker:** Redis
- **Result Backend:** Redis

### Why

TalentOS performs several long-running operations that should not block API requests, including:

- Resume parsing
- AI analysis
- Job scraping
- Email notifications
- Scheduled tasks
- Future autonomous agents

Celery provides a mature and scalable distributed task processing framework.

### Alternatives Considered

| Technology | Reason Not Selected |
|------------|---------------------|
| RQ | Simpler but less feature-rich than Celery. |
| Dramatiq | Promising, but Celery has a larger ecosystem and community. |
| FastAPI BackgroundTasks | Suitable for lightweight tasks only; not appropriate for production workloads. |

---

## 7. Cache

### Decision

**Redis**

### Why

Redis will be used for:

- Application caching
- Celery broker
- Celery result backend
- Rate limiting
- Temporary AI context
- Short-lived application state

Using Redis for multiple responsibilities keeps the MVP architecture simple while remaining highly scalable.

## 8. File Storage

### Decision

- **Development:** Local File System
- **Production:** Amazon S3-compatible Object Storage

### Why

TalentOS needs to store:

- Resumes
- Cover letters
- Generated documents
- Attachments
- Future portfolio assets

The application will use a storage abstraction layer so that the underlying storage provider can be changed without affecting business logic.

### Alternatives Considered

| Technology | Reason Not Selected |
|------------|---------------------|
| Database BLOB Storage | Increases database size and reduces performance. |
| Local Storage in Production | Not scalable for distributed deployments. |

---

## 9. Infrastructure

### Decision

| Component | Technology |
|----------|------------|
| Containerization | Docker |
| Local Orchestration | Docker Compose |
| Production Cloud | AWS |
| Production Database | Amazon RDS (PostgreSQL) |
| Cache | Amazon ElastiCache (Redis) |
| Object Storage | Amazon S3 |
| Monitoring | Amazon CloudWatch |

### Why

- Docker ensures consistent development and deployment environments.
- Docker Compose simplifies local development.
- AWS provides a mature ecosystem and managed services that align with TalentOS's long-term growth.
- Managed services reduce operational overhead and improve reliability.

### Future Roadmap

Kubernetes will be considered only when application scale justifies container orchestration.

## 10. DevOps

### Decision

- **CI/CD:** GitHub Actions
- **Version Control:** Git + GitHub
- **Branching Strategy:** Git Flow (main, develop, feature/*)

### Why

- Native GitHub integration.
- Automated quality checks.
- Repeatable deployment pipeline.
- Consistent development workflow.

---

## 11. Code Quality

### Decision

| Tool | Purpose |
|------|---------|
| Ruff | Linting |
| Black | Code formatting |
| mypy | Static type checking |
| pytest | Unit & integration testing |
| pre-commit | Pre-commit hooks |

### Why

These tools enforce a consistent codebase, catch issues early, and reduce review effort by automating formatting and quality checks.

## 12. Observability

### Logging

- Structured JSON logs
- Request correlation IDs
- Configurable log levels

### Monitoring

- **MVP:** AWS CloudWatch
- **Future:** Prometheus + Grafana

### Error Tracking

- **Future:** Sentry

### Secrets Management

- Development: `.env`
- Production: AWS Secrets Manager

---

# Engineering Principles

The TalentOS technology stack follows these principles:

1. **Choose the simplest solution that satisfies current requirements.**
2. **Avoid vendor lock-in whenever practical.**
3. **Prefer open standards over proprietary solutions.**
4. **Design for maintainability before optimization.**
5. **Introduce complexity only when justified by product growth.**
6. **Keep business logic independent of infrastructure and third-party services.**
7. **Favor proven, well-supported technologies over emerging trends.**

**Document ID:** TOS-009
**Status:** Draft
...

# Table of Contents

1. Purpose
2. Backend
3. Database
4. Frontend
5. Authentication
6. AI Integration
7. Background Processing
8. Cache
9. File Storage
10. Infrastructure
11. DevOps
12. Code Quality
13. Observability
14. Engineering Principles

### Status

✅ Accepted

### Version

Python 3.13+

FastAPI 0.116+

PostgreSQL 17

React 19

TypeScript 5

Redis 8

Docker 28

# Future Considerations

The following technologies may be adopted in future releases:

- Kubernetes
- Prometheus
- Grafana
- Sentry
- Azure OpenAI
- Anthropic
- Ollama
- Elasticsearch

| Layer    | Technology     |
| -------- | -------------- |
| Backend  | FastAPI        |
| Language | Python         |
| Frontend | React          |
| Database | PostgreSQL     |
| Cache    | Redis          |
| Queue    | Celery         |
| Auth     | JWT            |
| Cloud    | AWS            |
| CI       | GitHub Actions |

This document is the authoritative reference for technology choices in TalentOS. Changes to these decisions should be made through a new ADR and reviewed before implementation.
