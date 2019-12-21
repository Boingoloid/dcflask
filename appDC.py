from flask import Flask

appDC = Flask(__name__)


@app.route('/')
def index():
    return "Hello World!"
