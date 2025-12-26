# Architecture Overview

## Purpose
This project implements a GitOps-driven DevOps/SRE platform using cost-efficient
infrastructure while maintaining production-style operational standards.

The goal is not high availability at any cost, but **clarity, reproducibility,
and operational correctness**.

---

## High-Level Architecture

### Core Components
- **AWS EC2**: Single virtual machine hosting the platform
- **K3s**: Lightweight Kubernetes distribution
- **GitHub Actions**: CI pipeline for build and security checks
- **GitHub Container Registry (GHCR)**: Container image storage
- **Argo CD**: GitOps continuous deployment
- **Prometheus & Grafana**: Metrics and dashboards
- **Loki**: Centralized logging

---

## Data Flow

1. Developer pushes code to GitHub
2. GitHub Actions:
   - runs tests
   - builds container images
   - performs security scans
   - pushes images to GHCR
3. Argo CD continuously syncs Kubernetes manifests from Git
4. K3s reconciles desired state and runs workloads
5. Observability stack collects metrics and logs

---

## Failure Modes and Handling

### EC2 Failure
- All workloads are lost
- Recovery is achieved by:
  - recreating the instance using infrastructure code
  - re-syncing GitOps manifests
- Acceptable trade-off for cost-controlled environments

### Application Failure
- Kubernetes restarts pods automatically
- Liveness and readiness probes prevent bad deployments

### CI Failure
- Image is not published
- Argo CD does not deploy broken artifacts

---

## Assumptions

- Single user / learning-focused platform
- No strict uptime SLA
- Cost control is prioritized over redundancy
- All infrastructure is reproducible

---

## Cost Control Decisions

The following managed services were intentionally avoided:

- **EKS**: fixed control-plane cost regardless of usage
- **NAT Gateway**: hourly cost + data transfer charges
- **Application Load Balancer**: unnecessary for single-node ingress

Instead:
- Single EC2 + K3s provides Kubernetes experience at minimal cost
- Ingress is handled directly at node level

---

## Security Posture

### Publicly Accessible
- EC2 instance (ports 80/443 when enabled)
- GitHub repository (read-only)

### Restricted / Internal
- Kubernetes API (local only)
- Argo CD UI (port-forward access)
- Prometheus and Grafana (port-forward access)

No administrative services are exposed publicly by default.

---

## Summary

This architecture prioritizes:
- Git as the single source of truth
- Operational transparency
- Cost-awareness
- Realistic DevOps and SRE workflows
