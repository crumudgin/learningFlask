import os

from app import create_app, db
from app.models import User, Role
import config

app = create_app(config.DevelopmentConfig())

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role)