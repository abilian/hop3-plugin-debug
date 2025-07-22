from __future__ import annotations

from hop3_host.hooks import hop3_hook_impl
from hop3_host.protocols import BuildStrategy, DeploymentStrategy

from .builder import DockerBuildStrategy
from .deployer import DockerDeploymentStrategy


class DockerPlugin:
    name = "docker-plugin"

    @hop3_hook_impl
    def get_build_strategies(self) -> list[type[BuildStrategy]]:
        print("Registering Docker build strategy")
        return [DockerBuildStrategy]

    @hop3_hook_impl
    def get_deployment_strategies(self) -> list[type[DeploymentStrategy]]:
        print("Registering SMO deployment strategy")
        return [DockerDeploymentStrategy]
