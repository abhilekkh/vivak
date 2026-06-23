from config import Jikan_Api, cache
import requests

def fetch(endpoint,**params):
    response=requests.get(f"{Jikan_Api}/{endpoint}",params=params,timeout=10)
    response.raise_for_status()
    return response.json()

@cache.memoize(timeout=3600)
def get_search_result(query):
    return fetch("anime",q=query)

@cache.memoize(timeout=86400)
def get_anime_details(mal_id):
    return fetch(f"anime/{mal_id}")

@cache.memoize(timeout=86400)
def get_character_details(mal_id):
    return fetch(f"anime/{mal_id}/characters")

@cache.memoize(timeout=1800)
def get_top_anime():
    return fetch("top/anime")

@cache.memoize(timeout=1800)
def get_recent_anime():
    return fetch("seasons/now")


