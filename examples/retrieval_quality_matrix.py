#!/usr/bin/env python3
"""Compare ZeroEntropy retrieval settings and emit replayable JSONL results.

This example runs the same query against a small matrix of retrieval settings so
you can inspect quality/latency tradeoffs before choosing defaults for an agent
or RAG workflow.

Usage:
    ZEROENTROPY_API_KEY=... python examples/retrieval_quality_matrix.py \
        --collection example_collection \
        --query "refund policy for enterprise customers" \
        --output traces/refund-policy.jsonl
"""

from __future__ import annotations

import argparse
import json
import time
from collections.abc import Iterable
from pathlib import Path
from typing import Any

from zeroentropy import ZeroEntropy


def compact_model(value: Any) -> dict[str, Any]:
    """Return a JSON-serializable dict for Pydantic models or plain objects."""
    if hasattr(value, "model_dump"):
        return value.model_dump(mode="json")
    if hasattr(value, "dict"):
        return value.dict()
    return dict(value)


def get_nested(item: dict[str, Any], *keys: str) -> Any:
    current: Any = item
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def summarize_documents(response: Any) -> list[dict[str, Any]]:
    payload = compact_model(response)
    documents = payload.get("documents") or payload.get("results") or []
    summary = []

    for rank, document in enumerate(documents, start=1):
        summary.append(
            {
                "rank": rank,
                "id": document.get("id") or document.get("document_id"),
                "path": document.get("path"),
                "score": document.get("score"),
                "metadata": document.get("metadata"),
            }
        )

    return summary


def summarize_snippets(response: Any) -> list[dict[str, Any]]:
    payload = compact_model(response)
    snippets = payload.get("snippets") or payload.get("results") or []
    summary = []

    for rank, snippet in enumerate(snippets, start=1):
        summary.append(
            {
                "rank": rank,
                "document_id": snippet.get("document_id")
                or get_nested(snippet, "document", "id"),
                "score": snippet.get("score"),
                "text_preview": (snippet.get("text") or snippet.get("content") or "")[
                    :240
                ],
            }
        )

    return summary


def iter_variants(rerankers: Iterable[str | None]) -> Iterable[dict[str, Any]]:
    for latency_mode in ("low", "high"):
        for reranker in rerankers:
            yield {
                "name": f"top_documents:{latency_mode}:reranker={reranker or 'none'}",
                "endpoint": "top_documents",
                "params": {
                    "latency_mode": latency_mode,
                    "reranker": reranker,
                },
            }

    for precise_responses in (False, True):
        for reranker in rerankers:
            yield {
                "name": f"top_snippets:precise={precise_responses}:reranker={reranker or 'none'}",
                "endpoint": "top_snippets",
                "params": {
                    "precise_responses": precise_responses,
                    "reranker": reranker,
                },
            }


def write_jsonl(path: Path, payload: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as file:
        file.write(json.dumps(payload, ensure_ascii=False) + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Compare ZeroEntropy retrieval quality/latency settings."
    )
    parser.add_argument("--collection", required=True, help="Collection name")
    parser.add_argument("--query", required=True, help="Search query")
    parser.add_argument("--k", type=int, default=10, help="Number of results")
    parser.add_argument(
        "--reranker",
        action="append",
        default=[],
        help="Reranker id to evaluate. Pass multiple times for a larger matrix.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("retrieval-quality-results.jsonl"),
        help="JSONL output path",
    )
    args = parser.parse_args()

    client = ZeroEntropy()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text("", encoding="utf-8")

    rerankers: list[str | None] = [None, *args.reranker]
    write_jsonl(
        args.output,
        {
            "type": "metadata",
            "collection": args.collection,
            "query": args.query,
            "k": args.k,
            "rerankers": rerankers,
        },
    )

    for variant in iter_variants(rerankers):
        started = time.perf_counter()
        base_params = {
            "collection_name": args.collection,
            "query": args.query,
            "k": args.k,
        }
        call_params = {
            **base_params,
            **{
                key: value
                for key, value in variant["params"].items()
                if value is not None
            },
        }

        if variant["endpoint"] == "top_documents":
            response = client.queries.top_documents(**call_params)
            results = summarize_documents(response)
        else:
            response = client.queries.top_snippets(**call_params)
            results = summarize_snippets(response)

        elapsed_ms = round((time.perf_counter() - started) * 1000)
        write_jsonl(
            args.output,
            {
                "type": "variant",
                "name": variant["name"],
                "endpoint": variant["endpoint"],
                "params": variant["params"],
                "elapsed_ms": elapsed_ms,
                "results": results,
            },
        )

        print(f"{variant['name']}: {len(results)} results in {elapsed_ms}ms")

    print(f"wrote {args.output}")


if __name__ == "__main__":
    main()
