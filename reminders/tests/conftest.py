from flask.testing import FlaskClient
import pytest
from flask import Flask
from werkzeug.security import generate_password_hash
from reminders import create_app, db
from reminders.models import User

from . import utils


@pytest.fixture
def app():
    app = create_app()
    app.config.update(
        {"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"}
    )

    with app.app_context():
        db.create_all()

    yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app: Flask):
    return app.test_client()


@pytest.fixture
def authenticated_client(app: Flask, client: FlaskClient):
    user_id = None
    with app.app_context():
        user = User(
            email="test@example.com",
            password=generate_password_hash("password", method="pbkdf2:sha256"),
            first_name="TestUser",
        )
        db.session.add(user)
        db.session.commit()
        user_id = user.id
    with client:
        client.post(
            "/auth/login", data={"email": "test@example.com", "password": "password"}
        )
        yield {
            "client": client,
            "get_user": lambda: utils.get_user_from_db(app, user_id),
        }

    with app.app_context():
        db.session.delete(user)
        db.session.commit()
