# Governance-First Security Architecture - Decision-State Matrix v0.1

## Status

Preparatory documentation.

This document is not an implementation.

This document is not an authorization engine.

This document defines an initial decision-state matrix for mapping modes, action classes, risk levels, authority outcomes, evidence outcomes, egress classes, and stop states to final governance decisions.

## Purpose

The purpose of the Decision-State Matrix is to make decisions predictable.

The model should not decide by instinct, confidence, pressure, or convenience.

It should decide by governed inputs.

This matrix answers:

```text
Given this mode, action, risk, authority, evidence, egress class, and stop state, what is the safest allowed decision?
```

## Core Principle

```text
The most restrictive valid signal wins.
```

If one signal says continue and another valid signal says stop, review, lockdown, or incident, the more restrictive signal controls.

## Decision Outputs

The canonical decision outputs are:

- `ALLOW`
- `ALLOW_WITH_CONDITIONS`
- `NEEDS_MORE_EVIDENCE`
- `NEEDS_AUTHORITY`
- `REVIEW_REQUIRED`
- `NEEDS_CAPABILITY_REVIEW`
- `BLOCK`
- `QUARANTINE`
- `LOCKDOWN`
- `INCIDENT_RESPONSE`

## Decision Output Definitions

### ALLOW

The action may proceed within the current scope.

Allowed only when:

- mode permits the action,
- action risk is acceptable,
- authority is valid,
- evidence is sufficient,
- egress is allowed,
- no capability change is present,
- no stop state is triggered,
- audit requirement is satisfied.

### ALLOW_WITH_CONDITIONS

The action may proceed only under explicit limits.

Examples:

- redacted output only,
- read-only continuation only,
- limited documentation change only,
- synthetic-data-only test only,
- no external egress,
- named reviewer must review before next step.

### NEEDS_MORE_EVIDENCE

The system lacks sufficient evidence.

The system may not make a stronger conclusion or perform a higher-risk action until evidence improves.

### NEEDS_AUTHORITY

The system lacks valid authority.

The action may not continue until the correct authority is identified, current, scoped, and recorded.

### REVIEW_REQUIRED

The system may not continue without human or domain review.

Review does not automatically mean approval.

### NEEDS_CAPABILITY_REVIEW

The requested action may add or expose new capability.

Capability review must happen before use.

### BLOCK

The action is not allowed in the current conditions.

The system may explain why it blocked, but must not perform the blocked action.

### QUARANTINE

The input, output, source, session, data, tool result, or artifact should be isolated from normal processing.

### LOCKDOWN

The system must restrict broader continuation and preserve evidence.

Lockdown is used when local blocking is not enough.

### INCIDENT_RESPONSE

The situation may involve a security, compliance, data, AI-governance, capability, or recovery incident.

Incident handling and evidence preservation take priority over normal continuation.

## Input Dimensions

The matrix uses these inputs:

- Lifecycle Mode.
- Operational Decision Mode.
- Action Class.
- Risk Level.
- Authority Outcome.
- Evidence Outcome.
- Egress Class.
- Capability Change Outcome.
- AI-Human Boundary Outcome.
- Audit Outcome.
- Rollback Outcome.
- Stop State.

## Priority Rule

Decision priority should be evaluated in this order:

```text
1. Incident state.
2. Lockdown state.
3. Prohibited egress.
4. Missing authority.
5. Mode boundary violation.
6. Capability change.
7. Audit/accountability failure.
8. Evidence insufficiency.
9. AI-human boundary issue.
10. Rollback/recovery issue.
11. Risk-level review requirement.
12. Conditional allow.
13. Allow.
```

The priority order prevents a low-risk or convenient signal from overriding a hard stop.

## Lifecycle Mode Decision Matrix

| Lifecycle Mode | Default Decision Boundary |
| --- | --- |
| `LM-0_DOCUMENTATION_ONLY` | Documentation-only actions may be allowed; runtime, automation, integration, production, and real data actions block |
| `LM-1_REVIEW_PACKAGE` | External review, feedback handling, and bounded review-package corrections may be allowed; build and prototype actions block |
| `LM-2_PROTOTYPE_DESIGN` | Prototype design may be allowed; prototype execution blocks |
| `LM-3_LIMITED_SYNTHETIC_PROTOTYPE` | Synthetic local prototype actions may be allowed if approved; real data and integrations block |
| `LM-4_VALIDATED_RESEARCH_PROTOTYPE` | Reviewed non-production prototype actions may be allowed with conditions |
| `LM-5_CONTROLLED_PILOT` | Out of current scope; review required |
| `LM-6_PRODUCTION` | Out of current scope; block |

Current project lifecycle mode:

```text
LM-1_REVIEW_PACKAGE
```

## Operational Decision Mode Matrix

| Operational Decision Mode | Observe | Plan | Review | Document | Change Docs | Prototype Design | Prototype Action | Runtime/Production |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `ODM-0_READ_ONLY` | ALLOW | ALLOW_WITH_CONDITIONS | ALLOW_WITH_CONDITIONS | BLOCK | BLOCK | BLOCK | BLOCK | BLOCK |
| `ODM-1_PLAN_ONLY` | ALLOW | ALLOW | REVIEW_REQUIRED | ALLOW_WITH_CONDITIONS | BLOCK | BLOCK | BLOCK | BLOCK |
| `ODM-2_REVIEW_ONLY` | ALLOW | ALLOW_WITH_CONDITIONS | ALLOW | ALLOW_WITH_CONDITIONS | BLOCK | BLOCK | BLOCK | BLOCK |
| `ODM-3_APPROVED_DOCUMENTATION_CHANGE` | ALLOW | ALLOW | ALLOW | ALLOW | ALLOW_WITH_CONDITIONS | BLOCK | BLOCK | BLOCK |
| `ODM-4_APPROVED_PROTOTYPE_DESIGN` | ALLOW | ALLOW | ALLOW | ALLOW | ALLOW_WITH_CONDITIONS | ALLOW_WITH_CONDITIONS | BLOCK | BLOCK |
| `ODM-5_APPROVED_SYNTHETIC_PROTOTYPE_ACTION` | ALLOW | ALLOW | ALLOW | ALLOW | ALLOW_WITH_CONDITIONS | ALLOW_WITH_CONDITIONS | ALLOW_WITH_CONDITIONS | BLOCK |
| `ODM-6_LOCKDOWN` | ALLOW_WITH_CONDITIONS | REVIEW_REQUIRED | REVIEW_REQUIRED | REVIEW_REQUIRED | BLOCK | BLOCK | BLOCK | BLOCK |
| `ODM-7_INCIDENT` | ALLOW_WITH_CONDITIONS | REVIEW_REQUIRED | REVIEW_REQUIRED | REVIEW_REQUIRED | BLOCK | BLOCK | BLOCK | BLOCK |

## Action Class Decision Matrix

| Action Class | Default Decision |
| --- | --- |
| `OBSERVE` | ALLOW if data is permitted and mode allows |
| `ANALYZE` | ALLOW or ALLOW_WITH_CONDITIONS depending on evidence and risk |
| `DOCUMENT` | ALLOW_WITH_CONDITIONS if documentation-only scope is approved |
| `RECOMMEND` | ALLOW_WITH_CONDITIONS; recommendation is not approval |
| `CHANGE` | REVIEW_REQUIRED or BLOCK unless explicitly approved |
| `EXPORT` | BLOCK unless egress is classified and authorized |
| `EXECUTE` | BLOCK unless explicitly approved in a suitable lifecycle mode |
| `ESCALATE` | REVIEW_REQUIRED or BLOCK unless mode transition is approved |
| `OVERRIDE` | REVIEW_REQUIRED; must be scoped, recorded, and time-limited |
| `RECOVER` | REVIEW_REQUIRED unless incident/recovery plan approves action |

## Risk Level Decision Matrix

| Risk Level | Default Decision |
| --- | --- |
| `LOW` | ALLOW or ALLOW_WITH_CONDITIONS if all checks pass |
| `MEDIUM` | ALLOW_WITH_CONDITIONS or REVIEW_REQUIRED |
| `HIGH` | REVIEW_REQUIRED by default |
| `CRITICAL` | BLOCK, LOCKDOWN, or INCIDENT_RESPONSE unless formal review approves bounded continuation |

Risk can only increase from additional signals.

Risk should not be downgraded by AI confidence.

## Authority Outcome Decision Matrix

| Authority Outcome | Decision |
| --- | --- |
| `AUTHORIZED` | Continue to evidence, egress, and risk checks |
| `NOT_AUTHORIZED` | NEEDS_AUTHORITY or BLOCK |
| `AUTHORITY_UNKNOWN` | NEEDS_AUTHORITY |
| `AUTHORITY_EXPIRED` | NEEDS_AUTHORITY |
| `AUTHORITY_CONFLICT` | REVIEW_REQUIRED |

Authority must be current, scoped, and relevant to the action class.

## Evidence Outcome Decision Matrix

| Evidence Outcome | Decision |
| --- | --- |
| `EVIDENCE_SUFFICIENT` | Continue to other checks |
| `EVIDENCE_SUFFICIENT_FOR_LOW_RISK` | ALLOW only for low-risk actions; otherwise NEEDS_MORE_EVIDENCE |
| `EVIDENCE_SUFFICIENT_FOR_REVIEW` | REVIEW_REQUIRED |
| `EVIDENCE_WEAK` | NEEDS_MORE_EVIDENCE |
| `EVIDENCE_PARTIAL` | NEEDS_MORE_EVIDENCE or REVIEW_REQUIRED |
| `EVIDENCE_INSUFFICIENT` | NEEDS_MORE_EVIDENCE |
| `SOURCE_MISSING` | NEEDS_MORE_EVIDENCE |
| `SOURCE_STALE` | REVIEW_REQUIRED |
| `SOURCE_CONFLICT` | REVIEW_REQUIRED |
| `SOURCE_UNTRUSTED` | QUARANTINE or REVIEW_REQUIRED |

## Egress Class Decision Matrix

| Egress Class | Decision |
| --- | --- |
| `NO_EGRESS` | Continue if other checks pass |
| `PUBLIC_SAFE` | ALLOW_WITH_CONDITIONS if verified |
| `INTERNAL_ONLY` | BLOCK external egress |
| `SENSITIVE` | REVIEW_REQUIRED or BLOCK |
| `SECRET` | BLOCK |
| `REGULATED` | REVIEW_REQUIRED or BLOCK |
| `BLOCKED` | BLOCK |

If egress classification is unknown:

```text
BLOCK external egress.
```

## Capability Change Decision Matrix

| Capability Outcome | Decision |
| --- | --- |
| `NO_CAPABILITY_CHANGE` | Continue to other checks |
| `CAPABILITY_CHANGE_POSSIBLE` | NEEDS_CAPABILITY_REVIEW |
| `CAPABILITY_CHANGE_CONFIRMED` | NEEDS_CAPABILITY_REVIEW |
| `HIDDEN_CAPABILITY_SUSPECTED` | NEEDS_CAPABILITY_REVIEW |
| `UNAPPROVED_CAPABILITY_PRESENT` | BLOCK or LOCKDOWN |

## AI-Human Boundary Decision Matrix

| Boundary Outcome | Decision |
| --- | --- |
| `AI_WITHIN_ROLE` | Continue to other checks |
| `AI_RECOMMENDATION_ONLY` | ALLOW_WITH_CONDITIONS; not approval |
| `AI_UNSUPPORTED_CONFIDENCE` | NEEDS_MORE_EVIDENCE |
| `AI_AUTHORITY_EXCEEDED` | BLOCK |
| `AI_SELF_ESCALATION` | BLOCK |
| `HUMAN_REVIEW_REQUIRED` | REVIEW_REQUIRED |
| `HUMAN_APPROVAL_MISSING` | NEEDS_AUTHORITY |
| `HUMAN_OVERRIDE_REQUESTED` | REVIEW_REQUIRED |
| `HUMAN_OVERRIDE_UNRECORDED` | BLOCK |

## Audit Outcome Decision Matrix

| Audit Outcome | Decision |
| --- | --- |
| `AUDIT_NOT_REQUIRED_FOR_LOW_RISK` | Continue if other checks pass |
| `AUDIT_RECORD_PRESENT` | Continue if other checks pass |
| `AUDIT_RECORD_INCOMPLETE` | REVIEW_REQUIRED |
| `AUDIT_RECORD_MISSING` | BLOCK for governed action |
| `ACCOUNTABILITY_MISSING` | BLOCK |

## Rollback Outcome Decision Matrix

| Rollback Outcome | Decision |
| --- | --- |
| `REVERSIBLE` | Continue if other checks pass |
| `PARTIALLY_REVERSIBLE` | REVIEW_REQUIRED for medium or higher risk |
| `IRREVERSIBLE` | REVIEW_REQUIRED or BLOCK |
| `ROLLBACK_UNKNOWN` | REVIEW_REQUIRED |
| `RECOVERY_REQUIRED` | REVIEW_REQUIRED or INCIDENT_RESPONSE |

## Stop-State Decision Matrix

The Stop-State Registry is authoritative for canonical stop-state handling.

Summary mapping:

| Stop-State Category | Default Decision |
| --- | --- |
| Authority stop | NEEDS_AUTHORITY or BLOCK |
| Evidence stop | NEEDS_MORE_EVIDENCE or REVIEW_REQUIRED |
| Mode stop | BLOCK |
| Egress stop | BLOCK |
| Capability stop | NEEDS_CAPABILITY_REVIEW |
| AI-human governance stop | REVIEW_REQUIRED or BLOCK |
| Audit/accountability stop | BLOCK |
| Conflict/ambiguity stop | REVIEW_REQUIRED |
| Lockdown state | LOCKDOWN |
| Incident state | INCIDENT_RESPONSE |
| Recovery state | REVIEW_REQUIRED or INCIDENT_RESPONSE |

## Combined Decision Examples

### Example 1 - Documentation Change In Current Project

```text
Lifecycle mode: LM-1_REVIEW_PACKAGE
Operational mode: ODM-3_APPROVED_DOCUMENTATION_CHANGE
Action class: DOCUMENT
Risk level: LOW
Authority outcome: AUTHORIZED
Evidence outcome: EVIDENCE_SUFFICIENT_FOR_REVIEW
Egress class: NO_EGRESS
Capability outcome: NO_CAPABILITY_CHANGE
Audit outcome: AUDIT_RECORD_PRESENT
Stop state: None
Decision: ALLOW_WITH_CONDITIONS
```

Conditions:

- documentation-only,
- no runtime,
- no automation,
- no production claim,
- no security claim.

### Example 2 - AI Suggests Prototype Execution Too Early

```text
Lifecycle mode: LM-1_REVIEW_PACKAGE
Operational mode: ODM-3_APPROVED_DOCUMENTATION_CHANGE
Action class: EXECUTE
Risk level: HIGH
Authority outcome: NOT_AUTHORIZED
Evidence outcome: EVIDENCE_PARTIAL
Egress class: UNKNOWN
Capability outcome: CAPABILITY_CHANGE_CONFIRMED
AI-human boundary: AI_AUTHORITY_EXCEEDED
Stop state: STOP_MODE_BOUNDARY
Decision: BLOCK
```

Reason:

The project is documentation-only and prototype execution is not authorized.

### Example 3 - Secret Export Attempt

```text
Action class: EXPORT
Risk level: CRITICAL
Authority outcome: NOT_AUTHORIZED
Egress class: SECRET
Stop state: STOP_SECRET_EXPORT
Decision: BLOCK
```

If a real secret already left the system:

```text
Decision: INCIDENT_RESPONSE
```

### Example 4 - Conflicting Evidence In High-Risk Decision

```text
Action class: RECOMMEND
Risk level: HIGH
Authority outcome: AUTHORIZED_FOR_REVIEW_ONLY
Evidence outcome: SOURCE_CONFLICT
Stop state: STOP_CONFLICTING_EVIDENCE
Decision: REVIEW_REQUIRED
```

The system may describe the conflict but must not make a final claim.

### Example 5 - Unapproved Capability In A Refactor

```text
Action class: CHANGE
Risk level: HIGH
Capability outcome: HIDDEN_CAPABILITY_SUSPECTED
Stop state: STOP_HIDDEN_CAPABILITY
Decision: NEEDS_CAPABILITY_REVIEW
```

The change must be reviewed as capability expansion, even if described as cleanup.

## Default Deny Rules

The following conditions default to block:

- Unknown egress classification for external output.
- Missing authority for governed action.
- Mode boundary violation.
- AI self-escalation.
- Secret export.
- Unrecorded human override.
- Missing audit record for high-risk action.
- Production action in current documentation-only lifecycle mode.

## Default Review Rules

The following conditions default to review:

- Conflicting evidence.
- Stale source for material claim.
- Medium or high risk with partial evidence.
- Role mismatch.
- Recovery or rollback uncertainty.
- Capability change possibility.
- Human override request.
- Compliance-related claim.
- Security-related claim.

## Current Project Decision Boundary

For the current project state:

```text
Lifecycle Mode: LM-1_REVIEW_PACKAGE
Operational Decision Mode: ODM-3_APPROVED_DOCUMENTATION_CHANGE
```

Allowed:

- conduct targeted external review,
- log and evaluate reviewer feedback,
- make approved bounded corrections to existing documents,
- maintain reviewer bundles and repository-release material,
- test the assessment offer without software or live data.

Not allowed:

- runtime,
- automation,
- prototype execution,
- live integrations,
- real sensitive data processing,
- production security use,
- compliance claims,
- security validation claims.

## Current Consistency Decision

This matrix should be treated as the initial authoritative decision mapping for future review documents.

It does not replace the Stop-State Registry.

It uses the Stop-State Registry as a decision input.
