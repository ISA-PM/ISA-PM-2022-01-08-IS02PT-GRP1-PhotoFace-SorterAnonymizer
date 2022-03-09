import sys
import pathlib
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    # initialize a flask object
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "facemasksystemkey"
    app.config['UPLOAD_FOLDER_GRP'] = 'input/group'
    app.config['UPLOAD_FOLDER_INDV'] = 'input/individual'
    app.config['PROCESSED_FOLDER'] = 'application/processed'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db2.sqlite'

    db.init_app(app)
    
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app