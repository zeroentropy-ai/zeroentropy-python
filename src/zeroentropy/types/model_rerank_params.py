# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ModelRerankParams"]


class ModelRerankParams(TypedDict, total=False):
    documents: Required[SequenceNotStr[str]]
    """The list of documents to rerank. Each document is a string."""

    model: Required[str]
    """The model ID to use for reranking.

    Options are: ["zerank-2", "zerank-1", "zerank-1-small"]
    """

    query: Required[str]
    """The query to rerank the documents by."""

    latency: Optional[Literal["fast", "slow"]]
    """Whether the call will be inferenced "fast" or "slow".

    RateLimits for slow API calls are orders of magnitude higher, but you can
    expect >10 second latency. Fast inferences are guaranteed subsecond, but rate
    limits are lower. If not specified, first a "fast" call will be attempted, but
    if you have exceeded your fast rate limit, then a slow call will be executed. If
    explicitly set to "fast", then 429 will be returned if it cannot be executed
    fast.
    """

    top_n: Optional[int]
    """
    If provided, then only the top `n` documents will be returned in the results
    array. Otherwise, `n` will be the length of the provided documents array.
    """
