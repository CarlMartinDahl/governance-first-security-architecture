# Governance-First Security Architecture

## Stop State Policy v0.1

## Status

This document is a historical foundational stop-state policy for the Governance-First Security Architecture concept.

Its `BLOCKED_*` labels predate the canonical [Stop-State Registry](Governance-First-Security-Architecture-Stop-State-Registry-v0.1.md). They are preserved here for traceability only and must be mapped through the registry's Legacy Stop-State Crosswalk before use in a current review record or synthetic case.

It is documentation-only.

It is not an implementation plan.

It is not a complete incident response policy.

It is not a security claim.

It is intended to define block states, human-review states, incident states, and fail-closed behavior before any build phase begins.

## Purpose

The purpose of this document is to answer:

```text
When must the system stop?
What kind of stop is required?
What can be retried?
What requires human review?
What becomes an incident?
What must never proceed automatically?
```

## Core Principle

Uncertainty is not permission.

Missing evidence is not permission.

Missing authority is not permission.

Silence is not approval.

Core rule:

```text
Fail closed unless a valid rule allows progress.
```

## Stop State Families

Initial stop-state families:

```text
BLOCKED_*
HUMAN_REVIEW_REQUIRED
APPROVAL_REQUIRED
INCIDENT_REVIEW_REQUIRED
LOCKDOWN_REQUIRED
STOP
```

## Stop State Severity

| Severity | Meaning |
|---|---|
| NOTICE | Informational; action may continue |
| REVIEW | Human review required before progress |
| APPROVAL | Explicit approval required before progress |
| BLOCK | Action must not continue |
| INCIDENT | Potential security/compliance incident |
| LOCKDOWN | Containment or freeze required |

## General Stop Rules

The system should stop when:

- source is missing
- evidence is insufficient
- authority is missing
- lawful purpose is missing
- asset class is unknown
- egress destination is unknown
- capability impact is unknown
- requested action exceeds current mode
- AI attempts self-escalation
- human override lacks accountability
- action is irreversible without rollback
- stale policy is used as current authority
- high-risk action lacks review
- critical action lacks stronger approval
- secret export is attempted
- multiple governance paths exist and none is selected by an authorized human

## BLOCKED_SOURCE_MISSING

Meaning:

The action, claim, recommendation, decision, or export lacks an identifiable source.

Default result:

```text
BLOCK
```

Allowed next steps:

- provide source
- downgrade to uncertainty
- route to human review if source cannot be identified but context may matter

Must not:

- invent source
- assume source
- proceed as if sourced

## BLOCKED_EVIDENCE_INSUFFICIENT

Meaning:

Evidence exists but is not sufficient for the requested action class or risk level.

Default result:

```text
BLOCK
```

or:

```text
HUMAN_REVIEW_REQUIRED
```

Allowed next steps:

- gather more evidence
- reduce action scope
- downgrade from decision to analysis
- route to review

Must not:

- treat weak evidence as approval
- escalate action based on partial evidence

## BLOCKED_AUTHORITY_MISSING

Meaning:

The requester, AI, process, or document lacks authority for the requested action.

Default result:

```text
BLOCK
```

Allowed next steps:

- identify authorized role
- request proper approval
- reduce action to non-authorizing analysis

Must not:

- treat request as approval
- use AI recommendation as authority

## BLOCKED_LAWFUL_PURPOSE_MISSING

Meaning:

The action involves personal data or regulated processing but lacks a stated lawful/purpose basis.

Default result:

```text
BLOCK
```

Allowed next steps:

- provide purpose
- perform legal/compliance review
- minimize or remove personal data

Must not:

- process data merely because access exists

## BLOCKED_STALE_CONTEXT

Meaning:

The requested action relies on stale policy, stale local files, superseded decisions, or outdated assumptions.

Default result:

```text
BLOCK
```

or:

```text
HUMAN_REVIEW_REQUIRED
```

Allowed next steps:

- refresh authoritative context
- identify current source
- treat stale material as historical only

Must not:

- treat stale reference as current authority

## BLOCKED_UNAUTHORIZED_EXIT

Meaning:

An asset attempts to leave an approved boundary without valid egress authority.

Default result:

```text
BLOCK
```

Allowed next steps:

- classify asset
- validate purpose
- validate destination
- obtain egress approval
- redact where appropriate

Must not:

- export because internal access exists

## BLOCKED_SECRET_EXPORT

Meaning:

Secrets, tokens, keys, credentials, or similarly sensitive control material are being exposed or exported.

Default result:

```text
BLOCK
INCIDENT_REVIEW_REQUIRED
```

Allowed next steps:

- revoke or rotate secret
- preserve evidence
- create incident record
- verify exposure scope

Must not:

- display, summarize, or transmit the secret further

## BLOCKED_HIGH_RISK_NO_REVIEW

Meaning:

The action is high-risk and lacks required human review.

Default result:

```text
HUMAN_REVIEW_REQUIRED
```

Allowed next steps:

- route to reviewer
- reduce scope
- provide evidence package

Must not:

- proceed automatically

## BLOCKED_CRITICAL_NO_STRONG_APPROVAL

Meaning:

The action is critical and lacks required stronger approval, such as multi-person review or authorized owner approval.

Default result:

```text
APPROVAL_REQUIRED
```

Allowed next steps:

- obtain required approval
- downgrade or defer action
- prepare rollback and incident plan

Must not:

- use single informal approval where stronger approval is required

## BLOCKED_CAPABILITY_CHANGE

Meaning:

The action creates or expands system capability without passing the capability-change gate.

Default result:

```text
BLOCK
```

Allowed next steps:

- classify capability change
- run capability-change review
- provide rollback or disable path
- obtain approval

Must not:

- hide capability change inside documentation, refactor, convenience, or automation

## BLOCKED_MODE_VIOLATION

Meaning:

The requested action is not allowed in the current operating mode.

Default result:

```text
BLOCK
```

Allowed next steps:

- remain in current mode
- request mode advancement through formal gate
- reduce action to permitted class

Must not:

- act as if mode advancement has occurred

## BLOCKED_AI_SELF_ESCALATION

Meaning:

AI attempts or is instructed to increase its own authority, tool access, autonomy, memory, mode, or execution capability.

Default result:

```text
BLOCK
```

Allowed next steps:

- request human review
- classify requested capability
- perform containment review

Must not:

- allow AI to approve its own escalation

## BLOCKED_IRREVERSIBLE_ACTION

Meaning:

The action may be irreversible or hard to undo, and no rollback or recovery path exists.

Default result:

```text
BLOCK
```

Allowed next steps:

- define rollback
- define incident fallback
- obtain higher approval
- test recovery path

Must not:

- proceed on convenience or urgency alone

## BLOCKED_COUNTER_EVIDENCE_SUPPRESSED

Meaning:

Material counter-evidence is known but omitted, hidden, or ignored.

Default result:

```text
BLOCK
HUMAN_REVIEW_REQUIRED
```

Allowed next steps:

- preserve counter-evidence
- reassess conclusion
- route to review

Must not:

- continue as if evidence is one-sided

## BLOCKED_GOVERNANCE_PATH_UNSELECTED

Meaning:

Multiple valid governance-only paths exist and no authorized human has selected one.

Default result:

```text
BLOCKED_REQUIRES_HUMAN_DECISION
```

Allowed next steps:

- present exact choices
- request explicit selection
- continue only after decision

Must not:

- let AI silently choose a materially directional path

## HUMAN_REVIEW_REQUIRED

Meaning:

The system cannot determine safety, authority, evidence sufficiency, or risk without human review.

Default result:

```text
PAUSE UNTIL REVIEW
```

Human review must include:

- what is being reviewed
- evidence available
- missing evidence
- risk level
- possible decisions
- recommended safe path if any

## APPROVAL_REQUIRED

Meaning:

Review alone is not enough; explicit approval from authorized role is required.

Default result:

```text
PAUSE UNTIL APPROVAL
```

Approval must identify:

- approver
- authority basis
- exact scope
- action class
- risk level
- evidence
- rollback if required

## INCIDENT_REVIEW_REQUIRED

Meaning:

The event may indicate security, privacy, compliance, or operational incident.

Triggers may include:

- secret exposure
- unauthorized export attempt
- suspicious bulk movement
- AI policy bypass attempt
- privileged misuse
- compromised account signal
- evidence tampering

Default result:

```text
PRESERVE EVIDENCE
PAUSE AFFECTED ACTION
ROUTE TO INCIDENT REVIEW
```

## LOCKDOWN_REQUIRED

Meaning:

Containment may be required to prevent further harm.

Possible actions:

- freeze export
- isolate session
- revoke token
- rotate secret
- suspend integration
- block tool access
- preserve logs
- alert responsible owner

Default result:

```text
CONTAIN BEFORE CONTINUING
```

## STOP

Meaning:

Action must stop and no safe continuation is available under current scope.

Default result:

```text
STOP
```

Allowed next steps:

- external review
- new scope
- new evidence
- new authority
- incident handling

## Stop State Output Requirements

When a stop state is reached, the system should provide:

- stop state name
- reason
- missing requirement
- affected asset
- action class
- risk level
- safe next step if available
- whether human review is allowed
- whether incident review is required

## Stop State Matrix

| Condition | Stop State |
|---|---|
| No source | BLOCKED_SOURCE_MISSING |
| Evidence insufficient | BLOCKED_EVIDENCE_INSUFFICIENT |
| Authority missing | BLOCKED_AUTHORITY_MISSING |
| Lawful purpose missing | BLOCKED_LAWFUL_PURPOSE_MISSING |
| Stale context | BLOCKED_STALE_CONTEXT |
| Unauthorized export | BLOCKED_UNAUTHORIZED_EXIT |
| Secret export | BLOCKED_SECRET_EXPORT |
| High risk without review | BLOCKED_HIGH_RISK_NO_REVIEW |
| Critical without stronger approval | BLOCKED_CRITICAL_NO_STRONG_APPROVAL |
| Capability change without gate | BLOCKED_CAPABILITY_CHANGE |
| Mode violation | BLOCKED_MODE_VIOLATION |
| AI self-escalation | BLOCKED_AI_SELF_ESCALATION |
| Irreversible without rollback | BLOCKED_IRREVERSIBLE_ACTION |
| Counter-evidence suppressed | BLOCKED_COUNTER_EVIDENCE_SUPPRESSED |
| Multiple governance paths | BLOCKED_REQUIRES_HUMAN_DECISION |

## Machine-Time Threats and the Pre-Authorized Circuit Breaker

The stop states and human-review requirements defined above assume that a human operator can intervene between threat detection and damage completion. That assumption holds for most operational conditions.

It does not hold for machine-time threats.

As defined in Machine-Time-Threat-Model-v0.1, machine-time threats are threats whose primary damage vector executes within the window between alert generation and human triage. The operational design constraint — the 1:1200:72000 ratio between attack execution time, alert delivery time, and human triage time — means that requiring human authorisation before pipeline suspension is, against machine-time threats, functionally equivalent to no suspension at all.

This policy recognises that contradiction and resolves it as follows:

**For machine-time threats, human authority governs the rules under which automated suspension operates — not each individual automated decision.**

The Governance Authority pre-authorises the conditions under which automatic suspension occurs. The automation acts on those pre-authorised conditions. The human operator reviews every automated suspension after the fact, with full evidence, and authorises any restart.

This is not a reduction in human accountability. It is a relocation of human accountability to the phases where human judgment can be effective: policy-setting before any session begins, and forensic review after automated containment.

The mechanism that implements this model is defined in Pre-Authorized-Circuit-Breaker-Policy-v0.1. That policy is a complement to this document, not a replacement. The stop state defined here — fail closed unless a valid rule allows progress — remains the governing principle. The circuit breaker is the path by which that stop state is reached in machine time.

The following conditions pre-authorise automatic pipeline suspension without requiring human decision at the moment of firing:

- Any CA-01 High alert where the pipeline alert rate exceeds the threshold defined in the relevant Operational Mandate within any 10-minute window
- Any CA-03 Critical alert (pipeline aggregate threshold exceeded)
- Any CA-04 Critical alert (authority laundering via orchestrator)
- Any CA-05 Critical alert (sub-agent output divergence)
- Any CA-06 Critical alert (lateral peer coordination outside orchestrator mediation)
- Any HR-03 Critical alert (outbound connection from inference engine to external IP)
- Any HR-07 Critical alert (system prompt hash mismatch)

For all other stop states and alert conditions, the human-review and approval requirements defined in this document apply without modification.

No agent or pipeline suspended under a pre-authorised circuit breaker may restart without explicit human authorisation. Automated suspension is always followed by mandatory human review. The stop state is not resolved by automation — it is reached by automation and resolved by humans.

## Open Questions

1. Are there too many stop states for version 0?
2. Which stop states should be merged?
3. Which stop states require incident handling?
4. Which stop states allow retry?
5. Which stop states must be final?
6. How should stop states be logged?
7. How should AI explain stop states to humans?
8. Which stop states require external review?
9. Which stop states should trigger lockdown?
10. How should approval fatigue be avoided?
