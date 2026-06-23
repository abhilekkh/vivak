# <h1 align="center">VIVAK</h1>

<p align="center">
  <strong>Anime Discovery Platform built with Flask and the Jikan REST API</strong>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.x-black?logo=flask)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)
![Jikan API](https://img.shields.io/badge/API-Jikan-green)
![GitHub stars](https://img.shields.io/github/stars/abhilekkh/vivak?style=social)

</p>

<p align="center">
  <a href="https://vivak.onrender.com">
    <img src="https://img.shields.io/badge/Live%20Demo-Visit%20Website-brightgreen?style=for-the-badge" />
  </a>
  <a href="https://github.com/abhilekkh/vivak">
    <img src="https://img.shields.io/badge/Source%20Code-GitHub-black?style=for-the-badge&logo=github" />
  </a>
</p>

---

# About

**VivaK** is a Flask-powered anime discovery platform built using the **Jikan REST API**. It enables users to search for anime, explore detailed information, watch trailers, browse character information, discover top-rated anime, and stay updated with currently airing titles through a modern, responsive interface.

The project also demonstrates clean backend architecture by separating routing, API communication, configuration, caching, and data formatting into dedicated modules.

---

# Features

* 🔍 Search anime using the Jikan REST API
* 📖 View detailed anime information
* 👥 Browse anime character listings
* 🎬 Watch official anime trailers
* ⭐ Browse top-rated anime
* 📺 Explore currently airing anime
* ⚡ Memoized API requests using **Flask-Caching (SimpleCache)** to reduce redundant API calls and improve response times
* 🧩 Modular backend architecture with dedicated API, utility, configuration, and routing layers
* 📱 Responsive Bootstrap-based interface

---

# Screenshots

## Home Page

![Home](static/screenshots/home.png)

---

## Anime Details

<p align="center">
  <img src="static/screenshots/details_1.png" width="48%">
  <img src="static/screenshots/details_2.png" width="48%">
</p>

<p align="center">
  <img src="static/screenshots/details_3.png" width="48%">
  <img src="static/screenshots/details_4.png" width="48%">
</p>

---

## Top Anime

![Top Anime](static/screenshots/top_anime.png)

---

## Recent Updates

![Recent Updates](static/screenshots/recent_anime.png)

---

# Live Demo

🌐 **https://vivak.onrender.com/**

---

# Project Architecture

The application follows a modular architecture that separates routing, API communication, configuration, caching, and data formatting, making the codebase easier to maintain, extend, and test.

```text
                Browser
                   │
                   ▼
        Flask Routes (app.py)
                   │
                   ▼
      Utility Layer (utils.py)
                   │
                   ▼
 Cached API Service Layer (api.py)
                   │
                   ▼
        Jikan REST API Server
```

---

# Tech Stack

## Frontend

* HTML5
* CSS3
* JavaScript
* Bootstrap 5
* Jinja2

## Backend

* Python
* Flask
* Flask-Caching

## API

* Jikan REST API (Unofficial MyAnimeList API)

---

# Project Structure

```text
VivaK/
│
├── app.py
├── api.py
├── utils.py
├── config.py
├── requirements.txt
│
├── static/
│   ├── favicon.ico
│   ├── logo3.png
│   ├── style.css
│   └── screenshots/
│       ├── home.png
│       ├── details_1.png
│       ├── details_2.png
│       ├── details_3.png
│       ├── details_4.png
│       ├── top_anime.png
│       └── recent_anime.png
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

# Installation

```bash
# Clone the repository
git clone https://github.com/abhilekkh/vivak.git

# Navigate into the project
cd vivak

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

---

# Contributors

## Y. V. S. Vivekanand

* Designed the overall project architecture
* Developed the Home page and search functionality
* Integrated the Jikan API for anime search
* Built the initial frontend structure and styling
* Contributed to UI refinement and responsive design

## Abhilekkh Krishna

* Developed the Anime Details module
* Implemented Character Listing functionality
* Built the Top Anime and Recent Updates pages
* Integrated additional Jikan API endpoints
* Implemented API caching using Flask-Caching
* Enhanced the UI using Bootstrap and improved responsiveness

---

# Future Improvements

* 🔹 Pagination for anime listings
* 🔹 Search autocomplete
* 🔹 Advanced filtering
* 🔹 User favorites and watchlists
* 🔹 Redis-based caching for production
* 🔹 Dark/Light theme toggle
* 🔹 User authentication

---

# Acknowledgements

* **Jikan REST API** for providing anime data
* **MyAnimeList** for the original anime database
* **Flask** and the open-source community

---

# Support

If you found this project useful, consider giving the repository a ⭐ on GitHub!

It helps the project reach more people and motivates future improvements.
