package kubernetes

# Deny :latest images
deny contains msg if {
	input.kind == "Deployment"
	some i
	container := input.spec.template.spec.containers[i]
	endswith(container.image, ":latest")
	msg := sprintf(
		"Deployment %s uses :latest image for container %s",
		[input.metadata.name, container.name],
	)
}

# Require resource requests
deny contains msg if {
	input.kind == "Deployment"
	some i
	container := input.spec.template.spec.containers[i]
	not container.resources.requests
	msg := sprintf(
		"Deployment %s missing resources.requests for container %s",
		[input.metadata.name, container.name],
	)
}

# Require resource limits
deny contains msg if {
	input.kind == "Deployment"
	some i
	container := input.spec.template.spec.containers[i]
	not container.resources.limits
	msg := sprintf(
		"Deployment %s missing resources.limits for container %s",
		[input.metadata.name, container.name],
	)
}

# Require standard label
deny contains msg if {
	not input.metadata.labels["app.kubernetes.io/name"]
	msg := sprintf(
		"Object %s/%s missing label app.kubernetes.io/name",
		[input.kind, input.metadata.name],
	)
}
