# Copyright 2021 iiPython

# Modules
import os
from app import app
from flask import send_from_directory

# Initialization
_STATIC_DIR = os.path.join(os.environ["_IIPYTHON_ROOT"], "src/static")

# Routes
@app.route("/s/<path:path>")
def _get_static_file(path):
    return send_from_directory(_STATIC_DIR, path, conditional = True)
