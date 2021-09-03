# Copyright 2021 iiPython

# Modules
from app import app
from flask import render_template

# Routes
@app.route("/")
def index():
    return render_template("index.html"), 200

@app.route("/about")
def about():
    return render_template("content/about.html"), 200
