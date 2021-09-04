# Copyright 2021 iiPython

# Modules
import io
import requests
import urllib.parse
from app import app
from flask import abort, request, send_file, render_template

# Routes
@app.route("/srv/badge_gen", methods = ["GET"])
def gen_badge():
    return render_template(
        "content/generator.html",
        location = "/srv/badge",
        method = "GET",
        groups = [
            {"id": "labelInput", "type": "text", "name": "Badge Label", "placeholder": "Enter a label", "qname": "label"},
            {"id": "msgInput", "type": "text", "name": "Badge Message", "placeholder": "Enter a message", "qname": "msg"},
            {"id": "labelColorInput", "type": "text", "name": "Label Color", "placeholder": "Choose a HEX label color", "qname": "labelcolor"},
            {"id": "msgColorInput", "type": "text", "name": "Message Color", "placeholder": "Choose a HEX message color", "qname": "msgcolor"}
        ],
        submit_text = "Create Embed"
    ), 200

@app.route("/srv/badge", methods = ["GET"])
def load_badge():
    """This is basically an easier to use API for shields.io"""

    # Initialization
    text_label = request.args.get("label")
    text_msg = request.args.get("msg")
    msg_color = request.args.get("msgcolor", "")
    label_color = request.args.get("labelcolor", "")

    # Check required args
    if not app.require_all([text_label, text_msg]):
        return abort(400)

    # Construct url
    url = "https://raster.shields.io/badge/{}-{}-{}{}".format(
        urllib.parse.quote(text_label),
        urllib.parse.quote(text_msg),
        "126bf1" if not msg_color.strip() else msg_color.lstrip("#"),
        "?labelColor=" + ("126bf1" if not label_color.strip() else label_color.lstrip("#"))
    )
    return send_file(io.BytesIO(requests.get(url).content), mimetype = "image/png", attachment_filename = "badge.png"), 200
