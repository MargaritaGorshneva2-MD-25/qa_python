import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

class TestBooksCollector:

    def test_add_new_book_valid_name(self, collector):
        collector.add_new_book("Название книги")
        assert "Название книги" in collector.get_books_genre()

    @pytest.mark.parametrize("name", ["Очень длинное название книги, которое превышает допустимую длину в 40 символов", ""])
    def test_add_new_book_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    def test_add_new_book_duplicate_name(self, collector):
        collector.add_new_book("Название книги")
        collector.add_new_book("Название книги")
        assert len(collector.get_books_genre()) == 1


@pytest.mark.parametrize("name, genre, expected_genre", [
    ("Название книги", "Фантастика", "Фантастика"),
    ("Другая книга", "Ужасы", "Ужасы"),
    ("Книга без жанра", "", ""), # Проверяем пустой жанр
    ("Название книги", "12345678901234567890123456789012345678901", ""), # Проверяем слишком длинный жанр, ожидаем обрезку до ""
])
def test_set_and_get_book_genre(collector, name, genre, expected_genre):
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) == expected_genre

def test_get_book_genre_non_existing(collector):
    assert collector.get_book_genre("Несуществующая книга") is None

@pytest.mark.parametrize("name, genre", [("Название книги", "Неизвестный жанр")])
def test_set_book_genre_invalid(collector, name, genre): # Тест на установку заведомо неверного жанра
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    assert collector.get_book_genre(name) == "" # "" или None, в зависимости от реализации


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

@pytest.mark.parametrize("use_age_rating, expected_books", [
    (True, ["Книга 1"]),
    (False, ["Книга 1", "Книга 2"]),
])
def test_get_books_for_children(collector, use_age_rating, expected_books):
    collector.add_new_book("Книга 1")
    collector.add_new_book("Книга 2")
    collector.set_book_genre("Книга 1", "Фантастика") # Фантастика подходит для детей
    collector.set_book_genre("Книга 2", "Ужасы")   # Ужасы не подходят для детей

    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Название книги")
        collector.add_book_in_favorites("Название книги")
        assert collector.get_list_of_favorites_books() == ["Название книги"]

    def test_add_book_in_favorites_duplicate(self):
        collector = BooksCollector()
        collector.add_new_book("Название книги")
        collector.add_book_in_favorites("Название книги")
        collector.add_book_in_favorites("Название книги")
        assert collector.get_list_of_favorites_books() == ["Название книги"]

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Название книги")
        collector.add_book_in_favorites("Название книги")
        collector.delete_book_from_favorites("Название книги")
        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_non_existing(self):
        collector = BooksCollector()
        collector.delete_book_from_favorites("Название книги")
        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Книга 1")
        collector.add_new_book("Книга 2")
        collector.add_book_in_favorites("Книга 1")
        assert collector.get_list_of_favorites_books() == ["Книга 1"]
