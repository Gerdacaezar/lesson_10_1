import random
from unittest.mock import Mock, patch

from edu.mock_patch_edu import get_github_user_info, get_random_number


def test_get_random_number():
    mock_random = Mock(return_value=5)
    random.randint = mock_random
    assert get_random_number() == 5
    mock_random.assert_called_once_with(0, 10)


@patch("random.randint")
def test2_get_random_number(mock_random):
    mock_random.return_value = 5
    assert get_random_number() == 5
    mock_random.assert_called_once_with(0, 10)


@patch("requests.get")
def test_github_user_info(mock_get):
    mock_get.return_value.json.return_value = {"login": "testuser", "name": "Test User"}
    assert get_github_user_info("testuser") == {"login": "testuser", "name": "Test User"}
    mock_get.assert_called_once_with("https://api.github.com/users/testuser")
