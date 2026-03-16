from __future__ import annotations

import json
from typing import Any, Dict, List

import httpx
import pytest
from respx import MockRouter  # type: ignore[import-not-found]

from zeroentropy import ZeroEntropy, AsyncZeroEntropy
from zeroentropy.lib.retrieval import (
    UnifiedDocumentResult,
    asearch_documents,
    search_documents,
)


base_url = "http://127.0.0.1:4010"


def _mock_top_documents_for_collections(respx_mock: Any, mapping: Dict[str, List[Dict[str, Any]]]) -> None:
    """Install a handler that returns different results per collection_name"""

    def handler(request: httpx.Request) -> httpx.Response:
        data: Dict[str, Any] = json.loads(request.content.decode("utf-8")) if request.content else {}
        collection_name = str(data.get("collection_name", ""))
        results = mapping.get(collection_name, [])
        return httpx.Response(200, json={"results": results})

    respx_mock.post("/queries/top-documents").mock(side_effect=handler)


class TestRetrieval:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_rrf_multi_collection(self, client: ZeroEntropy, respx_mock: Any) -> None:
        # Collection A ranks: doc1 (1), doc2 (2)
        # Collection B ranks: doc2 (1), doc3 (2)
        _mock_top_documents_for_collections(
            respx_mock,
            {
                "A": [
                    {"path": "doc1", "score": 0.9, "file_url": "u1", "metadata": {"a": "1"}},
                    {"path": "doc2", "score": 0.5, "file_url": "u2", "metadata": {"a": "2"}},
                ],
                "B": [
                    {"path": "doc2", "score": 0.95, "file_url": "u3", "metadata": {"b": "1"}},
                    {"path": "doc3", "score": 0.4, "file_url": "u4", "metadata": {"b": "2"}},
                ],
            },
        )

        results = search_documents(
            client,
            query="q",
            collections=["A", "B"],
            k=3,
            include_metadata=True,
            diversify=False,
        )

        assert [r.path for r in results] == ["doc2", "doc1", "doc3"]
        # best_collection for doc2 should be B (rank 1 there)
        assert results[0].best_collection == "B"
        assert isinstance(results[0], UnifiedDocumentResult)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_concat_strategy(self, client: ZeroEntropy, respx_mock: Any) -> None:
        _mock_top_documents_for_collections(
            respx_mock,
            {
                "TeamX": [
                    {"path": "x1", "score": 0.6, "file_url": "ux1", "metadata": {}},
                ],
                "TeamY": [
                    {"path": "y1", "score": 0.9, "file_url": "uy1", "metadata": {}},
                ],
            },
        )

        results = search_documents(
            client,
            query="hello",
            collections=["TeamX", "TeamY"],
            k=2,
            strategy="concat",
            diversify=False,
        )

        # Sorted by score descending after concatenation
        assert [r.path for r in results] == ["y1", "x1"]


class TestAsyncRetrieval:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.asyncio
    @pytest.mark.respx(base_url=base_url)
    async def test_async_rrf_multi_collection(self, async_client: AsyncZeroEntropy, respx_mock: Any) -> None:
        _mock_top_documents_for_collections(
            respx_mock,
            {
                "C1": [
                    {"path": "a", "score": 0.8, "file_url": "ua", "metadata": {}},
                    {"path": "b", "score": 0.6, "file_url": "ub", "metadata": {}},
                ],
                "C2": [
                    {"path": "b", "score": 0.95, "file_url": "ub2", "metadata": {}},
                ],
            },
        )

        results = await asearch_documents(
            async_client,
            query="q",
            collections=["C1", "C2"],
            k=2,
            diversify=True,
        )

        assert [r.path for r in results] == ["b", "a"]


