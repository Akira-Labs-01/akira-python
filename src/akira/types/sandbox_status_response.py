# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["SandboxStatusResponse", "Current", "History"]


class Current(BaseModel):
    """Current resource usage"""

    cpu_percent: float
    """CPU usage percentage (0-100)"""

    memory_mb: float
    """Current memory usage in megabytes"""

    memory_percent: float
    """Memory usage percentage (0-100)"""


class History(BaseModel):
    cpu_percent: float
    """CPU usage percentage (0-100)"""

    memory_mb: float
    """Memory usage in megabytes"""

    timestamp: str
    """Sample timestamp (ISO 8601)"""


class SandboxStatusResponse(BaseModel):
    sandbox_name: str
    """Sandbox name"""

    timestamp: str
    """Response timestamp (ISO 8601)"""

    current: Optional[Current] = None
    """Current resource usage"""

    history: Optional[List[History]] = None
    """Historical usage data"""
