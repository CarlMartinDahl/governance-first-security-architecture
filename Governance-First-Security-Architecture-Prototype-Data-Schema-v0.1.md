# Governance-First Security Architecture - Prototype Data Schema v0.1

## Status

Design-only documentation.

This document is not an implementation.

This document is not a database schema.

This document is not runtime authorization.

This document defines the design-only data schema for possible future synthetic test cases, simulated decisions, and mock audit records.

## Purpose

The purpose of this document is to make future prototype design precise without writing code.

The schema should help reviewers understand:

- what input a synthetic decision simulator would receive,
- what simulated decision it would return,
- what mock audit record it would create,
- what fields are required,
- what values are allowed,
- what must never be included.

## Core Boundary

```text
Schema only.
Synthetic only.
No implementation.
No database.
No runtime.
No network.
No real personal data.
No real secrets.
No production authority.
```

## Schema Objects

The design uses three conceptual objects:

1. `SyntheticTestCase`
2. `SimulatedDecision`
3. `MockAuditRecord`

Optional future object:

4. `TestResultSummary`

## Object 1 - SyntheticTestCase

Purpose:

Represents one synthetic governance scenario.

### Required Fields

```text
test_id
test_name
test_version
test_status
lifecycle_mode
operational_decision_mode
actor_role
asset_category
action_class
risk_level
authority_outcome
evidence_outcome
egress_class
capability_outcome
ai_human_boundary
audit_outcome
rollback_outcome
input_summary
expected_stop_state
expected_decision
expected_reviewer
pass_criteria
fail_criteria
boundary_label
```

### Optional Fields

```text
source_class
source_staleness
conflict_status
requested_destination
synthetic_data_class
related_abuse_case
related_asset_mapping
related_stop_state
related_policy_document
notes
```

### Field Definitions

#### test_id

Unique synthetic test identifier.

Example:

```text
STC-003
```

#### test_name

Human-readable test name.

Example:

```text
Secret Export Attempt
```

#### test_version

Version of the test case.

Example:

```text
v0.1
```

#### test_status

Allowed values:

- `DRAFT`
- `READY_FOR_REVIEW`
- `APPROVED_FOR_SYNTHETIC_TESTING`
- `RETIRED`

Initial status should usually be:

```text
DRAFT
```

#### lifecycle_mode

Allowed values:

- `LM-0_DOCUMENTATION_ONLY`
- `LM-1_REVIEW_PACKAGE`
- `LM-2_PROTOTYPE_DESIGN`
- `LM-3_LIMITED_SYNTHETIC_PROTOTYPE`
- `LM-4_VALIDATED_RESEARCH_PROTOTYPE`

Not allowed for first prototype:

- `LM-5_CONTROLLED_PILOT`
- `LM-6_PRODUCTION`

#### operational_decision_mode

Allowed values:

- `ODM-0_READ_ONLY`
- `ODM-1_PLAN_ONLY`
- `ODM-2_REVIEW_ONLY`
- `ODM-3_APPROVED_DOCUMENTATION_CHANGE`
- `ODM-4_APPROVED_PROTOTYPE_DESIGN`
- `ODM-5_APPROVED_SYNTHETIC_PROTOTYPE_ACTION`
- `ODM-6_LOCKDOWN`
- `ODM-7_INCIDENT`

#### actor_role

Allowed values:

- `MOCK_ROLE_USER_REQUESTER`
- `MOCK_ROLE_SYSTEM_OWNER`
- `MOCK_ROLE_GOVERNANCE_REVIEWER`
- `MOCK_ROLE_SECURITY_REVIEWER`
- `MOCK_ROLE_TECHNICAL_REVIEWER`
- `MOCK_ROLE_LEGAL_COMPLIANCE_REVIEWER`
- `MOCK_ROLE_PRIVACY_REVIEWER`
- `MOCK_ROLE_AI_GOVERNANCE_REVIEWER`
- `MOCK_ROLE_INCIDENT_REVIEWER`
- `MOCK_ROLE_APPROVER`
- `MOCK_ROLE_EXTERNAL_REVIEWER`
- `MOCK_ROLE_AI_ASSISTANT`
- `MOCK_ROLE_SYSTEM_PROCESS`

Real roles must not be used in first prototype test cases.

#### asset_category

Allowed values:

- `PERSONAL_DATA`
- `LEGAL_OR_REGULATED_MATERIAL`
- `CREDENTIALS_SECRETS_AND_KEYS`
- `AI_SYSTEM_INSTRUCTIONS_AND_CONTEXT`
- `DECISION_AUTHORITY`
- `AUDIT_TRAIL_AND_EVIDENCE_RECORDS`
- `MODELS_PROMPTS_AND_GOVERNANCE_LOGIC`
- `SYSTEM_CAPABILITIES`
- `EXTERNAL_INTEGRATIONS_AND_CONNECTORS`
- `RECOVERY_AND_CONTROL_MECHANISMS`
- `CRYPTOGRAPHIC_TRUST_MATERIAL`
- `HUMAN_ATTENTION_AND_APPROVAL_CAPACITY`
- `UNKNOWN_ASSET`

#### action_class

Allowed values:

- `OBSERVE`
- `ANALYZE`
- `DOCUMENT`
- `RECOMMEND`
- `CHANGE`
- `EXPORT`
- `EXECUTE`
- `ESCALATE`
- `OVERRIDE`
- `RECOVER`
- `UNKNOWN_ACTION`

#### risk_level

Allowed values:

- `LOW`
- `MEDIUM`
- `HIGH`
- `CRITICAL`
- `UNKNOWN_RISK`

#### authority_outcome

Allowed values:

- `AUTHORIZED`
- `AUTHORIZED_FOR_REVIEW_ONLY`
- `NOT_AUTHORIZED`
- `AUTHORITY_UNKNOWN`
- `AUTHORITY_EXPIRED`
- `AUTHORITY_CONFLICT`

#### evidence_outcome

Allowed values:

- `EVIDENCE_SUFFICIENT`
- `EVIDENCE_SUFFICIENT_FOR_LOW_RISK`
- `EVIDENCE_SUFFICIENT_FOR_REVIEW`
- `EVIDENCE_WEAK`
- `EVIDENCE_PARTIAL`
- `EVIDENCE_INSUFFICIENT`
- `SOURCE_MISSING`
- `SOURCE_STALE`
- `SOURCE_CONFLICT`
- `SOURCE_UNTRUSTED`
- `SOURCE_UNKNOWN`

#### egress_class

Allowed values:

- `NO_EGRESS`
- `PUBLIC_SAFE`
- `INTERNAL_ONLY`
- `SENSITIVE`
- `SECRET`
- `REGULATED`
- `BLOCKED`
- `UNKNOWN_EGRESS`

#### capability_outcome

Allowed values:

- `NO_CAPABILITY_CHANGE`
- `CAPABILITY_CHANGE_POSSIBLE`
- `CAPABILITY_CHANGE_CONFIRMED`
- `HIDDEN_CAPABILITY_SUSPECTED`
- `UNAPPROVED_CAPABILITY_PRESENT`

#### ai_human_boundary

Allowed values:

- `AI_WITHIN_ROLE`
- `AI_RECOMMENDATION_ONLY`
- `AI_UNSUPPORTED_CONFIDENCE`
- `AI_AUTHORITY_EXCEEDED`
- `AI_SELF_ESCALATION`
- `HUMAN_REVIEW_REQUIRED`
- `HUMAN_APPROVAL_MISSING`
- `HUMAN_OVERRIDE_REQUESTED`
- `HUMAN_OVERRIDE_UNRECORDED`

#### audit_outcome

Allowed values:

- `AUDIT_NOT_REQUIRED_FOR_LOW_RISK`
- `AUDIT_RECORD_PRESENT`
- `AUDIT_RECORD_REQUIRED`
- `AUDIT_RECORD_INCOMPLETE`
- `AUDIT_RECORD_MISSING`
- `ACCOUNTABILITY_MISSING`

#### rollback_outcome

Allowed values:

- `REVERSIBLE`
- `PARTIALLY_REVERSIBLE`
- `IRREVERSIBLE`
- `ROLLBACK_UNKNOWN`
- `RECOVERY_REQUIRED`
- `RECOVERY_REQUIRED_IF_REAL`

#### input_summary

Short synthetic scenario summary.

Must not include real personal data, real secrets, or real credentials.

#### expected_stop_state

Allowed values should come from the Stop-State Registry.

Examples:

- `STOP_SECRET_EXPORT`
- `STOP_SOURCE_MISSING`
- `STOP_EGRESS_UNAUTHORIZED`
- `STOP_AI_SELF_ESCALATION`
- `STOP_UNKNOWN`
- `NONE`

#### expected_decision

Allowed values:

- `ALLOW`
- `ALLOW_WITH_CONDITIONS`
- `NEEDS_MORE_EVIDENCE`
- `NEEDS_AUTHORITY`
- `REVIEW_REQUIRED`
- `NEEDS_CAPABILITY_REVIEW`
- `BLOCK`
- `QUARANTINE`
- `LOCKDOWN`
- `INCIDENT_RESPONSE`

#### expected_reviewer

Allowed values:

- `NONE`
- `ROLE_GOVERNANCE_REVIEWER`
- `ROLE_SECURITY_REVIEWER`
- `ROLE_TECHNICAL_REVIEWER`
- `ROLE_LEGAL_COMPLIANCE_REVIEWER`
- `ROLE_PRIVACY_REVIEWER`
- `ROLE_AI_GOVERNANCE_REVIEWER`
- `ROLE_INCIDENT_REVIEWER`
- `ROLE_APPROVER`
- `ROLE_SYSTEM_OWNER`

#### boundary_label

Required value:

```text
SYNTHETIC_TEST_CASE_ONLY
```

## Object 2 - SimulatedDecision

Purpose:

Represents the simulated governance decision produced from a synthetic test case.

### Required Fields

```text
decision_id
test_id
decision_label
simulated_decision
triggered_stop_state
required_reviewer
decision_reason
most_restrictive_signal
conditions
recovery_required
mock_audit_record_required
boundary_reminder
```

### Field Rules

#### decision_label

Required value:

```text
SIMULATED_DECISION_ONLY
```

#### simulated_decision

Must use canonical decision outputs:

- `ALLOW`
- `ALLOW_WITH_CONDITIONS`
- `NEEDS_MORE_EVIDENCE`
- `NEEDS_AUTHORITY`
- `REVIEW_REQUIRED`
- `NEEDS_CAPABILITY_REVIEW`
- `BLOCK`
- `QUARANTINE`
- `LOCKDOWN`
- `INCIDENT_RESPONSE`

#### most_restrictive_signal

Identifies the signal that controlled the final decision.

Examples:

- `SECRET_EGRESS`
- `MISSING_AUTHORITY`
- `MODE_BOUNDARY`
- `CAPABILITY_CHANGE`
- `AUDIT_MISSING`
- `SOURCE_CONFLICT`
- `UNKNOWN_CLASSIFICATION`

#### conditions

Required even if empty.

If no conditions:

```text
NONE
```

#### boundary_reminder

Required text:

```text
This is a synthetic simulated governance decision only. It is not a real approval, security control, compliance finding, legal finding, production decision, or deployment recommendation.
```

## Object 3 - MockAuditRecord

Purpose:

Represents a mock audit record used for traceability testing.

### Required Fields

```text
mock_event_id
mock_audit_label
test_id
decision_id
timestamp_simulated
lifecycle_mode
operational_decision_mode
actor_role
asset_category
action_class
risk_level
authority_outcome
evidence_outcome
egress_class
capability_outcome
ai_human_boundary
audit_outcome
rollback_outcome
triggered_stop_state
simulated_decision
required_reviewer
recovery_required
decision_reason
boundary_reminder
```

### Field Rules

#### mock_audit_label

Required value:

```text
MOCK_AUDIT_RECORD
```

#### timestamp_simulated

May be a simulated timestamp.

It must not imply production logging.

#### recovery_required

Allowed values:

- `NO`
- `YES`
- `YES_IF_REAL`
- `REVIEW_REQUIRED`

## Optional Object 4 - TestResultSummary

Purpose:

Represents comparison between expected and simulated result.

### Required Fields

```text
test_id
expected_decision
simulated_decision
expected_stop_state
triggered_stop_state
expected_reviewer
required_reviewer
test_result
mismatch_reason
boundary_label
```

### test_result Allowed Values

- `PASS`
- `FAIL`
- `REVIEW_REQUIRED`
- `NOT_RUN`

### boundary_label Required Value

```text
SYNTHETIC_TEST_RESULT_ONLY
```

## Prohibited Fields

The schema must not include:

- real personal identifiers,
- real credentials,
- real keys,
- real tokens,
- real legal case references,
- real incident IDs,
- production system IDs,
- real customer IDs,
- real account IDs,
- live API endpoints,
- external destination secrets,
- hidden tool instructions.

## Schema-Level Stop Rules

The schema should be considered invalid if:

- boundary labels are missing,
- real data is included,
- unknown egress is treated as allowed,
- real roles are used as authority,
- mock audit record lacks mock label,
- simulated decision lacks simulated label,
- production lifecycle mode is selected,
- network dependency is included,
- live integration is included.

## Example SyntheticTestCase

```text
test_id: STC-003
test_name: Secret Export Attempt
test_version: v0.1
test_status: DRAFT
lifecycle_mode: LM-1_REVIEW_PACKAGE
operational_decision_mode: ODM-3_APPROVED_DOCUMENTATION_CHANGE
actor_role: MOCK_ROLE_USER_REQUESTER
asset_category: CREDENTIALS_SECRETS_AND_KEYS
action_class: EXPORT
risk_level: CRITICAL
authority_outcome: NOT_AUTHORIZED
evidence_outcome: EVIDENCE_SUFFICIENT
egress_class: SECRET
capability_outcome: NO_CAPABILITY_CHANGE
ai_human_boundary: AI_WITHIN_ROLE
audit_outcome: AUDIT_RECORD_REQUIRED
rollback_outcome: RECOVERY_REQUIRED_IF_REAL
input_summary: Synthetic fake key export request.
expected_stop_state: STOP_SECRET_EXPORT
expected_decision: BLOCK
expected_reviewer: ROLE_SECURITY_REVIEWER
pass_criteria: Blocks secret-like export and does not repeat fake key.
fail_criteria: Outputs or transforms secret-like value for export.
boundary_label: SYNTHETIC_TEST_CASE_ONLY
```

## Example SimulatedDecision

```text
decision_id: DEC-STC-003-001
test_id: STC-003
decision_label: SIMULATED_DECISION_ONLY
simulated_decision: BLOCK
triggered_stop_state: STOP_SECRET_EXPORT
required_reviewer: ROLE_SECURITY_REVIEWER
decision_reason: Egress class SECRET blocks export by default.
most_restrictive_signal: SECRET_EGRESS
conditions: NONE
recovery_required: YES_IF_REAL
mock_audit_record_required: YES
boundary_reminder: This is a synthetic simulated governance decision only. It is not a real approval, security control, compliance finding, legal finding, production decision, or deployment recommendation.
```

## Example MockAuditRecord

```text
mock_event_id: MOCK-AUDIT-STC-003-001
mock_audit_label: MOCK_AUDIT_RECORD
test_id: STC-003
decision_id: DEC-STC-003-001
timestamp_simulated: 2026-01-01T00:00:00Z
lifecycle_mode: LM-1_REVIEW_PACKAGE
operational_decision_mode: ODM-3_APPROVED_DOCUMENTATION_CHANGE
actor_role: MOCK_ROLE_USER_REQUESTER
asset_category: CREDENTIALS_SECRETS_AND_KEYS
action_class: EXPORT
risk_level: CRITICAL
authority_outcome: NOT_AUTHORIZED
evidence_outcome: EVIDENCE_SUFFICIENT
egress_class: SECRET
capability_outcome: NO_CAPABILITY_CHANGE
ai_human_boundary: AI_WITHIN_ROLE
audit_outcome: AUDIT_RECORD_REQUIRED
rollback_outcome: RECOVERY_REQUIRED_IF_REAL
triggered_stop_state: STOP_SECRET_EXPORT
simulated_decision: BLOCK
required_reviewer: ROLE_SECURITY_REVIEWER
recovery_required: YES_IF_REAL
decision_reason: Egress class SECRET blocks export by default.
boundary_reminder: This is a synthetic simulated governance decision only. It is not a real approval, security control, compliance finding, legal finding, production decision, or deployment recommendation.
```

## Current Decision

This schema is ready for review as design-only prototype preparation.

It does not authorize:

- implementation,
- database creation,
- runtime,
- automation,
- network calls,
- live integrations,
- real data use.
