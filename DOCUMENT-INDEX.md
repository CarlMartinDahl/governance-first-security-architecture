# Document Index

This index organizes the complete Governance-First Security Architecture review package.

The package is documentation-only. Inclusion in this index does not imply implementation, validation, production readiness, or a security or compliance claim.

## Start Here

- [README](README.md) - Project thesis, status, reading paths, and contribution boundary.
- [Executive Overview](Governance-First-Security-Architecture-Executive-Overview-v0.1.md) - Short first-read overview.
- [Technical Review Brief](Governance-First-Security-Architecture-Technical-Review-Brief-v0.1.md) - Deeper conceptual and technical framing.
- [Documentation Freeze And Review Gate](Governance-First-Security-Architecture-Documentation-Freeze-And-Review-Gate-v0.1.md) - Current freeze and authorization boundary.

## Governance Kernel And Canonical Model

- [Minimal Viable Governance Kernel](Governance-First-Security-Architecture-Minimal-Viable-Governance-Kernel-v0.1.md) - Smallest proposed governance rule set.
- [Mode Model Normalization](Governance-First-Security-Architecture-Mode-Model-Normalization-v0.1.md) - Lifecycle and operational mode vocabulary.
- [Stop-State Registry](Governance-First-Security-Architecture-Stop-State-Registry-v0.1.md) - Canonical stop, review, lockdown, and incident states — including agentic stops for authority chain failure, identity mismatch, unsanctioned inter-agent communication, and emergent swarm behaviour.
- [Decision-State Matrix](Governance-First-Security-Architecture-Decision-State-Matrix-v0.1.md) - Mapping from governance signals to decisions.
- [Role Registry](Governance-First-Security-Architecture-Role-Registry-v0.1.md) - Role, authority, review, approval, and accountability boundaries.
- [Roles And Responsibilities](Governance-First-Security-Architecture-Roles-And-Responsibilities-v0.1.md) - Competence profiles, staffing requirements, and independence requirements for all governance roles. Addresses Gap S (sign-off authority concentration).
- [Asset-To-Kernel Mapping](Governance-First-Security-Architecture-Asset-To-Kernel-Mapping-v0.1.md) - Asset categories mapped to governance defaults.

## Security And Risk Foundations

- [Threat Model](Governance-First-Security-Architecture-Threat-Model-v0.1.md) - Threat actors, misuse paths, assets, and boundaries — including agentic threat taxonomy, emergent swarm behaviour, and multi-model hybrid attack patterns.
- [Asset Register](Governance-First-Security-Architecture-Asset-Register-v0.1.md) - Data, credentials, decisions, context, capabilities, and records.
- [Trust Boundaries](Governance-First-Security-Architecture-Trust-Boundaries-v0.1.md) - Human, AI, tool, authority, data, and integration boundaries.
- [Risk And Action Taxonomy](Governance-First-Security-Architecture-Risk-And-Action-Taxonomy-v0.1.md) - Risk levels, action classes, escalation, and hard blocks.
- [Abuse Case Library](Governance-First-Security-Architecture-Abuse-Case-Library-v0.1.md) - Misuse and attack scenarios for review.
- [Supply Chain Abuse Cases](Governance-First-Security-Architecture-Supply-Chain-Abuse-Cases-v0.1.md) - Third-party, supplier, and supply chain attack scenarios including agentic AI threats.

## Governance Policies

- [Ingress Egress Policy](Governance-First-Security-Architecture-Ingress-Egress-Policy-v0.1.md) - Entry, exit, export, containment, and fail-closed rules.
- [Evidence And Source Policy](Governance-First-Security-Architecture-Evidence-And-Source-Policy-v0.1.md) - Authority, freshness, sufficiency, conflicts, and counter-evidence.
- [AI-Human Governance](Governance-First-Security-Architecture-AI-Human-Governance-v0.1.md) - Recommendation, review, approval, override, and accountability.
- [Capability Change Gate](Governance-First-Security-Architecture-Capability-Change-Gate-v0.1.md) - Governance required before capability expansion.
- [Stop-State Policy](Governance-First-Security-Architecture-Stop-State-Policy-v0.1.md) - Earlier policy-level stop and blocked outcomes.
- [Audit And Accountability](Governance-First-Security-Architecture-Audit-And-Accountability-v0.1.md) - Decision records, approval chains, AI assistance, and traceability.
- [Recovery Rollback Incidents](Governance-First-Security-Architecture-Recovery-Rollback-Incidents-v0.1.md) - Freeze, isolation, rollback, incident review, and recovery.
- [Third-Party Governance](Governance-First-Security-Architecture-Third-Party-Governance-v0.1.md) - Supplier authority, access lifecycle, scope boundaries, and compromised third-party response.
- [Identity And Credential Governance](Governance-First-Security-Architecture-Identity-And-Credential-Governance-v0.1.md) - Credential lifecycle, scope minimisation, rotation, revocation, and compromise response.
- [Continuous Validation Policy](Governance-First-Security-Architecture-Continuous-Validation-Policy-v0.1.md) - Ongoing session trust, revalidation schedule, agentic actor controls, and fail-closed default.
- [Vendor Offboarding And Revocation](Governance-First-Security-Architecture-Vendor-Offboarding-And-Revocation-v0.1.md) - Planned and emergency vendor offboarding, credential confirmation, and residual access checks.
- [Social Engineering And Human Manipulation Policy](Governance-First-Security-Architecture-Social-Engineering-Policy-v0.1.md) - Verification tiers, BEC controls, SIM-swapping response, deepfake governance, and out-of-band confirmation requirements.
- [Secrets Sprawl And Hardcoded Credentials Policy](Governance-First-Security-Architecture-Secrets-Sprawl-And-Hardcoded-Credentials-v0.1.md) - Secret lifecycle, prohibited patterns, rotation schedules, CI/CD pipeline governance, and remediation workflow.
- [Lateral Movement Containment Policy](Governance-First-Security-Architecture-Lateral-Movement-Containment-v0.1.md) - Default-deny east-west traffic, segment classification, lateral movement indicators, mandatory isolation triggers, and break-glass authorisation. See also CA-06 Lateral Peer Coordination Rule.
- [Log Integrity And Tamper-Evidence Policy](Governance-First-Security-Architecture-Log-Integrity-And-Tamper-Evidence-v0.1.md) - Write-once log forwarding, immutability controls, absence-as-alert, forensic preservation, and retention requirements.
- [Log Retention And Rotation Policy](Governance-First-Security-Architecture-Log-Retention-And-Rotation-Policy-v0.1.md) - Retention periods by log type, rotation triggers and procedure, authorised deletion workflow, capacity planning, and regulatory alignment (EU AI Act, GDPR, NIS2).
- [Ransomware Recovery Policy](Governance-First-Security-Architecture-Ransomware-Recovery-Policy-v0.1.md) - 3-2-1-1 backup architecture, payment decision governance, containment phases, sanctions screening, GDPR notification obligations, and recovery process.
- [Vulnerability Disclosure And Patch Governance](Governance-First-Security-Architecture-Vulnerability-Disclosure-And-Patch-Governance-v0.1.md) - Inbound responsible disclosure, safe harbour, patch remediation windows, zero-day protocol, dependency scanning, and vulnerability register.
- [Data Classification And Handling Policy](Governance-First-Security-Architecture-Data-Classification-And-Handling-Policy-v0.1.md) - Four-tier classification (Public/Internal/Confidential/Restricted), handling requirements per tier, GDPR overlay, AI data governance, and breach impact mapping.
- [Privileged Access Management Policy](Governance-First-Security-Architecture-Privileged-Access-Management-Policy-v0.1.md) - Privileged account tiers, account separation, just-in-time access, session recording, break-glass governance, and insider threat indicators.
- [Insider Threat Governance](Governance-First-Security-Architecture-Insider-Threat-Governance-v0.1.md) - Structural blast-radius controls, separation of duties, four-eyes principle, offboarding risk window, negligence vs. malice framework, and GDPR monitoring constraints.
- [Cryptographic Standards Policy](Governance-First-Security-Architecture-Cryptographic-Standards-Policy-v0.1.md) - Approved and prohibited algorithms, TLS requirements, password hashing standards, certificate governance, key management, and post-quantum transition alignment.
- [Security Awareness And Training Governance](Governance-First-Security-Architecture-Security-Awareness-And-Training-Governance-v0.1.md) - Role-differentiated training requirements, phishing simulation governance, effectiveness metrics, non-completion consequences, and post-incident training response.
- [Agentic Operational Boundary](Governance-First-Security-Architecture-Agentic-Operational-Boundary-v0.1.md) - Action authority tiers (Autonomous/Confirm/Escalate/Stop), Operational Mandate requirements, tool use governance, memory and persistence controls, multi-agent pipeline governance, and prompt injection response.
- [Business Continuity And Disaster Recovery Governance](Governance-First-Security-Architecture-Business-Continuity-And-Disaster-Recovery-Governance-v0.1.md) - RTO/RPO/MTO definitions, system criticality tiers, continuity strategy requirements, disaster declaration governance, continuity testing programme, and return-to-normal criteria.
- [Data Egress And Exfiltration Prevention](Governance-First-Security-Architecture-Data-Egress-And-Exfiltration-Prevention-v0.1.md) - Egress classification per data tier, approved egress channels, agentic system egress controls, derived data classification, exfiltration detection indicators, and GDPR cross-border transfer governance.
- [Network Segmentation Architecture](Governance-First-Security-Architecture-Network-Segmentation-Architecture-v0.1.md) - Eight-segment classification (including dedicated AI And Agentic segment), default-deny boundary posture, micro-segmentation for agentic systems, inspecting egress gateway, and segmentation validation requirements.
- [AI Model And Supply Chain Integrity](Governance-First-Security-Architecture-AI-Model-And-Supply-Chain-Integrity-v0.1.md) - Model provenance requirements, cryptographic integrity verification, training data poisoning controls, weight file integrity, behavioural drift monitoring, agentic reasoning model integrity, model integrity incident response, and trigger surface map sign-off requirement (Gap O remediation).
- [Agentic Identity Security — Conceptual Foundation](Governance-First-Security-Architecture-Agentic-Identity-Security-Conceptual-Foundation-v0.1.md) - Agent constitutional core, authority chain verification, cognitive reset protocol, and the layer switch from hostile agent to intelligence asset. Forms a containment system with the Deceptive Containment Environment.
- [Deceptive Containment Environment — Conceptual Foundation](Governance-First-Security-Architecture-Deceptive-Containment-Environment-Conceptual-Foundation-v0.1.md) - Sandbox isolation combined with digital twin fidelity for real-time intelligence extraction from hostile AI agents and multi-agent swarms. Forms a containment system with Agentic Identity Security.

## Private AI Deployment And Operations

- [Private AI Deployment Guide](Governance-First-Security-Architecture-Private-AI-Deployment-Guide-v0.1.md) - Five-phase deployment lifecycle (provision, configure, harden, validate, hand-off), governance gate table, air-gap variant, and sign-off requirements.
- [System Prompt Governance Layer](Governance-First-Security-Architecture-System-Prompt-Governance-Layer-v0.1.md) - Permitted and prohibited system prompt content, authorship and approval workflow, version control and signing requirements, runtime injection resistance, and five mandatory validation tests.
- [Agent Baseline Profile](Governance-First-Security-Architecture-Agent-Baseline-Profile-v0.1.md) - Five-dimension baseline structure (identity, capability, interaction, resource, temporal), establishment procedure with supervised observation period, risk-differentiated observation requirements (Gap P remediation), anomaly severity mapping, and quarterly review schedule.
- [Monitoring And Detection Operations](Governance-First-Security-Architecture-Monitoring-And-Detection-Operations-v0.1.md) - Four-component monitoring architecture, ten hard rules, eight threshold rules, six pattern rules, triage procedure, coverage requirements, monitoring failure stop conditions, and Confirm mode exit threshold (Gap Q remediation).

## Incident Response And Recovery

- [Agent Attribution Playbook](Governance-First-Security-Architecture-Agent-Attribution-Playbook-v0.1.md) - Evidence collection, three confidence levels (Suspected/Probable/Confirmed), attribution record template, special cases (prompt injection, supply chain, multi-agent, attribution failure).
- [Attribution SLA Policy](Governance-First-Security-Architecture-Attribution-SLA-Policy-v0.1.md) - Four severity tiers (SEV-1 to SEV-4) with time-bound milestones per role, SLA breach procedure, evidence degradation windows, and evidence adjudication authority.
- [Active Neutralization Runbook](Governance-First-Security-Architecture-Active-Neutralization-Runbook-v0.1.md) - Four neutralization tracks with authorisation requirements, deceptive containment integration, downstream agent handling, and decision matrix.
- [Recovery Rollback Incidents](Governance-First-Security-Architecture-Recovery-Rollback-Incidents-v0.1.md) - Five recovery classes (Agent Replacement through Full Clean Rebuild), root-cause-before-restoration principle, downstream impact remediation, and ten-point return-to-normal checklist.

## Legal, Provider, And Future Readiness

- [GDPR And EU AI Act Alignment](Governance-First-Security-Architecture-GDPR-EU-AI-Act-Alignment-v0.1.md) - Alignment goals without compliance claims.
- [Provider And Platform Constraints](Governance-First-Security-Architecture-Provider-And-Platform-Constraints-v0.1.md) - Time-sensitive policy, platform, tool-use, and cyber constraints. Note: platform-specific content in this document may become outdated as provider policies evolve; verify against current provider documentation before use.
- [Post-Quantum And Future AI Readiness](Governance-First-Security-Architecture-Post-Quantum-And-Future-AI-Readiness-v0.1.md) - Crypto-agility and future capability reassessment.

## Test And Design-Only Material

- [Test Plan](Governance-First-Security-Architecture-Test-Plan-v0.1.md) - Safe governance-control test categories.
- [Synthetic Test Case Set](Governance-First-Security-Architecture-Synthetic-Test-Case-Set-v0.1.md) - Synthetic-only test cases.
- [Implementation Roadmap](Governance-First-Security-Architecture-Implementation-Roadmap-v0.1.md) - Historical staged path with implementation still unauthorized.
- [Prototype Boundary Definition](Governance-First-Security-Architecture-Prototype-Boundary-Definition-v0.1.md) - No-network, no-real-data, no-real-effect boundary.
- [Prototype Design Readiness Checklist](Governance-First-Security-Architecture-Prototype-Design-Readiness-Checklist-v0.1.md) - Preconditions for design discussion.
- [Prototype Design Sketch](Governance-First-Security-Architecture-Prototype-Design-Sketch-v0.1.md) - Design-only synthetic simulator sketch.
- [Prototype Data Schema](Governance-First-Security-Architecture-Prototype-Data-Schema-v0.1.md) - Synthetic test and mock-decision schema.
- [Prototype Review Request](Governance-First-Security-Architecture-Prototype-Review-Request-v0.1.md) - Focused request for boundary critique.

## External Review And Revision

- [External Review Checklist](Governance-First-Security-Architecture-External-Review-Checklist-v0.1.md) - Questions for critical external review.
- [Internal Consistency Review](Governance-First-Security-Architecture-Internal-Consistency-Review-v0.1.md) - Internal contradictions, cleanup findings, and historical review state.
- [External Review Package Manifest](Governance-First-Security-Architecture-External-Review-Package-Manifest-v0.1.md) - Suggested reviewer subsets and outputs.
- [External Reviewer Message Pack](Governance-First-Security-Architecture-External-Reviewer-Message-Pack-v0.1.md) - Role-based review requests.
- [Security Reviewer Bundle](Security-Reviewer-Bundle-v0.1.md) - Security-oriented review path.
- [Technical Reviewer Bundle](Technical-Reviewer-Bundle-v0.1.md) - Senior technical review path.
- [Post-Review Revision Log](Governance-First-Security-Architecture-Post-Review-Revision-Log-v0.1.md) - Anonymized feedback, decisions, and traceability.

## Gap Responses

Documents produced in direct response to identified gaps from external review. Each document is linked to a specific gap finding in the Post-Review Revision Log.

- [CA-06 Lateral Peer Coordination Rule](Governance-First-Security-Architecture-CA-06-Lateral-Peer-Coordination-Rule-v0.1.md) - Control rule governing lateral and peer-to-peer coordination between agents; prohibits unsanctioned inter-agent communication channels. Gap O response. See also Lateral Movement Containment Policy.
- [CA-06 Control Test](Governance-First-Security-Architecture-CA-06-Control-Test-v0.1.md) - Analytical bounded control test for the CA-06 multi-agent coordination control; documents test design, expected outcomes, and empirical validation status. Gap O response.

## Commercial Discovery

- [Governance Decision Assessment Workshop Offer](Governance-First-Security-Architecture-Governance-Decision-Assessment-Workshop-Offer-v0.1.md) - Narrow paid problem-validation offer without software or claims.

## Repository Governance

- [Repository Governance](GOVERNANCE.md) - Canonical maintainer, decision authority, contribution, fork, and future-code boundaries.
- [Attribution And Derivative Works](ATTRIBUTION.md) - Requested credit, canonical source, change notice, and no-endorsement wording.
- [Project Identity](PROJECT-IDENTITY.md) - Official name, canonical-project distinction, and architecture-project classification.
- [Citation Metadata](CITATION.cff) - Machine-readable project citation metadata.
- [Contributing](CONTRIBUTING.md) - Allowed review contributions and hard boundaries.
- [Code Of Conduct](CODE_OF_CONDUCT.md) - Participation expectations and private reporting path.
- [Security And Sensitive Feedback](SECURITY.md) - Safe reporting boundary.
- [GitHub Release Checklist](GITHUB-RELEASE-CHECKLIST.md) - Internal process document; private-first and public-release gates. Not an architecture document.
- [License](LICENSE) - Canonical CC BY-SA 4.0 legal code.
- [Notices And Attribution](NOTICE.md) - Project attribution, license scope, exclusions, and claim boundaries.
