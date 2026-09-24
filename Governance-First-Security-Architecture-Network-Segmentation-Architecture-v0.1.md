# Governance-First Security Architecture
## Network Segmentation Architecture
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This document defines the governance requirements and architectural principles for network segmentation within the governed environment. Segmentation is the structural mechanism that limits lateral movement, contains blast radius, and enforces trust boundaries at the network layer. A governance framework without defined segmentation principles is a set of policies with no structural enforcement.

This document provides the architectural governance layer. Implementation details — specific VLAN configurations, firewall rule sets, cloud security group definitions — are implementation artefacts governed by this framework but not defined within it.

---

## 2. Scope

Applies to all network environments operated by or on behalf of the organisation: on-premises infrastructure, cloud environments, hybrid architectures, container networking, and agentic AI system network access. Applies equally to physical and virtual network boundaries.

---

## 3. Core Governance Principle

> **Segments are trust boundaries, not convenience groupings. A segment boundary means that traffic crossing it is inspected, logged, and controlled by explicit policy — not permitted by default. The default posture between any two segments is deny. Permit rules are exceptions that require justification, ownership, and review.**

---

## 4. Segment Classification

The governed environment is divided into segments based on the trust level and risk profile of the systems and data within them:

| Segment | Contents | Trust Level | Default Posture |
|---|---|---|---|
| External | Internet-facing systems, public APIs, CDN endpoints | Untrusted | Deny all inbound except defined service ports |
| DMZ | Systems that must accept external connections and communicate with internal systems | Semi-trusted | Strict allow-list in both directions |
| Application | Internal application servers, APIs, microservices | Internal trusted | Least-privilege allow-list; no direct internet access |
| Data | Databases, data stores, object storage, backup targets | Sensitive | Application segment only; no direct user access |
| Management | Administrative interfaces, privileged access jump hosts, monitoring infrastructure | Privileged | PAM-gated access only; highest inspection |
| AI And Agentic | AI inference infrastructure, agentic system runtime environments, model storage | Controlled | Defined tool access list per Agentic Operational Boundary; egress via approved channels only |
| Identity | Identity providers, certificate authorities, secret management systems | Critical | Tier 0 access controls; near-total isolation |
| Development And Test | Non-production environments | Isolated | No production data; no production credential access; no connectivity to production segments |

---

## 5. Segment Boundary Requirements

### 5.1 All Segment Boundaries
- All traffic crossing a segment boundary is logged
- Default posture is deny; all permit rules are explicit, documented, and owned
- Permit rules are reviewed at minimum annually and following any significant architecture change
- Unused permit rules are removed; a rule with no observed traffic for 90 days is reviewed for removal

### 5.2 Data Segment
- No direct user workstation access to the Data segment; access is via Application segment only
- Bulk data export from the Data segment requires authorisation per Data Classification And Handling Policy
- Data segment egress is monitored for volume anomalies per Data Egress And Exfiltration Prevention

### 5.3 AI And Agentic Segment
- Agentic systems are network-isolated from segments they do not operationally require
- External API calls from the AI And Agentic segment are proxied through an inspecting egress gateway
- The egress gateway enforces the Operational Mandate allow-list for each agentic system
- Agentic system network access is logged at the connection level, not only at the application level
- A new agentic system deployment requires a documented network access profile before activation

### 5.4 Management Segment
- Management segment access is exclusively via PAM-gated privileged access per Privileged Access Management Policy
- No application or agentic system has direct access to the Management segment
- Management segment traffic is fully logged and subject to session recording

### 5.5 Identity Segment
- The Identity segment is the most isolated segment in the architecture
- No system outside the Identity segment initiates connections to it except through defined, audited authentication protocols
- Changes to Identity segment configuration require Tier 0 privileged access and four-eyes approval

### 5.6 Development And Test Segment
- Development and test environments are fully isolated from production segments
- Production data does not enter development or test segments without explicit anonymisation or synthetic data substitution
- Production credentials do not exist in development or test environments
- A development system that has ever had production data or production credential access is treated as a production system for security purposes until confirmed clean

---

## 6. Micro-Segmentation For Agentic Systems

Agentic systems with distinct operational mandates are isolated from each other within the AI And Agentic segment. An agentic system compromised through prompt injection or model manipulation cannot reach another agentic system's runtime, memory, or tool access by default.

- Each agentic system deployment has a defined network identity
- Inter-agent communication is explicit and logged; it is not a default-permitted path within the segment
- Sub-agent invocation crosses a logical boundary that is governed by the Agentic Operational Boundary authority transfer rules

---

## 7. Segmentation Testing And Validation

- Segmentation controls are validated at minimum annually through penetration testing or equivalent
- Segmentation validation specifically tests: can a compromised Application segment system reach the Data segment directly? Can a compromised agentic system reach the Identity segment? Can a Development segment system reach Production?
- Segmentation gaps found in testing are findings tracked in Vulnerability Disclosure And Patch Governance with High minimum severity
- Segmentation architecture is reviewed following any significant infrastructure change before the change goes to production

---

## 8. Cloud And Hybrid Environments

Cloud environments implement segmentation through equivalent controls: VPCs, security groups, network ACLs, service mesh policies. The governance requirements are identical; the implementation mechanisms are cloud-native.

- Cloud segmentation design is reviewed before deployment under the Capability Change Gate
- Cloud provider network controls are not assumed to be equivalent to on-premises controls without documented assessment
- Hybrid environments — where on-premises and cloud segments are connected — treat the connection boundary as a high-risk segment crossing requiring explicit governance

---

## 9. Related Documents

- Lateral Movement Containment Policy
- Trust Boundaries
- Ingress Egress Policy
- Data Egress And Exfiltration Prevention
- Privileged Access Management Policy
- Agentic Operational Boundary
- Identity And Credential Governance
- Vulnerability Disclosure And Patch Governance
- Capability Change Gate
- Log Integrity And Tamper-Evidence Policy
