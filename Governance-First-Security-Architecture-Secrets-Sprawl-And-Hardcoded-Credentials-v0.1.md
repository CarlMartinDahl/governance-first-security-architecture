# Governance-First Security Architecture
## Secrets Sprawl And Hardcoded Credentials Policy
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy governs the detection, prevention, and remediation of secrets sprawl — the condition in which cryptographic secrets, API keys, tokens, passwords, and credentials exist outside of designated secret management systems. Hardcoded credentials in source code, CI/CD pipelines, configuration files, and container images are among the most reliably exploited vulnerabilities in real-world breach investigations.

A secret found in a repository must be treated as compromised from the moment of first commit — regardless of whether the repository is private.

---

## 2. Scope

Covers all secrets used by the organisation: API keys, OAuth tokens, database credentials, private keys, certificates, webhook secrets, CI/CD pipeline variables, infrastructure-as-code secrets, and any value that grants access to a system or validates identity.

---

## 3. Core Governance Principle

> **A secret committed to version control is a secret that must be rotated immediately and unconditionally. The commit history, not the current file state, defines exposure.**

Deleting a secret from the current HEAD of a repository does not remove it from history. Treat exposure as confirmed from the timestamp of the original commit.

---

## 4. Prohibited Patterns

The following are prohibited in all code, configuration, and infrastructure files committed to any version control system, regardless of repository visibility:

- Plaintext API keys, tokens, or passwords in any file
- Secrets in environment variable files (`.env`, `.env.local`, etc.) committed to version control
- Private keys (PEM, PPK, or equivalent formats) in any committed file
- Credentials in CI/CD pipeline definitions (GitHub Actions, GitLab CI, Jenkinsfile, etc.) as literal values
- Connection strings containing embedded credentials
- Secrets in Docker images, Dockerfiles, or Kubernetes manifests committed to repositories
- Secrets in commented-out code

---

## 5. Required Controls

### Pre-commit Detection
- All developer workstations and CI/CD pipelines must have secret scanning enabled before commit
- Pre-commit hooks must reject commits containing patterns matching known secret formats
- Detection tooling must be reviewed and updated at minimum quarterly to cover new secret formats

### Repository Scanning
- All repositories (including private and archived) must be scanned for historical secret exposure at minimum monthly
- New repositories must be scanned within 24 hours of creation
- Scan results feed directly into the remediation workflow defined in Section 7

### Secret Management System
- All secrets must be stored in a designated secret management system with audit logging
- Access to secrets must be scoped to the minimum required identity and time window
- Secrets must not be passed between systems as plaintext environment variables in production

---

## 6. Secret Lifecycle

All secrets follow the lifecycle defined in Identity And Credential Governance with the following additions:

| Phase | Requirement |
|---|---|
| Creation | Generated with cryptographic randomness; minimum entropy requirements per type |
| Storage | Secret management system only; never plaintext at rest |
| Transmission | Encrypted channel only; never in URLs, headers logged by default, or query strings |
| Rotation | Scheduled rotation per type (see Section 6.1); immediate rotation on suspected exposure |
| Revocation | Revocation must be confirmed active before rotation is considered complete |
| Disposal | Deletion confirmed in secret management system; all copies accounted for |

### 6.1 Rotation Schedule

| Secret Type | Maximum Lifetime | On Exposure |
|---|---|---|
| CI/CD tokens | 90 days | Immediate rotation |
| API keys (external services) | 180 days | Immediate rotation |
| Database credentials | 90 days | Immediate rotation |
| Service account passwords | 90 days | Immediate rotation |
| Private keys / certificates | Per certificate validity; max 1 year | Immediate revocation and reissue |

---

## 7. Remediation Workflow

When a secret is detected outside a designated secret management system:

1. **Classify** — determine the secret type, systems it grants access to, and blast radius
2. **Revoke** — disable or revoke the secret in the issuing system immediately; do not wait for rotation to be ready
3. **Rotate** — issue a new secret through proper channels and deploy it to all consuming systems
4. **Assess exposure** — review access logs of the system the secret grants access to, from the timestamp of first commit exposure forward
5. **Purge history** (where feasible) — use repository history rewriting tools if the repository is not yet public; treat as cosmetic only if already public or cloned
6. **Document** — record in the Audit and Accountability system: what was exposed, when, for how long, what access was possible, what was observed in logs
7. **Root cause** — identify why the secret was committed and update controls to prevent recurrence

---

## 8. CI/CD Pipeline Governance

- Pipeline secrets must be stored as encrypted pipeline variables in the CI/CD platform, not as literal values in pipeline definition files
- Pipeline secret access must be scoped to the minimum required job and environment
- Pipeline logs must not contain secret values; log scrubbing must be verified
- Pipeline service accounts must follow the same lifecycle and rotation requirements as other credentials
- Third-party GitHub Actions and CI/CD plugins must be pinned to a specific commit SHA, not a floating tag, to prevent supply chain injection of secret-harvesting code

---

## 9. Container And Infrastructure Governance

- Container images must be scanned for embedded secrets before push to any registry
- Kubernetes secrets must be encrypted at rest in etcd
- Infrastructure-as-code templates must not contain literal secret values; all secrets must reference the secret management system
- Immutable infrastructure deployments must verify that no secrets are baked into base images

---

## 10. Related Documents

- Identity And Credential Governance
- Vendor Offboarding And Revocation
- Audit And Accountability
- Supply Chain Abuse Cases
- Capability Change Gate
