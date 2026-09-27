"""Run the Governance Decision Simulator — Phase 1.

Usage:
    python run_simulator.py

Requirements:
    - Python 3.10+
    - No network access
    - No third-party packages
    - synthetic_test_cases.yaml in the same directory

SYNTHETIC SIMULATED GOVERNANCE ONLY.
Not a real security control. Not a real compliance system.
"""

import json
import pathlib
import sys
import datetime

# ---------------------------------------------------------------------------
# Inline YAML parser (standard library only — no PyYAML)
# ---------------------------------------------------------------------------
# For Phase 1 we use a minimal YAML reader that handles the specific
# structure of synthetic_test_cases.yaml. It parses only the fields
# used by the simulator. This avoids any third-party dependency.

def _parse_yaml_test_cases(text: str) -> list[dict]:
    """Minimal YAML parser for the synthetic test cases file.
    Handles block scalars (>) and simple key: value pairs under test_cases.
    """
    lines = text.splitlines()
    cases = []
    current: dict | None = None
    in_test_cases = False
    folded_key: str | None = None
    folded_lines: list[str] = []

    for raw in lines:
        # Strip inline comments
        line = raw.split(" #")[0].rstrip()

        if not in_test_cases:
            if line.strip() == "test_cases:":
                in_test_cases = True
            continue

        # Handle folded scalar continuation
        if folded_key is not None:
            if line.startswith("    ") and line.strip():
                folded_lines.append(line.strip())
                continue
            else:
                if current is not None:
                    current[folded_key] = " ".join(folded_lines)
                folded_key = None
                folded_lines = []

        stripped = line.strip()
        if not stripped:
            continue

        # New test case entry
        if stripped == "- test_id:" or stripped.startswith("- test_id:"):
            if current is not None:
                cases.append(current)
            val = stripped[len("- test_id:"):].strip()
            current = {"test_id": val}
            continue

        if current is None:
            continue

        if ":" in stripped:
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip()
            if val == ">":
                folded_key = key
                folded_lines = []
            else:
                current[key] = val

    # Flush last folded scalar
    if folded_key is not None and current is not None:
        current[folded_key] = " ".join(folded_lines)

    if current is not None:
        cases.append(current)

    return cases


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> None:
    here = pathlib.Path(__file__).parent
    sys.path.insert(0, str(here))

    # Must import after path setup
    from governance_simulator import (
        no_network_gate,
        run_test_case,
        OUTPUT_DIR,
        MOCK_AUDIT_DIR,
        TEST_RESULTS_DIR,
        BOUNDARY_REMINDER,
    )

    # Step 0 — NO_NETWORK GATE (mandatory first step)
    no_network_gate()

    # Ensure output dirs exist
    MOCK_AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    TEST_RESULTS_DIR.mkdir(parents=True, exist_ok=True)

    # Load test cases
    tc_file = here / "synthetic_test_cases.yaml"
    if not tc_file.exists():
        print(f"ERROR: {tc_file} not found.")
        sys.exit(1)

    raw = tc_file.read_text(encoding="utf-8")
    test_cases = _parse_yaml_test_cases(raw)

    if not test_cases:
        print("ERROR: No test cases found in synthetic_test_cases.yaml.")
        sys.exit(1)

    print(f"\nLoaded {len(test_cases)} synthetic test cases.\n")
    print("-" * 60)

    results = []
    passed = 0
    failed = 0

    for tc in test_cases:
        output = run_test_case(tc)
        result = output["test_result"]
        audit = output["mock_audit"]
        results.append(result)

        # Write mock audit record
        audit_path = MOCK_AUDIT_DIR / f"{result['test_id']}_mock_audit.json"
        audit_path.write_text(
            json.dumps(audit, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        # Write test result
        result_path = TEST_RESULTS_DIR / f"{result['test_id']}_result.json"
        result_path.write_text(
            json.dumps(result, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

        # Console output
        status = result["test_result"]
        if status == "PASS":
            passed += 1
        else:
            failed += 1

        print(
            f"[{status}] {result['test_id']:<10} "
            f"expected={result['expected_decision']:<22} "
            f"got={result['simulated_decision']:<22} "
            f"stop={result['triggered_stop_state'] or 'none'}"
        )
        if result["mismatch_reason"]:
            print(f"       MISMATCH: {result['mismatch_reason']}")

    # Summary
    print("-" * 60)
    print(f"\nResults: {passed} PASS / {failed} FAIL out of {len(results)} test cases.")
    print(f"\nMock audit records written to: {MOCK_AUDIT_DIR}")
    print(f"Test results written to:       {TEST_RESULTS_DIR}")
    print(f"\n{BOUNDARY_REMINDER}\n")

    # Write run summary
    summary = {
        "run_timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "total": len(results),
        "passed": passed,
        "failed": failed,
        "label": "SIMULATED_DECISION_ONLY",
        "boundary_reminder": BOUNDARY_REMINDER,
    }
    summary_path = OUTPUT_DIR / "run_summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Run summary written to:        {summary_path}")

    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
