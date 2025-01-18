# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ParserParseDocumentParams"]


class ParserParseDocumentParams(TypedDict, total=False):
    base64_data: Required[str]
    """The document's raw data, as a base64-encoded string"""
