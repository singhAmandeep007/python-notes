from unittest import mock

import pytest
import requests

import testing.Services as services


@mock.patch("testing.Services.get_user_by_user_id")
def test_get_user_by_user_id(mock_get_user_by_user_id):
    user = {"name": "John", "age": 22}
    mock_get_user_by_user_id.return_value = user

    assert services.get_user_by_user_id(1) == user


@mock.patch("requests.get")
def test_get_users_success(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = [
        {"name": "John", "age": 22},
        {"name": "Doe", "age": 25},
        {"name": "Smith", "age": 30},
    ]

    mock_get.return_value = mock_response

    response = services.get_users()

    assert len(response) == 3
    assert response[0]["name"] == "John"
    assert response[1]["age"] == 25
    assert response[2]["name"] == "Smith"


@mock.patch("requests.get")
def test_get_users_failure(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404

    mock_get.return_value = mock_response

    with pytest.raises(requests.HTTPError):
        services.get_users()
