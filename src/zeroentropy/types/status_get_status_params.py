# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

__all__ = ["StatusGetStatusParams"]


class StatusGetStatusParams(TypedDict, total=False):
    collection_name: Optional[str]
    """The collection name to use.

    If `collection_name` is `null` or omitted, then the cumulative status across all
    collections will be shown.
    """
