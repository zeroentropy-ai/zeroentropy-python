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
    CollectionListResponse,
    CollectionAddCollectionResponse,
    CollectionDeleteCollectionResponse,
)
```

Methods:

- <code title="post /collections/get-collection-list">client.collections.<a href="./src/zeroentropy/resources/collections.py">list</a>() -> <a href="./src/zeroentropy/types/collection_list_response.py">CollectionListResponse</a></code>
- <code title="post /collections/add-collection">client.collections.<a href="./src/zeroentropy/resources/collections.py">add_collection</a>(\*\*<a href="src/zeroentropy/types/collection_add_collection_params.py">params</a>) -> <a href="./src/zeroentropy/types/collection_add_collection_response.py">CollectionAddCollectionResponse</a></code>
- <code title="post /collections/delete-collection">client.collections.<a href="./src/zeroentropy/resources/collections.py">delete_collection</a>(\*\*<a href="src/zeroentropy/types/collection_delete_collection_params.py">params</a>) -> <a href="./src/zeroentropy/types/collection_delete_collection_response.py">CollectionDeleteCollectionResponse</a></code>

# Documents

Types:

```python
from zeroentropy.types import (
    DocumentAddDocumentResponse,
    DocumentDeleteDocumentResponse,
    DocumentGetInfoResponse,
    DocumentGetPageInfoResponse,
    DocumentListInfoResponse,
)
```

Methods:

- <code title="post /documents/add-document">client.documents.<a href="./src/zeroentropy/resources/documents.py">add_document</a>(\*\*<a href="src/zeroentropy/types/document_add_document_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_add_document_response.py">DocumentAddDocumentResponse</a></code>
- <code title="post /documents/delete-document">client.documents.<a href="./src/zeroentropy/resources/documents.py">delete_document</a>(\*\*<a href="src/zeroentropy/types/document_delete_document_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_delete_document_response.py">DocumentDeleteDocumentResponse</a></code>
- <code title="post /documents/get-document-info">client.documents.<a href="./src/zeroentropy/resources/documents.py">get_info</a>(\*\*<a href="src/zeroentropy/types/document_get_info_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_get_info_response.py">DocumentGetInfoResponse</a></code>
- <code title="post /documents/get-page-info">client.documents.<a href="./src/zeroentropy/resources/documents.py">get_page_info</a>(\*\*<a href="src/zeroentropy/types/document_get_page_info_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_get_page_info_response.py">DocumentGetPageInfoResponse</a></code>
- <code title="post /documents/get-document-info-list">client.documents.<a href="./src/zeroentropy/resources/documents.py">list_info</a>(\*\*<a href="src/zeroentropy/types/document_list_info_params.py">params</a>) -> <a href="./src/zeroentropy/types/document_list_info_response.py">DocumentListInfoResponse</a></code>

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
from zeroentropy.types import ParserParseResponse
```

Methods:

- <code title="post /parsers/parse-document">client.parsers.<a href="./src/zeroentropy/resources/parsers.py">parse</a>(\*\*<a href="src/zeroentropy/types/parser_parse_params.py">params</a>) -> <a href="./src/zeroentropy/types/parser_parse_response.py">ParserParseResponse</a></code>

# Models

Types:

```python
from zeroentropy.types import StrJson
```
