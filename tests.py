import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_valid_name(self):
        collector = BooksCollector()
        collector.add_new_book("Название книги")
        assert "Название книги" in collector.get_books_genre()

    @pytest.mark.parametrize("name", ["Очень длинное название книги, которое превышает допустимую длину в 40 символов", ""])
    def test_add_new_book_invalid_name(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_duplicate_name(self):
        collector = BooksCollector()
        collector.add_new_book("Название книги")
        collector.add_new_book("Название книги")
        assert len(collector.get_books_genre()) == 1


    @pytest.mark.parametrize("name, genre", [("Название книги", "Фантастика"), ("Другая книга", "Ужасы")])
    def test_set_book_genre_valid(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    @pytest.mark.parametrize("name, genre", [("Название книги", "Неизвестный жанр"), ("Другая книга", "")] )
    def test_set_book_genre_invalid(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == ""

    def test_get_book_genre_existing(self):
        collector = BooksCollector()
        collector.add_new_book("Название книги")
        collector.set_book_genre("Название книги", "Фантастика")
        assert collector.get_book_genre("Название книги") == "Фантастика"

    def test_get_book_genre_non_existing(self):
        collector = BooksCollector()
        assert collector.get_book_genre("Название книги") is None


    @pytest.mark.parametrize("genre, expected", [("Фантастика", ["Название книги"]), ("Ужасы", [])])
    def test_get_books_with_specific_genre(self, genre, expected):
        collector = BooksCollector()
        collector.add_new_book("Название книги")
        collector.set_book_genre("Название книги", "Фантастика")
        assert collector.get_books_with_specific_genre(genre) == expected

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        assert collector.get_books_genre() == {"Книга 1": "Фантастика", "Книга 2": ""}

    @pytest.mark.parametrize("genre_age_rating", [True, False])
    def test_get_books_for_children(self, genre_age_rating):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.set_book_genre("Книга 1", "Фантастика")
        collector.set_book_genre("Книга 2", "Ужасы")
        if genre_age_rating:
            assert collector.get_books_for_children() == ["Книга 1"]
        else:
            assert collector.get_books_for_children() == ["Книга 1", "Книга 2"]
