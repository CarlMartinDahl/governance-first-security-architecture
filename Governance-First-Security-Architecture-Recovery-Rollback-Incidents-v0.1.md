# Governance-First Security Architecture

## Recovery Rollback Incidents v0.1

## Status

This document is a preparatory recovery, rollback, and incident policy for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a full incident response plan.

It is not a business continuity plan.

It is not a security claim.

It is intended to define initial recovery, rollback, containment, incident review, and verification principles before any build phase begins.

## Purpose

The purpose of this document is to answer:

```text
What happens when something goes wrong?
How does the system contain harm?
How are actions rolled back?
When are keys or access revoked?
How is evidence preserved?
Who reviews the incident?
How is recovery verified?
```

## Core Principle

Security is not only prevention.

Security also requires containment, recovery, rollback, and accountability after failure or misuse.

Core rules:

```text
No irreversible action without rollback.
No incident response without evidence preservation.
No recovery without verification.
No containment without audit.
No return to normal without review.
```

## Recovery Goals

Recovery should aim to:

- stop ongoing harm
- preserve evidence
- protect sensitive assets
- revoke unsafe access
- restore safe state
- verify integrity
- document what happened
- identify remaining risk
- prevent repeat failure

## Incident Triggers

Potential incident triggers include:

- secret exposure
- unauthorized export
- attempted secret export
- suspicious bulk movement
- AI self-escalation attempt
- policy bypass attempt
- unauthorized capability change
- mode violation
- privileged misuse
- stale authority used for high-risk action
- audit tampering
- evidence suppression
- external integration behaving unexpectedly
- irreversible action without rollback
- compromised account signal

## Incident Severity

Initial incident severity levels:

```text
INCIDENT_SEV_0_NOTICE
INCIDENT_SEV_1_LOW
INCIDENT_SEV_2_MEDIUM
INCIDENT_SEV_3_HIGH
INCIDENT_SEV_4_CRITICAL
```

| Severity | Meaning |
|---|---|
| SEV_0 Notice | Record only; no immediate harm detected |
| SEV_1 Low | Limited risk; review needed |
| SEV_2 Medium | Potential harm; containment may be needed |
| SEV_3 High | Likely harm or sensitive asset involved |
| SEV_4 Critical | Active breach, secret exposure, critical asset, or irreversible harm |

## Containment Actions

Initial containment actions:

```text
CONTAIN_FREEZE_EXPORT
CONTAIN_ISOLATE_SESSION
CONTAIN_REVOKE_TOKEN
CONTAIN_ROTATE_SECRET
CONTAIN_DISABLE_INTEGRATION
CONTAIN_DISABLE_TOOL_ACCESS
CONTAIN_LOCK_MODE
CONTAIN_PRESERVE_LOGS
CONTAIN_REQUIRE_REVIEW
CONTAIN_BLOCK_AUTOMATION
```

## CONTAIN_FREEZE_EXPORT

Use when:

- unauthorized egress is suspected
- bulk movement is abnormal
- sensitive export is attempted
- destination is unknown

Goal:

```text
Prevent further data or value escape.
```

## CONTAIN_ISOLATE_SESSION

Use when:

- account compromise is suspected
- session behavior is abnormal
- AI/tool session is behaving outside scope

Goal:

```text
Limit spread and preserve evidence.
```

## CONTAIN_REVOKE_TOKEN

Use when:

- token exposure is suspected
- unauthorized API use is detected
- token scope is excessive

Goal:

```text
Remove active access path.
```

## CONTAIN_ROTATE_SECRET

Use when:

- secret was exposed
- private key may be compromised
- credential reuse risk exists

Goal:

```text
Invalidate exposed trust material.
```

## CONTAIN_DISABLE_INTEGRATION

Use when:

- third-party connector behaves unexpectedly
- data-flow is unclear
- integration appears compromised

Goal:

```text
Stop uncertain external dependency.
```

## CONTAIN_DISABLE_TOOL_ACCESS

Use when:

- AI/tool access exceeds scope
- tool can export or execute unexpectedly
- tool is used in prohibited mode

Goal:

```text
Prevent capability misuse.
```

## CONTAIN_LOCK_MODE

Use when:

- mode boundary is violated
- system is drifting toward higher capability
- safe operating level is uncertain

Goal:

```text
Return system to safer mode.
```

## CONTAIN_PRESERVE_LOGS

Use when:

- incident review may be needed
- audit tampering is suspected
- decision chain must be reconstructed

Goal:

```text
Protect evidence integrity.
```

## CONTAIN_REQUIRE_REVIEW

Use when:

- system cannot determine safe continuation
- human accountability is required
- multiple recovery paths exist

Goal:

```text
Pause until accountable decision.
```

## CONTAIN_BLOCK_AUTOMATION

Use when:

- automated workflow may amplify harm
- AI agent continues unsafe path
- repeated unsafe action occurs

Goal:

```text
Stop repeated or autonomous harm.
```

## Rollback Requirements

Rollback should be defined before high-risk or irreversible action.

Rollback plan should identify:

- what can be reversed
- how reversal occurs
- who may approve rollback
- what data/state may be lost
- what audit evidence must be preserved
- how success is verified
- what remains unrecoverable

Default rule:

```text
No high-risk change without rollback path.
```

## Recovery Verification

Recovery is not complete until verified.

Verification should check:

- access revoked where required
- secrets rotated where required
- export stopped
- affected assets identified
- logs preserved
- mode restored
- risky capability disabled
- integrity checked
- remaining risk recorded
- owner notified where required

Default rule:

```text
Recovery requires verification, not assumption.
```

## Incident Review Flow

Suggested flow:

```text
Trigger detected
-> classify severity
-> contain if needed
-> preserve evidence
-> identify affected assets
-> identify actor/session/tool
-> assess egress/capability impact
-> revoke/rotate/disable if needed
-> review root cause
-> verify recovery
-> record lessons learned
```

## Evidence Preservation

Incident evidence may include:

- audit events
- access logs
- egress attempts
- AI prompts and outputs where allowed
- tool calls
- file diffs
- approvals
- denied actions
- stop states
- session metadata
- integration logs

Evidence preservation must respect privacy and legal boundaries.

Default rule:

```text
Preserve enough to investigate, not more than justified.
```

## Recovery And GDPR

If personal data is involved, recovery and incident handling may require:

- data impact assessment
- breach assessment
- minimization
- access restriction
- deletion or correction path
- notification review
- legal/compliance review

This document does not define legal obligations.

It only flags governance needs.

## Recovery And AI

AI-related incidents may involve:

- unsafe output
- prompt injection
- policy bypass attempt
- hidden instruction exposure
- unauthorized tool use
- AI autonomy drift
- incorrect confidence
- stale context use

Possible recovery actions:

- reset context
- disable tool access
- return to read-only mode
- require human review
- update governance source
- preserve prompt/output evidence where allowed

Default rule:

```text
AI incident recovery must include context and tool-boundary review.
```

## Recovery And Egress

Egress incidents may involve:

- data export
- secret exposure
- prompt leakage
- model context leakage
- external API transmission
- repository push containing sensitive content

Possible recovery actions:

- freeze export
- revoke external access
- rotate exposed secrets
- remove or restrict exposed material where possible
- notify owner
- preserve evidence
- review destination risk

Default rule:

```text
Egress incident response must focus on containment first.
```

## Recovery And Capability Change

Capability-change incidents may involve:

- new tool access
- network enablement
- automation added
- mode advancement
- write access granted
- execution enabled
- AI autonomy increased

Possible recovery actions:

- disable new capability
- revert configuration
- revoke permissions
- restore previous mode
- review approval chain
- verify no further capability remains

Default rule:

```text
Unsafe capability change must be revocable.
```

## Emergency Override

Emergency override may be needed in rare cases.

Emergency override must still require:

- accountable actor
- reason
- scope
- time limit
- audit event
- post-review
- rollback or recovery plan

Default rule:

```text
Emergency does not remove accountability.
```

## Return To Normal

Return to normal operation should require:

- incident reviewed
- containment complete
- recovery verified
- residual risk documented
- required notifications considered
- affected controls restored
- owner approval where required

Default rule:

```text
No return to normal without review.
```

## Initial Incident-To-Response Matrix

| Incident Trigger | Default Response |
|---|---|
| Secret exposure | Block, rotate, incident review |
| Unauthorized export | Freeze export, preserve logs, review |
| Suspicious bulk movement | Freeze export, session review |
| AI self-escalation | Block, disable capability, review |
| Mode violation | Lock mode, review |
| Capability change without gate | Disable capability, review |
| Stale authority used for high-risk action | Block, refresh authority, review |
| Audit tampering suspected | Preserve logs, incident review |
| Irreversible action without rollback | Stop, incident review |
| Integration behaving unexpectedly | Disable integration, review |

## Open Questions

1. Which incidents require immediate lockdown?
2. Which incidents require legal/compliance review?
3. Which incidents require notification?
4. Which recovery actions can be automated safely?
5. Which recovery actions require human approval?
6. How should audit evidence be preserved without overcollecting personal data?
7. What is the minimal incident schema for version 0?
8. How should AI prompts/outputs be handled as incident evidence?
9. How should repository pushes be recovered if sensitive material leaks?
10. What recovery controls require external security review?
