# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentGetInfoListParams"]


class DocumentGetInfoListParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    limit: int
    """The maximum number of documents to return.

    This field is by default 1024, and cannot be set larger than 1024
    """

    path_gt: Optional[str]
    """
    All documents returned will have a path strictly greater than the provided
    `path_gt` argument. (Comparison will be based on lexicographic comparison. It is
    guaranteed that two strings are lexicographically equal if and only if they have
    identical binary representations.).
    """

    path_prefix: Optional[str]
    """
    All documents returned will have a path that starts with the provided path
    prefix.
    """
