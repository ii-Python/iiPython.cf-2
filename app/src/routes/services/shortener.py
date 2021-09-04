# Copyright 2021 iiPython

# Modules
import string
import random
from app import app
from flask import (
    abort, request, render_template,
    url_for, redirect, flash
)

# Initialization
db = app.db.load_db("shorturls")
db.initialize("""
CREATE TABLE shorturls (
    id text,
    url text
)
""")

# Routes
@app.route("/srv/shortener", methods = ["GET"])
def shorten_url_page():
    return render_template(
        "content/generator.html",
        location = "/srv/shorten",
        method = "POST",
        groups = [
            {"id": "urlInput", "type": "text", "name": "Long URL", "placeholder": "Enter your long URL", "qname": "url"}
        ],
        submit_text = "Shorten URL"
    ), 200

@app.route("/srv/shorten", methods = ["POST"])
def shorten_url():
    url = request.form.get("url")
    if not app.require_all([url]):
        return abort(400)

    # Small URL formatting
    if url.startswith("//"):
        url.replace("//", "http://", 1)

    # Shorten URL
    short_id = None
    existing_url = db.get("shorturls", ("url", url))
    if existing_url:
        short_id = existing_url["id"]

    else:
        while True:
            short_id = "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(5))
            if db.get("shorturls", ("id", short_id)) is None:
                db.add("shorturls", (short_id, url))
                break

    # Back to index
    flash(f"New URL: <b>https://{app.config['hostname']}/l/{short_id}</b>")
    return redirect(url_for("index"))

@app.route("/l/<string:shortid>", methods = ["GET"])
def redirect_short(shortid):

    # Grab URL
    url = db.get("shorturls", ("id", shortid))
    if url is None:
        return abort(404)

    # Redirect
    return render_template("content/redirect.html", url = url["url"]), 200
