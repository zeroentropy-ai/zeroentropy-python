# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AdminCreateOrganizationParams"]


class AdminCreateOrganizationParams(TypedDict, total=False):
    organization_name: Required[str]
    """The orgniazation name to create. Must be unique."""
