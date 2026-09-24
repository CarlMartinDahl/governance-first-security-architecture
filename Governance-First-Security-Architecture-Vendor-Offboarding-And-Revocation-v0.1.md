# Governance-First Security Architecture

## Vendor Offboarding And Revocation v0.1

## Status

This document is a preparatory vendor offboarding and revocation module for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a procurement or contract management framework.

It is not a security claim.

It is intended to define how third-party access is formally closed, verified, and documented when a vendor relationship ends, when access is revoked for cause, or when a vendor is suspected or confirmed compromised.

## Purpose

The purpose of this document is to answer:

```text
What must happen before a vendor relationship is considered safely closed?
How is credential invalidation confirmed, not merely requested?
How is offboarding triggered outside of planned relationship endings?
What is the governance record of the offboarding?
How does offboarding interact with an active incident?
What must be reviewed after offboarding to confirm no residual access remains?
```

## Governing Principle

A vendor relationship that has ended on paper but not in the access layer is an open attack path.

Offboarding is not complete when the contract ends. It is complete when access is confirmed closed, credentials are confirmed invalidated, and the closure is documented with evidence.

## Offboarding Triggers

Vendor offboarding is triggered by any of the following:

```text
Planned ending:
  Contract or engagement ends as scheduled.
  Business relationship is terminated by mutual agreement.
  Vendor is replaced by another supplier.

Unplanned ending:
  Vendor relationship is terminated for cause.
  Vendor is acquired, restructured, or ceases operation.
  Vendor key personnel with system access depart.

Security-driven ending:
  Vendor is suspected or confirmed compromised.
  Anomalous access pattern is detected on vendor credentials.
  Vendor fails to meet governance or security requirements on review.
  Active security incident implicates vendor access path.
```

Security-driven offboarding is treated as an incident and follows the incident response path in parallel with the offboarding process.

## Offboarding Steps

Offboarding must complete all of the following steps in sequence:

### Step 1: Access Suspension

```text
All active vendor sessions are terminated immediately.
All vendor credentials are suspended.
Suspension is logged with timestamp and authority.
```

Suspension precedes all other steps. Access is not maintained during offboarding for convenience.

### Step 2: Credential Invalidation

```text
All credentials issued to the vendor are revoked.
Revocation is confirmed through the credential governance record, not assumed.
API keys, certificates, tokens, VPN access, and any other access mechanism are each individually confirmed invalidated.
If revocation cannot be confirmed for any credential, that credential is treated as still active and escalated immediately.
```

### Step 3: Access Audit

```text
All vendor access within the defined review window is audited.
Any access outside the vendor's defined scope is flagged for review.
Data accessed or modified by the vendor during the review window is identified.
If any anomalous access is found, INCIDENT_REVIEW_REQUIRED is triggered regardless of whether offboarding was planned.
```

### Step 4: Data Review

```text
Any data shared with or accessible to the vendor is reviewed.
Data that should not have been accessible is flagged and reported.
Data return or destruction is confirmed per the contractual and governance agreement.
Personal data handling is reviewed for GDPR alignment.
```

### Step 5: Residual Access Check

```text
Systems previously accessible to the vendor are scanned for residual access paths.
This includes: shared accounts, cached credentials, delegated permissions, OAuth grants, saved sessions, and any integration connectors.
Residual access found after Step 2 is treated as a governance failure and triggers immediate escalation.
```

### Step 6: Offboarding Record

```text
Offboarding is documented with:
  - vendor name and governance record reference
  - offboarding trigger and type
  - date and time of access suspension
  - date and time of credential invalidation confirmed
  - audit findings summary
  - data review outcome
  - residual access check outcome
  - accountability owner sign-off
  - any open items and their resolution path
```

Offboarding is not complete until the record is signed off by the accountability owner.

## Emergency Offboarding

When a vendor must be offboarded immediately due to a suspected or confirmed compromise:

```text
Step 1 (access suspension) is executed without waiting for any other step.
Steps 2 through 6 follow as quickly as possible but do not delay Step 1.
INCIDENT_REVIEW_REQUIRED is triggered in parallel.
If lateral movement is suspected, LOCKDOWN_REQUIRED is triggered.
Emergency offboarding record is created within the incident review window.
```

Emergency offboarding prioritises containment over process completeness. Missing steps are completed as part of the incident review, not deferred indefinitely.

## Re-Onboarding After Offboarding

A vendor that has been offboarded is not automatically eligible for re-onboarding.

Re-onboarding requires:

- a new authority decision by the accountable internal role
- a review of the offboarding record and any incident findings
- confirmation that the conditions that triggered offboarding have been resolved
- full onboarding process as defined in Third-Party Governance, not a credential reinstatement

A vendor that was offboarded due to confirmed compromise requires additional evidence of remediation before re-onboarding is considered.

## Relationship To Other Modules

- Third-Party Governance: offboarding closes the access lifecycle defined in that module
- Identity And Credential Governance: credential revocation in Step 2 follows that module's revocation rules
- Supply Chain Abuse Cases: SC-006 (third party as persistence path) is directly addressed by Steps 2 and 5
- Stop-State Registry: security-driven offboarding triggers defined stop states
- Audit And Accountability: offboarding record and audit findings are subject to audit requirements
- Recovery Rollback Incidents: emergency offboarding runs in parallel with the incident recovery path
- GDPR And EU AI Act Alignment: Step 4 data review interacts with personal data handling obligations

## Open Questions

1. What is the maximum acceptable time between offboarding trigger and completion of Step 1 for each offboarding type?
2. Should the offboarding record be stored inside or outside the governed environment?
3. How should offboarding interact with contractual notice periods that assume continued access?
4. Should residual access checks be automated or manual, or both?
5. What constitutes sufficient evidence of remediation before a compromised vendor is considered for re-onboarding?
6. How should offboarding be tested without disrupting active vendor relationships?
7. Should the accountability owner be able to sign off on their own offboarding record, or is independent sign-off required?
