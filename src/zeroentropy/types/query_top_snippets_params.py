# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

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

    filter: Optional[Dict[str, object]]
    """The query filter to apply.

    Please read [Metadata Filtering](/metadata-filtering) for more information. If
    not provided, then all documents will be searched.
    """

    include_document_metadata: bool
    """
    If true, the `document_results` returns will additionally contain document
    metadata. This is false by default, as returning metadata can add overhead if
    the amount of data to return is large.
    """

    latency_mode: Literal["low"]
    """Note that for Top K Snippets, only latency_mode "low" is available.

    This option selects between our latency modes. The higher latency mode takes
    longer, but can allow for more accurate responses. If desired, test both to
    customize your search experience for your particular use-case, or use the
    default of "low" and only swap if you need an additional improvement in search
    result quality.
    """

    precise_responses: bool
    """Enable precise responses.

    Precise responses will have higher latency, but provide much more precise
    snippets. When `precise_responses` is set to `true`, the responses will average
    200 characters. If set to `false`, the responses will average 2000 characters.
    The default is `false`.
    """
