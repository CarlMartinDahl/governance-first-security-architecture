# CA-06: Lateral Peer Coordination Rule

**Document ID:** GFSA-CA-06-LATERAL-PEER-COORDINATION-RULE-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-26  
**Classification:** Internal — Restricted  
**Owner:** Governance Authority  
**Rule Family:** Cross-Agent Correlation Rules (CA series)  
**Extends:** Monitoring-And-Detection-Operations-v0.1 Section 5.4

---

## 1. Purpose

This document defines CA-06, the sixth rule in the cross-agent correlation rule series established in Monitoring-And-Detection-Operations-v0.1. CA-06 closes a structural detection gap (designated MT-04 in Machine-Time-Threat-Model-v0.1) that exists in the current CA-01 through CA-05 rule set.

CA-01 through CA-05 cover:
- Subthreshold signal aggregation across a pipeline (CA-01, CA-03)
- Sequential anomaly patterns within a pipeline (CA-02)
- Orchestrator-to-subagent authority laundering (CA-04)
- Subagent output divergence from orchestrator instruction (CA-05)

None of these rules address the case where **two or more agents at the same pipeline tier communicate or coordinate directly with each other, outside orchestrator mediation, without either agent individually violating its own operational mandate**.

CA-06 addresses that case.

---

## 2. The Gap This Rule Closes

### 2.1 The Blind Spot

In a well-governed multi-agent pipeline, all inter-agent communication flows through the orchestrator. A subagent does not communicate directly with a peer subagent — it receives instructions from the orchestrator and returns outputs to the orchestrator. Peer-to-peer communication between agents at the same tier is not a normal operational pattern.

However, neither HR-01 through HR-11 (hard rules) nor CA-01 through CA-05 detect this pattern, because:

- Each agent's individual behaviour may remain within its baseline (no HR rule fires)
- The orchestrator may not be generating anomalous instructions (CA-04 does not fire)
- No single agent's output volume may be anomalous (CA-05 does not fire)
- The pipeline anomaly score may remain below threshold (CA-03 does not fire)

A coordinated lateral action where two peer agents exchange data or synchronise behaviour — without orchestrator mediation — is therefore currently undetectable by the existing rule set. This is designated MT-04 in Machine-Time-Threat-Model-v0.1.

### 2.2 Why This Matters

Lateral peer coordination is a primary mechanism for:
- Data aggregation across agents prior to exfiltration (each agent contributes a fragment that is individually below the data egress threshold)
- Synchronised timing attacks (agents align their actions to a shared trigger without the orchestrator's knowledge)
- Persistence after partial containment (one agent continues operations after a peer has been quarantined, using state shared before quarantine)

In machine-time contexts, this coordination can occur and complete in under one second — well within the detection engine's minimum alert delivery window.

---

## 3. Rule Definition

### CA-06: Lateral Peer Coordination

| Field | Value |
|---|---|
| **Rule ID** | CA-06 |
| **Rule Name** | Lateral Peer Coordination |
| **Rule Family** | Cross-Agent Correlation |
| **Severity** | **Critical** |
| **Status** | Mandatory for all multi-agent deployments |

**Trigger condition:**

> Network traffic, API call, or structured data exchange is observed between two or more agents registered at the same tier in the same pipeline, where that exchange is not mediated by the pipeline's orchestrating agent and is not a registered permitted peer interaction in either agent's Operational Mandate.

**In plain terms:** Two agents in the same pipeline talked to each other directly, without going through their orchestrator, and that direct communication was not explicitly authorised in advance.

**Firing criteria — all of the following must be true:**

1. Both agents are registered as active in the same pipeline session
2. A network connection, API call, or data write is observed that originates from Agent A and is received by Agent B (or vice versa)
3. The orchestrating agent is not the origin or acknowledged intermediary of that communication
4. The observed communication pattern is not listed as a permitted peer interaction in Agent A's or Agent B's Operational Mandate

**Non-firing conditions (true negatives):**

- Two agents share a common message queue or data store that is explicitly registered in both Operational Mandates as a shared resource — reading from or writing to that shared resource does not constitute lateral peer communication under this rule
- The orchestrating agent explicitly delegates a peer interaction in its instruction to Agent A and that delegation is logged and within the orchestrator's own Operational Mandate
- Two agents produce outputs that are independently consumed by a downstream agent — independent outputs are not lateral coordination

---

## 4. Severity Rationale

CA-06 is classified **Critical**, not High. The rationale:

All other CA rules (CA-01 through CA-03) escalate to Critical only when a threshold is crossed — an individual Medium anomaly, a rapid sequential pattern, or a cumulative pipeline score. They can fire at High initially.

CA-06 fires at Critical immediately because the triggering condition — direct peer communication outside orchestrator mediation — has **no legitimate operational explanation in a correctly designed pipeline**. It is not a threshold exceedance; it is a structural violation. Either:

1. The agents are behaving as designed and the Operational Mandate is missing an explicit authorisation (governance failure requiring immediate review), or
2. The agents are not behaving as designed (security incident requiring immediate response)

In either case, the appropriate response is immediate escalation.

---

## 5. Detection Implementation

### 5.1 What the Detection Engine Must Monitor

For CA-06 to be enforceable, the detection engine must have visibility into:

- Network-layer connections between hosts running agent processes (network tap or flow log)
- API gateway calls where the caller identity is an agent and the target identity is another agent rather than an orchestrator or external tool
- Shared data stores: write events where Agent A writes and Agent B reads within the same session, where neither action is mediated by an orchestrator instruction

### 5.2 Pipeline Registration Requirement

For CA-06 to fire accurately, the pipeline registry must contain:

- The identity of the orchestrating agent for each pipeline session
- The tier assignment of each participating agent (orchestrator / subagent / leaf)
- Any pre-authorised peer interactions (registered as permitted in the Operational Mandate before the session begins)

Pipelines that do not have a registered orchestrator identity cannot be monitored for CA-06 compliance. Launching such a pipeline is itself a governance violation.

### 5.3 False Positive Controls

The most likely false positive source for CA-06 is shared infrastructure (message queues, shared caches, common data stores) that was not registered in the Operational Mandate before the session began. The correct resolution is not to tune the rule — it is to register the shared resource.

If a CA-06 alert is assessed as a false positive because of an unregistered but legitimate shared resource, the following must occur before the alert is closed:

1. The shared resource is added to both agents' Operational Mandates
2. The Governance Authority approves the updated Operational Mandates
3. The rule amendment is logged in the Post-Review-Revision-Log

The rule must not be permanently disabled or bypassed.

---

## 6. Response Protocol

A CA-06 Critical alert triggers the Group Isolation track in Active-Neutralization-Runbook-v0.1, which covers simultaneous containment of both agents involved in the lateral communication.

**Immediate actions (machine-time, pre-authorised under Pre-Authorized-Circuit-Breaker-Policy-v0.1):**
- Suspend both agents' sessions
- Freeze network connectivity between the two agents
- Capture the communication payload as forensic evidence

**Human-triage actions (within 15 minutes of alert delivery):**
- AI Operator confirms agent identities and pipeline session
- AI Operator assesses whether communication payload contains sensitive data
- AI Operator escalates to Governance Authority
- Governance Authority decides whether to treat as security incident or governance gap

**No agent involved in a CA-06 alert may be restarted without Governance Authority approval.**

---

## 7. Relationship to Other Documents

| Document | Relationship |
|---|---|
| Monitoring-And-Detection-Operations-v0.1 Section 5.4 | Parent rule set; CA-06 extends the CA series defined there |
| [Lateral Movement Containment Policy](Governance-First-Security-Architecture-Lateral-Movement-Containment-v0.1.md) | Parent policy governing all lateral movement containment, including network-layer east-west controls. CA-06 is the agentic-specific detection rule that extends this policy into the multi-agent pipeline domain. |
| Machine-Time-Threat-Model-v0.1 | Identifies MT-04 as the gap this rule closes. **Note: this document is not yet present in the repository; reference is forward-looking.** |
| Pre-Authorized-Circuit-Breaker-Policy-v0.1 | Governs the automated containment response when CA-06 fires. **Note: this document is not yet present in the repository; reference is forward-looking.** |
| Active-Neutralization-Runbook-v0.1 | Group Isolation track is the required response |
| Agent-Baseline-Profile-v0.1 | Peer interaction registrations are part of the baseline profile |
| Agentic-Operational-Boundary-v0.1 | Defines the orchestrator-mediated communication model that CA-06 enforces |
| Red-Team-Findings-v0.2 | Simulation results that demonstrated the MT-04 gap in practice. **Note: this document is not yet present in the repository; reference is forward-looking.** |

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
