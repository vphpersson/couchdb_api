from typing import Optional

from httpx import Request, Response, HTTPStatusError


class CouchDBHTTPStatusError(HTTPStatusError):
    def __init__(self, message: str, request: Request, response: Response):
        super().__init__(message=message, request=request, response=response)


def get_db_doc_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `GET /{db}/{docid}` response to a message.

    https://docs.couchdb.org/en/stable/api/document/common.html#get--db-docid

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 200:
            return 'Request completed successfully.'
        case 304:
            return 'Document wasn’t modified since specified revision.'
        case 400:
            return 'The format of the request or revision was invalid.'
        case 401:
            return 'Read privilege required.'
        case 404:
            return 'Document not found.'
        case _:
            return None


def put_db_doc_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `PUT /{db}/{docid}` response to a message.

    https://docs.couchdb.org/en/stable/api/document/common.html#put--db-docid

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 201:
            return 'Document created and stored on disk.'
        case 202:
            return 'Document data accepted, but not yet stored on disk.'
        case 400:
            return 'Invalid request body or parameters.'
        case 401:
            return 'Write privileges required.'
        case 404:
            return 'Specified database or document ID doesn’t exists.'
        case 409:
            return 'Document with the specified ID already exists or specified revision is not latest for target document.'
        case _:
            return None


def delete_db_doc_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `DELETE /{db}/{docid}` response to a message.

    https://docs.couchdb.org/en/stable/api/document/common.html#delete--db-docid

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 200:
            return 'Document successfully removed.'
        case 202:
            return 'Request was accepted, but changes are not yet stored on disk.'
        case 400:
            return 'Invalid request body or parameters.'
        case 401:
            return 'Write privileges required.'
        case 404:
            return 'Specified database or document ID doesn’t exists.'
        case 409:
            return 'Specified revision is not the latest for target document.'
        case _:
            return None


def db_put_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `PUT /{db}` response to a message.

    https://docs.couchdb.org/en/stable/api/database/common.html#put--db

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 201:
            return 'Database created successfully (quorum is met).'
        case 202:
            return 'Accepted (at least by one node).'
        case 400:
            return 'Invalid database name.'
        case 401:
            return 'CouchDB Server Administrator privileges required.'
        case 412:
            return 'Database already exists.'
        case _:
            return None


def db_post_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `POST /{db}` response to a message.

    https://docs.couchdb.org/en/stable/api/database/common.html#post--db

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 201:
            return 'Document created and stored on disk.'
        case 202:
            return 'Document data accepted, but not yet stored on disk.'
        case 400:
            return 'Invalid database name.'
        case 401:
            return 'Write privileges required.'
        case 404:
            return 'Database doesn’t exist.'
        case 409:
            return 'A Conflicting Document with same ID already exists.'
        case _:
            return None


def db_find_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `POST /{db}/_find` response to a message.

    https://docs.couchdb.org/en/stable/api/database/find.html#post--db-_find

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 200:
            return 'Request completed successfully.'
        case 400:
            return 'Invalid request.'
        case 401:
            return 'Read permission required.'
        case 404:
            return 'Requested database not found.'
        case _:
            return None


def db_all_docs_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `GET /{db}/_all_docs` response to a message.

    https://docs.couchdb.org/en/stable/api/database/bulk-api.html#get--db-_all_docs

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 200:
            return 'Request completed successfully.'
        case 404:
            return 'Requested database not found.'
        case _:
            return None


def db_bulk_docs_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `POST /{db}/_bulk_docs` response to a message.

    https://docs.couchdb.org/en/stable/api/database/bulk-api.html#post--db-_bulk_docs

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 201:
            return 'Document(s) have been created or updated.'
        case 400:
            return 'The request provided invalid JSON data.'
        case 404:
            return 'Requested database not found.'
        case _:
            return None


def all_dbs_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `GET /_all_dbs` response to a message.

    https://docs.couchdb.org/en/stable/api/server/common.html#all-dbs

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 200:
            return 'Request completed successfully.'
        case _:
            return None


def put_design_doc_status_code_message(status_code: int) -> str:
    """
    Translate a status code from a `PUT /{db}/_design/{ddoc}` response to a message.

    https://docs.couchdb.org/en/stable/api/ddoc/common.html#put--db-_design-ddoc

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    return put_db_doc_status_code_message(status_code=status_code)


def put_db_security_status_code_message(status_code: int) -> Optional[str]:
    """
    Translate a status code from a `PUT /{db}/_security` response to a message.

    https://docs.couchdb.org/en/stable/api/database/security.html#put--db-_security

    :param status_code: The status code to be translated.
    :return: The message corresponding to the status code if a translation was found.
    """

    match status_code:
        case 200:
            return 'Request completed successfully.'
        case 401:
            return 'CouchDB Server Administrator privileges required.'
        case _:
            return None


def status_code_message_from_response(response: Response) -> Optional[str]:
    """
    Translate a status code from a CouchDB API call response to a message.

    The response's status code, method, and path are used in conjunction to determine the corresponding message.

    :param response: A CouchDB API call response whose status code to translate to a message.
    :return: The message corresponding to the response's status code.
    """

    url_path_parts: tuple[str, ...] = tuple(part for part in response.request.url.path.split('/') if part != '')

    match response.request.method:
        case 'GET':
            if len(url_path_parts) == 1:
                match url_path_parts[0]:
                    case '_all_dbs':
                        return all_dbs_status_code_message(status_code=response.status_code)
                    case _:
                        return None
            elif len(url_path_parts) == 2:
                match url_path_parts[1]:
                    case '_all_docs':
                        return all_dbs_status_code_message(status_code=response.status_code)
                    case _:
                        return get_db_doc_status_code_message(status_code=response.status_code)
            else:
                return None
        case 'PUT':
            if len(url_path_parts) == 1:
                match url_path_parts[0]:
                    case _:
                        return db_put_status_code_message(status_code=response.status_code)
            elif len(url_path_parts) == 2:
                match url_path_parts[1]:
                    case '_security':
                        return put_db_security_status_code_message(status_code=response.status_code)
                    case _:
                        return put_db_doc_status_code_message(status_code=response.status_code)
            elif len(url_path_parts) == 3:
                match url_path_parts[1]:
                    case '_design':
                        return put_design_doc_status_code_message(status_code=response.status_code)
                    case _:
                        return None
        case 'POST':
            if len(url_path_parts) == 1:
                match url_path_parts[0]:
                    case _:
                        return db_post_status_code_message(status_code=response.status_code)
            elif len(url_path_parts) == 2:
                match url_path_parts[1]:
                    case '_bulk_docs':
                        return db_bulk_docs_status_code_message(status_code=response.status_code)
                    case '_find':
                        return db_find_status_code_message(status_code=response.status_code)
                    case _:
                        return None
        case 'DELETE':
            if len(url_path_parts) == 2:
                match url_path_parts[0]:
                    case _:
                        return delete_db_doc_status_code_message(status_code=response.status_code)
            else:
                return None


def raise_from_status_with_status_code_message(response: Response) -> None:
    """
    Check and CouchDB API call response and raise an exception with a descriptive message.

    :param response: The response whose response code to check.
    :return: None
    """

    try:
        response.raise_for_status()
    except HTTPStatusError as http_status_error:
        if message := status_code_message_from_response(response=response):
            raise CouchDBHTTPStatusError(
                message=message,
                request=http_status_error.request,
                response=http_status_error.response
            )
        else:
            raise http_status_error
