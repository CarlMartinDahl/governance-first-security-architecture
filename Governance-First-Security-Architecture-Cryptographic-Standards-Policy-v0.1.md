# Governance-First Security Architecture
## Cryptographic Standards Policy
**Version:** 0.1 — Initial Release
**Status:** Active
**Classification:** Governance Policy

---

## 1. Purpose

This policy defines which cryptographic algorithms, key lengths, and protocols are approved, deprecated, or prohibited across the organisation's systems and data. Cryptography is the technical foundation of confidentiality, integrity, and authenticity — but its value degrades over time as computational power increases and weaknesses are discovered. Governance over cryptographic choices prevents the silent accumulation of weak cryptography that appears to work until it is exploited.

This policy complements Post-Quantum And Future AI Readiness, which addresses long-term crypto-agility strategy. This document addresses current operational standards.

---

## 2. Scope

Applies to all cryptographic operations performed by or on behalf of the organisation: data encryption at rest, data encryption in transit, digital signatures, certificate management, password hashing, key exchange, and random number generation.

---

## 3. Core Governance Principle

> **Cryptographic choices are governance decisions. The use of a prohibited algorithm is a finding requiring remediation regardless of the system's age, the effort required to change it, or whether exploitation has been observed. "It hasn't been broken yet" is not a risk acceptance position.**

---

## 4. Approved Algorithms

### 4.1 Symmetric Encryption
| Algorithm | Key Length | Status | Notes |
|---|---|---|---|
| AES-GCM | 256-bit | ✅ Approved | Preferred for authenticated encryption |
| AES-CBC | 256-bit | ✅ Approved | Requires separate integrity check (HMAC) |
| AES-GCM | 128-bit | ⚠️ Conditionally approved | Permitted for low-sensitivity, high-performance contexts with documented justification |
| ChaCha20-Poly1305 | 256-bit | ✅ Approved | Preferred where hardware AES acceleration unavailable |

### 4.2 Asymmetric Encryption And Key Exchange
| Algorithm | Key Length | Status | Notes |
|---|---|---|---|
| RSA-OAEP | 3072-bit minimum | ✅ Approved | 4096-bit preferred for new implementations |
| RSA | 2048-bit | ⚠️ Legacy only | Permitted for existing systems; not for new implementations; migration required by review date |
| ECDH / ECDSA | P-256, P-384 | ✅ Approved | P-384 preferred for high-sensitivity contexts |
| X25519 / Ed25519 | — | ✅ Approved | Preferred for new key exchange and signature implementations |
| Diffie-Hellman | < 2048-bit | 🚫 Prohibited | |

### 4.3 Hashing
| Algorithm | Status | Notes |
|---|---|---|
| SHA-256 | ✅ Approved | Minimum for integrity and signature use |
| SHA-384 / SHA-512 | ✅ Approved | Preferred for high-sensitivity and long-term integrity |
| SHA-3 | ✅ Approved | Approved alternative |
| SHA-1 | 🚫 Prohibited | Collision attacks demonstrated; no exceptions |
| MD5 | 🚫 Prohibited | Broken; no exceptions, including non-security uses |
| MD4, MD2 | 🚫 Prohibited | |

### 4.4 Password And Secret Hashing
| Algorithm | Status | Notes |
|---|---|---|
| Argon2id | ✅ Approved — Preferred | OWASP recommended; use with minimum memory 64MB, iterations 3, parallelism 4 |
| bcrypt | ✅ Approved | Minimum cost factor 12 |
| scrypt | ✅ Approved | Minimum N=32768 |
| PBKDF2-HMAC-SHA256 | ⚠️ Conditionally approved | Minimum 600,000 iterations; only where Argon2id/bcrypt unavailable |
| SHA-256 / SHA-512 (unsalted or single-round) | 🚫 Prohibited | Not suitable for password storage regardless of iteration count |
| MD5 / SHA-1 (any use for passwords) | 🚫 Prohibited | |
| Plaintext password storage | 🚫 Prohibited | No exceptions |

### 4.5 Transport Layer Security
| Protocol / Configuration | Status | Notes |
|---|---|---|
| TLS 1.3 | ✅ Approved — Preferred | |
| TLS 1.2 with approved cipher suites | ✅ Approved | Cipher suites must exclude RC4, 3DES, and export-grade; forward secrecy required |
| TLS 1.1 | 🚫 Prohibited | |
| TLS 1.0 | 🚫 Prohibited | |
| SSL 3.0 and below | 🚫 Prohibited | |
| Self-signed certificates in production | 🚫 Prohibited | Permitted in isolated test environments only |

### 4.6 Random Number Generation
- Cryptographic operations must use a cryptographically secure pseudo-random number generator (CSPRNG)
- Language-standard `rand()`, `Math.random()`, and equivalent non-cryptographic RNG functions are prohibited for any security-relevant purpose
- Entropy sources must be appropriate for the platform (OS-provided CSPRNG preferred)

---

## 5. Certificate Governance

- All public-facing TLS certificates are issued by a trusted public CA; self-signed certificates are prohibited in production
- Certificate validity period: maximum 1 year for public-facing; maximum 2 years for internal
- Certificate expiry is monitored with automated alerting at 60 days, 30 days, and 7 days before expiry
- An expired certificate in production is a Stop State condition for the affected service
- Certificate inventory is maintained in the Asset Register with owner, expiry date, and renewal owner
- Wildcard certificates are used only where operationally necessary; each use is documented and reviewed annually
- Certificate revocation (via CRL or OCSP) must be validated by clients; services that do not check revocation are a finding

---

## 6. Key Management

- All cryptographic keys are stored in the designated secret management system; no key material is stored in source code, configuration files, or environment variables in plaintext
- Key generation follows entropy requirements for the algorithm and key length
- Key rotation follows the schedule in Secrets Sprawl And Hardcoded Credentials Policy
- Key access is logged; all key usage events are auditable
- Key destruction must be confirmed and documented; destroyed keys cannot be reconstructed
- Hardware Security Modules (HSMs) are required for Tier 0 key material (root CA keys, signing keys for identity infrastructure)

---

## 7. Exception Process

Use of a conditionally approved or prohibited algorithm may be required for legacy system interoperability or third-party constraints. Exceptions:

- Require named approval from the Cryptographic Governance role
- Must document: which prohibited algorithm, which system, why it cannot be changed, what compensating controls are in place, and a hard remediation deadline
- Are reviewed at every governance cycle; they do not auto-renew
- Prohibited algorithms (MD5, SHA-1, SSL, TLS 1.0/1.1) have no exception path for new implementations — exceptions apply to existing systems only and only with a migration timeline

---

## 8. Discovery And Remediation

- All systems are scanned for use of prohibited algorithms at minimum quarterly
- New systems are assessed for cryptographic compliance before deployment under the Capability Change Gate
- Findings are tracked in the vulnerability register under Vulnerability Disclosure And Patch Governance with severity:
  - Prohibited algorithm in use protecting Restricted data: **Critical**
  - Prohibited algorithm in use protecting Confidential data: **High**
  - Prohibited algorithm in use in non-sensitive context: **Medium**

---

## 9. Post-Quantum Transition

This policy reflects current (pre-quantum) cryptographic standards. The transition to post-quantum cryptography is governed by Post-Quantum And Future AI Readiness. When NIST-standardised post-quantum algorithms (ML-KEM, ML-DSA, SLH-DSA) are ready for operational deployment, this policy will be updated to include them as approved and to begin the deprecation timeline for classical asymmetric algorithms.

Crypto-agility — the ability to replace cryptographic primitives without re-architecting systems — is a design requirement for all new systems.

---

## 10. Related Documents

- Post-Quantum And Future AI Readiness
- Secrets Sprawl And Hardcoded Credentials Policy
- Identity And Credential Governance
- Data Classification And Handling Policy
- Asset Register
- Capability Change Gate
- Vulnerability Disclosure And Patch Governance
- Log Integrity And Tamper-Evidence Policy
