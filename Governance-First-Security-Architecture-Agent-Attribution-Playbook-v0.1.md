# Agent Attribution Playbook

**Document ID:** GFSA-AGENT-ATTRIBUTION-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-25  
**Classification:** Internal — Restricted  
**Owner:** Governance Authority  

---

## 1. Purpose

This playbook defines the methodology for attributing a hostile or compromised action to a specific AI agent — including the forensic chain, log correlation, and decision criteria required to make an attribution claim with sufficient confidence to justify a governance response.

Attribution in an agentic AI environment is distinct from traditional IT forensics because:
- Agents may share identities, credentials, or instruction channels
- A compromised agent may mimic legitimate behaviour before deviating
- The attacker may be the agent's original instruction source (prompt injection, supply chain compromise) or an external actor that hijacked the agent after deployment
- Multiple agents may be involved in a coordinated action, with attribution needing to span the chain

This playbook answers: *Who did what, under whose authority, and with what evidence?*

---

## 2. Scope

This playbook applies to:
- All AI agents operating within the governed boundary
- Any action flagged as anomalous by the monitoring layer
- Any stop-state event that references agent behaviour as a contributing cause
- Post-incident reviews where agent attribution is required for accountability or legal purposes

---

## 3. Attribution Confidence Levels

All attribution claims must be assigned one of three confidence levels before any governance action is taken:

| Level | Definition | Permitted Actions |
|---|---|---|
| **CONFIRMED** | Direct log evidence links action to agent identity with no plausible alternative explanation | Full governance response; neutralisation authorised |
| **PROBABLE** | Circumstantial log evidence strongly suggests agent; no direct link but no contradicting evidence | Containment authorised; neutralisation requires Governance Authority sign-off |
| **SUSPECTED** | Behavioural indicators point toward agent; evidence is incomplete or ambiguous | Monitoring uplift only; no containment without escalation |

Attribution must never be escalated to a higher confidence level without the evidence criteria for that level being explicitly met.

---

## 4. Evidence Sources and Collection

### 4.1 Primary Evidence Sources

| Source | What It Provides | Integrity Requirement |
|---|---|---|
| Audit log (append-only) | Timestamped record of every agent action, tool call, and decision point | Must be tamper-evident per Log-Integrity-And-Tamper-Evidence-v0.1 |
| API gateway access log | Authenticated identity behind each request; token lineage | Must be preserved in original form; no post-hoc modification |
| Agent identity token | Signed credential that identifies the agent instance | Must be validated against the identity registry at time of action |
| Tool call trace | Sequence of external calls made by the agent | Must include inputs, outputs, and timestamps |
| Instruction provenance record | The instruction chain that authorised the agent's task | Must be version-controlled and signed |
| Network traffic log | Source/destination of all network calls made during the incident window | Must be preserved before any remediation changes routing |

### 4.2 Evidence Collection Procedure

1. **Freeze the evidence window:** Immediately upon a flag or stop-state trigger, snapshot and cryptographically hash all log files for the incident window. Do not proceed with any remediation that could overwrite these logs.
2. **Preserve agent state:** If the agent process is still running, capture a memory dump and process snapshot before any shutdown.
3. **Extract the identity token:** Retrieve the agent's identity token from the API gateway log for every action in the incident window.
4. **Pull the instruction provenance record:** Identify the task instruction that authorised the agent's activity; trace it to its originating human principal or orchestrating agent.
5. **Correlate timestamps:** Align all log sources to a common time reference (NTP-synchronised); flag any gaps or timestamp anomalies as potential evidence of tampering.
6. **Chain of custody:** All evidence must be transferred to a write-protected evidence store immediately; access to evidence must be logged.

---

## 5. Attribution Analysis Procedure

### Step 1 — Establish the Action

Define precisely what action is under investigation:
- What system or resource was affected?
- What was the observed outcome?
- What timestamp range covers the action?
- Is this a single action or a sequence?

### Step 2 — Identify Candidate Agents

From the API gateway log, identify all agent identities that were active during the incident window. List each as a candidate.

### Step 3 — Match Identity to Action

For each candidate agent:
1. Retrieve the signed identity token used in the API calls during the incident window
2. Verify the token signature against the identity registry
3. Check whether the token's declared permissions include the capability used in the action
4. If the token is valid and the capability matches: this agent is a primary candidate
5. If the token is invalid, forged, or replayed: escalate immediately — this indicates a credential compromise event, not just a behavioural anomaly

### Step 4 — Trace the Instruction Chain

1. Retrieve the instruction that authorised the agent's task at the time of the action
2. Identify who or what issued that instruction (human operator, orchestrating agent, automated trigger)
3. Determine whether the instruction was within the agent's declared operational boundary (see Agentic-Operational-Boundary-v0.1)
4. If the action was within the instruction boundary but the instruction itself was malicious: this is a **prompt injection** or **instruction source compromise** — attribution shifts to the instruction source
5. If the action exceeded the instruction boundary: this is **agent boundary violation** — attribution rests with the agent instance

### Step 5 — Check for Coordination

If the incident involves multiple anomalous actions:
1. Map all involved agent identities and their action timelines
2. Check for shared instruction sources, shared credentials, or sequential actions that suggest coordination
3. If coordination is detected, attribute to the full agent group and trace to the common instruction source or compromised orchestrator

### Step 6 — Assign Confidence Level

Apply the confidence criteria from Section 3. Document the evidence that supports the assigned level and any evidence gaps.

### Step 7 — Document and Escalate

1. Complete the Attribution Record (see Section 7) 
2. Submit to Governance Authority with recommended confidence level
3. Governance Authority approves or downgrades confidence level
4. Approved attribution triggers the appropriate response track per Active-Neutralization-Runbook-v0.1

---

## 6. Special Cases

### 6.1 Prompt Injection Attribution

If the evidence shows the agent acted on injected instructions (from a malicious document, API response, or user input that was not the authorised operator):
- The agent is NOT the primary attributable party; the injection source is
- Document the injection vector and the agent's failure to detect or reject it
- Attribution record must note both the injection source (if identifiable) and the agent's detection failure
- Review system prompt governance layer for gaps

### 6.2 Supply Chain Compromise Attribution

If the agent was running a compromised model or dependency (see AI-Model-And-Supply-Chain-Integrity-v0.1):
- Attribution extends beyond the deployed agent to the supply chain failure point
- All agents running the same compromised component are treated as a single attribution group
- Governance Authority must be notified immediately; this is a stop-state condition

### 6.3 Coordinated Multi-Agent Attribution

If multiple agents are involved:
- Map the full action graph: which agent called which, in what sequence, under what instruction
- The root attributable party is the orchestrating agent or the instruction source that initiated the chain
- Each participating agent is also individually documented as a secondary attributable party

### 6.4 Attribution Failure

If attribution cannot reach even SUSPECTED level due to log gaps, destroyed evidence, or identity spoofing:
- Document the failure and its cause
- Treat all agents active during the incident window as under enhanced monitoring
- Escalate to Governance Authority as an unattributed incident
- Initiate a log integrity review to determine whether evidence was deliberately destroyed

---

## 7. Attribution Record Template

```
ATTRIBUTION RECORD
==================
Incident ID:         [Link to stop-state or incident record]
Date / Time:         [UTC timestamp of attribution completion]
Prepared by:         [Role and identity of analyst]
Approved by:         [Governance Authority sign-off]

ACTION UNDER INVESTIGATION
--------------------------
Description:         [What happened]
Timestamp range:     [Start – End UTC]
Systems affected:    [List]

ATTRIBUTION RESULT
------------------
Primary agent:       [Agent identity / token ID]
Confidence level:    [CONFIRMED / PROBABLE / SUSPECTED]
Evidence basis:      [Summary of evidence; link to evidence store]
Instruction source:  [Who or what authorised the task]
Boundary violation:  [Yes / No — if Yes, which boundary]
Coordination:        [Yes / No — if Yes, list all agents]

SPECIAL CIRCUMSTANCES
---------------------
Prompt injection:    [Yes / No — if Yes, describe vector]
Supply chain:        [Yes / No — if Yes, component and version]
Credential anomaly:  [Yes / No — if Yes, describe]

RECOMMENDED RESPONSE
--------------------
Track:               [Neutralization / Containment / Monitoring uplift]
Reference:           Active-Neutralization-Runbook-v0.1 Section [X]
Urgency:             [Immediate / Within 4 hours / Within 24 hours]

GOVERNANCE AUTHORITY DECISION
------------------------------
Approved confidence: [Level]
Approved response:   [Track]
Signature:           [Role / Date]
```

---

## 8. Related Documents

- Active-Neutralization-Runbook-v0.1
- Agentic-Identity-Security-Conceptual-Foundation-v0.1
- Agentic-Operational-Boundary-v0.1
- Log-Integrity-And-Tamper-Evidence-v0.1
- Audit-And-Accountability-v0.1
- Stop-State-Policy-v0.1
- Stop-State-Registry-v0.1
- AI-Model-And-Supply-Chain-Integrity-v0.1
- Deceptive-Containment-Environment-Conceptual-Foundation-v0.1
- Identity-And-Credential-Governance-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
