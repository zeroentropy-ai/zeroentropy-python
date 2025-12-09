# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional

from .._models import BaseModel

__all__ = ["QueryTopSnippetsResponse", "DocumentResult", "Result"]


class DocumentResult(BaseModel):
    file_url: str
    """
    A URL to the document data, which can be used to download the raw document
    content or to display the document in frontend applications.

    NOTE: If a `/documents/update-document` call returned a new document id, then
    this url will be invalidated and must be retrieved again.
    """

    metadata: Optional[Dict[str, Union[str, List[str]]]] = None
    """The metadata for that document.

    Will be `None` if `include_metadata` is `False`.
    """

    path: str
    """The path of the document."""

    score: float
    """The relevancy score assigned to this document."""


class Result(BaseModel):
    """This is a Snippet.

    A snippet refers to a particular document path, and index range. Note that all documents, regardless of filetype, are converted into `UTF-8`-encoded strings. The `start_index` and `end_index` refer to the range of characters in that string, that have been matched by this snippet.
    """

    content: str
    """The full string content of this snippet."""

    end_index: int
    """The end index of this snippet."""

    page_span: List[int]
    """The range of page indices spanned by this snippet, as a 2-tuple of integers.

    Inclusive on the first page_index and exclusive on the second page_index.
    """

    path: str
    """The path of the document that this snippet comes from."""

    score: float
    """The relevancy score assigned to this snippet."""

    start_index: int
    """The start index of this snippet."""


class QueryTopSnippetsResponse(BaseModel):
    document_results: List[DocumentResult]
    """The array of associated document information.

    Note how each snippet has an associated document path. After deduplicating the
    document paths, this array will contain document info for each document path
    that is referenced by at least one snippet result.
    """

    results: List[Result]
    """The array of snippets returned by this endpoint.

    Each snippet result refers to a particular document path, and index range. Note
    that all documents, regardless of filetype, are converted into `UTF-8`-encoded
    strings. The `start_index` and `end_index` of a snippet refer to the range of
    characters in that string, that have been matched by this snippet.
    """
