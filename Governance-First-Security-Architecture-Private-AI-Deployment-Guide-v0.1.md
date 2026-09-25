# Private-AI Deployment Guide

**Document ID:** GFSA-PRIVATE-AI-DEPLOY-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-25  
**Classification:** Internal  
**Owner:** Governance Authority  

---

## 1. Purpose

This document provides a concrete, step-by-step guide for deploying and validating a fully private, self-hosted AI environment — such as one based on an Ollama/Lugano-style stack — under the governance controls defined in this architecture. It bridges the gap between the conceptual policies (Network Segmentation, Ingress-Egress, Data Exfiltration Prevention) and the operational reality of standing up an isolated AI inference environment.

A "Private AI" environment in this context means:
- All model weights are stored and executed locally
- No prompts, outputs, or telemetry leave the controlled boundary
- All access is authenticated and audited
- The environment can operate fully air-gapped or network-isolated

---

## 2. Scope

This guide applies to:
- On-premises or private-cloud AI inference deployments
- Self-hosted model serving (e.g., Ollama, llama.cpp, vLLM, LocalAI)
- Environments where data sovereignty, confidentiality, or regulatory compliance requires zero external model API calls
- Prototype and production-grade Private-AI environments governed by this architecture

Out of scope: Cloud-hosted AI APIs, shared inference endpoints, fine-tuning pipelines.

---

## 3. Prerequisite Governance Gates

Before deployment begins, the following governance conditions must be satisfied:

| Gate | Document Reference | Required State |
|---|---|---|
| Asset registered | Asset-Register-v0.1 | AI host machine registered as a controlled asset |
| Network segment defined | Network-Segmentation-Architecture-v0.1 | Dedicated AI inference segment created |
| Ingress/egress rules approved | Ingress-Egress-Policy-v0.1 | Outbound rules set to deny-all by default |
| Data classification confirmed | Data-Classification-And-Handling-Policy-v0.1 | All input/output data classified before deployment |
| Roles assigned | Role-Registry-v0.1 | AI Operator and Governance Reviewer roles filled |
| Stop-state trigger defined | Stop-State-Policy-v0.1 | At least one hard stop condition documented |

No deployment proceeds until all gates are confirmed in writing by the Governance Authority.

---

## 4. Reference Stack (Lugano/Ollama Example)

The following is a reference stack validated against this architecture. Other stacks are permitted provided they satisfy all governance requirements below.

```
┌─────────────────────────────────────────────┐
│           PRIVATE AI BOUNDARY               │
│                                             │
│  ┌──────────────┐   ┌─────────────────────┐ │
│  │  Model Store │   │  Inference Engine   │ │
│  │  (local FS)  │──▶│  (Ollama / llama.cpp│ │
│  └──────────────┘   └──────────┬──────────┘ │
│                                │             │
│                    ┌───────────▼──────────┐  │
│                    │   API Gateway        │  │
│                    │   (authenticated,    │  │
│                    │    rate-limited)     │  │
│                    └───────────┬──────────┘  │
│                                │             │
│                    ┌───────────▼──────────┐  │
│                    │   Audit Logger       │  │
│                    │   (append-only,      │  │
│                    │    tamper-evident)   │  │
│                    └──────────────────────┘  │
└─────────────────────────────────────────────┘
         │ No outbound traffic permitted │
```

**Stack components:**
- **Model storage:** Local encrypted filesystem (LUKS or equivalent); models verified by SHA-256 hash against a signed manifest before loading
- **Inference engine:** Ollama (recommended for single-node), llama.cpp (recommended for embedded/air-gapped), vLLM (recommended for multi-GPU)
- **API gateway:** Nginx or Caddy with mutual TLS; all requests require a signed token; no unauthenticated endpoint exposed
- **Audit logger:** Append-only structured log (JSON Lines); written to a separate volume; integrity protected per Log-Integrity-And-Tamper-Evidence-v0.1

---

## 5. Deployment Procedure

### Phase 1 — Environment Preparation

1. **Provision the host machine** on the designated AI inference network segment.
2. **Harden the OS:** Disable all non-essential services; apply CIS Benchmark Level 2 (or equivalent); remove compilers and package managers from production image.
3. **Configure network rules:** Apply deny-all outbound; whitelist only intra-boundary traffic; confirm with a network scan before proceeding.
4. **Mount encrypted model storage:** Verify encryption key is held in the approved key management system (not on the host).
5. **Document host in Asset Register** with: hostname, IP, OS version, model storage path, assigned Operator identity.

### Phase 2 — Model Integrity Verification

1. **Obtain model weights** through the approved supply chain (see AI-Model-And-Supply-Chain-Integrity-v0.1).
2. **Verify SHA-256 hash** of each model file against the signed manifest.
3. **Record verification result** in the audit log before any model is loaded.
4. **Reject and quarantine** any model that fails hash verification; escalate to Governance Authority.

### Phase 3 — Service Configuration

1. **Install inference engine** from a verified, pinned release (hash-verified installer).
2. **Configure API gateway** with mutual TLS; generate per-operator client certificates; disable all unencrypted endpoints.
3. **Set resource limits:** CPU, RAM, and GPU quotas to prevent runaway inference consuming host resources needed for security controls.
4. **Configure audit logger** with an append-only volume; test tamper-evidence mechanism before going live.
5. **Define and load the system prompt governance layer:** Any system-level instructions that enforce boundaries must be loaded from a version-controlled, signed configuration file — not passed ad hoc.

### Phase 4 — Validation and Sign-Off

1. **Run the network isolation test:** Attempt an outbound HTTP request from the inference engine; confirm it is blocked and logged.
2. **Run the authentication test:** Attempt an unauthenticated API call; confirm it is rejected with a 401 and logged.
3. **Run the audit integrity test:** Write a test log entry; attempt to modify it; confirm tamper evidence triggers.
4. **Run a governance prompt test:** Send a prompt that should trigger a boundary violation (e.g., a request to exfiltrate data); confirm the system prompt governance layer blocks it and logs the event.
5. **Governance Authority sign-off:** A designated reviewer confirms all four tests passed and countersigns the deployment record.

### Phase 5 — Operational Hand-Off

1. **Document all access credentials** in the approved secrets store (never in config files).
2. **Brief the AI Operator** on stop-state triggers and escalation path.
3. **Schedule first audit review** within 30 days of deployment.
4. **Confirm in the Asset Register** that the environment is now in operational status.

---

## 6. Air-Gap Variant

For environments that must be fully disconnected:

- Model weights are transferred via verified physical media (USB with hash manifest); media is destroyed or securely stored after transfer
- No network interface is active during inference; network cards are disabled at BIOS/UEFI level
- Audit logs are exported via verified physical media on a defined schedule and verified by the Governance Authority off-system
- All updates follow the same physical media procedure; no remote update mechanism is permitted

---

## 7. Ongoing Governance Requirements

| Requirement | Frequency | Owner |
|---|---|---|
| Model hash re-verification | Monthly | AI Operator |
| Access credential rotation | Quarterly | Identity & Credential Governance |
| Network isolation re-test | Quarterly | Security Reviewer |
| Audit log integrity check | Weekly | AI Operator |
| Full governance review | Annually | Governance Authority |
| Stop-state test | Semi-annually | Governance Authority |

---

## 8. Failure Modes and Stop Conditions

| Failure | Immediate Action | Stop State? |
|---|---|---|
| Model hash mismatch | Halt inference; quarantine model; escalate | Yes |
| Outbound traffic detected from inference engine | Isolate host immediately; investigate | Yes |
| Unauthenticated access succeeds | Isolate API gateway; audit all recent sessions | Yes |
| Audit log tamper evidence triggers | Preserve log state; escalate to Governance Authority | Yes |
| System prompt governance layer bypassed | Halt inference; review all outputs since last known-good state | Yes |

All stop conditions reference Stop-State-Policy-v0.1 and must be logged in Stop-State-Registry-v0.1.

---

## 9. Related Documents

- Network-Segmentation-Architecture-v0.1
- Ingress-Egress-Policy-v0.1
- Data-Egress-And-Exfiltration-Prevention-v0.1
- AI-Model-And-Supply-Chain-Integrity-v0.1
- Log-Integrity-And-Tamper-Evidence-v0.1
- Stop-State-Policy-v0.1
- Stop-State-Registry-v0.1
- Asset-Register-v0.1
- Identity-And-Credential-Governance-v0.1
- Cryptographic-Standards-Policy-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
