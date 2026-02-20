# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SandboxSnapshotResponse"]


class SandboxSnapshotResponse(BaseModel):
    id: str
    """Snapshot ID (Kubernetes UID)"""

    consistency: Literal["application", "crash"]
    """Snapshot consistency level"""

    created_at: str
    """Creation timestamp"""

    name: str
    """Snapshot name"""

    source_sandbox_id: str
    """Source sandbox ID"""

    source_sandbox_name: str
    """Source sandbox name"""

    status: Literal["creating", "ready", "error"]
    """Snapshot status"""
