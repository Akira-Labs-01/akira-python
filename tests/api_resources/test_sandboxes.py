# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from akira import Akira, AsyncAkira
from akira.types import (
    SandboxListResponse,
    SandboxLogsResponse,
    SandboxCloneResponse,
    SandboxCreateResponse,
    SandboxDeleteResponse,
    SandboxStatusResponse,
    SandboxUploadResponse,
    SandboxExecuteResponse,
    SandboxSnapshotResponse,
    SandboxDeleteAllResponse,
    SandboxExecuteAsyncResponse,
)
from tests.utils import assert_matches_type
from akira._utils import parse_datetime
from akira._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from akira._decoders.jsonl import JSONLDecoder, AsyncJSONLDecoder

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSandboxes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Akira) -> None:
        sandbox = client.sandboxes.create()
        assert_matches_type(SandboxCreateResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Akira) -> None:
        sandbox = client.sandboxes.create(
            env_vars={"foo": "string"},
            image="avmcodes/avm-default-sandbox",
            name="my-project",
            resources={
                "cpus": 1,
                "memory": 512,
                "storage": 10,
            },
            wait_for_ready=True,
        )
        assert_matches_type(SandboxCreateResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxCreateResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxCreateResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Akira) -> None:
        sandbox = client.sandboxes.list()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Akira) -> None:
        sandbox = client.sandboxes.list(
            page=1,
            page_size=20,
        )
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxListResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Akira) -> None:
        sandbox = client.sandboxes.delete(
            id="id",
        )
        assert_matches_type(SandboxDeleteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_with_all_params(self, client: Akira) -> None:
        sandbox = client.sandboxes.delete(
            id="id",
            create_snapshot=True,
            keep_storage=True,
            snapshot_name="final-backup",
        )
        assert_matches_type(SandboxDeleteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxDeleteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxDeleteResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sandboxes.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone(self, client: Akira) -> None:
        sandbox = client.sandboxes.clone(
            id="id",
        )
        assert_matches_type(SandboxCloneResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_clone_with_all_params(self, client: Akira) -> None:
        sandbox = client.sandboxes.clone(
            id="id",
            image="image",
            name="my-cloned-sandbox",
            resources={
                "cpus": 2,
                "memory": 1024,
            },
            snapshot_name="clone-backup-1",
            wait_for_ready=True,
        )
        assert_matches_type(SandboxCloneResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_clone(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxCloneResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_clone(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxCloneResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_clone(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sandboxes.with_raw_response.clone(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Akira) -> None:
        sandbox = client.sandboxes.delete_all()
        assert_matches_type(SandboxDeleteAllResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxDeleteAllResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxDeleteAllResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_download(self, client: Akira, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sandboxes/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        sandbox = client.sandboxes.download(
            id="id",
            path="path",
        )
        assert sandbox.is_closed
        assert sandbox.json() == {"foo": "bar"}
        assert cast(Any, sandbox.is_closed) is True
        assert isinstance(sandbox, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_download(self, client: Akira, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sandboxes/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        sandbox = client.sandboxes.with_raw_response.download(
            id="id",
            path="path",
        )

        assert sandbox.is_closed is True
        assert sandbox.http_request.headers.get("X-Stainless-Lang") == "python"
        assert sandbox.json() == {"foo": "bar"}
        assert isinstance(sandbox, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_download(self, client: Akira, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sandboxes/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.sandboxes.with_streaming_response.download(
            id="id",
            path="path",
        ) as sandbox:
            assert not sandbox.is_closed
            assert sandbox.http_request.headers.get("X-Stainless-Lang") == "python"

            assert sandbox.json() == {"foo": "bar"}
            assert cast(Any, sandbox.is_closed) is True
            assert isinstance(sandbox, StreamedBinaryAPIResponse)

        assert cast(Any, sandbox.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_download(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sandboxes.with_raw_response.download(
                id="",
                path="path",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute(self, client: Akira) -> None:
        sandbox = client.sandboxes.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_with_all_params(self, client: Akira) -> None:
        sandbox = client.sandboxes.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
            env={"foo": "string"},
            api_timeout=5,
            working_dir="working_dir",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sandboxes.with_raw_response.execute(
                id="",
                command="python -c \"print('Hello, World!')\"",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_async(self, client: Akira) -> None:
        sandbox_stream = client.sandboxes.execute_async(
            id="id",
            command="npm run dev",
        )
        assert_matches_type(JSONLDecoder[SandboxExecuteAsyncResponse], sandbox_stream, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_execute_async_with_all_params(self, client: Akira) -> None:
        sandbox_stream = client.sandboxes.execute_async(
            id="id",
            command="npm run dev",
            env={"foo": "string"},
            working_dir="working_dir",
        )
        assert_matches_type(JSONLDecoder[SandboxExecuteAsyncResponse], sandbox_stream, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_execute_async(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.execute_async(
            id="id",
            command="npm run dev",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = response.parse()
        stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_execute_async(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.execute_async(
            id="id",
            command="npm run dev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = response.parse()
            stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_execute_async(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sandboxes.with_raw_response.execute_async(
                id="",
                command="npm run dev",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_logs(self, client: Akira) -> None:
        sandbox = client.sandboxes.logs()
        assert_matches_type(SandboxLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_logs_with_all_params(self, client: Akira) -> None:
        sandbox = client.sandboxes.logs(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            sandbox_id="sandbox_id",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SandboxLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_logs(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_logs(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxLogsResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_snapshot(self, client: Akira) -> None:
        sandbox = client.sandboxes.snapshot(
            id="id",
        )
        assert_matches_type(SandboxSnapshotResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_snapshot_with_all_params(self, client: Akira) -> None:
        sandbox = client.sandboxes.snapshot(
            id="id",
            name="my-snapshot-backup",
            quick=False,
        )
        assert_matches_type(SandboxSnapshotResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_snapshot(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.snapshot(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxSnapshotResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_snapshot(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.snapshot(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxSnapshotResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_snapshot(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sandboxes.with_raw_response.snapshot(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status(self, client: Akira) -> None:
        sandbox = client.sandboxes.status(
            id="id",
        )
        assert_matches_type(SandboxStatusResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_status_with_all_params(self, client: Akira) -> None:
        sandbox = client.sandboxes.status(
            id="id",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SandboxStatusResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.status(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxStatusResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.status(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxStatusResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_status(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sandboxes.with_raw_response.status(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload(self, client: Akira) -> None:
        sandbox = client.sandboxes.upload(
            id="id",
            path="path",
        )
        assert_matches_type(SandboxUploadResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: Akira) -> None:
        sandbox = client.sandboxes.upload(
            id="id",
            path="path",
            file={},
        )
        assert_matches_type(SandboxUploadResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: Akira) -> None:
        response = client.sandboxes.with_raw_response.upload(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = response.parse()
        assert_matches_type(SandboxUploadResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: Akira) -> None:
        with client.sandboxes.with_streaming_response.upload(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = response.parse()
            assert_matches_type(SandboxUploadResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_upload(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.sandboxes.with_raw_response.upload(
                id="",
                path="path",
            )


class TestAsyncSandboxes:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.create()
        assert_matches_type(SandboxCreateResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.create(
            env_vars={"foo": "string"},
            image="avmcodes/avm-default-sandbox",
            name="my-project",
            resources={
                "cpus": 1,
                "memory": 512,
                "storage": 10,
            },
            wait_for_ready=True,
        )
        assert_matches_type(SandboxCreateResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxCreateResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxCreateResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.list()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.list(
            page=1,
            page_size=20,
        )
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxListResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxListResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.delete(
            id="id",
        )
        assert_matches_type(SandboxDeleteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.delete(
            id="id",
            create_snapshot=True,
            keep_storage=True,
            snapshot_name="final-backup",
        )
        assert_matches_type(SandboxDeleteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.delete(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxDeleteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.delete(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxDeleteResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sandboxes.with_raw_response.delete(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.clone(
            id="id",
        )
        assert_matches_type(SandboxCloneResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_clone_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.clone(
            id="id",
            image="image",
            name="my-cloned-sandbox",
            resources={
                "cpus": 2,
                "memory": 1024,
            },
            snapshot_name="clone-backup-1",
            wait_for_ready=True,
        )
        assert_matches_type(SandboxCloneResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_clone(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.clone(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxCloneResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_clone(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.clone(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxCloneResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_clone(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sandboxes.with_raw_response.clone(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.delete_all()
        assert_matches_type(SandboxDeleteAllResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxDeleteAllResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxDeleteAllResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_download(self, async_client: AsyncAkira, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sandboxes/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        sandbox = await async_client.sandboxes.download(
            id="id",
            path="path",
        )
        assert sandbox.is_closed
        assert await sandbox.json() == {"foo": "bar"}
        assert cast(Any, sandbox.is_closed) is True
        assert isinstance(sandbox, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_download(self, async_client: AsyncAkira, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sandboxes/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        sandbox = await async_client.sandboxes.with_raw_response.download(
            id="id",
            path="path",
        )

        assert sandbox.is_closed is True
        assert sandbox.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await sandbox.json() == {"foo": "bar"}
        assert isinstance(sandbox, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_download(self, async_client: AsyncAkira, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/sandboxes/id/download").mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.sandboxes.with_streaming_response.download(
            id="id",
            path="path",
        ) as sandbox:
            assert not sandbox.is_closed
            assert sandbox.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await sandbox.json() == {"foo": "bar"}
            assert cast(Any, sandbox.is_closed) is True
            assert isinstance(sandbox, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, sandbox.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_download(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sandboxes.with_raw_response.download(
                id="",
                path="path",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
            env={"foo": "string"},
            api_timeout=5,
            working_dir="working_dir",
        )
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.execute(
            id="id",
            command="python -c \"print('Hello, World!')\"",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxExecuteResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sandboxes.with_raw_response.execute(
                id="",
                command="python -c \"print('Hello, World!')\"",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_async(self, async_client: AsyncAkira) -> None:
        sandbox_stream = await async_client.sandboxes.execute_async(
            id="id",
            command="npm run dev",
        )
        assert_matches_type(AsyncJSONLDecoder[SandboxExecuteAsyncResponse], sandbox_stream, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_execute_async_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox_stream = await async_client.sandboxes.execute_async(
            id="id",
            command="npm run dev",
            env={"foo": "string"},
            working_dir="working_dir",
        )
        assert_matches_type(AsyncJSONLDecoder[SandboxExecuteAsyncResponse], sandbox_stream, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_execute_async(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.execute_async(
            id="id",
            command="npm run dev",
        )

        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stream = await response.parse()
        await stream.close()

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_execute_async(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.execute_async(
            id="id",
            command="npm run dev",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stream = await response.parse()
            await stream.close()

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_execute_async(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sandboxes.with_raw_response.execute_async(
                id="",
                command="npm run dev",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_logs(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.logs()
        assert_matches_type(SandboxLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_logs_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.logs(
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            limit=1,
            sandbox_id="sandbox_id",
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SandboxLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_logs(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.logs()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxLogsResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_logs(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.logs() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxLogsResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_snapshot(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.snapshot(
            id="id",
        )
        assert_matches_type(SandboxSnapshotResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_snapshot_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.snapshot(
            id="id",
            name="my-snapshot-backup",
            quick=False,
        )
        assert_matches_type(SandboxSnapshotResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_snapshot(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.snapshot(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxSnapshotResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_snapshot(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.snapshot(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxSnapshotResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_snapshot(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sandboxes.with_raw_response.snapshot(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.status(
            id="id",
        )
        assert_matches_type(SandboxStatusResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_status_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.status(
            id="id",
            from_=parse_datetime("2019-12-27T18:11:19.117Z"),
            to=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(SandboxStatusResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.status(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxStatusResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.status(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxStatusResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sandboxes.with_raw_response.status(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.upload(
            id="id",
            path="path",
        )
        assert_matches_type(SandboxUploadResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncAkira) -> None:
        sandbox = await async_client.sandboxes.upload(
            id="id",
            path="path",
            file={},
        )
        assert_matches_type(SandboxUploadResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncAkira) -> None:
        response = await async_client.sandboxes.with_raw_response.upload(
            id="id",
            path="path",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sandbox = await response.parse()
        assert_matches_type(SandboxUploadResponse, sandbox, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncAkira) -> None:
        async with async_client.sandboxes.with_streaming_response.upload(
            id="id",
            path="path",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sandbox = await response.parse()
            assert_matches_type(SandboxUploadResponse, sandbox, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_upload(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.sandboxes.with_raw_response.upload(
                id="",
                path="path",
            )
