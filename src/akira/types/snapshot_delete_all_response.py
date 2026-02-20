# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SnapshotDeleteAllResponse", "Error"]


class Error(BaseModel):
    id: str
    """Snapshot ID that failed to mark for deletion"""

    error: str
    """Error message"""


class SnapshotDeleteAllResponse(BaseModel):
    deleted_count: float
    """Number of snapshots marked for deletion"""

    deleted_ids: List[str]
    """Array of snapshot IDs marked for deletion"""

    message: str
    """Success message"""

    errors: Optional[List[Error]] = None
    """Array of deletion errors, if any"""
