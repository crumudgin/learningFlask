from flask import Blueprint

# from . import views, errors

main = Blueprint("main", __name__)

from . import views, errors
