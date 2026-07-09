# TalentOS Decision Log

> This document records significant product, business, UX, and engineering decisions made during the development of TalentOS.
>
> Unlike ADRs, these decisions do not necessarily define the software architecture. They capture why important product directions were chosen and provide historical context for future contributors.

---

## Decision Categories

| Prefix | Category |
|---------|----------|
| PD | Product Decision |
| UX | User Experience |
| ED | Engineering Decision |
| AI | AI / LLM Decision |
| BD | Business Decision |

---

# 2026

---

## PD-001

**Date:** 2026-07-02

### Decision

TalentOS is an AI Career Operating System.

### Reason

Users need a unified career workspace instead of another job application bot.

### Impact

This changes the scope from automation-only to end-to-end career management.

---

## PD-002

**Date:** 2026-07-02

### Decision

Review Mode will be the default application workflow before introducing Autonomous Mode.

### Reason

Trust must be established before allowing AI to submit applications without user approval.

### Impact

The MVP will require user confirmation before every application.

---

## PD-003

**Date:** 2026-07-02

### Decision

The Dashboard will become the primary workspace.

### Reason

Users should always know what requires their attention next.

### Impact

Every feature should ultimately surface actionable information on the dashboard.

---

## PD-004

**Date:** 2026-07-02

### Decision

TalentOS will initially target experienced professionals rather than fresh graduates.

### Reason

Experienced professionals have more complex job search workflows and gain greater value from automation.

---

## PD-005

**Date:** 2026-07-02

### Decision

Job Clustering is a core platform capability.

### Reason

Similar job postings should be grouped to reduce duplicate applications and improve job management.

---

## ED-001

**Date:** 2026-07-08

### Decision

Python + FastAPI selected as backend technology.

### Reason

Excellent ecosystem for AI, browser automation, async APIs, and rapid development.

### Reference

ADR-002

---

## ED-002

**Date:** 2026-07-08

### Decision

Development follows a Git Flow model.

### Reason

Feature branches, pull requests, and code reviews provide a scalable development workflow.

---

## ED-003

**Date:** 2026-07-08

### Decision

All major technical decisions must be documented as ADRs.

### Reason

Architectural decisions should remain traceable as the project evolves.

---

## ED-004

**Date:** 2026-07-08

### Decision

Product decisions will be documented separately from architectural decisions.

### Reason

Not every important decision belongs in an ADR. Separating concerns keeps architectural documentation focused while preserving product history.

---

# Decision Index

| ID | Category | Summary | Status |
|----|----------|---------|--------|
| PD-001 | Product | TalentOS is a Career Operating System | Active |
| PD-002 | Product | Review Mode before Autonomous Mode | Active |
| PD-003 | Product | Dashboard is primary workspace | Active |
| PD-004 | Product | Target experienced professionals first | Active |
| PD-005 | Product | Job Clustering is a core capability | Active |
| ED-001 | Engineering | Backend uses Python + FastAPI | Active |
| ED-002 | Engineering | Git Flow workflow | Active |
| ED-003 | Engineering | ADRs required for architecture | Active |
| ED-004 | Engineering | Separate Product Decisions from ADRs | Active |
