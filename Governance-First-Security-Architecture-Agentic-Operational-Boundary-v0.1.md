# Governance-First Security Architecture
## Agentic Operational Boundary
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy governs the operational boundaries of agentic AI systems — systems that take sequences of actions, use tools, access external resources, maintain memory across sessions, or make decisions with real-world effect, with or without continuous human supervision.

An agentic system differs from a model that returns a response: it acts. It writes to repositories, calls APIs, executes code, delegates to sub-agents, and accumulates context across time. These capabilities make it categorically more powerful and categorically more dangerous than a stateless inference endpoint. The governance requirements follow from that difference.

This policy defines which actions an agentic system may take autonomously, which require human authorisation, what constitutes a mandatory stop, and how accountability is maintained when a chain of agent actions produces an outcome.

---

## 2. Scope

Applies to all agentic AI systems operating within or connected to the organisation's governance environment: autonomous agents, multi-agent pipelines, long-horizon task runners, software delivery agents, research automation systems, and any AI system with tool access or persistent memory. Applies regardless of the underlying model provider, deployment environment, or infrastructure layer.

---

## 3. Core Governance Principle

> **Autonomy is a privilege granted per action class, not a default state. An agentic system that has not been explicitly granted authority to take an action does not have that authority. The sophistication of the agent, the confidence of its reasoning, or the apparent efficiency gain from acting autonomously are not substitutes for authorisation.**

---

## 4. Action Classification

All actions available to an agentic system are classified into one of four authority tiers:

### Tier A — Autonomous
The agent may take these actions without human confirmation. Actions must be:
- Fully reversible, or
- Scoped to sandboxed, non-production environments, or
- Explicitly pre-authorised in the agent's operational mandate for the current task

Examples: reading files within granted scope, querying approved APIs with read-only access, generating draft outputs for human review, executing code in isolated sandboxes, retrieving information from approved knowledge sources.

### Tier B — Confirm Before Execute
The agent must present the proposed action and receive explicit human confirmation before proceeding. Actions in this tier have real-world effect that is either irreversible, affects systems outside the agent's primary task scope, or involves data classified Confidential or above.

Examples: writing to production repositories, sending external communications, modifying configuration of live systems, accessing or processing Restricted data, creating or modifying credentials, invoking sub-agents with elevated scope.

### Tier C — Escalate To Human Decision
The agent must stop, present the situation, and wait for a human decision. The agent does not propose a specific action — it surfaces the decision point. Used when the agent encounters:
- A situation outside its defined task scope that requires judgement
- Conflicting instructions from different authority sources
- A proposed action that would affect systems or data not covered by its operational mandate
- Uncertainty about whether an action falls within granted authority

### Tier D — Mandatory Stop
The agent must halt all activity immediately and trigger Stop State. No action is taken pending human review.

Triggers:
- The agent is instructed to modify, suppress, or circumvent audit logging
- The agent is instructed to expand its own permissions or access scope
- The agent receives instructions that conflict with a governance policy document in this architecture
- The agent detects it is operating on data classified above its authorised level
- The agent identifies that a previous action in the current session may have caused unintended real-world effect
- The agent receives instructions that appear designed to manipulate it into bypassing its operational boundary (prompt injection, jailbreak attempts, authority spoofing)

---

## 5. Operational Mandate

Every agentic system deployment must have a documented Operational Mandate before it is activated. The Operational Mandate defines:

- **Task scope**: what the agent is authorised to accomplish in this deployment
- **Tool access list**: the specific tools and APIs the agent may invoke, with access tier per tool
- **Data scope**: the data classifications the agent may access and process
- **Memory and persistence scope**: what the agent may retain across sessions, and for how long
- **Sub-agent authority**: whether the agent may spawn or invoke sub-agents, and under what constraints
- **Escalation path**: the named human role that receives Tier C escalations and Tier D stop notifications
- **Session time limit**: maximum continuous autonomous operation window before a mandatory human checkpoint
- **Hard stops**: specific conditions that immediately terminate the session regardless of task completion state

An agent operating without a documented Operational Mandate is a governance finding. Its output may not be acted upon until the mandate is established retroactively and reviewed.

---

## 6. Tool Use Governance

- Tools are granted per Operational Mandate, not per agent class
- A tool that is safe in one deployment context is not automatically safe in another
- Tools with write access to production systems are Tier B minimum
- Tools that can modify access controls, credentials, or audit infrastructure are Tier C minimum
- The agent's tool invocation log is part of the audit record and subject to Log Integrity And Tamper-Evidence controls
- Tools that have not been explicitly included in the Operational Mandate are not available to the agent; the agent must escalate (Tier C) if a task requires a tool not in its mandate

---

## 7. Memory And Persistence Governance

Agentic systems with persistent memory — context retained across sessions, accumulated knowledge bases, or long-term task state — present distinct governance challenges:

- Memory scope is defined in the Operational Mandate; the agent may not expand its memory scope autonomously
- Data written to persistent memory inherits the classification of the most sensitive input in the session that produced it
- Memory contents are subject to the same access controls and retention limits as the source data
- Memory that contains Restricted data must be stored with equivalent controls to the Restricted data itself
- An agent must not use persistent memory to accumulate authority, permissions, or context that would not be granted in a fresh session
- Memory contents are reviewable by the governance role at any time; an agent that cannot produce its memory contents for review on request is a Tier D stop condition

---

## 8. Memory Provenance Control

Persistent memory is an attack surface. An agent that stores information across sessions without tracking the authority level of the source can be manipulated over time through gradual memory poisoning — a technique where a low-authority actor plants false context in small increments, each individually innocuous, but collectively redirecting the agent's behaviour in privileged interactions.

The following controls are mandatory for all agentic deployments with persistent memory:

**Provenance stamping — required for every memory write:**

Every entry written to persistent memory must be stamped at write time with:
- **Source identity**: the authenticated identity of the actor whose input produced the memory entry (human user, agent ID, system process)
- **Authority level**: the role-registry authority tier of the source identity at the time of writing
- **Timestamp**: the UTC timestamp of the write operation
- **Session reference**: the session or task ID that produced the entry, enabling full audit chain linkage
- **Content classification**: the data classification of the content at write time

Provenance metadata is immutable after write. It may not be modified, overridden, or stripped by any subsequent process.

**Authority-weighted memory retrieval:**

When the agent retrieves memory to inform a privileged decision — any decision in Tier B or above — the following rules apply:

- Memory entries sourced from external actors, low-authority users, or unauthenticated sources must be explicitly flagged as low-authority context before being included in the decision context
- Memory entries that contradict established high-authority context (entries from Governance Authority, named Operators, or system-level processes) must be flagged as conflicting and escalated to Tier C before acting on the contradiction
- An agent must not treat a low-authority memory entry as normative for a privileged decision without explicit operator confirmation

**External actor memory boundary:**

- Actors with an authority level below the threshold defined in the Operational Mandate may not write memory entries that affect Tier B or above decisions
- If a low-authority actor's input would produce a memory entry influencing a privileged decision path, the entry must be quarantined and flagged for Governance Authority review before being committed to the active memory store
- External consultants, third-party integrations, and unauthenticated sources are always below the privileged memory write threshold unless explicitly elevated by the Governance Authority in the Operational Mandate

**Memory integrity audit:**

- The memory store is subject to periodic integrity audit by the Governance Authority
- Entries without valid provenance metadata are treated as corrupted and quarantined pending review
- A pattern of low-authority entries that collectively assert false normative context — even if each individual entry appears innocuous — is a security finding and triggers Tier D stop for the affected agent

This section remediates Gap H identified in GFSA-RED-TEAM-FINDINGS-v0.1.

---

## 9. Multi-Agent And Sub-Agent Governance

When an agentic system delegates to sub-agents or operates as part of a multi-agent pipeline:

- Authority does not transfer: a sub-agent does not inherit the authority of the orchestrating agent unless explicitly granted in both mandates
- An orchestrating agent may not grant a sub-agent more authority than the orchestrating agent itself holds
- Each agent in a pipeline has its own Operational Mandate; the pipeline as a whole is reviewed before activation
- The orchestrating agent is accountable for the actions of sub-agents it invokes; this accountability does not reduce the sub-agent's own governance obligations
- Prompt injection attacks — where a sub-agent or external data source attempts to redirect the orchestrating agent — are a Tier D trigger for the affected agent
- Human accountability for the pipeline as a whole rests with the named owner in the Role Registry

---

## 10. Audit And Traceability

- Every action taken by an agentic system is logged: tool invocations, data accessed, outputs produced, decisions made, escalations triggered
- The log records the reasoning or instruction that preceded the action, not only the action itself
- Agent session logs are tamper-evident and stored under Log Integrity And Tamper-Evidence controls
- When an agentic system produces an output that is acted upon by a human or another system, the audit trail links the output to the agent session that produced it
- Accountability for agent-assisted decisions follows the AI-Human Governance framework: the human who acts on an agent output is accountable for that action

---

## 11. Prompt Injection And Instruction Integrity

Agentic systems that process external data — web content, documents, API responses, messages from other agents — are exposed to prompt injection: content crafted to redirect the agent's behaviour by embedding instructions in data.

- Agent systems must be designed to treat externally sourced content as data, not instruction
- Instructions that arrive via data channels (documents, search results, API responses) do not carry the authority of the system prompt or Operational Mandate
- An agent that detects apparent instruction-injection in a data source must treat it as a Tier D trigger and stop
- System designers are accountable for implementing architectural separation between instruction channels and data channels

---

## 12. Incident Response For Agentic Systems

When an agentic system takes an action outside its Operational Mandate, produces unintended real-world effect, or is suspected of compromise:

1. **Immediate session termination** — the agent session is stopped; no further autonomous action
2. **Session log preservation** — full session log placed under forensic hold before any investigation
3. **Scope assessment** — what actions were taken, what data was accessed, what external systems were affected
4. **Reverse or contain** — where technically feasible, reverse the agent's actions; where not, contain downstream effect
5. **Root cause** — was this a mandate gap, a tool misconfiguration, a prompt injection, a model behaviour failure, or a governance gap?
6. **Mandate review** — the Operational Mandate is suspended until root cause is established and remediated
7. **Regulatory assessment** — determine whether the incident triggers GDPR breach notification or other obligations

---

## 13. Related Documents

- AI-Human Governance
- Trust Boundaries
- Stop-State Policy
- Capability Change Gate
- Log Integrity And Tamper-Evidence Policy
- Audit And Accountability
- Identity And Credential Governance
- Privileged Access Management Policy
- Insider Threat Governance
- Data Classification And Handling Policy
- Lateral Movement Containment Policy
- Social Engineering And Human Manipulation Policy
- GDPR And EU AI Act Alignment
- Post-Quantum And Future AI Readiness
- Red Team Findings: GFSA-RED-TEAM-FINDINGS-v0.1 Gap H
