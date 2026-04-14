---
name: red-teaming
description: Offensive security methodology, PTES phases, and ethical hacking protocols.
---

# Red Teaming & Penetration Testing

## Core Philosophy

> "Think like an attacker. Find weaknesses before malicious actors do."

## Methodology: PTES Phases

1. **PRE-ENGAGEMENT**: Define scope, rules of engagement, authorization
2. **RECONNAISSANCE**: Passive → Active information gathering
3. **THREAT MODELING**: Identify attack surface and vectors
4. **VULNERABILITY ANALYSIS**: Discover and validate weaknesses
5. **EXPLOITATION**: Demonstrate impact (Proof of Concept only)
6. **POST-EXPLOITATION**: Privilege escalation (Theoretical only)
7. **REPORTING**: Document findings with evidence

---

## Attack Surface Categories

### OWASP Top 10 Focus
- **Broken Access Control**: IDOR, privilege escalation, SSRF
- **Security Misconfiguration**: Cloud configs, headers, defaults
- **Supply Chain Failures**: Deps, CI/CD, lock file integrity
- **Cryptographic Failures**: Weak encryption, exposed secrets
- **Injection**: SQL, command, LDAP, XSS
- **Insecure Design**: Business logic flaws
- **Auth Failures**: Weak passwords, session issues

---

## Vulnerability Prioritization

**Risk Assessment Formula:**
$$ Risk = Likelihood \times Impact $$

| Severity | Action |
|----------|--------|
| **Critical** | Immediate report, stop testing if data at risk |
| **High** | Report same day |
| **Medium** | Include in final report |
| **Low** | Document for completeness |

---

## Reporting Principles

**Structure:**
1. **Executive Summary**: Business impact, risk level
2. **Findings**: Vulnerability, evidence, impact
3. **Remediation**: How to fix, priority
4. **Technical Details**: Steps to reproduce

**Evidence:**
- Screenshots with timestamps
- Request/response logs
- Sanitized sensitive data

---

## Ethical Boundaries (MANDATORY)

- [ ] Written authorization before testing
- [ ] Stay within defined scope
- [ ] Report critical issues immediately
- [ ] Protect discovered data
- [ ] Document all actions
- [ ] **NEVER** Denial of Service (DoS)
- [ ] **NEVER** Social Engineering without explicit scope
