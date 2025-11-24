# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import collection_add_params, collection_delete_params
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
from ..types.collection_add_response import CollectionAddResponse
from ..types.collection_delete_response import CollectionDeleteResponse
from ..types.collection_get_list_response import CollectionGetListResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionDeleteResponse:
        """
        Deletes a collection.

        A `404 Not Found` status code will be returned, if the provided collection name
        does not exist.

        Args:
          collection_name: The name of the collection to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections/delete-collection",
            body=maybe_transform({"collection_name": collection_name}, collection_delete_params.CollectionDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDeleteResponse,
        )

    def add(
        self,
        *,
        collection_name: str,
        num_shards: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionAddResponse:
        """
        Adds a collection.

        If the collection already exists, a `409 Conflict` status code will be returned.

        Args:
          collection_name: The name of the collection to add. The maximum length of this string is 1024
              characters. If special characters are used, then the UTF-8 encoded string cannot
              exceed 1024 bytes.

          num_shards: [ADVANCED] The number of shards to use for this collection. By using K shards,
              your documents can index with K times more throughput. However, queries will be
              automatically sent to all K shards and then aggregated. For large collections,
              this can make queries faster. But for small collections, this will make queries
              slower. `num_shards` must be one of [1, 8, 16, 32, 64]. The default is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections/add-collection",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "num_shards": num_shards,
                },
                collection_add_params.CollectionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionAddResponse,
        )

    def get_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionGetListResponse:
        """Gets a complete list of all of your collections."""
        return self._post(
            "/collections/get-collection-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionGetListResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionDeleteResponse:
        """
        Deletes a collection.

        A `404 Not Found` status code will be returned, if the provided collection name
        does not exist.

        Args:
          collection_name: The name of the collection to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections/delete-collection",
            body=await async_maybe_transform(
                {"collection_name": collection_name}, collection_delete_params.CollectionDeleteParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDeleteResponse,
        )

    async def add(
        self,
        *,
        collection_name: str,
        num_shards: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionAddResponse:
        """
        Adds a collection.

        If the collection already exists, a `409 Conflict` status code will be returned.

        Args:
          collection_name: The name of the collection to add. The maximum length of this string is 1024
              characters. If special characters are used, then the UTF-8 encoded string cannot
              exceed 1024 bytes.

          num_shards: [ADVANCED] The number of shards to use for this collection. By using K shards,
              your documents can index with K times more throughput. However, queries will be
              automatically sent to all K shards and then aggregated. For large collections,
              this can make queries faster. But for small collections, this will make queries
              slower. `num_shards` must be one of [1, 8, 16, 32, 64]. The default is 1.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections/add-collection",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "num_shards": num_shards,
                },
                collection_add_params.CollectionAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionAddResponse,
        )

    async def get_list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CollectionGetListResponse:
        """Gets a complete list of all of your collections."""
        return await self._post(
            "/collections/get-collection-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionGetListResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.delete = to_raw_response_wrapper(
            collections.delete,
        )
        self.add = to_raw_response_wrapper(
            collections.add,
        )
        self.get_list = to_raw_response_wrapper(
            collections.get_list,
        )


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.delete = async_to_raw_response_wrapper(
            collections.delete,
        )
        self.add = async_to_raw_response_wrapper(
            collections.add,
        )
        self.get_list = async_to_raw_response_wrapper(
            collections.get_list,
        )


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.delete = to_streamed_response_wrapper(
            collections.delete,
        )
        self.add = to_streamed_response_wrapper(
            collections.add,
        )
        self.get_list = to_streamed_response_wrapper(
            collections.get_list,
        )


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.delete = async_to_streamed_response_wrapper(
            collections.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            collections.add,
        )
        self.get_list = async_to_streamed_response_wrapper(
            collections.get_list,
        )
