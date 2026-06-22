# VIVAK
---
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![Jikan API](https://img.shields.io/badge/API-Jikan-green)
## About the project 
 **VivaK** is a Flask-powered anime discovery platform built using the **Jikan API**. It allows users to search for anime, explore detailed information, watch trailers, browse characters, discover top-rated anime, and stay updated with currently airing titles through a modern and responsive interface.
 
 ---
 ## Features

- Search anime by title
- View detailed anime information
- Browse character profiles and roles
- Watch embedded trailers
- Explore top-rated anime
- View recent/seasonal anime
- Responsive design for desktop and mobile

---

## Live Demo

https://vivak.onrender.com/

---

## How it works
1. User searches for an anime characrter
2. VIVAK sends a request to Jikan API
3. API returns character information.
4. Then data is displayed on the website

```
User -> VIVAK -> Jikan API-> Anime Data -> User
```
---
## Tech Used 

### Frontend
- HTML 5
- CSS
- JS
- Bootstrap 5
- Jinja2

### API
- Jikan API (Unoficial MyAnimeList API)

### Backend
- Python
- Flask Framework

# Project Structure

```
VivaK/
│
├── app.py
├── config.py
├── requirements.txt
│
├── static/
│   ├── style.css
│   ├── favicon.ico
│   ├── logo3.png
│   └── ...
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── anime_detail.html
│   ├── top_anime.html
│   └── updates.html
│
└── README.md
```

---

## Contributors

### Y.V.S. Vivekanand

- Designed the overall project architecture
- Developed the Home page and search functionality
- Integrated the Jikan API for search operations
- Built the initial frontend structure and styling
- Contributed to UI refinement and responsive design

### Abhilekkh Krishna

- Developed the Anime Details module
- Implemented Character Listing functionality
- Built the Top Anime and Recent Updates pages
- Integrated additional Jikan API endpoints
- Enhanced the UI using Bootstrap and improved responsiveness

---
## If you enjoyed this project

Consider giving the repository a **Star** on GitHub!
