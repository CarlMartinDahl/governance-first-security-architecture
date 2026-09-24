# Governance-First Security Architecture
## AI Model And Supply Chain Integrity
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy governs the integrity of AI models and the supply chain through which they are acquired, deployed, updated, and retired. A model that has been tampered with, poisoned during training, or substituted in transit is an adversarial system operating inside the governed environment with all the trust and access of a legitimate system. Model integrity is not a model provider's responsibility alone — it is a governance obligation of the deploying organisation.

This policy addresses model provenance, integrity verification, update governance, and the specific risks of training data poisoning, weight manipulation, and supply chain substitution.

---

## 2. Scope

Applies to all AI models deployed within the governed environment: foundation models accessed via API, locally hosted models, fine-tuned models, embedded models in third-party products, and models used by agentic systems as reasoning or execution engines. Applies to the full lifecycle: acquisition, deployment, update, and retirement.

---

## 3. Core Governance Principle

> **A model's behaviour cannot be fully predicted from its documentation. Provenance verification, behavioural testing, and continuous monitoring are not optional quality gates — they are the governance controls that make model deployment a managed risk rather than an uncontrolled one. Trusting a model because its provider is reputable is not the same as verifying its integrity.**

---

## 4. Model Provenance Requirements

Before any model is deployed in the governed environment:

- **Source verification**: the model originates from a documented, approved source; supply chain for the model weights or API endpoint is recorded in the Asset Register
- **Cryptographic integrity check**: where the provider publishes checksums or cryptographic signatures for model weights, these are verified before deployment; a model whose integrity cannot be verified is not deployed without a documented exception
- **Provider assessment**: the model provider is assessed under Third-Party Governance; their security posture, incident history, and update practices are reviewed
- **Licence and data provenance**: the model's training data provenance is assessed for legal risk and for potential training data poisoning vectors; models trained on unvetted internet scrapes without documented filtering carry higher risk
- **Behavioural baseline**: before deployment, the model is assessed against a defined set of test cases that probe for: unexpected capability boundaries, refusal bypasses, instruction-following anomalies, and outputs inconsistent with documented behaviour

---

## 5. Model Update And Patch Governance

Model updates — including provider-side updates to API-accessed models — are supply chain events:

- Model updates are treated as new deployments for governance purposes; they pass through the same provenance and integrity checks as the initial deployment
- Provider-side updates to API-accessed models that change model behaviour are detected through continuous behavioural monitoring and trigger a governance review
- A model update that introduces behaviour inconsistent with the deployed model's established baseline is treated as a potential integrity event pending investigation
- The Capability Change Gate is triggered by any model update that materially changes the model's capabilities or behaviour profile
- Model rollback capability is maintained: the previous model version must be recoverable for minimum 30 days after an update

---

## 6. Training Data Poisoning

For models fine-tuned or trained within the organisation's environment:

- Training data is classified under the Data Classification And Handling Policy before use; Restricted data requires explicit approval for training use
- Training data sources are documented and reviewed for integrity; data sourced from external or user-generated inputs carries higher poisoning risk
- Fine-tuning pipelines are isolated from production systems; a fine-tuning environment that has access to production data or systems is a finding
- Fine-tuned models are behaviourally tested after training and before deployment; the test set includes adversarial probes designed to detect poisoning-induced behaviour changes
- Training runs are logged with data sources, hyperparameters, and output model checksums; this log is the provenance record for the model

---

## 7. Model Weight Integrity

For locally hosted models:

- Model weights are stored in the governed environment with access controls equivalent to Confidential data minimum
- Weight files are checksummed at storage and verified at load time; a weight file that fails integrity check is not loaded
- Unexpected modification of weight files is a Tier D stop condition for any system using those weights
- Weight files are not accessible to agentic systems or application-tier systems; they are managed exclusively through defined model serving infrastructure
- Model weight backups follow the backup governance in Business Continuity And Disaster Recovery Governance

---

## 8. Behavioural Monitoring

Deployed models are monitored continuously for behavioural drift — changes in output patterns that may indicate compromise, unintended update, or emergent capability:

- A baseline of model behaviour is established at deployment using a defined probe set
- Probe set results are compared at minimum weekly; significant deviation triggers investigation
- Monitoring covers: output format consistency, refusal rate changes, latency anomalies, unexpected capability appearances, and outputs inconsistent with the model's documented training
- Behavioural monitoring logs are tamper-evident per Log Integrity And Tamper-Evidence Policy
- A model that exhibits behaviour materially inconsistent with its baseline is suspended pending investigation; its outputs are not acted upon during the investigation period

---

## 9. Agentic System Model Integrity

Agentic systems that use models as reasoning engines have an amplified model integrity risk: a compromised reasoning model in an agentic system can direct tool use, data access, and external communications in ways that a stateless inference endpoint cannot.

- The model used as a reasoning engine in each agentic system is explicitly named in the Operational Mandate per the Agentic Operational Boundary
- A change to the reasoning model used by an agentic system is a new deployment requiring full provenance and integrity review
- Agentic systems are monitored for decision-pattern drift in addition to output-pattern drift; unexpected changes in tool selection, escalation frequency, or data access patterns may indicate reasoning model compromise
- An agentic system whose reasoning model fails integrity checks is a Tier D stop condition

---

## 10. Incident Response For Model Integrity Events

When a model integrity event is suspected or confirmed:

1. **Immediate suspension** — the affected model and any agentic systems using it are suspended
2. **Output review** — outputs produced since the suspected integrity breach are reviewed and flagged; downstream actions taken on those outputs are assessed
3. **Integrity verification** — model weights or API endpoint are re-verified against known-good checksums or provider attestation
4. **Provider notification** — if the model is API-accessed, the provider is notified of the suspected integrity event
5. **Root cause** — was this a supply chain compromise, an unannounced update, a weight file modification, or a monitoring false positive?
6. **Regulatory assessment** — if the model processed personal data during the integrity breach window, GDPR breach notification obligations are assessed
7. **Redeployment gate** — the model is not redeployed until integrity is confirmed and root cause is understood

---

## 11. Related Documents

- Supply Chain Abuse Cases
- Agentic Operational Boundary
- Third-Party Governance
- Asset Register
- Capability Change Gate
- Data Classification And Handling Policy
- Log Integrity And Tamper-Evidence Policy
- Business Continuity And Disaster Recovery Governance
- Post-Quantum And Future AI Readiness
- GDPR And EU AI Act Alignment
- Stop-State Policy
- Audit And Accountability
