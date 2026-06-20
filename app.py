from flask import Flask, render_template
import requests
from config import Jikan_Api

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)