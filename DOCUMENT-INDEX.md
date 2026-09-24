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
- [Stop-State Registry](Governance-First-Security-Architecture-Stop-State-Registry-v0.1.md) - Canonical stop, review, lockdown, and incident states.
- [Decision-State Matrix](Governance-First-Security-Architecture-Decision-State-Matrix-v0.1.md) - Mapping from governance signals to decisions.
- [Role Registry](Governance-First-Security-Architecture-Role-Registry-v0.1.md) - Role, authority, review, approval, and accountability boundaries.
- [Asset-To-Kernel Mapping](Governance-First-Security-Architecture-Asset-To-Kernel-Mapping-v0.1.md) - Asset categories mapped to governance defaults.

## Security And Risk Foundations

- [Threat Model](Governance-First-Security-Architecture-Threat-Model-v0.1.md) - Threat actors, misuse paths, assets, and boundaries.
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
- [Lateral Movement Containment Policy](Governance-First-Security-Architecture-Lateral-Movement-Containment-v0.1.md) - Default-deny east-west traffic, segment classification, lateral movement indicators, mandatory isolation triggers, and break-glass authorisation.
- [Log Integrity And Tamper-Evidence Policy](Governance-First-Security-Architecture-Log-Integrity-And-Tamper-Evidence-v0.1.md) - Write-once log forwarding, immutability controls, absence-as-alert, forensic preservation, and retention requirements.
- [Ransomware Recovery Policy](Governance-First-Security-Architecture-Ransomware-Recovery-Policy-v0.1.md) - 3-2-1-1 backup architecture, payment decision governance, containment phases, sanctions screening, GDPR notification obligations, and recovery process.
- [Vulnerability Disclosure And Patch Governance](Governance-First-Security-Architecture-Vulnerability-Disclosure-And-Patch-Governance-v0.1.md) - Inbound responsible disclosure, safe harbour, patch remediation windows, zero-day protocol, dependency scanning, and vulnerability register.
- [Data Classification And Handling Policy](Governance-First-Security-Architecture-Data-Classification-And-Handling-Policy-v0.1.md) - Four-tier classification (Public/Internal/Confidential/Restricted), handling requirements per tier, GDPR overlay, AI data governance, and breach impact mapping.
- [Privileged Access Management Policy](Governance-First-Security-Architecture-Privileged-Access-Management-Policy-v0.1.md) - Privileged account tiers, account separation, just-in-time access, session recording, break-glass governance, and insider threat indicators.
- [Insider Threat Governance](Governance-First-Security-Architecture-Insider-Threat-Governance-v0.1.md) - Structural blast-radius controls, separation of duties, four-eyes principle, offboarding risk window, negligence vs. malice framework, and GDPR monitoring constraints.
- [Cryptographic Standards Policy](Governance-First-Security-Architecture-Cryptographic-Standards-Policy-v0.1.md) - Approved and prohibited algorithms, TLS requirements, password hashing standards, certificate governance, key management, and post-quantum transition alignment.
- [Security Awareness And Training Governance](Governance-First-Security-Architecture-Security-Awareness-And-Training-Governance-v0.1.md) - Role-differentiated training requirements, phishing simulation governance, effectiveness metrics, non-completion consequences, and post-incident training response.

## Legal, Provider, And Future Readiness

- [GDPR And EU AI Act Alignment](Governance-First-Security-Architecture-GDPR-EU-AI-Act-Alignment-v0.1.md) - Alignment goals without compliance claims.
- [Provider And Platform Constraints](Governance-First-Security-Architecture-Provider-And-Platform-Constraints-v0.1.md) - Time-sensitive policy, platform, tool-use, and cyber constraints.
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
- [GitHub Release Checklist](GITHUB-RELEASE-CHECKLIST.md) - Private-first and public-release gates.
- [License](LICENSE) - Canonical CC BY-SA 4.0 legal code.
- [Notices And Attribution](NOTICE.md) - Project attribution, license scope, exclusions, and claim boundaries.
