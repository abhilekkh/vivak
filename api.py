from config import AniList_Api, cache
import requests
import time
from datetime import datetime

# ── GraphQL Queries ──────────────────────────────────────────────────────────

SEARCH_QUERY = """
query ($search: String, $page: Int, $perPage: Int) {
  Page(page: $page, perPage: $perPage) {
    media(search: $search, type: ANIME) {
      id
      title { romaji english }
      coverImage { medium }
      averageScore
    }
  }
}
"""

TOP_ANIME_QUERY = """
query ($page: Int, $perPage: Int) {
  Page(page: $page, perPage: $perPage) {
    media(sort: SCORE_DESC, type: ANIME, status_not: NOT_YET_RELEASED) {
      id
      title { romaji english }
      coverImage { medium }
      averageScore
    }
  }
}
"""

RECENT_ANIME_QUERY = """
query ($season: MediaSeason, $seasonYear: Int, $page: Int, $perPage: Int) {
  Page(page: $page, perPage: $perPage) {
    media(season: $season, seasonYear: $seasonYear, type: ANIME, sort: POPULARITY_DESC) {
      id
      title { romaji english }
      coverImage { medium }
      averageScore
    }
  }
}
"""

ANIME_DETAILS_QUERY = """
query ($id: Int) {
  Media(id: $id, type: ANIME) {
    id
    title { romaji english }
    coverImage { large }
    trailer { id site }
    episodes
    source
    format
    genres
    tags { name category }
    status
    startDate { year month day }
    endDate { year month day }
    averageScore
    rankings { rank type allTime }
    popularity
    description
    season
    seasonYear
    studios { edges { isMain node { name } } }
    characters(sort: ROLE, perPage: 20) {
      edges {
        node { name { full } image { medium } }
        role
      }
    }
  }
}
"""

# ── Core fetch ───────────────────────────────────────────────────────────────

def fetch(query, variables=None):
    retries = 3
    backoff = 3

    for attempt in range(retries):
        try:
            response = requests.post(
                AniList_Api,
                json={"query": query, "variables": variables or {}},
                headers={"Content-Type": "application/json"},
                timeout=10
            )

            if response.status_code == 429 or response.status_code >= 500:
                wait = backoff * (attempt + 1)
                print(f"AniList returned {response.status_code}. Retrying in {wait}s... (attempt {attempt + 1}/{retries})")
                time.sleep(wait)
                continue

            response.raise_for_status()
            return response.json()

        except requests.exceptions.Timeout:
            print(f"AniList timeout on attempt {attempt + 1}")
        except requests.exceptions.ConnectionError:
            print(f"AniList connection error on attempt {attempt + 1}")
        except requests.exceptions.HTTPError as e:
            print(f"AniList HTTP error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"AniList error: {e}")
            return None

        if attempt < retries - 1:
            time.sleep(backoff)

    print(f"AniList API failed after {retries} attempts")
    return None

# ── Public API functions ─────────────────────────────────────────────────────

@cache.memoize(timeout=3600)
def get_search_result(query):
    return fetch(SEARCH_QUERY, {"search": query, "page": 1, "perPage": 20})

@cache.memoize(timeout=86400)
def get_anime_details(anime_id):
    return fetch(ANIME_DETAILS_QUERY, {"id": int(anime_id)})

@cache.memoize(timeout=1800)
def get_top_anime():
    return fetch(TOP_ANIME_QUERY, {"page": 1, "perPage": 50})

@cache.memoize(timeout=1800)
def get_recent_anime():
    month = datetime.now().month
    year = datetime.now().year
    if month <= 3:
        season = "WINTER"
    elif month <= 6:
        season = "SPRING"
    elif month <= 9:
        season = "SUMMER"
    else:
        season = "FALL"
    return fetch(RECENT_ANIME_QUERY, {"season": season, "seasonYear": year, "page": 1, "perPage": 50})
