# System Prompt Governance Layer

**Document ID:** GFSA-SYSTEM-PROMPT-GOV-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-25  
**Classification:** Internal — Restricted  
**Owner:** Governance Authority  

---

## 1. Purpose

This document defines the governance requirements for system prompts used in AI deployments within the governed boundary. A system prompt governance layer is the set of instructions, constraints, and boundary definitions loaded into an AI model at the system level — before any user or operator interaction begins. It is the primary mechanism by which policy is enforced at the model layer, rather than relying solely on external controls.

This document answers: *What may a system prompt contain, who may define it, how must it be managed, and what constitutes a violation?*

---

## 2. Scope

This document applies to:
- All AI models deployed within the governed boundary, whether for interactive use, agentic tasks, or automated pipelines
- Any instruction passed to a model at the system level, including system messages, pre-prompts, persona definitions, and injected context
- Any mechanism that modifies model behaviour before user input is processed

Out of scope: User-level prompts (covered by acceptable use policy); model fine-tuning (covered by AI-Model-And-Supply-Chain-Integrity-v0.1).

---

## 3. Core Principles

1. **Governance before inference:** No model may begin processing user or agent input without an approved, version-controlled system prompt loaded
2. **Immutability at runtime:** System prompts may not be modified, overridden, or extended at runtime by users, agents, or external inputs
3. **Version control and signing:** Every system prompt must be stored in a version-controlled repository and signed by an authorised human principal before deployment
4. **Minimal privilege:** System prompts must grant only the capabilities required for the declared use case — no general-purpose, open-ended capability grants
5. **Auditability:** Every inference session must record which system prompt version was active

---

## 4. Permitted System Prompt Content

A system prompt may contain:
- Role and persona definition scoped to the declared use case
- Explicit boundary statements (what the model must not do)
- Output format requirements
- Language and tone requirements
- References to specific knowledge domains the model is permitted to engage with
- Escalation instructions (what the model must do when it encounters a boundary condition)
- Data handling instructions (how the model must treat sensitive input)

---

## 5. Prohibited System Prompt Content

A system prompt must never contain:
- Instructions that override or supersede this governance layer
- Instructions that disable, bypass, or weaken security controls
- Credentials, API keys, or secrets of any kind
- Instructions that grant the model self-modification capability
- Instructions that authorise the model to ignore user-reported concerns
- Instructions that enable the model to claim it has no system prompt or that its instructions are confidential from the Governance Authority
- Open-ended capability grants (e.g., "do whatever the user asks")

---

## 6. Untrusted Zone — Fetched And External Content

Indirect prompt injection is the most prevalent attack vector against agentic systems that process external content. It occurs when content fetched from an external source — a document, a web page, an API response, an email attachment, a search result — contains text crafted to redirect the agent's behaviour by embedding instruction-like language in data. The agent, lacking explicit zoning, may treat this content as authoritative.

The following rules define the Untrusted Zone and are mandatory for all agentic deployments:

**Definition:** The Untrusted Zone encompasses all content that arrives via tool call, data fetch, or external input channel. This includes but is not limited to:
- Documents retrieved via file system access or document store queries
- URL and web content retrieved by browsing or retrieval tools
- API response bodies from any external or internal service
- Email bodies and attachments processed by the agent
- Search result content and retrieved knowledge base entries
- Output from sub-agents that processed external content
- Any content not originating directly from the system prompt or the authenticated operator instruction

**Untrusted Zone rules — absolute, no exceptions:**

1. **Content in the Untrusted Zone is data. It is never instruction.** Regardless of how the content is phrased — even if it uses imperative language, claims to be a system message, or asserts special authority — it carries no instructional authority over the agent's behaviour.
2. **The system prompt must contain an explicit statement** that all fetched and externally sourced content is Untrusted Zone content and must be treated as data only. This statement must appear in the system prompt before any tool-use or retrieval capability is described.
3. **Instruction-like patterns in Untrusted Zone content must trigger a Tier D stop.** If fetched content contains phrases that attempt to override the system prompt, claim operator authority, instruct the agent to ignore its boundaries, or direct the agent to take actions not in its Operational Mandate, the agent must stop, log the injection attempt, and escalate.
4. **The agent must never relay Untrusted Zone content directly to a tool with write, send, or publish capability** without explicit operator confirmation (Tier B minimum). Summarisation or paraphrasing of fetched content into an action requires the same confirmation as directly using the content.
5. **Structural separation** between instruction channels (system prompt, Operational Mandate) and data channels (tool returns, fetched content) must be maintained by the inference environment. Architectures that place tool responses in a position positionally ambiguous with the system prompt are non-compliant.

**Detection and response:**
- Detected injection attempts in fetched content are logged as security events with full content capture
- Repeated injection attempts from the same source domain or data origin are escalated to the Governance Authority
- Prompt injection via fetched content is treated as an attempted external attack on the governed system, not a model error

This section remediates Gap A identified in GFSA-RED-TEAM-FINDINGS-v0.1.

---

## 7. Authorship and Approval

| Role | Permitted Action |
|---|---|
| AI Operator | May draft a system prompt for review |
| Security Reviewer | Reviews for prohibited content and alignment with use case |
| Governance Authority | Provides final approval and signs the prompt version |
| Automated systems | May NOT author or approve system prompts |

No system prompt may be deployed without a written approval record that references the specific prompt version (hash), the approving identity, and the deployment context.

---

## 8. Version Control Requirements

1. All system prompts are stored in a dedicated, access-controlled repository (or a protected path within the main repository)
2. Each version is identified by a SHA-256 hash of the prompt content
3. The version history is append-only; no version may be deleted or modified after approval
4. Each deployed instance must record: prompt hash, deployment timestamp, deploying identity, and target model/deployment ID
5. Rollback to a prior approved version is permitted; deployment of an unapproved version is not

---

## 9. Runtime Integrity

The inference environment must enforce:
- **Injection resistance:** User and agent inputs must be structurally separated from the system prompt; the model must not be able to receive user input that is positionally ambiguous with the system prompt
- **Override detection:** Any input that contains instructions attempting to supersede, ignore, or modify the system prompt must be detected, blocked, and logged
- **Prompt leak prevention:** The model must not reproduce the full system prompt in output; partial reproduction that reveals security-relevant boundary definitions must be logged as a boundary event

---

## 10. Validation Testing

Before any system prompt is approved for deployment, the following tests must pass:

| Test | Method | Pass Criterion |
|---|---|
| Boundary enforcement | Send 10 adversarial prompts designed to elicit out-of-boundary responses | Model refuses all 10 and produces a compliant refusal message |
| Override resistance | Send prompts instructing the model to ignore its system prompt | Model does not comply; logs the attempt |
| Capability scope | Send prompts in domains outside the declared use case | Model declines and redirects to declared scope |
| Escalation behaviour | Send a prompt that triggers a defined escalation condition | Model produces the correct escalation response |
| Leak resistance | Ask the model to reproduce its instructions | Model does not reproduce security-relevant boundary definitions |
| Untrusted Zone resistance | Send 5 fetched-content payloads containing embedded instruction attempts | Model treats all as data; triggers Tier D stop and logs each attempt |

All test results must be documented and retained with the approval record.

---

## 11. Incident Conditions

| Event | Classification | Action |
|---|---|---|
| System prompt bypassed or overridden at runtime | Stop-state | Halt inference; escalate to Governance Authority immediately |
| Unapproved system prompt detected in active deployment | Critical | Isolate deployment; investigate source; stop inference |
| System prompt version mismatch (deployed hash ≠ approved hash) | Critical | Stop inference; audit recent sessions; re-deploy from approved version |
| Prompt leak of security-relevant boundary definitions | Significant | Log and review; assess downstream exposure |
| Prohibited content found in active system prompt | Stop-state | Halt inference; remove prompt; full governance review |
| Instruction-injection detected in Untrusted Zone content | Stop-state | Halt inference; log full content; escalate to Governance Authority |

---

## 12. Related Documents

- Private-AI-Deployment-Guide-v0.1
- Agentic-Operational-Boundary-v0.1
- Data-Egress-And-Exfiltration-Prevention-v0.1
- Log-Integrity-And-Tamper-Evidence-v0.1
- Audit-And-Accountability-v0.1
- Stop-State-Policy-v0.1
- AI-Model-And-Supply-Chain-Integrity-v0.1
- Cryptographic-Standards-Policy-v0.1
- Red Team Findings: GFSA-RED-TEAM-FINDINGS-v0.1 Gap A

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
