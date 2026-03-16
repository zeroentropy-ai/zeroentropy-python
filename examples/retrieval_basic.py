#!/usr/bin/env -S rye run python
import os
from zeroentropy import ZeroEntropy
from zeroentropy.lib.retrieval import search_documents


def main() -> None:
    client = ZeroEntropy(api_key=os.environ.get("ZEROENTROPY_API_KEY"))
    results = search_documents(
        client,
        query="how to reset password",
        collections=["product_docs", "engineering_notes"],
        k=5,
        include_metadata=True,
        diversify=True,
    )
    for r in results:
        print(f"{r.fused_score:.4f}\t{r.best_collection}\t{r.path}")


if __name__ == "__main__":
    main()


