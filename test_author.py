import pytest

from data_models import Author, Book


def test_create_author_instance():
    author = Author(name="Test Author", birth_date="1990-01-01", date_of_death="2022-05-10")
    assert author.name == "Test Author"
    assert author.birth_date == "1990-01-01"
    assert author.date_of_death == "2022-05-10"


def test_create_book_instance():
    author = Author(name="Test Author")
    book = Book(isbn="1234567890", title="Test Book", publication_year=2023, author_id=author.id)
    assert book.isbn == "1234567890"
    assert book.title == "Test Book"
    assert book.publication_year == 2023
    assert book.author_id == author.id
