# ADR 0001: Use Single-Node K3s on EC2

## Status
Accepted

## Context
Running a managed Kubernetes service (EKS) introduces a fixed control-plane cost.
For a learning and portfolio-focused platform, this cost outweighs the benefits.

## Decision
Use K3s running on a single AWS EC2 instance.

## Consequences
### Positive
- No Kubernetes control-plane cost
- Full Kubernetes API and behavior
- Faster bootstrap and teardown

### Negative
- No high availability
- Node failure causes full outage

This trade-off is acceptable for a cost-controlled, reproducible environment.
