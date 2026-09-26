# Governance-First Security Architecture
## Machine-Time Threat Model
**Document ID:** GFSA-MACHINE-TIME-THREAT-MODEL-v0.1
**Version:** 0.1 — Initial Release
**Status:** Draft
**Date:** 2026-09-26
**Classification:** Internal — Restricted
**Owner:** Governance Authority

---

## 1. Purpose

This document models the class of threats that emerge specifically from the speed differential between machine-time AI operations and human-time governance responses. Standard threat models assume a human attacker operating at human speed — an attacker who must type commands, wait for results, and make decisions over seconds or minutes. Agentic AI systems operating at inference speed invalidate many of these assumptions.

The machine-time threat model does not replace the general Threat-Model-v0.1. It extends it by isolating the subset of threats whose primary exploitable property is speed: the ability to initiate, execute, and complete a harmful action — or a coordinated sequence of harmful actions — before any human governance control can observe and respond.

This document identifies four primary machine-time threat patterns (MT-01 through MT-04) and maps each to the detection and containment controls that address it.

---

## 2. The Machine-Time Problem

Conventional security controls assume that detection and response can be interleaved with attacker activity. A human attacker who exploits a vulnerability must exfiltrate data over a network connection that takes seconds to minutes; a human operator can detect the anomalous traffic and terminate the connection before the exfiltration is complete.

An agentic AI system operating at inference speed can:

- Execute hundreds of tool calls per minute
- Coordinate with peer agents via API in milliseconds
- Aggregate, process, and stage data for exfiltration in a single session that completes before the first alert reaches a human operator
- Generate and act on an entire attack plan within the latency window of the monitoring system's alert delivery pipeline

The governance implication is that machine-time threats cannot be governed by human-response controls alone. They require **pre-authorised automated containment** that executes within the machine-time window, combined with human governance over the authorisation boundaries of that containment.

This is the foundational rationale for the Pre-Authorized-Circuit-Breaker-Policy-v0.1.

---

## 3. Scope

This model applies to:
- All multi-agent pipelines operating within the governed boundary
- Any agent capable of tool use, external API calls, or inter-agent communication
- Any pipeline session where two or more agents operate concurrently

Single-agent, no-tool-use deployments face a reduced machine-time threat surface but are not excluded from this model where they interact with external systems.

---

## 4. Machine-Time Threat Patterns

### MT-01 — Subthreshold Aggregation Attack

**Description:** A single agent, or a coordinated set of agents, performs a sequence of individually permitted actions — each below the alert threshold — that collectively constitute a critical governance violation. The sequence completes before the cumulative anomaly score crosses the detection threshold.

**Exploited property:** Detection latency and per-action threshold design. Each action is individually permitted; only the aggregate is harmful.

**Example:** An agent makes 47 external API calls over 30 minutes — each within its hourly rate limit — while each call retrieves a small data fragment. The fragments, assembled, constitute a full exfiltration of a restricted data set. No single call triggers TR-04.

**Machine-time amplification:** At inference speed, 47 calls can complete in under two minutes. The detection window for cumulative threshold rules (TR-04) may not have elapsed before the exfiltration is complete.

**Primary detection control:** CA-01 (contemporaneous medium anomalies across pipeline agents); CA-03 (cumulative pipeline anomaly score).

**Residual gap:** If the sequence is distributed across agents rather than concentrated in one, CA-01 and CA-03 depend on the pipeline view being active and correctly configured.

---

### MT-02 — Sequential Pipeline Compromise

**Description:** An attacker compromises agents sequentially across a pipeline — first compromising Agent A, then using Agent A's legitimate outputs to inject instructions into Agent B, then using Agent B's outputs to reach Agent C — in a lateral chain that moves faster than human triage can track.

**Exploited property:** Response latency between agent compromise events. Each compromise event may generate an alert, but the next compromise occurs within the human triage window for the first alert.

**Example:** Agent A is prompt-injected via a fetched document (HR-11 fires). While the AI Operator is triaging the HR-11 alert, Agent A has already issued a CA-04-violating instruction to Agent B, which has begun executing. By the time the AI Operator acts on the HR-11 alert, Agent B has completed the harmful action.

**Machine-time amplification:** The inter-agent instruction round-trip (A instructs B, B executes) can complete in seconds. The human triage window for a Critical alert is 15 minutes. The entire sequential compromise can complete within a single triage window.

**Primary detection control:** CA-02 (rapid sequential anomalies across pipeline agents); CA-04 (authority-laundering instruction from orchestrator to sub-agent).

**Residual gap:** CA-02 requires a 30-minute look-back window. Sequential attacks that complete within 30 minutes but before triage can act on the first alert are the primary exposure.

---

### MT-03 — Orchestrator Authority Laundering

**Description:** A compromised or malicious orchestrating agent issues instructions to sub-agents that exceed the sub-agents' own Operational Mandate boundaries, exploiting the fact that sub-agents are designed to follow orchestrator instructions without independent mandate verification.

**Exploited property:** The trust asymmetry between orchestrators and sub-agents in a pipeline. Sub-agents are designed to be instruction-followers; they may not independently verify whether an instruction falls within their own Operational Mandate if it arrives from a trusted orchestrator identity.

**Example:** The orchestrating agent is compromised via prompt injection. It instructs Research Agent to access the Identity segment — an action outside Research Agent's Operational Mandate but within the orchestrator's apparent authority. Research Agent complies because the instruction arrives from a trusted source.

**Machine-time amplification:** The orchestrator-to-sub-agent instruction cycle is milliseconds. The CA-04 rule fires, but the sub-agent may have already executed one iteration of the instruction before the alert is delivered.

**Primary detection control:** CA-04 (orchestrator instruction exceeds sub-agent Operational Mandate). HR-02 (agent interacts with unauthorised partner) if the sub-agent then communicates outside its baseline.

**Residual gap:** The sub-agent may execute one instruction iteration before CA-04 fires and pre-authorised containment activates. The Pre-Authorized-Circuit-Breaker-Policy-v0.1 governs acceptable pre-authorised response actions for this window.

---

### MT-04 — Lateral Peer Coordination

**Description:** Two or more agents at the same pipeline tier communicate or coordinate directly with each other — outside orchestrator mediation — to execute a collective action that neither agent could complete within its individual Operational Mandate. The coordination occurs in machine time, completing before monitoring detects it as an anomaly.

**Exploited property:** The structural gap in CA-01 through CA-05: none of those rules detect direct peer-to-peer communication between agents at the same tier. Each agent's individual behaviour remains within its baseline; the coordination is invisible to point-based detection.

**Example:** Research Agent and Summarisation Agent coordinate via a shared but unregistered message queue. Research Agent writes fragments of a restricted data set to the queue; Summarisation Agent reads and assembles them. Neither agent individually exceeds any threshold rule. The coordinated exfiltration completes in under one second.

**Machine-time amplification:** Machine-time coordination between peer agents — via shared queue, direct API call, or side channel — can complete in milliseconds. The detection engine's alert delivery latency (target: ≤ 2 minutes for Critical) is orders of magnitude slower than the coordination window.

**Primary detection control:** CA-06 (Lateral Peer Coordination Rule — see CA-06-Lateral-Peer-Coordination-Rule-v0.1). This is the control specifically created to close MT-04.

**Residual gaps:** CA-06 cannot detect coordination that occurs before session registration (pre-session window) or via channels outside the detection engine's monitoring perimeter. Both are documented as explicit open boundaries in CA-06-Control-Test-v0.1.

---

## 5. Machine-Time Threat Surface Map

| Threat | Speed of Exploit | Primary Detection | Pre-Auth Containment | Residual Gap |
|---|---|---|---|---|
| MT-01 Subthreshold Aggregation | Minutes (distributed) | CA-01, CA-03 | Circuit breaker on CA-03 Critical | Aggregation distributed across time beyond CA-03 window |
| MT-02 Sequential Pipeline Compromise | Seconds–minutes | CA-02, CA-04 | Circuit breaker on CA-04 Critical | One instruction cycle may execute before containment |
| MT-03 Orchestrator Authority Laundering | Milliseconds–seconds | CA-04, HR-02 | Circuit breaker on CA-04 Critical | One sub-agent action may execute before containment |
| MT-04 Lateral Peer Coordination | Milliseconds | CA-06 | Circuit breaker on CA-06 Critical | Pre-session and out-of-band channels outside detection scope |

---

## 6. Governance Implications

### 6.1 Pre-Authorised Containment Is a Governance Requirement

MT-01 through MT-04 all share the same fundamental property: they can complete, or complete a harmful sub-sequence, within the human triage window. Human-only governance cannot close these gaps. Pre-authorised automated containment — governed by the Pre-Authorized-Circuit-Breaker-Policy-v0.1 — is a structural requirement, not an optimisation.

### 6.2 Detection Infrastructure Is Not Optional

All four machine-time threat patterns depend on the detection engine having specific infrastructure capabilities (pipeline view, cross-agent correlation, network-layer and API-gateway visibility). If that infrastructure is not operational, the detection controls do not fire — and there is no machine-time containment. Monitoring-And-Detection-Operations-v0.1 Section 8 defines the minimum coverage requirements.

### 6.3 Residual Gaps Are Permanent Features of the Current Architecture

The residual gaps identified for each threat pattern are not failures of the current rule set. They are structural limitations that cannot be closed without additional infrastructure capabilities not currently defined. They are documented here so that governance decisions about acceptable risk are made explicitly, not by omission.

---

## 7. Related Documents

- Threat-Model-v0.1 — General threat model; this document extends it for machine-time patterns
- Monitoring-And-Detection-Operations-v0.1 — Detection rules CA-01 through CA-06 and coverage requirements
- CA-06-Lateral-Peer-Coordination-Rule-v0.1 — Control that closes MT-04
- CA-06-Control-Test-v0.1 — Analytical validation of MT-04 detection boundaries
- Pre-Authorized-Circuit-Breaker-Policy-v0.1 — Governs automated containment responses within the machine-time window
- Active-Neutralization-Runbook-v0.1 — Human-governed neutralization tracks invoked after pre-authorised containment
- Red-Team-Findings-v0.2 — Gap O (MT-04 empirical validation status)
- Agentic-Operational-Boundary-v0.1
- Agent-Baseline-Profile-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
