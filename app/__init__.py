# Copyright 2021 iiPython

# Modules
import os
from flask import Flask

# Initialization
os.environ["_IIPYTHON_ROOT"] = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    "iiPython",
    template_folder = os.path.join(os.environ["_IIPYTHON_ROOT"], "src/templates")
)
app.config["hostname"] = "local.iipython.cf"

# Global Jinja
@app.context_processor
def inject_globals():
    return {"app": app, "lstrip": lambda t, s: t.lstrip(s)}

# Routes
from .src.routes import (
    static, public, root, errors
)
from .src.routes.services import (
    embeds
)
