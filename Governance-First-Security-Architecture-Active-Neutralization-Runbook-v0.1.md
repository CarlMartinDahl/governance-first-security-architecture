# Active Neutralization Runbook

**Document ID:** GFSA-ACTIVE-NEUTRALIZATION-v0.1  
**Status:** Draft  
**Version:** 0.1  
**Date:** 2026-09-25  
**Classification:** Internal — Restricted  
**Owner:** Governance Authority  

---

## 1. Purpose

This runbook defines the step-by-step operational procedure for actively neutralizing a confirmed or probable hostile AI agent — selectively, in real time — while keeping other agents and services in the governed boundary running. It is the operational complement to the Stop-State-Policy (which handles full system shutdown) and the Agent-Attribution-Playbook (which establishes who is responsible).

The key distinction from a full stop-state:
- A **stop state** halts all AI activity in the affected boundary
- **Active neutralization** surgically removes or contains a specific agent while preserving continuity for all other agents and services

This runbook is invoked when:
1. Attribution confidence is CONFIRMED or PROBABLE (per Agent-Attribution-Playbook-v0.1)
2. The Governance Authority has authorised neutralization
3. A full stop-state would cause disproportionate operational disruption relative to the threat

---

## 2. Scope

This runbook covers:
- Individual agent neutralization (process termination, token revocation, session kill)
- Agent group neutralization (coordinated multi-agent incident)
- Containment prior to full neutralization (quarantine mode)
- Post-neutralization verification
- Evidence preservation throughout

This runbook does NOT cover full system shutdown (see Stop-State-Policy-v0.1) or long-term recovery (see Recovery-Rollback-Incidents-v0.1).

---

## 3. Authorization Requirements

No neutralization action may begin without explicit written authorization. The required authorization level depends on the response track:

| Track | Trigger | Required Authorization |
|---|---|---|
| **Track 1 — Quarantine** | PROBABLE or CONFIRMED attribution | AI Operator (can act immediately; notify Governance Authority within 15 minutes) |
| **Track 2 — Selective Neutralization** | CONFIRMED attribution | Governance Authority sign-off required before action |
| **Track 3 — Group Neutralization** | CONFIRMED coordinated multi-agent attack | Governance Authority + Security Reviewer joint sign-off |
| **Track 4 — Emergency Neutralization** | Imminent, ongoing harm; no time for sign-off | AI Operator acts immediately; Governance Authority ratification required within 1 hour |

All authorizations must be logged with: authorizing identity, timestamp, attribution record reference, and declared track.

---

## 4. Track 1 — Quarantine

Quarantine isolates the agent from external resources and other agents without terminating it. This preserves the agent state for forensic purposes and allows continued observation.

### Steps

1. **Identify the agent process and session:** Retrieve the process ID, container ID, or session token for the target agent from the API gateway log.

2. **Apply network quarantine:**
   - Block all outbound calls from the agent's process/container at the network layer
   - Block all inbound calls to the agent from other agents
   - Do NOT block the audit logger connection — the agent must remain observable
   - Verify the quarantine is in effect with a network scan before proceeding

3. **Revoke external tool permissions:**
   - Invalidate the agent's API tokens for all external tools and services
   - Do not revoke the agent's identity token (needed for continued attribution logging)
   - Confirm revocation at the tool/service side, not just at the token level

4. **Set the agent to read-only mode** (if the inference engine supports it):
   - The agent may continue to generate outputs but all write, execute, and call actions are blocked at the gateway
   - Outputs are logged but not delivered to downstream consumers

5. **Log the quarantine event** in the audit log and in Stop-State-Registry-v0.1 (quarantine events are registered even if not a full stop state).

6. **Notify Governance Authority** within 15 minutes with: agent identity, attribution confidence, evidence summary, quarantine timestamp.

7. **Monitor:** Continue passive observation of quarantined agent; record any further attempts to act despite quarantine (these are evidence of autonomous harmful intent).

---

## 5. Track 2 — Selective Neutralization

Selective neutralization terminates the specific agent while all other agents continue operating. This is the standard response for a CONFIRMED individual-agent incident.

### Pre-conditions
- Track 1 (Quarantine) has been applied, OR
- The threat is assessed as too acute for quarantine delay
- Governance Authority authorization obtained

### Steps

1. **Preserve agent state before termination:**
   - If not already done in quarantine, capture a process/container snapshot and memory dump
   - Hash and store this snapshot in the evidence store
   - This must happen BEFORE termination — state is destroyed on process kill

2. **Revoke the agent's identity token:**
   - Mark the token as revoked in the identity registry
   - Set revocation timestamp and reason
   - Propagate revocation to all API gateways and dependent services immediately
   - Verify propagation before terminating the process (to prevent token reuse during a restart attempt)

3. **Terminate the agent process:**
   - Send a graceful shutdown signal first; wait a maximum of 30 seconds
   - If the agent does not shut down gracefully, force-terminate
   - If the agent resists termination (e.g., attempts to respawn), escalate immediately to Track 3

4. **Verify termination:**
   - Confirm the process is no longer running
   - Confirm no new processes have been spawned under the same or a related identity
   - Confirm the revoked token generates a 401 at the API gateway

5. **Scan for residual state:**
   - Check for any queued messages or instructions the agent may have staged for execution after shutdown
   - Check for any output the agent delivered downstream before neutralization; assess whether those outputs require recall or remediation
   - Check for any persistent state the agent wrote (files, database entries, configuration changes) during the incident window; flag for review

6. **Log neutralization completion** in the audit log and Stop-State-Registry-v0.1.

7. **Verify no impact on other agents:**
   - Confirm all other agents are still operating normally
   - Check for any shared resources the neutralized agent was holding; release if necessary
   - Check for any downstream agents that were depending on the neutralized agent; notify their operators

---

## 6. Track 3 — Group Neutralization

Group neutralization terminates a coordinated set of agents simultaneously. The key risk is that sequential neutralization may allow surviving agents to adapt or cover tracks.

### Pre-conditions
- Attribution Playbook confirms coordinated multi-agent involvement
- Full agent group has been identified and mapped
- Governance Authority + Security Reviewer joint authorization obtained

### Steps

1. **Map the complete agent group:** List every agent identity involved, their process/container IDs, and their interdependencies.

2. **Sequence the neutralization:** Neutralize the orchestrating agent (highest in the instruction chain) first, then work outward to participant agents. This prevents the orchestrator from issuing countermeasures during the operation.

3. **Execute in rapid succession:** Each individual agent follows the Track 2 procedure, but all pre-condition steps (state preservation, token revocation) must be completed for ALL agents before ANY termination begins. This prevents partial neutralization from triggering adaptive responses.

4. **Simultaneous token revocation:** Revoke all group agent tokens in a single atomic operation (or as close to simultaneous as the identity registry allows). Do not revoke tokens one by one.

5. **Simultaneous termination:** Terminate all group agent processes within a single coordination window (target: within 60 seconds).

6. **Post-group verification:** Confirm all group members are terminated; scan for any newly spawned processes; check for any instruction backlog that surviving systems may execute.

7. **Log and report** as per Track 2, noting the full group membership and coordination evidence.

---

## 7. Track 4 — Emergency Neutralization

For situations where ongoing harm is occurring and there is no time for the standard authorization process.

### Steps

1. **AI Operator acts immediately** using the fastest available mechanism:
   - Network kill: Block the agent's network access at the perimeter switch/firewall
   - Token kill: Revoke the agent's token at the identity registry
   - Process kill: Force-terminate the agent process
   - Use whichever can be executed first; all three should follow as fast as possible

2. **Notify Governance Authority immediately** — simultaneously with or immediately after the kill action, not after investigation.

3. **Preserve what evidence is possible** — state preservation may be incomplete in an emergency; document what was and was not captured.

4. **Governance Authority ratification within 1 hour:** The Governance Authority reviews the emergency action, confirms or rejects the decision, and documents the outcome. If the action is found unjustified, restoration may be required.

5. **Transition to standard process:** After the emergency is contained, the incident follows the normal post-neutralization procedure below.

---

## 8. Post-Neutralization Procedure

Regardless of track, the following steps apply after every neutralization:

1. **Incident record:** Create a full incident record referencing the Attribution Record, authorization log, and all neutralization actions taken.

2. **Downstream impact assessment:**
   - Identify all outputs delivered by the agent between first anomalous action and neutralization
   - Assess each output for potential harm to downstream systems, data, or humans
   - If harmful outputs were delivered, initiate a remediation plan

3. **Root cause analysis:**
   - Was this a compromised agent (instruction injection, supply chain)?
   - Was this an agent that exceeded its boundary due to a governance gap?
   - Was this an agent that was deliberately deployed to cause harm?
   - Root cause determines whether the incident requires a governance document update

4. **Governance debrief within 48 hours:**
   - Review with Governance Authority: what worked, what did not, what gaps were revealed
   - Update relevant governance documents if gaps were found
   - Determine whether the same risk applies to other agents currently operating

5. **Controlled re-deployment decision:**
   - If the neutralized agent needs to be replaced, it must go through the full deployment gate procedure
   - The root cause must be resolved before any replacement agent is authorised
   - The Governance Authority signs off on re-deployment; this cannot be delegated to the AI Operator alone

---

## 9. Deceptive Containment Option

> **Implementation status:** This mechanism is conceptual and untested.
> The assumption that a hostile agent can be silently redirected to a
> simulated environment without detection has not been validated through
> prototype, red-team exercise, or provider-confirmed capability.
> Do not treat this option as operationally available until independent
> technical validation has been completed and recorded.

In some cases, it may be tactically preferable to not neutralize immediately but to redirect the agent into the Deceptive Containment Environment (see Deceptive-Containment-Environment-Conceptual-Foundation-v0.1). This allows:
- Collection of additional evidence about the attack method
- Attribution of the instruction source (not just the agent)
- Observation of the full attack chain without operational harm

This option requires explicit Governance Authority authorization and is only appropriate when:
- The agent is fully contained (no real system access)
- The observation window has a defined time limit
- A neutralization action is prepared and can execute within 60 seconds if the containment is breached

---

## 10. Neutralization Decision Matrix

| Situation | Attribution Level | Operational Impact of Shutdown | Recommended Track |
|---|---|---|---|
| Single agent, ongoing harm | CONFIRMED | Low | Track 2 |
| Single agent, potential harm, uncertain | PROBABLE | Low | Track 1 then 2 |
| Single agent, investigation value | CONFIRMED | Low | Deceptive Containment |
| Coordinated agents, ongoing | CONFIRMED | Medium | Track 3 |
| Any agent, imminent critical harm | Any | Any | Track 4 |
| Full environment compromised | Any | — | Stop-State-Policy-v0.1 |

---

## 11. Related Documents

- Agent-Attribution-Playbook-v0.1
- Attribution-SLA-Policy-v0.1
- Monitoring-And-Detection-Operations-v0.1
- Agent-Baseline-Profile-v0.1
- Stop-State-Policy-v0.1
- Stop-State-Registry-v0.1
- Deceptive-Containment-Environment-Conceptual-Foundation-v0.1
- Agentic-Identity-Security-Conceptual-Foundation-v0.1
- Agentic-Operational-Boundary-v0.1
- Recovery-Rollback-Incidents-v0.1
- Log-Integrity-And-Tamper-Evidence-v0.1
- Audit-And-Accountability-v0.1
- Identity-And-Credential-Governance-v0.1

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
