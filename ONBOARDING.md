# External Reviewer Onboarding Guide

**For:** External reviewers, potential adopters, and first-time contributors 
**Time required:** 30 minutes to oriented; 2–4 hours for a meaningful review 
**Package status:** `FROZEN_FOR_EXTERNAL_REVIEW` 
**Not required:** Prior familiarity with this architecture

---

## What This Repository Is

This is a documentation-only governance framework for AI agents and agentic systems. It defines how an organisation governs what AI agents are permitted to do, how their behaviour is monitored, how violations are detected and responded to, and how governance decisions are made and recorded.

It is **not** implementation code. It is **not** a security certification. It is **not** a compliance guarantee. It is a structured set of governance policies, processes, and controls at the documentation stage, prepared for external review before any prototype work begins.

Your job as a reviewer is to find what is wrong, missing, contradictory, or overclaimed — not to validate that it is correct.

---

## Before You Start: Two Documents to Read First

These two documents give you the architectural core and the rules for contributing. Read them before anything else.

| Document | Why first |
|---|---|
| [`GOVERNANCE.md`](GOVERNANCE.md) | Defines who owns decisions and what authority structure governs this project |
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | Defines what contributions are in scope, how to submit them, and what is explicitly out of scope |

If you disagree with the scope or constraints in CONTRIBUTING.md, raise that as a scoped issue before proceeding. Do not work around the scope boundary.

---

## The Architecture in Five Minutes

The framework is built on one premise: **governance must precede capability**. An AI agent may not act until its authority, boundaries, monitoring, and accountability are defined and in place.

The architecture is structured in layers:

```
┌───────────────────────────────────────────────────────┐
│  GOVERNANCE LAYER                                      │
│  Who is accountable? What is the authority structure?  │
│  → Governance-Authority-Charter                        │
│  → Minimal-Viable-Governance-Kernel                    │
│  → Roles-And-Responsibilities                          │
└───────────────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────┐
│  BOUNDARY LAYER                                        │
│  What are agents permitted to do?                      │
│  → Agentic-Operational-Boundary                        │
│  → Agent-Baseline-Profile                              │
│  → System-Prompt-Governance-Layer                      │
│  → Capability-Change-Gate                              │
└───────────────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────┐
│  DETECTION LAYER                                       │
│  How do we know when something is wrong?               │
│  → Monitoring-And-Detection-Operations                 │
│  → Threat-Intelligence-Intake                          │
│  → Log-Integrity-And-Tamper-Evidence-Policy            │
│  → Audit-And-Accountability                            │
└───────────────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────┐
│  RESPONSE LAYER                                        │
│  What happens when something goes wrong?               │
│  → Active-Neutralization-Runbook                       │
│  → Agent-Attribution-Playbook                          │
│  → Incident-Response-Policy                            │
│  → Stop-State-Policy                                   │
└───────────────────────────────────────────────────────┘
┌───────────────────────────────────────────────────────┐
│  COMPLIANCE & EXTERNAL LAYER                           │
│  How does this relate to law and standards?            │
│  → GDPR-And-EU-AI-Act-Alignment                        │
│  → Provider-And-Platform-Constraints                   │
│  → Governance-Maturity-Model                           │
└───────────────────────────────────────────────────────┘
```

---

## Suggested Reading Paths

Depending on your background and review focus, start with one of these paths. Each path is designed to give you a coherent picture in a defined reading sequence.

### Path A: Governance and Authority (30 min)
*Best for: policy reviewers, legal reviewers, compliance assessors*

1. `Minimal-Viable-Governance-Kernel` — the irreducible minimum the framework requires
2. `Governance-Authority-Charter` — who has what authority
3. `Roles-And-Responsibilities` — named roles and their accountability
4. `Agentic-Operational-Boundary` — what agents are and are not permitted to do
5. `GDPR-And-EU-AI-Act-Alignment` — regulatory positioning
6. `Governance-Maturity-Model` — honest current-state assessment

### Path B: Security Controls and Detection (30 min)
*Best for: security engineers, red team reviewers, threat modellers*

1. `Agentic-Operational-Boundary` — the boundary being defended
2. `Agent-Baseline-Profile` — what normal agent behaviour looks like
3. `Monitoring-And-Detection-Operations` — detection rules and architecture
4. `Active-Neutralization-Runbook` — response to detected violations
5. `Agent-Attribution-Playbook` — tracing violations to source
6. `Threat-Intelligence-Intake` — how external threats reach the detection engine

### Path C: Prototype Readiness (30 min)
*Best for: technical reviewers assessing implementation readiness*

1. `Prototype-Design-Readiness-Checklist` — the gate before implementation
2. `Provider-And-Platform-Constraints` — what providers permit
3. `Capability-Change-Gate` — how new capabilities are assessed
4. `System-Prompt-Governance-Layer` — how agent instructions are governed
5. `Network-Segmentation-Architecture` — infrastructure boundary
6. `Private-AI-Deployment-Guide` — deployment constraints

### Path D: Review History and Current State (20 min)
*Best for: reviewers who want to understand what has already been challenged and changed*

1. `Post-Review-Revision-Log` — every accepted change and its source
2. `Internal-Consistency-Review` (GFSA-REV-010) — the most recent structured review
3. `Red-Team-Findings` — what adversarial review found
4. `Governance-Maturity-Model` Section 4 — honest current-state placement

---

## How to Submit a Finding

Keep findings narrow and document-specific. One issue per document section is more useful than one issue covering multiple documents.

**Step 1: Identify the type of finding**

| Finding Type | Example |
|---|---|
| Contradiction | Document A says X; Document B says Y on the same point |
| Scope gap | A governance domain exists with no controlling document |
| Unsupported claim | A claim is made without a basis in the framework |
| Ambiguous term | A term is used inconsistently across documents |
| Missing accountability | A process has no named owner or escalation path |
| Overclaim | The framework claims more than the evidence supports |
| Blocking issue | A gap that must be resolved before external review can conclude |

**Step 2: Format your finding**

```
Document:       [Document name and version]
Section:        [Section number]
Finding type:   [Type from table above]
Description:    [One paragraph: what is wrong and why it matters]
Suggested fix:  [Optional: what would resolve it]
```

**Step 3: Submit**

- Open a GitHub Issue using the format above, or
- Prepare a pull request with a narrow change and the same format in the PR description
- Reference the document ID and section in the issue or PR title

Do not combine unrelated findings in a single issue. Do not propose implementation changes.

---

## What Happens to Your Finding

1. The maintainer assesses the finding and assigns a feedback ID (e.g. GFSA-REV-011-F1)
2. If accepted: the change is made and recorded in `Post-Review-Revision-Log`
3. If rejected: the reason is documented in the issue or PR
4. If deferred: the finding is tracked as an open item with a stated condition for resolution

Your contribution, if accepted, is attributed to your reviewer role or anonymised reviewer ID per the privacy policy in CONTRIBUTING.md.

---

## What Makes a Strong Finding

- **Specific:** Points to a document, section, and the exact text in question
- **Falsifiable:** Describes a verifiable gap or contradiction, not a preference
- **Scoped:** Addresses one issue in one place, not a systemic redesign
- **Governance-focused:** Challenges the governance structure, not the implementation approach
- **Conservative:** Suggests narrowing, clarifying, or strengthening — not expanding

The most valuable review findings are the ones that identify something the framework is claiming it cannot yet support.

---

## Frequently Asked Questions

**Q: Do I need to read all 60+ documents before contributing?**
No. Choose a reading path above that matches your focus. You can submit a meaningful finding after reading 5–6 documents if your finding is well-scoped.

**Q: Can I propose new documents or new governance domains?**
Yes, as an issue. Propose it as a scope gap finding with a rationale. The maintainer will assess whether it falls within the current architecture scope.

**Q: Can I submit implementation code?**
No. Implementation code is explicitly out of scope per CONTRIBUTING.md. The framework is documentation-only at this stage.

**Q: What if I think the entire architecture has a fundamental flaw?**
Raise it as a scoped blocking issue. Identify the specific claim or structural assumption you believe is unsupportable. The framework cannot improve from general criticism but can improve from specific, traceable findings.

**Q: Who decides what gets merged?**
The canonical maintainer (Martin Dahl), per GOVERNANCE.md. External reviewers do not have merge authority.

**Q: Is this framework ready for production use?**
No. Current maturity is 2.7/4.0 on the Governance Maturity Model. The targeted external review of the prototype boundary is complete (PDG-028 passed with conditions, GFSA-REV-012), and the Phase 1 and Phase 2 synthetic simulator has been executed and accepted (GFSA-REV-013, -014). Further implementation (Phase 3) requires a new documented owner decision.

---

## Current Package Status at a Glance

| Dimension | Status |
|---|---|
| Package status | `FROZEN_FOR_EXTERNAL_REVIEW` |
| Overall maturity | 2.7 / 4.0 (Governance Maturity Model) |
| Implementation authorised | No |
| Prototype gate | PDG-028 passed with conditions (2026-09-27); Phase 3 requires a new owner decision |
| Open SWOT gaps | 0 (all gaps from GFSA-REV-010 resolved as of this version) |
| Last structured review | GFSA-REV-014 (2026-09-27) |
| External reviews completed | 2 (GFSA-REV-009; GFSA-REV-012, Sami) |

---

*This guide is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
