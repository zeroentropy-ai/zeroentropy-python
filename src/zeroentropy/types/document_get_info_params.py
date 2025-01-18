# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentGetInfoParams"]


class DocumentGetInfoParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    path: Required[str]
    """The filepath of the document that you're requesting.

    A `404 Not Found` status code will be returned if no document with this path was
    found.
    """

    include_content: bool
    """
    If `true`, then the document response will have the `content` attribute be a
    `string`, rather than `null`. This string will contain the full contents of the
    document.
    """
