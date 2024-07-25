from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path, getcwd
from flask_login import LoginManager

# Creating a database object
db = SQLAlchemy()
# Name of the database
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "somerandomstringtoencryptsessiondata"
    # Configuring the database to work with flask app.
    # sqlite database is stored at the root of the project folder.
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    # Initialize the database with the app
    db.init_app(app)

    from .views import views
    from .auth import auth

    # Registering the blueprints, all the routes in views can be accessed with prefix with / and all the routes in auth can be accessed with prefix /auth
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    from .models import User, Reminder

    with app.app_context():
        # Create our database if it doesn't exist.
        db.create_all()

    login_manager = LoginManager()
    # The name of the view to redirect to when the user needs to log in. (This can be an absolute URL as well, if your authentication machinery is external to your application.). Here it is the function name `login` in auth blueprint.
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    # telling flask how to load a user,
    # this function is called whenever a user logs in
    # current_user exposed by flask-login as A proxy for the current user.
    @login_manager.user_loader
    def load_user(id):
        return db.session.get(User, int(id))

    return app


def create_database(app):
    current_dir = getcwd()
    # Check if the database already exist.
    if not path.exists(current_dir + "/instance/" + DB_NAME):
        with app.app_context():
            # Create our database if it doesn't exist.
            db.create_all()
            print("Created Database!")
