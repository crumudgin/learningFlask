from datetime import datetime

from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

bootsrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

from .main import main as main_blueprint

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)

    bootsrap.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    app.register_blueprint(main_blueprint)
    return app