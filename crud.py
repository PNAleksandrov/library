from models import Book
from typing import List
import json


def save_books_to_file(books: List[Book]) -> None:
    """
    Сохраняет новую(измененную) книгу в файл
    """
    with open('books.json', 'w') as file:
        json.dump([book.to_dict() for book in books], file)


def load_books_from_file() -> List[Book]:
    """
    Загружает книги из файла
    """
    try:
        with open('books.json', 'r') as file:
            books_data = json.load(file)
            return [Book(**book) for book in books_data]
    except FileNotFoundError:
        return []


def add_book(title: str, author: str, year: int) -> None:
    """
     Добавляет новую книгу в библиотеку.

    :param title: Название книги
    :param author: Автор книги
    :param year: Год издания
    """
    books = load_books_from_file()
    new_id = len(books) + 1 if not books else max([book.id for book in books]) + 1
    book = Book(new_id, title, author, year, "in stock")
    books.append(book)
    save_books_to_file(books)


def delete_book(id: str) -> None:
    """
    Удаляет книгу по номеру ID
    :param id: уникальный идентификационный номер
    """
    books = load_books_from_file()
    books = [book for book in books if book.id != id]
    save_books_to_file(books)


def find_books(query: str) -> List[Book]:
    """
    Ищет книги в библиотеке по названию, по автору, по году издания.
    """
    books = load_books_from_file()
    return [book for book in books if query.lower() in book.title.lower() or
            query.lower() in book.author.lower() or
            str(query).lower() in str(book.year)]


def display_books() -> None:
    """
    Отображает список всех книг в библиотеке
    """
    books = load_books_from_file()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")


def change_status(id: str, new_status: str) -> None:
    """
    Меняет статус книги по ID: статус "in stock(в наличии)" и "issue(выдана)"
    """
    books = load_books_from_file()
    for book in books:
        if book.id == id:
            book.status = new_status
            break
    save_books_to_file(books)
