from flask import Flask


app = Flask(__name__)

from automate_everything import routes
