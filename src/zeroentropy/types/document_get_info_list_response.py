# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentGetInfoListResponse"]


class DocumentGetInfoListResponse(BaseModel):
    id: str

    collection_name: str

    created_at: datetime

    file_url: str
    """
    A URL to the document data, which can be used to download the raw document
    content or to display the document in frontend applications.

    NOTE: If a `/documents/update-document` call returned a new document id, then
    this url will be invalidated and must be retrieved again.
    """

    index_status: Literal[
        "not_parsed", "parsing", "not_indexed", "indexing", "indexed", "parsing_failed", "indexing_failed"
    ]

    metadata: Dict[str, Union[str, List[str]]]

    num_pages: Optional[int] = None
    """The number of pages in this document.

    This will be `null` if the document is parsing or failed to parse. It can also
    be `null` if the document is a filetype that does not support pages.
    """

    path: str

    size: int
    """The total size of the raw document data, in bytes."""
