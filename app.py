from flask import Flask, render_template, request
from config import cache
from api import get_search_result, get_top_anime, get_recent_anime
from utils import format_anime_list, format_anime_detailed_list

app = Flask(__name__)
cache.init_app(app,config={
   "CACHE_TYPE": "SimpleCache"
})

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q")

    if not query:
        return render_template("index.html", animes=[])


    result = get_search_result(query)

    if result is None:
        return render_template(
            "index.html",
            animes=[],
            error="AniList is currently unreachable. Please try again in a few minutes."
        )

    animes = format_anime_list(result)
    return render_template("index.html", animes=animes)

@app.route("/anime/<path:selected>")
def show_anime_details(selected):
    print(selected)
    mal_id=selected.rsplit('-',1)[1]

    details=format_anime_detailed_list(mal_id)
    if details is None:
        return render_template(
            "anime_detail.html",
            details=None,
            error="AniList is currently unreachable. Please try again in a few minutes."
        )

    return render_template("anime_detail.html",details=details)

@app.route("/topanime")
def topanime():
    result = get_top_anime()

    if result is None:
        return render_template(
            "top_anime.html",
            animes=[],
            error="AniList is currently unreachable. Please try again in a few minutes."
        )
    animes = format_anime_list(result)
    return render_template("top_anime.html",animes=animes)

@app.route("/recentupdates")
def recentupdates():
    result = get_recent_anime()

    if result is None:
        return render_template(
            "updates.html",
            animes=[],
            error="AniList is currently unreachable. Please try again in a few minutes."
        )

    animes = format_anime_list(result)
    return render_template("updates.html", animes=animes)

if __name__ == "__main__":
    app.run()