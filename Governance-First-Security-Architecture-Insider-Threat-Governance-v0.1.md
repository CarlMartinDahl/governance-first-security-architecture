# Governance-First Security Architecture
## Insider Threat Governance
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy governs the detection, prevention, and response to insider threats — harm caused by individuals with legitimate access to organisational systems, data, or facilities. Insider threats include malicious actors (intentional harm), negligent actors (unintentional harm through careless behaviour), and compromised actors (legitimate users whose accounts or devices have been taken over by external parties).

Insider threat governance is not about surveillance of employees. It is about designing systems, processes, and access structures so that the blast radius of any individual — regardless of intent — is bounded and detectable.

---

## 2. Scope

Applies to all personnel, contractors, and third parties with access to organisational systems, data, or facilities. Covers both current and departing individuals.

---

## 3. Core Governance Principle

> **The goal is not to detect bad people. The goal is to design systems where the impact of any individual acting outside their sanctioned boundary — whether through malice, negligence, or compromise — is limited, visible, and recoverable.**

---

## 4. Structural Controls (Prevention)

The most effective insider threat controls are structural: they limit what any individual can do unilaterally, regardless of intent.

### 4.1 Separation Of Duties
No single individual should be able to complete a high-risk action from initiation to execution without a second person's involvement. Applied to:
- Financial transactions above defined threshold
- Privileged account provisioning and approval
- Code deployment to production (author cannot be sole approver)
- Bulk data export of Restricted classification
- Modification of audit logs or security configuration
- Disabling security controls

### 4.2 Least Privilege
All access is scoped to the minimum required for the individual's current role and active tasks. Scope creep — accumulation of access rights over time without corresponding role changes — is a leading insider threat enabler and is addressed in the quarterly access review process.

### 4.3 Four-Eyes Principle
For the highest-risk actions (Tier 0 privileged access use, production database modification, bulk personal data export, payment instruction changes above threshold), a second named individual must review and confirm the action before or immediately after execution. The confirming individual is accountable alongside the actor.

### 4.4 Time-Bounded Access
Access is granted for the duration of a role or task, not indefinitely. Role changes, project completions, and departures trigger immediate access review under the Role Registry and Vendor Offboarding And Revocation processes.

---

## 5. Detection Controls

Insider threat detection relies on behavioural baselines and anomaly detection rather than content surveillance.

### 5.1 Behavioural Baseline Indicators
The following deviations from established individual behaviour patterns trigger investigation:

- Significant increase in data access volume without operational justification
- Access to data or systems outside the individual's established pattern
- Bulk download or export of Confidential or Restricted data
- Access at unusual hours inconsistent with established patterns, particularly for privileged accounts
- Repeated failed access attempts to systems outside scope
- Use of personal storage devices or unapproved cloud services to transfer organisational data
- Attempts to disable, circumvent, or query the monitoring or logging infrastructure
- Sudden pattern change in access behaviour proximate to a resignation, disciplinary event, or organisational change

### 5.2 Offboarding Risk Window
The period surrounding an individual's departure — from notice of resignation or termination through final access revocation — is the highest-risk window for insider threat activity. During this period:
- Access is reviewed and scoped to only what is operationally required for the transition
- Privileged access is revoked at the point of notice where operationally feasible
- Data access activity is monitored with heightened sensitivity
- Final access revocation is confirmed and logged within 24 hours of last working day

---

## 6. Negligence And Unintentional Harm

The majority of insider incidents are negligence rather than malice. Governance response to negligence:

- Negligence-driven incidents are treated as process failures requiring root cause analysis, not primarily as individual failures requiring punishment
- Root cause analysis asks: what control should have prevented this? Why did it not?
- Findings feed into Risk And Action Taxonomy and training programme updates
- Repeated negligence by an individual after remediation support has been provided becomes an accountability matter under the Role Registry

---

## 7. Compromised Insider Scenarios

A legitimate user whose account or device has been taken over by an external actor presents as an insider threat from a detection perspective. Indicators specific to account compromise:

- Authentication from an unexpected geographic location or IP range
- Simultaneous sessions from geographically inconsistent locations
- MFA prompts reported as unexpected by the account holder
- Activity during periods the individual has confirmed they were not working
- Credential use pattern inconsistent with the individual's established behaviour

These indicators trigger the Stop State process and credential revocation under Identity And Credential Governance before investigation is complete.

---

## 8. Whistleblower And Safe Reporting Protection

Insider threat governance must not suppress legitimate internal reporting. Individuals who report suspected policy violations, security incidents, or governance failures through defined channels are protected from retaliation. The reporting channel defined in SECURITY.md is available for sensitive internal reports as well as external vulnerability disclosure.

Any action taken against an individual in retaliation for a good-faith internal report is itself a governance violation.

---

## 9. Privacy And Legal Constraints

Insider threat monitoring must operate within applicable privacy law. In the EU/EEA context:

- Monitoring of employee activity requires a documented lawful basis under GDPR
- The scope and nature of monitoring must be proportionate to the risk
- Individuals must be informed that monitoring occurs (in employment agreements or equivalent)
- Data collected through monitoring is used only for the stated security purpose and retained only as long as necessary
- Any use of monitoring data in disciplinary or legal proceedings is reviewed by legal counsel before use

---

## 10. Response To Confirmed Insider Incident

1. **Immediate access revocation** — all access for the individual suspended pending investigation
2. **Evidence preservation** — do not alert the individual; preserve logs and access records under forensic hold
3. **Legal counsel engagement** — before any investigative interview or disciplinary action
4. **Scope assessment** — identify what data or systems were accessed, what actions were taken, and what harm occurred or may occur
5. **Regulatory assessment** — determine whether the incident triggers GDPR breach notification or other reporting obligations
6. **Root cause and structural review** — what structural control failed or was absent that permitted this incident?

---

## 11. Related Documents

- Privileged Access Management Policy
- Role Registry
- Identity And Credential Governance
- Vendor Offboarding And Revocation
- Audit And Accountability
- Log Integrity And Tamper-Evidence Policy
- Stop State Policy
- Data Classification And Handling Policy
- GDPR And EU AI Act Alignment
- Social Engineering And Human Manipulation Policy
