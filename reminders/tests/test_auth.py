from flask import Flask
from flask.testing import FlaskClient
import logging

from reminders.models import User


def test_home_page_authenticated(authenticated_client):
    client, get_user = authenticated_client.values()
    response = client.get("/")
    user = get_user()

    assert response.status_code == 200, logging.error(
        f"Expected 200, got {str(response.status_code)}"
    )

    assert f"{user.first_name}'s reminders".encode("utf-8") in response.data


def test_home_page_unauthenticated(client):
    response = client.get("/")
    assert response.status_code == 302, logging.error(
        f"Expected 302, got {str(response.status_code)}"
    )
    redirect_url = response.headers["Location"]
    assert "/auth/login" in redirect_url, logging.error(
        f"Expected '/auth/login' to be in redirect url, got {redirect_url}"
    )


def test_signup_success(client: FlaskClient, app: Flask):
    response = client.post(
        "/auth/sign-up",
        data={
            "email": "test@gmail.com",
            "firstName": "Test User",
            "password1": "password",
            "password2": "password",
        },
    )

    # Redirect after successful post request
    assert response.status_code == 302, logging.error(
        f"Expected 302, got {str(response.status_code)}"
    )

    with app.app_context():
        user = User.query.filter_by(email="test@gmail.com").first()
        # assert user is not None
        assert user.first_name == "Test User"


def test_signup_failure(client: FlaskClient):
    response = client.post(
        "/auth/sign-up",
        data={
            "email": "test@gmail.com",
            "firstName": "Test User",
            "password1": "password",
            "password2": "password123",
        },
    )

    assert response.status_code == 200, logging.error(
        f"Expected 200, got {str(response.status_code)}"
    )

    assert f"Passwords don&#39;t match".encode("utf-8") in response.data


def test_logout(authenticated_client):
    client, _ = authenticated_client.values()
    response = client.get("/auth/logout")
    assert response.status_code == 302, logging.error(
        f"Expected 302, got {response.status_code}"
    )
    redirect_url = response.headers["Location"]
    assert "/auth/login" in redirect_url
