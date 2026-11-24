# Governance-First Security Architecture — Governance Decision Assessment Worksheet v0.1

## Status

Operational workshop template (commercial discovery — updated under `GFSA-REV-018`).

This worksheet is not a new architecture layer. It operationalizes the Core AI Decision-Governance Overlay (`Framework-Delta-And-Scope-Map-v0.1`, `Minimal-Viable-Governance-Kernel-v0.1`, `Agentic-Operational-Boundary-v0.1`, `Decision-State-Matrix-v0.1`, `Stop-State-Registry-v0.1`, `Role-Registry-v0.1`, and `GDPR-EU-AI-Act-Alignment-v0.1`) into a runnable 2–3 hour or 1-day workshop sheet for **both assistive and agentic AI workflows**.

It does not constitute legal advice, compliance certification, security validation, or authorization for production automation.

---

## Core Assessment Formula

```text
Authority + Evidence + Mode/Tier & Risk + Egress + Stop Path + Accountability
before any governed AI-assisted or agentic action.
```

Rule: **The most restrictive valid signal wins.** A stop state is a valid governance outcome, not a system failure.

---

## 1. Pre-Session Scope, Confidentiality & Legal Hygiene

| Field | Entry |
| --- | --- |
| Organization / Team | |
| NDA / Confidentiality Classification | `[ ] Mutual NDA executed` / `[ ] Client Confidential — Internal Only` |
| Data Ownership & Facilitator GDPR Role | Completed worksheet belongs to Client; facilitator processes no live customer PII or production secrets during session |
| Artifact Retention & Deletion | Retained strictly for agreed engagement window (`____ days`), then deleted or returned per client instruction |
| Workshop Format | `[ ] Option A (2–3 hours)` / `[ ] Option B (1 working day)` |
| Single Workflow In Scope | |
| Executive Sponsor & Participants | Sponsor: `__________` · Roles: Business / Tech / Security / Privacy-DPO / Legal |
| Target Enterprise Runtime Mode (`Framework-Delta-And-Scope-Map-v0.1`) | `OBSERVE_ONLY` / `ADVISORY_DRAFT` / `SUPERVISED_CONFIRM` / `BOUNDED_AUTONOMOUS` |
| Existing Enterprise Stack to Map Into | AI Gateway / IAM / Policy Engine (OPA/Cedar) / DLP / SIEM / ISO 42001 or NIST AI RMF program |

> **Live-data prohibition:** Use synthetic or anonymized workflow examples during the workshop. Do **not** paste live personal data, credentials, or production secrets into this worksheet.

---

## 2. Gate 0 — Legal, Privacy & EU AI Act Pre-Screen (10 Minutes)

Complete before mapping workflow actions (escalate any `YES` or `UNCLEAR` to `ROLE_LEGAL_COMPLIANCE_REVIEWER`, `ROLE_PRIVACY_REVIEWER`, and independent statutory **DPO**):

| Screening Question | Answer (`YES` / `NO` / `UNCLEAR`) | Triggered Canonical Gate / Required Action |
| --- | --- | --- |
| **EU AI Act Art. 5 (Prohibited Practices):** Does the workflow involve workplace emotion inference (Art. 5(1)(f)), social scoring, or manipulative exploitation? | | If `YES` → Hard stop (`STOP_PROHIBITED_AI_USE`) |
| **EU AI Act High-Risk (Annex I / Annex III) or Art. 25 Reclassification:** Does it affect employment/worker monitoring (Annex III(4)(b)), credit/insurance, critical infrastructure, or fine-tune/rebrand a third-party model? | | If `YES` → Counsel classification + Art. 27 FRIA check (`STOP_DPIA_OR_FRIA_REQUIRED`) + Art. 4 literacy + Art. 73 incident routing |
| **EU AI Act Art. 50 Transparency:** Do natural persons interact with AI or receive synthetic content requiring disclosure/marking? | | If `YES` → Add external disclosure requirement to Section 3 |
| **GDPR Personal / Art. 9 Data & Lawful Basis:** Does the workflow process personal data or special-category data? Is Art. 5(1)(b) purpose + Art. 6(1)/9(2) lawful basis documented in RoPA? | | If missing → `STOP_LAWFUL_BASIS_MISSING`; if high-risk/employee monitoring → mandatory GDPR Art. 35 DPIA + DPO advice + Art. 88/works-council check |
| **GDPR Chapter V Cross-Border Transfer:** Do prompts, tool calls, sub-processors, or support access cross outside the EEA? | | If `YES` without adequacy or SCC + *Schrems II* TIA → `STOP_UNAPPROVED_CROSS_BORDER_TRANSFER` |
| **GDPR Art. 22 Automated Decisions:** Can the workflow or an automated block produce legal or similarly significant effects on a natural person? | | If `YES` → Enforce non-rubber-stamped human review (*SCHUFA* / AI Act Art. 14(4)(b)) + human contestability path (Art. 22(3)) |

---

## 3. Decision Map & Guardrail Matrix (5–8 Concrete Workflow Steps)

Map each step using the customer's **actual job titles** alongside canonical GFSA authority tiers and decisions:

| Step ID | Workflow Step & Tool / System Touched | AI Authority Tier (`Assistive`, `Tier A Autonomous`, `Tier B Confirm`, `Tier C Escalate`, `Tier D Stop`) | Risk (`LOW`, `MED`, `HIGH`, `CRIT`) | Accountable Human Owner / Approver (Customer Title + `ROLE_*`) | Egress & Data Tier (`Internal` / `Confidential` / `Restricted` + External Endpoint?) | Decision & Stop State on Failure (`ALLOW`, `ALLOW_WITH_CONDITIONS`, `REVIEW_REQUIRED`, `BLOCK`, `INCIDENT_RESPONSE` + `STOP_*`) |
| --- | --- | --- | --- | --- | --- | --- |
| D-01 | | | | | | |
| D-02 | | | | | | |
| D-03 | | | | | | |
| D-04 | | | | | | |
| D-05 | | | | | | |

---

## 4. Six-Gate Kernel Check & Enforcement Split

| Gate | Core Question | Enforcement Layer (`Tier 1 Inline Policy` vs `Tier 2 Human/Attested`) | Status (`PASS` / `PARTIAL` / `GAP`) | Gap / Technical Guardrail Needed |
| --- | --- | --- | --- | --- |
| **1. Authority** | Named human owner/approver assigned; requester ≠ approver on high-risk steps; AI never self-approves; DPO independent? | Tier 1 (IAM/token) + Tier 2 (role record) | | |
| **2. Evidence** | Source authority, freshness limits, and counter-evidence defined (plus anti-automation-bias display for human approvers)? | Tier 2 (signed attestation / UI cue) | | |
| **3. Mode & Capability** | Explicit runtime mode (`OBSERVE_ONLY` / `ADVISORY_DRAFT` / `SUPERVISED_CONFIRM` / `BOUNDED_AUTONOMOUS`) enforced; new tools/fine-tuning gated? | Tier 1 (AI Gateway / tool allowlist) + Tier 2 (Capability Change Gate) | | |
| **4. Egress & Transfer** | External APIs/tools allowlisted in Operational Mandate; secrets/restricted data blocked by default; Chapter V / TIA verified? | Tier 1 (Egress Gateway / DLP) | | |
| **5. Stop & Circuit Breakers** | Fail-closed canonical stop states wired to reversible pre-authorized circuit breakers (machine-time containment) + escalation path? | Tier 1 (Circuit Breaker) + Tier 2 (SOC/IR) | | |
| **6. Privacy-Safe Audit & Rollback** | Privacy-minimised, retention-bounded tamper-evident audit trail (metadata/hashes in WORM, PII separated/erasable per GDPR Art. 5(1)(e)/17) + verified rollback? | Tier 1 (Log pipeline) + Tier 2 (Recovery test) | | |

---

## 5. Stop-State Gaps, Do-Not-Automate Register & Next Safe Actions

### Stop-State Gaps
| Gap ID | Step | Missing Control / Guardrail | Target Canonical Stop State | Named Owner | Target Implementation Point (AI Gateway / IAM / DLP / SOP) |
| --- | --- | --- | --- | --- | --- |
| GAP-01 | | | | | |
| GAP-02 | | | | | |

### Explicit Do-Not-Automate List
Actions in this workflow that must **remain human-decided** (four-eyes where high/critical risk) and must not be delegated to autonomous AI execution:

1. `___________________________________________________________________` (Rationale: `____________________`)
2. `___________________________________________________________________` (Rationale: `____________________`)
3. `___________________________________________________________________` (Rationale: `____________________`)

### Prioritized Next Safe Actions (30/60/90-Day Blueprint)
| Priority | Action | Owner | Target System / Governance Artifact | Verification Evidence |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## 6. Worked Example (Synthetic Illustration — Customer Refund & Escalation Agent)

*Illustrative example showing expected workshop output granularity (synthetic only — not production advice):*

| Step ID | Workflow Step & Tool Touched | AI Authority Tier | Risk | Accountable Human Owner | Egress & Data Tier | Decision & Failure Stop State |
| --- | --- | --- | --- | --- | --- | --- |
| EX-01 | Read order & return policy via internal CRM API | `Tier A Autonomous` (`BOUNDED_AUTONOMOUS`) | `LOW` | Support Ops Lead (`ROLE_SYSTEM_OWNER`) | Internal only (`Confidential` routine customer data; Art. 6(1)(b) contract basis) | `ALLOW` (fail closed → `STOP_MODE_BOUNDARY` if unapproved CRM endpoint called) |
| EX-02 | Issue refund ≤ €50 via Billing API | `Tier A Autonomous` (bounded tool allowlist + daily velocity circuit breaker) | `MED` | Finance Ops Manager (`ROLE_APPROVER`) | Internal Billing API; Art. 50 customer AI notice shown | `ALLOW_WITH_CONDITIONS` (exceeds daily velocity → circuit breaker `QUARANTINE`) |
| EX-03 | Issue refund > €50 or override return window | `Tier B Confirm` (`SUPERVISED_CONFIRM`) | `HIGH` | Team Lead (`ROLE_APPROVER`; shown order evidence + fraud flags to avoid rubber-stamping) | Internal Billing API | `REVIEW_REQUIRED` (`STOP_AUTHORITY_MISSING` if unconfirmed) |
| EX-04 | Export customer dispute history to external non-EEA analytics tool | `Tier C Escalate` / `Tier D Stop` | `CRIT` | Privacy Lead (`ROLE_PRIVACY_REVIEWER`) + Legal (`ROLE_LEGAL_COMPLIANCE_REVIEWER`) | External non-EEA (`Restricted` bulk PII) | `BLOCK` (`STOP_UNAPPROVED_CROSS_BORDER_TRANSFER` / `STOP_SENSITIVE_DATA_EXPORT`) |

**Do-Not-Automate (Example):** (1) Refunds > €500 or fraud-flagged account closures (GDPR Art. 22 significant effect → mandatory human decision + contestability); (2) Adding new Billing API scopes or fine-tuning the model on customer tickets (Capability Change Gate + EU AI Act Art. 25 check).

---

## Boundary Reminder

```text
This worksheet is a structured governance assessment and design aid only.
Completion of this worksheet does not constitute legal advice, GDPR or EU AI Act
compliance, certification, security validation, or authorization for production
AI deployment or runtime automation.
```
