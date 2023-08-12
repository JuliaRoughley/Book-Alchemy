import datetime
from flask import Flask, redirect, render_template, request
import data_models
from flask_sqlalchemy import SQLAlchemy
import os

basepath = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
    os.path.join(basepath, "data/library.sqlite")

data_models.db.init_app(app)


@app.route("/", methods=["GET"])
def index_get():
    return redirect("/add_author")


@app.route("/add_author", methods=["GET"])
def add_author_get():
    return render_template("add_author.html")


@app.route("/add_author", methods=["POST"])
def add_author_post():

    name = request.form['name']
    birthdate = datetime.date.fromisoformat(request.form['birthdate'])
    date_of_death = datetime.date.fromisoformat(request.form['date_of_death'])

    try:
        new_author = data_models.Author(
            name=name, birth_date=birthdate, date_of_death=date_of_death)
        data_models.db.session.add(new_author)
        data_models.db.session.commit()
    except Exception as ex:
        return render_template("add_author.html", message="Can't add this Author!")

    return render_template("add_author.html", message="Author added!")


@app.route("/add_book", methods=["GET"])
def add_book_get():
    try:
        authors = data_models.Author.query.all()
        return render_template("add_book.html", authors=authors)
    except Exception as ex:
        return render_template("add_book.html", message="Cannot load authors at this time!")



@app.route("/add_book", methods=["POST"])
def add_book_post():

    isbn = request.form['isbn']
    title = request.form['title']
    publication_year = int(request.form['publication_year'])
    author_id = request.form['author_id']

    try:
        new_book = data_models.Book(
            isbn=isbn, title=title, publication_year=publication_year, author_id=author_id)
        data_models.db.session.add(new_book)
        data_models.db.session.commit()
    except Exception as ex:
        return render_template("add_book.html", message="Can't add this Book!")

    return render_template("add_book.html", message="Book added!")


if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()

    app.run()
