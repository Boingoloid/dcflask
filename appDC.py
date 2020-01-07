from flask import Flask

appDC = Flask(__name__)


@appDC.route('/')
def index():
    return "Hello Cruel World"
