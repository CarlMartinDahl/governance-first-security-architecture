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
- Inference audit logs (every prompt, output, and model decision point)
- API gateway access logs
- Agent identity and token logs
- Network traffic logs
- System and OS security logs
- Stop-state and incident logs
- Governance decision logs (approvals, sign-offs, change records)

---

## 3. Retention Periods

Retention periods are defined by log type and sensitivity. No log may be deleted before its minimum retention period has elapsed.

| Log Type | Minimum Retention | Recommended Retention | Legal Hold Override |
|---|---|---|---|
| Inference audit log (standard) | 12 months | 24 months | Indefinite until hold released |
| Inference audit log (incident window) | Indefinite | Indefinite | N/A — never deleted while incident is open |
| API gateway access log | 12 months | 24 months | Indefinite until hold released |
| Agent identity and token log | 24 months | 36 months | Indefinite until hold released |
| Network traffic log | 6 months | 12 months | Indefinite until hold released |
| Stop-state and incident log | Indefinite | Indefinite | N/A |
| Governance decision log | Indefinite | Indefinite | N/A |
| System and OS security log | 6 months | 12 months | Indefinite until hold released |

**Legal hold:** Any log that is, or may become, relevant to a legal proceeding, regulatory investigation, or formal governance review is placed under legal hold. Legal hold supersedes all retention periods; logs under legal hold may not be deleted or rotated without explicit written authorisation from the Governance Authority and, where applicable, legal counsel.

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

### 4.3 Archive Integrity

- Archived log files must be stored in a write-protected volume or object store with immutability enforced at the storage layer
- Archived files must not be accessible for modification by the inference engine, API gateway, or any agent
- Archive integrity must be spot-checked monthly: a random sample of archived files is re-hashed and compared against the rotation manifest

---

## 5. Deletion Procedure

Deletion of logs that have reached their retention period expiry requires:

1. **Retention period confirmation:** The AI Operator confirms in writing that the log's minimum retention period has elapsed
2. **Legal hold check:** The Security Reviewer confirms that no legal hold applies to the log or the time period it covers
3. **Incident window check:** Confirm the log does not cover any period that is still under open incident investigation
4. **Governance Authority approval:** Written approval for deletion, referencing the specific log files and their retention period
5. **Deletion execution:** Secure deletion (overwrite, not just file system removal) by the AI Operator
6. **Deletion record:** The deletion event is recorded in the governance decision log: which files, deletion timestamp, approving identity, and method used

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
| AI Operator | Read access to active logs; write only via system (no direct log editing) |
| Security Reviewer | Read access to all logs including archives |
| Governance Authority | Read access to all logs; approve deletion |
| Automated systems / agents | No direct log access; may write to active log via designated logging interface only |
| External parties | No access without explicit Governance Authority approval and legal basis |

---

## 8. Regulatory Alignment

Retention periods in this policy are set to meet the following baseline requirements; local regulation may require longer periods and always takes precedence:

- **EU AI Act:** Incident and high-risk system logs — minimum 10 years for high-risk AI systems
- **GDPR Article 5(1)(e):** Personal data in logs must not be kept longer than necessary; pseudonymisation or anonymisation required where feasible before the retention period expires
- **NIS2 Directive:** Security incident records — minimum 5 years

Where regulatory requirements exceed the minimums in Section 3, the regulatory requirement applies.

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
