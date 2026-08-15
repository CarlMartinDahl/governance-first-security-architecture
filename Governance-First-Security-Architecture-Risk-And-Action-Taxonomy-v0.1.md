# Governance-First Security Architecture

## Risk And Action Taxonomy v0.1

## Status

This document is a preparatory risk and action taxonomy for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a complete risk model.

It is not a security claim.

It is intended to define initial action classes, risk levels, escalation rules, and governance treatment before any build phase begins.

## Purpose

The purpose of this document is to answer:

```text
What kind of action is being requested?
How risky is it?
What evidence is required?
Who must approve it?
When must it be blocked?
```

## Core Rule

The same technical operation can have different risk depending on context.

Example:

```text
Reading a public document is low risk.
Reading a restricted legal file is high risk.
Exporting a restricted legal file is critical or blocked.
```

Therefore, risk must be based on:

- action type
- asset sensitivity
- requester authority
- mode
- evidence sufficiency
- egress impact
- capability impact
- reversibility
- compliance impact

## Action Classes

### ACTION_CLASS_0: Observation

Description:

The system observes, lists, inspects, reads metadata, or checks state without changing anything.

Examples:

- read status
- list files
- inspect logs
- check sync state
- identify latest document
- summarize current governance state

Default risk:

```text
LOW
```

Can become higher risk if:

- sensitive content is displayed
- logs contain personal data
- metadata reveals secrets
- observation crosses an export boundary

Default governance:

```text
Allowed in read-only mode if asset access is permitted.
```

### ACTION_CLASS_1: Analysis

Description:

The system interprets, compares, reasons, summarizes, or evaluates information without making an authoritative decision.

Examples:

- summarize evidence
- compare documents
- identify inconsistency
- assess possible risk
- describe options

Default risk:

```text
LOW_TO_MEDIUM
```

Can become higher risk if:

- output is treated as authoritative
- legal, financial, medical, or security conclusions are made
- analysis is used to justify execution
- evidence is weak or stale

Default governance:

```text
Requires source and uncertainty marking.
High-impact analysis requires human review before use.
```

### ACTION_CLASS_2: Recommendation

Description:

The system suggests a possible action but does not authorize or execute it.

Examples:

- recommend next governance step
- suggest risk treatment
- suggest review path
- propose mitigation
- propose export denial

Default risk:

```text
MEDIUM
```

Can become higher risk if:

- recommendation affects sensitive assets
- recommendation implies approval
- recommendation changes direction of a model
- multiple options exist and the system chooses without authority

Default governance:

```text
Must be labeled non-authorizing unless explicitly approved.
```

### ACTION_CLASS_3: Decision

Description:

The system or authorized human selects, approves, rejects, blocks, or classifies a path.

Examples:

- approve next step
- reject export
- classify risk
- close a plan
- authorize review
- assign stop state

Default risk:

```text
MEDIUM_TO_HIGH
```

Can become critical if:

- decision enables execution
- decision enables export
- decision changes system capability
- decision affects regulated data
- decision advances mode

Default governance:

```text
Requires authority, evidence, audit trail, and explicit decision state.
```

### ACTION_CLASS_4: Write Or State Change

Description:

The system changes files, records, configuration, state, policy, metadata, or governance documents.

Examples:

- create document
- update policy
- change configuration
- commit file
- update steering state
- write decision record

Default risk:

```text
MEDIUM
```

Can become high or critical if:

- it affects runtime behavior
- it changes policy
- it modifies authority
- it modifies logs
- it changes access or mode

Default governance:

```text
Requires exact scope approval, pre/post verification, and audit trail.
```

### ACTION_CLASS_5: Export Or Egress

Description:

The system moves data, documents, secrets, outputs, prompts, decisions, or capability outside an approved boundary.

Examples:

- download
- send externally
- publish
- push to remote
- copy to another system
- expose API output
- share prompt/system instruction

Default risk:

```text
HIGH
```

Can be blocked by default if:

- secrets are involved
- restricted personal data is involved
- privileged governance instructions are involved
- security internals are involved
- destination is unapproved

Default governance:

```text
Requires egress classification, destination validation, purpose check, and audit.
```

### ACTION_CLASS_6: Execution

Description:

The system performs an action with direct operational, external, financial, security, legal, or real-world effect.

Examples:

- run automation
- deploy change
- call external API with effect
- place order
- modify access rights
- delete data
- trigger incident response
- change security control

Default risk:

```text
HIGH_TO_CRITICAL
```

Default governance:

```text
Requires explicit execution approval, rollback plan, audit, and mode authorization.
```

### ACTION_CLASS_7: Capability Change

Description:

The system gains or enables a new ability.

Examples:

- read-only to write-capable
- local-only to network-enabled
- manual to automated
- analysis to execution
- no-export to export-capable
- no-tools to tool-enabled
- no-memory to memory-enabled

Default risk:

```text
HIGH
```

Can be critical if:

- external impact is possible
- sensitive data is reachable
- AI autonomy increases
- security controls are affected

Default governance:

```text
Requires separate capability-change gate.
```

### ACTION_CLASS_8: Mode Advancement

Description:

The system moves from one operating mode to a higher-capability mode.

Examples:

- read-only to sandbox
- sandbox to controlled test
- controlled test to limited deployment
- limited deployment to production

Default risk:

```text
HIGH_TO_CRITICAL
```

Default governance:

```text
Requires formal review, evidence, approval, rollback, and audit.
```

### ACTION_CLASS_9: Recovery Or Incident Response

Description:

The system freezes, isolates, revokes, rotates, restores, rolls back, or creates incident handling actions.

Examples:

- freeze export
- revoke credentials
- rotate keys
- isolate session
- roll back state
- create incident report

Default risk:

```text
MEDIUM_TO_HIGH
```

Can be critical if:

- recovery control can disrupt operations
- evidence may be destroyed
- access can be permanently revoked

Default governance:

```text
Requires incident authority, audit, and recovery verification.
```

## Risk Levels

### RISK_0: Minimal

Description:

Trivial action with no sensitive asset, no export, no state change, no capability change, and no compliance impact.

Default treatment:

```text
Allow with normal logging.
```

### RISK_1: Low

Description:

Low-impact observation or analysis within an approved boundary.

Default treatment:

```text
Allow if role, asset access, and mode are valid.
```

### RISK_2: Medium

Description:

Action affects internal state, non-sensitive governance documentation, or non-authoritative recommendations.

Default treatment:

```text
Require source/evidence, scope, and audit.
```

### RISK_3: High

Description:

Action affects sensitive assets, authority, export, policy, security controls, human accountability, or high-impact decisions.

Default treatment:

```text
Require human review, approval, audit, and rollback where applicable.
```

### RISK_4: Critical

Description:

Action may cause irreversible harm, data breach, regulatory exposure, system compromise, capability expansion, production impact, or high-risk AI effect.

Default treatment:

```text
Require explicit approval, stronger review, rollback plan, incident fallback, and audit.
```

### RISK_5: Blocked

Description:

Action is not allowed in the current mode, lacks lawful purpose, lacks authority, attempts prohibited export, attempts unsafe AI self-escalation, or violates a hard boundary.

Default treatment:

```text
BLOCKED
```

## Risk Escalators

Any action should be escalated if it involves:

- personal data
- secrets or credentials
- regulated material
- legal or financial impact
- security control changes
- external export
- irreversible changes
- AI autonomy increase
- tool or network access
- stale authority
- weak evidence
- conflicting sources
- unclear human accountability
- production impact
- compliance impact

## Risk Reducers

Risk may be reduced if:

- data is public
- action is read-only
- no export occurs
- no state change occurs
- no capability changes
- source is current and authoritative
- action is reversible
- audit trail is complete
- human review is already completed
- mode explicitly permits the action

Risk reducers must not override hard blocks.

## Required Governance By Risk Level

| Risk Level | Required Governance |
|---|---|
| RISK_0 Minimal | Basic log |
| RISK_1 Low | Role + asset + mode check |
| RISK_2 Medium | Source/evidence + scope + audit |
| RISK_3 High | Human review + approval + audit |
| RISK_4 Critical | Strong review + rollback + incident fallback + audit |
| RISK_5 Blocked | Stop |

## Canonical Vocabulary Crosswalk

The ordinal classes in this document are explanatory taxonomy labels. Structured review records, synthetic test cases, and future schema-compatible material should use the canonical values in the Decision-State Matrix and Prototype Data Schema.

### Action-Class Crosswalk

| Taxonomy Class | Canonical Action Value | Interpretation |
| --- | --- | --- |
| `ACTION_CLASS_0` Observation | `OBSERVE` | Read or inspect without changing state |
| `ACTION_CLASS_1` Analysis | `ANALYZE` | Interpret available information |
| `ACTION_CLASS_2` Recommendation | `RECOMMEND` | Non-authorizing recommendation |
| `ACTION_CLASS_3` Decision | `RECOMMEND`, `CHANGE`, or `EXECUTE` | Use `RECOMMEND` when non-authorizing; otherwise use the value matching the effect |
| `ACTION_CLASS_4` Write or state change | `DOCUMENT` or `CHANGE` | Use `DOCUMENT` for approved documentation changes and `CHANGE` for other state changes |
| `ACTION_CLASS_5` Export or egress | `EXPORT` | Move information across a boundary |
| `ACTION_CLASS_6` Execution | `EXECUTE` | Perform an approved operation |
| `ACTION_CLASS_7` Capability change | `CHANGE` | Pair with the applicable `capability_outcome` value |
| `ACTION_CLASS_8` Mode advancement | `ESCALATE` | Request a more permissive mode |
| `ACTION_CLASS_9` Recovery or incident action | `RECOVER` | Perform an authorized recovery action |

`OVERRIDE` is the canonical value for an explicit override attempt. It was not separated from the ordinal taxonomy and must not be inferred from a generic decision or change.

### Risk-Level Crosswalk

| Taxonomy Level | Canonical Risk Value | Interpretation |
| --- | --- | --- |
| `RISK_0` Minimal | `LOW` | Preserve "minimal" only as an explanatory qualifier |
| `RISK_1` Low | `LOW` | Low risk |
| `RISK_2` Medium | `MEDIUM` | Medium risk |
| `RISK_3` High | `HIGH` | High risk |
| `RISK_4` Critical | `CRITICAL` | Critical risk |
| `RISK_5` Blocked | Not a risk input | Record the applicable stop state and a final `BLOCK` decision instead |

Unknown or unresolved risk maps to `UNKNOWN_RISK` and must not be silently reduced to `LOW`.

## Hard Blocks

The following should default to blocked unless a future document defines a safe, reviewed exception path:

- secret export
- AI self-escalation
- execution in read-only mode
- unauthorized sensitive data export
- capability change without gate
- mode advancement without approval
- irreversible action without rollback
- processing without lawful purpose
- action based on missing source
- action based on stale authority treated as current authority
- human override without accountability

## Action-To-Risk Matrix

| Action Class | Default Risk | Key Gate |
|---|---|---|
| Observation | Low | Asset/mode check |
| Analysis | Low to Medium | Source/evidence |
| Recommendation | Medium | Non-authorization label |
| Decision | Medium to High | Authority and audit |
| Write/state change | Medium | Exact scope approval |
| Export/egress | High | Egress gate |
| Execution | High to Critical | Execution approval |
| Capability change | High | Capability gate |
| Mode advancement | High to Critical | Mode gate |
| Recovery/incident | Medium to High | Incident authority |

## Example Classifications

### Example 1: Summarize public document

Action class:

```text
Analysis
```

Risk:

```text
Low
```

Required:

```text
Source reference, no authority claim.
```

### Example 2: Summarize restricted legal document

Action class:

```text
Analysis
```

Risk:

```text
High
```

Required:

```text
Access authority, source traceability, human review before use.
```

### Example 3: Export audit log externally

Action class:

```text
Export/Egress
```

Risk:

```text
High to Critical
```

Required:

```text
Purpose, authority, redaction review, destination validation, audit.
```

### Example 4: Give AI network access

Action class:

```text
Capability Change
```

Risk:

```text
High
```

Required:

```text
Capability-change gate, tool boundary review, egress review.
```

### Example 5: Execute production security change

Action class:

```text
Execution
```

Risk:

```text
Critical
```

Required:

```text
Explicit approval, rollback, audit, incident fallback.
```

## AI-Specific Classification Rules

AI output should be classified separately from human authorization.

AI may produce:

- observation
- analysis
- recommendation
- uncertainty
- refusal
- stop-state suggestion

AI must not independently create:

- final approval
- mode advancement
- execution authority
- capability change
- high-risk override
- lawful basis

Default rule:

```text
AI recommendation is not authorization.
```

## Human-Specific Classification Rules

Human requests should be classified separately from human authority.

A human may request an action without having authority to approve it.

Default rule:

```text
Human request is not approval.
```

High-risk human override requires:

- role authority
- reason
- audit
- review
- accountability

## Open Questions

1. Are the action classes too many or too few?
2. Should export and execution be separated more strongly?
3. Should capability change always be high risk?
4. Which actions can be automated safely?
5. Which actions must always require human review?
6. Which risks require four-eyes approval?
7. How should legal/compliance risk alter classification?
8. How should AI-generated decisions be prevented from becoming authority?
9. How should low-risk actions avoid approval fatigue?
10. What is the safest minimal taxonomy for version 0?
