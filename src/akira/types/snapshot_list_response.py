# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SnapshotListResponse", "Data", "Pagination"]


class Data(BaseModel):
    id: str
    """Snapshot ID (Kubernetes UID)"""

    created_at: str
    """Creation timestamp"""

    name: str
    """Snapshot name"""

    status: Literal["creating", "ready", "error", "pending_deletion"]
    """Snapshot status"""

    depends_on: Optional[List[str]] = None
    """PVCs that depend on this snapshot (clones).

    Snapshot cannot be deleted until these are removed.
    """

    size: Optional[str] = None
    """Restore size"""


class Pagination(BaseModel):
    """Pagination metadata"""

    page: float
    """Current page number"""

    page_size: float
    """Number of items per page"""

    total_items: float
    """Total number of items"""

    total_pages: float
    """Total number of pages"""


class SnapshotListResponse(BaseModel):
    data: List[Data]
    """Array of snapshots"""

    pagination: Pagination
    """Pagination metadata"""
