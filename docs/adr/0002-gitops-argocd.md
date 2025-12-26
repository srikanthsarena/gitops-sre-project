# ADR 0002: GitOps Deployment with Argo CD

## Status
Accepted

## Context
Manual Kubernetes deployments lead to configuration drift,
poor auditability, and unreliable rollback procedures.

## Decision
Adopt GitOps using Argo CD, with Git as the single source of truth.

## Consequences
### Positive
- Declarative, auditable deployments
- Easy rollback through Git history
- Automatic drift detection and reconciliation

### Negative
- Initial learning curve
- Requires disciplined Git practices

This approach aligns with modern production SRE standards.
