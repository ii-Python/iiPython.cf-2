# Copyright 2021 iiPython

# Modules
from app import app
from flask import abort, request, render_template

# Routes
@app.route("/srv/embed", methods = ["GET"])
def gen_embed():
    return render_template(
        "services/embed.html",
        title = request.args.get("title"),
        image = request.args.get("image"),
        desc = request.args.get("desc"),
        color = request.args.get("color"),
        author = request.args.get("author"),
        url = request.args.get("url")
    ), 200

@app.route("/srv/embed_gen", methods = ["GET"])
def load_embed_page():
    return render_template(
        "content/generator.html",
        location = "/srv/embed",
        method = "GET",
        groups = [
            {"id": "textInput", "type": "text", "name": "Embed Title", "placeholder": "Embed title (optional)", "qname": "title"},
            {"id": "descInput", "type": "text", "name": "Embed Description", "placeholder": "Embed description (optional)", "qname": "desc"},
            {"id": "authorInput", "type": "text", "name": "Embed Author", "placeholder": "Author Text (optional)", "qname": "author"},
            {"id": "colorInput", "type": "text", "name": "Embed Color", "placeholder": "HEX color code (optional)", "qname": "color"},
            {"id": "imgInput", "type": "text", "name": "Thumbnail URL", "placeholder": "Image URL for the thumbnail (optional)", "qname": "image"}
        ],
        submit_text = "Create Embed"
    ), 200

@app.route("/srv/oembed", methods = ["GET"])
def generate_oembed():
    author = request.args.get("author", None)
    if author is None or author is not None and not author.strip():
        return abort(400)

    return '{{"type":"photo","author_name":"{}"}}'.format(author), 200
