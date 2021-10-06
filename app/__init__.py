# Copyright 2021 iiPython

# Modules
import os
from flask import Flask
from dotenv import load_dotenv
from .database import DBLoader

# Initialization
load_dotenv()
os.environ["_IIPYTHON_ROOT"] = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    "iiPython",
    template_folder = os.path.join(os.environ["_IIPYTHON_ROOT"], "src/templates")
)

# Configuration
app.config["hostname"] = "local.iipython.cf"
app.secret_key = os.getenv("SECRET_KEY") or input("Secret key: ")

# Functions/post-init
app.db = DBLoader(os.path.abspath("app/db"))
app.require_all = lambda x: len([_ for _ in [_.strip() for _ in x] if _]) == len(x)

# Global Jinja
@app.context_processor
def inject_globals():
    return {"app": app, "lstrip": lambda t, s: t.lstrip(s)}

# Routes
from .src.routes import (
    static, public, root, errors,
    legal
)
from .src.routes.services import (
    embeds, images, shortener
)
