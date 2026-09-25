# Recovery and Rollback — Incident Procedures

**Document ID:** GFSA-RECOVERY-ROLLBACK-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-25  
**Classification:** Internal  
**Owner:** Governance Authority  

---

## 1. Purpose

This document defines the procedures for recovering the governed AI environment to a known-good state after a security incident, neutralization event, or stop-state activation. It covers both rollback (returning to a prior verified state) and recovery (restoring service in a governance-compliant manner). It is the operational successor to the Active-Neutralization-Runbook-v0.1 and is invoked after the immediate threat has been contained.

This document answers: *How do we safely return to normal operation after an incident, and how do we verify that we are actually safe before we do?*

---

## 2. Scope

This document applies to:
- Any recovery following a stop-state event (Stop-State-Policy-v0.1)
- Any recovery following agent neutralization (Active-Neutralization-Runbook-v0.1)
- Any rollback of AI model, system prompt, agent configuration, or infrastructure state
- Partial recoveries (restoring some services while others remain suspended)

Out of scope: Routine maintenance, planned upgrades, and non-security-related outages (which follow standard operational procedures).

---

## 3. Recovery Principles

1. **Verified state first:** No service is restored until a governance-verified known-good state has been identified and confirmed
2. **Root cause before restoration:** The root cause of the incident must be understood and addressed before any affected component is restored; restoration without root cause resolution is prohibited
3. **Staged restoration:** Services are restored in order of decreasing criticality; no stage proceeds without verification of the prior stage
4. **Governance Authority gates every stage:** Each restoration stage requires explicit Governance Authority approval before proceeding
5. **Independent verification:** Verification of restored state must be performed by a role different from the one that performed the restoration
6. **Audit continuity:** Audit logging must be verified as intact and operational before any other service is restored

---

## 4. Known-Good State Definition

A known-good state is a recorded snapshot of the environment that:
- Was explicitly approved by the Governance Authority at the time of recording
- Has a cryptographic integrity record (hash of all component versions, configurations, and system prompt versions)
- Was recorded before the earliest confirmed point of compromise
- Has been verified against its integrity record at the time of recovery

If no known-good state can be identified that predates the compromise, a **clean rebuild** is required (see Section 8).

---

## 5. Recovery Classification

Before recovery begins, classify the incident to determine the appropriate recovery track:

| Class | Description | Recovery Track |
|---|---|---|
| **Class 1 — Agent Isolation** | A single agent was neutralized; infrastructure and other agents are unaffected | Track A: Agent Replacement |
| **Class 2 — Configuration Compromise** | A system prompt, configuration, or policy file was tampered with | Track B: Configuration Rollback |
| **Class 3 — Model Compromise** | The model weights or inference engine were tampered with | Track C: Model Rollback |
| **Class 4 — Infrastructure Compromise** | The host, network, or storage layer was compromised | Track D: Infrastructure Rebuild |
| **Class 5 — Full Environment Compromise** | Multiple classes; coordinated attack across layers | Track E: Full Clean Rebuild |

Classification is determined by the Governance Authority based on the incident record and attribution findings. A higher class always supersedes a lower class.

---

## 6. Track A — Agent Replacement

*Use when: A single agent was neutralized; all other components are verified clean.*

1. **Verify the root cause** of the compromised agent's behaviour (per Agent-Attribution-Playbook-v0.1 post-incident findings)
2. **Resolve the root cause** before any replacement: if the cause was a system prompt vulnerability, update and re-approve the system prompt; if it was a capability boundary gap, update the Agentic-Operational-Boundary and the agent's baseline profile
3. **Create a new agent identity:** The compromised agent's identity token is permanently revoked; a replacement agent receives a new identity, not a reissued version of the old one
4. **Load the approved, updated system prompt** (hash-verified)
5. **Register a new baseline profile** for the replacement agent (per Agent-Baseline-Profile-v0.1)
6. **Run supervised trial period** (minimum 3 sessions or 24 hours) before returning to unsupervised operation
7. **Governance Authority sign-off** on return to full operation

---

## 7. Track B — Configuration Rollback

*Use when: A system prompt, governance configuration, or policy file was tampered with.*

1. **Halt all inference** using the compromised configuration immediately
2. **Preserve the tampered configuration** as evidence (hash and store; do not delete)
3. **Identify the last approved configuration version** from the version control history; verify its integrity hash
4. **Assess the exposure window:** Determine how long the tampered configuration was active and what inferences were processed during that window
5. **Review all outputs from the exposure window** for potential boundary violations or harmful outputs; document findings
6. **Restore the approved configuration** (copy from version control to deployment; do not re-run through any process that touched the tampered version)
7. **Re-run Phase 4 validation tests** from Private-AI-Deployment-Guide-v0.1 against the restored configuration
8. **Governance Authority sign-off** before resuming inference
9. **Open a configuration integrity investigation** to determine how the tampering occurred and whether the version control or signing mechanism was also compromised

---

## 8. Track C — Model Rollback

*Use when: Model weights or the inference engine binary were tampered with or a compromised version was loaded.*

1. **Halt all inference immediately** — a compromised model may produce harmful outputs even with a correct system prompt
2. **Preserve the compromised model artefacts** as evidence (do not delete; isolate to a write-protected evidence volume)
3. **Identify the last verified model version** from the supply chain record (AI-Model-And-Supply-Chain-Integrity-v0.1); retrieve its approved hash
4. **Obtain a clean copy of the verified model** through the approved supply chain procedure; verify its hash before loading
5. **Inspect the inference engine binary** independently; if it was also tampered with, replace it from a verified source
6. **Re-run Phase 2 and Phase 3** of the Private-AI-Deployment-Guide-v0.1 in full
7. **Re-run Phase 4 validation tests** in full
8. **Assess outputs from the exposure window** (all inferences made with the compromised model); document and remediate any harmful outputs
9. **Governance Authority sign-off** before resuming inference
10. **Notify supply chain:** If the compromise originated in the supply chain, escalate to the model provider and update the Supply Chain Abuse Cases document

---

## 9. Track D — Infrastructure Rollback

*Use when: The host machine, storage layer, or network configuration was compromised.*

1. **Take the entire host offline** immediately; do not attempt to recover in-place
2. **Preserve disk images** as forensic evidence before any changes
3. **Provision a new host** from a verified, clean base image on the correct network segment (per Network-Segmentation-Architecture-v0.1)
4. **Restore from a pre-compromise backup** only if the backup integrity is verified; otherwise proceed as a clean build
5. **Re-execute the full deployment procedure** from Phase 1 of the Private-AI-Deployment-Guide-v0.1
6. **Do not migrate any data or configuration** from the compromised host without explicit inspection and approval by the Security Reviewer
7. **Investigate the compromise vector** before bringing the replacement host online; if the vector is still active, restoration will re-compromise the new host
8. **Governance Authority sign-off** at each phase of re-deployment

---

## 10. Track E — Full Clean Rebuild

*Use when: Multiple layers are compromised or the extent of compromise cannot be bounded.*

1. **Take the entire environment offline**
2. **Preserve all forensic evidence** before any changes
3. **Conduct a full incident investigation** before beginning rebuild; the scope of rebuild must be based on confirmed findings, not assumptions
4. **Build from first principles:** New hosts, new model downloads (hash-verified from source), new configurations authored from scratch (not copied from the compromised environment), new agent identities
5. **Each component follows its applicable track** (A through D) as a sub-procedure within the full rebuild
6. **Independent verification at every stage** by a role not involved in the rebuild
7. **External review** (if available): an independent party reviews the rebuild plan and verification results before the environment is brought back online
8. **Governance Authority sign-off on each stage and final go-live**
9. **Post-incident report** documenting: timeline, root cause, extent of compromise, all actions taken, and governance improvements made as a result

---

## 11. Downstream Impact Remediation

Regardless of track, if any harmful outputs were delivered to downstream systems or humans during the incident window:

1. **Identify all affected recipients** of outputs from the incident window
2. **Assess each output** for potential harm: incorrect information acted upon, data exfiltrated, instructions executed, decisions made
3. **Notify affected parties** as required by applicable regulations and the organisation's incident communication policy
4. **Remediate where possible:** Correct records, reverse actions, provide updated information
5. **Document all remediation actions** in the incident record
6. **Determine whether regulatory reporting is required** (data breach, AI Act incident reporting, etc.)

---

## 12. Return-to-Normal Checklist

Before declaring the environment fully recovered and closing the incident:

- [ ] Root cause identified and resolved
- [ ] All affected components restored from verified sources
- [ ] Full Phase 4 validation tests passed on all restored components
- [ ] Audit log integrity verified and continuous
- [ ] All agent baseline profiles reviewed and updated
- [ ] All identity tokens from the incident window revoked and replaced
- [ ] Downstream impact assessed and remediated
- [ ] Incident record complete and signed by Governance Authority
- [ ] Post-incident governance debrief completed
- [ ] Any governance document updates identified have been scheduled

---

## 13. Related Documents

- Active-Neutralization-Runbook-v0.1
- Agent-Attribution-Playbook-v0.1
- Stop-State-Policy-v0.1
- Stop-State-Registry-v0.1
- Private-AI-Deployment-Guide-v0.1
- AI-Model-And-Supply-Chain-Integrity-v0.1
- System-Prompt-Governance-Layer-v0.1
- Agent-Baseline-Profile-v0.1
- Log-Integrity-And-Tamper-Evidence-v0.1
- Network-Segmentation-Architecture-v0.1
- Business-Continuity-And-Disaster-Recovery-Governance-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
