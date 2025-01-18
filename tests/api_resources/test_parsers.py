# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from zeroentropy import ZeroEntropy, AsyncZeroEntropy
from zeroentropy.types import ParserParseDocumentResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_parse_document(self, client: ZeroEntropy) -> None:
        parser = client.parsers.parse_document(
            base64_data="base64_data",
        )
        assert_matches_type(ParserParseDocumentResponse, parser, path=["response"])

    @parametrize
    def test_raw_response_parse_document(self, client: ZeroEntropy) -> None:
        response = client.parsers.with_raw_response.parse_document(
            base64_data="base64_data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parser = response.parse()
        assert_matches_type(ParserParseDocumentResponse, parser, path=["response"])

    @parametrize
    def test_streaming_response_parse_document(self, client: ZeroEntropy) -> None:
        with client.parsers.with_streaming_response.parse_document(
            base64_data="base64_data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parser = response.parse()
            assert_matches_type(ParserParseDocumentResponse, parser, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParsers:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_parse_document(self, async_client: AsyncZeroEntropy) -> None:
        parser = await async_client.parsers.parse_document(
            base64_data="base64_data",
        )
        assert_matches_type(ParserParseDocumentResponse, parser, path=["response"])

    @parametrize
    async def test_raw_response_parse_document(self, async_client: AsyncZeroEntropy) -> None:
        response = await async_client.parsers.with_raw_response.parse_document(
            base64_data="base64_data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parser = await response.parse()
        assert_matches_type(ParserParseDocumentResponse, parser, path=["response"])

    @parametrize
    async def test_streaming_response_parse_document(self, async_client: AsyncZeroEntropy) -> None:
        async with async_client.parsers.with_streaming_response.parse_document(
            base64_data="base64_data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parser = await response.parse()
            assert_matches_type(ParserParseDocumentResponse, parser, path=["response"])

        assert cast(Any, response.is_closed) is True
