# Governance-First Security Architecture
## Insider Threat Governance
**Version:** 0.1 — Initial Release
**Status:** Draft / Review-Stage Template (`LM-1_REVIEW_PACKAGE` — Not Approved for Production or Compliance Use)
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

Insider threat governance must not suppress legitimate internal reporting. Individuals who report suspected policy violations, security incidents, or governance failures through defined channels are protected from retaliation.

Internal whistleblowing reports must be routed through a **dedicated internal reporting channel compliant with Directive (EU) 2019/1937 (EU Whistleblowing Directive)** and applicable national transposition law — providing strict confidentiality of the reporter's identity, impartial designated recipients, **7-day acknowledgment**, **3-month feedback**, access segregation, and GDPR-compliant retention/erasure. `SECURITY.md` is strictly for external security vulnerability disclosure and must **not** be used as an internal employee whistleblowing channel.

Any action taken against an individual in retaliation for a good-faith internal report is itself a governance violation.

---

## 9. Privacy, Employment Law, And AI Act Constraints

Insider threat monitoring must operate within applicable privacy, employment, and AI law. In the EU/EEA context, before deploying any employee behavioural monitoring:

- **Lawful basis & transparency (GDPR Arts. 6, 13–14):** Monitoring requires a documented statutory lawful basis — typically legitimate interest (`Art. 6(1)(f)` with a documented Legitimate Interest Assessment) or legal obligation / national employment-law basis (`Art. 6(1)(c)` / `Art. 88`), **not** employee consent (which is generally invalid due to employer-employee subordination under Recital 43). Employees must receive transparent, specific standalone privacy notices (not generic boilerplate in employment contracts).
- **Mandatory DPIA & DPO consultation (GDPR Art. 35):** Because employees are vulnerable data subjects, systematic behavioural monitoring triggers a mandatory **Data Protection Impact Assessment (DPIA)** with statutory **DPO advice (Art. 35(2))** prior to deployment (and Art. 36 prior consultation if residual risk remains high).
- **Works council / employee-representative co-determination (GDPR Art. 88):** Deployment must satisfy national labour-law consultation or co-determination requirements (for example, German *BetrVG § 87(1)(6)*, French *CSE*, Swedish *MBL*, Dutch *WOR*); evidence gathered without mandatory consultation may be unlawful and inadmissible.
- **EU AI Act workplace rules (currently binding):** Any AI/ML system used to monitor or evaluate employee behaviour falls under **Annex III(4)(b) high-risk AI**, requiring advance notification to **workers' representatives and affected workers (Art. 26(7))**, human oversight (Art. 26(2)), and logging (Art. 26(6)). Any emotion, stress, or sentiment inference in the workplace is **strictly prohibited under Art. 5(1)(f)** (`STOP_PROHIBITED_AI_USE`).
- **Purpose limitation & Art. 22 safeguards:** Monitoring data is used strictly for the stated security purpose, retained only per bounded ceilings, never repurposed for unrelated HR performance scoring, and any automated suspension affecting an employee must provide **GDPR Art. 22(3)** human review and contestability, with legal counsel review before any disciplinary or legal use.

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
