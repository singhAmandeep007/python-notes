from reminders import db
from reminders.models import User, Reminder


def get_user_from_db(app, user_id):
    with app.app_context():
        return db.session.get(User, user_id)


def get_reminder_from_db(app, reminder_id):
    with app.app_context():
        return db.session.get(Reminder, reminder_id)
