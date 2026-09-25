# Governance-First Security Architecture
## Privileged Access Management Policy
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy governs the management of privileged access — access that grants elevated control over systems, infrastructure, data, or other accounts beyond what is required for standard operational tasks. Privileged accounts are the highest-value target for both external attackers and malicious insiders: a single compromised privileged credential can undo every other security control in the environment.

This policy defines who holds privileged access, under what conditions, through what mechanisms, and how that access is monitored and reviewed.

---

## 2. Scope

Applies to all accounts, roles, and credentials that hold elevated permissions: system administrators, database administrators, cloud infrastructure roles, CI/CD pipeline service accounts with deployment authority, identity provider administrators, security tool operators, and any account capable of modifying access controls, audit logs, or security configuration.

---

## 3. Core Governance Principle

> **No person or system holds standing privileged access by default. Privileged access is granted for a defined purpose, a defined time window, and subject to session recording. The existence of standing privileged access that is not actively required is itself a finding.**

---

## 4. Privileged Account Classification

| Class | Description | Examples |
|---|---|---|
| Tier 0 — Identity Infrastructure | Control over the identity and authentication plane itself | Identity provider admin, PKI admin, secret store admin, MFA system admin |
| Tier 1 — Systems And Infrastructure | Control over operating systems, hypervisors, cloud infrastructure | Server admin, cloud IAM admin, network device admin, container orchestration admin |
| Tier 2 — Applications, Data, And Audit Infrastructure | Elevated access within applications, data stores, or audit and log infrastructure | Database admin, application admin, data lake admin, AI model platform admin, raw gateway log read access, agent audit log read access |
| Tier 3 — Security And Audit Tools | Access to security tooling, log query interfaces, and processed audit outputs | SIEM admin, vulnerability scanner admin, log management admin |
| Break-Glass | Emergency access outside normal provisioning | Disaster recovery accounts, emergency admin credentials |

Tier 0 is the most sensitive. A compromise of Tier 0 accounts can invalidate all other access controls.

---

## 5. Log And Audit Infrastructure As Privileged Access

Raw log access — particularly access to gateway logs, API proxy logs, and agent audit logs in their unprocessed form — is a privileged access class, not a read-only operational convenience. This classification follows directly from the attack surface these logs represent: an unprocessed log may contain authentication tokens, session identifiers, API keys, or other credentials that were inadvertently captured before scrubbing controls were applied.

The following rules apply to all raw log and audit infrastructure access:

- **Raw gateway logs, API proxy logs, and agent audit logs are classified as Tier 2 Privileged Access.** Read access to these resources requires the same governance controls as write access to Tier 2 application systems.
- **Access is just-in-time.** No standing read access to raw logs is permitted. Access is requested for a defined purpose and time window, provisioned at request time, and automatically revoked at window expiry.
- **All access is logged** in a separate audit trail that is itself stored under Log Integrity And Tamper-Evidence controls. The audit trail for log access must be stored in a location that cannot be accessed by the same access path as the logs being accessed.
- **Bulk export of raw logs requires Governance Authority approval** and is treated as a high-severity audit event regardless of the stated purpose.
- **Processed and anonymised log outputs** — dashboards, aggregated metrics, alert summaries, and query results that do not expose raw request content — may be accessed under standard role-based access controls without Tier 2 treatment. The boundary between raw and processed must be enforced technically, not by convention.
- **Configuration of log scrubbing pipelines** — the systems responsible for removing credentials and sensitive content from logs before storage — is Tier 1 access. Modifying scrubbing configuration can expose credentials retroactively in future log entries and is treated with corresponding severity.

This section remediates Gap F identified in GFSA-RED-TEAM-FINDINGS-v0.1.

---

## 6. Account Separation Requirements

- Privileged accounts must be **separate identities** from the individual's standard user account. An administrator does not use their admin account for email, browsing, or non-administrative tasks.
- Privileged account usernames must not be personally identifiable by convention — they are tracked in the Role Registry, not embedded in the account name
- Tier 0 and Tier 1 privileged accounts must authenticate using phishing-resistant MFA (hardware security key or equivalent); SMS OTP is not acceptable
- Privileged accounts must not have external email addresses or be enrolled in consumer identity services
- Shared privileged accounts are prohibited except for Break-Glass accounts; all other privileged accounts are individual and named

---

## 7. Just-In-Time Access

Standing privileged access — where an account holds elevated permissions continuously rather than for a defined task window — is the highest-risk configuration and must be eliminated where technically feasible:

- Privileged access is requested for a specific task with a defined time window (maximum 8 hours for standard tasks; maximum 24 hours for extended maintenance)
- Access is provisioned at request time and automatically revoked at window expiry
- The requesting individual documents the purpose at time of request; this is logged in Audit and Accountability
- Where the technology does not support just-in-time provisioning, standing access is permitted only with compensating controls: session recording, enhanced monitoring, and quarterly access review
- All just-in-time access requests are reviewed weekly for patterns; anomalous request frequency is escalated

---

## 8. Session Recording And Monitoring

- All privileged sessions for Tier 0 and Tier 1 accounts must be recorded where technically feasible
- Session recordings are stored in the centralised log management system under Log Integrity And Tamper-Evidence controls
- Session recordings are retained for minimum 1 year
- Privileged session activity is monitored for the following anomalies, which trigger immediate investigation:
  - Session initiated outside normal working hours without prior authorisation
  - Bulk data access or export within a privileged session
  - Access to systems outside the account's defined scope
  - Attempts to disable or modify audit logging during a session
  - Lateral movement from a privileged session to systems not in the account's scope
  - Session duration significantly exceeding the requested window

---

## 9. Break-Glass Accounts

Break-glass accounts exist for emergency scenarios where normal just-in-time provisioning is unavailable. They are not for convenience.

- Break-glass credentials are stored in a physically secured location and/or a secret management system accessible only in emergencies
- Use of any break-glass account triggers immediate notification to the Security Governance role
- All break-glass sessions are fully recorded
- Post-use: break-glass credentials are rotated immediately after use; use is reviewed within 24 hours
- Break-glass accounts are tested for accessibility at minimum annually without activating them operationally
- The number of break-glass accounts is minimised; each must have a documented specific emergency scenario it addresses

---

## 10. Privileged Access Review

- All privileged account assignments are reviewed quarterly by the Security Governance role
- Review confirms: the individual still requires the access, the access scope remains appropriate, the account has been used within the review period (unused privileged accounts are revoked)
- Privileged access for individuals who have changed roles, gone on extended leave, or left the organisation is revoked immediately under Vendor Offboarding And Revocation and the Role Registry offboarding process
- Review results are documented in Audit and Accountability

---

## 11. Privileged Service Accounts

Service accounts (non-human identities used by systems and automation) with privileged access follow the same governance principles with adaptations:

- Each privileged service account has a named human owner accountable for its use
- Service accounts are scoped to the minimum privilege required for their function; they do not hold standing Tier 0 or Tier 1 access unless technically unavoidable
- Service account credentials are stored in the secret management system and rotated per the Secrets Sprawl And Hardcoded Credentials Policy schedule
- Service accounts that have not authenticated within 90 days are reviewed and revoked if no active use case is confirmed
- Privileged service accounts used in CI/CD pipelines are restricted to the environments they serve; a pipeline service account for development does not have production access

---

## 12. Insider Threat Indicators

Privileged access abuse — whether by a malicious insider or a compromised account — presents distinct indicators. The following trigger mandatory investigation under this policy:

- Privileged account used to access data outside the individual's documented role scope
- Privileged session used to modify audit logs, disable monitoring, or alter security configuration
- Bulk download or export of Confidential or Restricted data from a privileged session
- Privileged account credentials shared between individuals
- Privileged access requested at unusual frequency without corresponding operational justification
- Privileged account active during a period when the named individual is on leave or has departed
- Raw log access outside a documented just-in-time window

---

## 13. Related Documents

- Identity And Credential Governance
- Role Registry
- Secrets Sprawl And Hardcoded Credentials Policy
- Log Integrity And Tamper-Evidence Policy
- Lateral Movement Containment Policy
- Stop State Policy
- Audit And Accountability
- Vendor Offboarding And Revocation
- Social Engineering And Human Manipulation Policy
- Continuous Validation Policy
- Red Team Findings: GFSA-RED-TEAM-FINDINGS-v0.1 Gap F
