#!/usr/bin/python3
""" Hello Flask! """

from flask import Flask

app = Flask(__name__)

@app.roote("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


def __main__():
    app.run(host="0.0.0.0", port=5000)