# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["CollectionAddResponse"]


class CollectionAddResponse(BaseModel):
    message: Optional[str] = None
    """This string will always be "Success!". This may change in the future."""
