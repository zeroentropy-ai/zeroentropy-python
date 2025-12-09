# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["QueryTopPagesResponse", "Result"]


class Result(BaseModel):
    """A Page's metadata."""

    content: Optional[str] = None
    """The contents of this page.

    This property will be null when `include_content` is `false`, and a string when
    `include_content` is `true`.
    """

    image_url: Optional[str] = None
    """A URL to an image of the page.

    This field will only be provided if the document has finished parsing, and if it
    is a filetype that is capable of producing images (e.g. PDF, DOCX, PPT, etc). In
    all other cases, this field will be `null`.

    NOTE: If a `/documents/update-document` call returned a new document id, then
    this url will be invalidated and must be retrieved again.
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
