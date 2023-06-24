from enum import Enum


class StatusCode(Enum):
    """
    Enumeration representing main HTTP status codes.

    This enumeration provides a set of commonly used HTTP status codes along with their corresponding integer values.
    It is used to represent and compare status codes in Python code.

    Attributes:
        OK (int): 200 - The request has succeeded.
        CREATED (int): 201 - The request has been fulfilled and a new resource has been created.
        ACCEPTED (int): 202 - The request has been accepted for processing but has not been completed yet.
        NO_CONTENT (int): 204 - The server has successfully fulfilled the request, but there is no content to send back.
        BAD_REQUEST (int): 400 - The server could not understand the request due to invalid syntax or other client error.
        UNAUTHORIZED (int): 401 - The client must authenticate to get the requested response.
        FORBIDDEN (int): 403 - The client does not have access rights to the content.
        NOT_FOUND (int): 404 - The server could not find the requested resource.
        METHOD_NOT_ALLOWED (int): 405 - The method specified in the request is not allowed for the resource.
        INTERNAL_SERVER_ERROR (int): 500 - The server encountered an unexpected condition that prevented it from fulfilling the request.
        SERVICE_UNAVAILABLE (int): 503 - The server is currently unavailable.
    Example:
        - Accessing status codes
          ```python
            print(StatusCode.OK)  # Output: StatusCode.OK
            print(StatusCode.OK.value)  # Output: 200
          ```
        - Comparing status codes
          ``` python
            status = StatusCode.OK

            if status == StatusCode.OK:
                print("Request successful.")
            elif status == StatusCode.NOT_FOUND:
                print("Requested resource not found.")
            else:
                print("Unhandled status code.")
          ```
    """

    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NO_CONTENT = 204
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    INTERNAL_SERVER_ERROR = 500
    SERVICE_UNAVAILABLE = 503
