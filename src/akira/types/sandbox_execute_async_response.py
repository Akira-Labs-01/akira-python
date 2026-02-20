# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["SandboxExecuteAsyncResponse"]


class SandboxExecuteAsyncResponse(BaseModel):
    error: Optional[str] = None
    """Error message if execution failed"""

    exit_code: Optional[int] = None
    """Exit code (sent in final chunk when command completes)"""

    stderr: Optional[str] = None
    """Standard error chunk"""

    stdout: Optional[str] = None
    """Standard output chunk"""
