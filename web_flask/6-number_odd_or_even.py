#!/usr/bin/python3
""" Odd or even? """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_dir(text):
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_dir(text=""):
    if text == "":
        return "Python is cool"
    else:
        return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_dir(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_even(n):
    if n % 2 != 0:
        dec = "is odd"
    else:
        dec = "is even"
    return render_template('6-number_odd_or_even.html',
                        number=n, even_odd=dec)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
