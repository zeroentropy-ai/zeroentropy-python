# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

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
    value is deterministic, but may vary slightly due to floating point error.
    """


class ModelRerankResponse(BaseModel):
    results: List[Result]
    """The results, ordered by descending order of relevance to the query."""
