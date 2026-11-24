# Governance-First Security Architecture — Governance Decision Assessment Worksheet v0.1

## Status

Operational workshop template (commercial discovery).

This worksheet is not a new architecture layer. It operationalizes the existing canonical documents (`Minimal-Viable-Governance-Kernel-v0.1`, `Decision-State-Matrix-v0.1`, `Stop-State-Registry-v0.1`, `Role-Registry-v0.1`, and `Governance-Decision-Assessment-Workshop-Offer-v0.1`) into a single runnable 2–3 hour or 1-day assessment sheet.

It does not authorize software implementation, runtime enforcement, live integration, or security/compliance claims.

---

## Core Assessment Formula

```text
Authority + Evidence + Mode & Risk + Egress + Stop Path + Accountability
before any governed AI-assisted action.
```

Rule: **The most restrictive valid signal wins.** A stop state is a valid governance outcome, not a system failure.

---

## 1. Assessment Scope & Sponsor (Complete Before Session)

| Field | Entry |
| --- | --- |
| Organization / Team (anonymized if shared) | |
| Workshop Format | `[ ] Option A (2–3 hours)` / `[ ] Option B (1 working day)` |
| Single Workflow In Scope | |
| Executive Sponsor / Problem Owner | |
| Participants (Business / Tech / Security / Risk / Legal) | |
| Current Lifecycle Mode (`Mode-Model-Normalization-v0.1`) | `LM-0` / `LM-1` / `LM-2` / `LM-3` / `LM-4` / `LM-5` / `LM-6` |
| Out-Of-Scope Confirmation | No software build, no live integration, no compliance/security certification |

---

## 2. Decision Map & Allow / Block / Escalate / Export / Audit Matrix

Map each decision point in the selected workflow (aim for 5–10 concrete decision steps).

| Step ID | Decision / Action | Action Class (`OBSERVE`, `ANALYZE`, `DOCUMENT`, `RECOMMEND`, `CHANGE`, `EXPORT`, `EXECUTE`, `ESCALATE`, `OVERRIDE`, `RECOVER`) | Risk Level (`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`) | AI Role (`ROLE_AI_ASSISTANT` — recommend/draft only) | Named Human Authority (`ROLE_*` from Role Registry) | Required Evidence | Egress Class (`NO_EGRESS`, `PUBLIC_SAFE`, `INTERNAL_ONLY`, `SENSITIVE`, `SECRET`, `REGULATED`, `BLOCKED`) | Default Decision (`ALLOW`, `ALLOW_WITH_CONDITIONS`, `NEEDS_MORE_EVIDENCE`, `NEEDS_AUTHORITY`, `REVIEW_REQUIRED`, `NEEDS_CAPABILITY_REVIEW`, `BLOCK`, `QUARANTINE`, `LOCKDOWN`, `INCIDENT_RESPONSE`) | Mandatory Audit Record |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| D-01 | | | | | | | | | |
| D-02 | | | | | | | | | |
| D-03 | | | | | | | | | |
| D-04 | | | | | | | | | |
| D-05 | | | | | | | | | |

---

## 3. Six-Gate Kernel Check (Per High-Risk Or Sensitive Decision)

Check each critical step against the six required kernel gates (`Minimal-Viable-Governance-Kernel-v0.1`):

| Gate | Assessment Question | Current State (`PASS` / `PARTIAL` / `GAP`) | Evidence / Gap Notes |
| --- | --- | --- | --- |
| **1. Authority** | Is a named human `ROLE_*` assigned with explicit approval scope, expiration, and separation of duties (requester ≠ approver; AI never self-approves)? | | |
| **2. Evidence** | Are source authority, freshness/staleness limits, and counter-evidence rules defined before action? | | |
| **3. Mode & Risk** | Does the workflow enforce explicit operating modes (`READ_ONLY`, `PLAN_ONLY`, `REVIEW_ONLY`, `APPROVED_ACTION`, `LOCKDOWN`, `INCIDENT`) and fail closed on unknown mode? | | |
| **4. Egress** | Is external/tool/API output classified separately from internal access? Are `SECRET` and `REGULATED` exports blocked by default? | | |
| **5. Stop Path** | Are canonical stop states defined with clear trigger, required reviewer, and containment path (`Stop-State-Registry-v0.1`)? | | |
| **6. Audit & Rollback** | Is every decision, override, and stop state recorded in an immutable audit trail with a verified rollback/recovery path? | | |

---

## 4. Canonical Quick Reference

### Canonical Roles (`Role-Registry-v0.1`)
- `ROLE_USER_REQUESTER` — submits requests; may approve low-risk documentation only.
- `ROLE_SYSTEM_OWNER` — owns system scope, continuity sign-off, and scoped risk acceptance.
- `ROLE_APPROVER` — holds scoped human approval authority (distinct from requester for high-risk actions).
- `ROLE_GOVERNANCE_REVIEWER` — owns governance process integrity and stop-state review.
- `ROLE_SECURITY_REVIEWER` — reviews security, egress, secrets, and capability-change impact.
- `ROLE_TECHNICAL_REVIEWER` — reviews technical feasibility, architecture, and rollback readiness.
- `ROLE_LEGAL_COMPLIANCE_REVIEWER` — reviews legal/regulatory language and transfer obligations.
- `ROLE_PRIVACY_REVIEWER` — reviews personal-data handling and GDPR boundaries.
- `ROLE_AI_GOVERNANCE_REVIEWER` — reviews AI autonomy, role boundaries, and multi-agent risks.
- `ROLE_INCIDENT_REVIEWER` — holds containment, isolation, and recovery-verification authority.
- `ROLE_AI_ASSISTANT` — assistive only; **never approves**, never self-escalates.

### Key Canonical Stop States (`Stop-State-Registry-v0.1`)
| Stop State | Default Decision | Typical Trigger |
| --- | --- | --- |
| `STOP_AUTHORITY_MISSING` | `BLOCK` | Required human authority absent or unverified |
| `STOP_EVIDENCE_INSUFFICIENT` / `STOP_SOURCE_STALE` | `NEEDS_MORE_EVIDENCE` / `REVIEW_REQUIRED` | Missing, stale, or conflicting basis for decision |
| `STOP_MODE_BOUNDARY` | `BLOCK` | Action disallowed in current lifecycle/operational mode |
| `STOP_SECRET_EXPORT` | `BLOCK` (`INCIDENT_RESPONSE` on 3+ compound hostile signals) | Secret, key, or token may leave boundary |
| `STOP_SENSITIVE_DATA_EXPORT` / `STOP_EGRESS_UNAUTHORIZED` | `BLOCK` | Unapproved personal/restricted data or external exit |
| `STOP_CAPABILITY_CHANGE` / `STOP_HIDDEN_CAPABILITY` | `NEEDS_CAPABILITY_REVIEW` | New tool, permission, or scope expansion introduced |
| `STOP_AI_AUTHORITY_EXCEEDED` / `STOP_AI_SELF_ESCALATION` | `BLOCK` | AI acts outside role or attempts to expand authority |
| `STOP_LATERAL_PEER_COORDINATION` | `INCIDENT_RESPONSE` | Unsanctioned cross-agent lateral coordination (CA-06) |
| `STOP_UNKNOWN` | `REVIEW_REQUIRED` | Classification, mode, or authority cannot be determined |
| `LOCKDOWN_REQUIRED` | `LOCKDOWN` | Broad containment required pending return-to-normal review |
| `INCIDENT_REVIEW_REQUIRED` | `INCIDENT_RESPONSE` | Potential security, data, or governance incident |

---

## 5. Stop-State Gap List & Do-Not-Automate Register

### Stop-State Gaps Identified
| Gap ID | Workflow Step | Missing Or Weak Stop Condition | Target Canonical Stop State | Named Owner | Target Resolution |
| --- | --- | --- | --- | --- | --- |
| GAP-01 | | | | | |
| GAP-02 | | | | | |
| GAP-03 | | | | | |

### Explicit Do-Not-Automate List
Actions in this workflow that must **remain human-decided** (four-eyes where high/critical risk) and must not be delegated to autonomous AI execution:

1. `___________________________________________________________________` (Rationale: `____________________`)
2. `___________________________________________________________________` (Rationale: `____________________`)
3. `___________________________________________________________________` (Rationale: `____________________`)

---

## 6. Prioritized Next Safe Actions (Workshop Output Summary)

| Priority | Action | Owner (`ROLE_*` / Named Person) | Dependency / Blocker | Verification Evidence |
| --- | --- | --- | --- | --- |
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

---

## Boundary Reminder

```text
This worksheet is a structured governance assessment and review aid only.
Completion of this worksheet does not constitute legal advice, regulatory
compliance, GDPR/EU AI Act certification, security validation, or authorization
for production AI deployment or runtime automation.
```
