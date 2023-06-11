from enum import Enum


class ErrorMessage(str, Enum):
    """
    Enum class representing error messages.

    This enum class defines different error messages that can be used within
    the application when handling errors and exceptions.

    Enum Values:
        INVALID_REQUEST: An error message indicating an invalid request.
        RESOURCE_NOT_FOUND: An error message indicating that a requested resource
                            was not found.
        UNAUTHORIZED: An error message indicating unauthorized access.
        FORBIDDEN: An error message indicating forbidden access.
        VALIDATION_ERROR: An error message indicating a validation error.

    """

    INVALID_REQUEST = "Invalid request."
    RESOURCE_NOT_FOUND = "Resource not found."
    UNAUTHORIZED = "Unauthorized access."
    FORBIDDEN = "Forbidden access."
    VALIDATION_ERROR = "Validation error."


class SuccessMessage(str, Enum):
    """
    Enum class representing success messages.

    This enum class defines different success messages that can be used within
    the application to indicate successful operations.

    Enum Values:
        CREATED_SUCCESSFULLY: A success message indicating that an entity was created successfully.
        UPDATED_SUCCESSFULLY: A success message indicating that an entity was updated successfully.
        DELETED_SUCCESSFULLY: A success message indicating that an entity was deleted successfully.
        RETRIEVED_SUCCESSFULLY: A success message indicating that an entity was retrieved successfully.

    """

    CREATED_SUCCESSFULLY = "Created successfully."
    UPDATED_SUCCESSFULLY = "Updated successfully."
    DELETED_SUCCESSFULLY = "Deleted successfully."
    RETRIEVED_SUCCESSFULLY = "Retrieved successfully."
