from flask import Flask, render_template, request
import sqlite3
from flask import g


app = Flask(__name__)


DATABASE = 'Proyectop4.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    cur = get_db().cursor()

    with app.app_context():
def make_dicts(cursor, row):
     return dict((cursor.description[idx][0], value)
                        for idx, value in enumerate(row))

        db.row_factory = make_dicts

db.row_factory = sqlite3.Row

@app.route("/")
def Formulario():
    return render_template("Formulario.html")

if __name__ == "__main__":
    app.run()