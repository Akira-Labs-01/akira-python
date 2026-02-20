# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SandboxCloneResponse", "Sandbox", "Snapshot"]


class Sandbox(BaseModel):
    id: str
    """Sandbox ID"""

    cpu: float
    """CPU count (API units)"""

    created_at: str
    """Creation timestamp"""

    memory: float
    """Memory size in MiB"""

    name: str
    """Sandbox name"""

    status: str
    """Sandbox status"""

    storage: float
    """Storage size in GB"""


class Snapshot(BaseModel):
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


class SandboxCloneResponse(BaseModel):
    sandbox: Sandbox

    snapshot: Snapshot
