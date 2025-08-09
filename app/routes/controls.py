from flask import Blueprint, request, render_template
from app.services.youtube import play_pause, next_video, search_youtube, prev_video

bp = Blueprint("controls", __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/playpause")
def playpause_route():
    play_pause()
    return render_template("index.html")

@bp.route("/next")
def next_route():
    next_video()
    return render_template("index.html")

@bp.route("/prev")
def prev_route():
    prev_video()
    return render_template("index.html")

@bp.route("/search", methods=["POST"])
def search_route():
    query = request.form.get("query", "").strip()
    if query:
        video_url =  search_youtube(query)
    return render_template("index.html")
    
