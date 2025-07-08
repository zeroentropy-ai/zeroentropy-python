# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from zeroentropy import ZeroEntropy, AsyncZeroEntropy
from zeroentropy.types import StatusGetStatusResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStatus:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get_status(self, client: ZeroEntropy) -> None:
        status = client.status.get_status()
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    def test_method_get_status_with_all_params(self, client: ZeroEntropy) -> None:
        status = client.status.get_status(
            collection_name="collection_name",
        )
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    def test_raw_response_get_status(self, client: ZeroEntropy) -> None:
        response = client.status.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = response.parse()
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    def test_streaming_response_get_status(self, client: ZeroEntropy) -> None:
        with client.status.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = response.parse()
            assert_matches_type(StatusGetStatusResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStatus:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_get_status(self, async_client: AsyncZeroEntropy) -> None:
        status = await async_client.status.get_status()
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    async def test_method_get_status_with_all_params(self, async_client: AsyncZeroEntropy) -> None:
        status = await async_client.status.get_status(
            collection_name="collection_name",
        )
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    async def test_raw_response_get_status(self, async_client: AsyncZeroEntropy) -> None:
        response = await async_client.status.with_raw_response.get_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        status = await response.parse()
        assert_matches_type(StatusGetStatusResponse, status, path=["response"])

    @parametrize
    async def test_streaming_response_get_status(self, async_client: AsyncZeroEntropy) -> None:
        async with async_client.status.with_streaming_response.get_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            status = await response.parse()
            assert_matches_type(StatusGetStatusResponse, status, path=["response"])

        assert cast(Any, response.is_closed) is True
