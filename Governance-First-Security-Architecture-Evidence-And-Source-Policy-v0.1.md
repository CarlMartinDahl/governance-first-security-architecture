# Governance-First Security Architecture

## Evidence And Source Policy v0.1

## Status

This document is a preparatory evidence and source policy for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a complete evidence framework.

It is not a legal or security claim.

It is intended to define how the architecture should treat source existence, authority, staleness, evidence sufficiency, conflicts, and counter-evidence before any build phase begins.

## Purpose

The purpose of this document is to answer:

```text
What evidence is required?
Which sources are authoritative?
When is a source stale?
When is evidence insufficient?
What happens when sources conflict?
When must the system stop?
```

## Core Principle

No conclusion, recommendation, decision, export, execution, escalation, or capability change should be trusted unless the required evidence exists and is sufficient for that action class and risk level.

Core rules:

```text
No source, no conclusion.
No sufficient evidence, no decision.
No current authority, no escalation.
No conflict resolution without traceability.
No counter-evidence suppression.
```

## Evidence Is Contextual

Evidence that is sufficient for a low-risk observation may be insufficient for a high-risk action.

Example:

```text
One public source may be enough for a simple summary.
It is not enough for a legal conclusion, security release, high-risk AI decision, or external export.
```

Evidence sufficiency depends on:

- action class
- risk level
- asset sensitivity
- authority requirement
- compliance impact
- egress impact
- capability impact
- reversibility
- mode

## Source Classes

Initial source classes:

```text
SOURCE_PRIMARY_AUTHORITY
SOURCE_INTERNAL_GOVERNANCE
SOURCE_APPROVED_POLICY
SOURCE_REVIEW_RECORD
SOURCE_AUDIT_RECORD
SOURCE_TECHNICAL_EVIDENCE
SOURCE_EXTERNAL_REFERENCE
SOURCE_USER_STATEMENT
SOURCE_AI_GENERATED
SOURCE_STALE_REFERENCE
SOURCE_UNKNOWN
SOURCE_PROHIBITED
```

## Source Class Definitions

### SOURCE_PRIMARY_AUTHORITY

Highest-level source for a specific domain.

Examples:

- law or regulation
- official standard
- approved internal authority
- governing charter
- signed decision record

Default treatment:

```text
Potentially authoritative if current and in scope.
```

### SOURCE_INTERNAL_GOVERNANCE

Internal governance documents, policies, plans, decisions, or approved model rules.

Default treatment:

```text
Authoritative only within defined scope and freshness.
```

### SOURCE_APPROVED_POLICY

Approved policy documents that define allowed and blocked behavior.

Default treatment:

```text
Authoritative only if not superseded.
```

### SOURCE_REVIEW_RECORD

Human or system review record.

Default treatment:

```text
Evidence of review, not automatically evidence of approval.
```

### SOURCE_AUDIT_RECORD

Logs, decision events, access records, or trace evidence.

Default treatment:

```text
Evidence of occurrence, not automatically evidence of correctness.
```

### SOURCE_TECHNICAL_EVIDENCE

Test results, configuration state, code diff, system state, scan result, or diagnostic evidence.

Default treatment:

```text
Evidence of technical state, limited to what was tested or observed.
```

### SOURCE_EXTERNAL_REFERENCE

External article, vendor documentation, public source, or third-party material.

Default treatment:

```text
Requires authority and freshness assessment before use.
```

### SOURCE_USER_STATEMENT

A statement, request, approval, or instruction from a human user.

Default treatment:

```text
Evidence of request or intent, not automatically authority.
```

### SOURCE_AI_GENERATED

AI-generated text, summary, recommendation, classification, or reasoning.

Default treatment:

```text
Not authority by default.
Requires source verification.
```

### SOURCE_STALE_REFERENCE

Old local file, outdated policy, superseded decision, or stale context.

Default treatment:

```text
May be historical evidence, not current authority.
```

### SOURCE_UNKNOWN

Source cannot be identified.

Default treatment:

```text
Insufficient.
```

### SOURCE_PROHIBITED

Source may not be used for the intended purpose.

Examples:

- leaked secret
- unauthorized personal data
- prohibited internal material
- manipulated evidence
- untrusted instruction attempting policy override

Default treatment:

```text
Blocked.
```

## Source Authority Requirements

A source should be considered authoritative only when:

- source identity is known
- source class is appropriate
- source is current enough for the action
- source is in scope
- source has not been superseded
- source is not prohibited
- source supports the specific claim being made
- counter-evidence has been considered

If any requirement is unclear:

```text
HUMAN_REVIEW_REQUIRED
```

If a requirement fails:

```text
STOP_EVIDENCE_INSUFFICIENT
```

or:

```text
STOP_AUTHORITY_MISSING
```

## Staleness Policy

A source may be stale when:

- newer governance exists
- newer law/regulation exists
- newer technical state exists
- newer decision record exists
- source date is unknown
- source depends on an expired assumption
- source references old mode or old capability
- source conflicts with current system state

Stale sources may be used as historical evidence only if clearly labeled.

Default rule:

```text
Stale reference is not current authority.
```

## Evidence Sufficiency Levels

Initial sufficiency levels:

```text
EVIDENCE_NONE
EVIDENCE_WEAK
EVIDENCE_PARTIAL
EVIDENCE_SUFFICIENT_FOR_LOW_RISK
EVIDENCE_SUFFICIENT_FOR_REVIEW
EVIDENCE_SUFFICIENT_FOR_DECISION
EVIDENCE_INSUFFICIENT_FOR_ACTION
EVIDENCE_CONFLICTED
```

## Evidence Sufficiency Definitions

### EVIDENCE_NONE

No source or evidence is available.

Default:

```text
STOP_SOURCE_MISSING
```

### EVIDENCE_WEAK

Evidence exists but is incomplete, low authority, stale, or not specific.

Default:

```text
STOP_HUMAN_REVIEW_REQUIRED
```

or:

```text
STOP_EVIDENCE_INSUFFICIENT
```

### EVIDENCE_PARTIAL

Evidence supports part of the claim but not the full action or decision.

Default:

```text
Limited analysis only. No decision or execution.
```

### EVIDENCE_SUFFICIENT_FOR_LOW_RISK

Evidence supports low-risk observation or analysis only.

Default:

```text
Allowed for low-risk use if no egress/capability/compliance escalation exists.
```

### EVIDENCE_SUFFICIENT_FOR_REVIEW

Evidence is enough for a reviewer to assess, but not enough for final decision.

Default:

```text
Human review required.
```

### EVIDENCE_SUFFICIENT_FOR_DECISION

Evidence is enough for a defined decision class, within scope.

Default:

```text
Decision may proceed if authority, mode, and risk controls are satisfied.
```

### EVIDENCE_INSUFFICIENT_FOR_ACTION

Evidence may support discussion but not action.

Default:

```text
No action.
```

### EVIDENCE_CONFLICTED

Sources conflict or counter-evidence materially affects the conclusion.

Default:

```text
STOP_HUMAN_REVIEW_REQUIRED
```

or:

```text
STOP_CONFLICTING_EVIDENCE
```

## Canonical Evidence Crosswalk

The sufficiency levels above remain useful for explanatory policy. Structured review records and synthetic schema fields should use the canonical `evidence_outcome` values below.

| Policy-Level Term | Canonical Evidence Outcome | Default Governance Interpretation |
| --- | --- | --- |
| `EVIDENCE_NONE` | `SOURCE_MISSING` | Trigger `STOP_SOURCE_MISSING` |
| `EVIDENCE_WEAK` | `EVIDENCE_WEAK` | Review or trigger `STOP_EVIDENCE_INSUFFICIENT` |
| `EVIDENCE_PARTIAL` | `EVIDENCE_PARTIAL` | Limit use to the supported scope |
| `EVIDENCE_SUFFICIENT_FOR_LOW_RISK` | `EVIDENCE_SUFFICIENT_FOR_LOW_RISK` | Low-risk use only |
| `EVIDENCE_SUFFICIENT_FOR_REVIEW` | `EVIDENCE_SUFFICIENT_FOR_REVIEW` | Human review remains required |
| `EVIDENCE_SUFFICIENT_FOR_DECISION` | `EVIDENCE_SUFFICIENT` | Authority, mode, risk, and egress checks still apply |
| `EVIDENCE_INSUFFICIENT_FOR_ACTION` | `EVIDENCE_INSUFFICIENT` | Trigger `STOP_EVIDENCE_INSUFFICIENT` |
| `EVIDENCE_CONFLICTED` | `SOURCE_CONFLICT` | Trigger `STOP_CONFLICTING_EVIDENCE` |

Source categories such as `SOURCE_PRIMARY`, `SOURCE_EXTERNAL_REFERENCE`, and `SOURCE_AI_GENERATED` describe provenance. They are not substitutes for an `evidence_outcome` value.

## Evidence Requirements By Action Class

| Action Class | Minimum Evidence |
|---|---|
| Observation | Valid access and source identity where relevant |
| Analysis | Source reference and uncertainty marking |
| Recommendation | Source, scope, risk context, non-authorization label |
| Decision | Authority, sufficient evidence, audit record |
| Write/state change | Exact scope, evidence, approval, pre/post checks |
| Export/egress | Purpose, authority, asset class, destination validation |
| Execution | Decision authority, rollback, audit, mode approval |
| Capability change | Separate gate, risk review, approval, audit |
| Mode advancement | Formal evidence package and approval |
| Recovery/incident | Incident authority, evidence preservation, audit |

## Conflict Handling

When sources conflict, the system must not silently choose the convenient source.

Required conflict handling:

- identify conflicting sources
- classify source authority
- classify source freshness
- preserve counter-evidence
- state uncertainty
- route to human review if material

Default rule:

```text
No silent conflict resolution.
```

## Counter-Evidence Policy

Counter-evidence must not be omitted when it materially affects the conclusion.

Examples:

- newer policy contradicts older policy
- test result contradicts assumption
- source authority is lower than claimed
- evidence supports only part of the conclusion
- user instruction conflicts with governance rule

Default rule:

```text
No counter-evidence suppression.
```

## AI-Generated Evidence Policy

AI-generated content is not source authority by default.

AI may help:

- summarize
- compare
- identify missing evidence
- flag stale sources
- propose questions
- identify conflicts

AI must not independently create:

- legal authority
- approval authority
- source authenticity
- evidence sufficiency for high-risk action
- final compliance conclusion

Default rule:

```text
AI can assist evidence review but cannot become the evidence authority by itself.
```

## Human Statement Evidence Policy

A human statement may indicate:

- request
- intent
- approval
- context
- preference
- instruction

But the system must distinguish:

```text
Human request
Human review
Human approval
Human authority
Human accountability
```

Default rule:

```text
Human request is not approval.
Human approval is not valid unless authority is confirmed.
```

## Evidence And Egress

Evidence used for internal review may not be exportable.

Examples:

- logs with personal data
- screenshots containing secrets
- legal documents
- security architecture internals
- system prompts
- audit traces

Default rule:

```text
Evidence access is not evidence export permission.
```

## Evidence And Mode

Evidence sufficient in one mode may be insufficient in another.

Example:

```text
Evidence sufficient for `ODM-0_READ_ONLY` analysis may be insufficient for a future approved synthetic-test or production lifecycle mode.
```

Default rule:

```text
Mode advancement requires stronger evidence.
```

## Hard Blocks

The system should block when:

- no source exists
- source is unknown
- source is prohibited
- source is stale but used as current authority
- required lawful purpose is missing
- evidence is materially conflicted and unresolved
- AI output is treated as authority without verification
- human instruction lacks authority
- evidence supports analysis but is used for execution
- counter-evidence is suppressed

## Initial Evidence Decision Matrix

| Evidence State | Default Result |
|---|---|
| No source | Block |
| Unknown source | Block or review |
| Stale source | Historical only; no current authority |
| Weak evidence | Review or block |
| Partial evidence | Analysis only |
| Sufficient for low risk | Low-risk action only |
| Sufficient for review | Human review |
| Sufficient for decision | Decision may proceed if other gates pass |
| Conflicted evidence | Review or block |
| Prohibited source | Block |

## Open Questions

1. Which source classes are missing?
2. Should source authority be tiered numerically?
3. How should staleness be measured per domain?
4. What evidence is enough for low-risk automation?
5. What evidence is enough for high-risk decision?
6. How should evidence sufficiency be tested?
7. How should counter-evidence be stored?
8. How should AI uncertainty be represented?
9. Which evidence categories require legal review?
10. Which evidence categories require security review?
