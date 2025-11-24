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

    num_shards: int
    """[ADVANCED] The number of shards to use for this collection.

    By using K shards, your documents can index with K times more throughput.
    However, queries will be automatically sent to all K shards and then aggregated.
    For large collections, this can make queries faster. But for small collections,
    this will make queries slower. `num_shards` must be one of [1, 8, 16, 32, 64].
    The default is 1.
    """
