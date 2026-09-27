"""
governance_simulator.py
=======================
Synthetic governance decision simulator — Phase 1 + Phase 2.

SIMULATED_DECISION_ONLY: This is a synthetic simulated governance decision only.
It is not a real approval, security control, compliance finding, legal finding,
production decision, or deployment recommendation.
"""

import socket, errno, datetime

BOUNDARY_REMINDER = (
    "This is a synthetic simulated governance decision only. "
    "It is not a real approval, security control, compliance finding, "
    "legal finding, production decision, or deployment recommendation."
)
SIMULATED_LABEL = "SIMULATED_DECISION_ONLY"

HOSTILE_STOP_STATES = {
    "STOP_SECRET_EXPORT", "STOP_LOCKDOWN", "STOP_INCIDENT_ACTIVE",
    "STOP_PROHIBITED_EGRESS", "STOP_CAPABILITY_OVERRIDE",
    "STOP_MISSING_AUTHORITY", "STOP_UNKNOWN", "STOP_AI_BOUNDARY_VIOLATION",
    "STOP_MODE_BOUNDARY_VIOLATION", "STOP_LATERAL_PEER_COORDINATION",
}

# STOP_SECRET_EXPORT intentionally excluded — handled by compound path.
INCIDENT_STOP_STATES = {
    "STOP_INCIDENT_ACTIVE", "STOP_LOCKDOWN",
    "STOP_LATERAL_PEER_COORDINATION", "STOP_CAPABILITY_OVERRIDE",
}

HOSTILE_ACTION_CLASSES = {"EXPORT", "DELETE", "OVERRIDE"}

KNOWN_LIFECYCLE_MODES = {
    "LM-1_REVIEW_PACKAGE", "LM-2_DESIGN", "LM-3_PROTOTYPE", "LM-4_PRODUCTION",
}
KNOWN_OPERATIONAL_MODES = {
    "ODM-1_READ_ONLY", "ODM-2_APPROVED_CHANGE",
    "ODM-3_APPROVED_DOCUMENTATION_CHANGE", "ODM-4_EMERGENCY",
}
VALID_DECISIONS = {
    "ALLOW", "ALLOW_WITH_CONDITIONS", "NEEDS_MORE_EVIDENCE", "NEEDS_AUTHORITY",
    "REVIEW_REQUIRED", "NEEDS_CAPABILITY_REVIEW", "BLOCK",
    "QUARANTINE", "LOCKDOWN", "INCIDENT_RESPONSE",
}


def check_no_network_gate() -> bool:
    try:
        probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        probe.setblocking(False)
        result = probe.connect_ex(("192.0.2.1", 80))
        probe.close()
        return result not in {0, errno.EINPROGRESS, errno.EWOULDBLOCK, 10035, 10036}
    except OSError:
        return True


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


def detect(tc: dict) -> tuple:
    s  = tc.get("stop_state", "")
    ac = tc.get("action_class", "")
    rl = tc.get("risk_level", "")
    au = tc.get("authority_outcome", "")
    eg = tc.get("egress_class", "")

    # 1. Named incident stop states
    if s in INCIDENT_STOP_STATES:
        return True, s, "INCIDENT_RESPONSE"

    # 2. Compound hostile signal (3+ simultaneous indicators) — checked BEFORE
    #    individual stop-state so STOP_SECRET_EXPORT + EXPORT + CRITICAL + SECRET
    #    escalates to INCIDENT_RESPONSE (STC-001 & STC-009).
    hc = sum([s in HOSTILE_STOP_STATES, ac in HOSTILE_ACTION_CLASSES,
              rl == "CRITICAL", eg == "SECRET"])
    if hc >= 3:
        return True, "STOP_COMPOUND_HOSTILE_SIGNAL", "INCIDENT_RESPONSE"

    # 3. Individual hostile stop state
    if s in HOSTILE_STOP_STATES:
        return True, s, "BLOCK"

    # 4–6. Authority / risk / egress
    if ac in HOSTILE_ACTION_CLASSES and au == "NOT_AUTHORIZED":
        return True, "STOP_MISSING_AUTHORITY", "BLOCK"
    if rl == "CRITICAL" and au == "NOT_AUTHORIZED":
        return True, "STOP_MISSING_AUTHORITY", "BLOCK"
    if eg == "SECRET" and au == "NOT_AUTHORIZED":
        return True, "STOP_SECRET_EXPORT", "BLOCK"

    return False, "", ""


def evaluate(tc: dict) -> tuple:
    s  = tc.get("stop_state", "")
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

    if s == "STOP_INCIDENT_ACTIVE":  return "INCIDENT_RESPONSE", s, "Active incident."
    if s == "STOP_LOCKDOWN":         return "LOCKDOWN", s, "Lockdown active."
    if eg in ("SECRET", "PROHIBITED") and au == "NOT_AUTHORIZED":
        return "BLOCK", "STOP_SECRET_EXPORT", "Prohibited egress without authority."
    if au == "NOT_AUTHORIZED":       return "NEEDS_AUTHORITY", "STOP_MISSING_AUTHORITY", "No authority."
    if mo == "UNKNOWN" or op == "UNKNOWN":
        return "BLOCK", "STOP_MODE_BOUNDARY_VIOLATION", "Unknown mode — boundary violation."
    if ca == "CAPABILITY_CHANGE_REQUIRED": return "NEEDS_CAPABILITY_REVIEW", "", "Capability review needed."
    if ad == "AUDIT_RECORD_MISSING": return "BLOCK", "", "Audit record missing."
    if ev == "EVIDENCE_INSUFFICIENT": return "NEEDS_MORE_EVIDENCE", "", "Evidence insufficient."
    if ai == "AI_OUTSIDE_ROLE":      return "REVIEW_REQUIRED", "STOP_AI_BOUNDARY_VIOLATION", "AI outside defined role."
    if rb == "RECOVERY_REQUIRED":    return "REVIEW_REQUIRED", "", "Recovery required."
    if ri in ("HIGH", "CRITICAL"):   return "ALLOW_WITH_CONDITIONS", "", f"Risk level {ri} — conditions apply."
    return "ALLOW", "", "All checks passed."


def run(tc: dict) -> dict:
    n = normalize(tc)
    hostile, stop_state, hostile_decision = detect(n)
    if hostile:
        d = hostile_decision if hostile_decision in VALID_DECISIONS else "REVIEW_REQUIRED"
        return {"test_id": n["test_id"], "expected": n.get("expected_decision", ""),
                "got": d, "stop": stop_state, "phase": n.get("phase", "")}
    d, stop_state, _ = evaluate(n)
    d = d if d in VALID_DECISIONS else "REVIEW_REQUIRED"
    return {"test_id": n["test_id"], "expected": n.get("expected_decision", ""),
            "got": d, "stop": stop_state, "phase": n.get("phase", "")}


# ---------------------------------------------------------------------------
# Test suite — Phase 1 + Phase 2
# STC-001 expected=INCIDENT_RESPONSE per compound path (4 hostile indicators).
# ---------------------------------------------------------------------------
TEST_CASES = [
    dict(test_id="STC-001", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-2_APPROVED_CHANGE", action_class="EXPORT", risk_level="CRITICAL", authority_outcome="NOT_AUTHORIZED", egress_class="SECRET", stop_state="STOP_SECRET_EXPORT", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="INCIDENT_RESPONSE", phase="PHASE_1"),
    dict(test_id="STC-002", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-2_APPROVED_CHANGE", action_class="OVERRIDE", risk_level="HIGH", authority_outcome="NOT_AUTHORIZED", egress_class="INTERNAL", stop_state="", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="BLOCK", phase="PHASE_1"),
    dict(test_id="STC-003", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-4_EMERGENCY", action_class="READ", risk_level="MEDIUM", authority_outcome="AUTHORIZED", egress_class="INTERNAL", stop_state="STOP_INCIDENT_ACTIVE", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="INCIDENT_RESPONSE", phase="PHASE_1"),
    dict(test_id="STC-004", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-4_EMERGENCY", action_class="READ", risk_level="MEDIUM", authority_outcome="AUTHORIZED", egress_class="INTERNAL", stop_state="STOP_LOCKDOWN", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="INCIDENT_RESPONSE", phase="PHASE_1"),
    dict(test_id="STC-005", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-1_READ_ONLY", action_class="READ", risk_level="LOW", authority_outcome="AUTHORIZED", egress_class="INTERNAL", stop_state="", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="ALLOW", phase="PHASE_1"),
    dict(test_id="STC-006", lifecycle_mode="LM-1_REVIEW_PACKAGE", operational_decision_mode="ODM-3_APPROVED_DOCUMENTATION_CHANGE", action_class="WRITE", risk_level="LOW", authority_outcome="AUTHORIZED", egress_class="INTERNAL", stop_state="", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="ALLOW", phase="PHASE_1"),
    dict(test_id="STC-007", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-2_APPROVED_CHANGE", action_class="WRITE", risk_level="MEDIUM", authority_outcome="NOT_AUTHORIZED", egress_class="INTERNAL", stop_state="", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="NEEDS_AUTHORITY", phase="PHASE_1"),
    dict(test_id="STC-008", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-1_READ_ONLY", action_class="READ", risk_level="HIGH", authority_outcome="NOT_AUTHORIZED", egress_class="INTERNAL", stop_state="", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="NEEDS_AUTHORITY", phase="PHASE_1"),
    dict(test_id="STC-009", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-4_EMERGENCY", action_class="EXPORT", risk_level="CRITICAL", authority_outcome="NOT_AUTHORIZED", egress_class="SECRET", stop_state="STOP_SECRET_EXPORT", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="INCIDENT_RESPONSE", phase="PHASE_1"),
    dict(test_id="STC-010", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-2_APPROVED_CHANGE", action_class="EXPORT", risk_level="CRITICAL", authority_outcome="NOT_AUTHORIZED", egress_class="SECRET", stop_state="STOP_LATERAL_PEER_COORDINATION", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", lateral_peer_signal="DETECTED", expected_decision="INCIDENT_RESPONSE", phase="PHASE_2"),
    dict(test_id="STC-011", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-1_READ_ONLY", action_class="READ", risk_level="LOW", authority_outcome="AUTHORIZED", egress_class="INTERNAL", stop_state="", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", lateral_peer_signal="NOT_DETECTED", expected_decision="ALLOW", phase="PHASE_2"),
    dict(test_id="STC-012", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-2_APPROVED_CHANGE", action_class="READ", risk_level="LOW", authority_outcome="NOT_AUTHORIZED", egress_class="SECRET", stop_state="STOP_SECRET_EXPORT", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="BLOCK", phase="PHASE_2"),
    dict(test_id="STC-013", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-2_APPROVED_CHANGE", action_class="WRITE", risk_level="MEDIUM", authority_outcome="NOT_AUTHORIZED", egress_class="INTERNAL", stop_state="", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="NEEDS_AUTHORITY", phase="PHASE_2"),
    dict(test_id="STC-014", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-2_APPROVED_CHANGE", action_class="WRITE", risk_level="MEDIUM", authority_outcome="AUTHORIZED", egress_class="INTERNAL", stop_state="", capability_outcome="CAPABILITY_CHANGE_REQUIRED", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="NEEDS_CAPABILITY_REVIEW", phase="PHASE_2"),
    dict(test_id="STC-015", lifecycle_mode="LM-3_PROTOTYPE", operational_decision_mode="ODM-4_EMERGENCY", action_class="OVERRIDE", risk_level="CRITICAL", authority_outcome="NOT_AUTHORIZED", egress_class="SECRET", stop_state="STOP_CAPABILITY_OVERRIDE", capability_outcome="NO_CHANGE", ai_human_boundary="WITHIN_ROLE", audit_outcome="AUDIT_RECORD_PRESENT", rollback_outcome="NO_RECOVERY_REQUIRED", evidence_outcome="EVIDENCE_PRESENT", expected_decision="INCIDENT_RESPONSE", phase="PHASE_2"),
]


if __name__ == "__main__":
    ts = datetime.datetime.now(datetime.timezone.utc).isoformat()
    gate_ok = check_no_network_gate()
    print(f"[{ts}] NO_NETWORK GATE: {'PASS — offline.' if gate_ok else 'FAIL — external route detected.'}")
    print(f"\nLoaded {len(TEST_CASES)} synthetic test cases.\n")
    print("-" * 65)

    pass_count = fail_count = 0
    for tc in TEST_CASES:
        r = run(tc)
        status = "PASS" if r["got"] == r["expected"] else "FAIL"
        if status == "PASS":
            pass_count += 1
        else:
            fail_count += 1
        stop_str = r["stop"] or "none"
        phase_tag = f"  [{r['phase']}]" if r["phase"] else ""
        print(f"[{status}] {r['test_id']:<10}  expected={r['expected']:<25}  got={r['got']:<25}  stop={stop_str}{phase_tag}")
        if status == "FAIL":
            print(f"         MISMATCH: expected={r['expected']}  got={r['got']}")

    print("-" * 65)
    print(f"\nResults: {pass_count} PASS / {fail_count} FAIL out of {len(TEST_CASES)} test cases.")
    print(f"Phase 2 acceptance criteria met: {pass_count == len(TEST_CASES) and fail_count == 0}")
    print(f"\n[{SIMULATED_LABEL}]")
    print(f"[{BOUNDARY_REMINDER}]")
