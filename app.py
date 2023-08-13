import datetime
from flask import Flask, redirect, render_template, request, url_for
import data_models
from flask_sqlalchemy import SQLAlchemy
import os

basepath = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + \
    os.path.join(basepath, "data/library.sqlite")

data_models.db.init_app(app)


@app.route("/home", methods=["GET"])
def home_page():
    try:
        session = data_models.db.session
        books = session.query(data_models.Book).join(data_models.Author).all()
        message = request.args.get("message")
        return render_template("home.html", books=books, message=message)
    except Exception as ex:
        return render_template("home.html", message="Cannot load books at this time!")
    

@app.route("/search_books", methods=["GET"])
def search_books():
    search_query = request.args.get("search_query")
    if search_query:
        books = data_models.Book.query.filter(
            (data_models.Book.title.ilike(f"%{search_query}%")) |
            (data_models.Book.isbn.ilike(f"%{search_query}%")) |
            (data_models.Author.name.ilike(f"%{search_query}%"))
        ).all()
        if books:
            return render_template("home.html", books=books)
        else:
            return render_template("home.html", message="No books found that match the search criteria.")
    else:
        return redirect("/")

    

@app.route("/sort_books", methods=["GET"])
def sort_books():
    sort_option = request.args.get("sort_option")
    if sort_option == "title":
        books = data_models.Book.query.order_by(data_models.Book.title).all()
    elif sort_option == "author":
        books = data_models.Book.query.join(data_models.Author).order_by(data_models.Author.name, data_models.Book.title).all()
    elif sort_option == "publication_year":
        books = data_models.Book.query.order_by(data_models.Book.publication_year, data_models.Book.title).all()
    else:
        books = data_models.Book.query.all()

    return render_template("home.html", books=books)



@app.route("/", methods=["GET"])
def index_get():
    return redirect("/home")


@app.route("/book/<int:book_id>/delete", methods=["GET", "POST"])
def delete_book(book_id):
    book = data_models.Book.query.get(book_id)
    if book:
        data_models.db.session.delete(book)
        data_models.db.session.commit()
        return redirect(url_for("home_page", message="Book deleted successfully."))
    else:
        return redirect(url_for("home_page", message="Book not found."))



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
