from automate_everything import app


@app.route("/")
def index():
    return "Hello World"


@app.route("/health")
def health():
    return "Health Check"
