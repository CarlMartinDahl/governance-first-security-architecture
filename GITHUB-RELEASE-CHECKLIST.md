# GitHub Release Checklist

## Current Release Decision

```text
Local release candidate: LOCALLY_VALIDATED
Initial GitHub visibility: PRIVATE
Public release: PENDING_PRIVATE_RENDER_REVIEW
Implementation repository: NO
GitHub Actions: NOT_ENABLED
```

## Repository Boundary

- [x] Git repository root is this project folder, not its parent folder.
- [x] No unrelated sibling project is staged.
- [x] `tmp/`, `output/`, `.DS_Store`, local credentials, and editor artifacts are ignored.
- [x] No remote has been added before repository visibility is confirmed.
- [x] Local commit author uses the public project identity rather than a private relay or machine identity.

## Content Boundary

- [x] README reflects the current freeze, review, and commercial-discovery status.
- [x] Reviewer bundles use role-based names only.
- [x] Feedback records use anonymized reviewer IDs.
- [x] No private reviewer quotes or private source documents are included.
- [x] No real personal data, secrets, credentials, customer data, or incident data are included.
- [x] No implementation, runtime, automation, live integration, scanning, remediation, or security-agent behavior is included.
- [x] No security, compliance, certification, production-readiness, product-market-fit, or venture-scale claim is made.

## Review Quality

- [x] All Markdown file references resolve.
- [x] Historical next-document sections are clearly marked as historical.
- [x] Current status is qualitative and does not use unsupported maturity percentages.
- [x] Current lifecycle and operational modes are consistently identified as `LM-1_REVIEW_PACKAGE` and `ODM-3_APPROVED_DOCUMENTATION_CHANGE`.
- [x] Action, risk, evidence, egress, stop-state, and role vocabulary differences are normalized or mapped explicitly.
- [x] Referenced project filenames and Markdown links resolve with exact case.
- [x] Time-sensitive legal, standards, provider, and platform references include a source and review date where material.

## GitHub Governance

- [x] `CONTRIBUTING.md` matches the documentation freeze.
- [x] `SECURITY.md` prohibits sensitive material in public issues.
- [x] `CODE_OF_CONDUCT.md` defines participation and confidential-reporting expectations.
- [x] `LICENSE` contains the canonical CC BY-SA 4.0 legal code and `NOTICE.md` carries project-specific scope notes.
- [x] `ATTRIBUTION.md` identifies Martin Dahl, the canonical source, material-change disclosure, and no-endorsement wording.
- [x] `GOVERNANCE.md` and `PROJECT-IDENTITY.md` distinguish official project revisions from independent forks and derivatives.
- [x] `CITATION.cff` contains machine-readable project citation metadata.
- [x] Future MPL-2.0 code licensing is separated from the current documentation license and does not authorize implementation.
- [x] Pull requests require scope, claim, privacy, and authorization checks.
- [x] Review feedback is linked to the post-review revision log.
- [x] No automated workflow is enabled during the current freeze.

## Private Launch Gate

A private GitHub repository may be created only after all repository-boundary and content-boundary checks pass.

Recommended first tag after review:

```text
review-v0.1
```

## Private Repository Verification

After the private repository is created and before any public release:

- [ ] Confirm GitHub displays the intended author identity on the initial commit.
- [ ] Confirm GitHub detects the CC BY-SA 4.0 license.
- [ ] Create the `review-feedback` label used by the issue form.
- [ ] Enable GitHub private vulnerability reporting.
- [ ] Verify a private conduct-reporting contact route.
- [ ] Review README, index, issue form, pull-request template, links, and rendered Markdown in GitHub.
- [ ] Confirm GitHub renders the intended citation metadata and canonical repository URL.
- [ ] Confirm repository topics, description, and visibility contain no unsupported claim.

## Public Release Gate

Before changing repository visibility to public:

- [ ] Public release is explicitly approved after private rendering is reviewed.
- [x] CC BY-SA 4.0 is selected for original project documentation.
- [x] Official project name, canonical source, attribution, and independent-fork language are explicit.
- [x] Third-party materials are excluded from the project license unless separately permitted.
- [x] Reviewers remain anonymized.
- [x] Legal and regulatory references are linked to current primary sources and bounded against compliance claims.
- [x] Provider policy references are re-verified for the documentation boundary; implementation-specific permission remains unverified and unauthorized.
- [ ] Private vulnerability reporting and the private conduct-reporting route are verified.
- [ ] A final private-render review confirms that no private or sensitive material remains in tracked content.

Changing repository visibility does not authorize implementation or alter the documentation freeze.
