import re
from api import get_anime_details

# â”€â”€ Helpers â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def strip_html(text):
    if not text:
        return "N/A"
    cleaned = re.sub(r'<[^>]+>', '', text).strip()
    return cleaned or "N/A"

def fmt_date(d):
    if not d or not d.get("year"):
        return "N/A"
    month = str(d.get("month") or "").zfill(2)
    day   = str(d.get("day")   or "").zfill(2)
    return f"{d['year']}-{month}-{day}"

SOURCE_MAP = {
    "ORIGINAL": "Original", "MANGA": "Manga", "LIGHT_NOVEL": "Light Novel",
    "VISUAL_NOVEL": "Visual Novel", "VIDEO_GAME": "Video Game", "NOVEL": "Novel",
    "DOUJINSHI": "Doujinshi", "ANIME": "Anime", "WEB_NOVEL": "Web Novel",
    "LIVE_ACTION": "Live Action", "GAME": "Game", "COMIC": "Comic",
    "MULTIMEDIA_PROJECT": "Multimedia Project", "PICTURE_BOOK": "Picture Book",
    "OTHER": "Other"
}

FORMAT_MAP = {
    "TV": "TV", "TV_SHORT": "TV Short", "MOVIE": "Movie",
    "SPECIAL": "Special", "OVA": "OVA", "ONA": "ONA", "MUSIC": "Music"
}

STATUS_MAP = {
    "FINISHED": "Finished Airing", "RELEASING": "Currently Airing",
    "NOT_YET_RELEASED": "Not yet aired", "CANCELLED": "Cancelled", "HIATUS": "On Hiatus"
}

# â”€â”€ Public formatters â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€

def format_anime_list(data):
    items = data.get("data", {}).get("Page", {}).get("media", [])
    result = []
    for item in items:
        score = item.get("averageScore")
        result.append({
            "mal_id":    item.get("id"),
            "title":     item.get("title", {}).get("english") or item.get("title", {}).get("romaji") or "N/A",
            "image_url": item.get("coverImage", {}).get("extraLarge"),
            "score":     round(score / 10, 1) if score else "N/A"
        })
    return result

def format_anime_detailed_list(anime_id):
    data = get_anime_details(anime_id)
    if data is None:
        return None

    item = data.get("data", {}).get("Media")
    if not item:
        return None

    # Trailer
    trailer = item.get("trailer") or {}
    if trailer.get("site") == "youtube" and trailer.get("id"):
        youtube_embed = f"https://www.youtube.com/embed/{trailer['id']}"
    else:
        youtube_embed = "N/A"

    # Score (AniList uses 0-100, convert to 0-10)
    raw_score = item.get("averageScore")
    score = round(raw_score / 10, 1) if raw_score else "N/A"

    # All-time score ranking
    ranking = "N/A"
    for r in (item.get("rankings") or []):
        if r.get("allTime") and r.get("type") == "RATED":
            ranking = r.get("rank")
            break

    # Studios vs producers
    all_studios = item.get("studios", {}).get("edges") or []
    studios   = [e["node"]["name"] for e in all_studios if e.get("isMain")]
    producers = [e["node"]["name"] for e in all_studios if not e.get("isMain")]

    # Season string
    season_name = item.get("season") or ""
    season_year = item.get("seasonYear") or ""
    season = f"{season_name.capitalize()} {season_year}".strip() if season_name else "N/A"

    # Characters
    characters = [
        {
            "name":  edge.get("node", {}).get("name", {}).get("full"),
            "image": edge.get("node", {}).get("image", {}).get("medium"),
            "role":  (edge.get("role") or "").replace("_", " ").title() or None
        }
        for edge in (item.get("characters", {}).get("edges") or [])
    ]

    # Themes from tags
    theme_categories = {"Theme-Action", "Theme-Arts", "Theme-Drama", "Theme-Fantasy",
                        "Theme-Other", "Theme-Romance", "Theme-Sci-Fi",
                        "Theme-Slice of Life", "Theme-Sports", "Theme-Supernatural", "Theme-Thriller"}
    themes = [t["name"] for t in (item.get("tags") or []) if t.get("category") in theme_categories][:8]

    return {
        "image":         item.get("coverImage", {}).get("extraLarge") or "N/A",
        "youtube_embed": youtube_embed,
        "title":         item.get("title", {}).get("english") or item.get("title", {}).get("romaji") or "N/A",
        "episodes":      item.get("episodes") or "N/A",
        "source":        SOURCE_MAP.get(item.get("source", ""), item.get("source") or "N/A"),
        "type":          FORMAT_MAP.get(item.get("format", ""), item.get("format") or "N/A"),
        "genres":        item.get("genres") or [],
        "themes":        themes,
        "status":        STATUS_MAP.get(item.get("status", ""), item.get("status") or "N/A"),
        "airing_start":  fmt_date(item.get("startDate")),
        "airing_end":    fmt_date(item.get("endDate")),
        "score":         score,
        "rating":        "N/A",
        "ranking":       ranking,
        "popularity":    item.get("popularity") or "N/A",
        "synopsis":      strip_html(item.get("description")),
        "season":        season,
        "demographics":  [],
        "licensors":     [],
        "studios":       studios,
        "producers":     producers,
        "character":     characters
    }

