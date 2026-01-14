from flask import render_template
from automate_everything import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/health")
def health():
    return "Health Check"
