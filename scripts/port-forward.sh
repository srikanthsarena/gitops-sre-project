#!/bin/bash

echo "Waiting for Kubernetes cluster..."

# Wait until cluster API is reachable
until kubectl cluster-info &> /dev/null
do
  sleep 2
done

echo "Starting GitOps project port-forwards..."

# Kill existing port-forwards if running
pkill -f "kubectl port-forward" 2>/dev/null

# User Service (local 8000 -> cluster 8000)
kubectl -n gitops-apps port-forward svc/user-service 8000:8000 &

# Order Service (local 8001 -> cluster 8000)
kubectl -n gitops-apps port-forward svc/order-service 8001:8000 &

# ArgoCD UI
kubectl -n argocd port-forward svc/argocd-server 8080:443 &

# Prometheus
kubectl -n gitops-apps port-forward svc/prometheus 9090:9090 &

# Grafana
kubectl -n gitops-apps port-forward svc/grafana 3000:3000 &

echo "All port-forwards started."
