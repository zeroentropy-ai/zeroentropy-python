# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["QueryTopDocumentsParams"]


class QueryTopDocumentsParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection."""

    k: Required[int]
    """The number of documents to return.

    If there are not enough documents matching your filters, then fewer may be
    returned. This number must be between 1 and 2048, inclusive.
    """

    query: Required[Optional[str]]
    """The natural language query to search with.

    This cannot exceed 4096 UTF-8 bytes. If `null`, then the sort will be undefined.
    The purpose of `null` is to do faster metadata filter searches without care for
    relevancy. Cost per query is unchanged.
    """

    filter: Optional[Dict[str, object]]
    """The query filter to apply.

    Please read [Metadata Filtering](/metadata-filtering) for more information. If
    not provided, then all documents will be searched.
    """

    include_metadata: bool
    """Whether or not to include the metadata in the top documents response.

    If not provided, then the default will be `False`.
    """

    latency_mode: Literal["low", "high"]
    """This option selects between our two latency modes.

    The higher latency mode takes longer, but can allow for more accurate responses.
    If desired, test both to customize your search experience for your particular
    use-case, or use the default of "low" and only swap if you need an additional
    improvement in search result quality.
    """

    reranker: Optional[str]
    """The reranker to use after initial retrieval.

    The default is `null`. You can find available model ids along with more
    information at [/models/rerank](/api-reference/models/rerank).
    """
