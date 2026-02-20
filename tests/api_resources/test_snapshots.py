# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from akira import Akira, AsyncAkira
from akira.types import (
    SnapshotListResponse,
    SnapshotDeleteResponse,
    SnapshotRestoreResponse,
    SnapshotDeleteAllResponse,
)
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSnapshots:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Akira) -> None:
        snapshot = client.snapshots.list()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Akira) -> None:
        snapshot = client.snapshots.list(
            page=1,
            page_size=20,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Akira) -> None:
        response = client.snapshots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Akira) -> None:
        with client.snapshots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Akira) -> None:
        snapshot = client.snapshots.delete(
            "id",
        )
        assert_matches_type(SnapshotDeleteResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Akira) -> None:
        response = client.snapshots.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotDeleteResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Akira) -> None:
        with client.snapshots.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotDeleteResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.snapshots.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_all(self, client: Akira) -> None:
        snapshot = client.snapshots.delete_all()
        assert_matches_type(SnapshotDeleteAllResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_all(self, client: Akira) -> None:
        response = client.snapshots.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotDeleteAllResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_all(self, client: Akira) -> None:
        with client.snapshots.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotDeleteAllResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore(self, client: Akira) -> None:
        snapshot = client.snapshots.restore(
            id="id",
            name="restored-project",
        )
        assert_matches_type(SnapshotRestoreResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_with_all_params(self, client: Akira) -> None:
        snapshot = client.snapshots.restore(
            id="id",
            name="restored-project",
            image="image",
            resources={
                "cpus": 2,
                "memory": 1024,
                "storage": "321669910225Gi",
            },
            wait_for_ready=True,
        )
        assert_matches_type(SnapshotRestoreResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore(self, client: Akira) -> None:
        response = client.snapshots.with_raw_response.restore(
            id="id",
            name="restored-project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = response.parse()
        assert_matches_type(SnapshotRestoreResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore(self, client: Akira) -> None:
        with client.snapshots.with_streaming_response.restore(
            id="id",
            name="restored-project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = response.parse()
            assert_matches_type(SnapshotRestoreResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore(self, client: Akira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.snapshots.with_raw_response.restore(
                id="",
                name="restored-project",
            )


class TestAsyncSnapshots:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncAkira) -> None:
        snapshot = await async_client.snapshots.list()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncAkira) -> None:
        snapshot = await async_client.snapshots.list(
            page=1,
            page_size=20,
        )
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncAkira) -> None:
        response = await async_client.snapshots.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncAkira) -> None:
        async with async_client.snapshots.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotListResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncAkira) -> None:
        snapshot = await async_client.snapshots.delete(
            "id",
        )
        assert_matches_type(SnapshotDeleteResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncAkira) -> None:
        response = await async_client.snapshots.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotDeleteResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncAkira) -> None:
        async with async_client.snapshots.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotDeleteResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.snapshots.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_all(self, async_client: AsyncAkira) -> None:
        snapshot = await async_client.snapshots.delete_all()
        assert_matches_type(SnapshotDeleteAllResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_all(self, async_client: AsyncAkira) -> None:
        response = await async_client.snapshots.with_raw_response.delete_all()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotDeleteAllResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_all(self, async_client: AsyncAkira) -> None:
        async with async_client.snapshots.with_streaming_response.delete_all() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotDeleteAllResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore(self, async_client: AsyncAkira) -> None:
        snapshot = await async_client.snapshots.restore(
            id="id",
            name="restored-project",
        )
        assert_matches_type(SnapshotRestoreResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_with_all_params(self, async_client: AsyncAkira) -> None:
        snapshot = await async_client.snapshots.restore(
            id="id",
            name="restored-project",
            image="image",
            resources={
                "cpus": 2,
                "memory": 1024,
                "storage": "321669910225Gi",
            },
            wait_for_ready=True,
        )
        assert_matches_type(SnapshotRestoreResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncAkira) -> None:
        response = await async_client.snapshots.with_raw_response.restore(
            id="id",
            name="restored-project",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        snapshot = await response.parse()
        assert_matches_type(SnapshotRestoreResponse, snapshot, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncAkira) -> None:
        async with async_client.snapshots.with_streaming_response.restore(
            id="id",
            name="restored-project",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            snapshot = await response.parse()
            assert_matches_type(SnapshotRestoreResponse, snapshot, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncAkira) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.snapshots.with_raw_response.restore(
                id="",
                name="restored-project",
            )
