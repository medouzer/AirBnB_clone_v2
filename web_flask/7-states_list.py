#!/usr/bin/python3
""" List of states """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def List_states():
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def close(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
