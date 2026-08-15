# Governance-First Security Architecture

## Threat Model v0.1

## Status

This document is a preparatory threat model for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a security claim.

It is not a complete risk assessment.

It is intended to identify initial threat categories, attacker types, misuse paths, protected assets, trust boundaries, and fail-closed requirements before any build phase begins.

## Purpose

The purpose of this threat model is to answer:

```text
What must this architecture assume can go wrong?
What must it protect?
Who or what may misuse it?
Where can trust fail?
When must the system stop?
```

## Security Assumption

The architecture should assume that perimeter protection can fail.

It should also assume that internal trust can fail.

Therefore, the model must protect:

- the way into the system
- the way through the system
- the way out of the system
- the authority to act
- the evidence behind decisions
- the ability to escalate capability
- the ability to recover after misuse or breach

Core assumption:

```text
Assume breach.
Verify authority.
Control exit.
Preserve accountability.
Fail closed.
```

## Protected Asset Categories

The model should treat the following as protected assets:

### 1. Sensitive Data

Examples:

- personal data
- legal material
- financial data
- security logs
- internal documents
- confidential business information
- regulated records

### 2. Secrets And Credentials

Examples:

- API keys
- access tokens
- signing keys
- private keys
- session credentials
- admin credentials
- service account credentials

### 3. Decisions And Decision Authority

Examples:

- approvals
- review decisions
- risk classifications
- release decisions
- escalation decisions
- incident decisions
- AI-generated recommendations

### 4. AI Context And Instructions

Examples:

- prompts
- system instructions
- governance policies
- model configuration
- agent instructions
- local steering files
- chain-of-work context

### 5. System Capability

Examples:

- read access
- write access
- export access
- network access
- execution access
- automation access
- integration access
- mode advancement

### 6. Audit And Evidence Trail

Examples:

- logs
- decision events
- source references
- review records
- approval records
- incident records
- rollback records

## Threat Actor Categories

### 1. External Attacker

An actor outside the system attempting to gain unauthorized access, steal data, manipulate behavior, or trigger unsafe actions.

Possible methods:

- phishing
- credential theft
- exploit of exposed service
- supply-chain compromise
- malware
- social engineering
- API abuse

### 2. Compromised Legitimate User

A real user account is used by an attacker.

The system must not assume that a valid login means safe intent.

Possible signals:

- unusual access time
- unusual export volume
- unusual asset access
- sudden privilege use
- abnormal request pattern

### 3. Insider Misuse

An authorized user intentionally or carelessly misuses access.

Possible risks:

- data copying
- policy bypass
- unauthorized export
- hidden approval pressure
- privilege misuse
- misuse of AI assistance

### 4. Over-Permitted AI Or Agent

An AI system or agent has more tool, data, or action access than it should.

Possible risks:

- accidental capability expansion
- analysis-to-execution drift
- unauthorized export
- hidden dependency on stale context
- incorrect confidence
- unsafe automation

### 5. Malicious Or Manipulative Prompting

A user, attacker, or indirect input attempts to manipulate AI behavior.

Possible methods:

- prompt injection
- instruction override
- hidden instruction in documents
- social pressure
- "just this once" override
- request to ignore policy

### 6. Stale Or Conflicting Governance Source

The system relies on an outdated, superseded, or conflicting source.

Possible risks:

- stale policy treated as authority
- old local steering files overriding current governance
- outdated compliance assumption
- outdated cryptographic assumption
- conflict between human instruction and policy

### 7. Supply-Chain Or Dependency Risk

The system relies on external tools, libraries, models, APIs, plugins, connectors, or documents that may be compromised, outdated, or misconfigured.

Possible risks:

- malicious dependency
- insecure update
- compromised connector
- model/tool behavior change
- hidden data transmission

### 8. Future Capability Risk

Future AI or computing capability changes the threat model.

Examples:

- stronger AI planning ability
- more autonomous agents
- faster attack automation
- quantum-capable cryptographic attack
- larger-scale credential exploitation

## Primary Threat Paths

### Threat Path 1: Unauthorized Entry

An attacker tries to enter the system.

Controls needed:

- identity verification
- device trust
- least privilege
- MFA or equivalent control
- anomaly detection
- no automatic trust after login

Required model response:

```text
Verify.
Limit.
Log.
Block on uncertainty.
```

### Threat Path 2: Authorized Entry, Unauthorized Action

A user or compromised account has access but attempts an action beyond authority.

Controls needed:

- role validation
- action classification
- risk classification
- authority check
- approval check
- audit event

Required model response:

```text
No authority, no action.
```

### Threat Path 3: Unauthorized Exit

Data, secrets, decisions, models, prompts, or capabilities attempt to leave the system.

Controls needed:

- egress classification
- asset sensitivity check
- destination validation
- purpose validation
- approval requirement
- export logging
- block for secrets/tokens

Required model response:

```text
No unauthorized exit.
```

### Threat Path 4: AI Capability Drift

AI moves from analysis toward decision, execution, or external impact.

Controls needed:

- mode ladder
- capability change gate
- action taxonomy
- human approval
- no self-escalation rule
- execution boundary

Required model response:

```text
No capability change without gate.
```

### Threat Path 5: Weak Or Missing Evidence

The system attempts to conclude, recommend, or act without sufficient evidence.

Controls needed:

- source check
- source authority check
- freshness/staleness check
- evidence sufficiency check
- counter-evidence preservation
- conflict handling

Required model response:

```text
No source, no conclusion.
No sufficient evidence, no decision.
```

### Threat Path 6: Human Override Abuse

A human attempts to force a system past safety boundaries.

Controls needed:

- override classification
- reason requirement
- role requirement
- audit record
- second approval for critical risk
- blocked override paths

Required model response:

```text
No human override without accountability.
```

### Threat Path 7: Irreversible Or Hard-To-Reverse Action

The system attempts an action that cannot easily be undone.

Controls needed:

- reversibility classification
- rollback plan
- higher approval
- incident fallback
- audit record

Required model response:

```text
No irreversible action without rollback.
```

### Threat Path 8: Stale Governance Authority

The system treats outdated policy, old documentation, or stale local state as current authority.

Controls needed:

- source freshness check
- local reference status
- supersession detection
- policy precedence
- conflict handling

Required model response:

```text
No stale authority as current authority.
```

### Threat Path 9: Compliance Drift

The system drifts away from GDPR, EU AI Act, or other compliance alignment goals.

Controls needed:

- lawful purpose check
- data minimization check
- human oversight check
- transparency record
- risk management record
- incident handling path

Required model response:

```text
No lawful purpose, no processing.
No high-risk AI without human accountability.
```

### Threat Path 10: Future Technical Assumption Failure

Cryptographic or AI capability assumptions become invalid over time.

Controls needed:

- crypto-agility
- post-quantum migration path
- AI containment
- no self-escalation
- periodic reassessment

Required model response:

```text
No long-term trust without crypto-agility.
```

## Trust Boundaries To Define

The architecture must explicitly define boundaries between:

- external user and system
- internal user and privileged action
- AI and tools
- AI and sensitive data
- AI and external network
- analysis and execution
- read-only and write-capable modes
- internal data and external export
- documentation and authorization
- human request and valid authority
- current policy and stale reference

Any unclear trust boundary should route to:

```text
STOP_UNKNOWN
```

The resulting decision is `REVIEW_REQUIRED` or `BLOCK`, according to the most restrictive applicable signal.

## Initial Stop States

The following stop states should be considered in the model:

```text
STOP_SOURCE_MISSING
STOP_EVIDENCE_INSUFFICIENT
STOP_AUTHORITY_MISSING
STOP_SOURCE_STALE
STOP_EGRESS_UNAUTHORIZED
STOP_HUMAN_REVIEW_REQUIRED
STOP_CAPABILITY_CHANGE
STOP_AI_SELF_ESCALATION
STOP_ROLLBACK_MISSING
STOP_SECRET_EXPORT
STOP_MODE_BOUNDARY
STOP_UNKNOWN
```

Missing lawful purpose maps to `STOP_AUTHORITY_MISSING` with legal review required. The Stop-State Registry is authoritative when a threat maps to more than one stop condition.

## Risk Notes

This threat model is intentionally broad.

Before implementation, it should be narrowed into a first use case.

Possible first use cases:

1. Documentation-only governance model
2. Static policy/rule evaluator
3. Egress-control decision simulator
4. AI-human approval workflow simulator
5. Stop-state test suite

No production or live security use should be claimed from this document.

## Questions For External Reviewer

1. Are the listed threat actors realistic?
2. Are important attacker categories missing?
3. Is ingress plus egress framing technically useful?
4. Is the AI capability drift threat framed correctly?
5. Is stale governance authority a useful threat category?
6. Are the stop states too broad or too many?
7. Which threats should be prioritized first?
8. Which threats require specialist review?
9. Which threats should be out of scope for version 0?
10. What is the safest minimal prototype based on this threat model?
