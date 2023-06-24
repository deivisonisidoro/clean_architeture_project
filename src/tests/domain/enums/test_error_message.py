import pytest

from src.domain.enums.error_message import ErrorMessage


class TestErrorMessage:
    """
    Test case class for the ErrorMessage enumeration.
    """

    @pytest.mark.parametrize(
        "error_message",
        [
            ErrorMessage.INVALID_REQUEST,
            ErrorMessage.RESOURCE_NOT_FOUND,
            ErrorMessage.UNAUTHORIZED,
            ErrorMessage.FORBIDDEN,
            ErrorMessage.VALIDATION_ERROR,
        ],
    )
    def test_error_message_values(self, error_message: ErrorMessage):
        """
        Test the values of the error_message enumeration.

        Args:
            error_message (ErrorMessage): An error message from the ErrorMessage enumeration.l.

        """
        assert isinstance(error_message, ErrorMessage)
        assert isinstance(error_message.value, str)
