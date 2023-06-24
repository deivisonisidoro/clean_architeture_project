import pytest

from src.domain.enums.status_code import StatusCode


class TestStatusCode:
    """
    Test case class for the StatusCode enumeration.

    """

    @pytest.mark.parametrize(
        "status_code",
        [
            StatusCode.OK,
            StatusCode.CREATED,
            StatusCode.ACCEPTED,
            StatusCode.NO_CONTENT,
            StatusCode.BAD_REQUEST,
            StatusCode.UNAUTHORIZED,
            StatusCode.FORBIDDEN,
            StatusCode.NOT_FOUND,
            StatusCode.METHOD_NOT_ALLOWED,
            StatusCode.INTERNAL_SERVER_ERROR,
            StatusCode.SERVICE_UNAVAILABLE,
        ],
    )
    def test_status_code_values(self, status_code: StatusCode):
        """
        Test the values of the status_code enumeration.

        Args:
            status_code (StatusCode): A status code from the StatusCode enumeration.

        """
        assert isinstance(status_code, StatusCode)
        assert isinstance(status_code.value, int)
