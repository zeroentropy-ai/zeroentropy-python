from __future__ import annotations

from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple, Union
from typing_extensions import Literal

from .. import ZeroEntropy, AsyncZeroEntropy
from .._models import BaseModel
from ..types.query_top_documents_response import QueryTopDocumentsResponse


class SourceRank(BaseModel):
    collection_name: str
    rank: int
    score: float


class UnifiedDocumentResult(BaseModel):
    path: str
    fused_score: float
    best_collection: str
    file_url: Optional[str] = None
    metadata: Optional[Dict[str, Union[str, List[str]]]] = None
    source_ranks: List[SourceRank]


def _tokenize_for_similarity(text: str) -> List[str]:
    lowered = text.lower()
    tokens: List[str] = []
    token_chars: List[str] = []
    for ch in lowered:
        if ch.isalnum():
            token_chars.append(ch)
        else:
            if token_chars:
                tokens.append("".join(token_chars))
                token_chars = []
    if token_chars:
        tokens.append("".join(token_chars))
    # de-duplicate tokens while preserving order
    seen: set[str] = set()
    unique: List[str] = []
    for t in tokens:
        if t not in seen:
            unique.append(t)
            seen.add(t)
    return unique


def _jaccard(a_tokens: Sequence[str], b_tokens: Sequence[str]) -> float:
    if not a_tokens and not b_tokens:
        return 0.0
    a = set(a_tokens)
    b = set(b_tokens)
    inter = len(a.intersection(b))
    union = len(a.union(b))
    if union == 0:
        return 0.0
    return inter / union


def _mmr(
    candidates: List[UnifiedDocumentResult],
    *,
    k: int,
    lambda_: float,
) -> List[UnifiedDocumentResult]:
    if k <= 0 or not candidates:
        return []
    k = min(k, len(candidates))

    # precompute normalized scores and tokenization for a simple similarity based on path
    max_score = max(c.fused_score for c in candidates) or 1.0
    norm_scores = {c.path: (c.fused_score / max_score) for c in candidates}
    tokens = {c.path: _tokenize_for_similarity(c.path) for c in candidates}

    selected: List[UnifiedDocumentResult] = []
    remaining = candidates.copy()

    while remaining and len(selected) < k:
        best: Tuple[float, UnifiedDocumentResult] | None = None
        for cand in remaining:
            # diversity penalty: similarity to closest already selected item
            if selected:
                max_sim = max(
                    _jaccard(tokens[cand.path], tokens[sel.path]) for sel in selected
                )
            else:
                max_sim = 0.0

            score = lambda_ * norm_scores[cand.path] - (1.0 - lambda_) * max_sim
            if best is None or score > best[0]:
                best = (score, cand)

        assert best is not None
        _, chosen = best
        selected.append(chosen)
        remaining = [c for c in remaining if c.path != chosen.path]

    return selected


def _rrf(scores_by_collection: Dict[str, List[Tuple[str, float, Optional[str], Optional[Dict[str, Union[str, List[str]]]]]]]) -> List[UnifiedDocumentResult]:
    # Reciprocal Rank Fusion across collections.
    K = 60  # standard constant stabilizer

    # aggregate by path
    by_path: Dict[str, Dict[str, Any]] = {}
    for collection, ranked in scores_by_collection.items():
        for idx, (path, score, file_url, metadata) in enumerate(ranked, start=1):
            entry = by_path.setdefault(
                path,
                {
                    "fused": 0.0,
                    "best_collection": collection,
                    "best_rank": idx,
                    "file_url": file_url,
                    "metadata": metadata,
                    "sources": [],
                },
            )
            entry["fused"] += 1.0 / (K + idx)
            if idx < entry["best_rank"]:
                entry["best_rank"] = idx
                entry["best_collection"] = collection
                # prefer latest non-null file_url/metadata for best source
                if file_url is not None:
                    entry["file_url"] = file_url
                if metadata is not None:
                    entry["metadata"] = metadata
            entry["sources"].append(SourceRank(collection_name=collection, rank=idx, score=score))

    fused: List[UnifiedDocumentResult] = []
    for path, data in by_path.items():
        fused.append(
            UnifiedDocumentResult(
                path=path,
                fused_score=data["fused"],
                best_collection=data["best_collection"],
                file_url=data.get("file_url"),
                metadata=data.get("metadata"),
                source_ranks=data["sources"],
            )
        )

    fused.sort(key=lambda r: r.fused_score, reverse=True)
    return fused


def search_documents(
    client: ZeroEntropy,
    *,
    query: str,
    collections: Sequence[str],
    k: int = 20,
    filter: Optional[Mapping[str, object]] = None,
    include_metadata: bool = False,
    latency_mode: Literal["low", "high"] = "low",
    strategy: Literal["rrf", "concat"] = "rrf",
    diversify: bool = True,
    mmr_lambda: float = 0.5,
) -> List[UnifiedDocumentResult]:
    """High-level retrieval that queries multiple collections and fuses results.

    This function performs multi-collection search and merges results using
    Reciprocal Rank Fusion (RRF). Optionally applies a simple MMR diversification
    step based on path similarity to improve diversity.
    """

    if not collections:
        return []

    scores_by_collection: Dict[str, List[Tuple[str, float, Optional[str], Optional[Dict[str, Union[str, List[str]]]]]]] = {}
    for collection_name in collections:
        resp: QueryTopDocumentsResponse = client.queries.top_documents(
            collection_name=collection_name,
            k=k,
            query=query,
            filter=dict(filter) if filter is not None else None,
            include_metadata=include_metadata,
            latency_mode=latency_mode,
        )

        ranked: List[Tuple[str, float, Optional[str], Optional[Dict[str, Union[str, List[str]]]]]] = []
        for r in resp.results:
            ranked.append((r.path, r.score, getattr(r, "file_url", None), getattr(r, "metadata", None)))
        scores_by_collection[collection_name] = ranked

    if strategy == "concat":
        # simply concatenate, keeping per-collection order
        concatenated: List[UnifiedDocumentResult] = []
        for c in collections:
            ranked = scores_by_collection.get(c, [])
            for idx, (path, score, file_url, metadata) in enumerate(ranked, start=1):
                concatenated.append(
                    UnifiedDocumentResult(
                        path=path,
                        fused_score=score,
                        best_collection=c,
                        file_url=file_url,
                        metadata=metadata,
                        source_ranks=[SourceRank(collection_name=c, rank=idx, score=score)],
                    )
                )
        concatenated.sort(key=lambda r: r.fused_score, reverse=True)
        results = concatenated[:k]
    else:
        results = _rrf(scores_by_collection)
        results = results[: max(k * 2, k)]  # keep a bit more for MMR to work with

    if diversify and results:
        results = _mmr(results, k=k, lambda_=mmr_lambda)
    else:
        results = results[:k]

    return results


async def asearch_documents(
    client: AsyncZeroEntropy,
    *,
    query: str,
    collections: Sequence[str],
    k: int = 20,
    filter: Optional[Mapping[str, object]] = None,
    include_metadata: bool = False,
    latency_mode: Literal["low", "high"] = "low",
    strategy: Literal["rrf", "concat"] = "rrf",
    diversify: bool = True,
    mmr_lambda: float = 0.5,
) -> List[UnifiedDocumentResult]:
    if not collections:
        return []

    scores_by_collection: Dict[str, List[Tuple[str, float, Optional[str], Optional[Dict[str, Union[str, List[str]]]]]]] = {}
    for collection_name in collections:
        resp: QueryTopDocumentsResponse = await client.queries.top_documents(
            collection_name=collection_name,
            k=k,
            query=query,
            filter=dict(filter) if filter is not None else None,
            include_metadata=include_metadata,
            latency_mode=latency_mode,
        )

        ranked: List[Tuple[str, float, Optional[str], Optional[Dict[str, Union[str, List[str]]]]]] = []
        for r in resp.results:
            ranked.append((r.path, r.score, getattr(r, "file_url", None), getattr(r, "metadata", None)))
        scores_by_collection[collection_name] = ranked

    if strategy == "concat":
        concatenated: List[UnifiedDocumentResult] = []
        for c in collections:
            ranked = scores_by_collection.get(c, [])
            for idx, (path, score, file_url, metadata) in enumerate(ranked, start=1):
                concatenated.append(
                    UnifiedDocumentResult(
                        path=path,
                        fused_score=score,
                        best_collection=c,
                        file_url=file_url,
                        metadata=metadata,
                        source_ranks=[SourceRank(collection_name=c, rank=idx, score=score)],
                    )
                )
        concatenated.sort(key=lambda r: r.fused_score, reverse=True)
        results = concatenated[:k]
    else:
        results = _rrf(scores_by_collection)
        results = results[: max(k * 2, k)]

    if diversify and results:
        results = _mmr(results, k=k, lambda_=mmr_lambda)
    else:
        results = results[:k]

    return results


