# Governance-First Security Architecture
## Data Egress And Exfiltration Prevention
**Version:** 0.1 — Initial Release
**Status:** Draft / Review-Stage Template (`LM-1_REVIEW_PACKAGE` — Not Approved for Production or Compliance Use)
**Classification:** Governance Policy

---

## 1. Purpose

This policy governs what data may leave the organisation's governed environment, through which channels, in which formats, with what authorisation, and under what conditions. Data egress is not only a security boundary — it is a governance boundary. The same data that is appropriately held inside the environment becomes a liability the moment it exits without authorisation, classification control, or audit trail.

This policy addresses both intentional egress (approved data transfers, API outputs, agent tool calls, external communications) and unintentional or malicious exfiltration (data leaving the environment in ways that were not authorised).

---

## 2. Scope

Applies to all data leaving the governed environment by any mechanism: human-initiated file transfer, API calls, email and messaging, agentic system tool use, automated pipeline outputs, backup replication to external locations, and third-party integrations. Applies to structured and unstructured data, to outputs generated from governed data, and to data carried in AI system outputs.

---

## 3. Core Governance Principle

> **Data does not leave the governed environment by default. Egress is a privilege that requires a defined channel, a defined authorisation, and a complete audit trail. The absence of an explicit egress authorisation is an implicit denial. An agentic system's ability to call an external API is not an authorisation to send governed data through it.**

---

## 4. Egress Classification By Data Tier

| Data Classification | Egress Default | Authorisation Required | Channel Requirements |
|---|---|---|---|
| Public | Permitted | None beyond standard process | No restrictions |
| Internal | Restricted | Line manager or equivalent | Approved channels only; no personal storage services |
| Confidential | Denied by default | Named data owner + Security Governance (`ROLE_SECURITY_REVIEWER` / `ROLE_GOVERNANCE_REVIEWER`) | Encrypted channel; recipient identity verified; logged |
| Restricted | Denied by default | Named data owner + Security Governance (`ROLE_SECURITY_REVIEWER` / `ROLE_GOVERNANCE_REVIEWER`) + Privacy & Legal review (`ROLE_PRIVACY_REVIEWER` / `ROLE_LEGAL_COMPLIANCE_REVIEWER`, with statutory DPO consultation where personal data is affected) | End-to-end encrypted; recipient vetted; audit record mandatory; GDPR Chapter V + *Schrems II* TIA rules apply |

AI-generated outputs that contain or are derived from Confidential or Restricted data inherit that classification for egress purposes.

---

## 5. Approved Egress Channels

Data may only leave the governed environment through explicitly approved channels. Approved channels are:

- Organisation-controlled email with TLS enforcement
- Approved secure file transfer platforms with access logging
- API integrations explicitly listed in the Third-Party Governance register
- Encrypted backup replication to approved offsite locations under BCP/DR Governance
- Approved cloud storage platforms with access controls equivalent to the data's classification

The following are not approved egress channels for Confidential or Restricted data:

- Personal email accounts
- Consumer cloud storage (personal accounts on any platform)
- Messaging applications not approved for the data's classification tier
- Removable media unless under an explicit documented exception
- Agentic system tool calls to external APIs not listed in the system's Operational Mandate

---

## 6. Agentic System Egress Controls

Agentic systems present a distinct exfiltration risk: a system with legitimate internal access and external tool access can transfer data across the boundary without a human explicitly initiating the transfer.

- Every external API call made by an agentic system is an egress event and is logged as such
- Agentic systems may only send data to external endpoints explicitly listed in their Operational Mandate under the Agentic Operational Boundary
- An agentic system that encounters a task requiring data to be sent to an endpoint not in its Operational Mandate must treat this as a Tier C escalation (`REVIEW_REQUIRED` / `STOP_EGRESS_UNAUTHORIZED` if unapproved) — it does not proceed autonomously
- Data classification is checked before any external API call; a call that would send Confidential or Restricted data is Tier B minimum (confirm before execute; blocked under `STOP_SENSITIVE_DATA_EXPORT` or `STOP_SECRET_EXPORT` if unauthorized)
- Agentic system outputs that are delivered externally — reports, summaries, generated content — are assessed for derived classification before delivery
- Prompt injection attempts that instruct an agent to exfiltrate data to an external endpoint are a Tier D stop condition (`STOP_EGRESS_UNAUTHORIZED` / `INCIDENT_REVIEW_REQUIRED`)

---

## 7. Derived And Synthesised Data

Data synthesised or generated from governed sources — summaries, analyses, AI-generated reports, aggregations — inherits the classification of the most sensitive source used in its generation. This applies to:

- AI model outputs generated using Confidential or Restricted input data
- Aggregations that, while individually non-sensitive, reveal sensitive patterns in combination
- Reports generated by agentic systems from governed data sources
- Training data derivatives and model outputs where the model was trained on classified data

The originating system or person is responsible for assessing derived classification before initiating egress.

---

## 8. Exfiltration Detection Indicators

The following patterns trigger investigation under Log Integrity And Tamper-Evidence and Insider Threat Governance:

- Bulk data access followed by external transfer within the same session
- Data transfer to a destination not previously observed in the individual's or system's behaviour pattern
- Transfer volume significantly above the individual's or system's established baseline
- Repeated access to Confidential or Restricted data outside normal working hours followed by external transfer
- Use of an unapproved egress channel for data above Internal classification
- Agentic system API calls to external endpoints not listed in its Operational Mandate
- Attempts to compress, encode, or obfuscate data immediately before external transfer
- Access to audit logs or egress monitoring configuration proximate to a large data transfer

---

## 9. GDPR And Cross-Border Transfer (Chapter V & *Schrems II*)

Personal data transferred outside the EEA — including **remote access by non-EEA support engineers** (EDPB Guidelines 05/2021) and **onward transfers to non-EEA AI API sub-processors or telemetry pipelines** — is subject to GDPR Chapter V restrictions. Egress of personal data:

- Is assessed for cross-border transfer requirements before approval (`STOP_UNAPPROVED_CROSS_BORDER_TRANSFER` blocks any unapproved transfer)
- Requires an EU adequacy decision, or Standard Contractual Clauses (SCCs) / BCRs **paired with a documented *Schrems II* Transfer Impact Assessment (TIA) and EDPB Recommendations 01/2020 supplementary technical/contractual/organisational measures** (e.g., EU-held encryption keys, ingestion-time pseudonymisation, zero-retention AI API agreements); **Art. 49 derogations** apply strictly to occasional, non-repetitive transfers only
- Is logged with the transfer mechanism, TIA reference, onward sub-processor status, and recipient country
- AI system prompts, tool payloads, and outputs containing personal data are assessed under the same rules as direct personal data transfers

Operational cross-border transfer approvals and TIAs must follow an **organisation-specific, counsel-approved GDPR Chapter V Transfer SOP** with `ROLE_PRIVACY_REVIEWER`, `ROLE_LEGAL_COMPLIANCE_REVIEWER`, and statutory DPO consultation (`GDPR-EU-AI-Act-Alignment-v0.1` is a preparatory alignment document and does not itself define operational transfer procedures).

---

## 10. Related Documents

- Ingress Egress Policy
- Data Classification And Handling Policy
- Agentic Operational Boundary
- Insider Threat Governance
- Log Integrity And Tamper-Evidence Policy
- Third-Party Governance
- Identity And Credential Governance
- GDPR And EU AI Act Alignment
- Business Continuity And Disaster Recovery Governance
- Audit And Accountability
- Stop-State Policy
