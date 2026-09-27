# Governance-First Security Architecture — Prototype Implementation Plan v0.1

## Status

This document authorizes a first concrete implementation step.

This document is scoped to the boundaries defined in:

- Governance-First-Security-Architecture-Prototype-Design-Sketch-v0.1.md
- Governance-First-Security-Architecture-Prototype-Boundary-Definition-v0.1.md

This document does not override, extend, or replace those boundaries.

This document does not authorize production use.

This document does not authorize real data.

This document does not authorize network access.

This document does not authorize security or compliance claims.

---

## Purpose

This plan describes how to implement the Governance Decision Simulator as a local, offline, synthetic-only Python prototype.

The simulator exists to answer one question:

```text
Given a synthetic governance scenario with hostile-action signals,
what simulated decision should the governance model return — and can it
detect that signal in time to matter?
```

It must not govern real systems.

It must not connect to a network.

It must not process real incidents.

---

## Implementer

```text
Implementer: Martin Dahl
Role: Sole implementer for this prototype phase.
Network-isolation verifier: Must be a second person or an automated pre-run assertion.
```

Because Martin is the sole implementer, the NO_NETWORK gate (see Section 6) must be implemented as an **automated self-check that halts execution** if network access is detected — not as a manual step that the implementer performs and self-approves.

This is required to preserve independence between the implementer and the verifier role.

---

## Why Python

Python is selected for this prototype for the following reasons:

- It supports deterministic rule evaluation with low latency in a local, offline environment.
- Its readable syntax makes the governance logic easy to inspect, challenge, and delete.
- It allows hostile-signal detection to run synchronously within a single process without requiring threads, daemons, or network sockets.
- It has no mandatory build step, which reduces attack surface and accidental scope creep.
- The entire prototype can run from a single directory with no external dependencies beyond the Python standard library.

The prototype must use **Python 3.10 or later**.

The prototype must use **only the Python standard library**.

No third-party packages are permitted in this phase.

---

## Real-Time Hostile Detection — Design Intent

The simulator must be able to detect hostile-action signals within the synthetic test input and return a blocking decision before any downstream step is reached.

For this prototype, "real-time" means:

```text
The hostile-signal check runs before rule evaluation.
If a hostile signal is detected, the simulator halts the evaluation
and returns BLOCK or INCIDENT_RESPONSE immediately.
No further steps are executed.
```

Hostile signals in synthetic inputs include:

- `stop_state` values in the STOP_* family.
- `action_class` values that map to EXPORT, DELETE, or OVERRIDE.
- `risk_level` values of CRITICAL combined with `authority_outcome: NOT_AUTHORIZED`.
- Any combination of `egress_class: SECRET` and missing authority.
- Simultaneous presence of multiple stop states (compound hostile signal).

The hostile-signal check must be the **first gate** in the evaluation pipeline.

If a hostile signal is detected:

1. Execution stops immediately.
2. A MOCK_AUDIT_RECORD is written with `triggered_stop_state` populated.
3. The output is labeled `SIMULATED_DECISION_ONLY`.
4. The simulated decision is returned as `BLOCK` or `INCIDENT_RESPONSE`.
5. No further rule evaluation occurs.

This design means that detection latency equals the time to parse the input and check the hostile-signal table — which for synthetic inputs in Python should be under 10 milliseconds on any modern local machine.

---

## Implementation Scope — Phase 1

Phase 1 is the only phase authorized by this document.

Phase 1 consists of:

1. A single Python module: `governance_simulator.py`
2. A single synthetic test-case file: `synthetic_test_cases.yaml`
3. A single runner script: `run_simulator.py`
4. A single output directory: `output/` — for mock audit records and test result reports only.

Nothing else is authorized in Phase 1.

No database.

No web interface.

No API.

No scheduler.

No daemon.

No external dependency.

---

## File Structure

```text
governance-simulator/
├── governance_simulator.py    # Core logic
├── run_simulator.py           # Entry point
├── synthetic_test_cases.yaml  # Synthetic test inputs
└── output/
    ├── mock_audit_records/    # MOCK_AUDIT_RECORD files
    └── test_results/          # Test result reports
```

All files must fit in one directory.

The directory must be possible to delete in its entirety without consequence to any other system.

---

## Module Responsibilities

### governance_simulator.py

Contains:

- `NO_NETWORK_GATE` — pre-run assertion (see Section 6).
- `HostileSignalDetector` — checks for hostile-action signals before rule evaluation.
- `GovernanceInputNormalizer` — converts raw test-case fields to canonical vocabulary.
- `RuleEvaluationLayer` — applies governance rules in priority order.
- `DecisionResolver` — returns one simulated decision.
- `MockAuditRecordBuilder` — builds a MOCK_AUDIT_RECORD.
- `TestResultReporter` — compares expected vs actual decision.

### run_simulator.py

- Loads `synthetic_test_cases.yaml`.
- Calls `NO_NETWORK_GATE` first.
- Iterates test cases.
- Calls `governance_simulator.py` for each.
- Writes output to `output/`.
- Prints summary to stdout.

### synthetic_test_cases.yaml

- Contains only synthetic test cases.
- Must include at least:
  - Two cases with hostile signals that should return `BLOCK`.
  - Two cases with hostile signals that should return `INCIDENT_RESPONSE`.
  - Two cases that should return `ALLOW`.
  - Two cases with missing authority that should return `NEEDS_AUTHORITY`.
  - One compound hostile signal case.

---

## Section 6 — NO_NETWORK Gate

This is the mandatory first-run gate.

The gate must be implemented as Python code inside `governance_simulator.py`.

The gate must run before any other logic.

The gate must:

1. Attempt to bind a socket to a local port.
2. Confirm that no outbound network socket is reachable.
3. If any outbound network check returns a routable address, halt immediately and exit with a non-zero code and the message:

```text
NO_NETWORK GATE FAILED: Outbound network access detected.
This simulator must run offline. Halting.
```

4. If the gate passes, print:

```text
NO_NETWORK GATE: PASS — Simulator is running offline.
```

The gate must not be bypassed, commented out, or removed.

If the gate is removed or bypassed, the simulator must be considered out of scope and must not be run.

Verification log: Every run must write the gate result to `output/no_network_gate_log.txt` with a timestamp.

---

## Evaluation Priority Order

The evaluation pipeline must follow this order:

```text
0. NO_NETWORK_GATE                   (pre-run, halts on failure)
1. HostileSignalDetector              (halts evaluation on detection)
2. Incident state check
3. Lockdown state check
4. Prohibited egress check
5. Missing authority check
6. Mode boundary violation check
7. Capability change check
8. Audit/accountability failure check
9. Evidence insufficiency check
10. AI-human boundary check
11. Rollback/recovery check
12. Risk-level review requirement
13. Conditional allow
14. Allow
```

Step 0 and Step 1 are hard stops.

All other steps follow the most-restrictive-wins rule.

---

## Output Labels

Every output must include:

```text
label: SIMULATED_DECISION_ONLY
```

Every mock audit record must be labeled:

```text
MOCK_AUDIT_RECORD
```

Neither label may be removed.

Outputs must never be used as:

- real compliance evidence,
- real security validation,
- real production decision,
- real incident record.

---

## Acceptance Criteria for Phase 1

Phase 1 is complete when:

- [ ] The NO_NETWORK gate runs and passes before any logic executes.
- [ ] The NO_NETWORK gate halts execution and exits non-zero if network access is detected.
- [ ] Hostile-signal detection runs before rule evaluation.
- [ ] All hostile-signal test cases return the correct BLOCK or INCIDENT_RESPONSE decision.
- [ ] All ALLOW test cases return the correct ALLOW decision.
- [ ] All mock audit records are labeled MOCK_AUDIT_RECORD.
- [ ] All outputs are labeled SIMULATED_DECISION_ONLY.
- [ ] The test result reporter prints pass/fail for each test case.
- [ ] The entire simulator runs with no network access.
- [ ] The entire simulator runs with no third-party dependencies.
- [ ] The entire simulator can be deleted without consequence to any other system.
- [ ] No real data appears anywhere in inputs or outputs.
- [ ] No real secrets appear anywhere.
- [ ] The `output/no_network_gate_log.txt` file is written on every run.

---

## What This Plan Does Not Authorize

This plan does not authorize:

- production deployment,
- real incident handling,
- real compliance assessment,
- real security claims,
- external API integration,
- database integration,
- web interface,
- real authentication,
- real authorization,
- real DLP enforcement,
- autonomous remediation,
- use of real personal data,
- use of real credentials or secrets,
- any use outside a controlled local development environment.

---

## Boundary Reminder

```text
This is a synthetic simulated governance decision simulator only.
It is not a real security control.
It is not a real compliance system.
It is not a production system.
Outputs are not real approvals, security findings, legal findings,
or deployment recommendations.
```

---

## Document Control

```text
Version:         v0.1
Status:          Active — Phase 1 authorized
Date:            2026-09-27
Implementer:     Martin Dahl
Reviewer:        Pending — second-person review required before Phase 2
Next gate:       Phase 1 Acceptance Criteria review
```
