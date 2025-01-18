# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentListInfoParams"]


class DocumentListInfoParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    id_gt: Optional[str]
    """All documents returned will have a UUID strictly greater than the provided UUID.

    (Comparison will be on the binary representations of the UUIDs)
    """

    limit: int
    """The maximum number of documents to return.

    This field is by default 1024, and cannot be set larger than 1024
    """
