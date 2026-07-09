# Development Setup

## Purpose

This document defines the standard development environment, engineering practices, and contribution workflow for TalentOS.

Its goal is to ensure every contributor can:

- Set up the project consistently.
- Follow the same coding standards.
- Use a unified development workflow.
- Maintain high code quality.
- Contribute changes with confidence.

This document serves as the primary reference for development practices throughout the TalentOS project.


## Development Philosophy

## Development Philosophy

TalentOS follows an AI-first, developer-friendly, and maintainable engineering approach. Every implementation should prioritize simplicity, readability, scalability, and automation.

The project is guided by the following principles:

- **Build for maintainability** – Write code that is easy to understand, modify, and extend.
- **Prefer simplicity** – Choose the simplest solution that satisfies the requirements.
- **Automate repetitive work** – Use tooling for formatting, linting, testing, and quality checks whenever possible.
- **Keep components modular** – Design services and modules with clear responsibilities and minimal coupling.
- **Fail fast** – Detect errors early through validation, type checking, automated tests, and CI.
- **Document decisions** – Significant architectural or technical decisions should be recorded using Architecture Decision Records (ADRs).
- **Consistency over preference** – Project-wide conventions take precedence over individual coding styles.
- **Security by default** – Never commit secrets, validate external inputs, and follow secure development practices.

## Prerequisites

## Prerequisites

Before setting up TalentOS, ensure the following tools are installed:

| Tool | Recommended Version | Purpose |
|------|----------------------|---------|
| Git | Latest Stable | Version control |
| Python | 3.13+ | Backend development |
| uv | Latest Stable | Python package and environment management |
| Node.js | 22 LTS | Frontend development |
| npm | Bundled with Node.js | Frontend package management |
| Docker Desktop | Latest Stable | Containerized development and services |
| Visual Studio Code | Latest Stable | Recommended IDE |

### Recommended VS Code Extensions

- Python
- Ruff
- Pylance
- ESLint
- Prettier
- Docker
- GitLens
- GitHub Pull Requests
- Markdown All in One

> Future tooling requirements should be added to this section as the project evolves.

## Repository Structure

## Repository Structure

TalentOS follows a monorepo architecture, where all core components are maintained within a single repository.

The repository structure is defined in **TOS-008: Repository Structure**. Contributors should familiarize themselves with the directory layout before making changes.

General guidelines:

- Place backend code under the `backend/` directory.
- Place frontend code under the `frontend/` directory.
- Store project documentation in `docs/`.
- Keep automation scripts in `scripts/`.
- Place infrastructure-related files in `infra/`.
- Keep tests close to the code they validate or under dedicated `tests/` directories, following project conventions.
- Avoid creating new top-level directories without team discussion and approval.

> Any structural changes to the repository should be documented and, if significant, recorded through an Architecture Decision Record (ADR).

## Local Development Environment

## Local Development Environment

All development should be performed in an isolated local environment to ensure consistency across contributors.

The recommended setup process is:

1. Clone the repository.
2. Install backend dependencies using `uv`.
3. Install frontend dependencies using `npm`.
4. Create a local `.env` file from `.env.example`.
5. Start required infrastructure services (if applicable) using Docker.
6. Run the backend and frontend in development mode.
7. Verify the application starts successfully before making changes.

### General Guidelines

- Use isolated virtual environments for Python development.
- Do not install project dependencies globally.
- Keep local dependencies synchronized with the project's lock files.
- Regularly update your local branch from `develop` to minimize merge conflicts.
- Validate changes locally before opening a pull request.

> Detailed setup commands may evolve over time and should be maintained alongside the project configuration files.

## Dependency Management

## Dependency Management

TalentOS uses dedicated package managers for each technology stack to ensure reproducible builds and consistent development environments.

### Backend

- Use **uv** as the official Python package and environment manager.
- Manage project dependencies through `pyproject.toml`.
- Commit the lock file to version control.
- Avoid installing packages outside the project environment.
- Keep runtime and development dependencies clearly separated.

### Frontend

- Use **npm** as the official package manager.
- Manage dependencies through `package.json`.
- Commit `package-lock.json` to version control.
- Avoid using multiple package managers within the project.

### Dependency Guidelines

- Prefer stable releases over experimental versions.
- Remove unused dependencies promptly.
- Keep third-party libraries up to date.
- Evaluate new dependencies for security, maintenance, licensing, and community support before adoption.
- Significant dependency changes should be discussed through a GitHub issue and, when appropriate, documented in an ADR.

## Environment Variables

## Environment Variables

Application configuration should be managed through environment variables rather than hard-coded values.

### Configuration Files

The repository should include:

- `.env.example` — Template containing all required environment variables without sensitive values.
- `.env` — Local development configuration (never committed to version control).

### Guidelines

- Never commit secrets, API keys, passwords, or tokens.
- Use descriptive environment variable names.
- Keep default values only in `.env.example` when appropriate.
- Store production secrets using the deployment platform's secret management solution.
- Rotate credentials immediately if they are accidentally exposed.

### Best Practices

- Validate required environment variables during application startup.
- Document every new environment variable in `.env.example`.
- Remove obsolete variables as part of regular maintenance.
- Keep development, staging, and production configurations separate.

## Running the Application

## Running the Application

TalentOS should be runnable in a consistent manner across all development environments.

Before starting the application:

- Ensure all dependencies are installed.
- Configure the local `.env` file.
- Start any required infrastructure services.
- Verify that all required ports are available.

### Development Workflow

The recommended workflow is:

1. Start supporting services (if required).
2. Start the backend development server.
3. Start the frontend development server.
4. Confirm both services are running successfully.
5. Verify that the frontend can communicate with the backend.
6. Run the test suite before committing changes.

### Validation Checklist

Before beginning development, verify that:

- The backend starts without errors.
- The frontend loads successfully.
- Database connectivity is working (if applicable).
- Required APIs are reachable.
- Environment variables are loaded correctly.

> The exact startup commands are maintained alongside the project configuration and may evolve as the project grows.

## Code Quality Standards

## Code Quality Standards

TalentOS prioritizes readable, maintainable, and well-tested code over clever or overly complex implementations.

All contributors are expected to follow consistent coding practices across the project.

### Backend Standards

- Follow PEP 8 where applicable.
- Use type hints for public functions, methods, and classes.
- Prefer small, single-responsibility functions.
- Write descriptive variable, function, and class names.
- Use asynchronous programming (`async`/`await`) where appropriate.
- Avoid duplicated logic.
- Favor composition over inheritance unless inheritance provides a clear benefit.
- Keep business logic separate from infrastructure and framework code.
- Add docstrings for public modules, classes, and complex functions.

### Frontend Standards

- Use TypeScript instead of JavaScript wherever possible.
- Build reusable UI components.
- Keep components focused on a single responsibility.
- Prefer composition over deeply nested component hierarchies.
- Avoid unnecessary state and prop drilling.
- Use consistent naming conventions for components, hooks, and utilities.
- Separate presentation logic from business logic.

### General Principles

- Write self-documenting code whenever possible.
- Keep functions and files reasonably small.
- Remove dead code before merging.
- Avoid premature optimization.
- Prefer explicit behavior over implicit behavior.
- Refactor when complexity begins to increase.y

## Testing Strategy

Testing is a fundamental part of the TalentOS development workflow. Every feature should include an appropriate level of automated testing.

### Testing Principles

- Write tests for new functionality.
- Update tests when modifying existing behavior.
- Fix failing tests before merging changes.
- Prefer automated tests over manual verification.
- Keep tests deterministic, isolated, and repeatable.

### Backend Testing

- Use **pytest** as the primary testing framework.
- Write unit tests for business logic.
- Write integration tests for APIs, database interactions, and external services where appropriate.
- Mock external dependencies whenever practical.

### Frontend Testing

- Use **Vitest** for unit testing.
- Test reusable components and business logic.
- Minimize reliance on snapshot tests.
- Focus on user-facing behavior rather than implementation details.

### End-to-End Testing

As TalentOS matures, end-to-end tests should validate critical user workflows, including:

- User authentication
- Resume management
- Job discovery
- AI-assisted resume tailoring
- Job application workflows

### Coverage Expectations

The goal is meaningful test coverage rather than maximizing coverage percentages. Critical business logic should always be tested.

## Git Workflow

TalentOS follows a feature-branch workflow to ensure stable development and well-reviewed changes.

### Workflow

```text
GitHub Issue
      ↓
Create Feature Branch
      ↓
Implement Changes
      ↓
Local Testing
      ↓
Commit Changes
      ↓
Open Pull Request
      ↓
Code Review
      ↓
Merge into develop
```

### Development Rules

- Every change must begin with a GitHub issue.
- Create a dedicated feature branch from `develop`.
- Keep pull requests focused on a single issue.
- Rebase or merge the latest `develop` branch before opening a pull request if necessary.
- Resolve conflicts locally before requesting a review.
- Merge only after all required checks have passed.
- Delete feature branches after they have been merged.

## Branch Naming Convention

Branch names should clearly indicate the type of work being performed and reference the related GitHub issue whenever possible.

### Naming Format

```text
<type>/<issue-id>-<short-description>
```

### Examples

```text
feature/TOS-010-development-setup
feature/TOS-023-authentication

bugfix/TOS-041-login-timeout

hotfix/TOS-087-production-crash

docs/TOS-012-api-documentation

refactor/TOS-065-workflow-engine

chore/TOS-030-update-dependencies
```

### Branch Types

| Type | Purpose |
|------|---------|
| `feature` | New functionality |
| `bugfix` | Bug fixes |
| `hotfix` | Urgent production fixes |
| `docs` | Documentation updates |
| `refactor` | Code restructuring without functional changes |
| `chore` | Maintenance, tooling, dependency updates |

## Commit Message Convention

TalentOS follows the Conventional Commits specification to maintain a clear and consistent Git history.

### Format

```text
<type>: <short description>
```

### Examples

```text
feat: add authentication service

fix: resolve login timeout issue

docs: add development setup guide

refactor: simplify workflow orchestration

test: add unit tests for resume parser

chore: update project dependencies
```

### Supported Commit Types

| Type | Description |
|------|-------------|
| `feat` | Introduces a new feature |
| `fix` | Fixes a bug |
| `docs` | Documentation changes |
| `refactor` | Code restructuring without changing behavior |
| `test` | Adds or updates tests |
| `chore` | Maintenance tasks, tooling, dependencies |
| `ci` | CI/CD configuration changes |
| `build` | Build system or dependency changes |
| `perf` | Performance improvements |
| `style` | Formatting or stylistic changes only |

### Guidelines

- Use the imperative mood (e.g., "add", "fix", "update").
- Keep the subject line concise (preferably under 72 characters).
- Each commit should represent a single logical change.
- Avoid combining unrelated changes into one commit.

## Pull Request Process

All code changes must be submitted through a Pull Request (PR). Direct commits to protected branches are not permitted.

### Before Opening a Pull Request

Ensure that:

- The related GitHub issue is complete or ready for review.
- Your branch is up to date with `develop`.
- All automated tests pass locally.
- Code has been formatted and linted.
- Type checking passes without errors.
- Documentation has been updated if required.
- No sensitive information has been committed.

### Pull Request Checklist

- [ ] Linked to the appropriate GitHub issue
- [ ] Code follows project standards
- [ ] Tests added or updated where applicable
- [ ] All local tests pass
- [ ] Documentation updated (if required)
- [ ] No unnecessary files or dependencies included
- [ ] Ready for code review

### Code Review Expectations

Reviewers should verify:

- Correctness
- Readability
- Maintainability
- Test coverage
- Performance implications
- Security considerations
- Documentation updates

Pull requests should remain focused on a single feature, bug fix, or improvement to simplify review and reduce merge conflicts.

## Pre-commit Hooks

TalentOS uses pre-commit hooks to automatically enforce code quality before changes are committed.

### Objectives

Pre-commit hooks help ensure that:

- Code is consistently formatted.
- Linting issues are detected early.
- Basic quality checks run before commits.
- Common mistakes are prevented from entering the repository.

### Recommended Checks

The pre-commit workflow should include:

- Code formatting
- Linting
- Type checking (where practical)
- Removal of trailing whitespace
- End-of-file newline validation
- Detection of merge conflict markers
- Validation of common configuration files

### Guidelines

- Developers should not bypass pre-commit hooks except in exceptional circumstances.
- Hooks should complete quickly to avoid slowing down development.
- More comprehensive validation should continue to run in the CI pipeline.

## Docker Development

Docker provides a consistent development environment by containerizing supporting services and, where appropriate, application components.

### Objectives

Docker should be used to:

- Standardize local development environments.
- Reduce environment-specific issues.
- Simplify onboarding for new contributors.
- Support reproducible builds and testing.

### Development Guidelines

- Use Docker Compose to orchestrate local development services.
- Keep application configuration externalized through environment variables.
- Persist development data using Docker volumes where appropriate.
- Keep container images lightweight and focused on a single responsibility.
- Avoid storing application data inside containers.

### Best Practices

- Rebuild containers after significant dependency changes.
- Keep Docker configuration under version control.
- Use official base images whenever practical.
- Regularly update base images to receive security patches.

> Docker is intended to simplify development and testing. Production deployment strategies may differ and should be documented separately.

## Continuous Integration

Every pull request should be validated through an automated Continuous Integration (CI) pipeline before it is eligible for merging.

### CI Objectives

The CI pipeline should:

- Detect issues early.
- Enforce consistent code quality.
- Verify application integrity.
- Prevent regressions.

### Minimum Quality Gates

Every pull request should successfully complete:

- Code formatting validation
- Linting
- Static type checking
- Backend test execution
- Frontend test execution
- Build verification

### Future Enhancements

As TalentOS evolves, the CI pipeline may include:

- Security vulnerability scanning
- Dependency auditing
- Container image scanning
- Performance benchmarking
- End-to-end testing
- Code coverage reporting

A pull request should not be merged until all required CI checks have passed.

## Versioning Strategy

TalentOS follows **Semantic Versioning (SemVer)** for all official releases.

### Version Format

```text
MAJOR.MINOR.PATCH
```

Example:

```text
1.4.2
```

### Versioning Rules

| Component | When to Increment |
|-----------|-------------------|
| **MAJOR** | Breaking or incompatible changes |
| **MINOR** | New backward-compatible features |
| **PATCH** | Backward-compatible bug fixes |

### Guidelines

- Development work may occur between official releases.
- Version numbers should only change as part of the release process.
- Breaking changes should be clearly documented.
- Release notes should summarize significant changes introduced in each version.

Following Semantic Versioning helps contributors and users understand the impact of upgrading to a newer release.

### Developer Best Practices

The following practices help maintain a high-quality, scalable, and collaborative codebase.

### General Guidelines

- Understand the related GitHub issue before starting implementation.
- Keep changes focused on a single objective.
- Prefer clarity over cleverness.
- Write code that is easy to read, test, and maintain.
- Leave the codebase in a better state than you found it.

### Documentation

- Update documentation whenever functionality or behavior changes.
- Record significant architectural decisions using ADRs.
- Write meaningful comments only when the intent is not obvious from the code.

### Collaboration

- Communicate design decisions early.
- Request reviews proactively.
- Address review feedback constructively.
- Share knowledge through documentation rather than tribal knowledge.

### Continuous Improvement

- Refactor when complexity becomes difficult to manage.
- Remove obsolete code and dependencies.
- Learn from production issues and incorporate improvements into the development process.
- Continuously improve tooling, automation, and engineering practices.

## References

- ADR-001: TalentOS is a Career Operating System
- ADR-002: Backend Technology Selection
- TOS-008: Repository Structure
- TOS-009: Technology Stack

## Future Improvements

Future revisions may include:

- AI-assisted development workflow
- Automated dependency updates
- Dev Containers
- Remote development
- Release automation
- Security scanning standards
