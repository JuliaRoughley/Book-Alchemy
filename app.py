from flask import Flask
from data_models import db
from flask_sqlalchemy import SQLAlchemy
import os

basepath = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(basepath, "data/library.sqlite")

db.init_app(app)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run()
