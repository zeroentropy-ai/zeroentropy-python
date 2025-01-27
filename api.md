# Admin

Types:

```python
from zeroentropy.types import AdminCreateOrganizationResponse
```

Methods:

- <code title="post /admin/create-organization">client.admin.<a href="./src/zeroentropy/resources/admin.py">create_organization</a>(\*\*<a href="src/zeroentropy/types/admin_create_organization_params.py">params</a>) -> <a href="./src/zeroentropy/types/admin_create_organization_response.py">AdminCreateOrganizationResponse</a></code>

# Status

Types:

```python
from zeroentropy.types import StatusGetStatusResponse
```

Methods:

- <code title="post /status/get-status">client.status.<a href="./src/zeroentropy/resources/status.py">get_status</a>(\*\*<a href="src/zeroentropy/types/status_get_status_params.py">params</a>) -> <a href="./src/zeroentropy/types/status_get_status_response.py">StatusGetStatusResponse</a></code>

# Collections

Types:

```python
from zeroentropy.types import (
    CollectionDeleteResponse,
    CollectionAddResponse,
    CollectionGetListResponse,
)
```

Methods:

- <code title="post /collections/delete-collection">client.collections.<a href="./src/zeroentropy/resources/collections.py">delete</a>(\*\*<a href="src/zeroentropy/types/collection_delete_params.py">params</a>) -> <a href="./src/zeroentropy/types/collection_delete_response.py">CollectionDeleteResponse</a></code>
- <code title="post /collections/add-collection">client.collections.<a href="./src/zeroentropy/resources/collections.py">add</a>(\*\*<a href="src/zeroentropy/types/collection_add_params.py">params</a>) -> <a href="./src/zeroentropy/types/collection_add_response.py">CollectionAddResponse</a></code>
- <code title="post /collections/get-collection-list">client.collections.<a href="./src/zeroentropy/resources/collections.py">get_list</a>() -> <a href="./src/zeroentropy/types/collection_get_list_response.py">CollectionGetListResponse</a></code>

# Documents

Types:

```python
from zeroentropy.types import (
    DocumentUpdateResponse,
    DocumentDeleteResponse,
    DocumentAddResponse,
    DocumentGetInfoResponse,
    DocumentGetInfoListResponse,
    DocumentGetPageInfoResponse,
)
```

Methods:

- <code title="post /documents/update-document">client.documents.<a href="./src/zeroentropy/resources/documents.py">update</a>(\*\*<a href="src/zeroentropy/types/document_update_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_update_response.py">DocumentUpdateResponse</a></code>
- <code title="post /documents/delete-document">client.documents.<a href="./src/zeroentropy/resources/documents.py">delete</a>(\*\*<a href="src/zeroentropy/types/document_delete_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_delete_response.py">DocumentDeleteResponse</a></code>
- <code title="post /documents/add-document">client.documents.<a href="./src/zeroentropy/resources/documents.py">add</a>(\*\*<a href="src/zeroentropy/types/document_add_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_add_response.py">DocumentAddResponse</a></code>
- <code title="post /documents/get-document-info">client.documents.<a href="./src/zeroentropy/resources/documents.py">get_info</a>(\*\*<a href="src/zeroentropy/types/document_get_info_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_get_info_response.py">DocumentGetInfoResponse</a></code>
- <code title="post /documents/get-document-info-list">client.documents.<a href="./src/zeroentropy/resources/documents.py">get_info_list</a>(\*\*<a href="src/zeroentropy/types/document_get_info_list_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_get_info_list_response.py">SyncGetDocumentInfoListCursor[DocumentGetInfoListResponse]</a></code>
- <code title="post /documents/get-page-info">client.documents.<a href="./src/zeroentropy/resources/documents.py">get_page_info</a>(\*\*<a href="src/zeroentropy/types/document_get_page_info_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_get_page_info_response.py">DocumentGetPageInfoResponse</a></code>

# Queries

Types:

```python
from zeroentropy.types import (
    QueryTopDocumentsResponse,
    QueryTopPagesResponse,
    QueryTopSnippetsResponse,
)
```

Methods:

- <code title="post /queries/top-documents">client.queries.<a href="./src/zeroentropy/resources/queries.py">top_documents</a>(\*\*<a href="src/zeroentropy/types/query_top_documents_params.py">params</a>) -> <a href="./src/zeroentropy/types/query_top_documents_response.py">QueryTopDocumentsResponse</a></code>
- <code title="post /queries/top-pages">client.queries.<a href="./src/zeroentropy/resources/queries.py">top_pages</a>(\*\*<a href="src/zeroentropy/types/query_top_pages_params.py">params</a>) -> <a href="./src/zeroentropy/types/query_top_pages_response.py">QueryTopPagesResponse</a></code>
- <code title="post /queries/top-snippets">client.queries.<a href="./src/zeroentropy/resources/queries.py">top_snippets</a>(\*\*<a href="src/zeroentropy/types/query_top_snippets_params.py">params</a>) -> <a href="./src/zeroentropy/types/query_top_snippets_response.py">QueryTopSnippetsResponse</a></code>

# Parsers

Types:

```python
from zeroentropy.types import ParserParseDocumentResponse
```

Methods:

- <code title="post /parsers/parse-document">client.parsers.<a href="./src/zeroentropy/resources/parsers.py">parse_document</a>(\*\*<a href="src/zeroentropy/types/parser_parse_document_params.py">params</a>) -> <a href="./src/zeroentropy/types/parser_parse_document_response.py">ParserParseDocumentResponse</a></code>
