# Governance-First Security Architecture — Framework Delta & Scope Map v0.1

## Status

Orientation and positioning guide (`GFSA-REV-018`).

This document is not a new policy layer and does not claim compliance with or certification under any standard listed below. It clarifies **what this project adds beyond existing security and AI-governance standards**, how the repository's documents divide into **Core Overlay vs. Assumed Baseline vs. Exploratory Research**, how **Enterprise Runtime Modes** separate from **Project Repository Modes**, and how checks divide between **deterministic inline enforcement** and **attested/human review**.

---

## 1. Framework Delta Matrix — What GFSA Adds (And Does Not Replace)

An enterprise adopting GFSA should **not** replace its existing ISO 27001, NIST CSF 2.0, IAM, SIEM, or DLP program. GFSA is designed as a **pre-action AI & agentic decision-governance overlay** addressing operational gaps left open by high-level frameworks:

| Existing Standard / Framework | What It Already Covers Well | Specific Operational Delta Added By GFSA |
| --- | --- | --- |
| **ISO/IEC 27001 & NIST CSF 2.0 / CIS Controls v8** | Enterprise ISMS, asset inventory, patching, crypto, PAM, BCDR, ransomware readiness, SOC fundamentals | GFSA assumes these as baseline; adds **pre-action AI decision semantics**, **agentic capability-change gates**, and **typed fail-closed stop states** |
| **NIST SP 800-207 (Zero Trust)** | Continuous identity/device verification and micro-segmented network access control | Extends Zero Trust from *access-to-resource* to *authority + evidence + egress + stop-state verification before every governed AI action* |
| **NIST AI RMF & ISO/IEC 42001 (AIMS)** | Organizational AI risk management lifecycle (Govern/Map/Measure/Manage) and management-system governance | Translates high-level AI risk governance into **concrete runtime decision states**, **agentic action authority tiers (A–D)**, **machine-time threat patterns (`MT-01`–`MT-04`)**, and **pre-authorized circuit breakers** |
| **OWASP Top 10 for LLM & Agentic Applications / MITRE ATLAS** | Threat taxonomies, attack techniques, and vulnerability classes (prompt injection, excessive agency, tool misuse) | Maps those threat classes directly to **mandatory pre-action stop states**, **separation of duties**, **deterministic tool/egress boundaries**, and **human accountability records** |
| **GDPR & EU AI Act (Regulation (EU) 2024/1689)** | Binding statutory obligations (lawful basis, Art. 22, DPO, Arts. 4/5/12/14/18/19/25/26/27/50/73) | Provides structured governance hooks (evidence records, anti-rubber-stamping checks, capability-change Art. 25 triggers, privacy-safe audit patterns) that *support* counsel-led compliance review without claiming compliance |

---

## 2. Corpus Partition — Core Overlay vs. Assumed Baseline vs. Exploratory Research

Although the repository contains ~95 documents for completeness, an adopting CISO or Enterprise Architect only needs the **Core AI Decision-Governance Overlay** (~15 documents):

| Corpus Layer | Purpose | Key Documents |
| --- | --- | --- |
| **Layer A — Core AI Decision-Governance Overlay (Start Here)** | The differentiated GFSA contribution: pre-action gating, typed stop states, agentic boundaries, machine-time circuit breakers, human/AI accountability, and workshop assessment | `Minimal-Viable-Governance-Kernel-v0.1`; `Decision-State-Matrix-v0.1`; `Stop-State-Registry-v0.1`; `Role-Registry-v0.1`; `Roles-And-Responsibilities-v0.1`; `AI-Human-Governance-v0.1`; `Agentic-Operational-Boundary-v0.1`; `Capability-Change-Gate-v0.1`; `Evidence-And-Source-Policy-v0.1`; `Machine-Time-Threat-Model-v0.1`; `Pre-Authorized-Circuit-Breaker-Policy-v0.1`; `CA-06-Lateral-Peer-Coordination-Rule-v0.1`; `GDPR-EU-AI-Act-Alignment-v0.1`; `Workshop-Offer-v0.1`; `Assessment-Worksheet-v0.1` |
| **Layer B — Assumed Enterprise InfoSec Baseline (Optional / Replaceable)** | Reference templates for enterprises without mature baseline policies; **enterprises with audited ISO 27001 / NIST CSF policies should retain their own** and keep only the AI-specific hooks | Ransomware Recovery, Cryptographic Standards, BCDR, PAM, Vulnerability Disclosure/Patching, Secrets Sprawl, Security Awareness, Social Engineering, Network Segmentation, Log Integrity/Retention, Vendor Offboarding, Insider Threat, Data Classification |
| **Layer C — Exploratory Research (Non-Operational / Unvalidated)** | Early research hypotheses included for critical challenge only; **must not** be treated as operational controls | `Deceptive-Containment-Environment-Conceptual-Foundation-v0.1`; `Agentic-Identity-Security-Conceptual-Foundation-v0.1` |

---

## 3. Enterprise Runtime Modes vs. Project Repository Modes

`Mode-Model-Normalization-v0.1` (`LM-0`..`LM-6`, `ODM-0`..`ODM-7`) governs **this documentation repository and its synthetic prototype gate** (where every ODM intentionally blocks `Runtime/Production`). Adopting enterprises governing live AI workflows should map their workflows to **Enterprise Runtime Modes** unified with the **Agentic Authority Tiers (`Agentic-Operational-Boundary-v0.1`)**:

| Enterprise Runtime Mode | Permitted AI / Agentic Scope | Unified Agentic Tier Mapping | Canonical Decision Default |
| --- | --- | --- | --- |
| `OBSERVE_ONLY` | Read-only telemetry, search, summarization; zero write/egress | Assistive read-only | `ALLOW` (within scoped read mandate) |
| `ADVISORY_DRAFT` | AI drafts recommendations/artifacts; human reviews and executes | Assistive (`ROLE_AI_ASSISTANT`) | `ALLOW_WITH_CONDITIONS` / `REVIEW_REQUIRED` |
| `SUPERVISED_CONFIRM` | Agent proposes tool calls or internal changes; named human confirms before execution | **Tier B — Confirm** | `REVIEW_REQUIRED` / `ALLOW_WITH_CONDITIONS` |
| `BOUNDED_AUTONOMOUS` | Agent executes strictly bounded, reversible, pre-authorized low-risk tool calls inside Operational Mandate | **Tier A — Autonomous** | `ALLOW` (with async audit + circuit breakers) |
| `ESCALATE_HOLD` | Out-of-mandate request, capability change, high/critical risk, or legal/privacy trigger | **Tier C — Escalate** | `NEEDS_AUTHORITY` / `NEEDS_CAPABILITY_REVIEW` / `REVIEW_REQUIRED` |
| `QUARANTINE_LOCKDOWN` / `INCIDENT` | Active hostile signal, prompt-injection exfiltration attempt, CA-06 peer coordination, or prohibited AI use | **Tier D — Mandatory Stop** | `BLOCK` / `QUARANTINE` / `LOCKDOWN` / `INCIDENT_RESPONSE` |

---

## 4. Technical Enforcement Split — Deterministic Policy Engine vs. Attested Human Gates

A practical enterprise architecture must never ask a non-deterministic LLM to self-enforce hard security boundaries. GFSA's six core gates split cleanly across two runtime enforcement tiers:

| Enforcement Tier | Latency & Mechanism | GFSA Gates Enforced Here | Enterprise Integration Point |
| --- | --- | --- | --- |
| **Tier 1 — Deterministic Inline Policy Enforcement** | Milliseconds; deterministic code / policy-as-code (no LLM-as-a-judge) | Mode/Tier check, Actor/Role/Token validity, Tool allowlist, Egress channel & data-tag block, Pre-authorized circuit breakers, Audit-write verification | **AI Gateway / Tool Broker + Policy Engine (OPA / Cedar) + IAM + DLP + SIEM** |
| **Tier 2 — Attested / Human Review Gates** | Asynchronous (minutes to days); cryptographically signed ticket/attestation consumed by Tier 1 | Evidence sufficiency & counter-evidence review, Capability-change & EU AI Act Art. 25 reclassification review, DPIA/FRIA & lawful-basis sign-off, High-risk Tier B/C human approval (anti-rubber-stamping) | **GRC / ServiceNow / Jira CAB + Privacy/DPO Workflow + Signed Mandate Registry** |
