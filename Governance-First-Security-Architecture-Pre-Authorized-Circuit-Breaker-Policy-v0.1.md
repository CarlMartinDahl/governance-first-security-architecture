# Pre-Authorized Circuit Breaker Policy

**Document ID:** GFSA-PRE-AUTHORIZED-CIRCUIT-BREAKER-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-26  
**Classification:** Internal — Restricted  
**Owner:** Governance Authority  

---

## 1. Purpose

This document defines the Pre-Authorized Circuit Breaker: an automated pipeline suspension mechanism that operates without requiring human decision-making at the moment of firing.

The circuit breaker is a **complement to Stop-State-Policy-v0.1**, not a replacement. Stop-State-Policy governs the defined stop state and the conditions under which the governed system must reach it. This policy governs the mechanism by which that stop state can be reached automatically — in machine time — when the 1:1200:72000 time asymmetry established in Machine-Time-Threat-Model-v0.1 makes human pre-firing authorisation structurally infeasible.

The human remains accountable. This policy relocates that accountability from the response instant to the policy-setting and post-hoc review phases.

---

## 2. The Problem This Policy Solves

### 2.1 The Contradiction in Stop-State-Policy

Stop-State-Policy-v0.1 defines conditions under which agent sessions must be suspended. The response protocol in that document requires AI Operator triage before suspension. That requirement is appropriate for threats that operate at human time.

For machine-time threats (as defined in Machine-Time-Threat-Model-v0.1 Section 3), the window between alert generation and damage completion may be measured in milliseconds to seconds. The minimum human triage time, under realistic conditions, is measured in minutes to hours.

The gap means that requiring human authorisation before suspension is, in practice, equivalent to no suspension at all against machine-time attacks. This is not a criticism of the operators — it is a structural property of the time scales involved.

### 2.2 What Pre-Authorisation Solves

Pre-authorisation resolves the contradiction by separating two governance decisions that the current policy conflates:

| Decision | When It Is Made | Who Makes It |
|---|---|---|
| *Under what conditions should a pipeline be automatically suspended?* | Before any session begins | Governance Authority |
| *Should this specific alert trigger suspension right now?* | At the moment the alert fires | Automation, acting under pre-authorised rules |
| *Was the automated suspension correct? What happens next?* | After suspension | AI Operator + Governance Authority |

The Governance Authority approves the threshold and the rule. The automation executes against that rule. The human reviews the execution. No decision is made without human involvement — the timing of the human involvement is what changes.

---

## 3. Scope

This policy applies to all AI agent pipelines operating within the governed boundary. It covers:

- Single-agent sessions monitored under Stop-State-Policy-v0.1
- Multi-agent pipeline sessions monitored under Monitoring-And-Detection-Operations-v0.1 CA rules
- Any pipeline session where a pre-authorised circuit breaker threshold has been registered

This policy does **not** apply to:
- Human operators (circuit breakers do not suspend human activity)
- Read-only monitoring agents with no write or action capabilities
- Agents operating in a designated test or simulation environment with no production access

---

## 4. Circuit Breaker Tiers

The circuit breaker operates at two tiers, each with different scope and authorisation requirements.

### Tier 1 — Session Suspension (Single Agent)

| Parameter | Value |
|---|---|
| Scope | Suspends one agent's session |
| Trigger | Any Critical alert (HR or CA series) attributed to that agent |
| Pre-authorisation | Granted automatically for all registered agents by this policy; no per-agent approval required |
| Human notification | AI Operator notified within 2 minutes of suspension |
| Restart authorisation | AI Operator (for non-CA-04, non-CA-05, non-CA-06 incidents) |

Tier 1 is the default. Every registered agent operates under Tier 1 circuit breaker rules from the moment it is registered.

### Tier 2 — Pipeline Suspension (All Agents in Pipeline)

| Parameter | Value |
|---|---|
| Scope | Suspends all agents in the affected pipeline simultaneously |
| Trigger | CA-03 (pipeline aggregate Critical), CA-04, CA-05, CA-06, or Tier 1 trigger for the orchestrating agent |
| Pre-authorisation | Granted per pipeline by Governance Authority at pipeline registration |
| Human notification | AI Operator and Governance Authority notified within 2 minutes of suspension |
| Restart authorisation | Governance Authority only |

Tier 2 requires explicit per-pipeline pre-authorisation. A pipeline may not operate under Tier 2 circuit breaker rules without a signed authorisation record from the Governance Authority.

---

## 5. Pre-Authorisation Record Requirements

For a pipeline to operate under Tier 2 circuit breaker rules, the following must be on record before the first session begins:

1. **Pipeline identity**: unique pipeline ID and list of participating agents
2. **Authorising role**: name and role of the Governance Authority representative who approved this pipeline's circuit breaker parameters
3. **Threshold confirmation**: confirmation that the pipeline-level anomaly threshold (CA-03) has been reviewed and accepted
4. **Restart protocol**: who is authorised to restart the pipeline after a Tier 2 suspension, and what forensic review is required before restart is permitted
5. **Review schedule**: date by which the circuit breaker parameters will be reviewed (maximum 6 months from authorisation)

Pre-authorisation records are stored in the governance log alongside the pipeline's Operational Mandate. They are subject to the same tamper-evidence requirements as audit logs (per Log-Integrity-And-Tamper-Evidence-v0.1).

---

## 6. What Happens When the Circuit Breaker Fires

### 6.1 Automated Actions (Machine Time — No Human Required)

When a pre-authorised trigger condition is met:

1. Affected agent session(s) receive a suspend signal — no new inference calls are permitted
2. Active network connections from the agent are terminated
3. All in-flight data writes are halted
4. An evidence snapshot is captured: last 500 log lines per agent, last known system prompt hash, last action taken
5. A Circuit Breaker Event record is written to the audit log: timestamp, trigger rule, affected agent IDs, evidence snapshot reference
6. Notification is dispatched to the AI Operator and, for Tier 2, the Governance Authority

All automated actions complete within the alert delivery window (target: under 30 seconds from trigger detection to suspension confirmation).

### 6.2 Human Actions (Post-Firing Triage)

| Action | Owner | Timing |
|---|---|---|
| Acknowledge Circuit Breaker Event | AI Operator | Within 15 minutes of notification |
| Review evidence snapshot | AI Operator | Within 1 hour |
| Classify: security incident or false positive | AI Operator | Within 1 hour |
| For security incidents: initiate full attribution process | AI Operator per Agent-Attribution-Playbook-v0.1 | Immediately after classification |
| For false positives: document root cause and threshold adjustment recommendation | AI Operator | Within 4 hours |
| Restart authorisation decision | AI Operator (Tier 1) or Governance Authority (Tier 2) | After evidence review |
| Post-incident threshold review | Governance Authority | Within 30 days |

### 6.3 No Auto-Restart

No agent or pipeline suspended by the circuit breaker may restart automatically. Restart requires explicit human authorisation, documented in the governance log. This constraint is not subject to override by any automated system.

---

## 7. False Positive Management

Pre-authorised automation will generate false positives. This is expected and acceptable. The circuit breaker is calibrated to minimise false negatives (missed real attacks) at the cost of occasional false positives (unnecessary suspensions).

**Acceptable false positive rate:** Reviewed quarterly. Action required if Tier 1 false positives exceed 15% of all Tier 1 firings in a quarter, or Tier 2 false positives exceed 5% of all Tier 2 firings.

**False positive response:**
- False positives do not justify disabling the circuit breaker
- False positives indicate a threshold calibration need, addressed through the quarterly review
- Each false positive is documented with root cause; patterns of false positives from the same rule trigger a rule review, not a rule suspension

---

## 8. Relationship to Stop-State-Policy-v0.1

Stop-State-Policy-v0.1 defines the target state. This policy defines one mechanism for reaching it. They are complementary instruments:

| Instrument | Governs | Human Moment |
|---|---|---|
| Stop-State-Policy-v0.1 | What the stop state is and when it is required | Triage and restart authorisation |
| Pre-Authorized-Circuit-Breaker-Policy-v0.1 | How the stop state is reached automatically in machine time | Pre-authorisation of thresholds; post-firing review |

In any incident where the circuit breaker fires, the stop state defined in Stop-State-Policy-v0.1 is the target outcome. The circuit breaker is the path to that outcome when human pre-firing intervention is not feasible.

**Stop-State-Policy-v0.1 is not superseded by this policy.** Where Stop-State-Policy requires human authorisation for suspension and the threat is not machine-time, that human authorisation requirement stands.

---

## 9. Governance of This Policy

This policy may not be modified without Governance Authority approval. Proposed changes must be reviewed by the Security Reviewer before Governance Authority decision.

The circuit breaker mechanism itself must be audited semi-annually to confirm:
- Automated suspension actions complete within the target window
- Evidence snapshot capture is reliable and tamper-evident
- Notification delivery is functioning
- Pre-authorisation records are current and have not lapsed

---

## 10. Related Documents

- Stop-State-Policy-v0.1
- Machine-Time-Threat-Model-v0.1
- Monitoring-And-Detection-Operations-v0.1
- CA-06-Lateral-Peer-Coordination-Rule-v0.1
- Active-Neutralization-Runbook-v0.1
- Agent-Attribution-Playbook-v0.1
- Log-Integrity-And-Tamper-Evidence-v0.1
- Agent-Baseline-Profile-v0.1
- Agentic-Operational-Boundary-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
