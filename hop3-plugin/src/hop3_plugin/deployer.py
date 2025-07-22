from __future__ import annotations

from hop3_host.protocols import DeploymentStrategy


class DockerDeploymentStrategy(DeploymentStrategy):
    name = "docker-deploy"

    def __init__(self, context, artifact):
        self.context = context
        self.artifact = artifact

    def accept(self) -> bool:
        return self.artifact.kind == "docker-image"

    def deploy(self, deltas: dict[str, int] | None = None):
        """Orchestrates the deployment by calling the private helper methods."""
        print("Starting Docker deployment...")
