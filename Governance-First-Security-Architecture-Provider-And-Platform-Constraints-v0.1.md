# Governance-First Security Architecture
## Provider And Platform Constraints
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy
**Document Owner:** Martin Dahl

---

## 1. Purpose

This document defines the governance requirements for identifying, verifying, and monitoring the constraints imposed by AI providers, platforms, and applicable policies on any use of the Governance-First Security Architecture.

The core problem this document addresses is asymmetric assumption: a governance framework can be technically well-designed but operationally blocked by provider policy, platform terms, or legal requirements that were not checked. Technical possibility is not the same as permitted use. This document defines the process for closing that gap before any capability discussion reaches the implementation stage.

This document does not open capabilities. It governs the process by which capabilities are assessed for permission before they are proposed.

---

## 2. Scope

Applies to:
- Any discussion of prototype implementation or capability expansion
- Any use of AI provider APIs (OpenAI, Anthropic, or any future provider)
- Any use of platform capabilities (operating system, browser, cloud, repository automation)
- Any agentic tool-use capability, regardless of scope
- Any cyber-adjacent capability, including synthetic or simulated scenarios

Does not apply to:
- Documentation-only work that does not involve AI provider API calls or platform execution
- Internal governance review and revision that produces no external system effects

---

## 3. Core Principle

```text
No capability assumption without provider, platform, policy, and legal review.
Technical possibility is not permitted use.
```

This principle applies at every stage: design discussion, prototype planning, and implementation. A capability that has not been verified against current provider and platform policy is not an available capability — regardless of its technical feasibility.

---

## 4. Constraint Categories

### 4.1 AI Provider Constraints

AI providers (OpenAI, Anthropic, and others) publish usage policies that define permitted and prohibited uses of their models and APIs. These policies:

- Change over time without notice
- May differ between API access tiers and model versions
- May require special approval or trusted-access status for certain capability categories
- May prohibit certain uses regardless of technical safeguards in place

Constraint categories requiring explicit provider policy verification before any capability discussion:

| Capability Category | Risk Level | Verification Requirement |
|---|---|---|
| Agentic tool use (any tool that acts on systems) | Critical | Verify current provider policy; confirm no prohibited use |
| Cyber security operations (scanning, testing, remediation) | Critical | Verify current provider policy; assume prohibited unless explicitly confirmed |
| Automated decision-making with real-world effects | Critical | Verify current provider policy; legal review required |
| Computer use / browser automation | High | Verify current provider policy per model and API tier |
| High-stakes domain operation (medical, legal, financial) | High | Verify current provider policy; additional legal review likely required |
| Bulk data processing involving personal data | High | Verify data processing terms; GDPR assessment required |
| Standard API use for synthetic/mock scenarios | Low | Confirm use remains within documented synthetic boundary |

### 4.2 Platform Constraints

Platform constraints govern what the execution environment permits. These include:

- Operating system permission boundaries (file access, process spawning, network access)
- Browser automation terms and technical restrictions
- Cloud provider acceptable use policies
- Repository and CI/CD platform automation terms (GitHub Actions, etc.)
- Local credential and keychain access rules
- Logging, telemetry, and data residency requirements

Platform constraints must be verified against the specific platform version and configuration in use. A constraint that was absent in a previous platform version may be present in a current one.

### 4.3 Cyber Safety Constraints

The following capability categories are prohibited unless explicitly authorised through the Capability Change Gate with provider policy confirmation and legal review:

```text
Prohibited without explicit authorisation:
───────────────────────────────────────────────
- Vulnerability scanning (active or passive)
- Exploit testing or proof-of-concept execution
- Malware analysis with live samples
- Credential testing or brute-force simulation
- Phishing simulation against real targets
- Active network reconnaissance
- Automated remediation on real systems
- Live incident response automation
- Security-tool orchestration with real-system effects
- Agentic cyber workflows with any real-system effect
```

Synthetic, mock, or simulated scenarios that produce no real-system effect are permitted within the documented prototype boundary. The distinction between synthetic and real must be explicit and verifiable — not assumed.

### 4.4 Responsible Disclosure Constraint

If any work under this architecture discovers a real vulnerability, real secret exposure, real misconfiguration, or real security issue — in any system, including systems used in testing — the finding must not be handled as an autonomous AI action.

Mandatory routing:

```text
INCIDENT_REVIEW_REQUIRED
ROLE: Security Reviewer
ROLE: Incident Reviewer
PROCESS: Responsible disclosure review per Vulnerability-Disclosure-And-Patch-Governance
```

No AI system may make a disclosure decision. No AI system may suppress a disclosure finding.

---

## 5. Current Prototype Boundary

The current authorised prototype boundary, consistent with the Prototype Design Readiness Checklist and PDG-028:

```text
Authorised prototype type:  Synthetic governance decision simulator
Not authorised:             Security agent, live integrations, real system effects

Active constraints:
  NO_NETWORK
  NO_LIVE_INTEGRATIONS
  NO_REAL_SYSTEM_EFFECT
  NO_SECURITY_AGENT_BEHAVIOR
  NO_ACTIVE_SCANNING
  NO_AUTOMATED_REMEDIATION
  NO_PROVIDER_RESTRICTED_CAPABILITY_ASSUMED
```

Any proposal to add tool use or expand the prototype boundary triggers:

```text
STOP_CAPABILITY_CHANGE → NEEDS_CAPABILITY_REVIEW
```

This routes to the Capability Change Gate, which requires provider policy verification as part of its assessment.

---

## 6. Verification Process

Provider and platform constraints must be verified before any capability discussion that involves API calls, tool use, or platform execution. Verification is not a one-time event — policies change, and a prior verification does not cover a later capability discussion.

### 6.1 Verification Steps

1. **Identify the capability category** using Section 4.1 and 4.2
2. **Retrieve current policy** directly from the provider’s primary policy source (not cached or secondary sources)
3. **Assess permission status** against the specific use case, model, and API tier in use
4. **Identify any approval requirement** (special access, trusted partner status, legal agreement)
5. **Document the verification** in the Provider Constraint Verification Log (Section 6.2)
6. **Route to legal review** if the capability category requires it (Section 4.1)
7. **Confirm or block** the capability discussion based on verification outcome

### 6.2 Provider Constraint Verification Log

Each verification is recorded as a log entry:

| Field | Description |
|---|---|
| Entry ID | Sequential identifier (PCV-YYYY-NNN) |
| Date | Date verification was performed |
| Capability assessed | Specific capability or use case being assessed |
| Provider / platform | Which provider or platform policy was checked |
| Policy source URL | Direct link to the policy document checked |
| Policy version / date | Version or last-updated date of the policy checked |
| Permission status | Permitted / Prohibited / Requires approval / Unclear |
| Conditions | Any conditions, restrictions, or approval requirements |
| Legal review required | Yes / No |
| Decision | Capability discussion proceeds / blocked / deferred |
| Decided by | Named governance authority |

Verification log entries expire after 90 days. A capability discussion that relies on an expired verification entry must re-verify before proceeding.

---

## 7. Policy Change Monitoring

Provider and platform policies are time-sensitive. A capability that is permitted today may be prohibited tomorrow. The following monitoring requirements apply:

- Registered provider policy sources are checked for material changes at minimum quarterly
- Any provider announcement of policy update triggers an immediate review of active capability assumptions
- The Threat Intelligence Intake process includes regulatory and provider policy updates as a recognised intelligence category
- If a policy change restricts a previously permitted capability, the Capability Change Gate must be triggered to assess impact on the current architecture

### 7.1 Registered Policy Sources

The following sources are the authoritative policy references for this architecture. These must be checked at current source — not cached versions — before any capability verification:

| Provider / Platform | Policy Document | Primary URL |
|---|---|---|
| OpenAI | Usage Policies | https://openai.com/policies/usage-policies/ |
| OpenAI | API Terms of Service | https://openai.com/policies/terms-of-use/ |
| Anthropic | Acceptable Use Policy | https://www.anthropic.com/legal/aup |
| Anthropic | Usage Policy | https://www.anthropic.com/legal/usage-policy |
| GitHub | Acceptable Use Policies | https://docs.github.com/en/site-policy/acceptable-use-policies |

Additional providers or platforms must be registered here before their capabilities are discussed. Unregistered providers are not available capabilities.

---

## 8. Constraint Assessment for New Capabilities

When a new capability is proposed — at any stage from design discussion to implementation — the following assessment must be completed before the capability proceeds:

| Assessment Question | If Yes | If No |
|---|---|---|
| Does this capability involve any AI provider API call? | Verify Section 4.1 constraints | Proceed to next question |
| Does this capability involve any platform execution? | Verify Section 4.2 constraints | Proceed to next question |
| Does this capability fall into a cyber safety category? | Block; require explicit authorisation per Section 4.3 | Proceed to next question |
| Does this capability involve real data, real systems, or real-world effects? | Legal review required; route to Governance Authority | Proceed to next question |
| Does this capability require provider special access or approval? | Obtain written confirmation before proceeding | Proceed |
| Has the relevant provider policy been checked within the last 90 days? | Proceed with documented verification | Re-verify before proceeding |

No capability clears this assessment by default. Each question must be answered explicitly.

---

## 9. Documentation Language Constraint

The documentation may state:

```text
The architecture is designed to account for provider and platform constraints.
Capability discussions are subject to provider policy verification.
```

The documentation must not state:

```text
The model is approved by providers.
The model has access to restricted cyber capabilities.
The model is a security agent.
The model can perform live cyber defence.
The model can scan or remediate real systems.
Provider policy has been verified for [specific implementation].
```

The last prohibition is particularly important: a general documentation-boundary review is not a verified permission for a specific implementation. These are different claims and must never be conflated.

---

## 10. Current Verification State

```text
Provider policy review for documentation boundary:  PERFORMED (2026-08-15)
Provider permission verification for implementation: NOT PERFORMED
Platform permission verification for implementation: NOT PERFORMED
Implementation authorisation:                        NOT GRANTED
Next scheduled policy review:                        2026-11-26 (90 days)
```

This verification state confirms that the current documentation boundary is consistent with provider policies as reviewed. It does not confirm that any implementation is permitted. A new verification is required before any implementation capability discussion.

---

## 11. Review Schedule

| Review Type | Frequency | Owner | Output |
|---|---|---|---|
| Provider policy source check | Quarterly | AI Operator / Governance Authority | Confirm no material policy changes; update verification state |
| Constraint assessment for new capability | Per capability proposal | Governance Authority | PCV log entry; capability decision |
| Full constraint document review | At each major version or significant provider policy change | Governance Authority | Updated registered sources; updated constraint categories |

---

## 12. Related Documents

- Capability-Change-Gate
- Prototype-Design-Readiness-Checklist (PDG-008, PDG-009)
- Vulnerability-Disclosure-And-Patch-Governance
- Threat-Intelligence-Intake
- GDPR-And-EU-AI-Act-Alignment
- Minimal-Viable-Governance-Kernel
- Stop-State-Policy
- Agentic-Operational-Boundary

---

*This document is part of the Governance-First Security Architecture. Before AI is allowed to act, someone must be accountable.*
