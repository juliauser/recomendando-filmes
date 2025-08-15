
from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.themoviedb.org/3"
IMG_BASE = "https://image.tmdb.org/t/p/w500"

def tmdb_get(path, params=None):
    """Helper: faz GET na TMDB já incluindo a API key e idioma pt-BR."""
    if not API_KEY:
        return None, "API key ausente. Defina TMDB_API_KEY no arquivo .env."
    params = params or {}
    params.update({"api_key": API_KEY, "language": "pt-BR"})
    try:
        resp = requests.get(f"{BASE_URL}{path}", params=params, timeout=15)
        if resp.status_code != 200:
            return None, f"Erro da TMDB: status {resp.status_code}"
        return resp.json(), None
    except requests.RequestException as e:
        return None, f"Erro de rede: {e}"

def search_movie(name):
    data, err = tmdb_get("/search/movie", {"query": name})
    if err:
        return None, None, err
    results = data.get("results", [])
    if not results:
        return None, None, None
    first = results[0]
    return first.get("id"), first.get("title"), None

def get_recommendations(movie_id, page=1):
    data, err = tmdb_get(f"/movie/{movie_id}/recommendations", {"page": page})
    if err:
        return [], err
    return data.get("results", []), None

@app.route("/", methods=["GET", "POST"])
def index():
    api_missing = API_KEY is None
    if request.method == "POST":
        movie_name = request.form.get("movie_name", "").strip()
        if not movie_name:
            return render_template("index.html", error="Digite o nome de um filme.", api_missing=api_missing)
        movie_id, title, err = search_movie(movie_name)
        if err:
            return render_template("index.html", error=err, api_missing=api_missing)
        if not movie_id:
            return render_template("index.html", error="Filme não encontrado. Tente outro.", api_missing=api_missing)
        page = int(request.form.get("page", 1))
        recs, err = get_recommendations(movie_id, page=page)
        if err:
            return render_template("index.html", error=err, api_missing=api_missing)
        return render_template("results.html", title=title, recommendations=recs, img_base=IMG_BASE, movie_name=movie_name, page=page)
    return render_template("index.html", api_missing=api_missing)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


if __name__ == "__main__":
    app.run(debug=True)
