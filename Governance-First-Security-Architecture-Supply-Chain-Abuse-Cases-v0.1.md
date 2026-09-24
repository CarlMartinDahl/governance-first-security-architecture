# Governance-First Security Architecture

## Supply Chain Abuse Cases v0.1

## Status

This document is a preparatory supply-chain abuse-case supplement for the Governance-First Security Architecture concept.

It is documentation-only.

It is not an implementation plan.

It is not a complete red-team plan.

It is not a security claim.

It supplements the main Abuse Case Library with scenarios specific to third-party, supplier, and supply chain attack paths. These scenarios share a common characteristic: the attacker enters or acts through a trusted relationship rather than through a direct attack on the primary organisation.

## Purpose

The purpose of this document is to answer:

```text
How could a trusted third party become an attack vector?
How could a supplier relationship be weaponised against the organisation?
How could indirect access cause direct harm?
Which controls must respond to supply chain scenarios specifically?
What stop states apply when the attacker is operating as a trusted actor?
```

## Abuse Case Format

Each abuse case identifies:

- scenario
- attacker or misuse actor
- target asset
- likely method
- risk
- required controls
- expected stop state
- open review question

## Abuse Case SC-001: Compromised Web Or IT Partner

Scenario:

A web agency, IT partner, or managed service provider with legitimate access to systems or infrastructure is compromised by an external attacker. The attacker uses the partner's credentials or access path to reach the primary organisation's environment.

Actor:

```text
External attacker operating through a compromised trusted third party.
```

Target assets:

- web infrastructure
- content management systems
- credentials stored or accessible by the partner
- internal systems reachable via partner access path

Method:

```text
Attacker compromises partner organisation through phishing, credential theft, or partner's own supply chain.
Attacker uses partner's legitimate credentials or remote access tools.
Attacker appears as trusted actor inside primary organisation's environment.
Traditional perimeter controls do not trigger because access looks legitimate.
```

Risk:

```text
High.
Attacker has authenticated access.
Lateral movement possible without triggering identity-based controls.
Data exfiltration, ransomware deployment, or persistence establishment all possible.
```

Required controls:

- third-party governance with explicit scope and egress boundary
- anomaly detection on third-party sessions
- session time-bounding
- credential isolation per third party
- stop state triggered on anomalous third-party behaviour
- audit of all third-party actions

Expected stop state:

```text
ACCESS_SUSPENDED
INCIDENT_REVIEW_REQUIRED
```

If lateral movement detected:

```text
LOCKDOWN_REQUIRED
```

Open review question:

```text
How quickly can third-party credentials be revoked if anomalous behaviour is detected at 03:00?
```

## Abuse Case SC-002: Malicious Or Trojanised Software Update

Scenario:

A software vendor or update provider delivers a malicious or trojanised update through a legitimate and trusted update channel. The organisation installs the update because it appears authorised.

Actor:

```text
External attacker who has compromised a software vendor's build or distribution pipeline.
```

Target assets:

- installed software
- system integrity
- credentials and secrets accessible to the software
- network access available to the software process

Method:

```text
Attacker compromises vendor's build, signing, or distribution process.
Malicious code is embedded in a legitimate-looking update.
Organisation's automated or manual update process installs the update.
Malicious code executes with the same trust level as the legitimate software.
```

Risk:

```text
Critical.
Code executes with elevated trust.
May have access to credentials, internal systems, and egress paths.
May persist undetected across multiple systems.
```

Required controls:

- software bill of materials awareness
- update approval gate for critical systems
- integrity verification before installation
- capability-change gate if update expands system permissions
- anomaly detection post-update
- rollback path if compromise is detected

Expected stop state:

```text
STOP_CAPABILITY_CHANGE
```

If active compromise detected post-installation:

```text
LOCKDOWN_REQUIRED
INCIDENT_REVIEW_REQUIRED
```

Open review question:

```text
Which installed software components have update processes that are not currently reviewed before installation?
```

## Abuse Case SC-003: Credential Theft From Third Party

Scenario:

Credentials issued to a third party are stolen from the third party's own environment, password manager, email, or device. The attacker uses these credentials to access the primary organisation without the third party's knowledge.

Actor:

```text
External attacker who has obtained third-party credentials through phishing, infostealer malware, or breach of third-party systems.
```

Target assets:

- systems accessible with the stolen credentials
- data within scope of the third party's access
- credentials the third party can reach from within the environment

Method:

```text
Attacker obtains credentials through third-party breach, phishing, or infostealer log.
Credentials are used directly or after a delay to avoid detection.
Access appears fully legitimate from the primary organisation's perspective.
No indication of compromise at the primary organisation's perimeter.
```

Risk:

```text
High.
Attacker has scoped but legitimate-looking access.
If third-party scope was not minimised, access may be broad.
Detection depends entirely on behavioural anomaly, not identity controls.
```

Required controls:

- principle of least privilege enforced on all third-party credentials
- session anomaly detection
- time-bounded credentials where feasible
- multi-factor authentication for third-party access paths
- regular review of whether credentials are still needed
- dark web and breach monitoring for third-party domains

Expected stop state:

```text
ACCESS_SUSPENDED
HUMAN_REVIEW_REQUIRED
```

Open review question:

```text
Are any third-party credentials persistent and non-expiring?
```

## Abuse Case SC-004: Agentic AI Attack Via Trusted Integration

Scenario:

An attacker deploys autonomous AI agents that probe, adapt, and escalate through an integration point, API, or third-party connector. The agents operate at a volume and speed that manual monitoring cannot match. Each individual action may appear within normal bounds while the aggregate effect represents a full compromise.

Actor:

```text
External attacker using autonomous AI agents to scale attack volume and adapt to defensive responses in real time.
```

Target assets:

- API endpoints and integration connectors
- credentials accessible through integration paths
- data reachable through permitted integration scope
- governance logic itself, if the agents can probe its boundaries

Method:

```text
Attacker launches many parallel agents targeting integration points.
Each agent tests a small variation: parameter, timing, encoding, or context.
Agents adapt based on responses, collectively mapping accessible boundaries.
No single request appears obviously malicious.
Aggregate access or exfiltration crosses the harm threshold undetected.
```

Risk:

```text
High and increasing.
Volume makes manual response impossible.
Adaptive behaviour evades static rule-based detection.
Governance boundaries that rely on human review speed will fail under agent-scale attack.
```

Required controls:

- rate limiting and volume anomaly detection on all integration points
- automated stop states that do not require human approval at initial trigger
- egress volume monitoring
- API scope minimisation
- fail-closed default on anomalous integration behaviour
- governance boundaries that are enforced at the architecture level, not only at the review level

Expected stop state:

```text
STOP_EGRESS_UNAUTHORIZED
```

or:

```text
LOCKDOWN_REQUIRED
```

Open review question:

```text
Which stop states in the current model require human approval before triggering, and should any of those be made automatic under volume-anomaly conditions?
```

## Abuse Case SC-005: Shared Hosting Or Infrastructure Compromise

Scenario:

The organisation, its web partner, or another supplier shares hosting infrastructure, a content delivery network, or a managed platform with other tenants. An attacker compromises a co-tenant or the shared infrastructure itself and uses that position to reach the organisation's environment.

Actor:

```text
External attacker who has compromised shared infrastructure or a co-tenant.
```

Target assets:

- web presence and content
- credentials stored or processed on shared infrastructure
- data in transit through shared network or CDN
- trust relationship between the organisation and its web partner

Method:

```text
Attacker compromises shared hosting environment, CDN, or managed platform.
Attacker modifies content, injects code, or intercepts credentials in transit.
Organisation and its users receive compromised content from what appears to be a trusted source.
```

Risk:

```text
Medium to high depending on what is hosted.
User-facing content integrity is compromised.
Credentials or sensitive data in transit may be intercepted.
Trust relationship is weaponised without the organisation's direct knowledge.
```

Required controls:

- content integrity monitoring
- subresource integrity where applicable
- TLS integrity verification
- supplier hosting environment review
- incident path if content integrity failure is detected

Expected stop state:

```text
CONTAIN_DISABLE_INTEGRATION
INCIDENT_REVIEW_REQUIRED
```

Open review question:

```text
Does the organisation know which shared infrastructure its third-party suppliers are using, and has that infrastructure been assessed?
```

## Abuse Case SC-006: Third Party Used As Persistence Path

Scenario:

An attacker who has been detected and partially remediated within the primary organisation has previously established access through a third-party relationship. After internal remediation, the attacker re-enters through the third party, which was not included in the remediation scope.

Actor:

```text
External attacker maintaining persistence through a third-party access path after partial internal remediation.
```

Target assets:

- any system accessible to the third party
- remediation effort integrity
- incident containment

Method:

```text
During initial compromise, attacker identifies third-party access paths.
Attacker establishes presence or credential copy accessible via the third party.
Internal remediation closes direct access but does not cover third-party paths.
Attacker re-enters through the third party after remediation is declared complete.
```

Risk:

```text
High.
Re-entry after remediation significantly increases harm and erodes trust in recovery process.
May not be detected because the re-entry path appears legitimate.
```

Required controls:

- all third-party access suspended as default during any incident response
- third-party access reviewed and confirmed clean before reinstatement
- incident scope explicitly includes all third-party access paths
- recovery rollback module covers third-party credential rotation

Expected stop state:

```text
ACCESS_SUSPENDED for all third parties during active incident
INCIDENT_REVIEW_REQUIRED before any third-party access is reinstated
```

Open review question:

```text
Does the current Recovery Rollback Incidents module explicitly require third-party credential rotation as part of incident recovery?
```

## Supply Chain Abuse Case Matrix

| Abuse Case | Attack Path | Primary Control |
|---|---|---|
| SC-001: Compromised web or IT partner | Partner credential | Third-party governance + anomaly detection |
| SC-002: Trojanised software update | Update channel | Update approval gate + integrity verification |
| SC-003: Credential theft from third party | Stolen credential | Least privilege + breach monitoring |
| SC-004: Agentic AI via integration | API or connector | Automated stop states + volume detection |
| SC-005: Shared infrastructure | Hosting or CDN | Content integrity + supplier review |
| SC-006: Third party as persistence path | Re-entry after remediation | Suspend all third-party access during incident |

## Relationship To Other Modules

- Abuse Case Library: this document supplements, not replaces, the main abuse case set
- Third-Party Governance: SC-001, SC-003, and SC-006 depend on third-party governance controls
- Trust Boundaries: all supply chain scenarios exploit a trust boundary failure
- Ingress Egress Policy: SC-002 and SC-004 involve egress boundary failures
- Recovery Rollback Incidents: SC-006 identifies a gap in current recovery scope
- Stop-State Registry: automated stop states without human delay are required for SC-004

## Open Questions

1. Which of these scenarios should be added to the synthetic test case set?
2. Which scenarios are most likely given the organisation's current third-party relationships?
3. Should SC-004 (agentic AI attack) trigger an automatic stop state without human approval?
4. How should the organisation respond if a third party refuses to participate in incident review?
5. Are there supply chain attack paths not covered here that reviewers have identified?
6. Should dark web monitoring for third-party domains be a required governance control?
7. Which scenarios require legal review before defining the expected organisational response?
