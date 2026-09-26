# Governance-First Security Architecture
## Threat Intelligence Intake
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy
**Document Owner:** Martin Dahl
**Verification Owner:** Martin Dahl

---

## 1. Purpose

This document defines how external threat intelligence is ingested, assessed, prioritised, and translated into governance actions within the governed environment. Monitoring-And-Detection-Operations governs internal detection of anomalous behaviour. This document governs the complementary process: receiving intelligence about the external threat landscape and ensuring that intelligence reaches the correct governance control in time to be acted upon.

Without a defined intake process, threat intelligence is ad hoc. A CVE may be published, an ISAC may issue a warning, or a STIX feed may flag a campaign targeting AI infrastructure — and none of it reaches the Detection Engine, the Patch Governance process, or the Agent Baseline Profile unless a human happens to notice. This document closes that gap.

---

## 2. Scope

Applies to all external threat intelligence relevant to:
- The governed AI and agentic system environment
- Infrastructure components (OS, runtime, API gateway, inference engine, identity systems)
- AI model and inference supply chain (model providers, fine-tuning pipelines, weight sources)
- Cryptographic dependencies and post-quantum transition risks
- Regulatory and compliance threat signals (new requirements, enforcement actions, guidance updates)

Does not apply to internal anomaly detection, which is governed by Monitoring-And-Detection-Operations.

---

## 3. Intelligence Source Registry

The following source categories are recognised as authoritative intake channels. Sources must be registered before their intelligence is acted upon. Unregistered sources may be reviewed but do not trigger governance actions without Governance Authority approval.

| Source Category | Examples | Update Frequency | Primary Governance Target |
|---|---|---|---|
| CVE / NVD feeds | NIST NVD, MITRE CVE | Continuous | Vulnerability-Disclosure-And-Patch-Governance |
| STIX/TAXII feeds | MITRE ATT&CK, commercial TI platforms | Continuous / scheduled | Detection-Engine rule updates, Agent-Baseline-Profile |
| ISAC advisories | AI-ISAC, FS-ISAC, ENISA advisories | Event-driven | Monitoring-And-Detection-Operations, Stop-State-Policy |
| Vendor security bulletins | Cloud provider advisories, inference engine vendors, model providers | Event-driven | Vulnerability-Disclosure-And-Patch-Governance |
| National cyber authority advisories | NCSC (SE/UK), CISA, BSI | Event-driven | All relevant controls depending on advisory scope |
| Post-quantum cryptography updates | NIST PQC standardisation, BSI PQC guidance | Periodic | Cryptographic-Policy, Post-Quantum-Readiness |
| Regulatory threat signals | EU AI Act enforcement guidance, GDPR supervisory authority rulings | Event-driven | GDPR-And-EU-AI-Act-Alignment |
| AI-specific threat research | Published adversarial ML research, prompt injection campaigns, model theft disclosures | Event-driven | Agent-Baseline-Profile, Detection-Engine, System-Prompt-Governance-Layer |

---

## 4. Intake Process

### 4.1 Intake Flow

All threat intelligence follows this intake sequence regardless of source:

```
External Source
      │
      ▼
┌─────────────────────────────┐
│ 1. RECEIVE                  │
│    AI Operator or automated │
│    feed subscription        │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ 2. ASSESS                   │
│    Relevance to governed    │
│    environment?             │
│    Severity classification? │
└─────────────┬───────────────┘
              │
       ┌──────┴──────┐
   Not relevant   Relevant
       │              │
       ▼              ▼
  Log and       ┌─────────────────────────────┐
  close         │ 3. ROUTE                    │
                │    Assign to correct        │
                │    governance control       │
                └─────────────┬───────────────┘
                              │
                              ▼
                ┌─────────────────────────────┐
                │ 4. ACT                      │
                │    Control owner takes      │
                │    defined action per SLA   │
                └─────────────┬───────────────┘
                              │
                              ▼
                ┌─────────────────────────────┐
                │ 5. CLOSE                    │
                │    Action recorded in       │
                │    intake log; finding      │
                │    closed or tracked        │
                └─────────────────────────────┘
```

### 4.2 Relevance Assessment Criteria

Intelligence is assessed as relevant if it meets any of the following criteria:

- Affects a component or dependency in the governed environment (OS, runtime, inference engine, API gateway, identity system, cryptographic library)
- Describes an attack technique applicable to AI agents, agentic pipelines, or prompt injection
- Involves a threat actor known to target AI infrastructure or the organisation's sector
- Represents a change in regulatory posture that affects the governance framework
- Describes a vulnerability with CVSS score ≥ 7.0 in any registered dependency
- Relates to post-quantum cryptographic risk affecting active cryptographic controls

---

## 5. Severity Classification

Once assessed as relevant, intelligence is classified by intake severity:

| Intake Severity | Criteria | SLA for Governance Action |
|---|---|---|
| **Critical** | CVSS ≥ 9.0; active exploitation confirmed; direct impact on AI agent runtime or identity systems | 24 hours |
| **High** | CVSS 7.0–8.9; credible exploitation likely; significant impact on governed components | 72 hours |
| **Medium** | CVSS 4.0–6.9; no confirmed exploitation; indirect or partial impact | 14 days |
| **Low** | CVSS < 4.0; informational; emerging research; no immediate exploitation path | Next scheduled review cycle |
| **Regulatory** | Regulatory guidance or enforcement action; no CVSS applicable | Assessed case by case; default 30 days |

Intake severity is independent of the severity classification used by the original source. The AI Operator assigns intake severity based on impact to the governed environment specifically.

---

## 6. Routing Rules

Each piece of relevant intelligence is routed to one or more governance controls based on its type and affected component:

| Intelligence Type | Primary Route | Secondary Route (if applicable) |
|---|---|---|
| CVE in infrastructure component | Vulnerability-Disclosure-And-Patch-Governance | Monitoring-And-Detection-Operations (if exploitable in-flight) |
| New AI attack technique (prompt injection, model theft, supply chain) | Agent-Baseline-Profile update review | System-Prompt-Governance-Layer; Detection-Engine rule review |
| ISAC advisory or national authority alert | Governance Authority notification | Monitoring-And-Detection-Operations; Stop-State-Policy review |
| Post-quantum cryptographic risk | Cryptographic-Policy review | Post-Quantum-Readiness update |
| Regulatory guidance update | GDPR-And-EU-AI-Act-Alignment review | Governance Authority notification |
| Active campaign targeting sector | Governance Authority notification | Monitoring-And-Detection-Operations (HR/TR/PR rule tuning); Incident-Response-Policy |
| Vendor security bulletin | Vulnerability-Disclosure-And-Patch-Governance | Capability-Change-Gate if patch requires component replacement |

Routing does not transfer accountability. The AI Operator who receives the intelligence retains accountability for confirming that the routed control owner has acknowledged receipt within the intake SLA.

---

## 7. Detection Engine Integration

Threat intelligence that describes new attack techniques or indicators of compromise must be reviewed for translation into Detection Engine rules. This review is not automatic — it requires human judgement.

- The AI Operator presents new technique intelligence to the Security Reviewer
- The Security Reviewer assesses whether new HR, TR, or PR rules are warranted (per Monitoring-And-Detection-Operations Section 5)
- Approved new rules are added under the standard Capability Change Gate process
- New rules derived from threat intelligence are tagged with the originating intelligence reference in the rule comment
- Temporary detection uplift (increasing sensitivity of existing rules during an active campaign) may be approved by the Governance Authority without full Capability Change Gate process, for a defined period not exceeding 30 days

---

## 8. Intake Log

All received intelligence — whether assessed as relevant or not — is recorded in the Intake Log. The log is append-only and integrity-protected per Log-Integrity-And-Tamper-Evidence-Policy.

Each log entry records:

| Field | Description |
|---|---|
| Entry ID | Sequential identifier (TI-YYYY-NNN) |
| Received date | Date intelligence was received |
| Source | Registered source category and specific source identifier |
| Summary | One-sentence description of the intelligence |
| Relevance assessment | Relevant / Not relevant; reasoning |
| Intake severity | Critical / High / Medium / Low / Regulatory (if relevant) |
| Routed to | Governance control(s) receiving the intelligence |
| Action SLA | Date by which governance action must be confirmed |
| Action confirmed | Date action was confirmed by receiving control owner |
| Status | Open / Closed / Escalated |

Entries with status Open beyond their Action SLA are escalated to the Governance Authority automatically.

---

## 9. Review Schedule

| Review Type | Frequency | Owner | Output |
|---|---|---|---|
| Intake log review | Weekly | AI Operator | Confirm all Open items within SLA; escalate overdue items |
| Source registry review | Quarterly | Security Reviewer + AI Operator | Confirm registered sources are still active and authoritative; add new sources; remove defunct sources |
| Detection engine translation review | Quarterly | Security Reviewer + AI Operator | Confirm all High/Critical intelligence from prior quarter has been reviewed for detection engine impact |
| Full intake effectiveness review | Semi-annually | Governance Authority | Coverage of source categories; SLA adherence; translation rate to detection rules |

---

## 10. Relationship to Vulnerability Disclosure And Patch Governance

This document governs the *intake* of threat intelligence. Vulnerability-Disclosure-And-Patch-Governance governs what happens *after* a vulnerability is received and accepted as relevant. The handoff point is the routing step in Section 6: once intelligence is assessed as relevant and routed to Vulnerability-Disclosure-And-Patch-Governance, that document's SLAs and processes take over.

The Intake Log entry remains open until the receiving control owner confirms action. Patch governance closure does not automatically close the intake log entry — the AI Operator must confirm and record closure explicitly.

---

## 11. Related Documents

- Monitoring-And-Detection-Operations
- Vulnerability-Disclosure-And-Patch-Governance
- Agent-Baseline-Profile
- System-Prompt-Governance-Layer
- Cryptographic-Policy
- Post-Quantum-Readiness
- GDPR-And-EU-AI-Act-Alignment
- Incident-Response-Policy
- Log-Integrity-And-Tamper-Evidence-Policy
- Capability-Change-Gate
- Stop-State-Policy

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
