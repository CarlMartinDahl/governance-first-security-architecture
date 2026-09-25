# Monitoring and Detection Operations

**Document ID:** GFSA-MONITORING-DETECTION-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-25  
**Classification:** Internal — Restricted  
**Owner:** Governance Authority  

---

## 1. Purpose

This document defines how real-time monitoring of AI agents and the governed boundary is organised, what signals trigger alerts, how those alerts are triaged, and who is responsible for acting on them. It is the operational layer that connects the static baseline definitions in Agent-Baseline-Profile-v0.1 to the dynamic, continuous surveillance required for timely detection of hostile or compromised behaviour.

This document answers: *What are we watching, how do we watch it, what triggers an alert, and who responds?*

---

## 2. Scope

This document applies to:
- All AI agents registered in the governed boundary
- The inference engine and API gateway layer
- Network traffic within and at the boundary of the AI inference segment
- Audit log streams
- System and OS health signals from AI host machines
- Identity and token activity

---

## 3. Monitoring Architecture

The monitoring layer consists of four components that must each be operational before any agent is permitted unsupervised activity:

```
┌──────────────────────────────────────────────────────────┐
│                  GOVERNED BOUNDARY                       │
│                                                          │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────────┐  │
│  │   Agents    │  │ API Gateway  │  │ Inference Eng. │  │
│  └──────┬──────┘  └──────┬───────┘  └───────┬────────┘  │
│         │                │                  │            │
│         └────────────────┴──────────────────┘            │
│                          │                               │
│              ┌───────────▼───────────┐                   │
│              │   Log Collector       │                   │
│              │   (append-only,       │                   │
│              │    tamper-evident)    │                   │
│              └───────────┬───────────┘                   │
│                          │                               │
│              ┌───────────▼───────────┐                   │
│              │   Detection Engine    │                   │
│              │   (rule + baseline    │                   │
│              │    comparison)        │                   │
│              └───────────┬───────────┘                   │
│                          │                               │
│         ┌────────────────┴─────────────────┐             │
│         │                                  │             │
│  ┌──────▼──────┐                  ┌────────▼──────────┐  │
│  │  Alert      │                  │  Monitoring       │  │
│  │  Queue      │                  │  Dashboard        │  │
│  └──────┬──────┘                  └───────────────────┘  │
│         │                                                 │
└─────────┼─────────────────────────────────────────────── ┘
          │
    ┌─────▼──────────────────┐
    │  AI Operator / On-call │
    │  (human triage)        │
    └────────────────────────┘
```

**Components:**
- **Log Collector:** Receives structured log streams from all monitored sources; append-only; integrity-protected per Log-Integrity-And-Tamper-Evidence-v0.1
- **Detection Engine:** Applies rule-based and baseline-comparison detection continuously against incoming log data
- **Alert Queue:** Holds generated alerts pending human triage; alerts are never auto-resolved without human acknowledgement
- **Monitoring Dashboard:** Real-time view of agent activity, resource usage, and open alerts; read-only for all roles except the system itself

---

## 4. Detection Signal Sources

| Signal Source | What Is Monitored | Collection Method |
|---|---|---|
| Agent audit log | Every action, tool call, and decision point per agent | Structured log stream (JSON Lines) |
| API gateway access log | Authentication events, token usage, request rates | Log forwarding from gateway |
| Network traffic | Inbound/outbound connections, blocked attempts, volume | Network tap or flow logs |
| Inference engine log | Model load events, resource consumption, errors | Structured log stream |
| OS and host log | Login events, process starts, file system changes, resource usage | Syslog forwarding |
| Identity registry | Token issuance, revocation, validation failures | Event stream from registry |
| Baseline comparison | Deviation from registered agent baseline profile | Computed by detection engine |

All signal sources must be active and confirmed delivering data before an agent session begins. A missing or silent signal source is treated as a monitoring failure and triggers an alert.

---

## 5. Detection Rules

### 5.1 Hard Rules (Always Alert — Critical)

These conditions always generate a Critical alert regardless of baseline:

| Rule ID | Condition | Rationale |
|---|---|---|
| HR-01 | Agent calls a tool not in its baseline capability list | Explicit boundary violation |
| HR-02 | Agent interacts with a partner not in its baseline interaction list | Unauthorised communication |
| HR-03 | Outbound network connection from inference engine to external IP | Potential exfiltration |
| HR-04 | Authentication token used after revocation timestamp | Credential replay attack |
| HR-05 | Log stream silent for > 2 minutes during active session | Potential log suppression |
| HR-06 | Agent process spawns a child process not in approved process list | Potential code execution |
| HR-07 | System prompt hash at runtime does not match approved hash | Configuration tampering |
| HR-08 | Agent activity detected outside permitted operating hours | Temporal boundary violation |
| HR-09 | Multiple failed authentication attempts from same agent identity | Potential credential stuffing or brute force |
| HR-10 | Agent attempts to read or write the audit log directly | Potential evidence tampering |

### 5.2 Threshold Rules (Alert When Baseline Exceeded)

These conditions generate alerts when the thresholds defined in the agent's baseline profile are exceeded:

| Rule ID | Condition | Default Severity |
|---|---|---|
| TR-01 | Inference calls per hour exceeds alert threshold | High |
| TR-02 | Inference calls per hour exceeds hard limit | Critical |
| TR-03 | Average tokens per request exceeds alert threshold | Medium |
| TR-04 | External API calls per hour exceeds alert threshold | High |
| TR-05 | Data written per session exceeds alert threshold | High |
| TR-06 | Session duration exceeds alert threshold | Medium |
| TR-07 | Storage volume reaches 80% capacity | Medium |
| TR-08 | Storage volume reaches 95% capacity | High |

### 5.3 Pattern Rules (Alert on Behavioural Anomaly)

These conditions detect unusual sequences or combinations of permitted actions:

| Rule ID | Condition | Default Severity |
|---|---|---|
| PR-01 | Agent calls the same tool > N times in rapid succession (N from baseline) | Medium |
| PR-02 | Agent accesses an unusual combination of data types within one session | Medium |
| PR-03 | Agent requests escalation or human confirmation significantly more than baseline | Low |
| PR-04 | Agent output volume spikes relative to input volume | Medium |
| PR-05 | Agent session terminates abnormally (no clean shutdown signal) | High |
| PR-06 | Multiple agents show identical anomalous pattern within same time window | Critical — possible coordination |

---

## 6. Alert Severity and Response Requirements

| Severity | Response Time | Required Action | Escalation |
|---|---|---|---|
| **Critical** | Immediate (≤ 15 min) | AI Operator must triage; initiate evidence freeze; notify Governance Authority | Auto-escalate to Attribution SLA SEV-1 if not acknowledged within 15 min |
| **High** | ≤ 1 hour | AI Operator triages; assesses whether quarantine is warranted | Escalate to Governance Authority if quarantine required |
| **Medium** | ≤ 4 hours | AI Operator reviews; logs finding; determines if escalation is needed | Escalate to Security Reviewer if pattern suggests systemic issue |
| **Low** | Next scheduled review (≤ 7 days) | Logged; reviewed in batch at next monitoring review | Escalate to Medium if same agent generates > 3 Low alerts within 7 days |

No alert may be closed without a documented triage decision. Auto-closing or bulk-dismissing alerts without individual review is prohibited.

---

## 7. Triage Procedure

When an alert is generated, the AI Operator follows this triage sequence:

1. **Acknowledge** the alert in the alert queue (stops auto-escalation timer)
2. **Classify** the alert: true positive, false positive, or indeterminate
3. **For true positives:**
   - Initiate evidence freeze immediately (per Agent-Attribution-Playbook-v0.1 Section 4.2)
   - Assess whether quarantine is warranted (per Active-Neutralization-Runbook-v0.1 Track 1)
   - Escalate to Governance Authority per Attribution-SLA-Policy-v0.1
4. **For false positives:**
   - Document the reason the rule fired incorrectly
   - Determine whether the rule requires tuning or whether the baseline profile requires updating
   - No rule may be permanently disabled without Governance Authority approval
5. **For indeterminate:**
   - Treat as a true positive until evidence shows otherwise
   - Escalate to Security Reviewer for second opinion
   - Do not close the alert until resolved

---

## 8. Monitoring Coverage Requirements

The monitoring layer must maintain the following coverage at all times:

| Requirement | Minimum Standard |
|---|---|
| Log collection latency | Logs must appear in the detection engine within 60 seconds of generation |
| Detection engine uptime | 99.5% during any rolling 30-day period |
| Alert delivery latency | Critical alerts must reach the AI Operator within 2 minutes of detection |
| Baseline profile load | All registered agent baselines loaded before any agent session begins |
| Signal source verification | All signal sources confirmed active at start of each operational day |
| False positive rate | Reviewed quarterly; action required if > 20% of alerts are false positives |

If any coverage requirement is not met, the AI Operator must notify the Governance Authority within 1 hour and document the monitoring gap. Agents must not operate during a monitoring gap without explicit Governance Authority authorisation.

---

## 9. Monitoring Reviews

| Review Type | Frequency | Owner | Output |
|---|---|---|---|
| Daily signal source check | Daily (start of operational day) | AI Operator | Confirmation log entry |
| Alert backlog review | Weekly | AI Operator | Closed or escalated alerts; no open Low alerts older than 7 days |
| False positive and rule tuning review | Quarterly | Security Reviewer + AI Operator | Rule adjustments; baseline updates |
| Full monitoring effectiveness review | Semi-annually | Governance Authority | Coverage metrics; SLA performance; capability gaps |
| Post-incident monitoring review | After every SEV-1 or SEV-2 incident | Governance Authority | Did monitoring detect the incident in time? What gaps were revealed? |

---

## 10. Monitoring Failure as a Stop Condition

The following monitoring failures are stop conditions that halt agent operation:

| Failure | Action |
|---|---|
| Detection engine offline for > 5 minutes during active session | Suspend all active agent sessions immediately; notify Governance Authority |
| Log collector fails to deliver data for > 2 minutes (HR-05) | Treat as active incident; initiate evidence freeze on last known state |
| Alert queue unavailable | Suspend new agent sessions; do not start new sessions without alert delivery confirmed |
| Baseline profiles fail to load | Do not start agent sessions; escalate to AI Operator and Governance Authority |

---

## 11. Related Documents

- Agent-Baseline-Profile-v0.1
- Agent-Attribution-Playbook-v0.1
- Active-Neutralization-Runbook-v0.1
- Attribution-SLA-Policy-v0.1
- Log-Integrity-And-Tamper-Evidence-v0.1
- Log-Retention-And-Rotation-Policy-v0.1
- Agentic-Operational-Boundary-v0.1
- Stop-State-Policy-v0.1
- Audit-And-Accountability-v0.1
- Network-Segmentation-Architecture-v0.1
- Private-AI-Deployment-Guide-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
