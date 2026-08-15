# Governance-First Security Architecture - Provider And Platform Constraints v0.1

## Status

Review-driven clarification.

This document is not a new model layer.

This document is not implementation authorization.

This document records provider, platform, tool-use, and policy constraints that may affect any future prototype or agent discussion.

## Purpose

The purpose of this document is to prevent the model from assuming that technical possibility equals permitted use.

Even if a future system could technically be built, it may still be constrained by:

- AI provider policy,
- platform terms,
- cyber safety restrictions,
- agent/tool-use restrictions,
- data processing restrictions,
- responsible disclosure requirements,
- legal or compliance requirements,
- organizational security rules.

## Core Principle

```text
No capability assumption without provider, platform, policy, and legal review.
```

## Current Constraint

External technical feedback has indicated that real security-agent functionality may be restricted, blocked, or require special approval/access with AI providers.

This reinforces the current boundary:

```text
The first possible prototype is a synthetic governance decision simulator.
It is not a security agent.
It does not scan, exploit, remediate, enforce, or act on real systems.
```

Current verification state:

```text
Provider policy reference review: PERFORMED_FOR_DOCUMENTATION_BOUNDARY
Provider permission verification for implementation: NOT_PERFORMED
Platform permission verification for implementation: NOT_PERFORMED
Implementation authorization: NOT_GRANTED
Document boundary last reviewed: 2026-08-15
```

Provider and platform policies are time-sensitive. They must be checked against current primary provider and platform sources before any future capability discussion.

Primary policy references reviewed for this documentation boundary:

- [OpenAI Usage Policies](https://openai.com/policies/usage-policies/)
- [Anthropic Acceptable Use Policy](https://www.anthropic.com/legal/aup)

These sources confirm that provider rules evolve and that cyber, agentic, privacy, and high-stakes uses may be prohibited, restricted, or subject to additional requirements. This review does not determine that any future implementation is permitted.

## Provider Constraints

Before any future prototype implementation discussion, verify current rules for:

- OpenAI usage policies,
- OpenAI cyber access or trusted-access requirements,
- Anthropic usage policies,
- Anthropic computer-use/tool-use restrictions,
- any model provider's cyber safety policy,
- any model provider's agent/tool access requirements.

No document in this package assumes that restricted provider access is available.

## Platform Constraints

Before any future prototype implementation discussion, verify current rules for:

- operating system permissions,
- browser automation permissions,
- cloud provider terms,
- GitHub or repository automation terms,
- local file access boundaries,
- keychain or credential access rules,
- logging and telemetry behavior,
- dependency download behavior.

## Tool-Use Constraints

The first prototype boundary remains:

```text
NO_NETWORK
NO_LIVE_INTEGRATIONS
NO_REAL_SYSTEM_EFFECT
NO_SECURITY_AGENT_BEHAVIOR
NO_ACTIVE_SCANNING
NO_AUTOMATED_REMEDIATION
NO_PROVIDER_RESTRICTED_CAPABILITY_ASSUMED
```

Any proposal to add tool use must trigger:

```text
STOP_CAPABILITY_CHANGE
NEEDS_CAPABILITY_REVIEW
```

## Cyber Safety Constraints

The model must not assume permission for:

- vulnerability scanning,
- exploit testing,
- malware analysis with live samples,
- credential testing,
- phishing simulation,
- active reconnaissance,
- automated remediation,
- live incident response,
- security-tool orchestration,
- agentic cyber workflows.

Any future cyber-related capability must be reviewed as high risk or critical.

## Responsible Disclosure Constraint

If future work ever discovers a real vulnerability, real secret exposure, real misconfiguration, or real security issue, it must not be handled as an autonomous AI action.

It must route to:

```text
INCIDENT_REVIEW_REQUIRED
ROLE_SECURITY_REVIEWER
ROLE_INCIDENT_REVIEWER
responsible disclosure review
```

## Documentation Constraint

The documentation may say:

```text
The model is designed to account for provider and platform constraints.
```

The documentation must not say:

```text
The model is approved by providers.
The model has access to restricted cyber capabilities.
The model is a security agent.
The model can perform live cyber defense.
The model can scan or remediate real systems.
```

## Review Requirement

Before any prototype implementation discussion, reviewers should answer:

- Are provider constraints current?
- Are tool-use constraints current?
- Are cyber policy constraints current?
- Does the prototype still avoid security-agent behavior?
- Does the prototype still avoid real system effect?
- Does any proposed capability require provider approval?
- Does any proposed capability require legal/security review?

## Current Decision

This document strengthens the freeze boundary.

It does not reopen model expansion.

It does not authorize implementation.

It confirms that the current safe path remains:

```text
documentation freeze
external review
synthetic decision-simulator discussion only after review
```
