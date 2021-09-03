# Copyright 2021 iiPython

# Modules
from app import app
from flask import render_template

# Routes
@app.errorhandler(404)
def _error_404(e: Exception):
    return render_template("errors/404.html"), 404
