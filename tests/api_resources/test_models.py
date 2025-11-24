# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from zeroentropy import ZeroEntropy, AsyncZeroEntropy
from zeroentropy.types import ModelRerankResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestModels:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_rerank(self, client: ZeroEntropy) -> None:
        model = client.models.rerank(
            documents=["string"],
            model="model",
            query="query",
        )
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    def test_method_rerank_with_all_params(self, client: ZeroEntropy) -> None:
        model = client.models.rerank(
            documents=["string"],
            model="model",
            query="query",
            latency="fast",
            top_n=0,
        )
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    def test_raw_response_rerank(self, client: ZeroEntropy) -> None:
        response = client.models.with_raw_response.rerank(
            documents=["string"],
            model="model",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = response.parse()
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    def test_streaming_response_rerank(self, client: ZeroEntropy) -> None:
        with client.models.with_streaming_response.rerank(
            documents=["string"],
            model="model",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = response.parse()
            assert_matches_type(ModelRerankResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncModels:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_rerank(self, async_client: AsyncZeroEntropy) -> None:
        model = await async_client.models.rerank(
            documents=["string"],
            model="model",
            query="query",
        )
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    async def test_method_rerank_with_all_params(self, async_client: AsyncZeroEntropy) -> None:
        model = await async_client.models.rerank(
            documents=["string"],
            model="model",
            query="query",
            latency="fast",
            top_n=0,
        )
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    async def test_raw_response_rerank(self, async_client: AsyncZeroEntropy) -> None:
        response = await async_client.models.with_raw_response.rerank(
            documents=["string"],
            model="model",
            query="query",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        model = await response.parse()
        assert_matches_type(ModelRerankResponse, model, path=["response"])

    @parametrize
    async def test_streaming_response_rerank(self, async_client: AsyncZeroEntropy) -> None:
        async with async_client.models.with_streaming_response.rerank(
            documents=["string"],
            model="model",
            query="query",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            model = await response.parse()
            assert_matches_type(ModelRerankResponse, model, path=["response"])

        assert cast(Any, response.is_closed) is True
