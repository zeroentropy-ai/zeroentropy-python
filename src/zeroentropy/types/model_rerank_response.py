# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ModelRerankResponse", "Result"]


class Result(BaseModel):
    index: int
    """
    The index of this document, relative to the original document array passed into
    the request.
    """

    relevance_score: float
    """The relevance score between this document and the query.

    This number will range between 0.0 and 1.0. This score is dependent on only the
    query and the scored document; other documents do not affect this score. This
    value is intended to be deterministic, but it may vary slightly due to floating
    point error.
    """


class ModelRerankResponse(BaseModel):
    actual_latency_mode: Literal["fast", "slow"]
    """The type of inference actually used.

    If `auto` is requested, then `fast` will be used by default, with `slow` as a
    fallback if your ratelimit is exceeded. Else, this field will be identical to
    the requested latency mode.
    """

    e2e_latency: float
    """
    The total time, in seconds, between rerank request received and rerank response
    returned. Client latency should equal `e2e_latency` + your ping to ZeroEntropy's
    API.
    """

    inference_latency: float
    """The time, in seconds, to actually inference the request.

    If this is significantly lower than `e2e_latency`, this is likely due to
    ratelimiting. Please request a higher ratelimit at
    [founders@zeroentropy.dev](mailto:founders@zeroentropy.dev) or message us on
    [Discord](https://go.zeroentropy.dev/discord) or
    [Slack](https://go.zeroentropy.dev/slack)!
    """

    results: List[Result]
    """The results, ordered by descending order of relevance to the query."""

    total_bytes: int
    """The total number of bytes in the request. This is used for ratelimiting."""

    total_tokens: int
    """The total number of tokens in the request. This is used for billing."""
