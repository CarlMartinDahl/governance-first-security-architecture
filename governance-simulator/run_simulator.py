"""Run the Governance Decision Simulator — Phase 2.

SYNTHETIC SIMULATED GOVERNANCE ONLY.
Not a real security control. Not a real compliance system.
Not a production system.

Usage:
    python3 run_simulator.py
    # or from repository root:
    python3 governance-simulator/run_simulator.py

Requires: Python 3.10+. Standard library only (no external dependencies).
"""

from __future__ import annotations

import datetime
import json
import sys

from governance_simulator import (
    BOUNDARY_REMINDER,
    GATE_LOG_FILE,
    MOCK_AUDIT_DIR,
    OUTPUT_DIR,
    SIMULATED_LABEL,
    TEST_CASE_FILE,
    TEST_RESULTS_DIR,
    load_test_cases,
    no_network_gate,
    run_test_case,
)


def main() -> None:
    # --- Step 0: NO_NETWORK GATE (must run first, must not be bypassed) ---
    no_network_gate()
    print()

    # --- Create output directories ---
    MOCK_AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    TEST_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # --- Load test cases (stdlib-only loader) ---
    try:
        test_cases = load_test_cases(TEST_CASE_FILE)
    except FileNotFoundError as exc:
        print(f"ERROR: {exc}")
        sys.exit(1)

    print(f"Loaded {len(test_cases)} synthetic test cases from {TEST_CASE_FILE.name}.")
    print()
    print("-" * 75)

    results = []
    pass_count = 0
    fail_count = 0

    for tc in test_cases:
        output = run_test_case(tc)
        result = output["test_result"]
        mock_audit = output["mock_audit"]

        test_id = result["test_id"]
        expected = result["expected_decision"]
        got = result["simulated_decision"]
        stop = result["triggered_stop_state"] or "none"
        phase = result.get("phase", "")
        status = result["test_result"]

        if status == "PASS":
            pass_count += 1
        else:
            fail_count += 1

        phase_tag = f"  [{phase}]" if phase else ""
        print(
            f"[{status}] {test_id:<10}"
            f"  expected={expected:<25}"
            f"  got={got:<25}"
            f"  stop={stop}{phase_tag}"
        )

        if status == "FAIL":
            print(f"        MISMATCH: {result['mismatch_reason']}")

        # Write mock audit record
        audit_path = MOCK_AUDIT_DIR / f"{test_id}_mock_audit.json"
        audit_path.write_text(json.dumps(mock_audit, indent=2) + "\n", encoding="utf-8")

        # Write test result
        result_path = TEST_RESULTS_DIR / f"{test_id}_result.json"
        result_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")

        results.append(result)

    print("-" * 75)
    print()
    print(f"Results: {pass_count} PASS / {fail_count} FAIL out of {len(test_cases)} test cases.")
    print(f"Gate log written to {GATE_LOG_FILE}")
    print()
    print(f"[{SIMULATED_LABEL}]")
    print(f"[{BOUNDARY_REMINDER}]")

    # Write run summary (timezone-aware UTC timestamp)
    summary = {
        "label": SIMULATED_LABEL,
        "run_timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "total": len(test_cases),
        "pass": pass_count,
        "fail": fail_count,
        "phase_2_acceptance_criteria": {
            "required_pass": 15,
            "required_fail": 0,
            "met": pass_count == 15 and fail_count == 0,
        },
        "boundary_reminder": BOUNDARY_REMINDER,
        "results": results,
    }
    summary_path = OUTPUT_DIR / "run_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(f"Run summary written to {summary_path}")

    if fail_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
