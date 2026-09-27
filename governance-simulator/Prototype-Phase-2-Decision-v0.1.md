# Governance-First Security Architecture — Prototype Phase 2 Decision v0.1

## Status

This document is a formal scope and boundary decision for Phase 2 of the
Governance Decision Simulator prototype.

This document does not authorize live implementation, runtime, automation,
live integrations, real data, security claims, or compliance claims.

Phase 2 work may not begin until this document is approved by the project owner
and committed to the repository.

## Decision Date

2026-09-27

## Decision Owner

Martin Dahl (project owner)

## Preconditions

The following conditions must be met before Phase 2 may begin:

- Phase 1 acceptance test: PASSED — 9 PASS / 0 FAIL (GFSA-REV-013, 2026-09-27)
- NO_NETWORK GATE: confirmed passing in Phase 1 run
- Revision Log entry GFSA-REV-013: committed to main branch
- This document: committed to main branch and approved by project owner

## Phase 2 Scope

Phase 2 extends the existing governance-simulator with two bounded additions:

### Addition 1 — Gap O Synthetic Test (CA-06 Lateral Peer Coordination)

Create one or more new synthetic test cases covering the CA-06
lateral peer coordination signal scenario.

Acceptance criteria:
- At least one test case where a lateral peer coordination signal
  triggers INCIDENT_RESPONSE
- At least one test case where the signal is absent and the decision
  passes through correctly (no false positive)
- All test cases pass with expected output
- Gap O status updated in Revision Log from OPEN to
  ANALYTICALLY_ADDRESSED_IN_SIMULATOR

Gap O remains empirically unvalidated until a live or
prototype test against a real detection engine is performed.
This change does not close Gap O — it narrows it.

### Addition 2 — Edge Case Test Expansion

Add synthetic test cases covering scenarios not exercised in Phase 1:

- Conflicting signals (e.g. ALLOW-classified action with a hostile
  signal present simultaneously)
- Unknown asset type (asset not in registry)
- Authority present but policy missing for action type
- Compound signal with no matching stop state

Acceptance criteria:
- Each new test case has a defined expected output
- All new test cases pass
- No regressions in existing STC-001 through STC-009

## Boundary Constraints

The following constraints carry forward unchanged from Phase 1:

- NO_NETWORK: enforced at gate level — simulator must not make
  any network calls
- SYNTHETIC_ONLY: all test data is synthetic — no real project data,
  no real identifiers, no real destinations
- SIMULATED_DECISION_ONLY: all outputs carry this label
- No live integrations
- No real agents
- No runtime authority
- No production deployment

## Acceptance Criteria for Phase 2 Completion

Phase 2 is complete when:

1. All Phase 1 test cases (STC-001 through STC-009) still pass
2. Gap O synthetic test cases pass with expected output
3. All edge case test cases pass with expected output
4. NO_NETWORK GATE passes on final run
5. Revision Log entry GFSA-REV-014 committed documenting
   Phase 2 acceptance test result

## What Phase 2 Does Not Authorize

- Empirical validation of CA-06 against a live detection engine
- Closure of Gap O (narrowed only, not closed)
- Phase 3 or any further prototype extension without a new
  documented decision
- Security validation, compliance validation, or production readiness
- Any claim beyond: synthetic governance decision simulator,
  Phase 2 acceptance test passed

## Revision Log Link

This document will be referenced in GFSA-REV-014 upon Phase 2
acceptance test completion.
