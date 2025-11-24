# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["StatusGetStatusResponse"]


class StatusGetStatusResponse(BaseModel):
    num_documents: int
    """The total number of documents, regardless of their status.

    It is guaranteed that the sum of all of the other fields, is this number.
    """

    num_failed_documents: int
    """The number of failed documents.

    Failures can occur during either parsing, or indexing. It can occur if the file
    is malformed or incomplete. If you believe that the file is formatted correctly,
    please contact us at `founders@zeroentropy.dev` to assist.
    """

    num_indexed_bytes: int
    """The total number of bytes used by documents that are currently indexed.

    Measured as UTF-8 bytes. For PDF/DOCX/PPT/etc, this is of the OCR'ed text.
    """

    num_indexed_documents: int
    """The number of documents that are currently indexed."""

    num_indexing_documents: int
    """The number of documents being indexed.

    Indexing occurs only after the document has finished parsing.
    """

    num_parsing_documents: int
    """The number of documents that are being parsed.

    This refers files of the type PDF, DOCX, PPT, etc, whose images are being
    processed, or are waiting to be processed, by our OCR system.
    """
