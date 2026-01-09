from automate_everything import app


@app.route("/")
def main():
    return "Hello World"


@app.route("/health")
def health():
    return "Health Check"
