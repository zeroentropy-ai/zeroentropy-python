# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["QueryTopPagesResponse", "Result"]


class Result(BaseModel):
    content: Optional[str] = None
    """The contents of this page.

    This property will be null when `include_content` is `false`, and a string when
    `include_content` is `true`.
    """

    page_index: int
    """The index of this page in the document.

    This field is 0-indexed. So, the 1st page has index 0, and the 2nd page has
    index 1.
    """

    path: str
    """The path of the document that this page comes from."""

    score: float
    """The relevancy score assigned to this page."""


class QueryTopPagesResponse(BaseModel):
    results: List[Result]
