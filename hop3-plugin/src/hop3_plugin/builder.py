from __future__ import annotations

import subprocess

from hop3_host.protocols import BuildStrategy


class DockerBuildStrategy(BuildStrategy):
    """A build strategy that uses `docker build`."""

    name = "docker/smo"

    def __init__(self, context):
        self.context = context

    def accept(self) -> bool:
        """Accepts if a Dockerfile is present in the source directory."""
        dockerfile_path = self.context.source_path / "Dockerfile"
        return dockerfile_path.is_file()
        # TODO: If there is no Dockerfile, it should use a default one or generate one.
        # Let's keep this feature for later.

    def build(self):
        """Runs `docker build` and returns a docker-image artifact."""
        print("Building Docker image...")
