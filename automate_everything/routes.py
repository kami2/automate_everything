from automate_everything import app


@app.route("/")
def main():
    return "Hello World"

