# Governance-First Security Architecture
## Business Continuity And Disaster Recovery Governance
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy governs the organisation's ability to sustain critical operations during disruption and recover systems and data after failure. Business continuity and disaster recovery are governance disciplines, not only technical ones: the decisions about which systems are critical, what recovery time is acceptable, who has authority to declare a disaster, and when recovery is complete are governance decisions that must be made before a disruption occurs, not during one.

This policy defines recovery objectives, system criticality classification, testing obligations, and the governance structure for continuity decisions.

---

## 2. Scope

Applies to all systems, data, and processes that support organisational operations, including third-party and cloud-hosted systems where the organisation depends on availability. Covers planned and unplanned disruptions: infrastructure failure, data corruption, ransomware, supply chain failure, natural events, and loss of key personnel.

---

## 3. Core Governance Principle

> **Recovery objectives are governance commitments, not engineering estimates. An RTO or RPO that has not been tested is a hypothesis. A continuity plan that has not been rehearsed is a document. Governance treats untested recovery capability as no recovery capability.**

---

## 4. Recovery Objective Definitions

| Term | Definition |
|---|---|
| RTO (Recovery Time Objective) | Maximum acceptable time from disruption to restored operation |
| RPO (Recovery Point Objective) | Maximum acceptable data loss expressed as time — how old the most recent recoverable state may be |
| MTTR (Mean Time To Recover) | Observed average recovery time across actual incidents and tests; compared to RTO to assess programme effectiveness |
| MTO (Maximum Tolerable Outage) | The absolute maximum time the organisation can sustain disruption before the impact becomes unrecoverable |

RTO must be shorter than MTO. RPO must align with backup frequency. Where they do not, it is a finding.

---

## 5. System Criticality Classification

All systems are assigned a criticality tier that determines their recovery priority and objective requirements:

| Tier | Description | RTO | RPO |
|---|---|---|---|
| Tier 1 — Mission Critical | Failure causes immediate operational halt or regulatory breach | < 4 hours | < 1 hour |
| Tier 2 — Business Critical | Failure significantly impairs operations; workarounds exist but degrade capability | < 24 hours | < 4 hours |
| Tier 3 — Important | Failure causes inconvenience; manual processes can substitute temporarily | < 72 hours | < 24 hours |
| Tier 4 — Non-Critical | Failure has minimal operational impact | Best effort | Best effort |

Criticality is assigned by the system owner in the Asset Register and reviewed annually or following any significant change to the system's role.

AI systems with operational authority (Tier B or above actions per the Agentic Operational Boundary) are minimum Tier 2. AI systems with Tier D Stop State authority are minimum Tier 1.

---

## 6. Continuity Strategy Requirements

### 6.1 Tier 1 Systems
- Active-active or active-passive redundancy with automated failover
- Recovery capability is in a separate failure domain from the primary system
- Backup and recovery tested at minimum quarterly
- Runbook documented and accessible without dependency on the failed system

### 6.2 Tier 2 Systems
- Backup and recovery tested at minimum semi-annually
- Runbook documented and accessible offline
- Recovery dependencies (credentials, configurations, documentation) stored in a location independent of the system being recovered

### 6.3 Tier 3 And Tier 4 Systems
- Backup tested at minimum annually
- Basic recovery procedure documented

### 6.4 All Tiers
- Recovery credentials and access are stored in the secret management system with break-glass access available offline
- No recovery procedure may depend solely on a system that is itself unavailable during the disruption scenario it is designed to address

---

## 7. Backup Governance

- Backup strategy follows the 3-2-1-1 model defined in the Ransomware Recovery Policy: three copies, two media types, one offsite, one offline/air-gapped
- Backup integrity is verified at minimum monthly through restore testing, not only backup job success logs — a successful backup job that produces an unrestorable backup is not a backup
- Backup encryption uses approved algorithms per the Cryptographic Standards Policy
- Backup access credentials are rotated per the Secrets Sprawl And Hardcoded Credentials Policy schedule
- Backups of Restricted data are subject to the same access controls as the source data
- Backup retention periods align with the Data Classification And Handling Policy and applicable regulatory requirements

---

## 8. Disaster Declaration Governance

A disaster declaration activates the full continuity response. It is a governance decision, not an automatic technical trigger:

- **Authority to declare**: the named Continuity Governance role in the Role Registry, or the Stop State authority if the Continuity role is unavailable
- **Threshold**: declaration is triggered when a disruption is expected to exceed the MTO of one or more Tier 1 systems, or when restoration within RTO is not achievable through normal incident response
- **Declaration activates**: alternate site or mode activation, external communication protocols, regulatory notification assessment, and escalated recovery resource allocation
- **Declaration is logged** with timestamp, declaring authority, and rationale
- **Undeclaring**: recovery is not complete until the Continuity Governance role confirms that affected systems meet their normal operational criteria — not merely that they are technically available

---

## 9. Continuity Testing Programme

Untested continuity is not continuity. The testing programme:

| Test Type | Frequency | Description |
|---|---|---|
| Backup restore test | Monthly | Restore a sample of production data from backup and verify integrity |
| Tabletop exercise | Semi-annual | Governance and technical leads walk through a disruption scenario without activating systems |
| Functional recovery test | Annual | Tier 1 and Tier 2 systems are recovered to alternate environment and validated |
| Full continuity exercise | Every 2 years | End-to-end simulation including disaster declaration, recovery, and return-to-normal |

- Test results are documented with findings, gaps, and remediation actions
- Findings are tracked in the Risk And Action Taxonomy
- A test that reveals a gap in recovery capability is treated as a finding, not a failure of the test programme — the test succeeded by revealing the gap
- Personnel responsible for recovery procedures participate in testing; a procedure that only its author can execute is a single point of failure

---

## 10. Third-Party And Cloud Dependency

- Third-party systems that the organisation depends on for Tier 1 or Tier 2 operations are assessed for their own continuity capability under Third-Party Governance
- SLA commitments from providers are compared against the organisation's RTO/RPO requirements; gaps are documented as risks
- The organisation does not treat a provider's SLA as equivalent to tested recovery capability
- Exit and portability plans exist for all Tier 1 and Tier 2 cloud or third-party dependencies: if the provider becomes unavailable, what is the recovery path?
- Provider continuity incidents are tracked as supply chain risks under Supply Chain Abuse Cases governance

---

## 11. Key Person Dependency

Continuity is not only a technical problem. Loss of key personnel — through illness, departure, or unavailability during a crisis — is a continuity risk:

- Recovery procedures are documented in sufficient detail to be executed by someone other than their primary owner
- Critical credentials and access are not sole-custody: at minimum two named individuals can access each Tier 1 system's recovery credentials
- The Role Registry identifies single points of failure in governance authority and defines backup authority for each named role
- Knowledge transfer requirements for critical roles are part of the offboarding process under Vendor Offboarding And Revocation and the Role Registry

---

## 12. Return To Normal Operations

Recovery is not complete when systems are technically available. Return to normal requires:

1. **Integrity verification** — recovered systems and data are verified against known-good states before production use resumes
2. **Security posture confirmation** — the incident or disruption has not left residual access, compromised credentials, or weakened controls
3. **Audit log continuity** — the audit trail covers the disruption period; gaps in logging are documented
4. **Root cause documented** — the cause of the disruption is understood before normal operations resume
5. **Governance sign-off** — the Continuity Governance role formally closes the incident
6. **Post-incident review** — findings feed into the Risk And Action Taxonomy and continuity programme within 30 days

---

## 13. Relationship To Ransomware Recovery

The Ransomware Recovery Policy governs the specific case of ransomware attack, including payment decision governance, sanctions screening, and cryptographic key considerations. This policy governs continuity and recovery broadly. In a ransomware incident, both policies apply: this policy provides the continuity framework and recovery objectives; the Ransomware Recovery Policy provides the attack-specific response protocol.

---

## 14. Related Documents

- Ransomware Recovery Policy
- Recovery Rollback Incidents
- Asset Register
- Role Registry
- Third-Party Governance
- Supply Chain Abuse Cases
- Data Classification And Handling Policy
- Cryptographic Standards Policy
- Secrets Sprawl And Hardcoded Credentials Policy
- Log Integrity And Tamper-Evidence Policy
- Agentic Operational Boundary
- Stop-State Policy
- Risk And Action Taxonomy
- Audit And Accountability
