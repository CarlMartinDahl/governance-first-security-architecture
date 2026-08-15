# Governance-First Security Architecture

## Asset Register v0.1

## Status

This document is a preparatory asset register for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a complete data inventory.

It is not a legal or security claim.

It is intended to identify the first asset categories the architecture must protect before risk, action, trust-boundary, and control models are finalized.

## Purpose

The purpose of this asset register is to answer:

```text
What must the architecture protect?
Why does it matter?
What can go wrong if it is exposed, changed, copied, misused, or exported?
Which governance controls should apply?
```

## Asset Classification Principles

Every protected asset should eventually have:

- owner
- purpose
- sensitivity level
- allowed users or roles
- allowed actions
- allowed export paths
- retention rule
- audit requirement
- recovery requirement
- mode restrictions
- capability-change implications

This v0.1 document defines categories only.

It does not assign real owners, systems, or production controls.

## Sensitivity Levels

Initial sensitivity levels:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
RESTRICTED
CRITICAL
BLOCKED_FROM_EXPORT
```

Suggested meaning:

| Level | Meaning |
|---|---|
| PUBLIC | Can be shared publicly if accurate and approved |
| INTERNAL | Internal use only |
| CONFIDENTIAL | Harmful if exposed |
| RESTRICTED | Strong access and review required |
| CRITICAL | High-impact asset requiring strict controls |
| BLOCKED_FROM_EXPORT | Must not leave approved boundary except under exceptional review |

## Asset Category 1: Personal Data

Examples:

- names
- contact details
- identification data
- account data
- user behavior data
- sensitive personal data
- metadata linked to individuals

Why it matters:

- GDPR relevance
- privacy harm
- identity misuse
- reputational harm
- legal/regulatory exposure

Required governance controls:

- lawful purpose check
- purpose limitation
- data minimization
- access control
- export control
- retention control
- audit trail
- incident path

Default posture:

```text
No lawful purpose, no processing.
No unnecessary data, no collection.
No unauthorized exit.
```

## Asset Category 2: Legal Or Regulated Material

Examples:

- legal documents
- contracts
- case records
- compliance records
- evidence files
- regulated business documents
- legal analysis outputs

Why it matters:

- confidentiality
- professional review requirements
- source integrity
- legal harm from incorrect output
- misuse of non-authoritative conclusions

Required governance controls:

- source authority check
- evidence sufficiency check
- human review for sensitive conclusions
- audit trail
- non-authorization labels
- no unsupported claims

Default posture:

```text
No source, no conclusion.
No certainty, no claim.
No approval, no escalation.
```

## Asset Category 3: Credentials, Secrets, And Keys

Examples:

- API keys
- access tokens
- refresh tokens
- private keys
- signing keys
- session tokens
- passwords
- service account credentials

Why it matters:

- direct system compromise
- unauthorized access
- privilege escalation
- data theft
- long-term breach risk

Required governance controls:

- blocked export by default
- secret detection
- vaulting or protected storage
- rotation path
- audit on access
- least privilege
- incident response

Default posture:

```text
Secrets do not leave approved boundaries.
Token exposure triggers incident path.
```

## Asset Category 4: AI System Instructions And Context

Examples:

- system prompts
- governance instructions
- agent rules
- local steering files
- model-specific constraints
- chain-of-work context
- policy memory
- task history

Why it matters:

- prompt leakage
- policy bypass
- stale instruction misuse
- unauthorized behavior modification
- AI control failure

Required governance controls:

- source freshness check
- authority hierarchy
- stale-reference detection
- no hidden objective
- no unauthorized instruction override
- audit of instruction changes

Default posture:

```text
No stale authority as current authority.
No hidden objective.
No instruction override without governance.
```

## Asset Category 5: Decision Authority

Examples:

- approvals
- review decisions
- release decisions
- escalation decisions
- risk classifications
- stop-state decisions
- incident decisions
- mode advancement decisions

Why it matters:

- determines what the system may do
- can authorize high-impact actions
- can be abused to bypass controls
- can create false accountability if unclear

Required governance controls:

- role validation
- decision type classification
- approval path
- human accountability
- audit trail
- non-repudiation where appropriate
- clear distinction between review and authorization

Default posture:

```text
No authority, no action.
No approval, no escalation.
Documentation is not authorization.
```

## Asset Category 6: Audit Trail And Evidence Records

Examples:

- access logs
- decision events
- source references
- approval records
- denial records
- incident records
- rollback records
- reviewer notes
- evidence sufficiency records

Why it matters:

- accountability
- forensic investigation
- compliance review
- dispute resolution
- detection of policy drift

Required governance controls:

- tamper resistance
- retention policy
- access control
- chain of custody where needed
- reviewability
- incident preservation

Default posture:

```text
No audit trail, no trusted decision.
```

## Asset Category 7: Models, Prompts, And Governance Logic

Examples:

- model configurations
- prompt templates
- governance rules
- decision policies
- scoring policies
- classifiers
- validators
- test policies

Why it matters:

- may encode business logic
- may expose security design
- may be used to bypass controls
- may be manipulated to change system behavior

Required governance controls:

- versioning
- source authority
- change review
- capability-change assessment
- no unreviewed deployment
- audit trail

Default posture:

```text
No capability change without gate.
No unreviewed governance logic change.
```

## Asset Category 8: System Capabilities

Examples:

- read access
- write access
- delete access
- export access
- network access
- execution access
- automation access
- integration access
- admin access

Why it matters:

- capability determines potential impact
- small changes may create large risk
- automation can amplify mistakes
- external connectivity can create egress paths

Required governance controls:

- mode ladder
- capability-change gate
- least privilege
- explicit approval
- test before expansion
- rollback path

Default posture:

```text
Analysis is not execution.
Read-only is not write-capable.
Internal access is not export permission.
```

## Asset Category 9: External Integrations And Connectors

Examples:

- APIs
- plugins
- data connectors
- cloud services
- identity providers
- logging services
- AI tools
- third-party systems

Why it matters:

- supply-chain risk
- data leakage
- permission expansion
- hidden external processing
- dependency compromise

Required governance controls:

- integration approval
- data flow review
- permission review
- logging
- vendor/security review where appropriate
- egress mapping

Default posture:

```text
No external integration without data-flow and authority review.
```

## Asset Category 10: Recovery And Control Mechanisms

Examples:

- rollback tools
- backup records
- key rotation procedures
- incident response playbooks
- freeze controls
- isolation controls
- revocation paths

Why it matters:

- recovery determines breach impact
- rollback reduces irreversibility
- incident response must be fast and accountable
- attackers may target recovery paths

Required governance controls:

- restricted access
- tested procedures
- audit trail
- emergency authorization model
- integrity protection

Default posture:

```text
No irreversible action without rollback.
No recovery control without access governance.
```

## Asset Category 11: Cryptographic Trust Material

Examples:

- certificates
- key algorithms
- signing policies
- encryption configuration
- trust stores
- algorithm migration plans

Why it matters:

- cryptographic assumptions can expire
- quantum-capable attackers may affect long-term trust
- weak algorithms can undermine system integrity

Required governance controls:

- crypto inventory
- algorithm agility
- post-quantum migration plan
- certificate lifecycle management
- trust review

Default posture:

```text
No long-term trust without crypto-agility.
```

## Asset Category 12: Human Attention And Approval Capacity

Examples:

- reviewer time
- approval attention
- security analyst attention
- incident response focus
- decision fatigue capacity

Why it matters:

- overloaded humans approve too much
- false positives reduce trust
- approval fatigue weakens governance
- unclear review burden causes bypass behavior

Required governance controls:

- risk-tiered review
- escalation filtering
- concise evidence presentation
- critical-only multi-review
- alert fatigue control

Default posture:

```text
Human review must be meaningful, not mechanical.
```

## Initial Egress Posture

Some assets should default to blocked export:

```text
credentials
private keys
session tokens
restricted personal data
privileged governance instructions
unredacted sensitive logs
security control internals
recovery mechanisms
unapproved model/system prompts
```

Other assets may be exportable only after review:

```text
legal material
regulated documents
audit extracts
risk assessments
security architecture documents
AI-generated high-risk recommendations
```

## Initial Asset-To-Control Matrix

| Asset Category | Default Control |
|---|---|
| Personal data | Lawful purpose + minimization + audit |
| Secrets/keys | Blocked export + incident on exposure |
| AI instructions/context | Authority + stale-reference control |
| Decision authority | Role validation + audit |
| Audit trail | Integrity + retention + restricted access |
| System capability | Mode ladder + capability gate |
| External integrations | Data-flow review + approval |
| Recovery mechanisms | Restricted access + tested rollback |
| Cryptographic trust | Crypto-agility + lifecycle review |
| Human attention | Risk-tiered review |

## Open Questions

1. Which asset category should be protected first in a minimal prototype?
2. Which assets should be `BLOCKED_FROM_EXPORT` by default?
3. Which assets require legal/compliance review?
4. Which assets require security expert review?
5. Which assets require owner assignment before implementation?
6. What retention rules are needed?
7. What audit events are required per asset type?
8. How should AI-generated outputs be classified?
9. How should prompts and governance instructions be classified?
10. Which assets need post-quantum readiness tracking?
