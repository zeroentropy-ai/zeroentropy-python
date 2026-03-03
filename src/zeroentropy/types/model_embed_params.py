# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ModelEmbedParams"]


class ModelEmbedParams(TypedDict, total=False):
    input: Required[Union[str, SequenceNotStr[str]]]
    """The string, or list of strings, to embed."""

    input_type: Required[Literal["query", "document"]]
    """The input type. For retrieval tasks, either `query` or `document`."""

    model: Required[str]
    """The model ID to use for embedding. Options are: ["zembed-1"]"""

    dimensions: Optional[int]
    """The output dimensionality of the embedding model.

    For `zembed-1`, the available options are: [2560, 1280, 640, 320, 160, 80, 40].
    """

    encoding_format: Literal["float", "base64"]
    """The output format of the embedding.

    If `float`, an array of floats will be returned for each embeddings. If
    `base64`, a f32 little endian byte array will be returned, encoded as a base64
    string. `base64` is significantly more efficient than `float`. The default is
    `float`.
    """

    latency: Optional[Literal["fast", "slow"]]
    """Whether the call will be inferenced "fast" or "slow".

    RateLimits for slow API calls are orders of magnitude higher, but you can expect
    2-20 second latency. Fast inferences are guaranteed subsecond, but rate limits
    are lower. If not specified, first a "fast" call will be attempted, but if you
    have exceeded your fast rate limit, then a slow call will be executed. If
    explicitly set to "fast", then 429 will be returned if it cannot be executed
    fast.
    """
