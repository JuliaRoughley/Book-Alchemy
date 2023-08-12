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
