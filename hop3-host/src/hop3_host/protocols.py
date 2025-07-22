# Copyright (c) 2024-2025, Abilian SAS
from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Protocol


#
# --- Protocols (Interfaces for the Strategies) ---
#
class BuildStrategy(Protocol):
    """Interface for turning source code into a runnable artifact."""

    name: str

    # @property
    # def name(self) -> str:
    #     """A unique name for the strategy, e.g., 'buildpack' or 'docker'."""

    def accept(self) -> bool:
        """Return True if this strategy can build the app."""

    def build(self):
        """Execute the build process and return an artifact."""


class DeploymentStrategy(Protocol):
    """Interface for running a build artifact."""

    name: str

    # @property
    # def name(self) -> str:
    #     """A unique name, e.g., 'uwsgi' or 'docker-compose'."""

    def accept(self) -> bool:
        """Return True if this target can deploy the given artifact."""

    def deploy(self) -> dict:
        """
        Deploy the artifact.
        Returns a dictionary with deployment details for the proxy,
        e.g., {"protocol": "http", "host": "127.0.0.1", "port": 8000}.
        """
