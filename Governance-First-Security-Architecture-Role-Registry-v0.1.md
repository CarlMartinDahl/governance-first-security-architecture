# Governance-First Security Architecture - Role Registry v0.1

## Status

Preparatory documentation.

This document is not an implementation.

This document is not an access-control system.

This document defines canonical roles, authority boundaries, review rights, approval rights, and accountability requirements used by the Governance-First Security Architecture.

## Purpose

The purpose of the Role Registry is to ensure that decisions are accountable.

The model should never rely on vague ownership.

Every governed decision should be able to answer:

```text
Who requested it?
Who reviewed it?
Who approved it?
Who is accountable?
Who can stop it?
Who can recover it?
```

## Core Principle

```text
No authority without role, scope, record, and accountability.
```

A role is not just a title.

A role is a bounded set of allowed review, approval, stop, escalation, and recovery rights.

## Role Classes

The architecture uses these role classes:

- Human governance roles.
- Human technical roles.
- Human compliance and legal roles.
- Human security roles.
- AI-assisted roles.
- System roles.
- External review roles.

## Universal Role Rules

All roles are governed by these rules:

- Role must be named.
- Scope must be defined.
- Authority must be bounded.
- Approval must be recorded.
- Review must not be treated as approval unless explicitly authorized.
- Override must be scoped and audited.
- High-risk decisions require accountable human ownership.
- AI may assist but may not become accountable approver.

## Canonical Roles

### ROLE_USER_REQUESTER

Role class: Human requester.

Purpose:

Initiates a request, question, documentation step, review request, or proposed action.

May:

- ask questions,
- provide context,
- request documentation,
- request review,
- approve continued documentation work within personal project scope.

May not:

- automatically authorize high-risk action,
- bypass governance,
- convert request into approval by wording alone,
- authorize security or compliance claims without expert review.

Approval rights:

- Low-risk documentation continuation within current approved scope.

Review rights:

- May review outputs as project owner or requester.

Stop rights:

- May stop the process at any time.

Audit requirement:

Record requester, scope, and requested action for governed work.

### ROLE_SYSTEM_OWNER

Role class: Human accountable owner.

Purpose:

Owns the system scope, lifecycle mode, and major governance decisions.

May:

- define project scope,
- approve documentation milestones,
- approve internal review,
- approve external review package preparation,
- decide whether to pause, narrow, or continue.

May not:

- claim legal compliance without legal/compliance review,
- claim security validation without security review,
- approve production use alone,
- approve AI self-escalation.

Approval rights:

- Documentation scope.
- Review package preparation.
- Limited prototype design discussion after required reviews.

Review rights:

- Full project-scope review.

Stop rights:

- May stop any project activity.

Audit requirement:

Record major scope, lifecycle, and approval decisions.

### ROLE_GOVERNANCE_REVIEWER

Role class: Human governance role.

Purpose:

Reviews whether actions follow governance rules, mode boundaries, stop states, decision matrix, and capability gates.

May:

- review governance consistency,
- identify missing authority,
- identify missing evidence,
- require stop states,
- require mode clarification,
- require capability review.

May not:

- approve technical security claims alone,
- approve legal compliance claims alone,
- approve production use alone.

Approval rights:

- Governance-process approval within defined scope.

Review rights:

- Governance rules, role boundaries, decision states, mode transitions.

Stop rights:

- May trigger governance stop states.

Audit requirement:

Record review findings, required stops, and escalation decisions.

### ROLE_SECURITY_REVIEWER

Role class: Human security role.

Purpose:

Reviews security risks, egress controls, secrets, incident triggers, capability risks, and attack or misuse paths.

May:

- review threat model,
- review egress controls,
- review secret-handling rules,
- review capability expansion,
- review incident triggers,
- recommend lockdown or incident review.

May not:

- approve legal compliance claims alone,
- approve business risk acceptance alone,
- approve AI governance boundaries alone unless also assigned that role.

Approval rights:

- Security review acceptance within defined non-production scope.

Review rights:

- Security architecture, misuse cases, egress, secrets, controls, incident handling.

Stop rights:

- May trigger security stop, lockdown, or incident review.

Audit requirement:

Record security review scope, findings, and unresolved risks.

### ROLE_TECHNICAL_REVIEWER

Role class: Human technical role.

Purpose:

Reviews architecture feasibility, implementation boundaries, prototype design, testability, and technical assumptions.

May:

- review technical design,
- review prototype boundaries,
- review test-plan feasibility,
- identify implementation risk,
- identify hidden capability expansion.

May not:

- approve legal compliance claims,
- approve security validation alone,
- approve production deployment alone.

Approval rights:

- Technical design review within defined scope.

Review rights:

- Architecture, prototype design, test cases, implementation risk.

Stop rights:

- May stop technical work for unclear scope, missing rollback, or hidden capability.

Audit requirement:

Record technical findings, assumptions, constraints, and unresolved risks.

### ROLE_LEGAL_COMPLIANCE_REVIEWER

Role class: Human legal/compliance role.

Purpose:

Reviews legal, regulatory, GDPR, EU AI Act, data protection, and compliance-related wording or claims.

May:

- review compliance alignment language,
- review lawful basis assumptions,
- review data-processing boundaries,
- review AI Act framing,
- approve or reject compliance-related language.

May not:

- approve technical security claims alone,
- approve implementation safety alone,
- approve cryptographic adequacy alone.

Approval rights:

- Compliance wording and legal-risk framing within reviewer competence.

Review rights:

- Legal/compliance statements, GDPR alignment, EU AI Act alignment, privacy/data protection concerns.

Stop rights:

- May block compliance claims.
- May require legal review before external sharing.

Audit requirement:

Record reviewed claim, scope, limitation, and approval or rejection.

### ROLE_PRIVACY_REVIEWER

Role class: Human privacy role.

Purpose:

Reviews personal data, data minimization, purpose limitation, retention, redaction, and privacy-risk boundaries.

May:

- review personal data handling,
- require minimization,
- require anonymization or redaction,
- review egress involving personal data,
- recommend privacy stop states.

May not:

- approve broader legal compliance alone,
- approve security validation alone,
- approve production use alone.

Approval rights:

- Privacy-specific review within defined scope.

Review rights:

- Personal data, data minimization, retention, redaction, privacy risk.

Stop rights:

- May block personal-data egress or processing when unsupported.

Audit requirement:

Record data category, purpose, minimization basis, and review decision.

### ROLE_AI_GOVERNANCE_REVIEWER

Role class: Human AI governance role.

Purpose:

Reviews AI role boundaries, AI authority limits, human oversight, AI self-escalation risk, and AI-assisted decision behavior.

May:

- review AI role boundaries,
- review AI-generated recommendations,
- identify unsupported AI confidence,
- require human accountability,
- stop AI self-escalation.

May not:

- approve legal compliance claims alone,
- approve technical security validation alone,
- approve production use alone.

Approval rights:

- AI-governance boundary approval within defined scope.

Review rights:

- AI behavior, AI permissions, human oversight, model-risk framing.

Stop rights:

- May trigger AI-governance stop states.

Audit requirement:

Record AI-governance issue, output reviewed, and required boundary.

### ROLE_INCIDENT_REVIEWER

Role class: Human incident role.

Purpose:

Reviews suspected incidents, containment, evidence preservation, recovery, and return-to-normal decisions.

May:

- review incident trigger,
- require freeze,
- require isolation,
- require evidence preservation,
- approve return-to-normal after verification.

May not:

- erase evidence,
- bypass audit,
- approve normal continuation without verification.

Approval rights:

- Incident handling and return-to-normal within defined incident scope.

Review rights:

- Incident state, containment, recovery verification, evidence preservation.

Stop rights:

- May trigger lockdown, freeze, isolation, and incident review.

Audit requirement:

Record incident scope, timeline, evidence, containment, recovery, and closure.

### ROLE_APPROVER

Role class: Human approval role.

Purpose:

Provides scoped approval for a specific action, transition, change, review package, or prototype boundary.

May:

- approve within assigned scope,
- attach conditions,
- set expiration,
- require rollback,
- require additional review.

May not:

- approve outside role scope,
- approve without record,
- approve indefinite blanket authority,
- approve AI self-escalation,
- approve prohibited egress.

Approval rights:

- Only within assigned and recorded scope.

Review rights:

- Scope-dependent.

Stop rights:

- May stop or withdraw approval within scope.

Audit requirement:

Approval record required with scope, time, conditions, and expiration.

### ROLE_EXTERNAL_REVIEWER

Role class: External human reviewer.

Purpose:

Provides independent challenge, critique, and expert review.

May:

- review documentation,
- challenge assumptions,
- identify gaps,
- suggest narrowing,
- reject overclaims,
- recommend next steps.

May not:

- authorize implementation unless separately assigned,
- approve production use,
- become accountable owner by reviewing,
- convert critique into approval automatically.

Approval rights:

- None by default.

Review rights:

- External review only.

Stop rights:

- May recommend stop, pause, narrow, or further review.

Audit requirement:

Record reviewer identity or reviewer category, scope, findings, and limitations.

### ROLE_AI_ASSISTANT

Role class: AI-assisted role.

Purpose:

Assists with analysis, drafting, summarization, classification, gap detection, and safe next-step recommendation.

May:

- summarize material,
- draft documentation,
- classify risks,
- identify missing evidence,
- identify stop states,
- propose next safe documentation steps,
- assist with internal consistency review.

May not:

- approve itself,
- become accountable owner,
- authorize egress,
- authorize capability expansion,
- self-escalate mode,
- make security validation claims,
- make legal compliance claims,
- override human governance.

Approval rights:

- None.

Review rights:

- Assistive review only.

Stop rights:

- May recommend stop states.
- May refuse unsafe continuation.

Audit requirement:

Record AI-assisted output when used for governed decisions.

### ROLE_SYSTEM_PROCESS

Role class: System role.

Purpose:

Represents automated or deterministic system processes in a future prototype.

May:

- apply deterministic decision rules,
- generate audit records,
- enforce stop-state routing,
- classify based on configured policy.

May not:

- create new authority,
- override governance,
- approve high-risk action,
- expand capability,
- hide audit records.

Approval rights:

- None.

Review rights:

- None.

Stop rights:

- May enforce configured stop states.

Audit requirement:

All automated decisions must be auditable.

## Role Authority Matrix

| Role | Review | Approve | Stop | Escalate | Recover |
| --- | --- | --- | --- | --- | --- |
| `ROLE_USER_REQUESTER` | Limited | Low-risk documentation only | Yes | Request only | No |
| `ROLE_SYSTEM_OWNER` | Yes | Scope-dependent | Yes | Yes | Scope-dependent |
| `ROLE_GOVERNANCE_REVIEWER` | Yes | Governance process only | Yes | Recommend | No |
| `ROLE_SECURITY_REVIEWER` | Yes | Security review scope only | Yes | Recommend | Security scope |
| `ROLE_TECHNICAL_REVIEWER` | Yes | Technical review scope only | Yes | Recommend | Technical scope |
| `ROLE_LEGAL_COMPLIANCE_REVIEWER` | Yes | Compliance language only | Yes | Recommend | No |
| `ROLE_PRIVACY_REVIEWER` | Yes | Privacy scope only | Yes | Recommend | No |
| `ROLE_AI_GOVERNANCE_REVIEWER` | Yes | AI-governance scope only | Yes | Recommend | No |
| `ROLE_INCIDENT_REVIEWER` | Yes | Incident/recovery scope only | Yes | Yes | Yes |
| `ROLE_APPROVER` | Scope-dependent | Yes, scoped | Yes | Scope-dependent | Scope-dependent |
| `ROLE_EXTERNAL_REVIEWER` | Yes | No by default | Recommend | Recommend | No |
| `ROLE_AI_ASSISTANT` | Assistive only | No | Recommend/refuse | No | No |
| `ROLE_SYSTEM_PROCESS` | No | No | Enforce configured stops | No | No |

## Separation Of Duties

The model should avoid one actor controlling the whole chain.

Recommended separation:

- Requester should not be sole approver for high-risk action.
- AI should never approve AI-generated recommendations.
- Technical reviewer should not alone approve compliance claims.
- Compliance reviewer should not alone approve technical security claims.
- Security reviewer should not alone approve legal compliance.
- Incident reviewer should verify recovery before return to normal.

## Four-Eyes Principle

High-risk or critical decisions should require at least two appropriate human roles.

Examples:

- Security plus governance review for egress expansion.
- Legal/compliance plus privacy review for personal-data processing.
- Technical plus security review for prototype capability expansion.
- AI governance plus system owner review for AI autonomy changes.

## Role Assignment Record

Every role assignment should record:

```text
Role ID:
Person or system assigned:
Scope:
Authority:
Approval rights:
Review rights:
Stop rights:
Expiration:
Conditions:
Assigned by:
Audit record:
```

## Current Project Role Assignment

Current documentation work should be treated as:

```text
Lifecycle Mode: LM-1_REVIEW_PACKAGE
Operational Decision Mode: ODM-3_APPROVED_DOCUMENTATION_CHANGE
Requester: ROLE_USER_REQUESTER
AI Assistant: ROLE_AI_ASSISTANT
System Owner: not formally assigned in this documentation package
External Reviewers: not yet assigned
```

The user is currently approving targeted review, feedback handling, bounded documentation corrections, and repository-readiness work only.

No production authority, compliance authority, security validation authority, prototype authority, or automation authority is assigned.

## Current Consistency Decision

This Role Registry should be treated as the initial canonical role vocabulary for future review and prototype design.

Future documents should map authority, review, approval, stop, and recovery actions to these roles or a later superseding registry.
