# Copyright 2021 iiPython

# Modules
import os
from flask import Flask

# Initialization
os.environ["_IIPYTHON_ROOT"] = os.path.abspath(os.path.dirname(__file__))
app = Flask(
    "iiPython",
    template_folder = os.path.join(os.environ["_IIPYTHON_ROOT"], "app/src/templates")
)

# Routes
from .src.routes import (
    static, public
)
