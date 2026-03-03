# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union

from .._models import BaseModel

__all__ = ["ModelEmbedResponse", "Result", "Usage"]


class Result(BaseModel):
    embedding: Union[List[float], str]
    """The embedding of the input text, as an array of floats.

    If `base64` format is requested, the response will be an fp32 little endian byte
    array, encoded as a base64 string.
    """


class Usage(BaseModel):
    """Statistics regarding the tokens used by the request."""

    total_bytes: int
    """The total number of bytes in the request. This is used for ratelimiting."""

    total_tokens: int
    """The total number of tokens in the request. This is used for billing."""


class ModelEmbedResponse(BaseModel):
    results: List[Result]
    """The list of embedding results."""

    usage: Usage
    """Statistics regarding the tokens used by the request."""
