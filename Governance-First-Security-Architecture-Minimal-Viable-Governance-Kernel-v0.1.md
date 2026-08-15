# Governance-First Security Architecture - Minimal Viable Governance Kernel v0.1

## Status

Preparatory documentation.

This document is not an implementation.

This document is not a production security design.

This document defines the smallest coherent governance kernel that would need to exist before the Governance-First Security Architecture could later be discussed as a prototype.

## Purpose

The purpose of the Minimal Viable Governance Kernel is to answer one question:

```text
What is the smallest set of rules, states, decisions, records, and gates required for the model to remain governance-first?
```

If this kernel is missing, the system risks becoming ordinary automation with governance language attached after the fact.

## Kernel Boundary

The kernel must not try to solve everything.

It should only define:

- What the system is allowed to know.
- What the system is allowed to do.
- What the system is not allowed to do.
- When the system must stop.
- Who or what can approve continuation.
- What evidence is required.
- What may leave the system.
- What must be recorded.
- What changes require new approval.

Everything else belongs outside the minimal kernel.

## Kernel Principle

The kernel is governed by this rule:

```text
No governed action without authority, evidence, mode, egress classification, audit record, and stop path.
```

In Swedish:

```text
Ingen styrd atgard utan behorighet, underlag, lage, utflodesklassning, granskningsspar och stoppvag.
```

## Required Kernel Components

### K-001 - Mode State

The system must always know which mode it is operating in.

Minimum modes:

- `READ_ONLY`
- `PLAN_ONLY`
- `REVIEW_ONLY`
- `APPROVED_ACTION`
- `LOCKDOWN`
- `INCIDENT`

Mode rules:

- Read-only mode may inspect but not change.
- Plan-only mode may propose but not execute.
- Review-only mode may evaluate but not approve itself.
- Approved-action mode requires explicit authority.
- Lockdown mode blocks non-essential continuation.
- Incident mode prioritizes containment, audit, and recovery.

### K-002 - Action Class

Every requested action must be classified before it is allowed.

Minimum action classes:

- `OBSERVE`
- `ANALYZE`
- `DOCUMENT`
- `RECOMMEND`
- `CHANGE`
- `EXPORT`
- `EXECUTE`
- `ESCALATE`
- `OVERRIDE`
- `RECOVER`

The system must not treat all actions as equal.

An observation is not an export.

A recommendation is not approval.

A document is not authority.

### K-003 - Risk Level

Every action must receive a risk level.

Minimum risk levels:

- `LOW`
- `MEDIUM`
- `HIGH`
- `CRITICAL`

Risk must consider:

- Data sensitivity.
- Action reversibility.
- External impact.
- Human impact.
- Financial impact.
- Legal or compliance impact.
- Security impact.
- AI autonomy level.
- Egress exposure.

### K-004 - Authority Check

The system must verify that the actor has authority for the requested action.

Minimum authority outcomes:

- `AUTHORIZED`
- `NOT_AUTHORIZED`
- `AUTHORITY_UNKNOWN`
- `AUTHORITY_EXPIRED`
- `AUTHORITY_CONFLICT`

If authority is missing, unknown, expired, or conflicting, the kernel must stop.

### K-005 - Evidence Check

The system must verify whether the action has enough evidence.

Minimum evidence outcomes:

- `EVIDENCE_SUFFICIENT`
- `EVIDENCE_INSUFFICIENT`
- `SOURCE_MISSING`
- `SOURCE_STALE`
- `SOURCE_CONFLICT`
- `SOURCE_UNTRUSTED`

The kernel must prevent unsupported conclusions from becoming approved actions.

### K-006 - Egress Classification

Every output, export, tool call, integration call, or external transmission must be classified before it leaves the system.

Minimum egress classes:

- `NO_EGRESS`
- `PUBLIC_SAFE`
- `INTERNAL_ONLY`
- `SENSITIVE`
- `SECRET`
- `REGULATED`
- `BLOCKED`

The system must treat egress as a first-class security boundary.

Internal access does not imply export permission.

### K-007 - Stop State

The kernel must be able to stop continuation.

Minimum stop states:

- `STOP_AUTHORITY_MISSING`
- `STOP_EVIDENCE_INSUFFICIENT`
- `STOP_MODE_BOUNDARY`
- `STOP_EGRESS_UNAUTHORIZED`
- `STOP_CAPABILITY_CHANGE`
- `STOP_AUDIT_RECORD_MISSING`
- `STOP_AI_AUTHORITY_EXCEEDED`
- `STOP_HUMAN_REVIEW_REQUIRED`
- `STOP_CONFLICT`
- `STOP_UNKNOWN`

A stop state must be treated as a valid system outcome, not a failure of productivity.

### K-008 - Review State

The kernel must distinguish stop, review, and approval.

Minimum review states:

- `NO_REVIEW_REQUIRED`
- `HUMAN_REVIEW_REQUIRED`
- `SECURITY_REVIEW_REQUIRED`
- `LEGAL_REVIEW_REQUIRED`
- `COMPLIANCE_REVIEW_REQUIRED`
- `TECHNICAL_REVIEW_REQUIRED`
- `EXTERNAL_REVIEW_REQUIRED`

Review is not approval unless explicitly recorded as approval by an authorized reviewer.

### K-009 - Approval Record

The kernel must record approval before high-risk continuation.

Minimum approval record fields:

```text
Approval ID:
Approver:
Approver role:
Scope:
Action class:
Risk level:
Mode:
Evidence basis:
Egress class:
Time:
Expiration:
Rollback requirement:
Conditions:
```

Approval must be scoped.

Blanket approval should not exist in the minimal kernel.

### K-010 - Audit Record

The kernel must create an audit record for governed actions.

Minimum audit record fields:

```text
Event ID:
Timestamp:
Actor:
Actor type:
Mode:
Requested action:
Action class:
Risk level:
Authority result:
Evidence result:
Egress class:
Decision:
Stop state:
Reviewer:
Approval ID:
Output allowed:
Rollback path:
Notes:
```

No audit record, no high-risk action.

### K-011 - Capability Change Gate

The kernel must detect when the system is about to gain new capability.

Capability change includes:

- New tool access.
- New automation.
- New external integration.
- New data source.
- New write access.
- New export path.
- New execution path.
- New AI autonomy.
- New decision authority.
- New recovery or rollback power.

Minimum decision:

```text
If capability changes, stop and review before use.
```

### K-012 - AI Authority Boundary

The kernel must define what AI may and may not do.

Minimum AI permissions:

- AI may observe provided material.
- AI may classify risk.
- AI may identify missing evidence.
- AI may recommend next review steps.
- AI may draft documentation.
- AI may propose stop states.

Minimum AI prohibitions:

- AI may not approve itself.
- AI may not self-escalate mode.
- AI may not override governance.
- AI may not treat its own confidence as evidence.
- AI may not authorize egress.
- AI may not create new capability without gate review.

### K-013 - Human Override Boundary

The kernel must allow human override only as a controlled event.

Minimum override requirements:

- Named human.
- Role.
- Reason.
- Scope.
- Time limit.
- Risk acceptance.
- Audit record.
- Rollback plan.
- Post-override review.

Human override without record is not governance.

### K-014 - Decision Output

Every governed evaluation must end in one of a small number of decisions.

Minimum decision outputs:

- `ALLOW`
- `ALLOW_WITH_CONDITIONS`
- `REVIEW_REQUIRED`
- `BLOCK`
- `QUARANTINE`
- `LOCKDOWN`
- `INCIDENT_RESPONSE`
- `NEEDS_MORE_EVIDENCE`
- `NEEDS_AUTHORITY`
- `NEEDS_CAPABILITY_REVIEW`

The system must not continue with vague decisions.

### K-015 - Rollback Or Recovery Path

The kernel must know whether an action can be reversed.

Minimum rollback status:

- `REVERSIBLE`
- `PARTIALLY_REVERSIBLE`
- `IRREVERSIBLE`
- `ROLLBACK_UNKNOWN`
- `RECOVERY_REQUIRED`

High-risk irreversible action requires stricter review.

If rollback is unknown, the system should treat the action as higher risk.

## Minimal Kernel Decision Flow

```text
1. Identify mode.
2. Classify requested action.
3. Assign risk level.
4. Check authority.
5. Check evidence.
6. Classify egress.
7. Check capability change.
8. Check AI-human boundary.
9. Check rollback or recovery path.
10. Create audit record.
11. Decide: allow, condition, review, block, quarantine, lockdown, or incident.
```

If any required check cannot be completed, the default outcome is:

```text
REVIEW_REQUIRED or BLOCK
```

not silent continuation.

## Minimal Kernel Table

| Kernel Area | Required? | Default If Missing |
| --- | --- | --- |
| Mode | Yes | Stop |
| Action class | Yes | Stop |
| Risk level | Yes | Review |
| Authority | Yes | Stop |
| Evidence | Yes | Stop or review |
| Egress class | Yes | Block egress |
| Stop state | Yes | Stop unknown |
| Review state | Yes | Human review |
| Approval record | For high risk | No approval |
| Audit record | Yes | Stop |
| Capability gate | Yes | Stop |
| AI boundary | Yes | Stop |
| Human override boundary | Yes | Stop |
| Decision output | Yes | Review |
| Rollback path | For change/execute/recover | Review or block |

## Kernel Non-Goals

The minimal kernel does not define:

- Full user interface.
- Full implementation architecture.
- Full legal compliance.
- Full cybersecurity controls.
- Encryption standards.
- Vendor selection.
- Runtime orchestration.
- Production monitoring.
- Commercial packaging.
- Performance targets.
- Penetration testing process.

Those may be defined later.

The kernel only defines the minimum governance logic.

## Prototype Readiness Criteria

The model may be ready for a later prototype design discussion only when the kernel can answer:

- What mode are we in?
- What action is requested?
- What risk level applies?
- Who has authority?
- What evidence supports the action?
- What may leave the system?
- Is capability changing?
- Is AI staying inside its role?
- Is human approval real and scoped?
- Is there a rollback or recovery path?
- What is the audit record?
- What is the final decision?

If these cannot be answered, the model is not ready for prototype design.

## Current Conclusion

The Minimal Viable Governance Kernel is the control heart of the Governance-First Security Architecture.

It is intentionally small.

Its purpose is not to make the system powerful.

Its purpose is to prevent power from appearing before governance exists.

The kernel should be treated as the first non-negotiable layer before any future runtime, automation, AI-agent behavior, integration, or security claim.
