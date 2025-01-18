# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["QueryTopSnippetsResponse", "Result"]


class Result(BaseModel):
    content: Optional[str] = None
    """If requested, this contains the full string content of this snippet."""

    end_index: int
    """The end index of this snippet."""

    page_span: List[int]
    """The range of page indices spanned by this snippet, as a 2-tuple of integers.

    Inclusive on the first page_index and exclusive on the second page_index.
    """

    path: str
    """The path of the document that this snippet comes from."""

    score: float
    """The relevancy score assigned to this snippet."""

    start_index: int
    """The start index of this snippet."""


class QueryTopSnippetsResponse(BaseModel):
    results: List[Result]
