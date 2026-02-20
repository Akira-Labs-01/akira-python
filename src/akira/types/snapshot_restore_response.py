# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SnapshotRestoreResponse"]


class SnapshotRestoreResponse(BaseModel):
    id: str
    """Sandbox ID"""

    cpu: float
    """CPU count (API units, minimum 1)"""

    created_at: str
    """Creation timestamp"""

    memory: float
    """Memory size in MB"""

    name: str
    """Sandbox name"""

    status: str
    """Sandbox status"""

    storage_id: Optional[str] = None
    """ID of the attached storage volume"""

    storage_name: Optional[str] = None
    """Name of the attached storage volume"""
