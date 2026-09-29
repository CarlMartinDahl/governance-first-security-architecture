# Governance-First Security Architecture
## Governance Maturity Model
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy
**Document Owner:** Martin Dahl

---

## 1. Purpose

This document defines the maturity model against which the Governance-First Security Architecture assesses and communicates its current state. A governance framework without a maturity axis cannot honestly answer the question: *how complete is this, and what is left to do?*

The model serves three functions:

1. **Internal prioritisation** — identifies which dimensions are weakest and where effort produces the most governance value
2. **External communication** — gives external reviewers, potential adopters, and auditors a calibrated, honest view of the framework’s current state without overclaiming
3. **Progress tracking** — provides a stable reference point against which future versions can demonstrate advancement

This model is not a compliance certification. A Level 3 rating on any dimension is not a security guarantee. It means the governance structures that make security auditable and improvable are in place.

---

## 2. Maturity Levels

Four maturity levels apply to each dimension. The levels are cumulative: a higher level requires all lower-level criteria to be met.

| Level | Name | Meaning |
|---|---|---|
| **1** | Defined | The governance requirement is documented and scoped. Someone knows what needs to exist. |
| **2** | Structured | The requirement is implemented with named owners, explicit processes, and traceable decisions. |
| **3** | Verified | The implementation has been tested, reviewed, or independently assessed. Evidence exists. |
| **4** | Adaptive | The implementation is continuously monitored, reviewed on a defined cycle, and updated in response to findings. |

Level 1 is the floor for any document that exists in this architecture. An undocumented control does not reach Level 1.

---

## 3. Maturity Dimensions

The architecture is assessed across six dimensions. Each dimension covers a distinct governance concern.

### Dimension 1: Policy Coverage

Does the framework define governance requirements across all relevant domains?

| Level | Criteria |
|---|---|
| 1 | Core governance domains are identified: identity, access, data, AI agents, monitoring, incident response, cryptography |
| 2 | Each domain has at least one dedicated policy document with defined scope, owner, and requirements |
| 3 | Policies are internally consistent; cross-references are accurate; no domain is implicitly governed by a document in another domain |
| 4 | Policy gaps are identified on a defined cycle; new domains (e.g. post-quantum, regulatory changes) are incorporated before they become operational risks |

### Dimension 2: Control Implementation

Are the governance requirements translated into specific, testable controls?

| Level | Criteria |
|---|---|
| 1 | Controls are named and described for each major governance requirement |
| 2 | Each control has defined firing criteria, ownership, and a response requirement |
| 3 | Controls have been analytically or empirically tested; detection boundaries are explicitly documented |
| 4 | Controls are tuned on a defined cycle based on false positive rates, incident findings, and new threat intelligence |

### Dimension 3: Observability

Can the framework detect when its own controls are failing or being violated?

| Level | Criteria |
|---|---|
| 1 | Log sources are identified for all governed components |
| 2 | A detection engine exists with defined rules; alerts are routed to a named human role |
| 3 | Monitoring coverage requirements are defined and measured; monitoring gaps trigger stop conditions |
| 4 | External threat intelligence is ingested on a defined cycle and translated into detection rule updates |

### Dimension 4: Process Integrity

Are governance decisions made through documented, repeatable processes with traceable authority?

| Level | Criteria |
|---|---|
| 1 | Decision-making processes exist for major governance events (capability changes, incidents, reviews) |
| 2 | Each process has defined roles, inputs, outputs, and escalation paths; no process requires improvisation |
| 3 | Processes have been exercised at least once and findings incorporated; post-review revision logs exist |
| 4 | Processes are reviewed on a defined cycle; bottlenecks and single points of failure are identified and mitigated |

### Dimension 5: Evidence Quality

Does the framework produce evidence that can be independently audited?

| Level | Criteria |
|---|---|
| 1 | Audit log requirements are defined; what must be logged is specified |
| 2 | Logs are append-only, integrity-protected, and retained per a defined policy |
| 3 | Evidence has been used in at least one review or test scenario; the evidence chain is traceable from event to governance record |
| 4 | Evidence quality is reviewed on a defined cycle; gaps in the evidence chain are tracked as findings |

### Dimension 6: External Validation

Has the framework been assessed by someone other than its author?

| Level | Criteria |
|---|---|
| 1 | An external review process is defined; a review package exists that a reviewer could use |
| 2 | At least one external reviewer has been engaged; their feedback is documented |
| 3 | External review findings have been incorporated; the revision log is traceable to reviewer feedback |
| 4 | External validation is scheduled on a defined cycle; reviewer scope expands as the framework matures |

---

## 4. Current State Assessment — GFSA v0.1

The following assessment reflects the honest current state of the Governance-First Security Architecture as of version 0.1. Assessments are conservative: a dimension is rated at the highest level for which all criteria are fully met, not partially met.

| Dimension | Current Level | Rationale | Next Step to Advance |
|---|---|---|---|
| Policy Coverage | **3** | 60+ documents covering all core domains; internal consistency review completed (GFSA-REV-010); cross-references corrected. Gap: new domains (threat intelligence intake) only just added at v0.1. | Advance to 4 by establishing a formal policy gap review cycle (quarterly or semi-annual) |
| Control Implementation | **2** | Controls named and described with firing criteria and ownership. CA-06 Control Test completed analytically; detection boundaries documented. Gap: empirical testing in a live or prototype environment not yet performed. | Advance to 3 via prototype implementation and live control test (gated by PDG-028 external review) |
| Observability | **3** | Monitoring-And-Detection-Operations defines sources, rules, coverage requirements, and stop conditions. Threat Intelligence Intake now defines external feed process. Gap: detection engine and monitoring infrastructure not yet implemented (documentation only at v0.1). | Advance to 4 by implementing and operating the monitoring infrastructure; demonstrating TI-to-rule translation cycle |
| Process Integrity | **3** | Capability Change Gate, PDG process, Post-Review Revision Log, Internal Consistency Review, and Documentation Freeze Gate all exist and have been exercised. Single point of failure (sole author) is documented as a known risk. | Advance to 4 by introducing a second named process authority and scheduling process reviews |
| Evidence Quality | **2** | Audit log requirements defined; append-only and integrity-protection requirements specified in Log-Integrity-And-Tamper-Evidence-Policy. Gap: no live audit log has been produced; evidence chain is theoretical at v0.1. | Advance to 3 via prototype implementation that produces real (synthetic) audit log entries reviewed in a test scenario |
| External Validation | **3** | External review package exists (PDG-028); two external reviews completed and incorporated (GFSA-REV-009; GFSA-REV-012, PDG-028 boundary review); Post-Review-Revision-Log is traceable. Gap: external review breadth remains limited to a small reviewer set. | Advance to 4 by broadening external review beyond the initial reviewers |

### 4.1 Overall Maturity Summary

```
Dimension               Level   Status
─────────────────────────────────────────────────────
1. Policy Coverage       3/4    Defined, structured, verified
2. Control Implementation 2/4   Defined, structured
3. Observability         3/4    Defined, structured, verified
4. Process Integrity     3/4    Defined, structured, verified
5. Evidence Quality      2/4    Defined, structured
6. External Validation   3/4    Defined, structured, verified
─────────────────────────────────────────────────────
Overall GFSA v0.1:       2.7 / 4.0 (documentation-only phase)
```

The 2.7 average reflects an architecture that is well-defined, structured, and partially verified — but not yet empirically tested or operating in a live environment. This is the correct and expected state for a documentation-only v0.1 release. The two dimensions at Level 2 (Control Implementation, Evidence Quality) are structurally dependent on prototype implementation, which is gated by external review per PDG-028.

---

## 5. Advancement Roadmap

The critical path to Level 3 across all dimensions runs through prototype implementation, which is gated by PDG-028 external review.

| Phase | Gate | Expected Maturity Outcome |
|---|---|---|
| Current (v0.1 documentation) | — | 2.7 / 4.0 as assessed above |
| Post external review | PDG-028 condition met (GFSA-REV-012, 2026-09-27) | External Validation advances to 4; Process Integrity advances to 4 |
| Post prototype implementation | PDG-028 gate passed | Control Implementation advances to 3; Evidence Quality advances to 3 |
| Post operational monitoring cycle | 6 months live operation | Observability advances to 4; Policy Coverage advances to 4 |
| Full v1.0 | All dimensions ≥ 3 | Target: 3.5+ average |

---

## 6. What This Model Does Not Claim

- A Level 3 or Level 4 rating on any dimension is not a security validation claim
- This model is self-assessed at v0.1; it has not been externally validated
- Maturity level is not a compliance certification for GDPR, EU AI Act, ISO 27001, or any other standard
- A high maturity score on this model does not mean the architecture is free of vulnerabilities or implementation flaws

This model measures *governance structure quality*, not security outcome guarantees.

---

## 7. Review Schedule

| Review Type | Frequency | Owner | Output |
|---|---|---|---|
| Maturity self-assessment update | At each major version release | Governance Authority | Updated Section 4 table |
| External maturity review | At v1.0 gate | External Reviewer | Independent validation of self-assessment ratings |
| Dimension advancement confirmation | When a dimension advances | Governance Authority | Updated assessment table; commit to Post-Review-Revision-Log |

---

## 8. Related Documents

- Minimal-Viable-Governance-Kernel
- Post-Review-Revision-Log
- Prototype-Design-Readiness-Checklist (PDG-028 gate)
- Monitoring-And-Detection-Operations
- Threat-Intelligence-Intake
- External-Review-Checklist
- Capability-Change-Gate
- Log-Integrity-And-Tamper-Evidence-Policy
- GDPR-And-EU-AI-Act-Alignment

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
