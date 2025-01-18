# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CollectionAddParams"]


class CollectionAddParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection to add.

    The maximum length of this string is 1024 characters. If special characters are
    used, then the UTF-8 encoded string cannot exceed 1024 bytes.
    """
