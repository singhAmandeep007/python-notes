# Import the db object from the current package (reminders)
from . import db
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Reminder(db.Model):
    """
    Represents a reminder in the application.

    Attributes:
        id (int): The unique identifier for the reminder.
        data (str): The content of the reminder.
        date (datetime): The date and time when the reminder was created.
        user_id (int): The foreign key referencing the user who created the reminder.
    """

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # The timezone=True argument tells SQLAlchemy to store the date in the database in UTC.
    # default=func.now() tells SQLAlchemy to use the current time when creating a new reminder.
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    # The user_id column is a foreign key that references the id column in the user table.
    # This column is used to associate a reminder with the user who created it.
    # one to many relationship between user and reminder
    # NOTE: user is lowercase because it references the table name, not the class name.
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


# Inherit methods from db.Model and UserMixin
# UserMixin is a class that has default implementations of the methods that Flask-Login expects user objects to have.
class User(db.Model, UserMixin):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        reminders (relationship): The relationship to the user's reminders.
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    # The relationship attribute establishes a one-to-many relationship between the User and Reminder models.
    # NOTE: here the "Reminder" is the class name, not the table name.
    reminders = db.relationship("Reminder")
