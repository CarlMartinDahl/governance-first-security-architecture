"""Governance Decision Simulator — Phase 1.

SYNTHETIC SIMULATED GOVERNANCE ONLY.
Not a real security control. Not a real compliance system.
Not a production system.
"""

import socket
import datetime
import os
import pathlib

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

BOUNDARY_REMINDER = (
    "This is a synthetic simulated governance decision only. "
    "It is not a real approval, security control, compliance finding, "
    "legal finding, production decision, or deployment recommendation."
)

SIMULATED_LABEL = "SIMULATED_DECISION_ONLY"
MOCK_AUDIT_LABEL = "MOCK_AUDIT_RECORD"

OUTPUT_DIR = pathlib.Path("output")
NO_NETWORK_LOG = OUTPUT_DIR / "no_network_gate_log.txt"
MOCK_AUDIT_DIR = OUTPUT_DIR / "mock_audit_records"
TEST_RESULTS_DIR = OUTPUT_DIR / "test_results"

# Hostile stop states — immediate BLOCK
HOSTILE_STOP_STATES = {
    "STOP_SECRET_EXPORT",
    "STOP_LOCKDOWN",
    "STOP_INCIDENT_ACTIVE",
    "STOP_PROHIBITED_EGRESS",
    "STOP_CAPABILITY_OVERRIDE",
    "STOP_MISSING_AUTHORITY",
    "STOP_UNKNOWN",
    "STOP_AI_BOUNDARY_VIOLATION",
    "STOP_MODE_BOUNDARY_VIOLATION",
}

# Stop states that escalate to INCIDENT_RESPONSE rather than plain BLOCK
INCIDENT_STOP_STATES = {
    "STOP_INCIDENT_ACTIVE",
    "STOP_LOCKDOWN",
}

HOSTILE_ACTION_CLASSES = {"EXPORT", "DELETE", "OVERRIDE"}
SECRET_EGRESS = "SECRET"


# ---------------------------------------------------------------------------
# Section 0 — NO_NETWORK GATE
# ---------------------------------------------------------------------------

def no_network_gate() -> None:
    """Halt execution if any outbound network route is reachable.

    This gate must run before any other logic.
    It must not be bypassed, commented out, or removed.
    """
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.datetime.utcnow().isoformat() + "Z"
    
    detected = False
    try:
        # Attempt a non-blocking connect to an external IP (TEST-NET, RFC 5737)
        # We use 192.0.2.1:80 — a documentation address that must never be routable.
        # If it connects (or we get ECONNREFUSED), a route exists.
        probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        probe.setblocking(False)
        try:
            result = probe.connect_ex(("192.0.2.1", 80))
            # On an offline machine, connect_ex returns ENETUNREACH or similar.
            # EINPROGRESS (115) or 0 indicates a routable interface exists.
            import errno
            routable_codes = {0, errno.EINPROGRESS, errno.EWOULDBLOCK, 10035, 10036}
            if result in routable_codes:
                detected = True
        finally:
            probe.close()
    except OSError:
        # ENETUNREACH or similar — no route, gate passes
        pass

    if detected:
        msg = (
            f"[{timestamp}] NO_NETWORK GATE: FAIL\n"
            "Outbound network access detected. "
            "This simulator must run offline. Halting.\n"
        )
        NO_NETWORK_LOG.write_text(msg)
        print(msg)
        raise SystemExit(1)

    msg = f"[{timestamp}] NO_NETWORK GATE: PASS — Simulator is running offline.\n"
    NO_NETWORK_LOG.write_text(msg)
    print(msg.strip())


# ---------------------------------------------------------------------------
# Section 1 — Hostile Signal Detector
# ---------------------------------------------------------------------------

class HostileSignalDetector:
    """Checks for hostile-action signals BEFORE rule evaluation.

    If a hostile signal is detected, evaluation halts immediately.
    """

    @staticmethod
    def detect(tc: dict) -> tuple[bool, str, str]:
        """Return (hostile, stop_state, decision)."""
        stop_state = tc.get("stop_state", "")
        action_class = tc.get("action_class", "")
        risk_level = tc.get("risk_level", "")
        authority = tc.get("authority_outcome", "")
        egress = tc.get("egress_class", "")

        # Named stop state
        if stop_state in INCIDENT_STOP_STATES:
            return True, stop_state, "INCIDENT_RESPONSE"
        if stop_state in HOSTILE_STOP_STATES:
            return True, stop_state, "BLOCK"

        # Hostile action class
        if action_class in HOSTILE_ACTION_CLASSES and authority == "NOT_AUTHORIZED":
            triggered = "STOP_MISSING_AUTHORITY"
            return True, triggered, "BLOCK"

        # Critical risk + no authority
        if risk_level == "CRITICAL" and authority == "NOT_AUTHORIZED":
            triggered = "STOP_MISSING_AUTHORITY"
            return True, triggered, "BLOCK"

        # Secret egress + no authority
        if egress == SECRET_EGRESS and authority == "NOT_AUTHORIZED":
            triggered = "STOP_SECRET_EXPORT"
            return True, triggered, "BLOCK"

        # Compound hostile signal: multiple stop indicators
        hostile_count = sum([
            stop_state in HOSTILE_STOP_STATES,
            action_class in HOSTILE_ACTION_CLASSES,
            risk_level == "CRITICAL",
            egress == SECRET_EGRESS,
        ])
        if hostile_count >= 3:
            return True, "STOP_COMPOUND_HOSTILE_SIGNAL", "INCIDENT_RESPONSE"

        return False, "", ""


# ---------------------------------------------------------------------------
# Section 2 — Governance Input Normalizer
# ---------------------------------------------------------------------------

KNOWN_LIFECYCLE_MODES = {
    "LM-1_REVIEW_PACKAGE",
    "LM-2_DESIGN",
    "LM-3_PROTOTYPE",
    "LM-4_PRODUCTION",
}

KNOWN_OPERATIONAL_MODES = {
    "ODM-1_READ_ONLY",
    "ODM-2_APPROVED_CHANGE",
    "ODM-3_APPROVED_DOCUMENTATION_CHANGE",
    "ODM-4_EMERGENCY",
}


class GovernanceInputNormalizer:
    @staticmethod
    def normalize(tc: dict) -> dict:
        out = dict(tc)
        if out.get("lifecycle_mode") not in KNOWN_LIFECYCLE_MODES:
            out["lifecycle_mode"] = "UNKNOWN"
            out["stop_state"] = "STOP_UNKNOWN"
        if out.get("operational_decision_mode") not in KNOWN_OPERATIONAL_MODES:
            out["operational_decision_mode"] = "UNKNOWN"
            if out.get("stop_state") != "STOP_UNKNOWN":
                out["stop_state"] = "REVIEW_REQUIRED"
        return out


# ---------------------------------------------------------------------------
# Section 3 — Rule Evaluation Layer
# ---------------------------------------------------------------------------

class RuleEvaluationLayer:
    """Applies governance rules in priority order (most restrictive wins)."""

    def evaluate(self, tc: dict) -> tuple[str, str, str]:
        """Return (decision, stop_state, reason)."""

        stop = tc.get("stop_state", "")
        authority = tc.get("authority_outcome", "")
        evidence = tc.get("evidence_outcome", "")
        egress = tc.get("egress_class", "")
        mode = tc.get("lifecycle_mode", "")
        op_mode = tc.get("operational_decision_mode", "")
        capability = tc.get("capability_outcome", "")
        audit = tc.get("audit_outcome", "")
        ai_boundary = tc.get("ai_human_boundary", "")
        rollback = tc.get("rollback_outcome", "")
        risk = tc.get("risk_level", "")

        # Priority 2 — Incident
        if stop == "STOP_INCIDENT_ACTIVE":
            return "INCIDENT_RESPONSE", stop, "Active incident state detected."

        # Priority 3 — Lockdown
        if stop == "STOP_LOCKDOWN":
            return "LOCKDOWN", stop, "Lockdown state active."

        # Priority 4 — Prohibited egress
        if egress in ("SECRET", "PROHIBITED") and authority == "NOT_AUTHORIZED":
            return "BLOCK", "STOP_SECRET_EXPORT", "Prohibited egress without authority."

        # Priority 5 — Missing authority
        if authority == "NOT_AUTHORIZED":
            return "NEEDS_AUTHORITY", "STOP_MISSING_AUTHORITY", "Authority not granted."

        # Priority 6 — Mode boundary
        if mode == "UNKNOWN" or op_mode == "UNKNOWN":
            return "BLOCK", "STOP_MODE_BOUNDARY_VIOLATION", "Unknown lifecycle or operational mode."

        # Priority 7 — Capability change
        if capability == "CAPABILITY_CHANGE_REQUIRED":
            return "NEEDS_CAPABILITY_REVIEW", "", "Capability change requires review."

        # Priority 8 — Audit failure
        if audit == "AUDIT_RECORD_MISSING":
            return "BLOCK", "", "Audit record missing."

        # Priority 9 — Evidence
        if evidence == "EVIDENCE_INSUFFICIENT":
            return "NEEDS_MORE_EVIDENCE", "", "Evidence insufficient."

        # Priority 10 — AI boundary
        if ai_boundary == "AI_OUTSIDE_ROLE":
            return "REVIEW_REQUIRED", "STOP_AI_BOUNDARY_VIOLATION", "AI acting outside role boundary."

        # Priority 11 — Rollback
        if rollback == "RECOVERY_REQUIRED":
            return "REVIEW_REQUIRED", "", "Recovery required before proceeding."

        # Priority 12 — Risk level
        if risk in ("HIGH", "CRITICAL"):
            return "ALLOW_WITH_CONDITIONS", "", f"Risk level {risk} requires conditional approval."

        return "ALLOW", "", "All checks passed."


# ---------------------------------------------------------------------------
# Section 4 — Decision Resolver
# ---------------------------------------------------------------------------

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


class DecisionResolver:
    @staticmethod
    def resolve(decision: str) -> str:
        if decision not in VALID_DECISIONS:
            return "REVIEW_REQUIRED"
        return decision


# ---------------------------------------------------------------------------
# Section 5 — Mock Audit Record Builder
# ---------------------------------------------------------------------------

class MockAuditRecordBuilder:
    @staticmethod
    def build(
        tc: dict,
        decision: str,
        stop_state: str,
        reason: str,
        reviewer: str,
    ) -> dict:
        return {
            "label": MOCK_AUDIT_LABEL,
            "mock_event_id": f"MOCK-{tc.get('test_id', 'UNKNOWN')}-{datetime.datetime.utcnow().strftime('%Y%m%dT%H%M%SZ')}",
            "test_id": tc.get("test_id", "UNKNOWN"),
            "timestamp_simulated": datetime.datetime.utcnow().isoformat() + "Z",
            "lifecycle_mode": tc.get("lifecycle_mode", ""),
            "operational_decision_mode": tc.get("operational_decision_mode", ""),
            "actor_role": tc.get("actor_role", ""),
            "asset_category": tc.get("asset_category", ""),
            "action_class": tc.get("action_class", ""),
            "risk_level": tc.get("risk_level", ""),
            "authority_outcome": tc.get("authority_outcome", ""),
            "evidence_outcome": tc.get("evidence_outcome", ""),
            "egress_class": tc.get("egress_class", ""),
            "capability_outcome": tc.get("capability_outcome", ""),
            "ai_human_boundary": tc.get("ai_human_boundary", ""),
            "audit_outcome": tc.get("audit_outcome", ""),
            "rollback_outcome": tc.get("rollback_outcome", ""),
            "triggered_stop_state": stop_state,
            "simulated_decision": decision,
            "required_reviewer": reviewer,
            "recovery_required": False,
            "decision_reason": reason,
            "boundary_reminder": BOUNDARY_REMINDER,
        }


# ---------------------------------------------------------------------------
# Section 6 — Test Result Reporter
# ---------------------------------------------------------------------------

class TestResultReporter:
    @staticmethod
    def report(
        tc: dict,
        decision: str,
        stop_state: str,
        reason: str,
        mock_audit: dict,
    ) -> dict:
        expected = tc.get("expected_decision", "")
        passed = decision == expected
        return {
            "label": SIMULATED_LABEL,
            "test_id": tc.get("test_id", ""),
            "expected_decision": expected,
            "simulated_decision": decision,
            "test_result": "PASS" if passed else "FAIL",
            "triggered_stop_state": stop_state,
            "mismatch_reason": "" if passed else f"Expected {expected}, got {decision}. Rule reason: {reason}",
            "required_reviewer": tc.get("expected_reviewer", ""),
            "boundary_reminder": BOUNDARY_REMINDER,
        }


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run_test_case(tc: dict) -> dict:
    """Run a single synthetic test case through the full pipeline."""
    normalizer = GovernanceInputNormalizer()
    detector = HostileSignalDetector()
    rules = RuleEvaluationLayer()
    resolver = DecisionResolver()
    audit_builder = MockAuditRecordBuilder()
    reporter = TestResultReporter()

    # Step 1 — Normalize
    tc_norm = normalizer.normalize(tc)

    # Step 2 — Hostile signal check (hard stop on detection)
    hostile, stop_state, hostile_decision = detector.detect(tc_norm)
    if hostile:
        decision = resolver.resolve(hostile_decision)
        reason = f"Hostile signal detected: {stop_state}"
        reviewer = tc_norm.get("expected_reviewer", "ROLE_SECURITY_REVIEWER")
        mock_audit = audit_builder.build(tc_norm, decision, stop_state, reason, reviewer)
        result = reporter.report(tc_norm, decision, stop_state, reason, mock_audit)
        return {"test_result": result, "mock_audit": mock_audit}

    # Step 3 — Rule evaluation
    decision, stop_state, reason = rules.evaluate(tc_norm)
    decision = resolver.resolve(decision)
    reviewer = tc_norm.get("expected_reviewer", "")
    mock_audit = audit_builder.build(tc_norm, decision, stop_state, reason, reviewer)
    result = reporter.report(tc_norm, decision, stop_state, reason, mock_audit)
    return {"test_result": result, "mock_audit": mock_audit}
