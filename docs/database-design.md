# Database Design

## Purpose

This document defines the logical database design for TalentOS MVP.

It identifies the core entities, their relationships, and the data required to support the application's functionality while remaining independent of any specific database technology.

---

## Database Design Principles

The TalentOS database is designed according to the following principles:

### DP-001 Single Source of Truth

Each business entity shall have one authoritative record.

---

### DP-002 Normalization

Data should be normalized to reduce duplication while maintaining efficient querying.

---

### DP-003 Extensibility

The schema should support future modules without major redesign.

---

### DP-004 Referential Integrity

Relationships between entities shall be maintained using foreign keys or equivalent mechanisms.

---

### DP-005 Auditability

Important business events such as applications and profile updates should be traceable.

---

### DP-006 Security

Sensitive user information shall be stored securely and protected according to security best practices.

## Core Entities

The TalentOS MVP consists of the following core entities:

### User

Represents a registered TalentOS user.

---

### Career Profile

Stores the user's professional profile generated from their resume and career preferences.

---

### Resume

Stores uploaded resumes and generated resume versions.

---

### Job

Represents job opportunities collected from supported job platforms.

---

### Job Cluster

Groups similar job opportunities into career clusters.

---

### Application

Represents a job application submitted by the user.

---

### Cover Letter

Stores AI-generated cover letters associated with applications.

---

### Dashboard

Represents aggregated user metrics and summaries displayed on the home dashboard.

---

### Insight

Stores AI-generated recommendations, resume insights, and career analytics.

### User

Represents a registered TalentOS user.

---

### Career Profile

Stores the user's professional profile generated from their resume and career preferences.

---

### Resume

Stores uploaded resumes and generated resume versions.

---

### Job

Represents job opportunities collected from supported job platforms.

---

### Job Cluster

Groups similar job opportunities into career clusters.

---

### Application

Represents a job application submitted by the user.

---

### Cover Letter

Stores AI-generated cover letters associated with applications.

---

### Dashboard

Represents aggregated user metrics and summaries displayed on the home dashboard.

---

### Insight

Stores AI-generated recommendations, resume insights, and career analytics.

---

## Entity Relationships

The following relationships define how the core entities interact.

```text
User
 │
 ├───────────────┐
 ▼               ▼
Career Profile   Resume
 │               │
 │               ▼
 │         Cover Letter
 │
 ▼
Job Cluster
 │
 ▼
Job
 │
 ▼
Application
 │
 ▼
Insight

User
 │
 ▼
Dashboard
```

### Relationship Summary

- One **User** owns one **Career Profile**.
- One **User** can have multiple **Resumes**.
- One **Career Profile** can match multiple **Job Clusters**.
- One **Job Cluster** contains multiple **Jobs**.
- One **Job** can result in one or more **Applications**.
- Each **Application** may reference one **Resume** and one **Cover Letter**.
- **Dashboard** aggregates information from Applications, Jobs, and Insights.
- **Insights** are generated using data from the Career Profile, Jobs, and Applications.

---

## Entity Definitions

### User

**Purpose:** Represents a registered TalentOS user.

**Key Attributes:**

- User ID
- Full Name
- Email
- Authentication Provider
- Account Status
- Created At
- Updated At

---

### Career Profile

**Purpose:** Stores the structured professional profile used by TalentOS.

**Key Attributes:**

- Career Profile ID
- User ID
- Skills
- Experience
- Education
- Certifications
- Career Preferences
- AI Profile Summary

---

### Resume

**Purpose:** Stores uploaded and AI-generated resumes.

**Key Attributes:**

- Resume ID
- User ID
- Resume Type (Original / Tailored)
- Version
- File Location
- Created At

---

### Job

**Purpose:** Represents a job opportunity.

**Key Attributes:**

- Job ID
- Job Title
- Company
- Location
- Employment Type
- Job Description
- Source Platform
- Match Score

---

### Job Cluster

**Purpose:** Groups similar jobs together.

**Key Attributes:**

- Cluster ID
- Cluster Name
- Target Role
- Average Match Score

---

### Application

**Purpose:** Tracks job applications.

**Key Attributes:**

- Application ID
- User ID
- Job ID
- Resume ID
- Cover Letter ID
- Status
- Applied Date

---

### Cover Letter

**Purpose:** Stores AI-generated cover letters.

**Key Attributes:**

- Cover Letter ID
- User ID
- Resume ID
- Content
- Version

---

### Dashboard

**Purpose:** Represents aggregated dashboard information.

**Key Attributes:**

- Dashboard ID
- User ID
- Total Applications
- Active Applications
- Interview Count
- Offer Count

---

### Insight

**Purpose:** Stores AI-generated recommendations and analytics.

**Key Attributes:**

- Insight ID
- User ID
- Insight Type
- Recommendation
- Generated At

---

## Future Expansion

The database schema is designed to support future enhancements without requiring major structural changes.

### Planned Future Entities

The following entities may be introduced in future phases:

- Interview
- Recruiter
- Company
- Notification
- Learning Recommendation
- Career Goal
- Skill Assessment
- Salary Benchmark
- Browser Extension Session
- AI Conversation History

---

### Schema Evolution Goals

The database design should support:

- Multiple resumes per career strategy
- Multiple AI providers
- Additional job platforms
- Mobile applications
- Public API integrations
- Audit history for major user actions
- Analytics and reporting

Future entities should integrate with the existing schema while preserving referential integrity and minimizing breaking changes.
