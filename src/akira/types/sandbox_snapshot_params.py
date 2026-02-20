# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["SandboxSnapshotParams"]


class SandboxSnapshotParams(TypedDict, total=False):
    name: str
    """Custom snapshot name (auto-generated if not provided)"""

    quick: bool
    """Quick mode: fsfreeze only (faster but crash-consistent)"""
