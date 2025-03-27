# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional

import httpx

from ..types import (
    document_add_params,
    document_delete_params,
    document_update_params,
    document_get_info_params,
    document_get_info_list_params,
    document_get_page_info_params,
)
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
from ..types.document_add_response import DocumentAddResponse
from ..types.document_delete_response import DocumentDeleteResponse
from ..types.document_update_response import DocumentUpdateResponse
from ..types.document_get_info_response import DocumentGetInfoResponse
from ..types.document_get_info_list_response import DocumentGetInfoListResponse
from ..types.document_get_page_info_response import DocumentGetPageInfoResponse

__all__ = ["DocumentsResource", "AsyncDocumentsResource"]


class DocumentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return DocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return DocumentsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        collection_name: str,
        path: str,
        metadata: Optional[Dict[str, Union[str, List[str]]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUpdateResponse:
        """Updates a document.

        This endpoint is atomic.

        The only attribute currently supported for update is `metadata`. This endpoint
        can only be called with a non-null `metadata` if the document status is
        `indexed`.

        Sometimes, when updating a document, a new document ID will be assigned and the
        previous will be deleted. For this reason, the previous and the new document ID
        will both be returned in the response. If the document ID was not updated, then
        these two IDs will be identical.

        A `404 Not Found` status code will be returned, if the provided collection name
        or document path does not exist.

        Args:
          collection_name: The name of the collection.

          path: The filepath of the document that you are updating. A `404 Not Found` status
              code will be returned if no document with this path was found.

          metadata: If this field is provided, the given metadata json will replace the document's
              existing metadata json. In other words, if you want to add a new field, you will
              need to provide the entire metadata object (Both the original fields, and the
              new field).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents/update-document",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "path": path,
                    "metadata": metadata,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    def delete(
        self,
        *,
        collection_name: str,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentDeleteResponse:
        """
        Deletes a document

        A `404 Not Found` status code will be returned, if the provided collection name
        or document path does not exist.

        Args:
          collection_name: The name of the collection.

          path: The filepath of the document that you are deleting. A `404 Not Found` status
              code will be returned if no document with this path was found.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents/delete-document",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "path": path,
                },
                document_delete_params.DocumentDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDeleteResponse,
        )

    def add(
        self,
        *,
        collection_name: str,
        content: document_add_params.Content,
        path: str,
        metadata: Dict[str, Union[str, List[str]]] | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentAddResponse:
        """
        Adds a document to a given collection.

        A status code of `201 Created` will be returned if a document was successfully
        added. A status code of `409 Conflict` will be returned if the given collection
        already has a document with the same path.

        If `overwrite` is given a value of `true`, then a status code of `200 OK` will
        be returned if a document was overwritten (Rather than a status code of
        `409 Conflict`).

        When a document is inserted, it can take time to appear in the index. Check the
        `/status/get-status` endpoint to see progress.

        Args:
          collection_name: The name of the collection to be used for this request. A `404 Not Found` status
              code will be returned if this collection name does not exist.

          content: The content of the document. There are three possible JSON types that can be
              passed into this parameter: `APITextDocument`, `APITextPagesDocument`,
              `APIBinaryDocument`. The `type` field is how ZeroEntropy will know which
              document object you have passed in.

          path: The filepath of the document that you are adding. A `409 Conflict` status code
              will be returned if this path already exists, unless `overwrite` is set to
              `true`.

          metadata: This is a metadata JSON object that can be used to assign various metadata
              attributes to your document. The provided object must match the type
              `dict[str, str | list[str]]`. Please read
              [Metadata Filtering](/metadata-filtering) for more details. By default, the
              metadata will be set to `{}`.

              NOTE: The UTF-8-encoded JSON string must be less than 65536 bytes (Whitespace
              does not count). This limit can be increased upon request.

          overwrite: Setting this property to true will put this endpoint in "upsert" mode: If the
              document already exists, this action will atomically replace it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents/add-document",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "content": content,
                    "path": path,
                    "metadata": metadata,
                    "overwrite": overwrite,
                },
                document_add_params.DocumentAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentAddResponse,
        )

    def get_info(
        self,
        *,
        collection_name: str,
        path: str,
        include_content: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentGetInfoResponse:
        """Retrieves information about a specific document.

        The request parameters define
        what information you would like to receive.

        A `404 Not Found` will be returned if either the collection name does not exist,
        or the document path does not exist within the provided collection.

        Args:
          collection_name: The name of the collection.

          path: The filepath of the document that you're requesting. A `404 Not Found` status
              code will be returned if no document with this path was found.

          include_content: If `true`, then the document response will have the `content` attribute be a
              `string`, rather than `null`. This string will contain the full contents of the
              document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents/get-document-info",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "path": path,
                    "include_content": include_content,
                },
                document_get_info_params.DocumentGetInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetInfoResponse,
        )

    def get_info_list(
        self,
        *,
        collection_name: str,
        id_gt: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentGetInfoListResponse:
        """
        Retrives a list of document metadata information that matches the provided
        filters.

        The documents returned will be sorted by ID in ascending order. `id_gt` can be
        used for pagination, and should be set to the ID of the last document returned
        in the previous call.

        A `404 Not Found` will be returned if either the collection name does not exist,
        or the document path does not exist within the provided collection.

        Args:
          collection_name: The name of the collection.

          id_gt: All documents returned will have a UUID strictly greater than the provided UUID.
              (Comparison will be on the binary representations of the UUIDs)

          limit: The maximum number of documents to return. This field is by default 1024, and
              cannot be set larger than 1024

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents/get-document-info-list",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "id_gt": id_gt,
                    "limit": limit,
                },
                document_get_info_list_params.DocumentGetInfoListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetInfoListResponse,
        )

    def get_page_info(
        self,
        *,
        collection_name: str,
        page_index: int,
        path: str,
        include_content: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentGetPageInfoResponse:
        """Retrieves information about a specific page.

        The request parameters define what
        information you would like to receive.

        A `404 Not Found` will be returned if either the collection name does not exist,
        or the document path does not exist within the provided collection.

        Args:
          collection_name: The name of the collection.

          page_index: The specific page index whose info is being requested. Pages are 0-indexed, so
              that the 1st page of a PDF is of page index 0. You may use the `num_pages`
              attribute of `/documents/get-document-info` or
              `/documents/get-document-info-list` to know what the range of valid indices are.
              A `404 Not Found` status code will be returned if no such page index exists.

          path: The filepath of the document whose page you are requesting. A `404 Not Found`
              status code will be returned if no document with this path was found.

          include_content: If `true`, then the response will have the `content` attribute be a `string`,
              rather than `null`. This string will contain the full contents of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/documents/get-page-info",
            body=maybe_transform(
                {
                    "collection_name": collection_name,
                    "page_index": page_index,
                    "path": path,
                    "include_content": include_content,
                },
                document_get_page_info_params.DocumentGetPageInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetPageInfoResponse,
        )


class AsyncDocumentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDocumentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/zeroentropy-ai/zeroentropy-python#with_streaming_response
        """
        return AsyncDocumentsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        collection_name: str,
        path: str,
        metadata: Optional[Dict[str, Union[str, List[str]]]] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentUpdateResponse:
        """Updates a document.

        This endpoint is atomic.

        The only attribute currently supported for update is `metadata`. This endpoint
        can only be called with a non-null `metadata` if the document status is
        `indexed`.

        Sometimes, when updating a document, a new document ID will be assigned and the
        previous will be deleted. For this reason, the previous and the new document ID
        will both be returned in the response. If the document ID was not updated, then
        these two IDs will be identical.

        A `404 Not Found` status code will be returned, if the provided collection name
        or document path does not exist.

        Args:
          collection_name: The name of the collection.

          path: The filepath of the document that you are updating. A `404 Not Found` status
              code will be returned if no document with this path was found.

          metadata: If this field is provided, the given metadata json will replace the document's
              existing metadata json. In other words, if you want to add a new field, you will
              need to provide the entire metadata object (Both the original fields, and the
              new field).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents/update-document",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "path": path,
                    "metadata": metadata,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    async def delete(
        self,
        *,
        collection_name: str,
        path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentDeleteResponse:
        """
        Deletes a document

        A `404 Not Found` status code will be returned, if the provided collection name
        or document path does not exist.

        Args:
          collection_name: The name of the collection.

          path: The filepath of the document that you are deleting. A `404 Not Found` status
              code will be returned if no document with this path was found.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents/delete-document",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "path": path,
                },
                document_delete_params.DocumentDeleteParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDeleteResponse,
        )

    async def add(
        self,
        *,
        collection_name: str,
        content: document_add_params.Content,
        path: str,
        metadata: Dict[str, Union[str, List[str]]] | NotGiven = NOT_GIVEN,
        overwrite: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentAddResponse:
        """
        Adds a document to a given collection.

        A status code of `201 Created` will be returned if a document was successfully
        added. A status code of `409 Conflict` will be returned if the given collection
        already has a document with the same path.

        If `overwrite` is given a value of `true`, then a status code of `200 OK` will
        be returned if a document was overwritten (Rather than a status code of
        `409 Conflict`).

        When a document is inserted, it can take time to appear in the index. Check the
        `/status/get-status` endpoint to see progress.

        Args:
          collection_name: The name of the collection to be used for this request. A `404 Not Found` status
              code will be returned if this collection name does not exist.

          content: The content of the document. There are three possible JSON types that can be
              passed into this parameter: `APITextDocument`, `APITextPagesDocument`,
              `APIBinaryDocument`. The `type` field is how ZeroEntropy will know which
              document object you have passed in.

          path: The filepath of the document that you are adding. A `409 Conflict` status code
              will be returned if this path already exists, unless `overwrite` is set to
              `true`.

          metadata: This is a metadata JSON object that can be used to assign various metadata
              attributes to your document. The provided object must match the type
              `dict[str, str | list[str]]`. Please read
              [Metadata Filtering](/metadata-filtering) for more details. By default, the
              metadata will be set to `{}`.

              NOTE: The UTF-8-encoded JSON string must be less than 65536 bytes (Whitespace
              does not count). This limit can be increased upon request.

          overwrite: Setting this property to true will put this endpoint in "upsert" mode: If the
              document already exists, this action will atomically replace it.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents/add-document",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "content": content,
                    "path": path,
                    "metadata": metadata,
                    "overwrite": overwrite,
                },
                document_add_params.DocumentAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentAddResponse,
        )

    async def get_info(
        self,
        *,
        collection_name: str,
        path: str,
        include_content: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentGetInfoResponse:
        """Retrieves information about a specific document.

        The request parameters define
        what information you would like to receive.

        A `404 Not Found` will be returned if either the collection name does not exist,
        or the document path does not exist within the provided collection.

        Args:
          collection_name: The name of the collection.

          path: The filepath of the document that you're requesting. A `404 Not Found` status
              code will be returned if no document with this path was found.

          include_content: If `true`, then the document response will have the `content` attribute be a
              `string`, rather than `null`. This string will contain the full contents of the
              document.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents/get-document-info",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "path": path,
                    "include_content": include_content,
                },
                document_get_info_params.DocumentGetInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetInfoResponse,
        )

    async def get_info_list(
        self,
        *,
        collection_name: str,
        id_gt: Optional[str] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentGetInfoListResponse:
        """
        Retrives a list of document metadata information that matches the provided
        filters.

        The documents returned will be sorted by ID in ascending order. `id_gt` can be
        used for pagination, and should be set to the ID of the last document returned
        in the previous call.

        A `404 Not Found` will be returned if either the collection name does not exist,
        or the document path does not exist within the provided collection.

        Args:
          collection_name: The name of the collection.

          id_gt: All documents returned will have a UUID strictly greater than the provided UUID.
              (Comparison will be on the binary representations of the UUIDs)

          limit: The maximum number of documents to return. This field is by default 1024, and
              cannot be set larger than 1024

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents/get-document-info-list",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "id_gt": id_gt,
                    "limit": limit,
                },
                document_get_info_list_params.DocumentGetInfoListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetInfoListResponse,
        )

    async def get_page_info(
        self,
        *,
        collection_name: str,
        page_index: int,
        path: str,
        include_content: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DocumentGetPageInfoResponse:
        """Retrieves information about a specific page.

        The request parameters define what
        information you would like to receive.

        A `404 Not Found` will be returned if either the collection name does not exist,
        or the document path does not exist within the provided collection.

        Args:
          collection_name: The name of the collection.

          page_index: The specific page index whose info is being requested. Pages are 0-indexed, so
              that the 1st page of a PDF is of page index 0. You may use the `num_pages`
              attribute of `/documents/get-document-info` or
              `/documents/get-document-info-list` to know what the range of valid indices are.
              A `404 Not Found` status code will be returned if no such page index exists.

          path: The filepath of the document whose page you are requesting. A `404 Not Found`
              status code will be returned if no document with this path was found.

          include_content: If `true`, then the response will have the `content` attribute be a `string`,
              rather than `null`. This string will contain the full contents of the page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/documents/get-page-info",
            body=await async_maybe_transform(
                {
                    "collection_name": collection_name,
                    "page_index": page_index,
                    "path": path,
                    "include_content": include_content,
                },
                document_get_page_info_params.DocumentGetPageInfoParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetPageInfoResponse,
        )


class DocumentsResourceWithRawResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.update = to_raw_response_wrapper(
            documents.update,
        )
        self.delete = to_raw_response_wrapper(
            documents.delete,
        )
        self.add = to_raw_response_wrapper(
            documents.add,
        )
        self.get_info = to_raw_response_wrapper(
            documents.get_info,
        )
        self.get_info_list = to_raw_response_wrapper(
            documents.get_info_list,
        )
        self.get_page_info = to_raw_response_wrapper(
            documents.get_page_info,
        )


class AsyncDocumentsResourceWithRawResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.update = async_to_raw_response_wrapper(
            documents.update,
        )
        self.delete = async_to_raw_response_wrapper(
            documents.delete,
        )
        self.add = async_to_raw_response_wrapper(
            documents.add,
        )
        self.get_info = async_to_raw_response_wrapper(
            documents.get_info,
        )
        self.get_info_list = async_to_raw_response_wrapper(
            documents.get_info_list,
        )
        self.get_page_info = async_to_raw_response_wrapper(
            documents.get_page_info,
        )


class DocumentsResourceWithStreamingResponse:
    def __init__(self, documents: DocumentsResource) -> None:
        self._documents = documents

        self.update = to_streamed_response_wrapper(
            documents.update,
        )
        self.delete = to_streamed_response_wrapper(
            documents.delete,
        )
        self.add = to_streamed_response_wrapper(
            documents.add,
        )
        self.get_info = to_streamed_response_wrapper(
            documents.get_info,
        )
        self.get_info_list = to_streamed_response_wrapper(
            documents.get_info_list,
        )
        self.get_page_info = to_streamed_response_wrapper(
            documents.get_page_info,
        )


class AsyncDocumentsResourceWithStreamingResponse:
    def __init__(self, documents: AsyncDocumentsResource) -> None:
        self._documents = documents

        self.update = async_to_streamed_response_wrapper(
            documents.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            documents.delete,
        )
        self.add = async_to_streamed_response_wrapper(
            documents.add,
        )
        self.get_info = async_to_streamed_response_wrapper(
            documents.get_info,
        )
        self.get_info_list = async_to_streamed_response_wrapper(
            documents.get_info_list,
        )
        self.get_page_info = async_to_streamed_response_wrapper(
            documents.get_page_info,
        )
