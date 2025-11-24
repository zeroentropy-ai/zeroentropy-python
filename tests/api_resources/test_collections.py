# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from zeroentropy import ZeroEntropy, AsyncZeroEntropy
from zeroentropy.types import (
    CollectionAddResponse,
    CollectionDeleteResponse,
    CollectionGetListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCollections:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_delete(self, client: ZeroEntropy) -> None:
        collection = client.collections.delete(
            collection_name="collection_name",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: ZeroEntropy) -> None:
        response = client.collections.with_raw_response.delete(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: ZeroEntropy) -> None:
        with client.collections.with_streaming_response.delete(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_add(self, client: ZeroEntropy) -> None:
        collection = client.collections.add(
            collection_name="collection_name",
        )
        assert_matches_type(CollectionAddResponse, collection, path=["response"])

    @parametrize
    def test_method_add_with_all_params(self, client: ZeroEntropy) -> None:
        collection = client.collections.add(
            collection_name="collection_name",
            num_shards=0,
        )
        assert_matches_type(CollectionAddResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_add(self, client: ZeroEntropy) -> None:
        response = client.collections.with_raw_response.add(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionAddResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_add(self, client: ZeroEntropy) -> None:
        with client.collections.with_streaming_response.add(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionAddResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get_list(self, client: ZeroEntropy) -> None:
        collection = client.collections.get_list()
        assert_matches_type(CollectionGetListResponse, collection, path=["response"])

    @parametrize
    def test_raw_response_get_list(self, client: ZeroEntropy) -> None:
        response = client.collections.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = response.parse()
        assert_matches_type(CollectionGetListResponse, collection, path=["response"])

    @parametrize
    def test_streaming_response_get_list(self, client: ZeroEntropy) -> None:
        with client.collections.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = response.parse()
            assert_matches_type(CollectionGetListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCollections:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_delete(self, async_client: AsyncZeroEntropy) -> None:
        collection = await async_client.collections.delete(
            collection_name="collection_name",
        )
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncZeroEntropy) -> None:
        response = await async_client.collections.with_raw_response.delete(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncZeroEntropy) -> None:
        async with async_client.collections.with_streaming_response.delete(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionDeleteResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_add(self, async_client: AsyncZeroEntropy) -> None:
        collection = await async_client.collections.add(
            collection_name="collection_name",
        )
        assert_matches_type(CollectionAddResponse, collection, path=["response"])

    @parametrize
    async def test_method_add_with_all_params(self, async_client: AsyncZeroEntropy) -> None:
        collection = await async_client.collections.add(
            collection_name="collection_name",
            num_shards=0,
        )
        assert_matches_type(CollectionAddResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_add(self, async_client: AsyncZeroEntropy) -> None:
        response = await async_client.collections.with_raw_response.add(
            collection_name="collection_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionAddResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncZeroEntropy) -> None:
        async with async_client.collections.with_streaming_response.add(
            collection_name="collection_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionAddResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get_list(self, async_client: AsyncZeroEntropy) -> None:
        collection = await async_client.collections.get_list()
        assert_matches_type(CollectionGetListResponse, collection, path=["response"])

    @parametrize
    async def test_raw_response_get_list(self, async_client: AsyncZeroEntropy) -> None:
        response = await async_client.collections.with_raw_response.get_list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        collection = await response.parse()
        assert_matches_type(CollectionGetListResponse, collection, path=["response"])

    @parametrize
    async def test_streaming_response_get_list(self, async_client: AsyncZeroEntropy) -> None:
        async with async_client.collections.with_streaming_response.get_list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            collection = await response.parse()
            assert_matches_type(CollectionGetListResponse, collection, path=["response"])

        assert cast(Any, response.is_closed) is True
