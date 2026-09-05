from config import Jikan_Api, cache
import requests
import time

def fetch(endpoint, **params):
    url = f"{Jikan_Api}/{endpoint}"
    retries = 3
    backoff = 3  # seconds

    for attempt in range(retries):
        try:
            response = requests.get(url, params=params, timeout=10)

            # Retry on rate limit (429) or any server error (5xx)
            if response.status_code == 429 or response.status_code >= 500:
                wait = backoff * (attempt + 1)
                print(f"Jikan returned {response.status_code}. Retrying in {wait}s... (attempt {attempt + 1}/{retries})")
                time.sleep(wait)
                continue

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            print(f"Jikan API timeout on attempt {attempt + 1}: {url}")
        except requests.exceptions.ConnectionError:
            print(f"Jikan API connection error on attempt {attempt + 1}: {url}")
        except requests.exceptions.HTTPError as e:
            print(f"Jikan API HTTP error: {e} — {url}")
            return None  # Don't retry on 4xx (except 429 handled above)
        except requests.exceptions.RequestException as e:
            print(f"Jikan API error: {e}")
            return None

        if attempt < retries - 1:
            time.sleep(backoff)

    print(f"Jikan API failed after {retries} attempts: {url}")
    return None

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


