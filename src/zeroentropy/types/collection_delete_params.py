# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CollectionDeleteParams"]


class CollectionDeleteParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection to delete."""
