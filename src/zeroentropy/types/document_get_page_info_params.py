# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentGetPageInfoParams"]


class DocumentGetPageInfoParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    page_index: Required[int]
    """The specific page index whose info is being requested.

    Pages are 0-indexed, so that the 1st page of a PDF is of page index 0. You may
    use the `num_pages` attribute of `/documents/get-document-info` or
    `/documents/get-document-info-list` to know what the range of valid indices are.
    A `404 Not Found` status code will be returned if no such page index exists.
    """

    path: Required[str]
    """The filepath of the document whose page you are requesting.

    A `404 Not Found` status code will be returned if no document with this path was
    found.
    """

    include_content: bool
    """
    If `true`, then the response will have the `content` attribute be a `string`,
    rather than `null`. This string will contain the full contents of the page.
    """

    include_image: bool
    """
    If `true`, then the response will have the `image_base64_data` attribute be a
    `string`\\**, rather than `null`. This string will contain the image data of the
    document, as a base64-encoded string. Currently, this data is guaranteed to be a
    JPEG-encoded image.

    \\**Note that the response may still be `null`, if the page has no image data,
    such as if the document was uploaded with raw text rather than as a PDF.
    """
