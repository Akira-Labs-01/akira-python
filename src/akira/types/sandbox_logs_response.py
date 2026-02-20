# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SandboxLogsResponse", "Log"]


class Log(BaseModel):
    command: str
    """Command that was executed"""

    execution_time_ms: int
    """Execution duration in milliseconds"""

    exit_code: int
    """Exit code of the command"""

    request_id: str
    """Request ID for correlation"""

    sandbox_id: str
    """Sandbox ID where command was executed"""

    source: Literal["sync", "stream"]
    """Source of the log entry - 'sync' for tRPC execute, 'stream' for REST streaming"""

    status: Literal["completed", "timeout", "error"]
    """Execution status"""

    timestamp: str
    """Execution timestamp (ISO 8601)"""

    execution_id: Optional[str] = None
    """Unique execution ID (only present for sync execution)"""

    stderr: Optional[str] = None
    """Standard error (only present for sync execution, may be truncated)"""

    stderr_truncated: Optional[bool] = None
    """Whether stderr was truncated"""

    stdout: Optional[str] = None
    """Standard output (only present for sync execution, may be truncated)"""

    stdout_truncated: Optional[bool] = None
    """Whether stdout was truncated"""

    working_dir: Optional[str] = None
    """Working directory"""


class SandboxLogsResponse(BaseModel):
    logs: List[Log]
    """Execution logs"""

    total: int
    """Total number of logs returned"""
