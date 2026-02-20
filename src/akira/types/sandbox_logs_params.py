# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SandboxLogsParams"]


class SandboxLogsParams(TypedDict, total=False):
    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Start time (ISO 8601). Default: 1 hour ago"""

    limit: int
    """Maximum number of logs to return (1-1000). Default: 100"""

    sandbox_id: str
    """Filter to specific sandbox ID"""

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """End time (ISO 8601). Default: now"""
