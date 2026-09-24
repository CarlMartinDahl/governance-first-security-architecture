# Governance-First Security Architecture
## Ransomware Recovery Policy
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy establishes the governance framework for responding to and recovering from ransomware incidents. Ransomware requires a distinct governance process from general incident response because it combines data encryption (destroying operational capability), data exfiltration (creating legal and regulatory exposure), extortion demands (creating legal and reputational risk), and accelerated decision timelines (creating pressure to bypass normal governance).

The purpose of this policy is to ensure that decisions made under extreme time pressure are still made with appropriate authority, documented accountability, and awareness of all relevant factors — before those decisions need to be made.

---

## 2. Scope

Applies to any event in which ransomware or ransomware-like behaviour is confirmed or strongly suspected: encryption of organisational data by unauthorised processes, extortion demands, or simultaneous data exfiltration and encryption.

---

## 3. Core Governance Principle

> **The payment decision and the recovery decision are separate governance decisions. Recovery must be possible without payment. The pressure to pay is a feature of the attack, not a fact about available options.**

---

## 4. Pre-Incident: Governance Readiness Requirements

The following must be in place and verified before an incident occurs. Verification is performed annually and after any significant infrastructure change.

### 4.1 Backup Architecture
Backups follow the 3-2-1-1 rule:
- **3** copies of data
- **2** different storage media types
- **1** copy offsite
- **1** copy air-gapped (no network connectivity from production environment to this backup destination)

The air-gapped backup copy must be:
- Written to on a scheduled basis via a one-way data transfer mechanism
- Verified as unreadable from production network after transfer
- Tested for restoration at minimum quarterly
- Stored under physical access control separate from primary data centre

### 4.2 Recovery Time Verification
Recovery from the air-gapped backup must be tested at minimum annually with a documented recovery time measurement. The maximum acceptable recovery time is defined in the governance record and reviewed by the board or equivalent.

### 4.3 Named Decision Authorities
Before an incident, the following roles must be named and alternates designated:
- **Ransomware Incident Commander** — overall incident authority
- **Payment Decision Authority** — the only role authorised to approve ransom payment consideration
- **Legal Counsel Contact** — engaged immediately upon incident declaration
- **Law Enforcement Liaison** — designated contact for reporting obligations
- **Communications Authority** — authorised to communicate externally about the incident

---

## 5. Incident Response: Phase 1 — Containment (0–4 hours)

1. **Isolate affected systems** immediately — disconnect from network; do not power off (preserve forensic evidence in memory where possible)
2. **Declare ransomware incident** — activates this policy and the Recovery Rollback Incidents process
3. **Engage named authorities** — Incident Commander, Legal Counsel, and Communications Authority notified within 1 hour
4. **Preserve air-gapped backup integrity** — confirm air-gapped backup has not been reached; if uncertain, treat as compromised
5. **Assess exfiltration** — determine whether data was exfiltrated before encryption; this determines regulatory notification requirements regardless of payment decision
6. **Do not pay and do not negotiate** — Payment Decision Authority has not yet convened; no individual has authority to initiate contact with attackers at this stage

---

## 6. Incident Response: Phase 2 — Assessment (4–24 hours)

1. **Scope the infection** — identify which systems are encrypted, which are clean, and the likely entry point
2. **Identify the variant** — determine ransomware family; consult public decryption resources before payment is considered
3. **Assess backup viability** — test restoration from clean backup copy; confirm backup data is not itself encrypted or corrupted
4. **Assess exfiltration scope** — identify what data categories may have been exfiltrated; this triggers GDPR breach notification assessment (72-hour clock)
5. **Convene Payment Decision Authority** — with legal counsel, assess: recovery without payment feasibility, insurance coverage, sanctions screening (paying certain threat actors is illegal), law enforcement position

---

## 7. The Payment Decision

This is the highest-stakes governance decision in a ransomware incident. The following framework governs it.

### 7.1 Who Decides
Only the named Payment Decision Authority, with legal counsel present, may authorise exploration of payment. No other individual or role has this authority.

### 7.2 Prerequisites Before Payment Is Considered
- Restoration from backup has been assessed as infeasible within acceptable recovery time, OR backup has been confirmed compromised
- Legal counsel has confirmed that payment does not violate sanctions obligations (paying sanctioned threat actors is a criminal offence in many jurisdictions)
- Cyber insurance provider has been notified and their requirements confirmed
- Law enforcement has been notified (notification does not preclude payment; it creates a record)

### 7.3 Payment Does Not Guarantee Recovery
Decision-makers must understand:
- Payment does not guarantee decryption
- Payment does not guarantee that exfiltrated data will not be published
- Payment funds further criminal operations
- Payment may attract repeat targeting

### 7.4 Documentation
All deliberations and the final decision — whether to pay or not — are documented with named participants, timestamps, and rationale. This documentation is treated as legal-hold material.

---

## 8. Recovery Process

1. **Rebuild from clean state** — do not restore encrypted systems; rebuild from known-good images and restore data from clean backup
2. **Verify backup integrity before restoration** — hash verification of backup data before deployment
3. **Patch the entry point** — the attack vector must be closed before any system is reconnected to the network
4. **Staged reconnection** — systems are reconnected in stages with monitoring at each stage before proceeding
5. **Confirm attacker eviction** — before declaring recovery complete, confirm no persistent access mechanisms (backdoors, scheduled tasks, modified credentials) remain
6. **Post-incident review** — root cause analysis, gap identification, and governance improvement within 30 days

---

## 9. Regulatory And Legal Obligations

| Obligation | Trigger | Timeline |
|---|---|---|
| GDPR breach notification to supervisory authority | Personal data confirmed or likely exfiltrated | 72 hours from awareness |
| GDPR notification to affected individuals | High risk to individuals confirmed | Without undue delay |
| NIS2 / sector reporting | Significant impact on service continuity | Per applicable regulation |
| Law enforcement reporting | Recommended in all cases | As early as feasible |
| Insurance notification | Policy requirement | Per policy terms; typically immediate |

The 72-hour GDPR clock runs from when the organisation becomes aware of a breach — not from when it is confirmed. Uncertainty does not pause the clock.

---

## 10. Communication Governance

- Only the named Communications Authority speaks publicly about the incident
- Internal communications are controlled — staff should be informed of what they may and may not say externally
- Attacker communications (ransom notes, negotiation channels) are handled only by designated individuals; no employee should engage independently
- Customer and partner communications are drafted with legal counsel review before sending

---

## 11. Related Documents

- Recovery Rollback Incidents
- Stop State Policy
- Log Integrity And Tamper-Evidence Policy
- GDPR EU AI Act Alignment
- Audit And Accountability
- Vendor Offboarding And Revocation
- Lateral Movement Containment Policy
