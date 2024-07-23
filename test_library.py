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
            Book(2, "Война и мир", "Л.Н. Толстой", 1869, "в наличии")
        ]
        save_books_to_file(self.books)

    def test_load_books(self):
        loaded_books = load_books_from_file()
        self.assertEqual(len(loaded_books), 2)

    def test_delete_book(self):
        initial_count = len(load_books_from_file())
        delete_book(initial_count)
        updated_count = len(load_books_from_file())
        self.assertEqual(updated_count, initial_count - 1)
        with self.assertRaises(IndexError):
            deleted_book = load_books_from_file()[initial_count - 1]

    def test_find_books(self):
        result = find_books("Преступление и наказание")
        expected_titles = ["Преступление и наказание"]
        for book in result:
            self.assertIn(book.title, expected_titles)


if __name__ == '__main__':
    unittest.main()
