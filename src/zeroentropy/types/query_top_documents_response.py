# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["QueryTopDocumentsResponse", "Result"]


class Result(BaseModel):
    metadata: Optional[Dict[str, Union[str, List[str]]]] = None
    """The metadata for that document.

    Will be `None` if `include_metadata` is `False`.
    """

    path: str
    """The path of the document."""

    score: float
    """The relevancy score assigned to this document."""


class QueryTopDocumentsResponse(BaseModel):
    results: List[Result]
