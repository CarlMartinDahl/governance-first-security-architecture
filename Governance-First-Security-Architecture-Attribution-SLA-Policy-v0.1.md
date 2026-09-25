# Attribution SLA Policy

**Document ID:** GFSA-ATTRIBUTION-SLA-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-25  
**Classification:** Internal  
**Owner:** Governance Authority  

---

## 1. Purpose

This document defines the time-bound service level agreements (SLAs) that govern how quickly attribution analysis must be completed, decisions must be made, and responses must be authorised during a security incident involving AI agents. Without defined time commitments, attribution can drift into a prolonged investigative process while a threat remains active or evidence degrades.

This document answers: *How fast must we move at each stage of attribution, who is accountable for each deadline, and what happens if we miss one?*

---

## 2. Scope

This policy applies to all incidents that trigger the Agent-Attribution-Playbook-v0.1, including:
- Anomalies detected by the monitoring layer that require attribution
- Stop-state events referencing agent behaviour
- Manual escalations by the AI Operator or Governance Authority
- Incidents flagged during audit review

---

## 3. Incident Severity Classification

Attribution SLAs are tiered by incident severity. Severity is assessed at first detection and may be escalated but not downgraded during an active incident.

| Severity | Definition | Examples |
|---|---|---|
| **SEV-1 — Critical** | Active, ongoing harm or imminent threat; containment not yet in place | Agent actively exfiltrating data; coordinated multi-agent attack in progress; stop-state triggered |
| **SEV-2 — High** | Threat is contained (quarantine applied) but not neutralized; significant potential harm | Single agent quarantined pending attribution; supply chain compromise suspected |
| **SEV-3 — Medium** | Anomaly detected; no confirmed harm; monitoring uplifted | Resource threshold exceeded; unexpected tool call; pattern anomaly flagged |
| **SEV-4 — Low** | Minor deviation from baseline; no harm; informational | Session slightly longer than baseline; single low-severity anomaly |

---

## 4. SLA Timetable

### SEV-1 — Critical

| Milestone | Time Limit (from detection) | Accountable Role |
|---|---|---|
| Evidence window frozen | 15 minutes | AI Operator |
| Governance Authority notified | 15 minutes | AI Operator |
| Initial attribution assessment (candidate agents identified) | 1 hour | Security Reviewer |
| Confidence level assigned (SUSPECTED minimum) | 2 hours | Security Reviewer |
| Governance Authority response decision | 3 hours | Governance Authority |
| Neutralization or containment action authorised and initiated | 4 hours | Governance Authority + AI Operator |
| Preliminary attribution record completed | 8 hours | Security Reviewer |
| Full attribution record completed and signed | 24 hours | Governance Authority |

### SEV-2 — High

| Milestone | Time Limit (from detection) | Accountable Role |
|---|---|---|
| Evidence window frozen | 30 minutes | AI Operator |
| Governance Authority notified | 1 hour | AI Operator |
| Initial attribution assessment | 4 hours | Security Reviewer |
| Confidence level assigned | 8 hours | Security Reviewer |
| Governance Authority response decision | 12 hours | Governance Authority |
| Neutralization or containment action initiated (if warranted) | 24 hours | Governance Authority + AI Operator |
| Full attribution record completed and signed | 72 hours | Governance Authority |

### SEV-3 — Medium

| Milestone | Time Limit (from detection) | Accountable Role |
|---|---|---|
| Anomaly logged and assigned | 2 hours | AI Operator |
| Initial review | 24 hours | Security Reviewer |
| Attribution assessment completed (or determination that attribution is not required) | 5 business days | Security Reviewer |
| Governance Authority briefed | 5 business days | Security Reviewer |

### SEV-4 — Low

| Milestone | Time Limit (from detection) | Accountable Role |
|---|---|---|
| Anomaly logged | Automatic (monitoring layer) | System |
| Reviewed at next scheduled monitoring review | Per monitoring schedule (max 7 days) | AI Operator |
| Escalated to SEV-3 if pattern emerges | At review | AI Operator |

---

## 5. SLA Breach Procedure

If any SLA milestone is missed:

1. **The accountable role** must immediately notify the Governance Authority with: which milestone was missed, by how much, and the reason
2. **The Governance Authority** assesses whether the breach increases the risk profile of the incident; if so, severity may be escalated
3. **The breach is recorded** in the incident record and the governance decision log
4. **No SLA breach is acceptable as a reason to skip a milestone** — a missed deadline means the milestone must still be completed, as soon as possible, with the breach documented
5. **Repeated SLA breaches** by the same role trigger a governance review of that role's capacity and competence

---

## 6. Evidence Degradation and Time Pressure

The following evidence types degrade or become unavailable if attribution is delayed:

| Evidence Type | Degradation Risk | Time Horizon |
|---|---|---|
| Agent process memory (if agent still running) | Lost on process termination | Minutes to hours |
| Network traffic logs (if not yet archived) | Overwritten by rotation | Days (per Log-Retention-And-Rotation-Policy-v0.1) |
| External service logs (third-party APIs) | Subject to external retention policies | Hours to days |
| Agent session state | May be cleared by garbage collection | Hours |
| Witness accounts (human operators) | Memory degrades; availability decreases | Days to weeks |

The evidence collection procedure in Section 4.2 of Agent-Attribution-Playbook-v0.1 must be initiated before evidence degradation windows close, regardless of whether the full attribution analysis has begun.

---

## 7. Escalation Authority

Any role may escalate a severity level upward at any time if new information warrants it. Only the Governance Authority may de-escalate a severity level, and only after:
- The evidence supporting the higher severity has been reviewed and found insufficient
- The de-escalation decision is documented in the incident record

---

## 8. Evidence Adjudication Authority

The question of whether an evidence gap is sufficient to block escalation from SUSPECTED to PROBABLE confidence level is decided exclusively by the Governance Authority. The Security Reviewer may recommend, but may not unilaterally decide, that an evidence gap is acceptable for confidence level escalation. This ensures that the risk of acting on incomplete attribution always rests with the accountable governance role, not the technical analyst.

---

## 9. SLA Reporting

SLA performance must be reviewed at each quarterly governance review:
- Number of incidents by severity
- Percentage of milestones met on time, by severity and milestone type
- Root causes of any SLA breaches
- Trend analysis (improving, stable, degrading)

If SLA performance for SEV-1 or SEV-2 incidents falls below 80% milestone compliance over any rolling 12-month period, the Governance Authority must initiate a capability review and remediation plan within 30 days.

---

## 10. Related Documents

- Agent-Attribution-Playbook-v0.1
- Active-Neutralization-Runbook-v0.1
- Stop-State-Policy-v0.1
- Log-Retention-And-Rotation-Policy-v0.1
- Audit-And-Accountability-v0.1
- Agent-Baseline-Profile-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
