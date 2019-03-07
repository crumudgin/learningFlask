from datetime import datetime

from flask import Flask, render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User

@main.route("/", methods=["GET", "POST"])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session["name"] = form.name.data
        return redirect(url_for(".index"))
    return render_template("index.html", current_time=datetime.utcnow(), form=form, name=session.get("name"))