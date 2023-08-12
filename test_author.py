import pytest

from data_models import Author


def test_create_author_instance():
    author = Author(name="Test Author", birth_date="1990-01-01", date_of_death="2022-05-10")
    assert author.name == "Test Author"
    assert author.birth_date == "1990-01-01"
    assert author.date_of_death == "2022-05-10"
