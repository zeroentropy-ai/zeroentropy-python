# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import collection_add_collection_params, collection_delete_collection_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.collection_list_response import CollectionListResponse
from ..types.collection_add_collection_response import CollectionAddCollectionResponse
from ..types.collection_delete_collection_response import CollectionDeleteCollectionResponse

__all__ = ["CollectionsResource", "AsyncCollectionsResource"]


class CollectionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return CollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/zeroentropy-python#with_streaming_response
        """
        return CollectionsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """Gets a complete list of all of your collections."""
        return self._post(
            "/collections/get-collection-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionListResponse,
        )

    def add_collection(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionAddCollectionResponse:
        """
        Adds a collection.

        If the collection already exists, a `409 Conflict` status code will be returned.

        Args:
          collection_name: The name of the collection to add. The maximum length of this string is 1024
              characters. If special characters are used, then the UTF-8 encoded string cannot
              exceed 1024 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/collections/add-collection",
            body=maybe_transform(
                {"collection_name": collection_name}, collection_add_collection_params.CollectionAddCollectionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionAddCollectionResponse,
        )

    def delete_collection(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionDeleteCollectionResponse:
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
            body=maybe_transform(
                {"collection_name": collection_name},
                collection_delete_collection_params.CollectionDeleteCollectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDeleteCollectionResponse,
        )


class AsyncCollectionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCollectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCollectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCollectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/zeroentropy-python#with_streaming_response
        """
        return AsyncCollectionsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionListResponse:
        """Gets a complete list of all of your collections."""
        return await self._post(
            "/collections/get-collection-list",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionListResponse,
        )

    async def add_collection(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionAddCollectionResponse:
        """
        Adds a collection.

        If the collection already exists, a `409 Conflict` status code will be returned.

        Args:
          collection_name: The name of the collection to add. The maximum length of this string is 1024
              characters. If special characters are used, then the UTF-8 encoded string cannot
              exceed 1024 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/collections/add-collection",
            body=await async_maybe_transform(
                {"collection_name": collection_name}, collection_add_collection_params.CollectionAddCollectionParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionAddCollectionResponse,
        )

    async def delete_collection(
        self,
        *,
        collection_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CollectionDeleteCollectionResponse:
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
                {"collection_name": collection_name},
                collection_delete_collection_params.CollectionDeleteCollectionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CollectionDeleteCollectionResponse,
        )


class CollectionsResourceWithRawResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.list = to_raw_response_wrapper(
            collections.list,
        )
        self.add_collection = to_raw_response_wrapper(
            collections.add_collection,
        )
        self.delete_collection = to_raw_response_wrapper(
            collections.delete_collection,
        )


class AsyncCollectionsResourceWithRawResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.list = async_to_raw_response_wrapper(
            collections.list,
        )
        self.add_collection = async_to_raw_response_wrapper(
            collections.add_collection,
        )
        self.delete_collection = async_to_raw_response_wrapper(
            collections.delete_collection,
        )


class CollectionsResourceWithStreamingResponse:
    def __init__(self, collections: CollectionsResource) -> None:
        self._collections = collections

        self.list = to_streamed_response_wrapper(
            collections.list,
        )
        self.add_collection = to_streamed_response_wrapper(
            collections.add_collection,
        )
        self.delete_collection = to_streamed_response_wrapper(
            collections.delete_collection,
        )


class AsyncCollectionsResourceWithStreamingResponse:
    def __init__(self, collections: AsyncCollectionsResource) -> None:
        self._collections = collections

        self.list = async_to_streamed_response_wrapper(
            collections.list,
        )
        self.add_collection = async_to_streamed_response_wrapper(
            collections.add_collection,
        )
        self.delete_collection = async_to_streamed_response_wrapper(
            collections.delete_collection,
        )
