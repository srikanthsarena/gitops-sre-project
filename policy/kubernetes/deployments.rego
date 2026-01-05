package kubernetes.deployments

# Rule 1: No privileged containers
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  container.securityContext.privileged == true
  msg := sprintf("Privileged container not allowed: %s", [container.name])
}

# Rule 2: No :latest image tags
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  endswith(container.image, ":latest")
  msg := sprintf("Image tag ':latest' is not allowed: %s", [container.image])
}

# Rule 3: Readiness probe is mandatory
deny[msg] {
  input.kind == "Deployment"
  container := input.spec.template.spec.containers[_]
  not container.readinessProbe
  msg := sprintf("Container %s must define a readinessProbe", [container.name])
}
