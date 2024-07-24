from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash

# from __init__.py import db
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # all of the data sent as a form will be accessible through the request.form object
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category="success")
                login_user(user, remember=True)
                # redirect to the home page after logging in
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password, try again.", category="error")
        else:
            flash("Email does not exist.", category="error")
    # render the login page if the request method is GET
    return render_template("login.html", user=current_user)


@auth.route("/logout")
# login_required decorator ensures that the user is logged in before they can log out
@login_required
def logout():
    logout_user()
    # redirect to the login page after logging out. The login page is named "auth.login" because the blueprint is named "auth"
    return redirect(url_for("auth.login"))


# accept both GET and POST requests
# GET requests are used to send data to the server (opening sign_up page)
# POST requests are used to submit data to the server to create/update a resource
@auth.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exists.", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(first_name) < 2:
            flash("First name must be greater than 1 character.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        elif len(password1) < 3:
            flash("Password must be at least 3 characters.", category="error")
        else:
            # create a new user
            new_user = User(
                email=email,
                first_name=first_name,
                password=generate_password_hash(password1, method="pbkdf2:sha256"),
            )
            # add the new user to the database
            db.session.add(new_user)
            # commit the changes to the database
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created!", category="success")
            # redirect to the home page after creating a new account
            # since we already defined views as a module using the blueprint, we can use url_for("views.home") to get call the home function on views module
            return redirect(url_for("views.home"))

    return render_template("sign_up.html", user=current_user)
