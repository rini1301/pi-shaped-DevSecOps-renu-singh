# 🔐 Core Concepts in DevSecOps

## 1. What is Shift-Left Security and Why is it Important?
Shift-left security means integrating security practices **early in the software development lifecycle (SDLC)** rather than waiting until later stages (like deployment or production).  
- It ensures vulnerabilities (e.g., exposed secrets, insecure code) are caught **when they are cheaper and easier to fix**.  
- In DevSecOps, shift-left security helps developers take ownership of security, making it part of the CI/CD pipeline.  
- This approach reduces risk, increases confidence in releases, and avoids costly security fixes late in the process.

---

## 2. How Does Detecting Secrets Early in the CI/CD Pipeline Prevent Production Vulnerabilities?
- Secrets like **API keys, database passwords, and cloud tokens** can allow attackers to access sensitive systems if exposed.  
- By scanning for secrets during **code commits or CI/CD builds**, you stop them before they ever reach production.  
- This prevents accidental leaks to GitHub, Docker images, logs, or monitoring tools.  
- Early detection also keeps your repository compliant with organizational and industry standards (e.g., SOC2, ISO, GDPR).

---

## 3. Strategies to Store Secrets Securely Instead of Hardcoding
Instead of embedding secrets directly in code:
- **Environment variables**: Store secrets in a `.env` file (ignored in version control) and load them at runtime.  
- **Secrets managers**: Use tools like AWS Secrets Manager, HashiCorp Vault, Azure Key Vault, or GitHub Actions Secrets.  
- **Configuration management**: Tools like Ansible, Kubernetes Secrets, or Helm can inject secrets securely at deployment.  
- **Encryption**: Encrypt sensitive files and use access-controlled decryption during build/deployment.

---

## 4. Situations Where Secrets Could Still Be Exposed & How to Prevent It
Even after scanning, secrets can still leak in cases such as:
- **Logs**: If applications log sensitive values (e.g., printing tokens for debugging).  
- **Misconfigured access controls**: If cloud IAM roles or CI/CD service accounts have overly broad permissions.  
- **Third-party integrations**: Accidentally pushing secrets to external monit
