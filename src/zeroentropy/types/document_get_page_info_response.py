# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DocumentGetPageInfoResponse", "Page"]


class Page(BaseModel):
    id: str

    collection_name: str
    """The name of the collection."""

    image_url: Optional[str] = None
    """A URL to an image of the page.

    This field will only be provided if the document has finished parsing, and if it
    is a filetype that is capable of producing images (e.g. PDF, DOCX, PPT, etc). In
    all other cases, this field will be `null`.

    NOTE: If a `/documents/update-document` call returned a new document id, then
    this url will be invalidated and must be retrieved again.
    """

    page_index: int
    """The specific page index of this page.

    Pages are 0-indexed, so that the 1st page of a PDF is of page index 0.
    """

    path: str
    """The filepath of the document associated with this page."""

    content: Optional[str] = None
    """The content of the page.

    This field will only be provided if `include_content` was set to `true`, and the
    document has finished parsing. Otherwise, this field will be set to `null`.
    """


class DocumentGetPageInfoResponse(BaseModel):
    page: Page
