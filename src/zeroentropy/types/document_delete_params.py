# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DocumentDeleteParams"]


class DocumentDeleteParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    path: Required[Union[str, SequenceNotStr[str]]]
    """The path(s) of the document(s) that you are deleting.

    Must be either a `string`, or a `list[str]` between 1 and 64 inclusive. A
    `404 Not Found` status code will be returned if no document(s) with this path
    was found. If at least one of the paths provided do exist, then `200 OK` will be
    returned, along with an array of the document paths that were found and thus
    deleted.
    """
