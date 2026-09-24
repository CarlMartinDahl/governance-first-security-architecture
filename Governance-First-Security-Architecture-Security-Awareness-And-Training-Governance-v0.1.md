# Governance-First Security Architecture
## Security Awareness And Training Governance
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy governs the design, delivery, measurement, and accountability of the organisation's security awareness and training programme. Technical controls cannot compensate for a workforce that does not understand the threats they face or the governance obligations they carry. Training is not a compliance checkbox — it is a governance control with measurable outcomes.

This policy defines minimum requirements, role-differentiated training obligations, how effectiveness is measured, and what happens when training objectives are not met.

---

## 2. Scope

Applies to all personnel, contractors, and third parties with ongoing access to organisational systems or data. Third parties with limited, supervised access may fulfil requirements through equivalent programmes with documented confirmation.

---

## 3. Core Governance Principle

> **Security awareness is a governance outcome, not a training event. The measure of success is behaviour change, not completion rates. A programme that produces high completion rates and unchanged behaviour has failed.**

---

## 4. Programme Ownership And Accountability

- The Security Awareness programme has a named owner in the Role Registry accountable for design, delivery, and outcome measurement
- Programme effectiveness is reported to governance leadership at minimum annually
- The programme is reviewed and updated at minimum annually and following any significant security incident where human factors contributed
- Budget and resources for the programme are allocated as a governance commitment, not a discretionary expense

---

## 5. Minimum Training Requirements By Role

### 5.1 All Personnel
| Training Module | Frequency | Format |
|---|---|---|
| Security fundamentals (phishing, passwords, data handling) | Onboarding + annual refresh | Mandatory completion |
| Social engineering and human manipulation | Annual | Mandatory completion |
| Data classification and handling obligations | Onboarding + annual refresh | Mandatory completion |
| Incident reporting — what to report, how, to whom | Onboarding | Mandatory completion |
| Acceptable use of AI tools | Annual | Mandatory completion |

### 5.2 Privileged And Technical Roles
All requirements above, plus:
| Training Module | Frequency | Format |
|---|---|---|
| Secure development practices (if applicable) | Annual | Mandatory completion |
| Privileged access responsibilities | At privilege grant + annual | Mandatory completion |
| Incident response role obligations | Annual | Mandatory completion |
| Cryptographic standards and key handling | Annual | Mandatory completion |

### 5.3 Governance And Leadership Roles
All All Personnel requirements, plus:
| Training Module | Frequency | Format |
|---|---|---|
| Governance decision accountability | Onboarding + annual | Mandatory completion |
| Regulatory obligations (GDPR, NIS2, sector-specific) | Annual | Mandatory completion |
| Crisis and incident decision-making | Annual | Tabletop exercise or equivalent |

---

## 6. Phishing And Social Engineering Simulation

- Simulations are conducted at minimum quarterly across all personnel
- Simulation design varies in sophistication — low-sophistication and high-sophistication scenarios are both used
- Results are analysed at programme level, not used for individual performance management
- Individuals who interact with a simulation receive immediate, non-punitive educational feedback at the point of interaction
- Persistent simulation failure (defined as interacting with simulations at a rate significantly above programme baseline across multiple quarters) triggers a supported remediation pathway, not disciplinary action as a first response
- Simulation results are reviewed at governance level quarterly; sustained programme-wide failure rates are a governance finding requiring programme redesign, not individual remediation

---

## 7. Measuring Effectiveness

Completion rates are a necessary but insufficient measure. The programme measures:

| Metric | Measurement Method | Review Frequency |
|---|---|---|
| Training completion rate | LMS or equivalent tracking | Monthly |
| Phishing simulation click / interaction rate | Simulation platform | Quarterly |
| Phishing simulation report rate | Simulation platform | Quarterly |
| Time to report a suspected incident | Incident log analysis | Quarterly |
| Human-factor contribution to confirmed incidents | Post-incident review | Per incident |
| Training satisfaction and perceived relevance | Periodic survey | Annual |

Trend analysis across quarters is more meaningful than point-in-time metrics. A declining simulation interaction rate combined with an increasing report rate is the target trajectory.

---

## 8. Overdue And Non-Completion

- Training completion is tracked with automated reminders at 14 days and 7 days before deadline
- Personnel who have not completed mandatory training by deadline are flagged to their line manager and the Security Awareness owner
- Access to systems classified Confidential or above may be suspended for personnel more than 30 days overdue on mandatory training; this is a governance decision, not an automatic technical enforcement
- Persistent non-completion without documented cause is an accountability matter under the Role Registry
- Exceptions (extended leave, medical absence, etc.) are documented and a completion plan agreed within 5 business days of return

---

## 9. Content Standards

Training content must meet minimum quality standards to be effective:

- Scenarios are based on real-world attack patterns, not hypothetical constructs; content is updated when the threat landscape changes significantly
- Content is reviewed for accuracy against current governance policies at each annual review cycle
- AI-specific threats (deepfakes, AI-generated phishing, agentic AI misuse) are included in content from 2025 onwards and updated as the threat evolves
- Content does not use fear or shame as primary motivators — psychological safety is required for effective reporting behaviour
- Content is accessible: language level, format, and delivery method account for the range of roles and technical backgrounds in the workforce

---

## 10. Third-Party And Contractor Requirements

- Contractors and third parties with ongoing system or data access must complete equivalent awareness training within 30 days of access being granted
- Evidence of completion is provided to the Security Awareness owner and retained in the vendor record
- Third parties may fulfil requirements through their own equivalent programme if it covers the minimum modules; equivalence must be documented and assessed, not assumed
- Training requirements for third parties are included in contractual obligations under Third-Party Governance

---

## 11. Post-Incident Training Response

When a confirmed incident involves a human factor — a person was deceived, made an error, or bypassed a control — the training response is:

1. Root cause analysis of what knowledge or behaviour gap contributed
2. Assessment of whether current training addresses that gap
3. If not: content update or targeted module deployment within 60 days
4. If yes: assess whether delivery or format is ineffective and redesign
5. Document findings and programme changes in the Post-Review Revision Log

The question is never only "why did that person do that" — it is always also "why did our programme not prepare them for this scenario."

---

## 12. Related Documents

- Social Engineering And Human Manipulation Policy
- Data Classification And Handling Policy
- Privileged Access Management Policy
- Role Registry
- Third-Party Governance
- Insider Threat Governance
- AI-Human Governance
- Audit And Accountability
- Recovery Rollback Incidents
