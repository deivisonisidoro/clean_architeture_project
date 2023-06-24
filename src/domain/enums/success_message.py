from enum import Enum


class SuccessMessage(Enum):
    """
    Enumeration representing success messages.

    This enumeration provides a set of commonly used success messages as string values.
    It is used to represent different success scenarios in an application.

    Attributes:
        CREATED_SUCCESSFULLY (str): Message indicating that an entity has been created successfully.
        UPDATED_SUCCESSFULLY (str): Message indicating that an entity has been updated successfully.
        DELETED_SUCCESSFULLY (str): Message indicating that an entity has been deleted successfully.
        RETRIEVED_SUCCESSFULLY (str): Message indicating that an entity has been retrieved successfully.

    Example:
        - Accessing success messages
          ```python
              print(SuccessMessage.CREATED_SUCCESSFULLY)  # Output: SuccessMessage.CREATED_SUCCESSFULLY
              print(SuccessMessage.CREATED_SUCCESSFULLY.value)  # Output: "Created successfully."
          ```
        - Using success messages in code
          ```python
            success_message = SuccessMessage.UPDATED_SUCCESSFULLY
            print(success_message.value)  # Output: "Updated successfully."
          ```
    """

    CREATED_SUCCESSFULLY = "Created successfully."
    UPDATED_SUCCESSFULLY = "Updated successfully."
    DELETED_SUCCESSFULLY = "Deleted successfully."
    RETRIEVED_SUCCESSFULLY = "Retrieved successfully."
