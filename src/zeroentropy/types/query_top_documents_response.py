# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["QueryTopDocumentsResponse", "Result"]


class Result(BaseModel):
    file_url: str
    """
    A URL to the document data, which can be used to download the raw document
    content or to display the document in frontend applications.

    NOTE: If a `/documents/update-document` call returned a new document id, then
    this url will be invalidated and must be retrieved again.
    """

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
