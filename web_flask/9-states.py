#!/usr/bin/python3
""" States and State """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def List_states():
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def List_state_id(id):
    for state in storage.all(State).values():
        if state.id == id:
            return render_template('9-states.html', state=state, id=id)
    return render_template('9-states.html')


@app.teardown_appcontext
def close(error):
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)