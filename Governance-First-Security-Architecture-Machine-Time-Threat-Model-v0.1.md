# Machine-Time Threat Model

**Document ID:** GFSA-MACHINE-TIME-THREAT-MODEL-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-26  
**Classification:** Internal — Restricted  
**Owner:** Governance Authority  

---

## 1. Purpose

This document formalises *machine time* as a distinct threat category in the Governance-First Security Architecture. Existing security models — including the detection and response framework defined in Monitoring-And-Detection-Operations-v0.1 — were designed for environments where human operators can intervene between attack initiation and impact. That assumption fails in AI agent pipelines.

This document establishes the design constraint that governs all time-sensitive detection and response decisions in this architecture.

---

## 2. The Core Problem: Asymmetric Time

The fundamental challenge of securing AI agent pipelines is not complexity — it is time asymmetry between attacker action, detection, and human response.

### 2.1 The 1:1200:72000 Ratio

The operational design constraint of this architecture is expressed as a ratio:

```
Attack execution time   :   Alert delivery time   :   Human triage time
        1 ms            :       1 200 ms           :     72 000 000 ms
```

Expressed in plain terms:

- An AI agent operating at inference speed can execute a multi-step action sequence in **under 1 millisecond per step**
- The monitoring stack (log collection → detection engine → alert queue → delivery) introduces a minimum latency of **approximately 1.2 seconds** under ideal conditions (per Monitoring-And-Detection-Operations-v0.1 Section 8, log collection latency ≤ 60 seconds; alert delivery ≤ 2 minutes)
- A human operator, once alerted, requires a minimum of **approximately 20 hours** (72 000 seconds) to triage, decide, and execute a response under realistic operational conditions — accounting for context-loading, decision-making, and coordination

This ratio is not a criticism of the monitoring stack. It is a structural property of any system where AI agents operate at inference speed and humans provide governance oversight. The ratio will not improve materially through faster monitoring alone.

### 2.2 What This Means for the Threat Model

Any threat actor — whether an external attacker, a compromised agent, or a prompt-injected instruction — that can trigger agent behaviour operates at machine time. Any defensive response that depends on human decision-making before containment operates at human time.

The gap between these time scales means that **the human operator cannot prevent damage from a machine-time attack — they can only contain, attribute, and recover from it**.

This is not a failure of governance. It is the governing constraint that determines what governance instruments are appropriate at which point in the incident lifecycle.

---

## 3. Machine-Time Threat Categories

The following threat categories are defined as machine-time threats: threats whose primary damage vector executes within the detection-to-human-response window and therefore cannot be prevented by human intervention once initiated.

| Threat ID | Threat Name | Execution Window | Primary Damage Vector | Detection Feasibility |
|---|---|---|---|---|
| MT-01 | Simultaneous multi-agent compromise | < 100 ms | Coordinated data exfiltration before any single agent exceeds alert threshold | Log-based: possible; Real-time: required for containment |
| MT-02 | Pipeline instruction injection cascade | < 500 ms | Injected instruction propagates from one agent to next faster than detection cycle | Detectable at orchestrator layer; CA-04/CA-05 rules apply |
| MT-03 | Token replay and lateral escalation | < 200 ms | Revoked token used to authenticate across multiple agents before revocation propagates | HR-04 detects; propagation lag is the risk window |
| MT-04 | Peer-to-peer lateral coordination | < 1 000 ms | Two or more agents coordinate outside orchestrator mediation; no single agent violates its own baseline | Not covered by CA-01 through CA-05; requires CA-06 |
| MT-05 | Log suppression under active exfiltration | Concurrent | Agent suppresses its own log stream while executing malicious actions; HR-05 fires after silence window | 2-minute silence threshold creates a 2-minute unlogged window |
| MT-06 | Sub-threshold volume accumulation | Continuous | Each agent individually stays below alert thresholds; pipeline aggregate exceeds safe total | CA-03 addresses pipeline aggregate; requires threshold calibration |

**MT-04 is the critical gap.** It is the only machine-time threat category not addressed by any existing detection rule in the current architecture. CA-06 (defined in the companion document GFSA-CA-06-LATERAL-PEER-COORDINATION-RULE-v0.1) is required to close this gap.

---

## 4. Implications for Governance Design

### 4.1 Human Loop Placement

Given the 1:1200:72000 ratio, human oversight must be positioned where it is effective:

| Phase | Human Role | Timing |
|---|---|---|
| Pre-incident authorisation | Approve operational mandates, thresholds, and circuit-breaker parameters | Before any agent session begins |
| Automated containment | None — machine-time response is pre-authorised | Milliseconds to seconds |
| Forensic triage | Review evidence, confirm attribution, assess damage | Minutes to hours after containment |
| Recovery authorisation | Approve restart of suspended agents or pipelines | After forensic review |
| Post-incident governance | Review thresholds; update detection rules; update threat model | Days after incident |

Human authorisation that is placed inside the automated containment phase — that is, human approval required before a circuit-breaker fires — is structurally incompatible with machine-time threats. This is the design contradiction addressed by Pre-Authorized-Circuit-Breaker-Policy-v0.1.

### 4.2 What Pre-Authorisation Covers

Pre-authorisation does not mean unaccountable automation. It means that the governance decision is made prospectively rather than reactively. The human operator approves the *rule* and the *threshold* — not each individual firing. Every automated action taken under a pre-authorised rule is logged, attributed, and subject to mandatory post-hoc review.

### 4.3 Detection vs. Prevention

For machine-time threats, the architecture must accept the following design constraint:

> **Prevention of damage from machine-time threats requires pre-authorised automated containment. Human oversight governs the rules under which automation operates, not the individual automated decisions.**

This constraint does not reduce human accountability. It relocates accountability from the response instant to the policy-setting and review phases — where human judgment can operate effectively.

---

## 5. Relationship to Existing Documents

| Document | Relationship |
|---|---|
| Monitoring-And-Detection-Operations-v0.1 | Provides the detection rules; this document explains why those rules alone are insufficient for machine-time containment |
| Stop-State-Policy-v0.1 | Defines the stop state; this document explains the time-scale constraint that requires the Pre-Authorized-Circuit-Breaker as a complement |
| Pre-Authorized-Circuit-Breaker-Policy-v0.1 | The operational instrument that implements the pre-authorisation model defined in Section 4 of this document |
| CA-06-Lateral-Peer-Coordination-Rule-v0.1 | Closes the MT-04 gap identified in Section 3 of this document |
| Red-Team-Findings-v0.1 and v0.2 | The simulation results that empirically validated the 1:1200:72000 ratio and identified MT-04 as a blind spot |
| Active-Neutralization-Runbook-v0.1 | The response playbook; this document defines the time constraints within which that playbook must operate |

---

## 6. Threat Model Maintenance

This threat model must be reviewed:

- After every SEV-1 or SEV-2 incident
- When a new agent type or pipeline architecture is added to the governed boundary
- Annually, regardless of incident history
- When the 1:1200:72000 ratio changes materially due to infrastructure changes

The Governance Authority is responsible for ensuring this document is current. Outdated threat models are themselves a governance failure.

---

## 7. Related Documents

- Monitoring-And-Detection-Operations-v0.1
- Stop-State-Policy-v0.1
- Pre-Authorized-Circuit-Breaker-Policy-v0.1
- CA-06-Lateral-Peer-Coordination-Rule-v0.1
- Active-Neutralization-Runbook-v0.1
- Red-Team-Findings-v0.1
- Red-Team-Findings-v0.2
- Agent-Baseline-Profile-v0.1
- Agentic-Operational-Boundary-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
