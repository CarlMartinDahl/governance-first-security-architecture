# Governance-First Security Architecture - Asset-To-Kernel Mapping v0.1

## Status

Preparatory documentation.

This document is not an implementation.

This document is not a complete data inventory.

This document maps asset categories to the minimal governance kernel for future review and prototype design.

## Purpose

The purpose of this document is to connect what the architecture protects to how the governance kernel should react.

The Asset Register identifies important asset categories.

The Minimal Viable Governance Kernel defines the minimum decision controls.

This mapping connects them.

For each asset category, this document defines:

- default risk level,
- default egress class,
- required reviewer,
- likely stop states,
- audit requirement,
- recovery requirement,
- prototype handling.

## Core Principle

```text
An asset is not protected until it has a risk level, egress rule, reviewer, stop path, audit path, and recovery path.
```

## Mapping Legend

### Risk Levels

- `LOW`
- `MEDIUM`
- `HIGH`
- `CRITICAL`

### Egress Classes

- `NO_EGRESS`
- `PUBLIC_SAFE`
- `INTERNAL_ONLY`
- `SENSITIVE`
- `SECRET`
- `REGULATED`
- `BLOCKED`

### Prototype Handling

- `SYNTHETIC_ONLY`
- `REDACTED_ONLY`
- `MOCK_ONLY`
- `REVIEW_ONLY`
- `OUT_OF_SCOPE`

## Asset Category 1 - Personal Data

Default risk level:

```text
HIGH
```

Default egress class:

```text
REGULATED
```

Required reviewer:

- `ROLE_PRIVACY_REVIEWER`
- `ROLE_LEGAL_COMPLIANCE_REVIEWER`
- `ROLE_GOVERNANCE_REVIEWER`

Likely stop states:

- `STOP_SENSITIVE_DATA_EXPORT`
- `STOP_EVIDENCE_INSUFFICIENT`
- `STOP_AUTHORITY_MISSING`
- `STOP_AUDIT_RECORD_MISSING`
- `INCIDENT_REVIEW_REQUIRED`

Audit requirement:

Record purpose, data category, lawful basis assumption if applicable, reviewer, egress decision, and minimization decision.

Recovery requirement:

If personal data leaves without authorization, incident and compliance review may be required.

Prototype handling:

```text
SYNTHETIC_ONLY
```

Notes:

Early prototypes must not use real personal data.

## Asset Category 2 - Legal Or Regulated Material

Default risk level:

```text
HIGH
```

Default egress class:

```text
REGULATED
```

Required reviewer:

- `ROLE_LEGAL_COMPLIANCE_REVIEWER`
- `ROLE_GOVERNANCE_REVIEWER`
- `ROLE_SECURITY_REVIEWER` when egress or sensitive handling is involved

Likely stop states:

- `STOP_SOURCE_MISSING`
- `STOP_SOURCE_STALE`
- `STOP_CONFLICTING_EVIDENCE`
- `STOP_SENSITIVE_DATA_EXPORT`
- `STOP_AUTHORITY_MISSING`

Audit requirement:

Record source, authority, use purpose, limitation, reviewer, and decision boundary.

Recovery requirement:

Review if unsupported legal or regulated claim was made.

Prototype handling:

```text
SYNTHETIC_ONLY
```

Notes:

Prototype data should use fictional legal or regulated examples only.

## Asset Category 3 - Credentials, Secrets, And Keys

Default risk level:

```text
CRITICAL
```

Default egress class:

```text
SECRET
```

Required reviewer:

- `ROLE_SECURITY_REVIEWER`
- `ROLE_INCIDENT_REVIEWER` if exposure occurred

Likely stop states:

- `STOP_SECRET_EXPORT`
- `STOP_EGRESS_UNAUTHORIZED`
- `STOP_BULK_EXPORT`
- `INCIDENT_REVIEW_REQUIRED`
- `INCIDENT_FREEZE`
- `INCIDENT_ISOLATION`

Audit requirement:

Record attempted secret class, actor, destination, and blocked reason without recording the secret value.

Recovery requirement:

If real secret exposure occurred, revoke, rotate, isolate, and review.

Prototype handling:

```text
MOCK_ONLY
```

Notes:

Only fake placeholder secrets may be used in examples.

## Asset Category 4 - AI System Instructions And Context

Default risk level:

```text
HIGH
```

Default egress class:

```text
INTERNAL_ONLY
```

Required reviewer:

- `ROLE_AI_GOVERNANCE_REVIEWER`
- `ROLE_SECURITY_REVIEWER`
- `ROLE_GOVERNANCE_REVIEWER`

Likely stop states:

- `STOP_EGRESS_UNAUTHORIZED`
- `STOP_AI_AUTHORITY_EXCEEDED`
- `STOP_AI_SELF_ESCALATION`
- `STOP_UNSUPPORTED_CONFIDENCE`
- `STOP_HIDDEN_CAPABILITY`

Audit requirement:

Record AI context source, instruction boundary, attempted use, and any attempted override or leakage.

Recovery requirement:

Review AI instructions and context if leakage, injection, or self-escalation is detected.

Prototype handling:

```text
REDACTED_ONLY
```

Notes:

System instructions should not be treated as ordinary exportable content.

## Asset Category 5 - Decision Authority

Default risk level:

```text
CRITICAL
```

Default egress class:

```text
INTERNAL_ONLY
```

Required reviewer:

- `ROLE_SYSTEM_OWNER`
- `ROLE_GOVERNANCE_REVIEWER`
- `ROLE_APPROVER`

Likely stop states:

- `STOP_AUTHORITY_MISSING`
- `STOP_ROLE_MISMATCH`
- `STOP_AUTHORITY_EXPIRED`
- `STOP_AI_AUTHORITY_EXCEEDED`
- `STOP_HUMAN_REVIEW_REQUIRED`

Audit requirement:

Record approver, role, scope, expiration, conditions, and related decision.

Recovery requirement:

Review any action performed under missing, expired, or mismatched authority.

Prototype handling:

```text
MOCK_ONLY
```

Notes:

Prototype authority should be simulated, not real.

## Asset Category 6 - Audit Trail And Evidence Records

Default risk level:

```text
HIGH
```

Default egress class:

```text
INTERNAL_ONLY
```

Required reviewer:

- `ROLE_GOVERNANCE_REVIEWER`
- `ROLE_SECURITY_REVIEWER`
- `ROLE_INCIDENT_REVIEWER` when incident-related

Likely stop states:

- `STOP_AUDIT_RECORD_MISSING`
- `STOP_ACCOUNTABILITY_MISSING`
- `STOP_CONFLICT`
- `INCIDENT_REVIEW_REQUIRED`

Audit requirement:

The audit trail itself must be protected, traceable, and tamper-aware.

Recovery requirement:

If audit records are missing, altered, or unreliable, review affected decisions.

Prototype handling:

```text
MOCK_ONLY
```

Notes:

Prototype audit records should be synthetic and clearly marked.

## Asset Category 7 - Models, Prompts, And Governance Logic

Default risk level:

```text
HIGH
```

Default egress class:

```text
INTERNAL_ONLY
```

Required reviewer:

- `ROLE_AI_GOVERNANCE_REVIEWER`
- `ROLE_TECHNICAL_REVIEWER`
- `ROLE_GOVERNANCE_REVIEWER`

Likely stop states:

- `STOP_CAPABILITY_CHANGE`
- `STOP_HIDDEN_CAPABILITY`
- `STOP_AI_SELF_ESCALATION`
- `STOP_MODE_BOUNDARY`
- `STOP_AUDIT_RECORD_MISSING`

Audit requirement:

Record changes to governance logic, prompt structure, model behavior assumptions, and approval scope.

Recovery requirement:

If governance logic changes unexpectedly, freeze affected behavior and review.

Prototype handling:

```text
REVIEW_ONLY
```

Notes:

Governance logic is itself a protected asset.

## Asset Category 8 - System Capabilities

Default risk level:

```text
HIGH
```

Default egress class:

```text
INTERNAL_ONLY
```

Required reviewer:

- `ROLE_TECHNICAL_REVIEWER`
- `ROLE_SECURITY_REVIEWER`
- `ROLE_GOVERNANCE_REVIEWER`

Likely stop states:

- `STOP_CAPABILITY_CHANGE`
- `STOP_HIDDEN_CAPABILITY`
- `STOP_MODE_BOUNDARY`
- `STOP_ESCALATION_NOT_APPROVED`

Audit requirement:

Record capability, trigger, scope, actor, approval, and risk.

Recovery requirement:

If capability was added without approval, revoke, disable, or isolate until reviewed.

Prototype handling:

```text
MOCK_ONLY
```

Notes:

Early prototype capability should be simulated wherever possible.

## Asset Category 9 - External Integrations And Connectors

Default risk level:

```text
CRITICAL
```

Default egress class:

```text
SENSITIVE
```

Required reviewer:

- `ROLE_SECURITY_REVIEWER`
- `ROLE_TECHNICAL_REVIEWER`
- `ROLE_GOVERNANCE_REVIEWER`
- `ROLE_PRIVACY_REVIEWER` when data is involved

Likely stop states:

- `STOP_CAPABILITY_CHANGE`
- `STOP_EGRESS_UNAUTHORIZED`
- `STOP_SENSITIVE_DATA_EXPORT`
- `STOP_SECRET_EXPORT`
- `INCIDENT_REVIEW_REQUIRED`

Audit requirement:

Record integration, data flow, direction, egress class, credentials, approval, and boundary.

Recovery requirement:

If integration leaks or acts unexpectedly, disable integration and review.

Prototype handling:

```text
OUT_OF_SCOPE
```

Notes:

Live external integrations should not exist in early prototype.

## Asset Category 10 - Recovery And Control Mechanisms

Default risk level:

```text
CRITICAL
```

Default egress class:

```text
INTERNAL_ONLY
```

Required reviewer:

- `ROLE_INCIDENT_REVIEWER`
- `ROLE_SECURITY_REVIEWER`
- `ROLE_TECHNICAL_REVIEWER`
- `ROLE_GOVERNANCE_REVIEWER`

Likely stop states:

- `STOP_ROLLBACK_MISSING`
- `REVIEW_REQUIRED_RECOVERY`
- `INCIDENT_FREEZE`
- `INCIDENT_ISOLATION`
- `LOCKDOWN_REQUIRED`

Audit requirement:

Record recovery action, authority, scope, affected assets, verification, and return-to-normal decision.

Recovery requirement:

Recovery actions themselves require verification and audit.

Prototype handling:

```text
MOCK_ONLY
```

Notes:

Recovery controls can be abused and must be governed.

## Asset Category 11 - Cryptographic Trust Material

Default risk level:

```text
CRITICAL
```

Default egress class:

```text
SECRET
```

Required reviewer:

- `ROLE_SECURITY_REVIEWER`
- `ROLE_TECHNICAL_REVIEWER`
- specialist cryptography reviewer if available

Likely stop states:

- `STOP_SECRET_EXPORT`
- `STOP_SOURCE_STALE`
- `STOP_EVIDENCE_INSUFFICIENT`
- `STOP_CAPABILITY_CHANGE`
- `INCIDENT_REVIEW_REQUIRED`

Audit requirement:

Record algorithm, key class, lifecycle assumption, rotation/migration status, and review basis without exposing secrets.

Recovery requirement:

If exposed or obsolete, rotate, revoke, migrate, or isolate based on review.

Prototype handling:

```text
MOCK_ONLY
```

Notes:

Post-quantum readiness requires crypto-agility awareness, not premature cryptographic claims.

## Asset Category 12 - Human Attention And Approval Capacity

Default risk level:

```text
HIGH
```

Default egress class:

```text
NO_EGRESS
```

Required reviewer:

- `ROLE_GOVERNANCE_REVIEWER`
- `ROLE_AI_GOVERNANCE_REVIEWER`
- `ROLE_SYSTEM_OWNER`

Likely stop states:

- `STOP_HUMAN_REVIEW_REQUIRED`
- `STOP_UNSUPPORTED_CONFIDENCE`
- `STOP_ACCOUNTABILITY_MISSING`
- `STOP_CONFLICT`

Audit requirement:

Record when human review was required, who reviewed, what was approved, and what was not approved.

Recovery requirement:

If human review was bypassed, review affected decisions.

Prototype handling:

```text
REVIEW_ONLY
```

Notes:

Human attention is a limited security resource.

Overloading reviewers can become a governance failure.

## Summary Matrix

| Asset Category | Risk | Egress | Prototype Handling |
| --- | --- | --- | --- |
| Personal Data | HIGH | REGULATED | SYNTHETIC_ONLY |
| Legal Or Regulated Material | HIGH | REGULATED | SYNTHETIC_ONLY |
| Credentials, Secrets, And Keys | CRITICAL | SECRET | MOCK_ONLY |
| AI System Instructions And Context | HIGH | INTERNAL_ONLY | REDACTED_ONLY |
| Decision Authority | CRITICAL | INTERNAL_ONLY | MOCK_ONLY |
| Audit Trail And Evidence Records | HIGH | INTERNAL_ONLY | MOCK_ONLY |
| Models, Prompts, And Governance Logic | HIGH | INTERNAL_ONLY | REVIEW_ONLY |
| System Capabilities | HIGH | INTERNAL_ONLY | MOCK_ONLY |
| External Integrations And Connectors | CRITICAL | SENSITIVE | OUT_OF_SCOPE |
| Recovery And Control Mechanisms | CRITICAL | INTERNAL_ONLY | MOCK_ONLY |
| Cryptographic Trust Material | CRITICAL | SECRET | MOCK_ONLY |
| Human Attention And Approval Capacity | HIGH | NO_EGRESS | REVIEW_ONLY |

## Current Project Boundary

For the current documentation-only project:

Allowed asset handling:

- documentation content,
- synthetic examples,
- mock records,
- redacted descriptions,
- conceptual mappings.

Not allowed asset handling:

- real personal data,
- real secrets,
- live integrations,
- production credentials,
- real incident artifacts,
- unredacted system instructions intended to remain private,
- real compliance determinations,
- real security validation evidence.

## Current Consistency Decision

This mapping connects the Asset Register to the Minimal Viable Governance Kernel.

Future prototype design should not begin until each prototype test case identifies:

- asset category,
- risk level,
- egress class,
- reviewer,
- likely stop states,
- audit record,
- recovery requirement.
