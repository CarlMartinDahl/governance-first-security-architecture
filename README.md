# Governance-First Security Architecture Project

The Governance-First Security Architecture Project is a documentation-only architecture project for controlling sensitive human- and AI-assisted decisions before technical capability is allowed to act.

The project asks a different first question:

```text
Not: What can the system do?

But: What is the system allowed to do,
under whose authority,
with what evidence,
in which mode,
with what egress boundary,
with whose accountability,
and when must it stop?
```

## About This Project

This is an independent project by Martin Dahl.

It is also a practical example of how I approach an ambiguous security and AI-governance problem: establish authority, evidence, decision boundaries, stop conditions, accountability, and review before discussing implementation.

The repository is intentionally documentation-first. It is open for critical review and further development, but it is not an implementation repository and does not claim that the model is secure, compliant, certified, production-ready, or commercially validated.

The canonical project source is `https://github.com/CarlMartinDahl/governance-first-security-architecture`. Independent forks and derivatives are welcome. They should remain distinguishable from official project revisions and must follow the applicable attribution and license terms for material they use.

## Current Status

| Area | Status |
| --- | --- |
| Repository | Documentation only |
| Documentation package | Frozen for external review |
| External feedback | Received and logged |
| Targeted external review | Partial |
| Commercial validation | Workshop and assessment discovery only |
| Prototype implementation | Not authorized |
| Production use | Not authorized |

## Model At A Glance

```mermaid
flowchart LR
    A["Authority"] --> D["Governed decision"]
    E["Evidence"] --> D
    M["Mode and risk"] --> D
    X["Egress boundary"] --> D
    C["Capability boundary"] --> D
    H["Human and AI roles"] --> D
    D --> AL["Allow"]
    D --> RV["Review or escalate"]
    D --> BL["Block or stop"]
    D --> IN["Incident or lockdown"]
    AL --> AU["Audit and accountability"]
    RV --> AU
    BL --> AU
    IN --> AU
```

The model treats a stop state as a valid governance outcome, not a system failure.

Its recurring control pattern is:

```text
Authority + evidence + mode + risk + egress + accountability
before governed action.
```

## What The Model Covers

- decision authority and role separation,
- evidence quality, source authority, staleness, and counter-evidence,
- ingress and egress as separate control boundaries,
- data classification, handling requirements, and breach impact mapping,
- explicit allow, review, block, quarantine, lockdown, and incident outcomes,
- AI recommendation versus human review, approval, and accountability,
- agentic system action authority tiers and operational mandate requirements,
- agentic operational boundaries, tool use governance, and prompt injection response,
- AI model provenance, integrity verification, and behavioural drift monitoring,
- capability-change gates,
- network segmentation including a dedicated AI and agentic segment,
- data egress classification, approved egress channels, and exfiltration detection,
- identity and credential lifecycle, scope minimisation, and compromise response,
- privileged access management, just-in-time access, and break-glass governance,
- insider threat structural controls and separation of duties,
- lateral movement containment and default-deny east-west posture,
- log integrity, tamper-evidence, and forensic preservation,
- social engineering, BEC, deepfake governance, and out-of-band confirmation,
- secrets sprawl prevention, rotation schedules, and CI/CD pipeline governance,
- cryptographic standards, prohibited algorithms, and post-quantum transition alignment,
- third-party and supply chain governance including agentic AI supply chain threats,
- vulnerability disclosure, patch governance, and zero-day protocol,
- ransomware recovery, backup architecture, and sanctions screening,
- business continuity, disaster recovery, and return-to-normal criteria,
- audit and decision traceability,
- recovery and rollback expectations,
- GDPR and EU AI Act alignment goals,
- synthetic-only test and prototype boundaries,
- restrained legal, regulatory, security, and commercial language.

## Practical Use Boundary

This repository is review and thinking material, not deployable software.

| Appropriate use | Current boundary |
| --- | --- |
| Challenge an AI, security, or governance design | Supported as a critical review lens |
| Run a decision assessment for one sensitive AI-assisted workflow | Intended commercial-discovery use through the bounded workshop offer |
| Reuse concepts such as stop states, role boundaries, decision matrices, or egress classes | Permitted under CC BY-SA 4.0 with attribution and share-alike obligations where applicable |
| Deploy the documentation as a live control plane | Not supported or authorized |
| Claim security, GDPR compliance, EU AI Act compliance, certification, or production readiness | Prohibited by the project claim boundary |
| Build a prototype or operational system from the package | Not authorized while the documentation freeze remains active |

The primary review audience includes CISOs, AI-governance leads, legal and risk functions, security reviewers, and enterprise architects who need to explain decision authority, required evidence, stop conditions, egress limits, and accountability.

## Reading Paths

### Executive Path

1. [Executive Overview](Governance-First-Security-Architecture-Executive-Overview-v0.1.md)
2. [Technical Review Brief](Governance-First-Security-Architecture-Technical-Review-Brief-v0.1.md)
3. [External Review Checklist](Governance-First-Security-Architecture-External-Review-Checklist-v0.1.md)

### Security Practitioner Path

1. [Threat Model](Governance-First-Security-Architecture-Threat-Model-v0.1.md)
2. [Risk And Action Taxonomy](Governance-First-Security-Architecture-Risk-And-Action-Taxonomy-v0.1.md)
3. [Trust Boundaries](Governance-First-Security-Architecture-Trust-Boundaries-v0.1.md)
4. [Abuse Case Library](Governance-First-Security-Architecture-Abuse-Case-Library-v0.1.md)
5. [Lateral Movement Containment Policy](Governance-First-Security-Architecture-Lateral-Movement-Containment-v0.1.md)
6. [Data Egress And Exfiltration Prevention](Governance-First-Security-Architecture-Data-Egress-And-Exfiltration-Prevention-v0.1.md)
7. [Network Segmentation Architecture](Governance-First-Security-Architecture-Network-Segmentation-Architecture-v0.1.md)
8. [Log Integrity And Tamper-Evidence Policy](Governance-First-Security-Architecture-Log-Integrity-And-Tamper-Evidence-v0.1.md)
9. [Security Reviewer Bundle](Security-Reviewer-Bundle-v0.1.md)

### Technical Path

1. [Minimal Viable Governance Kernel](Governance-First-Security-Architecture-Minimal-Viable-Governance-Kernel-v0.1.md)
2. [Mode Model Normalization](Governance-First-Security-Architecture-Mode-Model-Normalization-v0.1.md)
3. [Stop-State Registry](Governance-First-Security-Architecture-Stop-State-Registry-v0.1.md)
4. [Decision-State Matrix](Governance-First-Security-Architecture-Decision-State-Matrix-v0.1.md)
5. [Threat Model](Governance-First-Security-Architecture-Threat-Model-v0.1.md)

### AI Governance Path

1. [AI-Human Governance](Governance-First-Security-Architecture-AI-Human-Governance-v0.1.md)
2. [Agentic Operational Boundary](Governance-First-Security-Architecture-Agentic-Operational-Boundary-v0.1.md)
3. [AI Model And Supply Chain Integrity](Governance-First-Security-Architecture-AI-Model-And-Supply-Chain-Integrity-v0.1.md)
4. [Evidence And Source Policy](Governance-First-Security-Architecture-Evidence-And-Source-Policy-v0.1.md)
5. [Audit And Accountability](Governance-First-Security-Architecture-Audit-And-Accountability-v0.1.md)
6. [GDPR And EU AI Act Alignment](Governance-First-Security-Architecture-GDPR-EU-AI-Act-Alignment-v0.1.md)

### Commercial Discovery Path

1. [Governance Decision Assessment Workshop Offer](Governance-First-Security-Architecture-Governance-Decision-Assessment-Workshop-Offer-v0.1.md)
2. [Post-Review Revision Log](Governance-First-Security-Architecture-Post-Review-Revision-Log-v0.1.md)

The complete package is organized in [DOCUMENT-INDEX.md](DOCUMENT-INDEX.md).

## Current Safe Path

```text
1. Keep major model expansion frozen.
2. Invite critical external review.
3. Record feedback and blockers.
4. Test 2-3 tightly scoped paid assessments.
5. Do not build software unless review and evidence justify reopening the gate.
```

## Known Review Questions

- Does the model add enough value beyond existing security and governance frameworks?
- Is the governance kernel actually minimal?
- Are the stop-state names and older blocked-outcome names mapped clearly enough?
- Are the decision matrix and role model practical, or still too broad?
- What should be removed before any prototype discussion?
- Can the workshop create useful paid outcomes without software?

Open questions are review inputs. They are not implementation instructions.

## Contributing

Critical review, scope reduction, terminology corrections, missing risks, stronger claim boundaries, and source improvements are welcome.

Read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before opening an issue or pull request. Do not submit secrets, personal data, private reviewer material, real incidents, or implementation code.

Repository authority, derivative-work attribution, and official-project identity are defined in [GOVERNANCE.md](GOVERNANCE.md), [ATTRIBUTION.md](ATTRIBUTION.md), and [PROJECT-IDENTITY.md](PROJECT-IDENTITY.md).

## License

Except where otherwise noted, this documentation is licensed under [Creative Commons Attribution-ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/).

Requested attribution: `Governance-First Security Architecture Project by Martin Dahl`.

The complete standard legal code is in [LICENSE](LICENSE). Project attribution, scope notes, third-party exclusions, and claim boundaries are in [NOTICE.md](NOTICE.md) and [ATTRIBUTION.md](ATTRIBUTION.md).

No software is currently included. If software is later authorized through the review gate, original project code is intended to use [Mozilla Public License 2.0](https://www.mozilla.org/MPL/2.0/). That future code license is not active and does not authorize implementation now.

## Originator And Canonical Maintainer

Martin Dahl

This repository is part concept package, part working portfolio: it shows the questions I ask, the boundaries I set, and how I turn uncertain ideas into material that can be challenged. Contributions are welcome, while official project revisions remain traceable to the canonical repository and its governance process.
