# Log Retention and Rotation Policy

**Document ID:** GFSA-LOG-RETENTION-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-25  
**Classification:** Internal  
**Owner:** Governance Authority  

---

## 1. Purpose

This document defines the requirements for how long audit logs generated within the governed AI boundary must be retained, how they are rotated when volume limits are reached, and what must happen when retention periods expire. Without defined retention rules, logs either accumulate without bound (creating storage and performance risks) or are deleted prematurely (destroying evidence needed for attribution, accountability, and regulatory compliance).

This document answers: *How long must logs be kept, what happens when storage fills up, and how is deletion authorised?*

---

## 2. Scope

This policy applies to all log types generated within the governed boundary:
- Inference audit logs (structured metadata, decision events, and cryptographic content hashes — **not** raw verbatim personal-data prompts/outputs in WORM storage by default; see Section 4.3)
- API gateway access logs
- Agent identity and token logs
- Network traffic logs
- System and OS security logs
- Stop-state and incident logs
- Governance decision logs (approvals, sign-offs, change records)

---

## 3. Retention Periods

Retention periods are defined by log type and sensitivity. No log may be deleted before its minimum retention period has elapsed, and logs containing personal data must not be retained past their maximum ceiling unless subject to a documented, periodically reviewed **Legal Hold** (GDPR Art. 17(3)(e)).

| Log Type | Minimum Retention | Maximum Retention Ceiling (with Personal Data) | Post-Expiry Action | Legal Hold Override |
|---|---|---|---|---|
| Inference audit log (standard metadata & hashes) | 6 months (EU AI Act Arts. 19(1)/26(6) floor for high-risk systems where applicable) | 12–24 months (or shorter per GDPR necessity) | Anonymise/pseudonymise or securely destroy | Time-reviewed hold until released by Legal Counsel |
| Inference audit log (incident window) | 12 months post-incident closure | 36 months post-closure (unless under Legal Hold) | Anonymise or securely destroy | Time-reviewed hold until released by Legal Counsel |
| API gateway access log | 6 months | 12 months | Securely destroy | Time-reviewed hold until released by Legal Counsel |
| Agent identity and token log | 12 months | 24 months | Anonymise or securely destroy | Time-reviewed hold until released by Legal Counsel |
| Network traffic log | 90 days | 6 months | Securely destroy | Time-reviewed hold until released by Legal Counsel |
| Stop-state and incident log | 12 months post-closure | 36 months (de-identified summary retained longer if needed) | Strip personal identifiers or securely destroy | Time-reviewed hold until released by Legal Counsel |
| Governance decision log | 24 months | 60 months (or statutory corporate/regulatory ceiling; personal identifiers minimised) | Anonymise actor identifiers or archive per statutory ceiling | Time-reviewed hold until released by Legal Counsel |
| System and OS security log | 6 months | 12 months | Securely destroy | Time-reviewed hold until released by Legal Counsel |

**Legal hold:** Any log that is, or may become, relevant to a legal proceeding, regulatory investigation, or formal governance review is placed under a documented Legal Hold (GDPR Art. 17(3)(e)). Legal holds must specify scope, legal basis, named legal owner (`ROLE_LEGAL_COMPLIANCE_REVIEWER`), and a mandatory semi-annual review date; logs under legal hold may not be deleted or rotated without explicit written authorisation from `ROLE_LEGAL_COMPLIANCE_REVIEWER` and the Governance Authority (`ROLE_SYSTEM_OWNER` / `ROLE_GOVERNANCE_REVIEWER`).

---

## 4. Log Rotation

Log rotation is the process of managing active log files when they reach a defined size or age threshold, to maintain system performance without deleting retained data.

### 4.1 Rotation Triggers

| Trigger | Action |
|---|---|
| Log file reaches maximum size (default: 500 MB) | Close current file; open new file; archive closed file |
| Log file reaches maximum age (default: 7 days) | Close current file regardless of size; open new file; archive closed file |
| Storage volume reaches 80% capacity | Alert AI Operator; initiate capacity review |
| Storage volume reaches 95% capacity | Alert Governance Authority; suspend non-critical log categories if necessary |

### 4.2 Rotation Procedure

1. The closing log file is hashed (SHA-256) and the hash is recorded in a rotation manifest
2. The file is compressed and moved to the archive volume
3. The rotation event is recorded in the governance decision log: filename, hash, timestamp, operator identity
4. The new log file opens and begins receiving entries
5. The rotation manifest is itself integrity-protected and stored separately from the log archive

### 4.3 Archive Integrity & GDPR Payload Separation

- Archived log metadata and hash manifests must be stored in a write-protected volume or object store with immutability (WORM) enforced at the storage layer for the active retention window (time-bounded WORM lock matching the retention ceiling — never an unbounded permanent lock on personal data)
- **GDPR Art. 5(1)(c), 5(1)(e), and Art. 17 reconciliation:** Raw verbatim prompts, outputs, and direct personal identifiers must **not** be written directly into immutable WORM objects by default. Where payload inspection is legally justified, personal-data payloads must be redacted/tokenised at ingestion or stored in a separate erasable/crypto-shreddable store referenced by hash from the WORM audit log, enabling lawful erasure (Art. 17) and retention expiry without breaking tamper-evidence
- Where an erasure request (GDPR Art. 17) targets security audit metadata, `ROLE_PRIVACY_REVIEWER` (with DPO consultation) and `ROLE_LEGAL_COMPLIANCE_REVIEWER` must document whether the Art. 17(3)(b) legal-obligation or Art. 17(3)(e) legal-claims exemption applies
- Archived files must not be accessible for modification by the inference engine, API gateway, or any agent
- Archive integrity must be spot-checked monthly: a random sample of archived files is re-hashed and compared against the rotation manifest

---

## 5. Deletion Procedure

Deletion of logs that have reached their retention period expiry requires:

1. **Retention period confirmation:** The AI Operator (`ROLE_INCIDENT_REVIEWER` / `ROLE_SECURITY_REVIEWER` operations function) confirms in writing that the log's minimum retention period has elapsed
2. **Legal hold check:** `ROLE_LEGAL_COMPLIANCE_REVIEWER` confirms in writing that no active legal hold applies to the log or the time period it covers
3. **Privacy / retention oversight:** `ROLE_PRIVACY_REVIEWER` (with DPO consultation where required) confirms alignment with personal-data retention schedules and any pending DSARs
4. **Incident window check:** Confirm the log does not cover any period that is still under open incident investigation
5. **Governance Authority approval:** Written approval for deletion from Governance Authority (`ROLE_SYSTEM_OWNER` / `ROLE_GOVERNANCE_REVIEWER`), referencing the specific log files and their retention period
6. **Deletion execution:** Secure deletion (cryptographic erasure or overwrite, not merely file-system unlink) by the AI Operator
7. **Deletion record:** The deletion event is recorded in the governance decision log: which files, deletion timestamp, approving identities, and method used

Deletion without following this procedure is a governance violation and must be reported to the Governance Authority immediately.

---

## 6. Capacity Planning

The AI Operator is responsible for maintaining sufficient storage capacity to meet retention requirements. Capacity planning must account for:

- Current log generation rate (measured monthly)
- Retention periods for all active log types
- A safety margin of at least 25% above projected need
- Growth in agent count or inference volume that would increase log generation

Capacity reviews must be conducted **quarterly** and results reported to the Governance Authority. If projected capacity will be exhausted within 90 days, an expansion plan must be submitted within 30 days.

---

## 7. Log Access Controls

| Role | Access Level |
|---|---|
| AI Operator (`ROLE_INCIDENT_REVIEWER` / `ROLE_SECURITY_REVIEWER` ops) | Read access to active logs; write only via system (no direct log editing) |
| `ROLE_SECURITY_REVIEWER` | Read access to all logs including archives |
| `ROLE_LEGAL_COMPLIANCE_REVIEWER` & `ROLE_PRIVACY_REVIEWER` / DPO | Scoped read access for legal hold, DSAR, and regulatory review; confirm legal-hold and privacy disposal checks |
| Governance Authority (`ROLE_SYSTEM_OWNER` / `ROLE_GOVERNANCE_REVIEWER`) | Read access to all logs; approve deletion |
| Automated systems / agents | No direct log access; may write to active log via designated logging interface only |
| External parties | No access without explicit Governance Authority approval, legal review, and verified legal basis |

---

## 8. Regulatory Alignment

Retention and reporting baselines must be verified by qualified legal counsel against applicable EU and Member State law for each deployment:

- **EU AI Act (Regulation (EU) 2024/1689) Arts. 19(1) & 26(6) — Operational Logs:** Automatically generated logs for high-risk AI systems must be retained for a period appropriate to the intended purpose of **at least 6 months**, unless provided otherwise in applicable Union or national law (in particular GDPR, or sectoral financial-institution law).
- **EU AI Act Art. 18(1) — Provider Compliance Documentation (Non-Log Artifacts):** Providers of high-risk AI systems must keep technical documentation (Art. 11), QMS records (Art. 17), EU declarations of conformity (Art. 47), and notified-body decisions for **10 years** after placing on the market or putting into service. This 10-year mandate applies to compliance documentation, **not** to operational inference logs containing personal data.
- **GDPR Article 5(1)(c), 5(1)(e) & Article 17:** Personal data in logs must be minimised at collection, must not be kept longer than necessary for a documented lawful purpose, and must have defined retention ceilings and anonymisation/erasure mechanisms (see Section 4.3).
- **NIS2 Directive (Directive (EU) 2022/2555) Art. 23:** Establishes mandatory incident notification deadlines (**24-hour early warning**, **72-hour incident notification**, and **1-month final report**), not a uniform EU-wide 5-year log retention period. Record retention durations for NIS2-covered entities must be verified against applicable Member State transposition and sectoral law.

Where binding statutory law requires a longer retention period than Section 3, that statutory requirement applies with a documented GDPR legal basis (Art. 6(1)(c)) and proportional data minimisation.

---

## 9. Related Documents

- Log-Integrity-And-Tamper-Evidence-v0.1
- Audit-And-Accountability-v0.1
- Agent-Attribution-Playbook-v0.1
- Stop-State-Registry-v0.1
- Data-Classification-And-Handling-Policy-v0.1
- Recovery-Rollback-Incidents-v0.1
- Private-AI-Deployment-Guide-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
