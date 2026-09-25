# Governance-First Security Architecture

## Identity And Credential Governance v0.1

## Status

This document is a preparatory identity and credential governance module for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not an identity management system specification.

It is not a security claim.

It is intended to define how identities, credentials, and access tokens must be governed throughout their lifecycle so that credential compromise does not automatically translate into uncontrolled access.

## Purpose

The purpose of this document is to answer:

```text
How is an identity established and verified before credentials are issued?
How are credentials scoped, time-bounded, and minimised?
How are credentials rotated and when?
How is a suspected or confirmed credential compromise detected and contained?
Who is accountable for each credential class?
When must a credential be revoked rather than rotated?
```

## Scope

This module applies to:

- human user credentials including passwords, MFA tokens, and SSO sessions
- service and system credentials including API keys, certificates, and tokens
- third-party credentials issued to external suppliers and partners
- administrative and privileged credentials
- AI system credentials and tool access tokens

## Governing Principle

A credential is not proof of identity. It is proof that someone or something once had authorised access.

A credential that has been compromised, stolen, or left unrevoked remains a valid attack path until it is explicitly invalidated.

The question is not only who holds the credential, but whether that holder still has current authority to act with it.

## Identity Establishment

Before credentials are issued, the identity of the requestor must be established:

```text
For human users:
  Identity verified through an authoritative source.
  Role and access scope confirmed by an accountable authority.
  MFA enrolled before any credentials are activated.

For service accounts and systems:
  Purpose and owning role documented.
  Scope of access defined and minimised.
  Expiry or rotation schedule set at issuance.

For third parties:
  Governed by Third-Party Governance module.
  Identity verified through legal and contractual process.
  Access scoped per third-party governance record.
```

## Credential Principles

All credentials must follow these principles:

- **Minimum scope**: a credential grants only the access required for its stated purpose, nothing more
- **Time boundary**: credentials expire or require renewal at a defined interval
- **Uniqueness**: credentials are not shared between individuals, systems, or third parties
- **Revocability**: every credential must have a defined revocation path that can be executed immediately
- **Auditability**: all credential issuance, use, rotation, and revocation is logged

## Agentic Token Lifetime Limits

Tokens used for inter-agent communication and agentic pipeline authentication have a fundamentally different risk profile from human session credentials. A stolen inter-agent token cannot be detected through behavioural anomaly alone — the agent receiving the token has no way to distinguish a legitimate call from a replay attack using a stolen token. For this reason, short mandatory expiry is the primary structural control.

The following hard limits apply to all agentic tokens. These limits may not be extended without documented approval from the Governance Authority and a corresponding risk acceptance record:

| Token Type | Maximum Lifetime | Additional Constraint |
|---|---|---|
| Inter-agent pipeline token | 15 minutes | Must be single-use or session-bound; a token that has been used once must not be accepted a second time |
| Human-to-agent session token | 60 minutes | Must require re-authentication after expiry; no silent renewal |
| Tool authorisation token | Duration of single tool call | Expires immediately on tool call completion or timeout |
| Agentic API key (long-lived) | 30 days maximum | Requires Governance Authority approval; must be scoped to minimum necessary permissions; rotation on any security event |

Replay prevention is mandatory for inter-agent tokens. The receiving agent must maintain a short-term record of accepted token identifiers sufficient to reject any token presented more than once within its validity window.

This section remediates Gap D identified in GFSA-RED-TEAM-FINDINGS-v0.1.

## Credential Lifecycle

### Issuance

Before a credential is issued:

- identity established and verified
- scope defined and minimised
- expiry or rotation schedule set
- accountability owner assigned
- issuance logged with date, scope, and authority

### Active Use

During active credential use:

- use is logged and reviewable
- anomalous use patterns trigger review
- scope expansion requires new issuance, not credential modification
- shared use of a credential is treated as a governance violation

### Rotation

Credentials are rotated:

- at the defined rotation interval
- immediately following any security incident involving the credential class
- immediately if the credential holder's role or employment status changes
- immediately if anomalous use is detected
- immediately if the credential is suspected exposed in a breach or infostealer log

Rotation is not complete until the old credential is confirmed invalidated.

### Suspension

A credential is suspended when:

- a review is triggered but compromise is not yet confirmed
- the credential holder is temporarily unavailable or under investigation
- a security incident is active and the credential's scope overlaps with the incident area

Suspension is temporary. It resolves to reinstatement or revocation.

### Revocation

A credential is revoked when:

- compromise is confirmed
- the credential holder's access is permanently removed
- the third-party relationship ends
- the service or system the credential belongs to is decommissioned
- rotation fails or cannot be confirmed

Revoked credentials are never reactivated. A new credential is issued through the full issuance process if access is still required.

## Privileged And Administrative Credentials

Privileged credentials require additional controls:

- just-in-time issuance where technically feasible: credentials are issued for a specific task and revoked on completion
- dual-person approval for issuance of the highest privilege classes
- session recording or enhanced audit for all privileged sessions
- privileged credentials are never stored in shared locations, wikis, or unencrypted files
- privileged credential use outside defined maintenance windows triggers immediate review

## Credential Compromise Response

If a credential is suspected or confirmed compromised:

```text
Immediate action:
  Suspend the credential.
  Audit all use of the credential within the review window.
  Identify all systems accessible with the credential.
  Assess whether lateral movement has occurred.

Secondary action:
  Revoke the credential.
  Issue replacement credential through full issuance process if access is still required.
  Notify accountability owner.
  Trigger INCIDENT_REVIEW_REQUIRED.

If lateral movement is confirmed or suspected:
  Trigger LOCKDOWN_REQUIRED.
  Follow Recovery Rollback Incidents module.
```

A suspected compromise is treated as a confirmed compromise for containment purposes until evidence confirms otherwise.

## Credential Register

For each active credential class, the following must be recorded and kept current:

| Field | Description |
|---|---|
| Credential identifier | Unique reference, not the credential value itself |
| Credential type | Password, API key, certificate, token, MFA seed |
| Identity bound to | Human user, service account, third party, AI system |
| Scope | Systems and capabilities accessible |
| Expiry or rotation interval | When the credential must be renewed or rotated |
| Accountability owner | Named internal individual |
| Issuance date | Date credential was issued |
| Last rotation date | Date of most recent rotation |
| Status | Active, suspended, revoked |

The credential register does not store credential values. It records governance metadata only.

## Relationship To Other Modules

- Third-Party Governance: third-party credentials follow this module's lifecycle rules
- Trust Boundaries: credential compromise is a trust boundary failure
- Supply Chain Abuse Cases: SC-003 (credential theft from third party) depends on this module
- Stop-State Registry: credential compromise triggers defined stop states
- Audit And Accountability: all credential lifecycle events are subject to audit requirements
- Recovery Rollback Incidents: credential compromise follows the incident recovery path
- Ingress Egress Policy: revoked credentials must be fail-closed at all ingress points
- Red Team Findings: GFSA-RED-TEAM-FINDINGS-v0.1 Gap D

## Open Questions

1. Should all credentials have a maximum lifetime regardless of rotation schedule?
2. What is the acceptable response time between detecting a suspected compromise and suspending the credential?
3. Should credential governance records be stored inside or outside the governed environment?
4. How should AI system credentials be governed differently from human credentials?
5. Should MFA be required for all credential classes or only privileged ones?
6. How does this module interact with existing identity provider or SSO configurations?
7. Should dark web monitoring for credential exposure be a required governance control?
8. How should credential governance be tested without using real credentials?
