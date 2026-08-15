# Governance-First Security Architecture - Mode Model Normalization v0.1

## Status

Preparatory documentation.

This document is not an implementation.

This document is not an authorization model.

This document normalizes mode terminology across the Governance-First Security Architecture documentation set.

## Purpose

The purpose of this document is to resolve terminology drift between:

- deployment or maturity modes, and
- operational decision modes.

Earlier documents use mode names such as:

```text
MODE_0_READ_ONLY
MODE_1_SANDBOX
MODE_2_CONTROLLED_TEST
MODE_3_LIMITED_DEPLOYMENT
MODE_4_PRODUCTION
```

The Minimal Viable Governance Kernel uses operational modes such as:

```text
READ_ONLY
PLAN_ONLY
REVIEW_ONLY
APPROVED_ACTION
LOCKDOWN
INCIDENT
```

Both are useful, but they describe different things.

## Core Normalization Decision

The model should use two separate mode vocabularies:

1. **Lifecycle Mode**
2. **Operational Decision Mode**

They must not be merged.

Lifecycle Mode answers:

```text
Where is the system in its maturity, deployment, or build lifecycle?
```

Operational Decision Mode answers:

```text
What is this specific session, request, action, or decision allowed to do right now?
```

## Vocabulary 1 - Lifecycle Mode

Lifecycle Mode describes the maturity or deployment state of the system itself.

### LM-0 - DOCUMENTATION_ONLY

The system exists only as documentation.

Allowed:

- concept writing,
- internal review,
- external review preparation,
- terminology cleanup,
- synthetic test planning.

Not allowed:

- runtime,
- automation,
- integration,
- live data processing,
- production use,
- security claim,
- compliance claim.

Historical project state before the external-review freeze:

```text
LM-0 - DOCUMENTATION_ONLY
```

### LM-1 - REVIEW_PACKAGE

The documentation is prepared for trusted external review.

Allowed:

- external expert review,
- challenge questions,
- review comments,
- scope correction,
- terminology correction.

Not allowed:

- prototype implementation,
- live integrations,
- production use,
- compliance claims,
- security claims.

Current project state:

```text
LM-1 - REVIEW_PACKAGE
```

### LM-2 - PROTOTYPE_DESIGN

A limited prototype is being designed but not yet built.

Allowed:

- prototype boundary definition,
- synthetic data design,
- test-case selection,
- local-only architecture planning,
- review of proposed prototype scope.

Not allowed:

- running prototype code,
- real data,
- external integrations,
- production controls,
- autonomous execution.

### LM-3 - LIMITED_SYNTHETIC_PROTOTYPE

A limited prototype exists with synthetic data only.

Allowed:

- local decision simulator,
- synthetic test cases,
- mock audit records,
- mock stop states,
- non-production evaluation.

Not allowed:

- real personal data,
- real secrets,
- external integrations,
- production enforcement,
- security claims,
- compliance claims.

### LM-4 - VALIDATED_RESEARCH_PROTOTYPE

A prototype has been reviewed and tested with stricter governance, but still remains non-production.

Allowed only after:

- external technical review,
- security review,
- legal/compliance review where relevant,
- test evidence,
- documented limitations,
- approved scope.

Not allowed by default:

- production deployment,
- autonomous remediation,
- live blocking,
- broad claims.

### LM-5 - CONTROLLED_PILOT

A controlled pilot may be considered only after formal review.

This lifecycle mode is intentionally out of scope for the current documentation package.

No current document authorizes LM-5.

### LM-6 - PRODUCTION

Production use.

This lifecycle mode is out of scope.

No current document authorizes production use.

## Vocabulary 2 - Operational Decision Mode

Operational Decision Mode describes what a specific action, request, session, or evaluation is allowed to do.

### ODM-0 - READ_ONLY

The system may inspect, summarize, classify, and report.

Allowed:

- read provided material,
- summarize,
- identify gaps,
- classify risk,
- propose questions,
- propose stop states.

Not allowed:

- change files or systems,
- export sensitive material,
- execute tools that alter state,
- approve actions,
- escalate mode.

### ODM-1 - PLAN_ONLY

The system may create plans but may not execute them.

Allowed:

- draft plans,
- define requirements,
- propose test cases,
- propose governance changes,
- identify blockers.

Not allowed:

- implementation,
- runtime change,
- external integration,
- action execution,
- approval of its own plan.

### ODM-2 - REVIEW_ONLY

The system may review material and produce findings.

Allowed:

- review documents,
- identify contradictions,
- identify overclaims,
- identify missing controls,
- recommend corrections.

Not allowed:

- approve high-risk continuation,
- modify approved scope without authorization,
- treat review as approval.

### ODM-3 - APPROVED_DOCUMENTATION_CHANGE

The system may update documentation within an explicitly approved scope.

Allowed:

- create approved documentation,
- edit approved documentation,
- update indexes,
- correct terminology,
- add review findings.

Not allowed:

- runtime implementation,
- automation,
- integration,
- real data processing,
- security enforcement.

### ODM-4 - APPROVED_PROTOTYPE_DESIGN

The system may design a prototype within an approved boundary.

Allowed:

- define architecture,
- define synthetic data,
- define test harness design,
- define non-production behavior,
- define audit record schema.

Not allowed:

- build or run prototype,
- use real data,
- connect real systems,
- claim security validation.

### ODM-5 - APPROVED_SYNTHETIC_PROTOTYPE_ACTION

The system may perform approved prototype work using synthetic data only.

Allowed only when:

- lifecycle mode permits prototype work,
- scope is explicit,
- data is synthetic,
- egress is blocked or controlled,
- audit records exist,
- rollback is trivial.

Not allowed:

- production use,
- real secrets,
- real personal data,
- live integrations,
- autonomous remediation.

### ODM-6 - LOCKDOWN

The system must restrict continuation and preserve safety.

Triggers may include:

- unauthorized egress attempt,
- suspected prompt injection,
- unapproved capability expansion,
- conflicting authority,
- missing audit path,
- suspected incident.

Allowed:

- preserve records,
- summarize safe state,
- request authorized review,
- block continuation.

Not allowed:

- normal workflow continuation,
- capability expansion,
- data export,
- silent recovery.

### ODM-7 - INCIDENT

The system must treat the situation as a potential incident.

Allowed:

- preserve audit trail,
- isolate affected scope,
- identify suspected trigger,
- recommend incident review,
- block unsafe action.

Not allowed:

- return to normal without review,
- erase evidence,
- continue affected capability,
- downplay severity without authority.

## Authoritative Current Mode

The current project state is:

```text
Lifecycle Mode: LM-1 - REVIEW_PACKAGE
Operational Decision Mode: ODM-3 - APPROVED_DOCUMENTATION_CHANGE
```

Reason:

- The documentation package is frozen and prepared for targeted external review.
- Approved changes are limited to review feedback, bounded corrections, and repository-readiness checks.
- No runtime, automation, prototype, integration, or production work is authorized.

## Mode Mapping From Earlier Documents

Older or earlier shorthand should be interpreted as follows:

| Earlier Term | Normalized Meaning |
| --- | --- |
| `MODE_0_READ_ONLY` | Usually LM-0 or ODM-0 depending on context |
| `MODE_1_SANDBOX` | Usually LM-3 or ODM-5 if synthetic prototype exists |
| `MODE_2_CONTROLLED_TEST` | Usually LM-3 or LM-4 with controlled synthetic tests |
| `MODE_3_LIMITED_DEPLOYMENT` | Future LM-5, currently out of scope |
| `MODE_4_PRODUCTION` | LM-6, out of scope |
| `READ_ONLY` | ODM-0 |
| `PLAN_ONLY` | ODM-1 |
| `REVIEW_ONLY` | ODM-2 |
| `APPROVED_ACTION` | Must be replaced by a more specific approved operational mode |
| `LOCKDOWN` | ODM-6 |
| `INCIDENT` | ODM-7 |

## Deprecated Term

The term:

```text
APPROVED_ACTION
```

is too broad for future prototype design.

It should be replaced by specific approved modes:

- `APPROVED_DOCUMENTATION_CHANGE`
- `APPROVED_PROTOTYPE_DESIGN`
- `APPROVED_SYNTHETIC_PROTOTYPE_ACTION`

Future documents should avoid generic `APPROVED_ACTION` unless it is explicitly defined.

## Mode Transition Rule

No mode may advance without:

- explicit scope,
- authority,
- evidence,
- risk classification,
- egress classification,
- audit record,
- rollback or recovery path,
- human review where required.

Default rule:

```text
If mode is unclear, downgrade to the safest applicable mode.
```

For current work, unclear mode should downgrade to:

```text
LM-0 - DOCUMENTATION_ONLY
ODM-0 - READ_ONLY
```

or stop for review.

## Mode Transition Matrix

| From | To | Default Decision |
| --- | --- | --- |
| LM-0 | LM-1 | Review required |
| LM-1 | LM-2 | External review required |
| LM-2 | LM-3 | Prototype design approval required |
| LM-3 | LM-4 | Test evidence and expert review required |
| LM-4 | LM-5 | Formal governance approval required |
| LM-5 | LM-6 | Out of scope |
| ODM-0 | ODM-1 | Scope approval required |
| ODM-1 | ODM-2 | Review scope required |
| ODM-2 | ODM-3 | Documentation-change approval required |
| ODM-3 | ODM-4 | Prototype-design approval required |
| ODM-4 | ODM-5 | Synthetic prototype approval required |
| Any | ODM-6 | Triggered by unsafe condition |
| Any | ODM-7 | Triggered by potential incident |

## Required Mode Record

Every future governed action should record:

```text
Lifecycle mode:
Operational decision mode:
Requested transition:
Actor:
Authority:
Evidence:
Risk level:
Egress class:
Approval:
Audit record:
Rollback or recovery path:
Decision:
```

## Impact On Current Documents

This document does not invalidate earlier documents.

It clarifies how their mode terms should be interpreted.

Future documents should use:

- Lifecycle Mode for project/system maturity.
- Operational Decision Mode for session/action/request permission.

## Current Consistency Decision

The package should be treated as internally consistent if this normalization is adopted.

Mode terminology is now clarified as:

```text
Lifecycle Mode != Operational Decision Mode
```

This removes the main ambiguity identified in the Internal Consistency Review.
