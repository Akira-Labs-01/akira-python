# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["SandboxExecuteAsyncParams"]


class SandboxExecuteAsyncParams(TypedDict, total=False):
    command: Required[str]
    """
    Command to execute (full CLI command, supports shell features like redirection,
    pipes, etc.)
    """

    env: Dict[str, str]
    """Environment variables to set for the command"""

    working_dir: str
    """Working directory for execution"""
