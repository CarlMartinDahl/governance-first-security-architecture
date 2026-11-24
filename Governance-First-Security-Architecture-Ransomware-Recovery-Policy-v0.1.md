# Governance-First Security Architecture
## Ransomware Recovery Policy
**Version:** 0.1 — Initial Release
**Status:** Draft / Review-Stage Template (`LM-1_REVIEW_PACKAGE` — Not Approved for Production or Compliance Use)
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
Recovery from the air-gapped backup is verified through the restoration testing required in Section 4.1; in addition, a full recovery test with a documented recovery time measurement must be performed at minimum annually. The maximum acceptable recovery time is defined in the governance record and reviewed by the board or equivalent.

### 4.3 Named Decision Authorities
Before an incident, the following roles must be named and alternates designated:
- **Ransomware Incident Commander** — overall incident authority (`ROLE_INCIDENT_REVIEWER` / designated executive commander)
- **Payment Decision Authority** — executive/Board-level corporate authority (CEO / CFO / Board delegate, mapped in `Role-Registry-v0.1` to `ROLE_SYSTEM_OWNER` and `ROLE_APPROVER`) with mandatory `ROLE_LEGAL_COMPLIANCE_REVIEWER` (specialized external counsel) and statutory DPO consultation where personal data is affected; the only authority permitted to approve ransom payment consideration
- **Legal Counsel Contact** — engaged immediately upon incident declaration
- **Data Protection Officer (DPO) / Privacy Lead** — engaged immediately when personal data availability, integrity, or confidentiality is impacted
- **Law Enforcement Liaison** — designated contact for reporting obligations
- **Communications Authority** — authorised to communicate externally about the incident

---

## 5. Incident Response: Phase 1 — Containment (0–4 hours)

1. **Isolate affected systems** immediately — disconnect from network; do not power off (preserve forensic evidence in memory where possible)
2. **Declare ransomware incident** — activates this policy and the Recovery Rollback Incidents process
3. **Engage named authorities** — Incident Commander, Legal Counsel, DPO/Privacy Lead, and Communications Authority notified within 1 hour
4. **Preserve air-gapped backup integrity** — confirm air-gapped backup has not been reached; if uncertain, treat as compromised
5. **Assess availability, integrity, and exfiltration impact** — under GDPR Art. 4(12) and EDPB Guidelines 01/2021, ransomware **encryption/unavailability alone** is a personal data breach even without exfiltration; assess both encryption impact and potential exfiltration immediately to inform statutory notification clocks regardless of payment decision
6. **Do not pay and do not negotiate** — Payment Decision Authority has not yet convened; no individual has authority to initiate contact with attackers at this stage

---

## 6. Incident Response: Phase 2 — Assessment (4–24 hours)

1. **Scope the infection** — identify which systems are encrypted, which are clean, and the likely entry point
2. **Identify the variant** — determine ransomware family; consult public decryption resources before payment is considered
3. **Assess backup viability** — test restoration from clean backup copy; confirm backup data is not itself encrypted or corrupted
4. **Assess personal-data breach & NIS2/AI Act scope** — identify affected personal data (confidentiality, integrity, and availability impact) and determine whether the organisation acts as Controller (Art. 33(1) 72-hour supervisory authority assessment) or Processor (Art. 33(2) notification to Controller without undue delay); evaluate **NIS2 Art. 23 24-hour early warning** and **EU AI Act Art. 73** serious-incident triggers if governed AI systems are impacted
5. **Convene Payment Decision Authority** — with specialized legal counsel, assess: recovery without payment feasibility, insurance coverage, sanctions and AML/terrorist-financing screening (paying sanctioned threat actors is a criminal offence in many jurisdictions), national payment prohibitions, and law enforcement reporting deadlines

---

## 7. The Payment Decision

This is the highest-stakes governance decision in a ransomware incident. The following framework governs it.

### 7.1 Who Decides
Only the named executive/Board-level Payment Decision Authority (`ROLE_SYSTEM_OWNER` / `ROLE_APPROVER` with CEO/CFO/Board mandate), with specialized legal counsel (`ROLE_LEGAL_COMPLIANCE_REVIEWER`) present, may authorise exploration of payment. No other individual or role has this authority.

### 7.2 Prerequisites Before Payment Is Considered
- Restoration from backup has been assessed as infeasible within acceptable recovery time, OR backup has been confirmed compromised
- Legal counsel has confirmed that payment does not violate sanctions, AML, counter-terrorist financing, or national statutory prohibitions
- Cyber insurance provider has been notified and their policy and statutory reimbursement requirements confirmed
- Law enforcement has been notified within any applicable national statutory window (for example, jurisdictions requiring a formal police complaint within 72 hours as a legal prerequisite for cyber-insurance ransom reimbursement)

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
| GDPR Art. 33(1) notification to supervisory authority (Controller) | Personal data confidentiality, integrity, **or availability** breach (including encryption without exfiltration), unless unlikely to result in risk to rights and freedoms | Without undue delay and, where feasible, within **72 hours** of becoming aware (phased reporting permitted under Art. 33(4)) |
| GDPR Art. 33(2) notification (Processor) | Organisation acts as a Data Processor and becomes aware of a personal data breach | Notify the **Data Controller** without undue delay (do not notify DPA directly) |
| GDPR Art. 34 notification to affected individuals | Breach is **likely** to result in a high risk to individuals' rights and freedoms (subject to Art. 34(3) exceptions) | Without undue delay |
| NIS2 Directive Art. 23 reporting (covered entities) | Significant incident affecting service continuity or security | **24 hours** early warning; **72 hours** incident notification; **1 month** final report |
| EU AI Act Art. 73 serious incident reporting (where high-risk AI affected) | Serious incident involving a high-risk AI system | **2 days** (widespread infringement / critical infrastructure); **10 days** (death); **15 days** (general serious incident) |
| Law enforcement reporting | Recommended in all cases; legally required in some jurisdictions for insurance reimbursement | As early as feasible (verify national statutory deadlines, e.g., 72h) |
| Insurance notification | Policy requirement | Per policy terms; typically immediate |

Under EDPB Guidelines 9/2022, GDPR "awareness" begins when the controller has a **reasonable degree of certainty** that a security incident has occurred leading to personal data compromise; brief initial verification is permitted, and remaining factual uncertainty is handled via phased notifications (GDPR Art. 33(4)) rather than delaying past 72 hours.

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
