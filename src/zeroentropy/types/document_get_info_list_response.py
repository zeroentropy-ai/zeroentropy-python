# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["DocumentGetInfoListResponse"]


class DocumentGetInfoListResponse(BaseModel):
    id: str

    collection_name: str

    index_status: Literal["parsing_failed", "not_parsed", "not_indexed", "indexing", "indexed"]

    metadata: Dict[str, Union[str, List[str]]]

    num_pages: Optional[int] = None
    """The number of pages in this document.

    This will be `null` if the document is parsing or failed to parse. It can also
    be `null` if the document is a filetype that does not support pages.
    """

    path: str
