# Copyright 2021 iiPython

# Modules
import os
from app import app
from flask import send_from_directory

# Initialization
_ROOT_FOLDER = os.path.join(os.environ["_IIPYTHON_ROOT"], "src/root")

# Routes
@app.route("/<path:path>")
def get_root_file(path):
    return send_from_directory(_ROOT_FOLDER, path, conditional = True)
