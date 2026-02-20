# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union
from datetime import datetime

import httpx

from ..types import (
    sandbox_list_params,
    sandbox_logs_params,
    sandbox_clone_params,
    sandbox_create_params,
    sandbox_delete_params,
    sandbox_status_params,
    sandbox_upload_params,
    sandbox_execute_params,
    sandbox_download_params,
    sandbox_snapshot_params,
    sandbox_execute_async_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .._base_client import make_request_options
from .._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder
from ..types.sandbox_list_response import SandboxListResponse
from ..types.sandbox_logs_response import SandboxLogsResponse
from ..types.sandbox_clone_response import SandboxCloneResponse
from ..types.sandbox_create_response import SandboxCreateResponse
from ..types.sandbox_delete_response import SandboxDeleteResponse
from ..types.sandbox_status_response import SandboxStatusResponse
from ..types.sandbox_upload_response import SandboxUploadResponse
from ..types.sandbox_execute_response import SandboxExecuteResponse
from ..types.sandbox_snapshot_response import SandboxSnapshotResponse
from ..types.sandbox_delete_all_response import SandboxDeleteAllResponse
from ..types.sandbox_execute_async_response import SandboxExecuteAsyncResponse

__all__ = ["SandboxesResource", "AsyncSandboxesResource"]


class SandboxesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SandboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/akira-python#accessing-raw-response-data-eg-headers
        """
        return SandboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SandboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/akira-python#with_streaming_response
        """
        return SandboxesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        env_vars: Dict[str, str] | Omit = omit,
        image: str | Omit = omit,
        name: str | Omit = omit,
        resources: sandbox_create_params.Resources | Omit = omit,
        wait_for_ready: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxCreateResponse:
        """
        Args:
          env_vars: Environment variables

          image: Docker image name (e.g., avmcodes/avm-default-sandbox)

          name: Custom sandbox name (auto-generated as sandbox-{user_id}-{timestamp} if not
              provided)

          wait_for_ready: Wait for sandbox to be ready before returning

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/sandboxes/create",
            body=maybe_transform(
                {
                    "env_vars": env_vars,
                    "image": image,
                    "name": name,
                    "resources": resources,
                    "wait_for_ready": wait_for_ready,
                },
                sandbox_create_params.SandboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxCreateResponse,
        )

    def list(
        self,
        *,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxListResponse:
        """
        Args:
          page: Page number

          page_size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/sandboxes/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    sandbox_list_params.SandboxListParams,
                ),
            ),
            cast_to=SandboxListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        create_snapshot: bool | Omit = omit,
        keep_storage: bool | Omit = omit,
        snapshot_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxDeleteResponse:
        """
        Args:
          id: Sandbox ID

          create_snapshot: Create snapshot before deleting storage

          keep_storage: @deprecated This option is ignored. Storage is always deleted.

          snapshot_name: Custom name for the snapshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/sandboxes/{id}/delete",
            body=maybe_transform(
                {
                    "create_snapshot": create_snapshot,
                    "keep_storage": keep_storage,
                    "snapshot_name": snapshot_name,
                },
                sandbox_delete_params.SandboxDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxDeleteResponse,
        )

    def clone(
        self,
        id: str,
        *,
        image: str | Omit = omit,
        name: str | Omit = omit,
        resources: sandbox_clone_params.Resources | Omit = omit,
        snapshot_name: str | Omit = omit,
        wait_for_ready: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxCloneResponse:
        """
        Args:
          id: Source sandbox ID

          image: Docker image override

          name: Name for the cloned sandbox (auto-generated as
              {source-sandbox-name}-clone-{timestamp} if not provided)

          resources: Resource overrides for cloned sandbox (storage inherited from source)

          snapshot_name: Custom name for intermediate snapshot (auto-generated if not provided)

          wait_for_ready: Wait for sandbox to be ready

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/sandboxes/{id}/clone",
            body=maybe_transform(
                {
                    "image": image,
                    "name": name,
                    "resources": resources,
                    "snapshot_name": snapshot_name,
                    "wait_for_ready": wait_for_ready,
                },
                sandbox_clone_params.SandboxCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxCloneResponse,
        )

    def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxDeleteAllResponse:
        return self._delete(
            "/v1/sandboxes/delete-all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxDeleteAllResponse,
        )

    def download(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Args:
          id: Sandbox ID

          path: File path in sandbox (e.g., /data/myfile.txt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return self._get(
            f"/v1/sandboxes/{id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"path": path}, sandbox_download_params.SandboxDownloadParams),
            ),
            cast_to=BinaryAPIResponse,
        )

    def execute(
        self,
        id: str,
        *,
        command: str,
        env: Dict[str, str] | Omit = omit,
        api_timeout: int | Omit = omit,
        working_dir: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxExecuteResponse:
        """
        Args:
          id: Sandbox ID

          command: Command to execute (full CLI command, supports shell features like redirection,
              pipes, etc.)

          env: Environment variables

          api_timeout: Execution timeout in seconds

          working_dir: Working directory for execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/sandboxes/{id}/execute",
            body=maybe_transform(
                {
                    "command": command,
                    "env": env,
                    "api_timeout": api_timeout,
                    "working_dir": working_dir,
                },
                sandbox_execute_params.SandboxExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxExecuteResponse,
        )

    def execute_async(
        self,
        id: str,
        *,
        command: str,
        env: Dict[str, str] | Omit = omit,
        working_dir: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JSONLDecoder[SandboxExecuteAsyncResponse]:
        """
        Execute command with streaming output.

        Executes a long-running command in a sandbox and streams stdout/stderr in
        real-time.

        **Response Format**: NDJSON (Newline Delimited JSON) - each line is a JSON
        object.

        **Streaming Behavior**:

        - Output chunks are sent as they're produced by the command
        - When the command completes, a final chunk with `exit_code` is sent

        **Client Disconnection**:

        - When the client closes the connection, the running process is automatically
          terminated

        **Example Client Code**:

        ```typescript
        const response = await fetch(url, {
          method: "POST",
          body: JSON.stringify({ command: "npm run dev" }),
        });
        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          const lines = decoder.decode(value).split("\n").filter(Boolean);
          for (const line of lines) {
            const { stdout, stderr, exit_code } = JSON.parse(line);
            if (stdout) process.stdout.write(stdout);
            if (stderr) process.stderr.write(stderr);
          }
        }
        ```

        Args:
          id: Sandbox ID

          command: Command to execute (full CLI command, supports shell features like redirection,
              pipes, etc.)

          env: Environment variables to set for the command

          working_dir: Working directory for execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/x-ndjson", **(extra_headers or {})}
        return self._post(
            f"/v1/sandboxes/{id}/execute_async",
            body=maybe_transform(
                {
                    "command": command,
                    "env": env,
                    "working_dir": working_dir,
                },
                sandbox_execute_async_params.SandboxExecuteAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JSONLDecoder[SandboxExecuteAsyncResponse],
            stream=True,
        )

    def logs(
        self,
        *,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        sandbox_id: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxLogsResponse:
        """Args:
          from_: Start time (ISO 8601).

        Default: 1 hour ago

          limit: Maximum number of logs to return (1-1000). Default: 100

          sandbox_id: Filter to specific sandbox ID

          to: End time (ISO 8601). Default: now

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/sandboxes/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "limit": limit,
                        "sandbox_id": sandbox_id,
                        "to": to,
                    },
                    sandbox_logs_params.SandboxLogsParams,
                ),
            ),
            cast_to=SandboxLogsResponse,
        )

    def snapshot(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        quick: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxSnapshotResponse:
        """
        Args:
          id: Sandbox ID

          name: Custom snapshot name (auto-generated if not provided)

          quick: Quick mode: fsfreeze only (faster but crash-consistent)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._post(
            f"/v1/sandboxes/{id}/snapshot",
            body=maybe_transform(
                {
                    "name": name,
                    "quick": quick,
                },
                sandbox_snapshot_params.SandboxSnapshotParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxSnapshotResponse,
        )

    def status(
        self,
        id: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxStatusResponse:
        """
        Args:
          id: Sandbox ID (UID or name)

          from_: Start time for historical data (ISO 8601)

          to: End time for historical data (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/sandboxes/{id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    sandbox_status_params.SandboxStatusParams,
                ),
            ),
            cast_to=SandboxStatusResponse,
        )

    def upload(
        self,
        id: str,
        *,
        path: str,
        file: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxUploadResponse:
        """
        Args:
          id: Sandbox ID

          path: Destination path in sandbox (e.g., /data/myfile.txt)

          file: File to upload (binary data)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            f"/v1/sandboxes/{id}/upload",
            body=maybe_transform(
                {
                    "path": path,
                    "file": file,
                },
                sandbox_upload_params.SandboxUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxUploadResponse,
        )


class AsyncSandboxesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSandboxesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/akira-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSandboxesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSandboxesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/akira-python#with_streaming_response
        """
        return AsyncSandboxesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        env_vars: Dict[str, str] | Omit = omit,
        image: str | Omit = omit,
        name: str | Omit = omit,
        resources: sandbox_create_params.Resources | Omit = omit,
        wait_for_ready: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxCreateResponse:
        """
        Args:
          env_vars: Environment variables

          image: Docker image name (e.g., avmcodes/avm-default-sandbox)

          name: Custom sandbox name (auto-generated as sandbox-{user_id}-{timestamp} if not
              provided)

          wait_for_ready: Wait for sandbox to be ready before returning

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/sandboxes/create",
            body=await async_maybe_transform(
                {
                    "env_vars": env_vars,
                    "image": image,
                    "name": name,
                    "resources": resources,
                    "wait_for_ready": wait_for_ready,
                },
                sandbox_create_params.SandboxCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxCreateResponse,
        )

    async def list(
        self,
        *,
        page: float | Omit = omit,
        page_size: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxListResponse:
        """
        Args:
          page: Page number

          page_size: Page size

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/sandboxes/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "page_size": page_size,
                    },
                    sandbox_list_params.SandboxListParams,
                ),
            ),
            cast_to=SandboxListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        create_snapshot: bool | Omit = omit,
        keep_storage: bool | Omit = omit,
        snapshot_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxDeleteResponse:
        """
        Args:
          id: Sandbox ID

          create_snapshot: Create snapshot before deleting storage

          keep_storage: @deprecated This option is ignored. Storage is always deleted.

          snapshot_name: Custom name for the snapshot

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/sandboxes/{id}/delete",
            body=await async_maybe_transform(
                {
                    "create_snapshot": create_snapshot,
                    "keep_storage": keep_storage,
                    "snapshot_name": snapshot_name,
                },
                sandbox_delete_params.SandboxDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxDeleteResponse,
        )

    async def clone(
        self,
        id: str,
        *,
        image: str | Omit = omit,
        name: str | Omit = omit,
        resources: sandbox_clone_params.Resources | Omit = omit,
        snapshot_name: str | Omit = omit,
        wait_for_ready: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxCloneResponse:
        """
        Args:
          id: Source sandbox ID

          image: Docker image override

          name: Name for the cloned sandbox (auto-generated as
              {source-sandbox-name}-clone-{timestamp} if not provided)

          resources: Resource overrides for cloned sandbox (storage inherited from source)

          snapshot_name: Custom name for intermediate snapshot (auto-generated if not provided)

          wait_for_ready: Wait for sandbox to be ready

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/sandboxes/{id}/clone",
            body=await async_maybe_transform(
                {
                    "image": image,
                    "name": name,
                    "resources": resources,
                    "snapshot_name": snapshot_name,
                    "wait_for_ready": wait_for_ready,
                },
                sandbox_clone_params.SandboxCloneParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxCloneResponse,
        )

    async def delete_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxDeleteAllResponse:
        return await self._delete(
            "/v1/sandboxes/delete-all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxDeleteAllResponse,
        )

    async def download(
        self,
        id: str,
        *,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Args:
          id: Sandbox ID

          path: File path in sandbox (e.g., /data/myfile.txt)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/octet-stream", **(extra_headers or {})}
        return await self._get(
            f"/v1/sandboxes/{id}/download",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"path": path}, sandbox_download_params.SandboxDownloadParams),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def execute(
        self,
        id: str,
        *,
        command: str,
        env: Dict[str, str] | Omit = omit,
        api_timeout: int | Omit = omit,
        working_dir: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxExecuteResponse:
        """
        Args:
          id: Sandbox ID

          command: Command to execute (full CLI command, supports shell features like redirection,
              pipes, etc.)

          env: Environment variables

          api_timeout: Execution timeout in seconds

          working_dir: Working directory for execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/sandboxes/{id}/execute",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "env": env,
                    "api_timeout": api_timeout,
                    "working_dir": working_dir,
                },
                sandbox_execute_params.SandboxExecuteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxExecuteResponse,
        )

    async def execute_async(
        self,
        id: str,
        *,
        command: str,
        env: Dict[str, str] | Omit = omit,
        working_dir: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncJSONLDecoder[SandboxExecuteAsyncResponse]:
        """
        Execute command with streaming output.

        Executes a long-running command in a sandbox and streams stdout/stderr in
        real-time.

        **Response Format**: NDJSON (Newline Delimited JSON) - each line is a JSON
        object.

        **Streaming Behavior**:

        - Output chunks are sent as they're produced by the command
        - When the command completes, a final chunk with `exit_code` is sent

        **Client Disconnection**:

        - When the client closes the connection, the running process is automatically
          terminated

        **Example Client Code**:

        ```typescript
        const response = await fetch(url, {
          method: "POST",
          body: JSON.stringify({ command: "npm run dev" }),
        });
        const reader = response.body.getReader();
        const decoder = new TextDecoder();

        while (true) {
          const { done, value } = await reader.read();
          if (done) break;
          const lines = decoder.decode(value).split("\n").filter(Boolean);
          for (const line of lines) {
            const { stdout, stderr, exit_code } = JSON.parse(line);
            if (stdout) process.stdout.write(stdout);
            if (stderr) process.stderr.write(stderr);
          }
        }
        ```

        Args:
          id: Sandbox ID

          command: Command to execute (full CLI command, supports shell features like redirection,
              pipes, etc.)

          env: Environment variables to set for the command

          working_dir: Working directory for execution

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "application/x-ndjson", **(extra_headers or {})}
        return await self._post(
            f"/v1/sandboxes/{id}/execute_async",
            body=await async_maybe_transform(
                {
                    "command": command,
                    "env": env,
                    "working_dir": working_dir,
                },
                sandbox_execute_async_params.SandboxExecuteAsyncParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncJSONLDecoder[SandboxExecuteAsyncResponse],
            stream=True,
        )

    async def logs(
        self,
        *,
        from_: Union[str, datetime] | Omit = omit,
        limit: int | Omit = omit,
        sandbox_id: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxLogsResponse:
        """Args:
          from_: Start time (ISO 8601).

        Default: 1 hour ago

          limit: Maximum number of logs to return (1-1000). Default: 100

          sandbox_id: Filter to specific sandbox ID

          to: End time (ISO 8601). Default: now

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/sandboxes/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "limit": limit,
                        "sandbox_id": sandbox_id,
                        "to": to,
                    },
                    sandbox_logs_params.SandboxLogsParams,
                ),
            ),
            cast_to=SandboxLogsResponse,
        )

    async def snapshot(
        self,
        id: str,
        *,
        name: str | Omit = omit,
        quick: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxSnapshotResponse:
        """
        Args:
          id: Sandbox ID

          name: Custom snapshot name (auto-generated if not provided)

          quick: Quick mode: fsfreeze only (faster but crash-consistent)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._post(
            f"/v1/sandboxes/{id}/snapshot",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "quick": quick,
                },
                sandbox_snapshot_params.SandboxSnapshotParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxSnapshotResponse,
        )

    async def status(
        self,
        id: str,
        *,
        from_: Union[str, datetime] | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxStatusResponse:
        """
        Args:
          id: Sandbox ID (UID or name)

          from_: Start time for historical data (ISO 8601)

          to: End time for historical data (ISO 8601)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/sandboxes/{id}/status",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "from_": from_,
                        "to": to,
                    },
                    sandbox_status_params.SandboxStatusParams,
                ),
            ),
            cast_to=SandboxStatusResponse,
        )

    async def upload(
        self,
        id: str,
        *,
        path: str,
        file: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SandboxUploadResponse:
        """
        Args:
          id: Sandbox ID

          path: Destination path in sandbox (e.g., /data/myfile.txt)

          file: File to upload (binary data)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            f"/v1/sandboxes/{id}/upload",
            body=await async_maybe_transform(
                {
                    "path": path,
                    "file": file,
                },
                sandbox_upload_params.SandboxUploadParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SandboxUploadResponse,
        )


class SandboxesResourceWithRawResponse:
    def __init__(self, sandboxes: SandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = to_raw_response_wrapper(
            sandboxes.create,
        )
        self.list = to_raw_response_wrapper(
            sandboxes.list,
        )
        self.delete = to_raw_response_wrapper(
            sandboxes.delete,
        )
        self.clone = to_raw_response_wrapper(
            sandboxes.clone,
        )
        self.delete_all = to_raw_response_wrapper(
            sandboxes.delete_all,
        )
        self.download = to_custom_raw_response_wrapper(
            sandboxes.download,
            BinaryAPIResponse,
        )
        self.execute = to_raw_response_wrapper(
            sandboxes.execute,
        )
        self.execute_async = to_raw_response_wrapper(
            sandboxes.execute_async,
        )
        self.logs = to_raw_response_wrapper(
            sandboxes.logs,
        )
        self.snapshot = to_raw_response_wrapper(
            sandboxes.snapshot,
        )
        self.status = to_raw_response_wrapper(
            sandboxes.status,
        )
        self.upload = to_raw_response_wrapper(
            sandboxes.upload,
        )


class AsyncSandboxesResourceWithRawResponse:
    def __init__(self, sandboxes: AsyncSandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = async_to_raw_response_wrapper(
            sandboxes.create,
        )
        self.list = async_to_raw_response_wrapper(
            sandboxes.list,
        )
        self.delete = async_to_raw_response_wrapper(
            sandboxes.delete,
        )
        self.clone = async_to_raw_response_wrapper(
            sandboxes.clone,
        )
        self.delete_all = async_to_raw_response_wrapper(
            sandboxes.delete_all,
        )
        self.download = async_to_custom_raw_response_wrapper(
            sandboxes.download,
            AsyncBinaryAPIResponse,
        )
        self.execute = async_to_raw_response_wrapper(
            sandboxes.execute,
        )
        self.execute_async = async_to_raw_response_wrapper(
            sandboxes.execute_async,
        )
        self.logs = async_to_raw_response_wrapper(
            sandboxes.logs,
        )
        self.snapshot = async_to_raw_response_wrapper(
            sandboxes.snapshot,
        )
        self.status = async_to_raw_response_wrapper(
            sandboxes.status,
        )
        self.upload = async_to_raw_response_wrapper(
            sandboxes.upload,
        )


class SandboxesResourceWithStreamingResponse:
    def __init__(self, sandboxes: SandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = to_streamed_response_wrapper(
            sandboxes.create,
        )
        self.list = to_streamed_response_wrapper(
            sandboxes.list,
        )
        self.delete = to_streamed_response_wrapper(
            sandboxes.delete,
        )
        self.clone = to_streamed_response_wrapper(
            sandboxes.clone,
        )
        self.delete_all = to_streamed_response_wrapper(
            sandboxes.delete_all,
        )
        self.download = to_custom_streamed_response_wrapper(
            sandboxes.download,
            StreamedBinaryAPIResponse,
        )
        self.execute = to_streamed_response_wrapper(
            sandboxes.execute,
        )
        self.execute_async = to_streamed_response_wrapper(
            sandboxes.execute_async,
        )
        self.logs = to_streamed_response_wrapper(
            sandboxes.logs,
        )
        self.snapshot = to_streamed_response_wrapper(
            sandboxes.snapshot,
        )
        self.status = to_streamed_response_wrapper(
            sandboxes.status,
        )
        self.upload = to_streamed_response_wrapper(
            sandboxes.upload,
        )


class AsyncSandboxesResourceWithStreamingResponse:
    def __init__(self, sandboxes: AsyncSandboxesResource) -> None:
        self._sandboxes = sandboxes

        self.create = async_to_streamed_response_wrapper(
            sandboxes.create,
        )
        self.list = async_to_streamed_response_wrapper(
            sandboxes.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            sandboxes.delete,
        )
        self.clone = async_to_streamed_response_wrapper(
            sandboxes.clone,
        )
        self.delete_all = async_to_streamed_response_wrapper(
            sandboxes.delete_all,
        )
        self.download = async_to_custom_streamed_response_wrapper(
            sandboxes.download,
            AsyncStreamedBinaryAPIResponse,
        )
        self.execute = async_to_streamed_response_wrapper(
            sandboxes.execute,
        )
        self.execute_async = async_to_streamed_response_wrapper(
            sandboxes.execute_async,
        )
        self.logs = async_to_streamed_response_wrapper(
            sandboxes.logs,
        )
        self.snapshot = async_to_streamed_response_wrapper(
            sandboxes.snapshot,
        )
        self.status = async_to_streamed_response_wrapper(
            sandboxes.status,
        )
        self.upload = async_to_streamed_response_wrapper(
            sandboxes.upload,
        )
