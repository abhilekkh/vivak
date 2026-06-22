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

@app.route("/anime/<selected>")
def show_anime_details(selected):
    mal_id=selected.rsplit('-',1)[1]
    response=requests.get(f"{Jikan_Api}/anime/{mal_id}")
    data=response.json()
    character_response=requests.get(f"{Jikan_Api}/anime/{mal_id}/characters")
    character_data=character_response.json()

    item=data["data"]
    char_item=character_data["data"]

    details={

            "image": item.get("images",{}).get("jpg",{}).get("image_url") or "N/A",
            "youtube_embed": item.get("trailer",{}).get("embed_url") or "N/A",

            "title": item.get("title") or "N/A",
            "episodes": item.get("episodes") or "N/A",
            "source": item.get("source") or "N/A",
            "type": item.get("type") or "N/A",

            "genres": [ genre.get("name") for genre in item.get("genres",[])],


           "themes": [ theme.get("name") for theme in item.get("themes",[])],
            "status": item.get("status"),
            "airing_start": item.get("aired",{}).get("from") or "N/A",
            "airing_end" : item.get("aired",{}).get("to") or "N/A",

            "score": item.get("score") or "N/A",
            "rating": item.get("rating") or "N/A",
            "ranking" :item.get("rank") or "N/A",
            "popularity": item.get("popularity") or "N/A",
            "synopsis": item.get("synopsis") or "N/A",
            "season": item.get("season") or "N/A",
            "demographics": [ demographic.get("name") for demographic in item.get("demographics",[])],
            "licensors": [ licensor.get("name") for licensor in item.get("licensors",[])],
            "studios": [ studio.get("name") for studio in item.get("studios",[])],
            "producers": [ producer.get("name") for producer in item.get("producers",[])],

            "character": [
             {
              "name": entry.get("character", {}).get("name"),
              "image": entry.get("character", {}).get("images", {}).get("jpg", {}).get("image_url"),
               "role": entry.get("role")
             }
           for entry in char_item
            ]
            
    }
    return render_template("anime_detail.html",details=details)

@app.route("/topanime")
def topanime():
    response=requests.get(f"{Jikan_Api}/top/anime")
    data=response.json()

    animes = []
    for item in data.get("data", []):
     animes.append({
            "mal_id": item.get("mal_id"),
            "title": item.get("title"),
            "image_url": item.get("images", {}).get("jpg", {}).get("image_url"),
            "score": item.get("score") or "N/A"
     })

    return render_template("top_anime.html",animes=animes)

@app.route("/recentupdates")
def recentupdates():
    response = requests.get(f"{Jikan_Api}/seasons/now")
    data=response.json()
    animes = []
    for item in data.get("data", []):
     animes.append({
            "mal_id": item.get("mal_id"),
            "title": item.get("title"),
            "image_url": item.get("images", {}).get("jpg", {}).get("image_url"),
            "score": item.get("score") or "N/A"
     })


    return render_template("updates.html", animes=animes)

if __name__ == "__main__":
    app.run()