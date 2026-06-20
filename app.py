from flask import Flask, render_template, request
import requests
from config import Jikan_Api

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q")

    if not query:
        return render_template("index.html", animes=[])

    response = requests.get(f"{Jikan_Api}/anime", params={"q": query})
    data = response.json()

    animes = []
    for item in data.get("data", []):
        animes.append({
            "mal_id": item.get("mal_id"),
            "title": item.get("title"),
            "image_url": item.get("images", {}).get("jpg", {}).get("image_url"),
            "score": item.get("score") or "N/A"
        })

    return render_template("index.html", animes=animes)

if __name__ == "__main__":
    app.run(debug=True)