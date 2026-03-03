# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal

import httpx

from ..types import model_embed_params, model_rerank_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.model_embed_response import ModelEmbedResponse
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

    def embed(
        self,
        *,
        input: Union[str, SequenceNotStr[str]],
        input_type: Literal["query", "document"],
        model: str,
        dimensions: Optional[int] | Omit = omit,
        encoding_format: Literal["float", "base64"] | Omit = omit,
        latency: Optional[Literal["fast", "slow"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelEmbedResponse:
        """
        Embeds the provided input text with ZeroEntropy embedding models.

        The results will be returned in the same order as the text provided. The
        embedding is such that queries will have high cosine similarity with documents
        that are relevant to that query.

        Organizations will, by default, have a ratelimit of `2,500,000` bytes-per-minute
        and 1000 QPM. Ratelimits are refreshed every 15 seconds. If this is exceeded,
        requests will be throttled into `latency: "slow"` mode, up to `20,000,000`
        bytes-per-minute. If even this is exceeded, you will get a `429` error. To
        request higher ratelimits, please contact
        [founders@zeroentropy.dev](mailto:founders@zeroentropy.dev) or message us on
        [Discord](https://go.zeroentropy.dev/discord) or
        [Slack](https://go.zeroentropy.dev/slack)!

        Args:
          input: The string, or list of strings, to embed.

          input_type: The input type. For retrieval tasks, either `query` or `document`.

          model: The model ID to use for embedding. Options are: ["zembed-1"]

          dimensions: The output dimensionality of the embedding model. For `zembed-1`, the available
              options are: [2560, 1280, 640, 320, 160, 80, 40].

          encoding_format: The output format of the embedding. If `float`, an array of floats will be
              returned for each embeddings. If `base64`, a f32 little endian byte array will
              be returned, encoded as a base64 string. `base64` is significantly more
              efficient than `float`. The default is `float`.

          latency: Whether the call will be inferenced "fast" or "slow". RateLimits for slow API
              calls are orders of magnitude higher, but you can expect 2-20 second latency.
              Fast inferences are guaranteed subsecond, but rate limits are lower. If not
              specified, first a "fast" call will be attempted, but if you have exceeded your
              fast rate limit, then a slow call will be executed. If explicitly set to "fast",
              then 429 will be returned if it cannot be executed fast.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/models/embed",
            body=maybe_transform(
                {
                    "input": input,
                    "input_type": input_type,
                    "model": model,
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                    "latency": latency,
                },
                model_embed_params.ModelEmbedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelEmbedResponse,
        )

    def rerank(
        self,
        *,
        documents: SequenceNotStr[str],
        model: str,
        query: str,
        latency: Optional[Literal["fast", "slow"]] | Omit = omit,
        top_n: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelRerankResponse:
        """
        Reranks the provided documents, according to the provided query.

        The results will be sorted by descending order of relevance. For each document,
        the index and the score will be returned. The index is relative to the documents
        array that was passed in. The score is the query-document relevancy determined
        by the reranker model. The results will be returned in descending order of
        relevance.

        Organizations will, by default, have a ratelimit of `2,500,000` bytes-per-minute
        and 1000 QPM. Ratelimits are refreshed every 15 seconds. If this is exceeded,
        requests will be throttled into `latency: "slow"` mode, up to `20,000,000`
        bytes-per-minute. If even this is exceeded, you will get a `429` error. To
        request higher ratelimits, please contact
        [founders@zeroentropy.dev](mailto:founders@zeroentropy.dev) or message us on
        [Discord](https://go.zeroentropy.dev/discord) or
        [Slack](https://go.zeroentropy.dev/slack)!

        Args:
          documents: The list of documents to rerank. Each document is a string.

          model: The model ID to use for reranking. Options are: ["zerank-2", "zerank-1",
              "zerank-1-small"]

          query: The query to rerank the documents by.

          latency: Whether the call will be inferenced "fast" or "slow". RateLimits for slow API
              calls are orders of magnitude higher, but you can expect >10 second latency.
              Fast inferences are guaranteed subsecond, but rate limits are lower. If not
              specified, first a "fast" call will be attempted, but if you have exceeded your
              fast rate limit, then a slow call will be executed. If explicitly set to "fast",
              then 429 will be returned if it cannot be executed fast.

          top_n: If provided, then only the top `n` documents will be returned in the results
              array. Otherwise, `n` will be the length of the provided documents array.

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
                    "model": model,
                    "query": query,
                    "latency": latency,
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

    async def embed(
        self,
        *,
        input: Union[str, SequenceNotStr[str]],
        input_type: Literal["query", "document"],
        model: str,
        dimensions: Optional[int] | Omit = omit,
        encoding_format: Literal["float", "base64"] | Omit = omit,
        latency: Optional[Literal["fast", "slow"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelEmbedResponse:
        """
        Embeds the provided input text with ZeroEntropy embedding models.

        The results will be returned in the same order as the text provided. The
        embedding is such that queries will have high cosine similarity with documents
        that are relevant to that query.

        Organizations will, by default, have a ratelimit of `2,500,000` bytes-per-minute
        and 1000 QPM. Ratelimits are refreshed every 15 seconds. If this is exceeded,
        requests will be throttled into `latency: "slow"` mode, up to `20,000,000`
        bytes-per-minute. If even this is exceeded, you will get a `429` error. To
        request higher ratelimits, please contact
        [founders@zeroentropy.dev](mailto:founders@zeroentropy.dev) or message us on
        [Discord](https://go.zeroentropy.dev/discord) or
        [Slack](https://go.zeroentropy.dev/slack)!

        Args:
          input: The string, or list of strings, to embed.

          input_type: The input type. For retrieval tasks, either `query` or `document`.

          model: The model ID to use for embedding. Options are: ["zembed-1"]

          dimensions: The output dimensionality of the embedding model. For `zembed-1`, the available
              options are: [2560, 1280, 640, 320, 160, 80, 40].

          encoding_format: The output format of the embedding. If `float`, an array of floats will be
              returned for each embeddings. If `base64`, a f32 little endian byte array will
              be returned, encoded as a base64 string. `base64` is significantly more
              efficient than `float`. The default is `float`.

          latency: Whether the call will be inferenced "fast" or "slow". RateLimits for slow API
              calls are orders of magnitude higher, but you can expect 2-20 second latency.
              Fast inferences are guaranteed subsecond, but rate limits are lower. If not
              specified, first a "fast" call will be attempted, but if you have exceeded your
              fast rate limit, then a slow call will be executed. If explicitly set to "fast",
              then 429 will be returned if it cannot be executed fast.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/models/embed",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "input_type": input_type,
                    "model": model,
                    "dimensions": dimensions,
                    "encoding_format": encoding_format,
                    "latency": latency,
                },
                model_embed_params.ModelEmbedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ModelEmbedResponse,
        )

    async def rerank(
        self,
        *,
        documents: SequenceNotStr[str],
        model: str,
        query: str,
        latency: Optional[Literal["fast", "slow"]] | Omit = omit,
        top_n: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ModelRerankResponse:
        """
        Reranks the provided documents, according to the provided query.

        The results will be sorted by descending order of relevance. For each document,
        the index and the score will be returned. The index is relative to the documents
        array that was passed in. The score is the query-document relevancy determined
        by the reranker model. The results will be returned in descending order of
        relevance.

        Organizations will, by default, have a ratelimit of `2,500,000` bytes-per-minute
        and 1000 QPM. Ratelimits are refreshed every 15 seconds. If this is exceeded,
        requests will be throttled into `latency: "slow"` mode, up to `20,000,000`
        bytes-per-minute. If even this is exceeded, you will get a `429` error. To
        request higher ratelimits, please contact
        [founders@zeroentropy.dev](mailto:founders@zeroentropy.dev) or message us on
        [Discord](https://go.zeroentropy.dev/discord) or
        [Slack](https://go.zeroentropy.dev/slack)!

        Args:
          documents: The list of documents to rerank. Each document is a string.

          model: The model ID to use for reranking. Options are: ["zerank-2", "zerank-1",
              "zerank-1-small"]

          query: The query to rerank the documents by.

          latency: Whether the call will be inferenced "fast" or "slow". RateLimits for slow API
              calls are orders of magnitude higher, but you can expect >10 second latency.
              Fast inferences are guaranteed subsecond, but rate limits are lower. If not
              specified, first a "fast" call will be attempted, but if you have exceeded your
              fast rate limit, then a slow call will be executed. If explicitly set to "fast",
              then 429 will be returned if it cannot be executed fast.

          top_n: If provided, then only the top `n` documents will be returned in the results
              array. Otherwise, `n` will be the length of the provided documents array.

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
                    "model": model,
                    "query": query,
                    "latency": latency,
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

        self.embed = to_raw_response_wrapper(
            models.embed,
        )
        self.rerank = to_raw_response_wrapper(
            models.rerank,
        )


class AsyncModelsResourceWithRawResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.embed = async_to_raw_response_wrapper(
            models.embed,
        )
        self.rerank = async_to_raw_response_wrapper(
            models.rerank,
        )


class ModelsResourceWithStreamingResponse:
    def __init__(self, models: ModelsResource) -> None:
        self._models = models

        self.embed = to_streamed_response_wrapper(
            models.embed,
        )
        self.rerank = to_streamed_response_wrapper(
            models.rerank,
        )


class AsyncModelsResourceWithStreamingResponse:
    def __init__(self, models: AsyncModelsResource) -> None:
        self._models = models

        self.embed = async_to_streamed_response_wrapper(
            models.embed,
        )
        self.rerank = async_to_streamed_response_wrapper(
            models.rerank,
        )
