"""
governance_simulator.py
=======================
Synthetic governance decision simulator — Phase 1 + Phase 2
(bounded defect remediation under GFSA-REV-016: issues #3, #4, #5, #8, #10).

Requires: Python 3.10+. Standard library only (no external dependencies).

SIMULATED_DECISION_ONLY: This is a synthetic simulated governance decision only.
It is not a real approval, security control, compliance finding, legal finding,
production decision, or deployment recommendation.
"""

from __future__ import annotations

import datetime
import pathlib
import platform
import socket
import sys
from typing import Any

BASE_DIR = pathlib.Path(__file__).resolve().parent
TEST_CASE_FILE = BASE_DIR / "synthetic_test_cases.yaml"
OUTPUT_DIR = BASE_DIR / "output"
MOCK_AUDIT_DIR = OUTPUT_DIR / "mock_audit_records"
TEST_RESULTS_DIR = OUTPUT_DIR / "test_results"
GATE_LOG_FILE = OUTPUT_DIR / "no_network_gate_log.txt"

BOUNDARY_REMINDER = (
    "This is a synthetic simulated governance decision only. "
    "It is not a real approval, security control, compliance finding, "
    "legal finding, production decision, or deployment recommendation."
)
SIMULATED_LABEL = "SIMULATED_DECISION_ONLY"
MOCK_AUDIT_LABEL = "MOCK_AUDIT_RECORD"

# Canonical stop states per Stop-State-Registry-v0.1 (reconciled under GFSA-REV-016).
INCIDENT_STOP_STATES = {
    "INCIDENT_REVIEW_REQUIRED",
    "INCIDENT_FREEZE",
    "INCIDENT_ISOLATION",
    "STOP_LATERAL_PEER_COORDINATION",
    "STOP_CAPABILITY_OVERRIDE",
    "STOP_COMPOUND_HOSTILE_SIGNAL",
    "STOP_AGENT_IDENTITY_MISMATCH",
    "STOP_EMERGENT_SWARM_BEHAVIOUR",
}

LOCKDOWN_STOP_STATES = {
    "LOCKDOWN_REQUIRED",
}

# STOP_UNKNOWN is intentionally excluded from HOSTILE_STOP_STATES:
# Stop-State-Registry-v0.1 maps STOP_UNKNOWN -> REVIEW_REQUIRED.
HOSTILE_STOP_STATES = (
    INCIDENT_STOP_STATES
    | LOCKDOWN_STOP_STATES
    | {
        "STOP_SECRET_EXPORT",
        "STOP_SENSITIVE_DATA_EXPORT",
        "STOP_BULK_EXPORT",
        "STOP_EGRESS_UNAUTHORIZED",
        "STOP_AUTHORITY_MISSING",
        "STOP_AUTHORITY_EXPIRED",
        "STOP_MODE_BOUNDARY",
        "STOP_ESCALATION_NOT_APPROVED",
        "STOP_AI_SELF_ESCALATION",
        "STOP_AI_AUTHORITY_EXCEEDED",
        "STOP_AGENT_AUTHORITY_CHAIN_BROKEN",
        "STOP_UNSANCTIONED_INTER_AGENT_COMMUNICATION",
        "STOP_AUDIT_RECORD_MISSING",
        "STOP_ACCOUNTABILITY_MISSING",
    }
)

HOSTILE_ACTION_CLASSES = {"EXPORT", "DELETE", "OVERRIDE"}

# Canonical modes per Mode-Model-Normalization-v0.1.
# LM-5_CONTROLLED_PILOT and LM-6_PRODUCTION are out of scope and intentionally excluded.
KNOWN_LIFECYCLE_MODES = {
    "LM-0_DOCUMENTATION_ONLY",
    "LM-1_REVIEW_PACKAGE",
    "LM-2_PROTOTYPE_DESIGN",
    "LM-3_LIMITED_SYNTHETIC_PROTOTYPE",
    "LM-4_VALIDATED_RESEARCH_PROTOTYPE",
}

KNOWN_OPERATIONAL_MODES = {
    "ODM-0_READ_ONLY",
    "ODM-1_PLAN_ONLY",
    "ODM-2_REVIEW_ONLY",
    "ODM-3_APPROVED_DOCUMENTATION_CHANGE",
    "ODM-4_APPROVED_PROTOTYPE_DESIGN",
    "ODM-5_APPROVED_SYNTHETIC_PROTOTYPE_ACTION",
    "ODM-6_LOCKDOWN",
    "ODM-7_INCIDENT",
}

VALID_DECISIONS = {
    "ALLOW",
    "ALLOW_WITH_CONDITIONS",
    "NEEDS_MORE_EVIDENCE",
    "NEEDS_AUTHORITY",
    "REVIEW_REQUIRED",
    "NEEDS_CAPABILITY_REVIEW",
    "BLOCK",
    "QUARANTINE",
    "LOCKDOWN",
    "INCIDENT_RESPONSE",
}


class NetworkAccessBlockedError(RuntimeError):
    """Raised when any code attempts socket creation while NO_NETWORK_GATE is active."""


class _BlockedSocket:
    """In-process socket guard replacing socket.socket during simulator execution."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        raise NetworkAccessBlockedError(
            "Outbound network access is blocked by NO_NETWORK_GATE."
        )


def _blocked_create_connection(*args: Any, **kwargs: Any) -> None:
    raise NetworkAccessBlockedError(
        "Outbound network connection is blocked by NO_NETWORK_GATE."
    )


_GUARD_INSTALLED = False


def _utc_now_iso() -> str:
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def check_no_network_gate(write_log: bool = True) -> bool:
    """Install and self-test the deterministic in-process socket guard.

    Replaces the earlier environment-dependent non-blocking connect_ex probe
    (issue #3). Independent host/sandbox isolation remains an external pre-run
    verification procedure per Prototype-Boundary-Definition-v0.1 (PDG-028 1b).
    """
    global _GUARD_INSTALLED

    if not _GUARD_INSTALLED:
        socket.socket = _BlockedSocket  # type: ignore[misc]
        socket.create_connection = _blocked_create_connection  # type: ignore[assignment]
        _GUARD_INSTALLED = True

    socket_blocked = False
    connect_blocked = False

    try:
        socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except NetworkAccessBlockedError:
        socket_blocked = True

    try:
        socket.create_connection(("192.0.2.1", 80), timeout=0.1)
    except NetworkAccessBlockedError:
        connect_blocked = True

    passed = socket_blocked and connect_blocked

    if write_log:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        log_lines = [
            f"label: {SIMULATED_LABEL}",
            f"timestamp_utc: {_utc_now_iso()}",
            f"gate_result: {'PASS' if passed else 'FAIL'}",
            "method: in_process_socket_guard_with_self_test",
            f"socket_ctor_blocked: {socket_blocked}",
            f"create_connection_blocked: {connect_blocked}",
            f"python_version: {platform.python_version()}",
            f"platform: {platform.platform()}",
            (
                "boundary_note: Deterministic in-process socket guard prevents simulator "
                "network calls independent of OS socket timing semantics. It is not a live "
                "host firewall; external host/sandbox network isolation remains a pre-run "
                "verification procedure under Prototype-Boundary-Definition-v0.1."
            ),
        ]
        GATE_LOG_FILE.write_text("\n".join(log_lines) + "\n", encoding="utf-8")

    return passed


def no_network_gate() -> None:
    """Mandatory pre-run NO_NETWORK gate. Halts non-zero if guard verification fails."""
    ts = _utc_now_iso()
    if not check_no_network_gate(write_log=True):
        print(f"[{ts}] NO_NETWORK GATE FAILED: In-process network guard could not be verified.")
        print("This simulator must run offline. Halting.")
        sys.exit(1)
    print(
        f"[{ts}] NO_NETWORK GATE: PASS — "
        "In-process socket guard active and verified (no outbound network permitted)."
    )


def _unquote_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and (
        (value[0] == '"' and value[-1] == '"')
        or (value[0] == "'" and value[-1] == "'")
    ):
        return value[1:-1]
    return value


def load_test_cases(yaml_path: pathlib.Path = TEST_CASE_FILE) -> list[dict[str, str]]:
    """Load synthetic_test_cases.yaml using Python stdlib only (issue #4).

    Supports the bounded schema of synthetic_test_cases.yaml:
    top-level `test_cases:` list of flat key-value mappings with single-line
    scalars, quoted strings, and folded block scalars (`>-`).
    """
    if not yaml_path.exists():
        raise FileNotFoundError(f"Test case file not found: {yaml_path}")

    cases: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    in_test_cases = False
    block_key: str | None = None
    block_indent: int = 0
    block_lines: list[str] = []

    def flush_block() -> None:
        nonlocal block_key, block_lines
        if current is not None and block_key is not None:
            current[block_key] = " ".join(part.strip() for part in block_lines if part.strip())
        block_key = None
        block_lines = []

    for raw_line in yaml_path.read_text(encoding="utf-8").splitlines():
        stripped = raw_line.strip()

        if block_key is not None:
            indent = len(raw_line) - len(raw_line.lstrip(" "))
            if stripped == "":
                continue
            if indent > block_indent:
                block_lines.append(stripped)
                continue
            flush_block()

        if not stripped or stripped.startswith("#"):
            continue

        if stripped == "test_cases:":
            in_test_cases = True
            continue

        if not in_test_cases:
            continue

        indent = len(raw_line) - len(raw_line.lstrip(" "))
        if stripped.startswith("- "):
            if current is not None:
                cases.append(current)
            current = {}
            entry = stripped[2:].strip()
            key, sep, val = entry.partition(":")
            if not sep:
                raise ValueError(f"Invalid list entry in {yaml_path}: {raw_line}")
            key = key.strip()
            val = val.strip()
            if val in (">-", ">", "|-", "|"):
                block_key = key
                block_indent = indent + 2
                block_lines = []
            else:
                current[key] = _unquote_yaml_scalar(val)
        elif current is not None:
            key, sep, val = stripped.partition(":")
            if not sep:
                raise ValueError(f"Invalid field line in {yaml_path}: {raw_line}")
            key = key.strip()
            val = val.strip()
            if val in (">-", ">", "|-", "|"):
                block_key = key
                block_indent = indent
                block_lines = []
            else:
                current[key] = _unquote_yaml_scalar(val)

    flush_block()
    if current is not None:
        cases.append(current)

    return cases


def normalize(tc: dict[str, Any]) -> dict[str, Any]:
    """GovernanceInputNormalizer: validate modes against Mode-Model-Normalization-v0.1.

    Per Prototype-Design-Sketch-v0.1 and Stop-State-Registry-v0.1, unknown modes
    always populate STOP_UNKNOWN in stop_state (never a decision value).
    """
    out = dict(tc)
    if out.get("lifecycle_mode") not in KNOWN_LIFECYCLE_MODES:
        out["lifecycle_mode"] = "UNKNOWN"
        out["stop_state"] = "STOP_UNKNOWN"
    if out.get("operational_decision_mode") not in KNOWN_OPERATIONAL_MODES:
        out["operational_decision_mode"] = "UNKNOWN"
        out["stop_state"] = "STOP_UNKNOWN"
    return out


def detect(tc: dict[str, Any]) -> tuple[bool, str, str, str]:
    """HostileSignalDetector: runs before rule evaluation."""
    s = tc.get("stop_state", "")
    ac = tc.get("action_class", "")
    rl = tc.get("risk_level", "")
    au = tc.get("authority_outcome", "")
    eg = tc.get("egress_class", "")
    lp = tc.get("lateral_peer_signal", "")

    # 1. Explicit CA-06 lateral peer coordination signal or named incident stop state
    if lp == "DETECTED" and not s:
        return True, "STOP_LATERAL_PEER_COORDINATION", "INCIDENT_RESPONSE", "CA-06 lateral peer coordination signal detected."
    if s in INCIDENT_STOP_STATES:
        return True, s, "INCIDENT_RESPONSE", f"Incident stop state triggered: {s}."

    # 2. Named lockdown stop state (Stop-State-Registry-v0.1: LOCKDOWN_REQUIRED -> LOCKDOWN)
    if s in LOCKDOWN_STOP_STATES:
        return True, s, "LOCKDOWN", f"Lockdown stop state triggered: {s}."

    # 3. Compound hostile signal (3+ simultaneous indicators) — checked BEFORE
    #    individual stop-state so STOP_SECRET_EXPORT + EXPORT + CRITICAL + SECRET
    #    escalates to STOP_COMPOUND_HOSTILE_SIGNAL / INCIDENT_RESPONSE (STC-001 & STC-009).
    hc = sum(
        [
            s in HOSTILE_STOP_STATES,
            ac in HOSTILE_ACTION_CLASSES,
            rl == "CRITICAL",
            eg == "SECRET",
        ]
    )
    if hc >= 3:
        return (
            True,
            "STOP_COMPOUND_HOSTILE_SIGNAL",
            "INCIDENT_RESPONSE",
            f"Compound hostile signal detected ({hc} simultaneous indicators).",
        )

    # 4. Individual hostile stop state (e.g., standalone STOP_SECRET_EXPORT -> BLOCK)
    if s in HOSTILE_STOP_STATES:
        return True, s, "BLOCK", f"Hostile stop state triggered: {s}."

    # 5–7. Hostile action / critical risk / secret egress without authority
    if ac in HOSTILE_ACTION_CLASSES and au == "NOT_AUTHORIZED":
        return True, "STOP_AUTHORITY_MISSING", "BLOCK", f"Unauthorized hostile action class: {ac}."
    if rl == "CRITICAL" and au == "NOT_AUTHORIZED":
        return True, "STOP_AUTHORITY_MISSING", "BLOCK", "Critical-risk action without authority."
    if eg == "SECRET" and au == "NOT_AUTHORIZED":
        return True, "STOP_SECRET_EXPORT", "BLOCK", "Secret egress attempted without authority."

    return False, "", "", ""


def evaluate(tc: dict[str, Any]) -> tuple[str, str, str]:
    """RuleEvaluationLayer: applies canonical governance rules in priority order."""
    s = tc.get("stop_state", "")
    au = tc.get("authority_outcome", "")
    ev = tc.get("evidence_outcome", "")
    eg = tc.get("egress_class", "")
    mo = tc.get("lifecycle_mode", "")
    op = tc.get("operational_decision_mode", "")
    ca = tc.get("capability_outcome", "")
    ad = tc.get("audit_outcome", "")
    ai = tc.get("ai_human_boundary", "")
    rb = tc.get("rollback_outcome", "")
    ri = tc.get("risk_level", "")

    if s in INCIDENT_STOP_STATES:
        return "INCIDENT_RESPONSE", s, "Active incident."
    if s in LOCKDOWN_STOP_STATES:
        return "LOCKDOWN", s, "Lockdown active."
    if eg in ("SECRET", "PROHIBITED") and au == "NOT_AUTHORIZED":
        return "BLOCK", "STOP_SECRET_EXPORT", "Prohibited egress without authority."
    if au == "NOT_AUTHORIZED":
        return "NEEDS_AUTHORITY", "STOP_AUTHORITY_MISSING", "No authority."
    if s == "STOP_UNKNOWN" or mo == "UNKNOWN" or op == "UNKNOWN":
        return "REVIEW_REQUIRED", "STOP_UNKNOWN", "Unknown mode or classification — safe stop for review."
    if ca == "CAPABILITY_CHANGE_REQUIRED":
        return "NEEDS_CAPABILITY_REVIEW", "STOP_CAPABILITY_CHANGE", "Capability review needed."
    if ad == "AUDIT_RECORD_MISSING":
        return "BLOCK", "STOP_AUDIT_RECORD_MISSING", "Audit record missing."
    if ev == "EVIDENCE_INSUFFICIENT":
        return "NEEDS_MORE_EVIDENCE", "STOP_EVIDENCE_INSUFFICIENT", "Evidence insufficient."
    if ai == "AI_OUTSIDE_ROLE":
        return "BLOCK", "STOP_AI_AUTHORITY_EXCEEDED", "AI outside defined role."
    if rb == "RECOVERY_REQUIRED":
        return "REVIEW_REQUIRED", "REVIEW_REQUIRED_RECOVERY", "Recovery required."
    if ri in ("HIGH", "CRITICAL"):
        return "ALLOW_WITH_CONDITIONS", "", f"Risk level {ri} — conditions apply."
    return "ALLOW", "", "All checks passed."


def build_mock_audit_record(
    tc: dict[str, Any],
    decision: str,
    stop_state: str,
    reason: str,
) -> dict[str, Any]:
    """MockAuditRecordBuilder: builds a labeled MOCK_AUDIT_RECORD."""
    return {
        "mock_audit_label": MOCK_AUDIT_LABEL,
        "decision_label": SIMULATED_LABEL,
        "timestamp_utc": _utc_now_iso(),
        "test_id": tc.get("test_id", ""),
        "phase": tc.get("phase", ""),
        "lifecycle_mode": tc.get("lifecycle_mode", ""),
        "operational_decision_mode": tc.get("operational_decision_mode", ""),
        "actor_role": tc.get("actor_role", ""),
        "asset_category": tc.get("asset_category", ""),
        "action_class": tc.get("action_class", ""),
        "risk_level": tc.get("risk_level", ""),
        "egress_class": tc.get("egress_class", ""),
        "simulated_decision": decision,
        "triggered_stop_state": stop_state,
        "decision_reason": reason,
        "expected_reviewer": tc.get("expected_reviewer", ""),
        "boundary_reminder": BOUNDARY_REMINDER,
    }


def build_test_result(
    tc: dict[str, Any],
    decision: str,
    stop_state: str,
    reason: str,
) -> dict[str, Any]:
    """TestResultReporter: compares expected vs actual decision and stop state."""
    expected_decision = tc.get("expected_decision", "")
    expected_stop = tc.get("expected_stop_state")
    decision_ok = decision == expected_decision
    stop_ok = True if expected_stop is None else (stop_state == expected_stop)
    passed = decision_ok and stop_ok

    mismatch_parts: list[str] = []
    if not decision_ok:
        mismatch_parts.append(f"decision expected={expected_decision} got={decision}")
    if not stop_ok:
        mismatch_parts.append(f"stop_state expected={expected_stop} got={stop_state}")

    return {
        "label": SIMULATED_LABEL,
        "test_id": tc.get("test_id", ""),
        "phase": tc.get("phase", ""),
        "expected_decision": expected_decision,
        "simulated_decision": decision,
        "expected_stop_state": expected_stop if expected_stop is not None else "",
        "triggered_stop_state": stop_state,
        "decision_reason": reason,
        "test_result": "PASS" if passed else "FAIL",
        "mismatch_reason": "; ".join(mismatch_parts),
        "boundary_reminder": BOUNDARY_REMINDER,
    }


def run(tc: dict[str, Any]) -> dict[str, Any]:
    """DecisionResolver (compact dict interface)."""
    n = normalize(tc)
    hostile, stop_state, hostile_decision, reason = detect(n)
    if hostile:
        d = hostile_decision if hostile_decision in VALID_DECISIONS else "REVIEW_REQUIRED"
    else:
        d, stop_state, reason = evaluate(n)
        d = d if d in VALID_DECISIONS else "REVIEW_REQUIRED"

    return {
        "test_id": n.get("test_id", ""),
        "expected": n.get("expected_decision", ""),
        "expected_stop": n.get("expected_stop_state"),
        "got": d,
        "stop": stop_state,
        "reason": reason,
        "phase": n.get("phase", ""),
    }


def run_test_case(tc: dict[str, Any]) -> dict[str, dict[str, Any]]:
    """DecisionResolver (full runner interface returning test_result and mock_audit)."""
    n = normalize(tc)
    r = run(n)
    return {
        "test_result": build_test_result(n, r["got"], r["stop"], r["reason"]),
        "mock_audit": build_mock_audit_record(n, r["got"], r["stop"], r["reason"]),
    }


if __name__ == "__main__":
    no_network_gate()
    cases = load_test_cases()
    print(f"\nLoaded {len(cases)} synthetic test cases from {TEST_CASE_FILE.name}.\n")
    print("-" * 75)

    pass_count = fail_count = 0
    for tc in cases:
        out = run_test_case(tc)["test_result"]
        status = out["test_result"]
        if status == "PASS":
            pass_count += 1
        else:
            fail_count += 1
        stop_str = out["triggered_stop_state"] or "none"
        phase_tag = f"  [{out['phase']}]" if out["phase"] else ""
        print(
            f"[{status}] {out['test_id']:<10}  "
            f"expected={out['expected_decision']:<25}  "
            f"got={out['simulated_decision']:<25}  "
            f"stop={stop_str}{phase_tag}"
        )
        if status == "FAIL":
            print(f"         MISMATCH: {out['mismatch_reason']}")

    print("-" * 75)
    print(f"\nResults: {pass_count} PASS / {fail_count} FAIL out of {len(cases)} test cases.")
    print(f"Phase 2 acceptance criteria met: {pass_count == len(cases) and fail_count == 0}")
    print(f"Gate log written to {GATE_LOG_FILE}")
    print(f"\n[{SIMULATED_LABEL}]")
    print(f"[{BOUNDARY_REMINDER}]")

    if fail_count > 0:
        sys.exit(1)
