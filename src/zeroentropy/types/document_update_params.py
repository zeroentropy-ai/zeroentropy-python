# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DocumentUpdateParams"]


class DocumentUpdateParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    path: Required[str]
    """The filepath of the document that you are updating.

    A `404 Not Found` status code will be returned if no document with this path was
    found.
    """

    metadata: Optional[Dict[str, Union[str, List[str]]]]
    """
    If this field is provided, the given metadata json will replace the document's
    existing metadata json. In other words, if you want to add a new field, you will
    need to provide the entire metadata object (Both the original fields, and the
    new field).
    """
