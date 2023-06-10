from enum import Enum


class ErrorMessage(str, Enum):
    INVALID_REQUEST = "Invalid request."
    RESOURCE_NOT_FOUND = "Resource not found."
    UNAUTHORIZED = "Unauthorized access."
    FORBIDDEN = "Forbidden access."
    VALIDATION_ERROR = "Validation error."


class SuccessMessage(str, Enum):
    CREATED_SUCCESSFULLY = "Created successfully."
    UPDATED_SUCCESSFULLY = "Updated successfully."
    DELETED_SUCCESSFULLY = "Deleted successfully."
    RETRIEVED_SUCCESSFULLY = "Retrieved successfully."
