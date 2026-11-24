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
2026-11-24
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

Under Regulation (EU) 2024/1689 (Art. 113) as of `2026-11-24`:

- **2 February 2025 (currently applicable):** Chapter I & II — **Art. 4** (AI literacy for providers and deployers) and **Art. 5** (prohibited AI practices).
- **2 August 2025 (currently applicable):** Chapter V (**Arts. 51–56** GPAI model obligations) and Chapter VII governance and penalty provisions.
- **2 August 2026 (currently applicable):** General application of the Act, including **Art. 50** (external transparency obligations) and **Annex III high-risk AI obligations** (including **Art. 12/19/26(6)** 6-month minimum operational log retention, **Art. 14** human oversight, **Art. 18(1)** 10-year provider compliance documentation, **Art. 25** deployer-to-provider reclassification, **Art. 26** deployer duties, **Art. 27** Fundamental Rights Impact Assessments (FRIA), and **Art. 73** serious incident reporting).
- **2 August 2027:** High-risk AI systems embedded as safety components in Annex I harmonized product legislation (Art. 113(c)).

The applicable date, role (provider vs. deployer), system category, and any subsequently enacted Official Journal amendments must be re-verified against current primary legal sources for each actual use case by qualified counsel. This document does not determine legal applicability.

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

Personal data processing must not occur unless **both** a specified, explicit, legitimate purpose (**GDPR Art. 5(1)(b)**) **and** a valid statutory lawful basis (**GDPR Art. 6(1)**, plus an **Art. 9(2)** condition for special category data) have been documented and verified prior to processing, with transparent Arts. 13–14 notices to data subjects.

Architecture support:

- documented lawful-basis and purpose-limitation check (`STOP_LAWFUL_BASIS_MISSING` when absent)
- actor/role accountability and statutory DPO consultation boundary (GDPR Arts. 37–39)
- privacy-minimised audit trail
- transparency notice reference
- human review and contestability for automated decisions with legal or similarly significant effects (GDPR Art. 22)

Policy expression:

```text
No documented GDPR lawful basis and specified purpose, no personal-data processing.
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

### 2. Human Oversight & Automated Decision-Making (EU AI Act Art. 14 & GDPR Art. 22)

Governance goal:

High-risk AI-supported action must not proceed without meaningful human oversight where required, and automated decisions producing legal or similarly significant effects on natural persons must satisfy **GDPR Art. 22** safeguards.

Architecture support:

- human review versus approval distinction (preventing *SCHUFA*-style rubber-stamping under CJEU Case C-634/21 by requiring meaningful human competence, authority, independent evidence, and time to overturn AI output)
- anti-automation-bias controls (**EU AI Act Art. 14(4)(b)**): surfacing uncertainty and counter-evidence prominently, tracking human-override rates, and prohibiting pre-filled approval defaults
- contestability and human-redress path (**GDPR Art. 22(3)** & Arts. 13(2)(f)/15(1)(h)) where deterministic or AI-assisted controls (including automated suspensions) produce legal or similarly significant effects on individuals
- accountable approver, override audit, AI refusal explanation, and shared context ledger

Policy expression:

```text
AI may propose. Meaningful, non-rubber-stamped human governance must decide where legally or risk-required.
```

### 3. Transparency And Traceability (EU AI Act Art. 50)

Governance goal:

AI involvement must be traceable internally **and** disclosed externally to affected natural persons where required under **EU AI Act Art. 50** (human-AI interaction notice under Art. 50(1), machine-readable marking of synthetic content under Art. 50(2), emotion/biometric notice under Art. 50(3), and deepfake/public-interest text disclosure under Art. 50(4)).

Architecture support:

- internal AI assistance audit event and non-authorization labels
- external user-facing AI interaction and synthetic-content disclosure check (`Art. 50`)
- source references, uncertainty marking, and decision chain record

Policy expression:

```text
AI recommendation is not authorization, and external AI interaction must be transparently disclosed where legally required.
```

### 4. Technical Documentation, AI Literacy And Record-Keeping (Arts. 4, 11, 12, 18, 19, 26, 27, 73)

Governance goal:

AI-supported systems should preserve privacy-minimised documentation and logs that support compliance review, while respecting distinct statutory retention duties (**Arts. 19(1)/26(6)**: minimum 6 months for operational logs, subject to GDPR; **Art. 18(1)**: 10 years for provider technical/QMS/conformity documentation), **Art. 4** AI literacy, **Art. 27** Fundamental Rights Impact Assessments (FRIA) where applicable, and **Art. 73** serious-incident reporting (2 / 10 / 15 days).

Architecture support:

- audit and accountability policy with GDPR Art. 5(1)(e) retention ceilings and payload separation
- decision events, source/evidence records, review/approval chain, stop-state records
- capability-change records including **Art. 25 deployer-to-provider reclassification check** (fine-tuning, substantial modification, rebranding, or repurposing into high-risk)
- `STOP_DPIA_OR_FRIA_REQUIRED` gate before deploying high-risk processing

Policy expression:

```text
No governance or capability change without trace, literacy readiness, and statutory impact review.
```

### 5. Accuracy, Robustness, And Security-Oriented Controls

Governance goal:

AI-supported outputs should not be treated as reliable without verified evidence sufficiency, bounded uncertainty handling, and security boundaries.

Architecture support:

- evidence sufficiency and source authority/staleness review
- fail-closed stop states
- ingress/egress controls
- AI tool boundary restrictions
- recovery and incident handling

Policy expression:

```text
No verified evidence sufficiency and bounded uncertainty, no execution.
```

### 6. Prohibited Or Restricted Use Gate (EU AI Act Art. 5 — Currently Binding)

Governance goal:

The architecture must block AI uses that fall within **EU AI Act Art. 5** prohibited practices (binding since 2 February 2025, e.g., workplace emotion inference under Art. 5(1)(f), social scoring, manipulative exploitation) or lack a verified GDPR lawful basis.

Architecture support:

- canonical `STOP_PROHIBITED_AI_USE` stop state (`BLOCK`, or `INCIDENT_RESPONSE` if already deployed)
- canonical `STOP_LAWFUL_BASIS_MISSING` and `STOP_UNAPPROVED_CROSS_BORDER_TRANSFER` stop states
- mandatory pre-deployment legal/privacy review gate and statutory DPO consultation boundary (GDPR Arts. 37–39)

Policy expression:

```text
Prohibited AI practices and legally unsupported processing are hard-blocked before execution.
```

## EU AI Act Risk Areas Requiring Specialist Review

AI governance/legal review (with statutory DPO consultation where personal data is involved) is required before defining:

- whether a use case is prohibited (Art. 5), high-risk (Annex I / Annex III, including Annex III(4)(b) workplace monitoring), limited-risk (Art. 50), or minimal-risk
- provider versus deployer responsibilities and **Art. 25** reclassification triggers (fine-tuning, substantial modification, rebranding)
- conformity assessment, CE marking, and **Art. 18(1)** 10-year provider documentation vs. **Arts. 19(1)/26(6)** 6-month operational log retention
- **Art. 4** AI literacy training obligations
- **Art. 14** human oversight & automation-bias controls and **GDPR Art. 22** automated decision-making / contestability
- **Art. 27** Fundamental Rights Impact Assessments (FRIA) and **GDPR Art. 35/36** DPIAs / prior consultation
- **Art. 50** external transparency and synthetic-content marking duties
- **Art. 73** serious-incident reporting (2 / 10 / 15 days) and post-market monitoring
- GPAI-related duties (Arts. 51–56) where relevant

This architecture must not classify regulated AI use cases without expert review.

## Alignment Matrix

| Architecture Control | GDPR Alignment Goal | EU AI Act Alignment Goal |
|---|---|---|
| Lawful basis & purpose check (`STOP_LAWFUL_BASIS_MISSING`) | Art. 5(1)(b), Art. 6(1), Art. 9(2) | Use-case governance |
| Data minimisation & payload separation | Art. 5(1)(c), Art. 5(1)(e), Art. 17 | Privacy-safe logging (Arts. 12/19/26(6)) |
| Egress & transfer control (`STOP_UNAPPROVED_CROSS_BORDER_TRANSFER`) | Art. 32, Chapter V (*Schrems II* TIA) | Security and misuse prevention (Art. 15) |
| Evidence sufficiency & uncertainty marking | Art. 5(1)(d) accuracy / accountability | Accuracy and robustness (Art. 15) |
| Audit trail & retention ceilings | Art. 5(2) accountability | Record-keeping (Arts. 12, 18, 19, 26(6)) |
| Human review/approval & anti-rubber-stamping | Art. 22 safeguards & contestability | Human oversight & Art. 14(4)(b) |
| External AI disclosure | Arts. 13–14 transparency | Art. 50 transparency & synthetic marking |
| Capability-change gate & Art. 25 check | Art. 25 privacy by design | Provider reclassification & lifecycle control |
| Prohibited-use & impact gates (`STOP_PROHIBITED_AI_USE`, `STOP_DPIA_OR_FRIA_REQUIRED`) | Arts. 35–36 DPIA / prior consultation | Art. 5 prohibited practices & Art. 27 FRIA |
| Recovery/incident handling | Arts. 33–34 breach readiness | Art. 73 serious incident reporting |

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

- purpose of processing and statutory GDPR lawful basis reference (Art. 6(1) / Art. 9(2))
- DPIA (GDPR Art. 35) / FRIA (EU AI Act Art. 27) and DPO consultation reference where applicable
- data categories, asset sensitivity, and Chapter V transfer / TIA reference
- AI involvement, Art. 50 disclosure status, and Art. 25 provider/deployer classification
- human review/approval (including anti-automation-bias check and override record)
- risk classification and source/evidence basis
- decision outcome and canonical stop state if blocked
- egress attempt or export
- retention ceiling classification and legal-hold status
- incident handling and statutory notification assessment (GDPR Arts. 33–34, NIS2 Art. 23, AI Act Art. 73)

## Open Questions

1. Which initial use case should be mapped to GDPR first?
2. Which initial use case should be mapped to EU AI Act first?
3. What legal expertise is required before deeper mapping?
4. What compliance claims must be explicitly prohibited?
5. Which personal data categories should be out of scope for early versions?
6. Which AI use cases should be out of scope for early versions?
7. How should meaningful human oversight (preventing Art. 22 rubber-stamping and Art. 14(4)(b) automation bias) be documented?
8. How should AI-generated output and user interactions be disclosed under Art. 50?
9. How should records be retained via WORM metadata + separated/erasable personal-data payloads without violating Art. 5(1)(e) or Art. 17?
10. When are a statutory **GDPR Art. 35 DPIA** (including Art. 36 prior consultation) and an **EU AI Act Art. 27 FRIA** mandatory for the target workflow?

## References For Review

- Regulation (EU) 2016/679, including personal-data processing and accountability principles.
- Regulation (EU) 2024/1689, including risk, human-oversight, transparency, documentation, and governance provisions.
- European Commission AI Act implementation guidance and current application timeline.

These references must be scoped to the selected use case and expanded with formal legal citations during external legal/compliance review.
