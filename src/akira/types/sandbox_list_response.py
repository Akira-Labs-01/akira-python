# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .sandbox import Sandbox
from .._models import BaseModel

__all__ = ["SandboxListResponse", "Pagination"]


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


class SandboxListResponse(BaseModel):
    data: List[Sandbox]
    """Array of sandboxes"""

    pagination: Pagination
    """Pagination metadata"""
