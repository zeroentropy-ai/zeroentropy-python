# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["DocumentGetPageInfoResponse", "Page"]


class Page(BaseModel):
    id: str

    collection_name: str
    """The name of the collection."""

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

    image_base64_data: Optional[str] = None
    """An image of the page.

    This will be a base64-encoded string. Currently, this data is guaranteed to be a
    JPEG-encoded image. This field will only be provided if `include_image` was set
    to `true`, and the document has finished parsing. Also, the document must be a
    datatype that supports images (PDF, DOCX, PPT, but not .txt). In all other
    cases, this field will be `null`.
    """


class DocumentGetPageInfoResponse(BaseModel):
    page: Page
