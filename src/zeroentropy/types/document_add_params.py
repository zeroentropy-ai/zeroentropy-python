# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict

__all__ = [
    "DocumentAddParams",
    "Content",
    "ContentAPITextDocument",
    "ContentAPITextPagesDocument",
    "ContentAPIBinaryDocument",
]


class DocumentAddParams(TypedDict, total=False):
    collection_name: Required[str]
    """The name of the collection to be used for this request.

    A `404 Not Found` status code will be returned if this collection name does not
    exist.
    """

    content: Required[Content]
    """The content of the document.

    There are three possible JSON types that can be passed into this parameter:
    `APITextDocument`, `APITextPagesDocument`, `APIBinaryDocument`. The `type` field
    is how ZeroEntropy will know which document object you have passed in.
    """

    path: Required[str]
    """The filepath of the document that you are adding.

    A `409 Conflict` status code will be returned if this path already exists,
    unless `overwrite` is set to `true`.
    """

    metadata: Dict[str, Union[str, List[str]]]
    """
    This is a metadata JSON object that can be used to assign various metadata
    attributes to your document. The provided object must match the type
    `dict[str, str | list[str]]`. Please read
    [Metadata Filtering](/metadata-filtering) for more details. By default, the
    metadata will be set to `{}`.

    NOTE: The UTF-8-encoded JSON string must be less than 65536 bytes (Whitespace
    does not count). This limit can be increased upon request.
    """

    overwrite: bool
    """
    Setting this property to true will put this endpoint in "upsert" mode: If the
    document already exists, this action will atomically replace it.
    """


class ContentAPITextDocument(TypedDict, total=False):
    text: Required[str]
    """The content of this document, as a text string"""

    type: Required[Literal["text"]]
    """This field must be `text`"""


class ContentAPITextPagesDocument(TypedDict, total=False):
    pages: Required[List[str]]
    """The content of this document, as an array of strings.

    Each string will be the content of a full page, and can be retrieved using the
    Top Pages endpoint. Pages are 0-indexed, so that the first string has index 0,
    the second string has index 1.
    """

    type: Required[Literal["text-pages"]]
    """This field must be `text-pages`"""


class ContentAPIBinaryDocument(TypedDict, total=False):
    base64_data: Required[str]
    """The file's raw data, as a base64-encoded string"""

    type: Required[Literal["auto"]]
    """
    When this is set to `auto`, then the file extension and binary data will be used
    to deduce a filetype automatically. Currently, only `auto` is supported.
    """


Content: TypeAlias = Union[ContentAPITextDocument, ContentAPITextPagesDocument, ContentAPIBinaryDocument]
