# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncGetDocumentInfoListCursor", "AsyncGetDocumentInfoListCursor"]

_T = TypeVar("_T")


@runtime_checkable
class GetDocumentInfoListCursorItem(Protocol):
    path: str


class SyncGetDocumentInfoListCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    documents: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        documents = self.documents
        if not documents:
            return []
        return documents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        documents = self.documents
        if not documents:
            return None

        item = cast(Any, documents[-1])
        if not isinstance(item, GetDocumentInfoListCursorItem) or item.path is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(json={"path_gt": item.path})


class AsyncGetDocumentInfoListCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    documents: List[_T]

    @override
    def _get_page_items(self) -> List[_T]:
        documents = self.documents
        if not documents:
            return []
        return documents

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        documents = self.documents
        if not documents:
            return None

        item = cast(Any, documents[-1])
        if not isinstance(item, GetDocumentInfoListCursorItem) or item.path is None:  # pyright: ignore[reportUnnecessaryComparison]
            # TODO emit warning log
            return None

        return PageInfo(json={"path_gt": item.path})
