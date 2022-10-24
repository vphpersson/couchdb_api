from typing import Optional, Mapping, Any, Coroutine
from dataclasses import asdict

from httpx import AsyncClient, Response

from couchdb_api.structures import DesignDocument, SecurityObject


JSON = str | int | float | bool | None | Mapping[str, 'JSON'] | list['JSON']


def get_db_doc(
    client: AsyncClient,
    db: str,
    docid: str,
    params: Optional[dict[str, str]] = None,
    **client_kwargs: dict[str, Any]
) -> Coroutine[Any, Any, Response]:
    """
    Retrieve from the CouchDB database with the name `db` a document having the document ID `docid`.

    https://docs.couchdb.org/en/stable/api/document/common.html#get--db-docid

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CouchDB database from which to retrieve the document.
    :param docid: The document ID of the document to retrieve.
    :param params: Optional query parameter options.
    :param client_kwargs: Arguments passed to the HTTP client.
    :return: The response of the HTTP request.
    """

    return client.get(f'/{db}/{docid}', params=params, **client_kwargs)


def put_db_doc(
    client: AsyncClient,
    db: str,
    docid: str,
    body: JSON,
    params: Optional[dict[str, str]] = None,
    **client_kwargs: dict[str, Any]
) -> Coroutine[Any, Any, Response]:
    """
    Add a new document to the CouchDB database with the name `db`.

    https://docs.couchdb.org/en/stable/api/document/common.html#put--db-docid

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CouchDB database to which to add the document.
    :param docid: The document ID of the new document.
    :param body: JSON content corresponding to the new document.
    :param params: Optional query parameter options.
    :param client_kwargs: Arguments passed to the HTTP client.
    :return: The response of the HTTP request.
    """

    return client.put(url=f'/{db}/{docid}', json=body, params=params, **client_kwargs)


def delete_db_doc(
    client: AsyncClient,
    db: str,
    docid: str,
    params: Optional[dict[str, str]] = None,
    **client_kwargs: dict[str, Any]
) -> Coroutine[Any, Any, Response]:
    """
    Mark a document as deleted.

    https://docs.couchdb.org/en/stable/api/document/common.html#delete--db-docid

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CocuhDB database that stores the document to be deleted.
    :param docid: The document ID of the document to be deleted.
    :param params: Optional query parameter options.
    :param client_kwargs: Arguments passed to the HTTP client.
    :return: The response of the HTTP request.
    """

    return client.delete(url=f'/{db}/{docid}', params=params, **client_kwargs)


def db_put(
    client: AsyncClient,
    db: str,
    params: Optional[dict[str, str]] = None,
    **client_kwargs: dict[str, Any]
) -> Coroutine[Any, Any, Response]:
    """
    Create a new database.

    https://docs.couchdb.org/en/stable/api/database/common.html#put--db

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the database to be created.
    :param params: Optional query parameter options.
    :param client_kwargs: Arguments passed to the HTTP client.
    :return: The response of the HTTP request.
    """

    return client.put(url=f'/{db}', params=params, **client_kwargs)


def db_post(
    client: AsyncClient,
    db: str,
    body: JSON,
    **client_kwargs: dict[str, Any]
) -> Coroutine[Any, Any, Response]:
    """
    Creates a new document in the specified database, using the supplied JSON document structure.

    If the JSON structure includes the _id field, then the document will be created with the specified document ID.

    If the _id field is not specified, a new unique ID will be generated, following whatever UUID algorithm is
    configured for that server.

    https://docs.couchdb.org/en/stable/api/database/common.html#post--db

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CouchDB database to which to add the document.
    :param body: JSON content corresponding to the new document.
    :param client_kwargs: Arguments passed to the HTTP client.
    :return: The response of the HTTP request.
    """

    return client.post(url=f'/{db}', json=body, **client_kwargs)


def db_find(
    client: AsyncClient,
    db: str,
    body: JSON,
    **client_kwargs: dict[str, Any]
) -> Coroutine[Any, Any, Response]:
    """
    Find documents from the CouchDB database with the name `db` matching a provided specification.

    https://docs.couchdb.org/en/stable/api/database/find.html#post--db-_find

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the CouchDB database in which to find the matching documents.
    :param body: JSON content corresponding to a specification for what documents to retrieve.
    :param client_kwargs: Arguments passed to the HTTP client.
    :return: The response of the HTTP request.
    """

    return client.post(url=f'/{db}/_find', json=body, **client_kwargs)


def db_all_docs(
    client: AsyncClient,
    db: str,
    params: Optional[dict[str, str]] = None,
    **client_kwargs: dict[str, Any]
) -> Coroutine[Any, Any, Response]:
    """
    Bulk retrieve documents from the CouchDB database with the name `db`.

    https://docs.couchdb.org/en/stable/api/database/bulk-api.html#get--db-_all_docs

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the database to retrieve documents from.
    :param params: Optional query parameter options.
    :param client_kwargs: Arguments passed to the HTTP client.
    :return: The response of the HTTP request.
    """

    return client.get(url=f'/{db}/_all_docs', params=params, **client_kwargs)


def db_bulk_docs(
    client: AsyncClient,
    db: str,
    documents: list[JSON],
    new_edits: bool = True,
    **client_kwargs: dict[str, Any]
) -> Coroutine[Any, Any, Response]:
    """
    Bulk create or update a set of documents to the CouchDB database with the name `db`.

    https://docs.couchdb.org/en/stable/api/database/bulk-api.html#post--db-_bulk_docs

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the database which to operate on.
    :param documents: The documents to be created or updated.
    :param new_edits: A flag indicating whether not to prevent the database from assigning new revision IDs.
    :param client_kwargs: Arguments passed to the HTTP client.
    :return: The response of the HTTP request.
    """

    return client.post(url=f'/{db}/_bulk_docs', json=dict(docs=documents, new_edits=new_edits), **client_kwargs)


def all_dbs(
    client: AsyncClient,
    params: Optional[dict[str, str]] = None,
    **client_kwargs: dict[str, Any]
) -> Coroutine[Any, Any, Response]:
    """
    Return a list of all the databases in the CouchDB instance.

    https://docs.couchdb.org/en/stable/api/server/common.html#all-dbs

    :param client: An HTTP client with which to perform the request.
    :param params: Optional query parameter options.
    :param client_kwargs: Arguments passed to the HTTP client.
    :return: The response of the HTTP request.
    """

    return client.get(url='/_all_dbs', params=params, **client_kwargs)


def put_design_doc(
    client: AsyncClient,
    db: str,
    ddoc: str,
    design_document: DesignDocument
) -> Coroutine[Any, Any, Response]:
    """
    Create a new named design document, or create a new revision of the existing design document.

    https://docs.couchdb.org/en/stable/api/ddoc/common.html#put--db-_design-ddoc

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the database which to operate on.
    :param ddoc: The name of the design document to be created in the database.
    :param design_document: The design document to be created in the database.
    :return: The response of the HTTP request.
    """

    return client.put(
        url=f'/{db}/_design/{ddoc}',
        json=asdict(design_document, dict_factory=lambda x: {k: v for (k, v) in x if v is not None})
    )


def put_db_security(
    client: AsyncClient,
    db: str,
    security_object: SecurityObject
) -> Coroutine[Any, Any, Response]:
    """
    Set the security object for a given database.

    https://docs.couchdb.org/en/stable/api/database/security.html#put--db-_security

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the database which to operate on.
    :param security_object: The security object to set for the database.
    :return: The response of the HTTP request.
    """

    return client.put(
        url=f'/{db}/_security',
        json=asdict(security_object)
    )


def put_attachment(
    client: AsyncClient,
    db: str,
    doc_id: str,
    attname: str,
    data: bytes
) -> Coroutine[Any, Any, Response]:
    """
    Upload the supplied content as an attachment to the specified document.

    https://docs.couchdb.org/en/stable/api/document/attachments.html#put--db-docid-attname

    :param client: An HTTP client with which to perform the request.
    :param db: The name of the database which to operate on.
    :param doc_id: The ID of the document in which to store the attachment.
    :param attname: The name of the attachment to be stored.
    :param data: The data constituting the attachment.
    :return: The response of the HTTP request.
    """

    return client.put(url=f'/{db}/{doc_id}/{attname}', data=data)


def create_user(
    client: AsyncClient,
    username: str,
    password: str,
    roles: Optional[list[str]] = None
) -> Coroutine[Any, Any, Response]:
    """
    Create a new user in CouchDB.

    A new user is created by adding a user object to the `_users` database.

    https://docs.couchdb.org/en/stable/intro/security.html#creating-a-new-user

    :param client: An HTTP client with which to perform the request.
    :param username: The username of the user to be created.
    :param password: The password of the user to be created.
    :param roles: The roles of the user to be created.
    :return: The response of the HTTP request.
    """

    return put_db_doc(
        client=client,
        db='_users',
        docid=f'org.couchdb.user:{username}',
        body=dict(
            name=username,
            password=password,
            roles=roles or [],
            type='user'
        )
    )
