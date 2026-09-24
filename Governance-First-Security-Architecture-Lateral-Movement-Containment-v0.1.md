# Governance-First Security Architecture
## Lateral Movement Containment Policy
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy governs the containment of attacker movement within the environment after an initial compromise has occurred. Perimeter controls and initial authentication are necessary but insufficient — an attacker who has gained a foothold in any system must be constrained in their ability to move laterally to other systems, escalate privilege, or reach high-value assets.

Lateral movement containment is a governance problem, not only a technical one: it requires explicit decisions about which systems may communicate with which, who may approve exceptions, and what triggers mandatory isolation.

---

## 2. Scope

Applies to all systems, services, and network segments within the environment, including cloud infrastructure, on-premises systems, third-party integrations, and any system reachable from within the environment.

---

## 3. Core Governance Principle

> **Default deny for east-west traffic. Systems communicate only with systems they are explicitly authorised to communicate with. Authorisation requires a documented business justification, a named owner, and a defined review date.**

This inverts the typical default: instead of allowing internal traffic and blocking known-bad, all internal traffic is blocked by default and allowed only where explicitly justified.

---

## 4. Segmentation Model

### 4.1 Segment Classification

All systems are assigned to a segment. Segments define the trust boundary within which default-allow traffic may flow. Cross-segment traffic requires explicit governance authorisation.

| Segment Class | Description | Examples |
|---|---|---|
| Public-facing | Directly reachable from the internet | Web servers, API gateways, CDN origins |
| Application | Internal application logic | App servers, microservices, APIs |
| Data | Persistent data storage | Databases, data lakes, object storage |
| Identity | Credential and authentication infrastructure | Identity providers, secret stores, PKI |
| Management | Administrative and operational systems | Bastion hosts, monitoring, CI/CD |
| AI/Agentic | AI model inference and agentic runtime systems | LLM endpoints, agent orchestrators |

### 4.2 Cross-Segment Communication Rules

- Public-facing → Application: Permitted with ingress control (see Ingress Egress Policy)
- Application → Data: Permitted only on explicitly authorised connection strings with scoped credentials
- Application → Identity: Permitted for authentication flows only; read-only where possible
- Management → Any: Permitted only from designated management networks; all sessions logged
- Any → Management: Denied; management access is outbound-only from management segment
- AI/Agentic → Data or Identity: Requires explicit per-capability authorisation reviewed quarterly

---

## 5. Lateral Movement Indicators

The following patterns are defined as lateral movement indicators and trigger mandatory investigation:

- Authentication attempts from a system to a system outside its authorised communication list
- Credential use from an IP address or hostname not associated with that credential's expected context
- Port scanning or service enumeration originating from an internal system
- New outbound connections from systems with no history of outbound connections
- Credential use at unusual hours not consistent with established behaviour baseline
- Use of administrative tools (PsExec, WMI, remote PowerShell, SSH from unexpected sources) from non-management systems
- Access to the Identity segment from Application or Data segments outside of defined authentication flows

---

## 6. Mandatory Isolation Triggers

The following conditions trigger mandatory isolation of the affected system, defined as removing all network connectivity except for forensic collection channels:

- Confirmed malware or attacker tooling detected on a system
- Lateral movement indicator confirmed as malicious (not false positive) after initial investigation
- Credential confirmed as compromised and used from an unexpected source
- System observed communicating with known command-and-control infrastructure
- System found to have been modified outside of the Change Gate process

Isolation authority: any Security Operations role may isolate; re-connection requires named approval from Security Governance role and documented justification.

---

## 7. Privileged Access Governance (East-West)

- Administrative credentials must not be reused across segments
- Domain administrator or equivalent credentials must not be used on systems in the Public-facing segment under any circumstances
- Privileged sessions must be proxied through a session recording system where technically feasible
- Just-in-time access must be used for cross-segment privileged operations where the technology supports it; standing privileged access is a finding requiring remediation
- Service accounts must have network access scoped to only the systems they serve

---

## 8. Break-Glass Authorisation

Where emergency access across segment boundaries is required outside of normal processes:

1. Named individual requests break-glass access, providing specific justification
2. Second named individual from a different role approves
3. All session activity is recorded and reviewed within 24 hours
4. Break-glass event is logged in Audit and Accountability as a Stop State candidate
5. Permanent exception review occurs within 5 business days

---

## 9. Segmentation Review

- Segmentation rules are reviewed quarterly by the Security Governance role
- Any change to segmentation rules follows the Capability Change Gate process
- Penetration testing must include lateral movement scenarios at minimum annually
- Results of lateral movement testing feed into the Synthetic Test Case Set and Risk and Action Taxonomy

---

## 10. Related Documents

- Ingress Egress Policy
- Trust Boundaries
- Identity And Credential Governance
- Stop State Policy
- Audit And Accountability
- Capability Change Gate
- AI Human Governance
