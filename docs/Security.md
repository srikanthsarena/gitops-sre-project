# Security Practices

## Container Image Scanning

This project uses **Trivy** to scan container images for known vulnerabilities.

### Scan details
- Scan runs in CI
- OS and language vulnerabilities included
- Pipeline fails on HIGH or CRITICAL findings

### Why this matters
- Prevents vulnerable images from being deployed
- Enforces security gates early
- Aligns with DevSecOps best practices

## Future improvements
- Add SBOM generation
- Policy enforcement (OPA)
- Runtime security
