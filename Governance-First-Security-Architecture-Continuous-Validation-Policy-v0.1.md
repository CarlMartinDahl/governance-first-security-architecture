# Governance-First Security Architecture

## Continuous Validation Policy v0.1

## Status

This document is a preparatory continuous validation policy for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a zero-trust architecture specification.

It is not a security claim.

It is intended to define that a legitimately established session, credential, or access grant does not remain valid indefinitely, and that trust must be revalidated continuously rather than assumed from initial authentication.

## Purpose

The purpose of this document is to answer:

```text
What does it mean that a session is currently legitimate?
How often must trust be revalidated?
What signals trigger revalidation outside the normal schedule?
What happens when revalidation fails or cannot be completed?
How does continuous validation interact with stop states?
How must the governance model respond to agentic and automated actors who do not operate at human speed?
```

## Governing Principle

Initial authentication is not ongoing authorisation.

A session that was legitimate at 09:00 may not be legitimate at 09:15 if context has changed.

The question the governance model must ask continuously is not only who authenticated, but whether the current behaviour is consistent with the authority that was originally granted.

## What Continuous Validation Covers

Continuous validation applies to:

- human user sessions
- third-party and supplier sessions
- service and system sessions
- AI agent sessions and tool use
- API and integration connections
- administrative and privileged sessions

## Validation Dimensions

For each active session or connection, the following dimensions are continuously assessed:

```text
Identity consistency:
  Is the session behaving in a manner consistent with the identity that authenticated?
  Has the source, device, location, or timing changed in a way that was not anticipated?

Scope consistency:
  Is the session accessing only the resources it was authorised to access?
  Has the session attempted access outside its defined scope?

Behavioural consistency:
  Is the volume, pattern, and timing of requests consistent with the session's normal profile?
  Are there signs of automated, scaled, or agentic behaviour in a session established by a human?

Context consistency:
  Has the organisational or security context changed since the session was established?
  Is there an active incident or lockdown that should affect this session's continued validity?
```

## Revalidation Schedule

All sessions are subject to revalidation at a defined maximum interval.

Revalidation intervals are shorter for higher-risk session classes:

| Session class | Maximum revalidation interval |
|---|---|
| Administrative and privileged | Short interval, defined per implementation |
| Third-party and supplier | Medium interval, defined per third-party governance record |
| AI agent and automated system | Continuous, per action or at short fixed interval |
| Standard human user | Standard interval, defined per role |
| Read-only and low-privilege | Extended interval, defined per risk classification |

Specific interval values are not defined in this document. They are defined during implementation review and governed by the capability change gate before any interval is extended.

## Event-Triggered Revalidation

Revalidation is triggered immediately on any of the following signals, regardless of scheduled interval:

- anomalous access volume or pattern detected
- access to a resource outside the session's defined scope attempted
- source, device, or network context changes unexpectedly
- active security incident is declared
- third-party compromise is suspected or confirmed
- stop state is triggered in any adjacent system
- AI agent attempts a capability or action outside its defined boundary
- privileged action attempted outside a defined maintenance window

## Revalidation Outcomes

Revalidation results in one of the following outcomes:

```text
SESSION_CONFIRMED:
  Validation signals are consistent.
  Session continues without interruption.
  Outcome is logged.

SESSION_STEP_UP_REQUIRED:
  Validation signals are borderline or insufficient.
  Additional authentication factor required before session continues.
  Session is suspended until step-up is completed.

SESSION_SUSPENDED:
  Validation signals are anomalous but not conclusive.
  Session is suspended pending human review.
  Triggers HUMAN_REVIEW_REQUIRED.

SESSION_TERMINATED:
  Validation signals indicate compromise, scope violation, or governance breach.
  Session is terminated immediately.
  Triggers INCIDENT_REVIEW_REQUIRED.
  All session actions since last confirmed validation are reviewed.
```

## Agentic And Automated Actor Validation

Agentic AI systems, automation, and high-volume actors require a distinct approach because they do not operate at human speed and can cause disproportionate harm within a single session if validation is only point-in-time.

For agentic and automated actors:

- validation is per-action or per-batch, not per-session
- any single action outside the actor's defined capability boundary triggers immediate stop
- volume anomaly is a first-class validation signal, not a secondary check
- the actor cannot self-extend its session, scope, or capability
- stop states for agentic actors do not require human approval before triggering

This is the governance response to the threat described in Supply Chain Abuse Case SC-004.

## Fail-Closed Default

If revalidation cannot be completed because the validation mechanism is unavailable, degraded, or under attack:

```text
Default outcome: SESSION_SUSPENDED

Sessions are not continued on the assumption that validation would have succeeded.
Access is restored only after validation is confirmed operational and revalidation is completed.
```

A validation outage is treated as a potential attack signal, not as a technical inconvenience.

## Relationship To Other Modules

- Identity And Credential Governance: continuous validation operates on top of the credential lifecycle
- Third-Party Governance: third-party sessions are subject to this policy's validation requirements
- Supply Chain Abuse Cases: SC-001 and SC-004 are directly addressed by this module
- Stop-State Registry: SESSION_TERMINATED triggers defined stop states
- Ingress Egress Policy: sessions that fail revalidation are fail-closed at all egress points
- Audit And Accountability: all revalidation events and outcomes are subject to audit requirements
- AI-Human Governance: agentic actor validation rules interact with AI capability boundaries

## Open Questions

1. Should revalidation intervals be defined in this document or deferred entirely to implementation review?
2. How should continuous validation interact with legitimate high-volume business processes that may trigger volume anomaly signals?
3. Should a validation outage automatically trigger a governance stop state or only a review?
4. What is the minimum acceptable step-up authentication factor for each session class?
5. How should continuous validation be tested without disrupting legitimate operations?
6. Should agentic actor stop states ever require human approval before triggering, and under what conditions?
7. How does this policy interact with existing session management in identity providers or SSO systems?
