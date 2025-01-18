# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from zeroentropy import Zeroentropy, AsyncZeroentropy
from zeroentropy.types import ParserParseResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_parse(self, client: Zeroentropy) -> None:
        parser = client.parsers.parse(
            base64_data="base64_data",
        )
        assert_matches_type(ParserParseResponse, parser, path=["response"])

    @parametrize
    def test_raw_response_parse(self, client: Zeroentropy) -> None:
        response = client.parsers.with_raw_response.parse(
            base64_data="base64_data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parser = response.parse()
        assert_matches_type(ParserParseResponse, parser, path=["response"])

    @parametrize
    def test_streaming_response_parse(self, client: Zeroentropy) -> None:
        with client.parsers.with_streaming_response.parse(
            base64_data="base64_data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parser = response.parse()
            assert_matches_type(ParserParseResponse, parser, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_parse(self, async_client: AsyncZeroentropy) -> None:
        parser = await async_client.parsers.parse(
            base64_data="base64_data",
        )
        assert_matches_type(ParserParseResponse, parser, path=["response"])

    @parametrize
    async def test_raw_response_parse(self, async_client: AsyncZeroentropy) -> None:
        response = await async_client.parsers.with_raw_response.parse(
            base64_data="base64_data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parser = await response.parse()
        assert_matches_type(ParserParseResponse, parser, path=["response"])

    @parametrize
    async def test_streaming_response_parse(self, async_client: AsyncZeroentropy) -> None:
        async with async_client.parsers.with_streaming_response.parse(
            base64_data="base64_data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parser = await response.parse()
            assert_matches_type(ParserParseResponse, parser, path=["response"])

        assert cast(Any, response.is_closed) is True
