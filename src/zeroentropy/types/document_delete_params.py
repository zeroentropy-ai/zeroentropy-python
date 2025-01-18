# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["DocumentDeleteParams"]


class DocumentDeleteParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    path: Required[str]
    """The filepath of the document that you are deleting.

    A `404 Not Found` status code will be returned if no document with this path was
    found.
    """
