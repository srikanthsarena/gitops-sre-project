## Policy Enforcement (OPA)

This project uses **OPA via Conftest** to enforce Kubernetes standards in CI.

### Policies enforced
- No privileged containers
- No `:latest` image tags
- Mandatory readiness probes

### Enforcement point
- Policies run during CI
- PRs are blocked if violations exist

This prevents insecure or unstable workloads from reaching the cluster.
