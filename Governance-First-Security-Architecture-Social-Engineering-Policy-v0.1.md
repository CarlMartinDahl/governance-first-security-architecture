# Governance-First Security Architecture
## Social Engineering And Human Manipulation Policy
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy establishes governance controls for the human attack surface. Technical controls cannot defend against an attacker who convinces an authorised person to take a harmful action voluntarily. Social engineering — including phishing, vishing, pretexting, SIM-swapping, and Business Email Compromise (BEC) — remains the most common initial access vector in confirmed breach investigations.

This policy defines who may authorise what through which channels, and how verification must occur before any sensitive action is approved.

---

## 2. Scope

Applies to all personnel, contractors, and third parties with access to systems, credentials, data, or financial authority. Covers inbound requests via email, phone, SMS, messaging platforms, in-person, and AI-mediated communication channels.

---

## 3. Core Governance Principle

> **Channel of receipt is not proof of identity. Request legitimacy must be verified through a pre-established, out-of-band confirmation pathway — regardless of how convincing the request appears.**

This principle applies even when:
- The request appears to come from a known executive or colleague
- The request references real internal information
- The request is marked urgent or confidential
- The communication channel is one normally trusted (corporate email, Slack, Teams)

---

## 4. Action Classification

All sensitive actions are classified into three tiers requiring different verification levels.

### Tier 1 — Standard Actions
Actions with limited blast radius, reversible, within established workflows.
- Requires: Normal authentication only
- Examples: Routine file access, standard support requests

### Tier 2 — Elevated Actions
Actions that affect credentials, access rights, financial transactions under threshold, or data export.
- Requires: Out-of-band verification via pre-registered phone number or in-person confirmation
- Examples: Password reset for privileged account, adding a new payment recipient, granting system access

### Tier 3 — Critical Actions
Actions with large or irreversible blast radius: wire transfers above threshold, credential infrastructure changes, executive impersonation scenarios.
- Requires: Dual authorisation — two named individuals via separate out-of-band channels
- Examples: Wire transfer >threshold, domain transfer, bulk credential rotation, disabling MFA for any account

---

## 5. Verification Pathway Registry

Each sensitive role must have a pre-registered verification pathway documented in the Role Registry. The pathway must:
- Use a channel different from the one the request arrived on
- Reference a number, address, or method established *before* the incident — not provided within the request itself
- Be reviewed and updated at least annually and upon role change

**Anti-pattern:** An attacker emails a finance officer claiming to be the CFO and provides a callback number. The finance officer must not call that number — they must call the CFO's pre-registered number.

---

## 6. BEC And Executive Impersonation

Business Email Compromise specifically targets financial and HR authority. Governance controls:

- **Payment instruction changes** received via email require Tier 3 verification regardless of claimed sender
- **Payroll redirection requests** require HR manager approval plus direct employee confirmation via separate channel
- **Urgent wire transfer requests** attributed to executives are presumed social engineering until verified — urgency is itself a red flag, not a reason to skip verification
- All payment instruction changes must be logged in the Audit and Accountability system with verification method recorded

---

## 7. SIM-Swapping And Phone-Based Attacks

SIM-swapping compromises SMS-based MFA and phone verification. Mitigations:

- SMS OTP is not accepted as sole second factor for Tier 2 or Tier 3 actions
- Phone-based verification for high-value actions must use a pre-registered device confirmed through a non-phone channel
- If a registered phone number is reported lost, stolen, or ported, all credentials and access associated with that number are suspended pending re-verification through the Stop State process

---

## 8. AI-Mediated Social Engineering

Deepfake audio and video, AI-generated phishing at scale, and AI impersonation of colleagues are active threats as of 2025–2026. Governance response:

- Voice or video alone is not sufficient verification for Tier 2 or Tier 3 actions — even live calls
- A pre-agreed codeword or challenge-response phrase may be registered between high-trust pairs for real-time verification
- Any request involving urgency + unusual channel + sensitive action should trigger Tier 3 verification regardless of apparent authenticity

---

## 9. Awareness And Simulation

- All personnel complete social engineering awareness training at onboarding and annually thereafter
- Phishing simulations are conducted at minimum quarterly; results are reviewed at governance level, not used punitively
- Personnel who identify and report social engineering attempts are acknowledged; those who fall victim receive remediation support, not punishment
- Simulation results feed into Risk and Action Taxonomy updates

---

## 10. Incident Response Trigger

Any of the following triggers immediate escalation to the Recovery and Rollback Incidents process:

- Credentials provided to an unverified party
- Financial transfer made on unverified instruction
- Access granted following a request that bypassed verification
- Suspected deepfake or AI-generated impersonation attempt
- SIM-swap or phone-porting event affecting a registered verification number

---

## 11. Policy Enforcement

Violation of verification requirements is a governance breach. Intent is irrelevant — a well-meaning action taken without required verification causes the same harm as a negligent one. Enforcement follows the Role Registry accountability assignments.

---

## 12. Related Documents

- Role Registry
- Identity And Credential Governance
- Audit And Accountability
- Recovery Rollback Incidents
- Stop State Policy
- Continuous Validation Policy
