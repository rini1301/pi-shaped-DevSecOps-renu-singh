# DevSecOps CI/CD Pipeline – Security Scanning

This repository demonstrates the integration of security tools in a CI/CD pipeline to detect vulnerabilities early in the software development lifecycle.  

---

## 🔄 Pipeline Steps

1. **Code Checkout**  
   Source code is pulled from the repository.

2. **Static Analysis (SAST)**  
   - **Bandit** scans Python code for security issues (e.g., hardcoded secrets, weak cryptography, unsafe function calls).  
   - **Semgrep** performs static code analysis with customizable security rules.

3. **Dependency & Image Scanning (SCA + Container Security)**  
   - **Trivy** scans OS packages, libraries, and base container images for known CVEs.

4. **Dynamic Application Security Testing (DAST)**  
   - **OWASP ZAP** scans the running application for runtime vulnerabilities like SQL Injection, XSS, and misconfigurations.

5. **Report & Action**  
   - Vulnerabilities are reported with severity levels (LOW, MEDIUM, HIGH, CRITICAL).  
   - Developers/DevOps engineers must review and fix them before production deployment.

---

## 📊 Findings

- **Bandit** flagged issues related to possible hardcoded secrets and unsafe code patterns.  
- **Semgrep** identified insecure coding practices.  
- **Trivy** detected outdated base images and vulnerable dependencies.  
- **OWASP ZAP** reported potential misconfigurations and runtime risks (XSS, SQLi).  

---

## 💡 Core Concept Questions

### 🔹 Pipeline Integration
**Q1: Why is it important to run Trivy scans (for OS packages and dependencies) as part of the CI/CD pipeline instead of only scanning after deployment?**  
- Because vulnerabilities in base images and dependencies can be caught early before deployment.  
- Early detection prevents insecure images from being promoted to staging/production, reducing remediation costs.  
- Shifting security left ensures only compliant and patched images are deployed.

**Q2: Why is it important to run security scans (SAST, dependency scanning, DAST) directly in the CI/CD pipeline instead of only during production?**  
- Security issues are cheaper and faster to fix in development than in production.  
- CI/CD scans prevent insecure code from being merged.  
- Continuous scanning builds a security-first culture and reduces the attack surface before deployment.

---

### 🔹 Tool Roles
**Q3: How do Bandit, Semgrep, Trivy, and OWASP ZAP complement each other in the pipeline?**  

- **Bandit** → Detects Python-specific issues (e.g., hardcoded secrets, unsafe `eval()` usage).  
- **Semgrep** → Finds insecure patterns using customizable rules (e.g., missing input validation).  
- **Trivy** → Identifies vulnerable OS packages & dependencies in Docker images (e.g., CVEs in OpenSSL).  
- **OWASP ZAP** → Finds runtime/web vulnerabilities (e.g., SQL Injection, XSS) that static analysis can’t detect.  

Each tool covers different layers → code, dependencies, and runtime. Together, they provide defense-in-depth.  

---

### 🔹 Developer Actionability
**Q4: If Trivy reports a HIGH severity vulnerability in a base image or Bandit flags hardcoded secrets, what should the developer or DevOps engineer do next?**  

- **For Trivy (base image CVE):**  
  - Upgrade to a patched base image version.  
  - Replace vulnerable dependencies with secure versions.  
  - Rebuild and rescan the image to verify the fix.  

- **For Bandit (hardcoded secrets):**  
  - Remove secrets from source code immediately.  
  - Store credentials in environment variables or a secure secret manager (e.g., Vault, AWS Secrets Manager).  
  - Rotate any exposed keys/passwords since they may already be compromised.  

---

✅ By integrating all these tools in CI/CD, we achieve **shift-left security**, ensuring vulnerabilities are caught and fixed early instead of waiting until production.  
