# Copyright 2021 iiPython

# Modules
from app import app
from flask import render_template

# Routes
@app.route("/privacy")
def privacy_policy():
    return render_template("content/legal/privacy.html"), 200
