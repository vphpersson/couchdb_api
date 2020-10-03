from typing import Optional, List, Dict, Union, Mapping, Any, Coroutine
from httpx import AsyncClient, Response

JSON = Union[str, int, float, bool, None, Mapping[str, 'JSON'], List['JSON']]


def get_db_doc(
    client: AsyncClient,
    db: str,
    docid: str,
    params: Optional[Dict[str, str]] = None
) -> Coroutine[Any, Any, Response]:
    """
    Retrieve from the CouchDB database with the name `db` a document having the document ID `docid`.

    https://docs.couchdb.org/en/stable/api/document/common.html#get--db-docid

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CouchDB database from which to retrieve the document.
    :param docid: The document ID of the document to retrieve.
    :param params: Optional query parameter options.
    :return: The response of the HTTP request.
    """

    return client.get(f'/{db}/{docid}', params=params)


def put_db_doc(
    client: AsyncClient,
    db: str,
    docid: str,
    body: JSON,
    params: Optional[Dict[str, str]] = None
) -> Coroutine[Any, Any, Response]:
    """
    Add a new document to the CouchDB database with the name `db`.

    https://docs.couchdb.org/en/stable/api/document/common.html#put--db-docid

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CouchDB database to which to add the document.
    :param docid: The document ID of the new document.
    :param body: JSON content corresponding to the new document.
    :param params: Optional query parameter options.
    :return: The response of the HTTP request.
    """

    return client.put(url=f'/{db}/{docid}', json=body, params=params)


def delete_db_doc(
    client: AsyncClient,
    db: str,
    docid: str,
    params: Optional[Dict[str, str]] = None
) -> Coroutine[Any, Any, Response]:
    """
    Mark a document as deleted.

    https://docs.couchdb.org/en/stable/api/document/common.html#delete--db-docid

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CocuhDB database that stores the document to be deleted.
    :param docid: The document ID of the document to be deleted.
    :param params: Optional query parameter options.
    :return: The response of the HTTP request.
    """

    return client.delete(url=f'/{db}/{docid}', params=params)


def db_put(client: AsyncClient, db: str, params: Optional[Dict[str, str]] = None) -> Coroutine[Any, Any, Response]:
    """
    Create a new database.

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the database to be created.
    :param params: Optional query parameter options.
    :return: The response of the HTTP request.
    """

    return client.put(url=f'/{db}', params=params)


def db_post(client: AsyncClient, db: str, body: JSON) -> Coroutine[Any, Any, Response]:
    """
    Add a new document to the CouchDB with the name `db`, without specifying an ID for the document.

    https://docs.couchdb.org/en/stable/api/database/common.html#post--db

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CouchDB database to which to add the document.
    :param body: JSON content corresponding to the new document.
    :return: The response of the HTTP request.
    """

    return client.post(url=f'/{db}', json=body)


def db_find(client: AsyncClient, db: str, body: JSON) -> Coroutine[Any, Any, Response]:
    """
    Find documents from the CouchDB database with the name `db` matching a provided specification.

    https://docs.couchdb.org/en/stable/api/database/find.html#post--db-_find

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CouchDB database in which to find the matching documents.
    :param body: JSON content corresponding to a specification for what documents to retrieve.
    :return: The response of the HTTP request.
    """

    return client.post(url=f'/{db}/_find', json=body)


def db_all_docs(
    client: AsyncClient,
    db: str,
    params: Optional[Dict[str, str]] = None
) -> Coroutine[Any, Any, Response]:
    """
    Bulk retrieve documents from the CouchDB database with the name `db`.

    https://docs.couchdb.org/en/stable/api/database/bulk-api.html#get--db-_all_docs

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the database to retrieve documents from.
    :param params: Optional query parameter options.
    :return: The response of the HTTP request.
    """

    return client.get(url=f'/{db}/_all_docs', params=params)


def db_bulk_docs(
    client: AsyncClient,
    db: str,
    documents: List[JSON],
    new_edits: bool = True
) -> Coroutine[Any, Any, Response]:
    """
    Bulk create or update a set of documents to the CouchDB database with the name `db`.

    https://docs.couchdb.org/en/stable/api/database/bulk-api.html#post--db-_bulk_docs

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the database which to operate on.
    :param documents: The documents to be created or updated.
    :param new_edits: A flag indicating whether not to prevent the database from assigning new revision IDs.
    :return: The response of the HTTP request.
    """

    return client.post(url=f'/{db}/_bulk_docs', json=dict(docs=documents, new_edits=new_edits))


def all_dbs(client: AsyncClient, params: Optional[Dict[str, str]] = None) -> Coroutine[Any, Any, Response]:
    """
    Return a list of all the databases in the CouchDB instance.

    https://docs.couchdb.org/en/stable/api/server/common.html#all-dbs

    :param client: An HTTP client with which to perform the request.
    :param params: Optional query parameter options.
    :return: The response of the HTTP request.
    """

    return client.get(url='/_all_dbs', params=params)
