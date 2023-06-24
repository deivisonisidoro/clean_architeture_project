from enum import Enum


class ErrorMessage(Enum):
    """
    Enumeration representing error messages.

    This enumeration provides a set of commonly used error messages as string values.
    It is used to represent different error scenarios in an application.

    Attributes:
        INVALID_REQUEST (str): Message indicating that the request is invalid.
        RESOURCE_NOT_FOUND (str): Message indicating that the requested resource could not be found.
        UNAUTHORIZED (str): Message indicating that the access is unauthorized.
        FORBIDDEN (str): Message indicating that the access is forbidden.
        VALIDATION_ERROR (str): Message indicating a validation error.

    Example:
        - Accessing error messages
          ```python
            print(ErrorMessage.INVALID_REQUEST)  # Output: ErrorMessage.INVALID_REQUEST
            print(ErrorMessage.INVALID_REQUEST.value)  # Output: "Invalid request."
          ```

        - Using error messages in code
          ```python
            error_message = ErrorMessage.RESOURCE_NOT_FOUND
            print(error_message.value)  # Output: "Resource not found."
          ```
    """

    INVALID_REQUEST = "Invalid request."
    RESOURCE_NOT_FOUND = "Resource not found."
    UNAUTHORIZED = "Unauthorized access."
    FORBIDDEN = "Forbidden access."
    VALIDATION_ERROR = "Validation error."
