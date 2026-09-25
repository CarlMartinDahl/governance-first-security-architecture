# Governance-First Security Architecture - Roles And Responsibilities v0.1

## Status

Preparatory documentation.

This document is not an implementation.

This document is not an access-control system.

This document is a companion to the Role Registry.

The Role Registry defines what each role may do.

This document defines who may hold each role, under what conditions, and what independence requirements must be met.

## Purpose

The Role Registry defines authority boundaries.

This document answers three questions the Role Registry does not answer:

```text
What competence must a person demonstrate before holding this role?
How many people must occupy each role?
What independence requirements prevent a single person from controlling the whole governance chain?
```

Without answers to these three questions, the role structure is a vocabulary, not a governance control.

A document can define four-eyes principle.

A document cannot create a second person.

This document records the minimum conditions under which the architecture's governance controls are genuine rather than nominal.

## Scope

This document applies to all roles defined in the Role Registry.

This document applies to human roles only.

AI-assisted roles and system roles have no competence or staffing requirements — they are bounded by configuration and governance rules, not by human qualifications.

## Core Principle

```text
A control that depends on a single person is not a control. It is a dependency.
```

Every role with approval or stop authority must be:

- held by a person with demonstrable competence in the role's review domain,
- distinct from the person who produces or requests the work being reviewed,
- independent from the person who holds the approval authority one level up the decision chain.

Where these conditions cannot be met, the architecture must record the gap, escalate to a compensating control, or block the decision until the condition is satisfied.

## Definitions

**Competence** — The ability to evaluate the specific claims, risks, or artifacts that a role is responsible for reviewing or approving. Competence is domain-specific. A person may hold competence in security without holding competence in legal compliance.

**Staffing requirement** — The minimum number of distinct persons who must occupy a role for the associated governance control to function. A staffing requirement of one means the role is assigned. A staffing requirement of two means the role has redundancy.

**Independence requirement** — A constraint on who may not hold a role relative to who holds another role. Independence prevents a single actor from controlling both the work and its review.

**Nominal control** — A governance control that exists in documentation but cannot function because the staffing or independence conditions are not met. A nominal control must be recorded as a gap.

**Compensating control** — An alternative governance measure adopted when a required control cannot be staffed or made independent. A compensating control must be recorded, time-bounded, and reviewed.

## Competence Profiles

### ROLE_SYSTEM_OWNER

Competence required:

- Sufficient understanding of the project scope to evaluate whether documentation milestones accurately reflect the system's intended function and boundaries.
- Sufficient understanding of governance controls to evaluate whether proposed changes affect the scope, risk profile, or review requirements of the project.
- Ability to identify when a scope change requires escalation to additional review roles.

Competence does not require:

- Technical security expertise.
- Legal or compliance expertise.
- AI governance expertise.

Where the System Owner lacks competence to evaluate a specific claim, they must route to the appropriate reviewer rather than approve the claim alone.

### ROLE_GOVERNANCE_REVIEWER

Competence required:

- Demonstrated familiarity with the governance model, lifecycle modes, decision states, and capability gate conditions defined in the architecture.
- Ability to evaluate whether a proposed action is consistent with the current lifecycle mode and decision state.
- Ability to identify missing authority, missing evidence, and unsatisfied stop conditions.

Competence does not require:

- Security expertise.
- Legal expertise.
- AI model expertise.

### ROLE_SECURITY_REVIEWER

Competence required:

- Working knowledge of threat modelling applicable to the system under review.
- Ability to evaluate whether egress controls, secret-handling rules, and incident triggers are adequate for the risk profile of the system.
- Ability to evaluate trigger surface maps, supply chain integrity claims, and capability expansion risk.
- Familiarity with the attack patterns and misuse cases documented in the Abuse Case Library.

Competence does not require:

- Legal or compliance expertise.
- Full AI model expertise.
- Business risk acceptance authority.

For the specific control of trigger surface map adequacy review, the Security Reviewer must be able to independently evaluate whether the map is complete, not merely whether it is present.

### ROLE_TECHNICAL_REVIEWER

Competence required:

- Ability to evaluate the technical feasibility of the system design within the stated boundaries.
- Ability to identify hidden capability expansion in prototype or implementation proposals.
- Ability to evaluate whether test plans are sufficient to validate the claimed boundaries.
- Sufficient familiarity with the relevant technology stack to assess implementation risk.

### ROLE_LEGAL_COMPLIANCE_REVIEWER

Competence required:

- Working knowledge of GDPR applicable to the data categories the system processes.
- Working knowledge of EU AI Act classification criteria sufficient to evaluate whether the system's classification claim is supportable.
- Ability to evaluate compliance-related wording for overclaim.

Competence does not require:

- Technical security expertise.
- AI model expertise.

### ROLE_PRIVACY_REVIEWER

Competence required:

- Ability to evaluate whether personal data is being processed with an adequate lawful basis and purpose limitation.
- Ability to evaluate data minimization and retention claims.
- Working knowledge of data subject rights applicable to the system.

### ROLE_AI_GOVERNANCE_REVIEWER

Competence required:

- Ability to evaluate whether AI role boundaries are appropriately constrained.
- Ability to identify AI self-escalation risk in proposed system designs.
- Sufficient understanding of the AI model's capabilities and limitations to evaluate whether human oversight is adequate.
- Ability to evaluate whether AI-generated recommendations are used as inputs to human decisions rather than as approvals.

### ROLE_INCIDENT_REVIEWER

Competence required:

- Ability to evaluate whether an incident trigger meets the threshold defined in the Active Neutralization Runbook.
- Ability to direct containment, isolation, and evidence preservation actions.
- Ability to verify that recovery actions have resolved the trigger condition before approving return to normal.

### ROLE_APPROVER

Competence required:

- Competence is scoped to the specific approval assignment.
- An Approver assigned to approve a security review decision must hold or have access to ROLE_SECURITY_REVIEWER competence.
- An Approver assigned to approve a compliance claim must hold or have access to ROLE_LEGAL_COMPLIANCE_REVIEWER competence.
- A general Approver without domain competence may approve only procedural completeness — not substantive correctness.

### ROLE_EXTERNAL_REVIEWER

Competence required:

- Domain-appropriate expertise relative to the scope of the review assignment.
- Independence from the organization producing the work being reviewed.
- Absence of financial, organizational, or personal interest that would compromise the independence of the review.

## Staffing Requirements

Staffing requirements state the minimum number of distinct persons who must hold a role for the associated governance control to be operational.

| Role | Minimum persons | Redundancy recommendation |
| --- | --- | --- |
| `ROLE_SYSTEM_OWNER` | 1 | 1 named alternate for continuity |
| `ROLE_GOVERNANCE_REVIEWER` | 1 | 2 for high-risk decisions |
| `ROLE_SECURITY_REVIEWER` | 1 | 2 when trigger surface map review is required |
| `ROLE_TECHNICAL_REVIEWER` | 1 | 2 for prototype capability expansion decisions |
| `ROLE_LEGAL_COMPLIANCE_REVIEWER` | 1 | External reviewer acceptable as redundancy |
| `ROLE_PRIVACY_REVIEWER` | 1 | May be combined with ROLE_LEGAL_COMPLIANCE_REVIEWER if competence is held |
| `ROLE_AI_GOVERNANCE_REVIEWER` | 1 | Required distinct from ROLE_SECURITY_REVIEWER |
| `ROLE_INCIDENT_REVIEWER` | 1 active + 1 escalation path | Escalation path must not be blocked by the incident |
| `ROLE_APPROVER` | 1 per approval event | Must be distinct from the requester |
| `ROLE_EXTERNAL_REVIEWER` | 1 per external review event | Must be organizationally independent |

Where a staffing minimum is not met, the affected governance control is nominal.

Nominal controls must be recorded in the gap register and a compensating control must be defined before the associated decision proceeds.

## Independence Requirements

Independence requirements state which role pairings must not be held by the same person for the governance control to be genuine.

### Absolute independence requirements

These pairings must never be held by the same person. No compensating control is sufficient.

| Role A | Role B | Rationale |
| --- | --- | --- |
| Designer of trigger surface map | Security Reviewer approving that map | Self-review is not review |
| `ROLE_USER_REQUESTER` for a decision | `ROLE_APPROVER` for that same decision | Self-approval is not approval |
| `ROLE_AI_ASSISTANT` | Any human approval role | AI may not approve AI-generated output |

### Strong independence requirements

These pairings should not be held by the same person. A documented compensating control is required if they are.

| Role A | Role B | Rationale | Compensating control if combined |
| --- | --- | --- | --- |
| `ROLE_SYSTEM_OWNER` | `ROLE_GOVERNANCE_REVIEWER` | Owner reviewing own scope | External governance review required |
| `ROLE_SECURITY_REVIEWER` | `ROLE_APPROVER` for the same security decision | Reviewer approving own review | Second security reviewer required |
| `ROLE_TECHNICAL_REVIEWER` | `ROLE_APPROVER` for the same technical decision | Reviewer approving own review | External technical reviewer required |
| `ROLE_LEGAL_COMPLIANCE_REVIEWER` | `ROLE_SYSTEM_OWNER` | Compliance reviewer owning the system | External legal review required before compliance claims are published |
| `ROLE_INCIDENT_REVIEWER` | Any role implicated in the incident | Conflict of interest | Independent escalation path must be available |

### Governance chain independence

The governance chain for any high-risk decision must not be controlled by a single person at more than one sequential step.

A high-risk decision is one that:

- changes the trigger surface map,
- expands AI agent capability,
- approves a supply chain update to the model or prompt layer,
- approves external sharing of security-sensitive documentation, or
- approves return to normal after an incident.

For high-risk decisions, the following sequential steps must each be held by distinct persons:

1. Requester.
2. Reviewer (domain-appropriate).
3. Approver.

If steps 2 and 3 must be combined due to staffing constraints, a time-bounded compensating control must be recorded and an independent escalation path must exist.

## Role Assignment Record Requirements

Every active role assignment must be recorded using the template defined in the Role Registry.

In addition to that template, this document requires the following fields for all roles with approval or stop authority:

```text
Role ID:
Person assigned:
Competence basis: [What makes this person competent to hold this role]
Independence check: [Which independence requirements were verified and how]
Staffing gap: [Yes / No — if Yes, compensating control must be named]
Compensating control: [If applicable]
Compensating control expiration: [Date or event]
Assigned by:
Review date:
```

## Gap Handling

Where a staffing minimum or independence requirement cannot be met, the following procedure applies:

1. Record the gap in the gap register with role affected, requirement unmet, and date identified.
2. Define a compensating control. A compensating control may include external review, increased audit frequency, or a temporary decision freeze for the affected control area.
3. Set an expiration date for the compensating control. A compensating control may not be treated as a permanent resolution.
4. Assign a named person responsible for resolving the gap.
5. Do not allow the affected governance control to be treated as satisfied while the gap is open.

A gap register entry for a staffing or independence gap is not a finding that the architecture has failed. It is evidence that the architecture is operating honestly about its own conditions.

## Relationship To Other Documents

| Document | Relationship |
| --- | --- |
| Role Registry v0.1 | This document extends the Role Registry with competence, staffing, and independence requirements. The Role Registry defines what roles may do. This document defines who may hold them. |
| Red Team Findings v0.2 | Gap S (sign-off authority concentration) identified the absence of the independence requirements now defined in this document. |
| Capability Change Gate v0.1 | High-risk capability changes require role assignments that satisfy the independence requirements in this document. |
| Active Neutralization Runbook v0.1 | Incident Reviewer assignments must satisfy the staffing and independence requirements in this document. |
| AI Model And Supply Chain Integrity v0.1 | Supply chain update approvals are high-risk decisions subject to governance chain independence requirements. |
| GDPR EU AI Act Alignment v0.1 | Legal and Privacy Reviewer assignments must satisfy the competence profiles in this document. |

## Current Project State

At time of writing, the following role assignments are active for this documentation project:

```text
Lifecycle Mode: LM-1_REVIEW_PACKAGE
Operational Decision Mode: ODM-3_APPROVED_DOCUMENTATION_CHANGE
Requester: ROLE_USER_REQUESTER — project owner
AI Assistant: ROLE_AI_ASSISTANT — documentation and analysis only
System Owner: not formally assigned
Security Reviewer: not formally assigned
Governance Reviewer: not formally assigned
External Reviewers: not yet assigned
```

All governance controls that require a named human role beyond ROLE_USER_REQUESTER and ROLE_AI_ASSISTANT are currently nominal.

This is expected at the current lifecycle stage.

This document should be populated with formal role assignments before the project transitions to prototype design, external review, or any production-adjacent activity.
