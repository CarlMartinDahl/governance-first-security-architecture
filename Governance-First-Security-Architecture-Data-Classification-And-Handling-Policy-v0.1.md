# Governance-First Security Architecture
## Data Classification And Handling Policy
**Version:** 0.1 — Initial Release
**Status:** Draft / Review-Stage Template (`LM-1_REVIEW_PACKAGE` — Not Approved for Production or Compliance Use)
**Classification:** Governance Policy

---

## 1. Purpose

This policy defines how data is classified by sensitivity and how each classification tier governs storage, transmission, access, sharing, retention, and disposal. Classification is the foundational control that makes GDPR alignment, access scoping, and breach impact assessment operational rather than aspirational.

Without classification, every data governance decision defaults to the most restrictive or the most permissive depending on individual judgement — neither is acceptable.

---

## 2. Scope

Applies to all data created, received, processed, stored, or transmitted by the organisation or on its behalf: structured data, unstructured documents, communications, logs, AI training data, model outputs, and data held by third parties under processing agreements.

---

## 3. Core Governance Principle

> **Data must be classified at creation or first receipt. The default classification when in doubt is Confidential. Downgrading a classification requires explicit approval; upgrading is immediate and requires no approval.**

---

## 4. Classification Tiers

### Tier 1 — Public
Data explicitly approved for unrestricted external distribution.
- **Examples:** Published documentation, press releases, open source code, public website content
- **Default:** No — data is not Public unless explicitly designated
- **Who designates:** Communications Authority (`ROLE_SYSTEM_OWNER` / `ROLE_APPROVER` delegate) or named equivalent

### Tier 2 — Internal
Data intended for use within the organisation but not approved for external distribution. Exposure causes limited harm.
- **Examples:** Internal process documentation, meeting notes without sensitive content, non-sensitive operational data
- **Default for:** General internal communications and documents with no other classification signal

### Tier 3 — Confidential
Data whose unauthorised disclosure would cause significant harm: reputational, financial, legal, or operational.
- **Examples:** Business strategy, contracts, financial data, routine/low-risk personal data (such as standard B2B contacts and basic employee directory/administrative data subject to GDPR baseline controls), security architecture documentation, audit findings, incident reports
- **Default when in doubt:** Yes — unclassified data with unclear sensitivity defaults here
- **Access:** Named roles only; access logged

### Tier 4 — Restricted
Highest sensitivity. Unauthorised disclosure causes severe harm or triggers heightened legal obligations. Includes high-risk personal data and data subject to special statutory protection.
- **Examples:** High-risk personal data, special category personal data (GDPR Article 9: health, biometric, trade union, etc.), criminal offence data (Article 10), children's data, bulk personal datasets, sensitive HR health/disciplinary records, credentials and cryptographic material, payment card data, vulnerability details pre-remediation, law enforcement requests
- **Access:** Minimum necessary; dual-person access for bulk operations; all access logged
- **Handling:** Additional controls mandatory (see Section 6)

---

## 5. Classification At Creation

- Data created internally must be classified by the creator at the point of creation
- Data received externally must be classified by the recipient within 24 hours of receipt
- AI-generated outputs inherit the classification of the most sensitive input data used to produce them
- Aggregated data is classified at the level of the most sensitive component — combining Internal and Restricted data produces Restricted data
- Classification labels must be applied in document metadata, file naming conventions, or system tags as appropriate to the medium

---

## 6. Handling Requirements By Tier

| Control | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Storage encryption at rest | Recommended | Required | Required | Required + key management audit |
| Transmission encryption | Recommended | Required | Required | Required; no unencrypted path permitted |
| Access control | None required | Authenticated users | Named roles only | Named individuals; logged |
| Sharing externally | Permitted | Requires approval | Requires named approval + NDA | Requires explicit governance authorisation |
| Third-party processing | Permitted | Contractual confidentiality (GDPR Art. 28 DPA only if acting as personal-data processor) | Confidentiality / Art. 28 DPA (processor) or Art. 26 / Controller agreement + security review | Art. 28 DPA (with sub-processor controls) or Art. 26 / Controller agreement + security & privacy review + ongoing monitoring |
| Retention | Per business need | Per retention schedule | Per retention schedule | Per retention schedule + GDPR Art. 5(1)(e) ceiling |
| Disposal | Standard deletion | Secure deletion | Secure deletion + confirmation | Cryptographic erasure or physical destruction + certificate |
| Bulk export | Permitted | Logged | Logged + approved | Logged + dual approval + audit trail |

---

## 7. Personal Data (Risk-Based GDPR Overlay)

Consistent with GDPR Art. 24 and Art. 32 risk-based proportionality, personal data is tiered rather than flatly collapsed into a single bucket: routine/low-risk personal data (e.g., standard B2B contacts or basic administrative records) is classified **minimum Tier 3 Confidential** with GDPR Arts. 5, 6, and 32 baseline controls, while **high-risk personal data, GDPR Art. 9 special category data, Art. 10 data, children's data, bulk personal datasets, and sensitive HR/health records** are classified **Tier 4 Restricted**:

- Processing requires a specified purpose (Art. 5(1)(b)) and documented statutory lawful basis (Art. 6(1), plus Art. 9(2) condition where applicable) recorded in the Record of Processing Activities (RoPA, Art. 30); missing lawful basis triggers `STOP_LAWFUL_BASIS_MISSING`
- Access is limited to roles with a documented, specific business need
- Pseudonymisation is applied where processing purpose permits
- Data subject rights requests (Arts. 15–22: access, rectification, erasure, restriction, portability, objection, and Art. 22 automated-decision contestability) must follow an **organisation-specific, counsel-approved DSAR SOP** meeting the GDPR Art. 12(3) 1-month deadline (note: `GDPR-EU-AI-Act-Alignment-v0.1` is a preparatory alignment document and does not itself define operational DSAR workflows)
- Cross-border transfers outside the EEA require an approved GDPR Chapter V mechanism plus *Schrems II* Transfer Impact Assessment (TIA) and supplementary measures (`STOP_UNAPPROVED_CROSS_BORDER_TRANSFER` when absent)
- Third-party sharing must distinguish **Data Processors (Art. 28 DPA + sub-processor authorisation)**, **Joint Controllers (Art. 26 arrangement)**, and **Independent Controllers (Data Sharing Agreement)**

---

## 8. AI And Model Data

AI systems introduce data classification and regulatory complexity because data flows through training, fine-tuning, inference, and output in ways that may not be visible to end users:

- Training datasets are classified at the level of their most sensitive constituent data
- Restricted data must not be used in AI training or fine-tuning without explicit governance authorisation, documented GDPR lawful basis, DPIA (Art. 35), and statutory DPO consultation
- **EU AI Act Art. 25 provider reclassification warning:** Fine-tuning, substantially modifying, rebranding, or changing the intended purpose of a third-party AI system into a high-risk use case can legally reclassify a deployer as a **Provider** under EU AI Act Art. 25(1) (inheriting conformity assessment, CE marking, Art. 11 technical documentation, QMS, and Art. 73 incident reporting). Any model fine-tuning or modification therefore requires a Capability Change Gate and `ROLE_LEGAL_COMPLIANCE_REVIEWER` review
- Model outputs that could reveal Restricted training data (membership inference, extraction attacks) are themselves treated as Restricted
- AI-generated content based on Confidential inputs is classified Confidential until reviewed
- Agentic AI systems that access data must operate under access credentials scoped to the minimum classification tier required for their task

---

## 9. Reclassification

- **Upgrading** (e.g. Internal → Restricted): Any person may upgrade; no approval required; notification to data owner recommended
- **Downgrading** (e.g. Confidential → Internal): Requires named approval from the Data Governance function (mapped in `Role-Registry-v0.1` to `ROLE_GOVERNANCE_REVIEWER` and `ROLE_PRIVACY_REVIEWER` where personal data is involved); rationale documented in Audit and Accountability
- **Declassification to Public**: Requires Communications Authority (`ROLE_SYSTEM_OWNER` / `ROLE_APPROVER` delegate) approval; irreversible once published

---

## 10. Third-Party And Cloud Handling

- Data shared with third parties retains its classification; the receiving party is bound to equivalent controls via contractual obligation
- Cloud storage locations for Confidential and Restricted data must be inventoried in the Asset Register with encryption and access control configuration documented
- Third parties processing Restricted data are subject to Third-Party Governance review including security assessment
- Data residency requirements (EEA, sector-specific) are documented per dataset in the Asset Register

---

## 11. Breach Impact Assessment

Data classification informs breach severity and statutory notification assessment (covering confidentiality, integrity, **and availability** compromise under GDPR Art. 4(12)):

| Classification Affected | Presumed Severity | GDPR Art. 33 / Art. 34 Assessment |
|---|---|---|
| Public | Negligible | Not required |
| Internal (non-personal) | Low | Not required unless combined with personal data |
| Confidential (incl. routine personal data) | Medium–High | Assess risk to individuals; Art. 33(1) 72-hour notification required unless unlikely to result in risk (or notify Controller under Art. 33(2) if Processor) |
| Restricted (high-risk personal data) | High–Critical | Art. 33(1) 72-hour notification likely required unless unlikelihood of risk is documented (e.g., encrypted with uncompromised key) |
| Restricted (special category / Art. 9–10) | Critical | Art. 33(1) 72-hour notification required unless strictly unlikely to result in risk; Art. 34 individual notification required where high risk is **likely** |

---

## 12. Related Documents

- Asset Register
- GDPR And EU AI Act Alignment
- Third-Party Governance
- Identity And Credential Governance
- Audit And Accountability
- Ransomware Recovery Policy
- Log Integrity And Tamper-Evidence Policy
- AI-Human Governance
- Vendor Offboarding And Revocation
