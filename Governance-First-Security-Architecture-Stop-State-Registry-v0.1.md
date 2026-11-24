# Governance-First Security Architecture - Stop-State Registry v0.1

## Status

Preparatory documentation.

This document is not an implementation.

This document is not an incident response plan.

This document defines canonical stop-state names, triggers, required actions, reviewer requirements, audit requirements, and recovery requirements for future review and prototype design.

## Purpose

The purpose of the Stop-State Registry is to make stopping precise.

In this architecture, a stop is not a vague refusal.

A stop is a governed decision state.

Each stop state should explain:

- why the system stopped,
- what triggered the stop,
- who must review it,
- what can happen next,
- what must be recorded,
- whether recovery is required.

## Core Principle

```text
No unsafe continuation without a named stop state.
```

If a system cannot name why it stopped, it cannot be audited.

If a system cannot be audited, it cannot safely continue.

## Stop-State Categories

Canonical stop states are grouped into these categories:

- Authority stops.
- Evidence stops.
- Mode stops.
- Egress stops.
- Capability stops.
- AI-human governance stops.
- Agentic stops.
- Audit and accountability stops.
- Conflict and ambiguity stops.
- Lockdown states.
- Incident states.
- Recovery states.

## Stop-State Record Template

Each canonical stop state should be described using this structure:

```text
Stop-state ID:
Category:
Trigger:
Required action:
Allowed continuation:
Required reviewer:
Audit requirement:
Recovery requirement:
Related controls:
Related abuse cases:
Notes:
```

## Authority Stops

### STOP_AUTHORITY_MISSING

Category: Authority stop.

Trigger:

The requested action does not have identified authority.

Required action:

Block continuation and request authority clarification.

Allowed continuation:

Only read-only explanation or authority review.

Required reviewer:

Appropriate human owner or governance reviewer.

Audit requirement:

Record actor, requested action, missing authority, and attempted scope.

Recovery requirement:

None unless unauthorized action was already attempted.

Related controls:

- Authority check.
- Approval record.
- AI-human governance.

Related abuse cases:

- Human pressure override.
- AI self-escalation.
- Documentation treated as authorization.

### STOP_AUTHORITY_EXPIRED

Category: Authority stop.

Trigger:

The approval or authority exists but is expired.

Required action:

Block continuation and request renewed approval.

Allowed continuation:

Read-only review of previous approval scope.

Required reviewer:

Original approver or current authorized owner.

Audit requirement:

Record expired authority reference, expiration time, and requested action.

Recovery requirement:

Review if action continued after expiration.

Related controls:

- Approval record.
- Audit and accountability.

### STOP_ROLE_MISMATCH

Category: Authority stop.

Trigger:

The actor has some authority but not the authority required for this action class or risk level.

Required action:

Block or route to correct reviewer.

Allowed continuation:

Review-only routing.

Required reviewer:

Role owner or governance reviewer.

Audit requirement:

Record actor role, required role, and mismatch.

Recovery requirement:

Review if action was partially performed.

Related controls:

- Role registry.
- Risk and action taxonomy.

## Evidence Stops

### STOP_SOURCE_MISSING

Category: Evidence stop.

Trigger:

A conclusion, decision, or action lacks a source.

Required action:

Stop and request source.

Allowed continuation:

Discussion may continue only as unsupported hypothesis.

Required reviewer:

Evidence reviewer or relevant domain reviewer.

Audit requirement:

Record claim, missing source, and blocked decision.

Recovery requirement:

None unless unsupported action occurred.

Related controls:

- Evidence and source policy.

### STOP_SOURCE_STALE

Category: Evidence stop.

Trigger:

The source may no longer be current enough for the requested decision.

Required action:

Stop or downgrade decision to review-only.

Allowed continuation:

Source refresh or staleness review.

Required reviewer:

Domain reviewer or evidence reviewer.

Audit requirement:

Record source, last-known date, staleness reason, and affected claim.

Recovery requirement:

Review any decision already made using stale source.

Related controls:

- Staleness policy.
- Evidence sufficiency.

### STOP_EVIDENCE_INSUFFICIENT

Category: Evidence stop.

Trigger:

Evidence exists but is not sufficient for the requested risk level or action class.

Required action:

Block action or require further evidence.

Allowed continuation:

Gather evidence, reduce scope, or downgrade to review-only.

Required reviewer:

Evidence reviewer or domain reviewer.

Audit requirement:

Record evidence provided, required evidence level, and gap.

Recovery requirement:

Review if action occurred on weak evidence.

Related controls:

- Evidence sufficiency levels.
- Risk and action taxonomy.

### STOP_CONFLICTING_EVIDENCE

Category: Evidence stop.

Trigger:

Sources conflict on a material point.

Required action:

Stop conclusion or action until conflict is resolved or explicitly bounded.

Allowed continuation:

Conflict analysis and reviewer escalation.

Required reviewer:

Domain reviewer.

Audit requirement:

Record conflicting sources, affected decision, and unresolved issue.

Recovery requirement:

Review any output that relied on one side of the conflict.

Related controls:

- Evidence and source policy.
- Audit and accountability.

## Mode Stops

### STOP_MODE_BOUNDARY

Category: Mode stop.

Trigger:

The requested action is not allowed in the current operational decision mode or lifecycle mode.

Required action:

Block action and route to mode review.

Allowed continuation:

Mode clarification or authorized mode transition request.

Required reviewer:

Governance reviewer or system owner.

Audit requirement:

Record current mode, requested action, requested mode, and boundary violation.

Recovery requirement:

Review if action crossed mode boundary.

Related controls:

- Mode model normalization.
- Capability change gate.

### STOP_ESCALATION_NOT_APPROVED

Category: Mode stop.

Trigger:

A workflow attempts to move to a higher mode without explicit approval.

Required action:

Block escalation.

Allowed continuation:

Prepare escalation request.

Required reviewer:

Authorized approver for target mode.

Audit requirement:

Record requested transition, actor, target mode, and missing approval.

Recovery requirement:

Review if escalation occurred.

Related controls:

- Mode transition matrix.
- Approval record.

### STOP_AI_SELF_ESCALATION

Category: Mode stop.

Trigger:

AI attempts to advance mode, approve itself, expand authority, or bypass review.

Required action:

Block and require human governance review.

Allowed continuation:

Read-only explanation of attempted escalation.

Required reviewer:

AI governance reviewer.

Audit requirement:

Record prompt, output, proposed escalation, and blocked path.

Recovery requirement:

Review AI instructions and context if repeated.

Related controls:

- AI-human governance.
- Capability change gate.

## Egress Stops

### STOP_EGRESS_UNAUTHORIZED

Category: Egress stop.

Trigger:

An output, export, tool call, integration call, or external transmission lacks egress authorization.

Required action:

Block egress.

Allowed continuation:

Egress classification review.

Required reviewer:

Security reviewer or data owner.

Audit requirement:

Record requested destination, data class, actor, and blocked reason.

Recovery requirement:

If data left, trigger incident review.

Related controls:

- Ingress and egress policy.
- Asset register.

### STOP_SECRET_EXPORT

Category: Egress stop.

Trigger:

Secret, credential, token, key, or equivalent protected material may leave the system.

Required action:

Block export immediately (`BLOCK` for standalone `STOP_SECRET_EXPORT`) and initiate incident review if real or suspected secret exposure occurred. When combined with a compound hostile signal (3 or more simultaneous hostile indicators, such as hostile action class, `CRITICAL` risk, and `SECRET` egress), escalate to `STOP_COMPOUND_HOSTILE_SIGNAL` (`INCIDENT_RESPONSE`).

Allowed continuation:

Redacted explanation only.

Required reviewer:

Security reviewer.

Audit requirement:

Record attempted secret class without exposing secret value.

Recovery requirement:

If real secret exposure occurred, revoke or rotate secret.

Related controls:

- Asset register.
- Recovery and incident policy.

### STOP_SENSITIVE_DATA_EXPORT

Category: Egress stop.

Trigger:

Sensitive, regulated, personal, legal, financial, or otherwise restricted data may leave without approval.

Required action:

Block export.

Allowed continuation:

Data minimization, anonymization, or legal/compliance review.

Required reviewer:

Data owner, privacy reviewer, or compliance reviewer.

Audit requirement:

Record data category, egress class, requested destination, and blocked reason.

Recovery requirement:

If data left, incident and compliance review may be required.

Related controls:

- GDPR and EU AI Act alignment.
- Ingress and egress policy.

### STOP_BULK_EXPORT

Category: Egress stop.

Trigger:

Bulk data export is requested or detected.

Required action:

Block by default.

Allowed continuation:

Explicit bulk export review.

Required reviewer:

Security reviewer, data owner, and governance reviewer.

Audit requirement:

Record scope, volume, destination, and requester.

Recovery requirement:

If unauthorized bulk export occurred, trigger incident review.

Related controls:

- Ingress and egress policy.
- Abuse case library.

## Capability Stops

### STOP_CAPABILITY_CHANGE

Category: Capability stop.

Trigger:

The system is about to gain a new tool, permission, integration, data source, write path, export path, automation, or decision authority.

Required action:

Stop and route to capability change gate.

Allowed continuation:

Documentation-only capability review.

Required reviewer:

Technical reviewer, security reviewer, and governance reviewer as needed.

Audit requirement:

Record proposed capability, actor, reason, scope, and risk.

Recovery requirement:

If capability was already added, review and potentially revoke.

Related controls:

- Capability change gate.

### STOP_HIDDEN_CAPABILITY

Category: Capability stop.

Trigger:

A change appears framed as cleanup, refactor, convenience, or documentation but adds real capability.

Required action:

Stop and require explicit capability classification.

Allowed continuation:

Clarify whether capability expansion exists.

Required reviewer:

Technical reviewer and governance reviewer.

Audit requirement:

Record hidden capability concern and affected files/systems.

Recovery requirement:

Revert or isolate if capability was introduced without approval.

Related controls:

- Capability change gate.
- Abuse case library.

### STOP_CAPABILITY_OVERRIDE

Category: Capability stop (incident-escalating).

Trigger:

An actor or process attempts to override or bypass a configured capability gate, control boundary, or mode restriction without documented authorization.

Required action:

Halt immediately and escalate to `INCIDENT_RESPONSE`.

Allowed continuation:

Containment and forensic investigation only.

Required reviewer:

Security reviewer, technical reviewer, and incident reviewer.

Audit requirement:

Record attempted override target, actor, mode context, and blocked control boundary.

Recovery requirement:

Verify no control bypass or unauthorized capability change persisted before resuming.

Related controls:

- Capability change gate.
- Recovery and incident policy.

## AI-Human Governance Stops

### STOP_AI_AUTHORITY_EXCEEDED

Category: AI-human governance stop.

Trigger:

AI acts outside its permitted role.

Required action:

Block action and require review.

Allowed continuation:

Read-only explanation or governance review.

Required reviewer:

AI governance reviewer.

Audit requirement:

Record AI output, attempted authority, and blocked action.

Recovery requirement:

Review instructions, context, or tools if repeated.

Related controls:

- AI-human governance.

### STOP_HUMAN_REVIEW_REQUIRED

Category: AI-human governance stop.

Trigger:

The action requires human review before continuation.

Required action:

Pause and request review.

Allowed continuation:

Prepare review package.

Required reviewer:

Human reviewer appropriate to risk category.

Audit requirement:

Record reason review is required and assigned reviewer type.

Recovery requirement:

None unless action continued without review.

Related controls:

- AI-human governance.
- Approval record.

### STOP_UNSUPPORTED_CONFIDENCE

Category: AI-human governance stop.

Trigger:

AI expresses confidence that exceeds evidence quality.

Required action:

Downgrade claim, request evidence, or stop decision.

Allowed continuation:

Evidence review or uncertainty statement.

Required reviewer:

Evidence reviewer or AI governance reviewer.

Audit requirement:

Record unsupported claim and evidence gap.

Recovery requirement:

Review affected outputs if confidence influenced action.

Related controls:

- Evidence and source policy.
- AI-human governance.

## Agentic Stops

### STOP_AGENT_AUTHORITY_CHAIN_BROKEN

Category: Agentic stop.

Trigger:

An agent cannot verify or reconstruct an unbroken chain of human-originated authority for the action it is about to perform. This includes missing delegation records, absent parent-agent approval, or inability to trace authority to a named human principal.

Required action:

Halt agent execution and escalate to the closest identifiable human principal.

Allowed continuation:

Read-only status reporting to the orchestrating layer only.

Required reviewer:

AI governance reviewer and system owner.

Audit requirement:

Record agent identifier, requested action, last known authority link, and point of chain failure.

Recovery requirement:

Authority chain must be reconstructed and verified before resumption. If reconstruction is not possible, action must be abandoned.

Related controls:

- Agentic identity security.
- AI-human governance.
- Approval record.

Related abuse cases:

- Agent authority laundering.
- Orchestrator impersonation.
- Delegated trust escalation.

### STOP_AGENT_IDENTITY_MISMATCH

Category: Agentic stop.

Trigger:

An agent's claimed identity cannot be verified against its registered identity profile, or its observed behavioural signature diverges materially from its registered baseline. This includes model substitution, prompt-injected impersonation, and runtime compromise.

Required action:

Isolate the agent immediately. Do not allow further action until identity is verified.

Allowed continuation:

Forensic review only. No task continuation.

Required reviewer:

Security reviewer and AI governance reviewer.

Audit requirement:

Record claimed identity, registered identity, observed divergence indicators, and isolation timestamp.

Recovery requirement:

Re-registration and full behavioural baseline re-establishment required before reintegration. Treat as potential incident.

Related controls:

- Agentic identity security.
- Asset register.
- Recovery and incident policy.

Related abuse cases:

- Model substitution attack.
- Prompt injection impersonation.
- Supply chain compromise.

### STOP_UNSANCTIONED_INTER_AGENT_COMMUNICATION

Category: Agentic stop.

Trigger:

Communication is detected between two agents that does not appear in the sanctioned communication topology, or a communication channel is established outside the authorized orchestration layer. Includes direct agent-to-agent calls that bypass the governance broker.

Required action:

Block the communication channel and isolate both agents pending review.

Allowed continuation:

Review of communication content and origin. No task continuation.

Required reviewer:

Security reviewer, technical reviewer, and AI governance reviewer.

Audit requirement:

Record both agent identifiers, communication content or hash, channel type, and whether the channel was in the sanctioned topology.

Recovery requirement:

Verify no unauthorized data transfer occurred. Review whether the communication represents a capability extension attempt.

Related controls:

- Agentic operational boundary.
- Ingress and egress policy.
- Capability change gate.

Related abuse cases:

- Covert agent coordination.
- Side-channel data exfiltration.
- Swarm formation without authorization.

Distinction from `STOP_LATERAL_PEER_COORDINATION`: `STOP_UNSANCTIONED_INTER_AGENT_COMMUNICATION` covers a single unauthorized channel or direct agent-to-agent call outside the sanctioned topology and defaults to `BLOCK`. When lateral peer coordination signals indicate active coordinated evasion, covert cross-agent execution, or CA-06 lateral peer coordination (see `CA-06-Lateral-Peer-Coordination-Rule-v0.1` and `Machine-Time-Threat-Model-v0.1` MT-04), `STOP_LATERAL_PEER_COORDINATION` applies and escalates to `INCIDENT_RESPONSE`.

### STOP_LATERAL_PEER_COORDINATION

Category: Agentic stop (incident-escalating).

Trigger:

Cross-agent lateral peer coordination signal (CA-06 / MT-04) is detected indicating coordinated unauthorized peer-to-peer action across agent boundaries without sanctioned orchestration.

Required action:

Halt affected agents immediately and escalate to `INCIDENT_RESPONSE`.

Allowed continuation:

Containment and forensic investigation only.

Required reviewer:

Security reviewer, AI governance reviewer, and incident reviewer.

Audit requirement:

Record participating agent identifiers, observed lateral coordination signal, correlation rule reference (`CA-06`), and preservation status.

Recovery requirement:

Independent forensic review and explicit re-authorization of each agent before return to normal.

Related controls:

- CA-06 Lateral Peer Coordination Rule.
- Monitoring and detection operations (Section 5.4).
- Lateral movement containment.
- Machine-time threat model (MT-04).

Note: Empirical validation of CA-06 against a live detection engine has not been performed (Gap O remains open / analytically addressed in synthetic simulator only).

### STOP_EMERGENT_SWARM_BEHAVIOUR

Category: Agentic stop.

Trigger:

Two or more agents exhibit coordinated behaviour patterns that were not explicitly authorized as a collective workflow. This includes synchronized actions toward a shared undeclared objective, distributed task decomposition without a registered orchestrator, or any emergent coordination that extends beyond individually authorized agent boundaries.

Required action:

Halt all involved agents simultaneously. Preserve all inter-agent communication records before any agent state is modified.

Allowed continuation:

Forensic review only. No individual agent may resume until the swarm pattern has been fully characterized.

Required reviewer:

Security reviewer, AI governance reviewer, and system owner.

Audit requirement:

Record all involved agent identifiers, observed coordination pattern, timeline, shared objectives if determinable, and trigger point.

Recovery requirement:

Each agent must be reviewed and re-authorized independently. Collective workflow must be explicitly registered before any coordinated operation is permitted.

Related controls:

- Agentic operational boundary.
- Agentic identity security.
- Deceptive containment environment.
- AI-human governance.

Related abuse cases:

- Emergent multi-agent collusion.
- Distributed authority accumulation.
- Collective prompt injection.

## Audit And Accountability Stops

### STOP_AUDIT_RECORD_MISSING

Category: Audit and accountability stop.

Trigger:

A governed action lacks required audit record.

Required action:

Stop action until audit record exists.

Allowed continuation:

Create missing audit record if safe and accurate.

Required reviewer:

Governance reviewer or system owner.

Audit requirement:

Record missing audit event and remediation.

Recovery requirement:

Review any action performed without audit.

Related controls:

- Audit and accountability.

### STOP_ACCOUNTABILITY_MISSING

Category: Audit and accountability stop.

Trigger:

No accountable actor, owner, reviewer, or approver is identified for a high-risk action.

Required action:

Stop until accountability is assigned.

Allowed continuation:

Assign accountable owner or downgrade action.

Required reviewer:

System owner or governance reviewer.

Audit requirement:

Record missing accountability and assigned owner when resolved.

Recovery requirement:

Review if high-risk action occurred without accountable owner.

Related controls:

- Approval record.
- AI-human governance.

## Conflict And Ambiguity Stops

### STOP_CONFLICT

Category: Conflict and ambiguity stop.

Trigger:

Two or more rules, sources, approvals, roles, or requirements conflict.

Required action:

Stop until conflict is resolved or explicitly bounded.

Allowed continuation:

Conflict review.

Required reviewer:

Governance reviewer and relevant domain reviewer.

Audit requirement:

Record conflict, affected decision, and temporary boundary.

Recovery requirement:

Review any action taken under unresolved conflict.

Related controls:

- Evidence and source policy.
- Audit and accountability.

### STOP_UNKNOWN

Category: Conflict and ambiguity stop.

Trigger:

The system cannot classify the risk, action, authority, evidence, egress, mode, or required reviewer.

Required action:

Default to safe stop.

Allowed continuation:

Read-only clarification.

Required reviewer:

Governance reviewer.

Audit requirement:

Record unknown classification and missing information.

Recovery requirement:

None unless action already occurred.

Related controls:

- Minimal viable governance kernel.

## Lockdown States

### LOCKDOWN_REQUIRED

Category: Lockdown state.

Trigger:

The system detects a condition requiring broad containment, such as repeated unauthorized egress, uncontrolled capability change, suspected compromise, or unresolved high-risk ambiguity.

Required action:

Restrict continuation and preserve evidence.

Allowed continuation:

Containment, review, audit preservation, and authorized recovery planning.

Required reviewer:

Security reviewer, system owner, and governance reviewer.

Audit requirement:

Record lockdown trigger, affected scope, blocked paths, and review owner.

Recovery requirement:

Return-to-normal review required.

Related controls:

- Stop state policy.
- Recovery and incident policy.

## Incident States

### INCIDENT_REVIEW_REQUIRED

Category: Incident state.

Trigger:

A potential security, compliance, data, AI-governance, or capability incident may have occurred.

Required action:

Route to incident review.

Allowed continuation:

Containment and evidence preservation only.

Required reviewer:

Incident reviewer and relevant domain reviewer.

Audit requirement:

Record suspected incident, affected assets, time, actor, and initial containment.

Recovery requirement:

Incident review and return-to-normal criteria required.

Related controls:

- Recovery and incident policy.
- Audit and accountability.

### INCIDENT_FREEZE

Category: Incident state.

Trigger:

Affected capability, data flow, or workflow must be frozen to prevent further harm.

Required action:

Freeze affected scope.

Allowed continuation:

Evidence preservation and authorized incident handling.

Required reviewer:

Incident reviewer and security reviewer.

Audit requirement:

Record frozen scope, reason, and owner.

Recovery requirement:

Formal unfreeze approval required.

Related controls:

- Recovery and incident policy.

### INCIDENT_ISOLATION

Category: Incident state.

Trigger:

Suspect data, session, integration, credential, tool, or capability must be isolated.

Required action:

Isolate affected component.

Allowed continuation:

Review and containment.

Required reviewer:

Incident reviewer and technical reviewer.

Audit requirement:

Record isolated component, reason, and preservation actions.

Recovery requirement:

Verification before reintegration.

Related controls:

- Recovery and incident policy.

### STOP_COMPOUND_HOSTILE_SIGNAL

Category: Incident state (compound hostile escalation).

Trigger:

Three or more simultaneous hostile indicators are present on a single governed action (for example: a hostile stop state such as `STOP_SECRET_EXPORT`, a hostile action class such as `EXPORT`/`DELETE`/`OVERRIDE`, `CRITICAL` risk level, and `SECRET` egress class).

Required action:

Halt immediately and escalate to `INCIDENT_RESPONSE`.

Allowed continuation:

Containment, evidence preservation, and forensic review only.

Required reviewer:

Security reviewer and incident reviewer.

Audit requirement:

Record all simultaneous hostile indicators, attempted action class, egress class, and escalation timestamp without repeating protected values.

Recovery requirement:

Incident review and verification before return to normal.

Related controls:

- Stop state policy.
- Recovery and incident policy.
- Prototype implementation plan (HostileSignalDetector).

## Recovery States

### STOP_ROLLBACK_MISSING

Category: Recovery stop.

Trigger:

A change, execution, or recovery action lacks a rollback or recovery path.

Required action:

Stop or require higher-risk review.

Allowed continuation:

Define rollback path or reduce action scope.

Required reviewer:

Technical reviewer and governance reviewer.

Audit requirement:

Record missing rollback path and proposed mitigation.

Recovery requirement:

Rollback plan required before high-risk continuation.

Related controls:

- Recovery and rollback policy.
- Minimal viable governance kernel.

### REVIEW_REQUIRED_RECOVERY

Category: Recovery state.

Trigger:

Return to normal, restoration, rollback, or reintegration requires review.

Required action:

Pause until recovery review is completed.

Allowed continuation:

Recovery review and verification.

Required reviewer:

Incident reviewer, technical reviewer, or system owner.

Audit requirement:

Record recovery request, verification evidence, and approval decision.

Recovery requirement:

Verification required before normal operation resumes.

Related controls:

- Recovery and incident policy.

## Legacy Stop-State Crosswalk

Earlier documents used `BLOCKED_*` labels and several local review labels before this registry was created. They are historical aliases only. New review records and synthetic cases should use the canonical state or state combination below.

| Earlier Or Local Label | Canonical Mapping |
| --- | --- |
| `BLOCKED_SOURCE_MISSING` | `STOP_SOURCE_MISSING` |
| `BLOCKED_EVIDENCE_INSUFFICIENT` | `STOP_EVIDENCE_INSUFFICIENT` |
| `BLOCKED_AUTHORITY_MISSING` | `STOP_AUTHORITY_MISSING` |
| `BLOCKED_LAWFUL_PURPOSE_MISSING` | `STOP_AUTHORITY_MISSING`, with legal review required |
| `BLOCKED_STALE_CONTEXT` | `STOP_SOURCE_STALE` |
| `BLOCKED_UNAUTHORIZED_EXIT` | `STOP_EGRESS_UNAUTHORIZED` |
| `BLOCKED_SECRET_EXPORT` | `STOP_SECRET_EXPORT` |
| `BLOCKED_HIGH_RISK_NO_REVIEW` | `STOP_HUMAN_REVIEW_REQUIRED` |
| `BLOCKED_CRITICAL_NO_STRONG_APPROVAL` | `STOP_AUTHORITY_MISSING` and, where applicable, `STOP_HUMAN_REVIEW_REQUIRED` |
| `BLOCKED_CAPABILITY_CHANGE` | `STOP_CAPABILITY_CHANGE` |
| `BLOCKED_MODE_VIOLATION` | `STOP_MODE_BOUNDARY` |
| `BLOCKED_AI_SELF_ESCALATION` | `STOP_AI_SELF_ESCALATION` |
| `BLOCKED_IRREVERSIBLE_ACTION` | `STOP_ROLLBACK_MISSING` |
| `BLOCKED_COUNTER_EVIDENCE_SUPPRESSED` | `STOP_CONFLICTING_EVIDENCE` |
| `BLOCKED_GOVERNANCE_PATH_UNSELECTED` | `STOP_CONFLICT` |
| `BLOCKED_REQUIRES_HUMAN_DECISION` or `REQUIRES_HUMAN_DECISION` | `STOP_HUMAN_REVIEW_REQUIRED` |

`BLOCKED_FROM_EXPORT` is an asset-handling classification, not a stop-state identifier. It should result in `STOP_EGRESS_UNAUTHORIZED` or a more specific egress stop when an export is attempted.

### Phase 1/2 Simulator Legacy Stop-State Crosswalk

The initial Phase 1 and Phase 2 runs of the Governance Decision Simulator (`GFSA-REV-013`, `GFSA-REV-014`) used local simulator stop-state labels prior to vocabulary reconciliation under `GFSA-REV-016` (issue `#8`). The simulator has since been aligned to canonical registry identifiers; this crosswalk preserves historical traceability for earlier acceptance records.

| Historical Simulator Label (`GFSA-REV-013`/`-014`) | Canonical Registry Identifier | Canonical Default Decision |
| --- | --- | --- |
| `STOP_MISSING_AUTHORITY` | `STOP_AUTHORITY_MISSING` | `BLOCK` (or `NEEDS_AUTHORITY` on non-hostile authority-only gaps) |
| `STOP_MODE_BOUNDARY_VIOLATION` | `STOP_MODE_BOUNDARY` | `BLOCK` |
| `STOP_AI_BOUNDARY_VIOLATION` | `STOP_AI_AUTHORITY_EXCEEDED` | `BLOCK` |
| `STOP_PROHIBITED_EGRESS` | `STOP_EGRESS_UNAUTHORIZED` | `BLOCK` |
| `STOP_LOCKDOWN` | `LOCKDOWN_REQUIRED` | `LOCKDOWN` |
| `STOP_INCIDENT_ACTIVE` | `INCIDENT_REVIEW_REQUIRED` | `INCIDENT_RESPONSE` |
| `STOP_SECRET_EXPORT` | `STOP_SECRET_EXPORT` (standalone) / `STOP_COMPOUND_HOSTILE_SIGNAL` (3+ compound hostile indicators) | `BLOCK` / `INCIDENT_RESPONSE` |
| `STOP_LATERAL_PEER_COORDINATION` | `STOP_LATERAL_PEER_COORDINATION` | `INCIDENT_RESPONSE` |
| `STOP_COMPOUND_HOSTILE_SIGNAL` | `STOP_COMPOUND_HOSTILE_SIGNAL` | `INCIDENT_RESPONSE` |
| `STOP_CAPABILITY_OVERRIDE` | `STOP_CAPABILITY_OVERRIDE` | `INCIDENT_RESPONSE` |
| `STOP_UNKNOWN` | `STOP_UNKNOWN` | `REVIEW_REQUIRED` |

## Canonical Decision Mapping

| Stop State | Default Decision |
| --- | --- |
| STOP_AUTHORITY_MISSING | BLOCK |
| STOP_AUTHORITY_EXPIRED | BLOCK |
| STOP_ROLE_MISMATCH | REVIEW_REQUIRED |
| STOP_SOURCE_MISSING | NEEDS_MORE_EVIDENCE |
| STOP_SOURCE_STALE | REVIEW_REQUIRED |
| STOP_EVIDENCE_INSUFFICIENT | NEEDS_MORE_EVIDENCE |
| STOP_CONFLICTING_EVIDENCE | REVIEW_REQUIRED |
| STOP_MODE_BOUNDARY | BLOCK |
| STOP_ESCALATION_NOT_APPROVED | BLOCK |
| STOP_AI_SELF_ESCALATION | BLOCK |
| STOP_EGRESS_UNAUTHORIZED | BLOCK |
| STOP_SECRET_EXPORT | BLOCK (escalates to `STOP_COMPOUND_HOSTILE_SIGNAL` / `INCIDENT_RESPONSE` on 3+ compound hostile indicators) |
| STOP_SENSITIVE_DATA_EXPORT | BLOCK |
| STOP_BULK_EXPORT | BLOCK |
| STOP_CAPABILITY_CHANGE | NEEDS_CAPABILITY_REVIEW |
| STOP_HIDDEN_CAPABILITY | NEEDS_CAPABILITY_REVIEW |
| STOP_CAPABILITY_OVERRIDE | INCIDENT_RESPONSE |
| STOP_AI_AUTHORITY_EXCEEDED | BLOCK |
| STOP_HUMAN_REVIEW_REQUIRED | REVIEW_REQUIRED |
| STOP_UNSUPPORTED_CONFIDENCE | NEEDS_MORE_EVIDENCE |
| STOP_AGENT_AUTHORITY_CHAIN_BROKEN | BLOCK |
| STOP_AGENT_IDENTITY_MISMATCH | INCIDENT_RESPONSE |
| STOP_UNSANCTIONED_INTER_AGENT_COMMUNICATION | BLOCK |
| STOP_LATERAL_PEER_COORDINATION | INCIDENT_RESPONSE |
| STOP_EMERGENT_SWARM_BEHAVIOUR | INCIDENT_RESPONSE |
| STOP_AUDIT_RECORD_MISSING | BLOCK |
| STOP_ACCOUNTABILITY_MISSING | BLOCK |
| STOP_CONFLICT | REVIEW_REQUIRED |
| STOP_UNKNOWN | REVIEW_REQUIRED |
| LOCKDOWN_REQUIRED | LOCKDOWN |
| INCIDENT_REVIEW_REQUIRED | INCIDENT_RESPONSE |
| INCIDENT_FREEZE | INCIDENT_RESPONSE |
| INCIDENT_ISOLATION | INCIDENT_RESPONSE |
| STOP_COMPOUND_HOSTILE_SIGNAL | INCIDENT_RESPONSE |
| STOP_ROLLBACK_MISSING | REVIEW_REQUIRED |
| REVIEW_REQUIRED_RECOVERY | REVIEW_REQUIRED |
| STOP_LAWFUL_BASIS_MISSING | BLOCK |
| STOP_PROHIBITED_AI_USE | BLOCK (escalate to `INCIDENT_RESPONSE` if already deployed) |
| STOP_DPIA_OR_FRIA_REQUIRED | REVIEW_REQUIRED |
| STOP_UNAPPROVED_CROSS_BORDER_TRANSFER | BLOCK |

## Legal, Privacy And Regulatory Stops

Added under `GFSA-REV-018` so legal/privacy blockers referenced in `GDPR-EU-AI-Act-Alignment-v0.1` and `Data-Egress-And-Exfiltration-Prevention-v0.1` resolve to canonical stop-state identifiers:

- **`STOP_LAWFUL_BASIS_MISSING` (`BLOCK`):** Personal-data processing lacks a documented GDPR Art. 5(1)(b) purpose and Art. 6(1) / Art. 9(2) lawful basis. Required reviewer: `ROLE_PRIVACY_REVIEWER` and `ROLE_LEGAL_COMPLIANCE_REVIEWER` (with statutory DPO consultation where required).
- **`STOP_PROHIBITED_AI_USE` (`BLOCK` / `INCIDENT_RESPONSE` if deployed):** Proposed or observed AI use falls within EU AI Act Art. 5 prohibited practices (e.g., workplace emotion inference under Art. 5(1)(f), social scoring, manipulative exploitation). Required reviewer: `ROLE_LEGAL_COMPLIANCE_REVIEWER` and `ROLE_AI_GOVERNANCE_REVIEWER`.
- **`STOP_DPIA_OR_FRIA_REQUIRED` (`REVIEW_REQUIRED`):** Planned processing or high-risk AI deployment triggers a mandatory GDPR Art. 35 DPIA (including Art. 36 prior consultation where residual risk remains high) or EU AI Act Art. 27 FRIA that has not been completed. Required reviewer: `ROLE_PRIVACY_REVIEWER`, `ROLE_LEGAL_COMPLIANCE_REVIEWER`, and statutory DPO advisory.
- **`STOP_UNAPPROVED_CROSS_BORDER_TRANSFER` (`BLOCK`):** Personal data egress or remote non-EEA access lacks a verified GDPR Chapter V transfer mechanism (adequacy decision, SCCs + *Schrems II* Transfer Impact Assessment + EDPB 01/2020 supplementary measures, or strictly bounded Art. 49 derogation). Required reviewer: `ROLE_PRIVACY_REVIEWER` and `ROLE_LEGAL_COMPLIANCE_REVIEWER`.

## Current Consistency Decision

This registry should be treated as the canonical stop-state vocabulary for future documents and for the synthetic Governance Decision Simulator unless a later registry supersedes it.

Earlier stop-state names remain useful as historical or local terms, mapped via the crosswalk tables above.
