# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal

import httpx

from ..types import query_top_pages_params, query_top_snippets_params, query_top_documents_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.query_top_pages_response import QueryTopPagesResponse
from ..types.query_top_snippets_response import QueryTopSnippetsResponse
from ..types.query_top_documents_response import QueryTopDocumentsResponse

__all__ = ["QueriesResource", "AsyncQueriesResource"]


class QueriesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> QueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return QueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> QueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return QueriesResourceWithStreamingResponse(self)

    def top_documents(
        self,
        *,
        collection_name: str,
        k: int,
        query: Optional[str],
        filter: Optional[Dict[str, object]] | Omit = omit,
        include_metadata: bool | Omit = omit,
        latency_mode: Literal["low", "high"] | Omit = omit,
        reranker: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryTopDocumentsResponse:
        """
        Get the top K documents that match the given query

        Args:
          collection_name: The name of the collection.

          k: The number of documents to return. If there are not enough documents matching
              your filters, then fewer may be returned. This number must be between 1 and
              2048, inclusive.

          query: The natural language query to search with. This cannot exceed 4096 UTF-8 bytes.
              If `null`, then the sort will be undefined. The purpose of `null` is to do
              faster metadata filter searches without care for relevancy. Cost per query is
              unchanged.

          filter: The query filter to apply. Please read [Metadata Filtering](/metadata-filtering)
              for more information. If not provided, then all documents will be searched.

          include_metadata: Whether or not to include the metadata in the top documents response. If not
              provided, then the default will be `False`.

          latency_mode: This option selects between our two latency modes. The higher latency mode takes
              longer, but can allow for more accurate responses. If desired, test both to
              customize your search experience for your particular use-case, or use the
              default of "low" and only swap if you need an additional improvement in search
              result quality.

          reranker: The reranker to use after initial retrieval. The default is `null`. You can find
              available model ids along with more information at
              [/models/rerank](/api-reference/models/rerank).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/queries/top-documents",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "k": k,
                    "query": query,
                    "filter": filter,
                    "include_metadata": include_metadata,
                    "latency_mode": latency_mode,
                    "reranker": reranker,
                },
                query_top_documents_params.QueryTopDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryTopDocumentsResponse,
        )

    def top_pages(
        self,
        *,
        collection_name: str,
        k: int,
        query: str,
        filter: Optional[Dict[str, object]] | Omit = omit,
        include_content: bool | Omit = omit,
        latency_mode: Literal["low", "high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryTopPagesResponse:
        """
        Get the top K pages that match the given query

        Args:
          collection_name: The name of the collection.

          k: The number of pages to return. If there are not enough pages matching your
              filters, then fewer may be returned. This number must be between 1 and 1024,
              inclusive.

          query: The natural language query to search with. This cannot exceed 4096 UTF-8 bytes.

          filter: The query filter to apply. Please read [Metadata Filtering](/metadata-filtering)
              for more information. If not provided, then all documents will be searched.

          include_content: If set to true, then the content of all pages will be returned.

          latency_mode: This option selects between our two latency modes. The higher latency mode takes
              longer, but can allow for more accurate responses. If desired, test both to
              customize your search experience for your particular use-case, or use the
              default of "low" and only swap if you need an additional improvement in search
              result quality.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/queries/top-pages",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "k": k,
                    "query": query,
                    "filter": filter,
                    "include_content": include_content,
                    "latency_mode": latency_mode,
                },
                query_top_pages_params.QueryTopPagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryTopPagesResponse,
        )

    def top_snippets(
        self,
        *,
        collection_name: str,
        k: int,
        query: str,
        filter: Optional[Dict[str, object]] | Omit = omit,
        include_document_metadata: bool | Omit = omit,
        precise_responses: bool | Omit = omit,
        reranker: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryTopSnippetsResponse:
        """
        Get the top K snippets that match the given query.

        You may choose between coarse and precise snippets. Precise snippets will
        average ~200 characters, while coarse snippets will average ~2000 characters.
        The default is coarse snippets. Use the `precise_responses` parameter to adjust.

        Args:
          collection_name: The name of the collection.

          k: The number of snippets to return. If there are not enough snippets matching your
              filters, then fewer may be returned. This number must be between 1 and 128,
              inclusive.

          query: The natural language query to search with. This cannot exceed 4096 characters (A
              single UTF-8 codepoint, is considered to be 1 character).

          filter: The query filter to apply. Please read [Metadata Filtering](/metadata-filtering)
              for more information. If not provided, then all documents will be searched.

          include_document_metadata: If true, the `document_results` returns will additionally contain document
              metadata. This is false by default, as returning metadata can add overhead if
              the amount of data to return is large.

          precise_responses: Enable precise responses. Precise responses will have higher latency, but
              provide much more precise snippets. When `precise_responses` is set to `true`,
              the responses will average 200 characters. If set to `false`, the responses will
              average 2000 characters. The default is `false`.

          reranker: The reranker to use after initial retrieval. The default is `null`. You can find
              available model ids, along with more information, at
              [/models/rerank](/api-reference/models/rerank).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/queries/top-snippets",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "k": k,
                    "query": query,
                    "filter": filter,
                    "include_document_metadata": include_document_metadata,
                    "precise_responses": precise_responses,
                    "reranker": reranker,
                },
                query_top_snippets_params.QueryTopSnippetsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryTopSnippetsResponse,
        )


class AsyncQueriesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncQueriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncQueriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncQueriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return AsyncQueriesResourceWithStreamingResponse(self)

    async def top_documents(
        self,
        *,
        collection_name: str,
        k: int,
        query: Optional[str],
        filter: Optional[Dict[str, object]] | Omit = omit,
        include_metadata: bool | Omit = omit,
        latency_mode: Literal["low", "high"] | Omit = omit,
        reranker: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryTopDocumentsResponse:
        """
        Get the top K documents that match the given query

        Args:
          collection_name: The name of the collection.

          k: The number of documents to return. If there are not enough documents matching
              your filters, then fewer may be returned. This number must be between 1 and
              2048, inclusive.

          query: The natural language query to search with. This cannot exceed 4096 UTF-8 bytes.
              If `null`, then the sort will be undefined. The purpose of `null` is to do
              faster metadata filter searches without care for relevancy. Cost per query is
              unchanged.

          filter: The query filter to apply. Please read [Metadata Filtering](/metadata-filtering)
              for more information. If not provided, then all documents will be searched.

          include_metadata: Whether or not to include the metadata in the top documents response. If not
              provided, then the default will be `False`.

          latency_mode: This option selects between our two latency modes. The higher latency mode takes
              longer, but can allow for more accurate responses. If desired, test both to
              customize your search experience for your particular use-case, or use the
              default of "low" and only swap if you need an additional improvement in search
              result quality.

          reranker: The reranker to use after initial retrieval. The default is `null`. You can find
              available model ids along with more information at
              [/models/rerank](/api-reference/models/rerank).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/queries/top-documents",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "k": k,
                    "query": query,
                    "filter": filter,
                    "include_metadata": include_metadata,
                    "latency_mode": latency_mode,
                    "reranker": reranker,
                },
                query_top_documents_params.QueryTopDocumentsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryTopDocumentsResponse,
        )

    async def top_pages(
        self,
        *,
        collection_name: str,
        k: int,
        query: str,
        filter: Optional[Dict[str, object]] | Omit = omit,
        include_content: bool | Omit = omit,
        latency_mode: Literal["low", "high"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryTopPagesResponse:
        """
        Get the top K pages that match the given query

        Args:
          collection_name: The name of the collection.

          k: The number of pages to return. If there are not enough pages matching your
              filters, then fewer may be returned. This number must be between 1 and 1024,
              inclusive.

          query: The natural language query to search with. This cannot exceed 4096 UTF-8 bytes.

          filter: The query filter to apply. Please read [Metadata Filtering](/metadata-filtering)
              for more information. If not provided, then all documents will be searched.

          include_content: If set to true, then the content of all pages will be returned.

          latency_mode: This option selects between our two latency modes. The higher latency mode takes
              longer, but can allow for more accurate responses. If desired, test both to
              customize your search experience for your particular use-case, or use the
              default of "low" and only swap if you need an additional improvement in search
              result quality.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/queries/top-pages",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "k": k,
                    "query": query,
                    "filter": filter,
                    "include_content": include_content,
                    "latency_mode": latency_mode,
                },
                query_top_pages_params.QueryTopPagesParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryTopPagesResponse,
        )

    async def top_snippets(
        self,
        *,
        collection_name: str,
        k: int,
        query: str,
        filter: Optional[Dict[str, object]] | Omit = omit,
        include_document_metadata: bool | Omit = omit,
        precise_responses: bool | Omit = omit,
        reranker: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> QueryTopSnippetsResponse:
        """
        Get the top K snippets that match the given query.

        You may choose between coarse and precise snippets. Precise snippets will
        average ~200 characters, while coarse snippets will average ~2000 characters.
        The default is coarse snippets. Use the `precise_responses` parameter to adjust.

        Args:
          collection_name: The name of the collection.

          k: The number of snippets to return. If there are not enough snippets matching your
              filters, then fewer may be returned. This number must be between 1 and 128,
              inclusive.

          query: The natural language query to search with. This cannot exceed 4096 characters (A
              single UTF-8 codepoint, is considered to be 1 character).

          filter: The query filter to apply. Please read [Metadata Filtering](/metadata-filtering)
              for more information. If not provided, then all documents will be searched.

          include_document_metadata: If true, the `document_results` returns will additionally contain document
              metadata. This is false by default, as returning metadata can add overhead if
              the amount of data to return is large.

          precise_responses: Enable precise responses. Precise responses will have higher latency, but
              provide much more precise snippets. When `precise_responses` is set to `true`,
              the responses will average 200 characters. If set to `false`, the responses will
              average 2000 characters. The default is `false`.

          reranker: The reranker to use after initial retrieval. The default is `null`. You can find
              available model ids, along with more information, at
              [/models/rerank](/api-reference/models/rerank).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/queries/top-snippets",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "k": k,
                    "query": query,
                    "filter": filter,
                    "include_document_metadata": include_document_metadata,
                    "precise_responses": precise_responses,
                    "reranker": reranker,
                },
                query_top_snippets_params.QueryTopSnippetsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=QueryTopSnippetsResponse,
        )


class QueriesResourceWithRawResponse:
    def __init__(self, queries: QueriesResource) -> None:
        self._queries = queries

        self.top_documents = to_raw_response_wrapper(
            queries.top_documents,
        )
        self.top_pages = to_raw_response_wrapper(
            queries.top_pages,
        )
        self.top_snippets = to_raw_response_wrapper(
            queries.top_snippets,
        )


class AsyncQueriesResourceWithRawResponse:
    def __init__(self, queries: AsyncQueriesResource) -> None:
        self._queries = queries

        self.top_documents = async_to_raw_response_wrapper(
            queries.top_documents,
        )
        self.top_pages = async_to_raw_response_wrapper(
            queries.top_pages,
        )
        self.top_snippets = async_to_raw_response_wrapper(
            queries.top_snippets,
        )


class QueriesResourceWithStreamingResponse:
    def __init__(self, queries: QueriesResource) -> None:
        self._queries = queries

        self.top_documents = to_streamed_response_wrapper(
            queries.top_documents,
        )
        self.top_pages = to_streamed_response_wrapper(
            queries.top_pages,
        )
        self.top_snippets = to_streamed_response_wrapper(
            queries.top_snippets,
        )


class AsyncQueriesResourceWithStreamingResponse:
    def __init__(self, queries: AsyncQueriesResource) -> None:
        self._queries = queries

        self.top_documents = async_to_streamed_response_wrapper(
            queries.top_documents,
        )
        self.top_pages = async_to_streamed_response_wrapper(
            queries.top_pages,
        )
        self.top_snippets = async_to_streamed_response_wrapper(
            queries.top_snippets,
        )
