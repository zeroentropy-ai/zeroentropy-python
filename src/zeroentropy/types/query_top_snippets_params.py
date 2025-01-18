# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .str_json_param import StrJsonParam

__all__ = ["QueryTopSnippetsParams"]


class QueryTopSnippetsParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    k: Required[int]
    """The number of snippets to return.

    If there are not enough snippets matching your filters, then fewer may be
    returned. This number must be between 1 and 2048, inclusive.
    """

    query: Required[str]
    """The natural language query to search with.

    This cannot exceed 4096 characters (A single UTF-8 codepoint, is considered to
    be 1 character).
    """

    filter: Optional[StrJsonParam]
    """The query filter to apply.

    Please read [Metadata Filtering](/metadata-filtering) for more information. If
    not provided, then all documents will be searched.
    """

    precise_responses: bool
    """Enable precise responses.

    Precise responses will have higher latency, but provide much more precise
    snippets. When `precise_responses` is set to `true`, the responses will average
    200 characters. If set to `false`, the responses will average 2000 characters.
    The default is `false`.
    """
