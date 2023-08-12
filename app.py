from flask import Flask, redirect, render_template
import data_models
from flask_sqlalchemy import SQLAlchemy
import os

basepath = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
    os.path.join(basepath, "data/library.sqlite")

data_models.db.init_app(app)


@app.route("/", methods=["GET"])
def index():
    return redirect("/add_author")


@app.route("/add_author")
def add_author():
    return render_template("add_author.html")


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()

    app.run()
