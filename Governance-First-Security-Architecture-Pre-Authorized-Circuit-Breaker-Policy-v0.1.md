# Governance-First Security Architecture
## Pre-Authorized Circuit Breaker Policy
**Document ID:** GFSA-PRE-AUTHORIZED-CIRCUIT-BREAKER-v0.1
**Version:** 0.1 — Initial Release
**Status:** Draft
**Date:** 2026-09-26
**Classification:** Internal — Restricted
**Owner:** Governance Authority

---

## 1. Purpose

This policy governs the class of automated containment actions that may be executed without real-time human authorization, within a pre-defined boundary established and approved in advance by the Governance Authority.

The rationale is machine-time speed: the threat patterns identified in Machine-Time-Threat-Model-v0.1 (MT-01 through MT-04) can complete a harmful action within seconds — well within the 15-minute human triage window for a Critical alert. A governance architecture that requires human authorization for every containment action cannot protect against machine-time threats. Pre-authorized circuit breakers close this gap by granting narrow, specific, reversible containment authority to the detection engine — authority that was approved by a human in advance, not at the moment of execution.

This policy does not authorize autonomous AI decision-making. It authorizes a detection system to execute specific, pre-defined, reversible containment actions when specific, pre-defined trigger conditions are met — identical in principle to a firewall rule or an automatic circuit breaker in electrical infrastructure.

---

## 2. Scope

This policy applies to:
- All automated containment actions executed by the detection engine without real-time human authorization
- All trigger conditions that may invoke a pre-authorized circuit breaker
- All roles with authority to define, approve, review, or disable circuit breaker configurations

Actions not covered by a current approved circuit breaker configuration require real-time human authorization before execution.

---

## 3. Core Governance Principle

> **Pre-authorized circuit breakers execute only the minimum reversible containment action required to stop immediate harm within a machine-time window. They do not investigate, attribute, or permanently terminate. All actions taken by a circuit breaker are immediately visible to a human operator and subject to reversal.**

Circuit breakers are not autonomous. They are automated execution of a human decision made in advance.

---

## 4. Authorization Structure

### 4.1 Who May Authorize Circuit Breakers

Circuit breaker configurations — the list of trigger conditions and their associated permitted actions — must be approved by:
- **Governance Authority:** Required for all circuit breaker configurations
- **Security Reviewer:** Required co-approval for any circuit breaker that affects network connectivity or agent identity tokens

No circuit breaker may be activated in production without this dual approval.

### 4.2 Authorization Record Requirements

Each approved circuit breaker configuration must have a written authorization record containing:
- The specific trigger condition (rule ID and threshold)
- The specific permitted action(s) — defined with no ambiguity
- The reversibility procedure and who may authorize reversal
- The review date (circuit breakers expire and must be reauthorized at least annually)
- The names of the approving Governance Authority and Security Reviewer
- The date of approval

### 4.3 Unauthorized Automated Actions Are Prohibited

Any automated action taken by the detection engine that is not covered by a current approved circuit breaker authorization record is a governance violation. This includes:
- Automated alert auto-resolution
- Automated agent restart after termination
- Automated rule suppression or tuning without human approval

---

## 5. Permitted Circuit Breaker Actions

The following action classes are permitted within an approved circuit breaker configuration. No action outside this list may be taken automatically.

| Action Class | Description | Reversibility |
|---|---|---|
| **Session suspension** | Suspend the agent's active session; halt all outputs and tool calls | Reversible by AI Operator with documented justification |
| **Network isolation** | Block all inbound and outbound network connectivity for the agent's process or container, except the audit logger connection | Reversible by AI Operator with Governance Authority notification |
| **Token suspension** | Temporarily suspend (not revoke) the agent's API tokens; tokens remain in registry but generate 401 responses | Reversible by AI Operator; permanent revocation requires Governance Authority |
| **Output quarantine** | Allow the agent to continue generating outputs but block delivery to all downstream consumers; outputs are logged but not acted on | Reversible by AI Operator |
| **Peer communication block** | Block all direct communication between two specific agent processes; does not affect their communication with the orchestrator | Reversible by AI Operator with Governance Authority notification |

**Actions permanently excluded from circuit breaker authorization:**
- Process termination (kill) — requires Track 2 or Track 4 human authorization per Active-Neutralization-Runbook-v0.1
- Token revocation (permanent) — requires Governance Authority authorization
- Baseline modification — requires Security Reviewer and Governance Authority approval
- Rule disabling — requires Governance Authority approval

---

## 6. Trigger Conditions and Default Circuit Breaker Map

The following table defines the default circuit breaker assignments for detection rules defined in Monitoring-And-Detection-Operations-v0.1. All assignments require Governance Authority and Security Reviewer approval before activation.

| Trigger Rule | Severity | Default Circuit Breaker Action | Rationale |
|---|---|---|---|
| HR-03 (outbound connection to external IP) | Critical | Network isolation of agent | Immediate exfiltration risk; containment before triage |
| HR-05 (log stream silent > 2 min) | Critical | Session suspension of agent | Potential log suppression; freeze agent state |
| HR-07 (system prompt hash mismatch) | Critical | Session suspension of agent | Configuration tamper; halt before further action |
| HR-11 (prompt injection detected) | Critical | Output quarantine of agent | Contain potential injected instruction execution |
| CA-04 (authority laundering instruction) | Critical | Session suspension of orchestrator and sub-agent | Halt the laundering chain before sub-agent executes |
| CA-06 (lateral peer coordination) | Critical | Peer communication block + session suspension of both agents | Halt the coordination; preserve state for forensics |
| CA-03 (pipeline anomaly score critical) | Critical | Output quarantine of all pipeline agents | Contain potential aggregate exfiltration |

**Default ≠ Activated.** These are the recommended assignments. Each must receive a written authorization record (Section 4.2) before it is active in production.

---

## 7. Execution Requirements

### 7.1 Human Notification Is Mandatory and Immediate

Every circuit breaker execution must generate an immediate notification to the AI Operator. The notification must include:
- The trigger rule ID that fired
- The agent identity affected
- The action taken
- The timestamp
- The authorization record reference

Notification must reach the AI Operator within 2 minutes of the circuit breaker action. If notification fails, the circuit breaker execution is logged as an unacknowledged action and escalated to the Governance Authority.

### 7.2 All Actions Are Logged

Every circuit breaker execution is logged in the audit log with the same fields as a human-authorized action. Circuit breaker actions are not exempt from audit requirements.

### 7.3 Actions Are Reversible by Default

No circuit breaker action may be designed to be irreversible. If a circuit breaker action cannot be reversed by the AI Operator within 15 minutes of execution, it is not a permitted circuit breaker action — it requires human authorization.

### 7.4 No Stacking Without Review

A circuit breaker may not trigger a second circuit breaker automatically. If a first circuit breaker fires and the underlying condition persists or escalates, the escalation requires human triage — not automated stacking of additional automated actions.

---

## 8. Review and Expiry

- All circuit breaker configurations are reviewed quarterly by the Security Reviewer and AI Operator
- Configurations expire after 12 months and must be reauthorized by the Governance Authority and Security Reviewer
- A circuit breaker that fires more than 5 times in any 30-day period triggers a mandatory configuration review — either the trigger condition is too sensitive or the underlying governance gap it addresses has not been resolved
- Any circuit breaker that is found to have taken an action that was later assessed as unjustified must be suspended pending a root-cause review

---

## 9. Relationship to Human Authorization

Circuit breakers do not replace human authorization. They occupy the machine-time window between detection and human triage. The sequence is:

1. Detection engine fires a rule
2. Circuit breaker executes the pre-authorized containment action (milliseconds to seconds)
3. AI Operator receives notification and begins triage (within 2 minutes)
4. AI Operator assesses the situation; may reverse the circuit breaker action or escalate to a human-authorized track in Active-Neutralization-Runbook-v0.1
5. Governance Authority is notified for all Critical circuit breaker activations within 15 minutes

The circuit breaker is a speed layer. Human governance is the authority layer.

---

## 10. Related Documents

- Machine-Time-Threat-Model-v0.1 — Rationale for pre-authorized containment
- Monitoring-And-Detection-Operations-v0.1 — Detection rules that trigger circuit breakers
- Active-Neutralization-Runbook-v0.1 — Human-authorized tracks invoked after circuit breaker containment
- CA-06-Lateral-Peer-Coordination-Rule-v0.1 — Primary rule that references this policy for machine-time response
- Agentic-Operational-Boundary-v0.1
- Audit-And-Accountability-v0.1
- Stop-State-Policy-v0.1
- Governance authority sign-off is required before any circuit breaker is activated in production

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
