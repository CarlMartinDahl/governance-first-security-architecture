# Governance-First Security Architecture

## Third-Party Governance v0.1

## Status

This document is a preparatory governance module for third-party and supplier relationships in the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a vendor assessment framework.

It is not a security claim.

It is intended to define how third-party authority, access, and accountability must be governed before any external party is permitted to act within or adjacent to a governed environment.

## Purpose

The purpose of this document is to answer:

```text
Under whose authority does a third party act?
What is the third party explicitly permitted to do?
What is the third party explicitly not permitted to do?
What evidence is required before access is granted?
How is access monitored, validated, and revoked?
What stop states apply if a third party is suspected compromised?
Who is accountable if a third party causes harm?
```

## Scope

This module applies to:

- external vendors and suppliers with any form of system access
- web, IT, and software partners
- managed service providers and outsourced IT functions
- integration partners and API consumers
- any party acting under a trust relationship without direct employment accountability

## Governing Principle

A third party inherits no implicit trust from its business relationship.

Trust must be explicitly granted, scoped, time-bounded, and revocable.

A third party operating outside its defined scope is treated as an untrusted actor regardless of its contractual status.

## Third-Party Authority Model

Before any third party is permitted access, the following must be defined:

```text
Authority source:
  Which internal role authorises this third party?
  Under what conditions can that authorisation be revoked?

Scope of access:
  Which systems, data, and capabilities is the third party permitted to access?
  Which systems, data, and capabilities are explicitly excluded?

Mode of access:
  Read-only, supervised write, unsupervised write, administrative?
  Time-bounded session or persistent credential?

Evidence requirement:
  What must the third party demonstrate before access is granted?
  Security posture, certifications, identity verification?

Egress boundary:
  What data, if any, is the third party permitted to take outside the environment?
  What data must never leave the environment regardless of business justification?

Accountability:
  Who inside the organisation is accountable for this third party's actions?
  Is that accountability documented and reviewable?
```

## Access Lifecycle

### Onboarding

Before access is granted:

- authority source identified and documented
- scope of access defined and minimised
- egress boundary declared
- accountability owner assigned
- access mode selected and justified
- review interval set

Access is not granted until all onboarding conditions are met.

### Active Access

During active access:

- access is logged and auditable
- sessions are time-bounded where technically feasible
- anomalous behaviour triggers review, not assumption of legitimacy
- scope expansion requires a new authority decision, not a convenience exception
- the third party is treated as an untrusted actor for egress purposes at all times

### Review

Access is reviewed at a defined interval and on any of the following events:

- third party reports a security incident
- third party is acquired, restructured, or changes key personnel
- anomalous access pattern is detected
- business relationship changes
- governance review flags the relationship

Review outcome must be one of:

```text
ACCESS_CONFIRMED
ACCESS_REDUCED
ACCESS_SUSPENDED
ACCESS_REVOKED
```

### Offboarding

When a third-party relationship ends or access is revoked:

- all credentials are invalidated immediately
- all active sessions are terminated
- access logs are preserved for incident review period
- data returned or destroyed per agreement
- offboarding is documented with date, authority, and reason

Offboarding is not complete until credential invalidation is confirmed, not merely requested.

## Compromised Third Party

If a third party is suspected or confirmed compromised:

```text
Immediate action:
  Suspend all active sessions.
  Revoke all credentials issued to the third party.
  Isolate any systems the third party had access to.
  Trigger INCIDENT_REVIEW_REQUIRED.

Secondary action:
  Audit all third-party actions within the review window.
  Identify any data that may have been accessed or exfiltrated.
  Notify accountability owner.
  Assess downstream exposure.

Stop state:
  LOCKDOWN_REQUIRED if lateral movement is suspected.
  INCIDENT_REVIEW_REQUIRED in all cases.
```

A compromised third party is treated as a full security incident regardless of the third party's own assessment of the compromise.

## Minimum Viable Third-Party Governance Record

For each active third party, the following must be recorded and kept current:

| Field | Description |
|---|---|
| Third-party name | Legal name and trading name |
| Authority source | Internal role authorising access |
| Access scope | Systems, data, and capabilities permitted |
| Excluded scope | Explicit exclusions |
| Egress boundary | What may and may not leave the environment |
| Access mode | Read-only, supervised, administrative |
| Credential type | API key, VPN, password, certificate |
| Session model | Time-bounded or persistent |
| Review interval | Maximum time between access reviews |
| Accountability owner | Named internal individual |
| Onboarding date | Date access was granted |
| Last review date | Date of most recent review |
| Status | Active, suspended, revoked |

## Relationship To Other Modules

- Trust Boundaries: third party is a distinct trust boundary class
- Ingress Egress Policy: third-party egress is governed by the same fail-closed rules
- Abuse Case Library: see Supply Chain Abuse Cases for third-party attack scenarios
- Stop-State Registry: compromised third party triggers defined stop states
- Role Registry: accountability owner must be a registered role
- Audit And Accountability: all third-party actions are subject to audit requirements
- Recovery Rollback Incidents: third-party compromise follows the incident recovery path

## Open Questions

1. Should third-party governance records be stored inside or outside the governed environment?
2. What is the minimum review interval for high-risk third parties?
3. Should third parties be required to demonstrate security posture before onboarding?
4. How should trust be re-established after a confirmed compromise and remediation?
5. Should a compromised third party ever be re-onboarded, and under what conditions?
6. How does this module interact with existing vendor contract and procurement processes?
7. Is a single accountability owner sufficient, or should there be a backup?
8. Should third-party access be technically enforced or governance-enforced, or both?
