from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Reminder
from . import db
import json

# creating a blueprint, a blueprint is a way to organize a group of related views and other code. It is like a mini-app inside the main app.
views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        # Gets the reminder from the HTML
        reminder = request.form.get("reminder")

        if len(reminder) < 1:
            flash("Reminder is too short!", category="error")
        else:
            # providing the schema for the reminder
            new_reminder = Reminder(data=reminder, user_id=current_user.id)
            # adding the reminder to the database
            db.session.add(new_reminder)
            # commit the changes to the database
            db.session.commit()
            flash("Reminder added!", category="success")

    return render_template("home.html", user=current_user)


@views.route("/delete-reminder", methods=["POST"])
def delete_reminder():
    # this function expects a JSON object with a reminderId key
    # using json.loads we can convert the JSON object to a Python dictionary
    reminder = json.loads(request.data)
    reminderId = reminder["reminderId"]
    reminder = Reminder.query.get(reminderId)
    if reminder:
        # check if the reminder belongs to the current user before deleting it
        if reminder.user_id == current_user.id:
            # delete the reminder from the database
            db.session.delete(reminder)
            # commit the changes to the database
            db.session.commit()
    # return an empty response
    return jsonify({})
