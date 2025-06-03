# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["AdminCreateOrganizationResponse"]


class AdminCreateOrganizationResponse(BaseModel):
    api_key: str
    """The API Key for this organization."""

    organization_name: str
    """The name of the organization"""
