# Governance-First Security Architecture

## Capability Change Gate v0.1

## Status

This document is a preparatory capability-change policy for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a production authorization model.

It is not a security claim.

It is intended to define what counts as new system capability and what governance is required before capability expansion.

## Purpose

The purpose of this document is to answer:

```text
What counts as new capability?
When does capability expansion create risk?
Who can approve it?
What evidence is required?
When must capability change be blocked?
```

## Core Principle

Capability determines impact.

Small technical changes can create large risk if they allow the system, AI, user, or integration to do something it could not do before.

Core rules:

```text
No capability change without gate.
No analysis-to-execution drift without approval.
No read-only-to-write transition without exact scope.
No internal-to-export transition without egress review.
No AI autonomy increase without containment review.
```

## Capability Change Definition

A capability change occurs when the system gains, enables, expands, automates, or exposes any ability that changes what it can do, reach, affect, export, decide, or execute.

Capability change may be explicit or hidden.

Examples:

- adding a tool
- enabling write access
- enabling network access
- enabling export
- enabling automation
- enabling memory
- enabling external API use
- increasing AI autonomy
- adding integration
- changing mode
- expanding role permissions
- turning recommendation into decision
- turning decision into execution

## Capability Change Classes

### CAPABILITY_CLASS_0: No Capability Change

Description:

The action does not expand what the system can do.

Examples:

- documentation-only clarification
- read-only status check
- non-authorizing review
- static analysis without export

Default treatment:

```text
Allowed if scope, source, and mode are valid.
```

### CAPABILITY_CLASS_1: Documentation Capability

Description:

The system adds documentation that may influence future governance but does not change runtime behavior.

Examples:

- charter
- policy draft
- review document
- threat model
- taxonomy

Risk:

```text
LOW_TO_MEDIUM
```

Required controls:

- non-authorization label
- no runtime claim
- no implementation claim
- no hidden approval

Default treatment:

```text
Documentation is not authorization.
```

### CAPABILITY_CLASS_2: State Or Write Capability

Description:

The system gains ability to write, modify, delete, commit, or change state.

Examples:

- write file
- update configuration
- modify policy
- create commit
- change metadata
- alter workflow

Risk:

```text
MEDIUM_TO_HIGH
```

Required controls:

- exact scope approval
- pre/post verification
- rollback where applicable
- audit trail

Default treatment:

```text
Read-only is not write permission.
```

### CAPABILITY_CLASS_3: Data Access Expansion

Description:

The system gains access to new data, more sensitive data, broader datasets, logs, personal data, secrets, or restricted material.

Risk:

```text
HIGH
```

Required controls:

- asset classification
- purpose validation
- lawful basis where relevant
- access authority
- audit
- egress review

Default treatment:

```text
New data access requires asset and purpose review.
```

### CAPABILITY_CLASS_4: Egress Capability

Description:

The system gains ability to export, share, publish, transmit, push, copy, or externally expose information.

Risk:

```text
HIGH_TO_CRITICAL
```

Required controls:

- egress classification
- destination validation
- purpose validation
- secret detection
- approval
- audit

Default treatment:

```text
Internal access is not export permission.
```

### CAPABILITY_CLASS_5: Tool Or Integration Capability

Description:

The system gains access to external tools, APIs, plugins, connectors, automation, cloud services, identity providers, or third-party systems.

Risk:

```text
HIGH
```

Required controls:

- integration review
- data-flow mapping
- permission minimization
- egress review
- vendor/security review where relevant
- audit

Default treatment:

```text
No external integration without data-flow review.
```

### CAPABILITY_CLASS_6: Network Capability

Description:

The system gains ability to communicate with external networks or remote systems.

Risk:

```text
HIGH
```

Required controls:

- destination restrictions
- egress policy
- logging
- purpose review
- abuse review
- rollback/disable path

Default treatment:

```text
Local-only is not network-enabled.
```

### CAPABILITY_CLASS_7: Execution Capability

Description:

The system gains ability to perform operations with real-world, production, financial, legal, operational, or security impact.

Risk:

```text
CRITICAL
```

Required controls:

- explicit execution approval
- mode authorization
- rollback plan
- human accountability
- audit
- incident fallback

Default treatment:

```text
Analysis is not execution.
```

### CAPABILITY_CLASS_8: AI Autonomy Capability

Description:

AI gains more autonomy, memory, tool choice, planning, delegation, background operation, or ability to continue without explicit human direction.

Risk:

```text
HIGH_TO_CRITICAL
```

Required controls:

- autonomy review
- containment review
- tool boundary review
- objective clarity
- stop condition
- human supervision
- audit

Default treatment:

```text
No advanced AI autonomy without containment.
```

### CAPABILITY_CLASS_9: Mode Advancement

Description:

The system moves to a higher operating mode.

Examples:

- read-only to sandbox
- sandbox to controlled test
- controlled test to limited deployment
- limited deployment to production

Risk:

```text
HIGH_TO_CRITICAL
```

Required controls:

- mode advancement review
- evidence package
- test evidence
- approval
- rollback
- audit

Default treatment:

```text
No mode advancement without explicit gate.
```

## Hidden Capability Change

Some changes may appear harmless but still expand capability.

Examples:

- adding a script that can later execute
- adding network dependency
- adding workflow automation
- adding export format
- adding broad file access
- adding memory persistence
- adding permission to read logs
- changing policy wording from "may review" to "may approve"

Default rule:

```text
Hidden capability change is still capability change.
```

## Capability Change Gate Requirements

Before capability expansion, the system should require:

- capability class
- current capability
- proposed new capability
- affected assets
- affected trust boundaries
- affected modes
- risk level
- evidence basis
- approval authority
- rollback or disable path
- audit event
- test requirement
- egress impact review
- compliance impact review where relevant

## Capability Change Decision States

Initial decision states:

```text
CAPABILITY_NO_CHANGE
CAPABILITY_CHANGE_PROPOSED
CAPABILITY_CHANGE_REVIEW_REQUIRED
CAPABILITY_CHANGE_APPROVED_FOR_TEST
CAPABILITY_CHANGE_APPROVED_FOR_LIMITED_USE
CAPABILITY_CHANGE_BLOCKED
CAPABILITY_CHANGE_REJECTED
CAPABILITY_CHANGE_REVOKED
```

## Capability Change By Normalized Mode

The Mode Model Normalization document is authoritative. Lifecycle Mode and Operational Decision Mode must be evaluated separately.

### Current Review-Package Boundary

At `LM-1_REVIEW_PACKAGE` with `ODM-3_APPROVED_DOCUMENTATION_CHANGE`, bounded documentation corrections may proceed when approved. Capability change, prototype action, runtime behavior, automation, integration, and live-data use remain blocked.

### Future Synthetic Prototype Modes

`LM-3_LIMITED_SYNTHETIC_PROTOTYPE` or `ODM-5_SYNTHETIC_TEST`, if separately approved in the future, may allow isolated mock actions and synthetic data. They do not authorize real secrets, live integrations, sensitive export, or production effects.

### Future Validated Research Mode

`LM-4_VALIDATED_RESEARCH_PROTOTYPE`, if separately approved in the future, may allow a reviewed non-production prototype within an explicit scope. Rollback, audit, evidence, capability, and egress gates would still apply.

### Controlled Pilot And Production Modes

`LM-5_CONTROLLED_PILOT` and `LM-6_PRODUCTION` are out of current scope. This document does not define sufficient approval, validation, security, compliance, operational ownership, incident response, or recovery conditions for either mode.

## Hard Blocks

Capability change should be blocked when:

- capability class is unknown
- authority is missing
- approval is missing
- affected assets are unknown
- egress impact is unknown
- rollback is missing for irreversible capability
- AI autonomy increases without containment
- execution is requested in read-only mode
- secret access is added without security review
- network access is added without data-flow review
- mode advancement lacks evidence

## AI-Specific Capability Rules

AI must not gain:

- unrestricted tool access
- unrestricted file access
- unrestricted network access
- ability to export sensitive content
- ability to approve its own actions
- ability to change its own governing policy
- ability to self-advance mode
- ability to hide uncertainty or counter-evidence

Default rule:

```text
AI capability expansion requires containment and human accountability.
```

## Human-Specific Capability Rules

Humans may request capability expansion, but request is not approval.

High-risk capability expansion requires:

- valid authority
- documented reason
- risk review
- evidence
- audit
- rollback
- possibly second approval

Default rule:

```text
Human request is not capability approval.
```

## Capability Change Examples

### Example 1: Add documentation file

Capability class:

```text
Documentation Capability
```

Default governance:

```text
Non-authorization label and scope check.
```

### Example 2: Add script but do not run it

Capability class:

```text
State Or Write Capability
Potential future Execution Capability
```

Default governance:

```text
Review for hidden capability change.
```

### Example 3: Enable API connector

Capability class:

```text
Tool Or Integration Capability
Network Capability
Potential Egress Capability
```

Default governance:

```text
Integration, data-flow, egress, and permission review.
```

### Example 4: Let AI run background tasks

Capability class:

```text
AI Autonomy Capability
```

Default governance:

```text
Containment, stop condition, tool boundary, and audit review.
```

### Example 5: Move from sandbox to limited deployment

Capability class:

```text
Mode Advancement
```

Default governance:

```text
Evidence package, approval, rollback, monitoring.
```

## Initial Capability Change Matrix

| Capability Change | Default Risk | Required Gate |
|---|---|---|
| Documentation only | Low to Medium | Non-authorization scope check |
| Write/state change | Medium to High | Exact scope approval |
| Data access expansion | High | Asset and purpose review |
| Export capability | High to Critical | Egress gate |
| Tool/integration access | High | Integration review |
| Network access | High | Data-flow and egress review |
| Execution capability | Critical | Execution gate |
| AI autonomy increase | High to Critical | Containment review |
| Mode advancement | High to Critical | Mode gate |

## Open Questions

1. Which capability classes are needed for version 0?
2. Which capability changes must always be blocked early?
3. Which capability changes can be tested safely in sandbox?
4. How should hidden capability change be detected?
5. How should AI tool access be scoped?
6. What counts as AI autonomy increase?
7. Which capability changes require external review?
8. Which capability changes require compliance review?
9. How should rollback be proven?
10. How should capability revocation work?
