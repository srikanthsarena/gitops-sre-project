# GitOps SRE Platform (K3s + AWS EC2 + GHCR)

A production-style DevOps/SRE reference platform built with low-cost infrastructure and enterprise practices.

## What this project demonstrates
- GitOps with Argo CD
- Kubernetes using K3s on a single EC2 instance
- CI with GitHub Actions
- Container registry using GitHub Container Registry (GHCR)
- Observability with Prometheus, Grafana, Loki
- Security scanning and policy-as-code
- SLOs, alerting, and operational runbooks

## Repository Structure
- apps/            → application services
- infrastructure/  → Terraform and cloud provisioning
- gitops/          → Argo CD applications and environments
- observability/   → dashboards, alerts, monitoring configs
- security/        → scanning and policy definitions
- runbooks/        → operational playbooks
- docs/adr/        → architecture decision records

This repository is built incrementally over few days to reflect senior-level DevOps/SRE practices.


# Release Checklist

Before creating a release:

- [ ] CI pipeline is green on `main`
- [ ] Container images are published to GHCR
- [ ] Argo CD application is `Synced` and `Healthy`
- [ ] CHANGELOG updated
- [ ] Version number chosen (SemVer)
- [ ] Git tag created
- [ ] GitHub Release published

## Rollback strategy

- Revert Argo CD to a previous Git tag
- Images are immutable and reproducible
