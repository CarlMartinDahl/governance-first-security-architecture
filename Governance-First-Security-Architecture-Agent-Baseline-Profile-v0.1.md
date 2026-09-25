# Agent Baseline Profile

**Document ID:** GFSA-AGENT-BASELINE-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-25  
**Classification:** Internal — Restricted  
**Owner:** Governance Authority  

---

## 1. Purpose

This document defines the standard for establishing, maintaining, and using agent baseline profiles within the governed boundary. An agent baseline profile is the authoritative definition of normal, expected behaviour for a specific AI agent — including its permitted actions, typical resource usage, expected call patterns, and declared interaction partners. Without a baseline, anomaly detection and attribution are impossible; there is no reference against which deviation can be measured.

This document answers: *What does normal look like for this agent, and how do we know when it has changed?*

---

## 2. Scope

This document applies to:
- Every AI agent deployed and registered within the governed boundary
- The monitoring layer that observes agent behaviour
- The attribution process (Agent-Attribution-Playbook-v0.1), which depends on baselines as its primary reference
- The capability change gate (Capability-Change-Gate-v0.1), which triggers a baseline update when agent capabilities change

---

## 3. Baseline Profile Structure

Every agent must have a registered baseline profile before it is permitted to operate. The profile consists of five dimensions:

### 3.1 Identity Dimension

| Field | Description |
|---|---|
| Agent ID | Unique, immutable identifier assigned at registration |
| Agent name | Human-readable label for the agent |
| Agent type | Classification: interactive assistant / task agent / orchestrator / monitor |
| Deployment context | Which system, environment, and use case this agent serves |
| System prompt version | Hash of the approved system prompt active for this agent |
| Authorised operator | The human principal responsible for this agent |
| Registration date | When this baseline was established |
| Last reviewed | When this baseline was last validated against actual behaviour |

### 3.2 Capability Dimension

The complete list of tools, APIs, and actions this agent is authorised to invoke:

| Capability | Permitted Scope | Rate Limit | Requires Confirmation? |
|---|---|---|---|
| [Tool/API name] | [Describe permitted inputs/outputs] | [Max calls per hour] | [Yes/No] |

Any capability not listed here is implicitly prohibited. The list must be exhaustive — "general access" is not a permitted entry.

### 3.3 Interaction Dimension

The complete list of systems, agents, and humans this agent is authorised to interact with:

| Interaction Partner | Direction | Permitted Content | Prohibited Content |
|---|---|---|---|
| [Partner identity] | [Inbound / Outbound / Bidirectional] | [Description] | [Description] |

Any interaction partner not listed here is implicitly prohibited.

### 3.4 Resource Dimension

Expected resource consumption under normal operating conditions:

| Resource | Typical Value | Alert Threshold | Hard Limit |
|---|---|---|---|
| Inference calls per hour | [N] | [N × 1.5] | [N × 3] |
| Average tokens per request | [N] | [N × 2] | [N × 4] |
| External API calls per hour | [N] | [N × 2] | [N × 3] |
| Data written per session (bytes) | [N] | [N × 3] | [N × 5] |
| Session duration (minutes) | [N] | [N × 2] | [N × 4] |

Exceeding an alert threshold triggers a monitoring event. Exceeding a hard limit triggers an automatic capability suspension and governance notification.

### 3.5 Temporal Dimension

| Field | Description |
|---|---|
| Permitted operating hours | Time windows during which this agent may be active |
| Expected session length | Typical duration of a single task session |
| Expected idle periods | When the agent is expected to be inactive |
| Scheduled tasks | Any recurring, time-triggered actions |

Activity outside permitted operating hours is flagged immediately as an anomaly.

---

## 4. Baseline Establishment Procedure

1. **Draft the profile:** The AI Operator drafts all five dimensions based on the declared use case and the approved system prompt
2. **Capability verification:** The Security Reviewer confirms that every listed capability has been explicitly authorised through the Capability-Change-Gate-v0.1
3. **Interaction map review:** The Security Reviewer confirms that every listed interaction partner is registered and within the governed boundary, or has been explicitly approved as an external partner
4. **Resource calibration:** During a supervised observation period (minimum 5 operational sessions or 48 hours, whichever is longer), actual resource usage is recorded and compared against the draft profile; thresholds are adjusted if the draft was materially inaccurate
5. **Governance Authority approval:** The completed profile is approved and signed; the signed profile hash is registered in the agent identity registry
6. **Monitoring layer configuration:** The alert and hard-limit thresholds from the profile are loaded into the monitoring layer before the agent is permitted unsupervised operation

---

## 5. Baseline Maintenance

A baseline profile must be updated whenever:

| Trigger | Required Action |
|---|---|
| Agent capabilities change | Full capability dimension review; Governance Authority re-approval |
| System prompt version changes | Identity dimension updated; new profile hash registered |
| New interaction partner added | Interaction dimension updated; Security Reviewer approval |
| Actual resource usage consistently exceeds alert thresholds | Resource dimension recalibration; Governance Authority notification |
| Scheduled review date reached | Full five-dimension review; re-approval or confirmation of no change |
| Incident involving this agent | Full profile review as part of post-incident root cause analysis |

Scheduled review frequency: **quarterly** for high-capability agents; **semi-annually** for low-capability or restricted agents.

A profile that has not been reviewed within its scheduled period is automatically flagged as **stale**. An agent running against a stale profile may not have its capabilities extended; it may be suspended at the Governance Authority's discretion.

---

## 6. Anomaly Detection Integration

The monitoring layer uses the baseline profile as its primary reference. An anomaly is any observed agent behaviour that deviates from the baseline in one or more dimensions:

| Anomaly Type | Dimension | Severity |
|---|---|---|
| Call to a tool not in the capability list | Capability | Critical |
| Interaction with a partner not in the interaction list | Interaction | Critical |
| Resource usage exceeds hard limit | Resource | High |
| Activity outside permitted operating hours | Temporal | High |
| Resource usage exceeds alert threshold | Resource | Medium |
| Unusual sequence of permitted calls (pattern anomaly) | Capability | Medium |
| Session significantly longer than expected | Temporal | Low |

Critical and High anomalies must be escalated to the Attribution Playbook workflow immediately. Medium anomalies are logged and reviewed at the next scheduled monitoring review. Low anomalies are logged.

---

## 7. Baseline Profile Registry

All approved baseline profiles are stored in the agent baseline registry:
- One entry per deployed agent instance
- Append-only version history (prior approved versions retained indefinitely)
- Access restricted to: AI Operator (read), Security Reviewer (read/write draft), Governance Authority (approve)
- The registry is itself an auditable asset; all access is logged

---

## 8. Related Documents

- Agent-Attribution-Playbook-v0.1
- Agentic-Identity-Security-Conceptual-Foundation-v0.1
- Agentic-Operational-Boundary-v0.1
- Capability-Change-Gate-v0.1
- Audit-And-Accountability-v0.1
- Log-Integrity-And-Tamper-Evidence-v0.1
- Stop-State-Policy-v0.1
- Identity-And-Credential-Governance-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
