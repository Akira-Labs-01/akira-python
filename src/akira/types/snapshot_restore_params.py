# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SnapshotRestoreParams", "Resources"]


class SnapshotRestoreParams(TypedDict, total=False):
    name: Required[str]
    """Name for the restored sandbox"""

    image: str
    """Docker image override"""

    resources: Resources
    """Resource overrides for restored sandbox"""

    wait_for_ready: bool
    """Wait for sandbox to be ready"""


class Resources(TypedDict, total=False):
    """Resource overrides for restored sandbox"""

    cpus: int
    """Number of CPUs (minimum: 1, 1 CPU = 0.25 Kubernetes vCPU)"""

    memory: int
    """Memory size in MiB"""

    storage: str
    """Storage size (must be >= snapshot size)"""
