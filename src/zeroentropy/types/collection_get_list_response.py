# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["CollectionGetListResponse"]


class CollectionGetListResponse(BaseModel):
    collection_names: List[str]
    """The names of the matched collections."""
