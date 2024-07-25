from flask import Flask
from flask.testing import FlaskClient
import pytest
import logging

from reminders.models import Reminder, User


def test_home_page_create_reminder(authenticated_client, app):
    client, get_user = authenticated_client.values()
    user = get_user()

    reminder_text = "Test reminder"

    # READ-MORE: https://flask.palletsprojects.com/en/3.0.x/testing/#form-data
    response = client.post(
        "/",
        data={
            "reminder": reminder_text,
        },
        follow_redirects=True,
    )

    assert response.status_code == 200, logging.error(
        f"Expected 200, got {str(response.status_code)}"
    )

    assert reminder_text.encode("utf-8") in response.data
    assert b"Reminder added" in response.data

    with app.app_context():
        reminder = Reminder.query.filter_by(data=reminder_text).first()
        assert reminder is not None
        assert reminder.user_id == user.id


def test_home_page_delete_reminder(authenticated_client, app):
    client, get_user = authenticated_client.values()
    user = get_user()

    # create a reminder
    reminder_text = "Test reminder"

    create_response = client.post(
        "/",
        data={
            "reminder": reminder_text,
        },
        follow_redirects=True,
    )
    # validate reminder created successfully
    assert reminder_text.encode("utf-8") in create_response.data
    assert b"Reminder added" in create_response.data

    # get the reminders from the database
    user_reminders = Reminder.query.filter_by(user_id=user.id).all()
    # validate that the reminder is in the database
    assert len(user_reminders) == 1

    # delete the reminder
    # READ-MORE: https://flask.palletsprojects.com/en/3.0.x/testing/#json-data
    delete_reponse = client.post(
        "/delete-reminder", json={"reminderId": user_reminders[0].id}
    )
    # validate that the reminder was deleted successfully
    assert delete_reponse.status_code == 200
    assert delete_reponse.json == {}
    # get the fresh reminders from the database
    user_reminders = Reminder.query.filter_by(user_id=user.id).all()
    # validate that the reminder is not in the database
    assert len(user_reminders) == 0
