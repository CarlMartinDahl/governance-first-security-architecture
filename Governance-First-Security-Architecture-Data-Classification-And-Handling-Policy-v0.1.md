# Governance-First Security Architecture
## Data Classification And Handling Policy
**Version:** 0.1 — Initial Release
**Status:** Active
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
- **Who designates:** Communications Authority or named equivalent

### Tier 2 — Internal
Data intended for use within the organisation but not approved for external distribution. Exposure causes limited harm.
- **Examples:** Internal process documentation, meeting notes without sensitive content, non-sensitive operational data
- **Default for:** General internal communications and documents with no other classification signal

### Tier 3 — Confidential
Data whose unauthorised disclosure would cause significant harm: reputational, financial, legal, or operational.
- **Examples:** Business strategy, contracts, financial data, personnel records, security architecture documentation, audit findings, incident reports
- **Default when in doubt:** Yes — unclassified data with unclear sensitivity defaults here
- **Access:** Named roles only; access logged

### Tier 4 — Restricted
Highest sensitivity. Unauthorised disclosure causes severe harm or triggers legal obligations. Includes all data subject to specific regulatory protection.
- **Examples:** Personal data (GDPR), special category personal data (GDPR Article 9), credentials and cryptographic material, payment card data, health records, vulnerability details pre-remediation, law enforcement requests
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
| Third-party processing | Permitted | Standard DPA | DPA + security review | DPA + security review + ongoing monitoring |
| Retention | Per business need | Per retention schedule | Per retention schedule | Per retention schedule + regulatory minimum |
| Disposal | Standard deletion | Secure deletion | Secure deletion + confirmation | Cryptographic erasure or physical destruction + certificate |
| Bulk export | Permitted | Logged | Logged + approved | Logged + dual approval + audit trail |

---

## 7. Personal Data (GDPR Overlay)

All personal data as defined under GDPR is classified minimum Restricted regardless of other characteristics. Special category personal data (Article 9: health, biometric, political opinion, religious belief, etc.) is Restricted with additional handling controls:

- Processing requires explicit lawful basis documented in the Record of Processing Activities (RoPA)
- Access is limited to roles with a documented, specific business need
- Pseudonymisation is required where processing purpose permits
- Data subject rights requests (access, erasure, portability) are handled under the GDPR And EU AI Act Alignment document
- Cross-border transfers outside the EEA require an approved transfer mechanism

---

## 8. AI And Model Data

AI systems introduce data classification complexity because data flows through training, fine-tuning, inference, and output in ways that may not be visible to end users:

- Training datasets are classified at the level of their most sensitive constituent data
- Restricted data must not be used in AI training without explicit governance authorisation and documented legal basis
- Model outputs that could reveal Restricted training data (membership inference, extraction attacks) are themselves treated as Restricted
- AI-generated content based on Confidential inputs is classified Confidential until reviewed
- Agentic AI systems that access data must operate under access credentials scoped to the minimum classification tier required for their task

---

## 9. Reclassification

- **Upgrading** (e.g. Internal → Restricted): Any person may upgrade; no approval required; notification to data owner recommended
- **Downgrading** (e.g. Confidential → Internal): Requires named approval from the Data Governance role; rationale documented in Audit and Accountability
- **Declassification to Public**: Requires Communications Authority approval; irreversible once published

---

## 10. Third-Party And Cloud Handling

- Data shared with third parties retains its classification; the receiving party is bound to equivalent controls via contractual obligation
- Cloud storage locations for Confidential and Restricted data must be inventoried in the Asset Register with encryption and access control configuration documented
- Third parties processing Restricted data are subject to Third-Party Governance review including security assessment
- Data residency requirements (EEA, sector-specific) are documented per dataset in the Asset Register

---

## 11. Breach Impact Assessment

Data classification directly determines breach severity and notification obligations:

| Classification Lost | Presumed Severity | GDPR Notification |
|---|---|---|
| Public | Negligible | Not required |
| Internal | Low | Not required unless combined with other data |
| Confidential | Medium–High | Assess per specific data content |
| Restricted (personal data) | High–Critical | 72-hour supervisory authority notification likely required |
| Restricted (special category) | Critical | 72-hour notification required; individual notification likely required |

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
