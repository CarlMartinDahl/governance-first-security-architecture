# Governance-First Security Architecture

## GDPR EU AI Act Alignment v0.1

## Status

This document is a preparatory GDPR and EU AI Act alignment document for the Governance-First Security Architecture concept.

It is documentation-only.

It is not legal advice.

It is not a compliance assessment.

It is not a claim of GDPR compliance.

It is not a claim of EU AI Act compliance.

It is intended to map the architecture's governance ideas to GDPR and EU AI Act alignment goals before any build phase begins.

## Source Basis

Source baseline last reviewed:

```text
2026-08-15
```

This document is based on high-level alignment with:

- GDPR personal data processing principles, including lawfulness, fairness, transparency, purpose limitation, data minimisation, storage limitation, accuracy, integrity/confidentiality, and accountability.
- EU AI Act governance concepts, including risk-based AI governance, prohibited/high-risk/limited/minimal risk framing, transparency, human oversight, documentation, and risk management.

This document should be reviewed by qualified legal/compliance professionals before being used for any compliance purpose.

Primary review sources:

- [Regulation (EU) 2016/679 (GDPR)](https://eur-lex.europa.eu/eli/reg/2016/679/oj)
- [Regulation (EU) 2024/1689 (AI Act)](https://eur-lex.europa.eu/eli/reg/2024/1689/oj?locale=en)
- [European Commission AI Act implementation overview](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)

## Current AI Act Timing Boundary

As of the source-review date:

- prohibited-practice and AI-literacy provisions have begun applying,
- governance and general-purpose AI obligations have begun applying,
- transparency obligations apply from August 2026,
- high-risk system timelines differ by category and have been affected by later implementation changes.

The applicable date, role, system category, and obligation must be re-verified against current primary sources for each actual use case. This document does not determine legal applicability.

## Purpose

The purpose of this document is to answer:

```text
How should the architecture prepare for GDPR alignment?
How should it prepare for EU AI Act alignment?
Which governance controls support compliance-oriented review?
Which claims must not be made yet?
Where is legal/compliance expertise required?
```

## Core Position

The architecture should not claim compliance by design.

It should instead create traceable controls that can support future compliance assessment.

Core rule:

```text
Alignment is not compliance.
Documentation is not certification.
Governance support is not legal approval.
```

## GDPR Alignment Goals

### 1. Lawfulness, Fairness, And Transparency

Governance goal:

Personal data processing should not occur unless the system can identify a valid purpose and authority basis for the processing.

Architecture support:

- lawful purpose check
- actor/role accountability
- audit trail
- transparency record
- human review for high-risk processing

Policy expression:

```text
No lawful purpose, no processing.
```

### 2. Purpose Limitation

Governance goal:

Data should be used only for defined and legitimate purposes.

Architecture support:

- purpose field in action requests
- purpose validation before export
- block processing when purpose is missing
- audit record of purpose
- review when purpose changes

Policy expression:

```text
No purpose drift without review.
```

### 3. Data Minimisation

Governance goal:

The system should use only the data necessary for the defined purpose.

Architecture support:

- asset classification
- minimisation check
- redaction review
- restricted egress
- least-data-needed principle

Policy expression:

```text
No unnecessary data, no collection.
```

### 4. Storage Limitation

Governance goal:

Data should not be retained longer than needed for its valid purpose.

Architecture support:

- retention policy fields
- audit retention classification
- incident evidence retention review
- deletion or archival workflow in future versions

Policy expression:

```text
No retention without purpose.
```

### 5. Accuracy

Governance goal:

Data and conclusions should not be treated as valid if source quality, freshness, or correctness is unclear.

Architecture support:

- source freshness check
- staleness detection
- evidence sufficiency
- counter-evidence preservation
- correction path in future versions

Policy expression:

```text
No stale authority as current authority.
```

### 6. Integrity And Confidentiality

Governance goal:

Personal and sensitive data should be protected against unauthorized access, alteration, loss, and export.

Architecture support:

- ingress controls
- egress controls
- secret blocking
- restricted asset handling
- audit trail
- incident response

Policy expression:

```text
No unauthorized exit.
```

### 7. Accountability

Governance goal:

The system should preserve evidence of who did what, why, under which authority, and with which safeguards.

Architecture support:

- audit event classes
- approval records
- review records
- stop-state records
- evidence traceability
- accountability roles

Policy expression:

```text
No audit trail, no trusted decision.
```

## GDPR Risk Areas Requiring Legal Review

Legal/compliance review is required before defining:

- lawful bases for processing
- special category data handling
- retention periods
- data subject rights workflows
- automated decision-making implications
- DPIA requirements
- breach notification requirements
- international transfers
- controller/processor roles

This architecture must not decide those legal questions by itself.

## EU AI Act Alignment Goals

### 1. Risk-Based AI Governance

Governance goal:

AI systems and AI-assisted workflows should be classified by risk and handled according to their potential impact.

Architecture support:

- risk and action taxonomy
- mode ladder
- capability-change gate
- human review for high-risk action
- stop states

Policy expression:

```text
No high-risk AI without human accountability.
```

### 2. Human Oversight

Governance goal:

High-risk AI-supported action should not proceed without meaningful human oversight where required.

Architecture support:

- human review versus approval distinction
- accountable approver
- override audit
- AI refusal explanation
- shared context ledger

Policy expression:

```text
AI may propose. Governance must decide.
```

### 3. Transparency And Traceability

Governance goal:

AI involvement should be traceable, and AI-generated or AI-assisted outputs should not be confused with human-authorized decisions.

Architecture support:

- AI assistance audit event
- non-authorization labels
- source references
- uncertainty marking
- decision chain record

Policy expression:

```text
AI recommendation is not authorization.
```

### 4. Technical Documentation And Record-Keeping

Governance goal:

AI-supported systems should preserve documentation and logs that make governance review possible.

Architecture support:

- audit and accountability policy
- decision events
- source/evidence records
- review/approval chain
- stop-state records
- capability-change records

Policy expression:

```text
No governance change without trace.
```

### 5. Accuracy, Robustness, And Security-Oriented Controls

Governance goal:

AI-supported outputs should not be treated as reliable without evidence, uncertainty handling, and security boundaries.

Architecture support:

- evidence sufficiency
- source authority/staleness review
- fail-closed stop states
- ingress/egress controls
- AI tool boundary restrictions
- recovery and incident handling

Policy expression:

```text
No certainty, no execution.
```

### 6. Prohibited Or Restricted Use Awareness

Governance goal:

The architecture should be able to block or escalate AI uses that may be prohibited, restricted, or high-risk under applicable law.

Architecture support:

- prohibited action classes in future versions
- risk classification
- human/legal review gate
- stop state for unclear legal basis

Policy expression:

```text
No legally unclear high-risk AI path without review.
```

## EU AI Act Risk Areas Requiring Specialist Review

AI governance/legal review is required before defining:

- whether a use case is prohibited, high-risk, limited-risk, or minimal-risk
- provider versus deployer responsibilities
- conformity assessment implications
- required technical documentation
- human oversight requirements
- post-market monitoring
- transparency duties
- GPAI-related duties where relevant
- biometric, employment, education, law enforcement, or critical infrastructure use cases

This architecture must not classify regulated AI use cases without expert review.

## Alignment Matrix

| Architecture Control | GDPR Alignment Goal | EU AI Act Alignment Goal |
|---|---|---|
| Lawful purpose check | Lawfulness, purpose limitation | Use-case governance |
| Data minimisation | Data minimisation | Risk reduction |
| Egress control | Integrity/confidentiality | Security and misuse prevention |
| Evidence sufficiency | Accuracy/accountability | Accuracy and robustness |
| Audit trail | Accountability | Record-keeping |
| Human review/approval | Accountability | Human oversight |
| Mode ladder | Risk limitation | Risk-based governance |
| Capability-change gate | Security/accountability | Lifecycle risk control |
| Stop states | Integrity/accountability | Risk mitigation |
| Recovery/incident handling | Security and breach readiness | Monitoring and response support |

## Must-Not-Claim Statements

The following claims must not be made at this stage:

```text
This model is GDPR compliant.
This model is EU AI Act compliant.
This model satisfies legal obligations.
This model replaces legal review.
This model replaces security review.
This model is production-ready.
This model is certified.
This model guarantees safe AI.
```

Allowed language:

```text
This model is designed with GDPR alignment goals.
This model is designed with EU AI Act alignment goals.
This model preserves evidence for future compliance review.
This model requires legal/compliance review before compliance claims.
```

## Compliance-Oriented Evidence To Preserve

Future versions should preserve:

- purpose of processing
- lawful basis review reference where applicable
- data categories
- asset sensitivity
- AI involvement
- human review/approval
- risk classification
- source/evidence basis
- decision outcome
- stop state if blocked
- egress attempt or export
- retention classification
- incident handling if applicable

## Open Questions

1. Which initial use case should be mapped to GDPR first?
2. Which initial use case should be mapped to EU AI Act first?
3. What legal expertise is required before deeper mapping?
4. What compliance claims must be explicitly prohibited?
5. Which personal data categories should be out of scope for early versions?
6. Which AI use cases should be out of scope for early versions?
7. How should human oversight be documented?
8. How should AI-generated output be labeled?
9. How should records be retained without overcollecting personal data?
10. When is a DPIA-like review required?

## References For Review

- Regulation (EU) 2016/679, including personal-data processing and accountability principles.
- Regulation (EU) 2024/1689, including risk, human-oversight, transparency, documentation, and governance provisions.
- European Commission AI Act implementation guidance and current application timeline.

These references must be scoped to the selected use case and expanded with formal legal citations during external legal/compliance review.
