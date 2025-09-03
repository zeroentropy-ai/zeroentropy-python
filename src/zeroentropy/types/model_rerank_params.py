# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ModelRerankParams"]


class ModelRerankParams(TypedDict, total=False):
    documents: Required[SequenceNotStr[str]]
    """The list of documents to rerank. Each document is a string."""

    query: Required[str]
    """The query to rerank the documents by.

    Results will be in descending order of relevance.
    """

    model: str
    """The model ID to use for reranking. Options are: ["zerank-1-large"]"""

    top_n: Optional[int]
    """
    If provided, then only the top `n` documents will be returned in the results
    array.
    """
