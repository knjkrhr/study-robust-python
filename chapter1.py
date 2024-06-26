from collections import Counter


class Book:
    auther: str
    pages: int

    def __init__(self, author: str, pages: int):
        self.author = author
        self.pages = pages


books: list[Book] = []
books.append(Book("aaaa", "100"))
books.append(Book("bbb", "100"))
books.append(Book("aaaa", "200"))

book_counter = Counter(book.author for book in books)

print(book_counter)

book_counter = Counter(book.pages for book in books)

print(book_counter)
