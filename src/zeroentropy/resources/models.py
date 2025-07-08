# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from ..types import model_rerank_params
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
from ..types.model_rerank_response import ModelRerankResponse

__all__ = ["ModelsResource", "AsyncModelsResource"]


class ModelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return ModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return ModelsResourceWithStreamingResponse(self)

    def rerank(
        self,
        *,
        documents: List[str],
        query: str,
        model: str | NotGiven = NOT_GIVEN,
        top_n: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelRerankResponse:
        """
        Reranks the provided documents, according to the provided query.

        The results will be sorted by descending order of relevance. For each document,
        the index and the score will be returned. The index is relative to the documents
        array that was passed in. The score is the query-document relevancy determined
        by the reranker model. The value will be returned in descending order to
        relevance.

        Args:
          documents: The list of documents to rerank. Each document is a string.

          query: The query to rerank the documents by. Results will be in descending order of
              relevance.

          model: The model ID to use for reranking. Options are: ["zerank-1-large"]

          top_n: If provided, then only the top `n` documents will be returned in the results
              array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/models/rerank",
            body=maybe_transform(
                {
                    "documents": documents,
                    "query": query,
                    "model": model,
                    "top_n": top_n,
                },
                model_rerank_params.ModelRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelRerankResponse,
        )


class AsyncModelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncModelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncModelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncModelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return AsyncModelsResourceWithStreamingResponse(self)

    async def rerank(
        self,
        *,
        documents: List[str],
        query: str,
        model: str | NotGiven = NOT_GIVEN,
        top_n: Optional[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ModelRerankResponse:
        """
        Reranks the provided documents, according to the provided query.

        The results will be sorted by descending order of relevance. For each document,
        the index and the score will be returned. The index is relative to the documents
        array that was passed in. The score is the query-document relevancy determined
        by the reranker model. The value will be returned in descending order to
        relevance.

        Args:
          documents: The list of documents to rerank. Each document is a string.

          query: The query to rerank the documents by. Results will be in descending order of
              relevance.

          model: The model ID to use for reranking. Options are: ["zerank-1-large"]

          top_n: If provided, then only the top `n` documents will be returned in the results
              array.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/models/rerank",
            body=await async_maybe_transform(
                {
                    "documents": documents,
                    "query": query,
                    "model": model,
                    "top_n": top_n,
                },
                model_rerank_params.ModelRerankParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelRerankResponse,
        )


class ModelsResourceWithRawResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.rerank = to_raw_response_wrapper(
            models.rerank,
        )


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.rerank = async_to_raw_response_wrapper(
            models.rerank,
        )


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.rerank = to_streamed_response_wrapper(
            models.rerank,
        )


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.rerank = async_to_streamed_response_wrapper(
            models.rerank,
        )
