# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["ModelParseDocumentResponse"]


class ModelParseDocumentResponse(BaseModel):
    pages: List[str]
    """The parsed pages. Each string will contain the full contents of a page."""
