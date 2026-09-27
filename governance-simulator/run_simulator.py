"""Run the Governance Decision Simulator — Phase 2.

SYNTHETIC SIMULATED GOVERNANCE ONLY.
Not a real security control. Not a real compliance system.
Not a production system.

Usage:
    python run_simulator.py

Requires: Python 3.10+. No external dependencies.
"""

import json
import pathlib
import datetime
import sys

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not found. Install with: pip install pyyaml")
    sys.exit(1)

from governance_simulator import (
    no_network_gate,
    run_test_case,
    OUTPUT_DIR,
    MOCK_AUDIT_DIR,
    TEST_RESULTS_DIR,
    BOUNDARY_REMINDER,
    SIMULATED_LABEL,
)

TEST_CASE_FILE = pathlib.Path("synthetic_test_cases.yaml")


def main() -> None:
    # --- Step 0: NO_NETWORK GATE (must run first, must not be bypassed) ---
    no_network_gate()
    print()

    # --- Create output directories ---
    MOCK_AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    TEST_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # --- Load test cases ---
    if not TEST_CASE_FILE.exists():
        print(f"ERROR: Test case file not found: {TEST_CASE_FILE}")
        sys.exit(1)

    with TEST_CASE_FILE.open() as f:
        data = yaml.safe_load(f)

    test_cases = data.get("test_cases", [])
    print(f"Loaded {len(test_cases)} synthetic test cases.")
    print()
    print("-" * 60)

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
        audit_path.write_text(json.dumps(mock_audit, indent=2))

        # Write test result
        result_path = TEST_RESULTS_DIR / f"{test_id}_result.json"
        result_path.write_text(json.dumps(result, indent=2))

        results.append(result)

    print("-" * 60)
    print()
    print(f"Results: {pass_count} PASS / {fail_count} FAIL out of {len(test_cases)} test cases.")
    print()
    print(f"[{SIMULATED_LABEL}]")
    print(f"[{BOUNDARY_REMINDER}]")

    # Write run summary
    summary = {
        "label": SIMULATED_LABEL,
        "run_timestamp": datetime.datetime.utcnow().isoformat() + "Z",
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
    summary_path.write_text(json.dumps(summary, indent=2))
    print(f"Run summary written to {summary_path}")

    if fail_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
