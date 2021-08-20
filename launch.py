# Copyright 2021 iiPython

# Modules
from app import app

# Launch server
app.run(
    host = "0.0.0.0",
    port = 8080,
    debug = True
)
