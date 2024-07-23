import unittest
from models import Book
from crud import (add_book,
                  delete_book,
                  find_books,
                  display_books,
                  change_status,
                  save_books_to_file,
                  load_books_from_file)


class TestLibrary(unittest.TestCase):
    """

    """
    def setUp(self):
        self.books = [
            Book(1, "Преступление и наказание", "Ф.М. Достоевский", 1866, "в наличии"),
            Book(2, "Война и мир", "Л.Н. Толстой", 1869, "в наличии"),
            Book(3, "Красная шапочка", "Шарль Перро", 1697, "выдана")
        ]
        save_books_to_file(self.books)

    def test_load_books(self):
        loaded_books = load_books_from_file()
        self.assertEqual(len(loaded_books), 3)

    def test_change_status(self):
        book = load_books_from_file()[0]
        old_status = book.status
        change_status(book.id, "выдана")
        updated_book = load_books_from_file()[0]
        self.assertNotEqual(old_status, updated_book.status)
        self.assertEqual(updated_book.status, "выдана")

    def test_find_books(self):
        result = find_books("Преступление и наказание")
        expected_titles = ["Преступление и наказание"]
        for book in result:
            self.assertIn(book.title, expected_titles)


if __name__ == '__main__':
    unittest.main()
