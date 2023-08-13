from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    birth_date = db.Column(db.Date, nullable=True)
    date_of_death = db.Column(db.Date, nullable=True)

    def __init__(self, name, birth_date=None, date_of_death=None):
        self.name = name
        self.birth_date = birth_date
        self.date_of_death = date_of_death

    def __repr__(self):
        return f"Author(id={self.id}, name='{self.name}', birth_date={self.birth_date}, date_of_death={self.date_of_death})"

    def __str__(self):
        return f"Author: {self.name}, ID: {self.id}"


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    publication_year = db.Column(db.Integer, nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey(
        'author.id'), nullable=False)

    author = db.relationship('Author', backref=db.backref('books', lazy=True))

    def __init__(self, isbn, title, publication_year=None, author_id=None):
        self.isbn = isbn
        self.title = title
        self.publication_year = publication_year
        self.author_id = author_id

    def __repr__(self):
        return f"Book(id={self.id}, isbn='{self.isbn}', title='{self.title}', publication_year={self.publication_year},"\
               f" author_id={self.author_id})"

    def __str__(self):
        return f"Book: {self.title}, ISBN: {self.isbn}"
    
    def img_url(self):
        API_address = "https://covers.openlibrary.org/b/"
        uri = f'{API_address}isbn/{self.isbn}-S.jpg'
        return uri
