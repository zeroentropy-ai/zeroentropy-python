# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["DocumentUpdateResponse"]


class DocumentUpdateResponse(BaseModel):
    new_id: str

    previous_id: str
