import pytest

from src.domain.enums.success_message import SuccessMessage


class TestSuccessMessage:
    """
    Test class for the SuccessMessage enumeration..
    """

    @pytest.mark.parametrize(
        "success_message",
        [
            SuccessMessage.CREATED_SUCCESSFULLY,
            SuccessMessage.UPDATED_SUCCESSFULLY,
            SuccessMessage.DELETED_SUCCESSFULLY,
            SuccessMessage.RETRIEVED_SUCCESSFULLY,
        ],
    )
    def test_success_message_values(self, success_message):
        """
        Test the values of success messages in the SuccessMessage enumeration.

        Args:
            success_message (SuccessMessage): A success message from the SuccessMessage enumeration.

        """
        assert isinstance(success_message, SuccessMessage)
        assert isinstance(success_message.value, str)
