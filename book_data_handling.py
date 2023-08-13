import requests

API_address = "https://covers.openlibrary.org/b/"


def get_book_cover(isbn):
    uri = f'{API_address}/isbn/{isbn}-S.jpg'
    book_cover = requests.get(uri)
    return book_cover



