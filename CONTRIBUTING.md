# Contributing To The Governance-First Security Architecture Project

## Repository Scope

This repository is a documentation-only external review package.

It is not an implementation repository, production security design, security validation, compliance assessment, or legal opinion.

The current package status is `FROZEN_FOR_EXTERNAL_REVIEW`.

## Welcome Contributions

Contributions should focus on:

- identifying contradictions or ambiguous terminology,
- finding missing risks, stop states, or accountability boundaries,
- challenging unsafe assumptions,
- weakening unsupported claims,
- narrowing scope,
- improving citations and source dates,
- improving reviewer navigation and document consistency,
- recording review feedback through the revision process.

## Out Of Scope

Do not submit:

- implementation code,
- runtime or automation proposals presented as approved work,
- live integrations,
- active scanning or remediation behavior,
- security-agent capabilities,
- real personal data, secrets, credentials, incidents, or customer material,
- claims that the model is secure, compliant, certified, production-ready, or validated,
- prototype expansion without an explicit review-gate decision.

## Review Process

1. Open a focused review-feedback issue or prepare a narrow pull request.
2. Reference an existing feedback ID, or request a new anonymized feedback ID.
3. Describe the affected document and section.
4. Explain whether the change narrows scope, clarifies text, weakens a claim, or identifies a blocker.
5. Update `Governance-First-Security-Architecture-Post-Review-Revision-Log-v0.1.md` when feedback is accepted for revision.
6. Keep unrelated model expansion out of the same change.

## Privacy

Use reviewer roles or anonymized reviewer IDs. Do not add reviewer names, private messages, identifying employment details, or verbatim private feedback without explicit authorization.

Do not submit sensitive information through an issue or pull request.

## Acceptance Boundary

Merging documentation does not authorize implementation, production use, a security claim, a compliance claim, or a public release.

Only changes accepted into the canonical repository by the canonical maintainer become official project revisions. Review [GOVERNANCE.md](GOVERNANCE.md) and [PROJECT-IDENTITY.md](PROJECT-IDENTITY.md) before representing a fork or derivative publicly.

## Contribution License

By submitting a contribution, you agree that your contribution may be distributed under the repository's Creative Commons Attribution-ShareAlike 4.0 International license.

Only submit material that you have the right to contribute. Clearly identify third-party material and its license or permission status.

Implementation code remains out of scope. The possible future MPL-2.0 code license is not active and does not apply to current contributions.
