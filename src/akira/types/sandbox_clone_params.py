# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SandboxCloneParams", "Resources"]


class SandboxCloneParams(TypedDict, total=False):
    image: str
    """Docker image override"""

    name: str
    """
    Name for the cloned sandbox (auto-generated as
    {source-sandbox-name}-clone-{timestamp} if not provided)
    """

    resources: Resources
    """Resource overrides for cloned sandbox (storage inherited from source)"""

    snapshot_name: str
    """Custom name for intermediate snapshot (auto-generated if not provided)"""

    wait_for_ready: bool
    """Wait for sandbox to be ready"""


class Resources(TypedDict, total=False):
    """Resource overrides for cloned sandbox (storage inherited from source)"""

    cpus: int
    """Number of CPUs (minimum: 1)"""

    memory: int
    """Memory size in MiB"""
