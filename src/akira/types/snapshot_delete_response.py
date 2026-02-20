# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["SnapshotDeleteResponse"]


class SnapshotDeleteResponse(BaseModel):
    deferred: bool
    """Whether deletion is deferred (always true for API)"""

    message: str
    """Deletion status message"""

    name: str
    """Snapshot name"""
