# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import parser_parse_document_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.parser_parse_document_response import ParserParseDocumentResponse

__all__ = ["ParsersResource", "AsyncParsersResource"]


class ParsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return ParsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return ParsersResourceWithStreamingResponse(self)

    def parse_document(
        self,
        *,
        base64_data: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParserParseDocumentResponse:
        """This provides access to the parsers that we use for indexing.

        This endpoint will
        not access any collection or search index, and the result will not be saved.
        This will use the same parsing method as the `/documents/add-document` endpoint.

        A common use-case for this endpoint, is to use our parser in combination with
        your own pre-processing step, before then uploading it to the search index using
        the `text-pages` filetype.

        Args:
          base64_data: The document's raw data, as a base64-encoded string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/parsers/parse-document",
            body=maybe_transform({"base64_data": base64_data}, parser_parse_document_params.ParserParseDocumentParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParserParseDocumentResponse,
        )


class AsyncParsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncParsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return AsyncParsersResourceWithStreamingResponse(self)

    async def parse_document(
        self,
        *,
        base64_data: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ParserParseDocumentResponse:
        """This provides access to the parsers that we use for indexing.

        This endpoint will
        not access any collection or search index, and the result will not be saved.
        This will use the same parsing method as the `/documents/add-document` endpoint.

        A common use-case for this endpoint, is to use our parser in combination with
        your own pre-processing step, before then uploading it to the search index using
        the `text-pages` filetype.

        Args:
          base64_data: The document's raw data, as a base64-encoded string

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/parsers/parse-document",
            body=await async_maybe_transform(
                {"base64_data": base64_data}, parser_parse_document_params.ParserParseDocumentParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ParserParseDocumentResponse,
        )


class ParsersResourceWithRawResponse:
    def __init__(self, parsers: ParsersResource) -> None:
        self._parsers = parsers

        self.parse_document = to_raw_response_wrapper(
            parsers.parse_document,
        )


class AsyncParsersResourceWithRawResponse:
    def __init__(self, parsers: AsyncParsersResource) -> None:
        self._parsers = parsers

        self.parse_document = async_to_raw_response_wrapper(
            parsers.parse_document,
        )


class ParsersResourceWithStreamingResponse:
    def __init__(self, parsers: ParsersResource) -> None:
        self._parsers = parsers

        self.parse_document = to_streamed_response_wrapper(
            parsers.parse_document,
        )


class AsyncParsersResourceWithStreamingResponse:
    def __init__(self, parsers: AsyncParsersResource) -> None:
        self._parsers = parsers

        self.parse_document = async_to_streamed_response_wrapper(
            parsers.parse_document,
        )
