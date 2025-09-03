# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["DocumentUpdateParams"]


class DocumentUpdateParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    path: Required[str]
    """The filepath of the document that you are updating.

    A `404 Not Found` status code will be returned if no document with this path was
    found.
    """

    index_status: Optional[Literal["not_parsed", "not_indexed"]]
    """
    If the document is in the index_status of
    `parsing_failed or `indexing_failed`, then this endpoint allows you to update the index status to `not_parsed`and`not_indexed`,
    respectively. This allows the document to re-attempt to parse/index after
    failure.
    """

    metadata: Optional[Dict[str, Union[str, SequenceNotStr[str]]]]
    """
    If this field is provided, the given metadata json will replace the document's
    existing metadata json. In other words, if you want to add a new field, you will
    need to provide the entire metadata object (Both the original fields, and the
    new field).
    """
