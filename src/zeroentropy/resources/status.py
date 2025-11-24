# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import status_get_status_params
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
from ..types.status_get_status_response import StatusGetStatusResponse

__all__ = ["StatusResource", "AsyncStatusResource"]


class StatusResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return StatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return StatusResourceWithStreamingResponse(self)

    def get_status(
        self,
        *,
        collection_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatusGetStatusResponse:
        """
        Gets the current indexing status across all documents.

        If a collection name is passed in, it will get the indexing status of only the
        documents within that collection. Otherwise, it will show the cumulative status
        across all of your collections.

        A `404 Not Found` status code will be returned, if a collection name was
        provided, but it does not exist.

        Args:
          collection_name: The collection name to use. If `collection_name` is `null` or omitted, then the
              cumulative status across all collections will be shown.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/status/get-status",
            body=maybe_transform({"collection_name": collection_name}, status_get_status_params.StatusGetStatusParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatusGetStatusResponse,
        )


class AsyncStatusResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStatusResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncStatusResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStatusResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return AsyncStatusResourceWithStreamingResponse(self)

    async def get_status(
        self,
        *,
        collection_name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> StatusGetStatusResponse:
        """
        Gets the current indexing status across all documents.

        If a collection name is passed in, it will get the indexing status of only the
        documents within that collection. Otherwise, it will show the cumulative status
        across all of your collections.

        A `404 Not Found` status code will be returned, if a collection name was
        provided, but it does not exist.

        Args:
          collection_name: The collection name to use. If `collection_name` is `null` or omitted, then the
              cumulative status across all collections will be shown.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/status/get-status",
            body=await async_maybe_transform(
                {"collection_name": collection_name}, status_get_status_params.StatusGetStatusParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StatusGetStatusResponse,
        )


class StatusResourceWithRawResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.get_status = to_raw_response_wrapper(
            status.get_status,
        )


class AsyncStatusResourceWithRawResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.get_status = async_to_raw_response_wrapper(
            status.get_status,
        )


class StatusResourceWithStreamingResponse:
    def __init__(self, status: StatusResource) -> None:
        self._status = status

        self.get_status = to_streamed_response_wrapper(
            status.get_status,
        )


class AsyncStatusResourceWithStreamingResponse:
    def __init__(self, status: AsyncStatusResource) -> None:
        self._status = status

        self.get_status = async_to_streamed_response_wrapper(
            status.get_status,
        )
