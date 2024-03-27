import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2 and collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    # напиши свои тесты ниже
    def test_set_book_genre_with_name_and_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Что делать, если ва')
        collector.set_book_genre('Что делать, если ва', 'Ужасы')
        assert 'Что делать, если ва' in collector.books_genre and collector.books_genre.get('Что делать, если ва') == 'Ужасы'

    def test_get_book_genre_correct_name_with_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Дратути')
        collector.set_book_genre('Дратути', 'Комедии')
        assert collector.get_book_genre('Дратути') == 'Комедии'

    def test_get_books_with_specific_genre_two_books_from_tree(self):
        collector = BooksCollector()
        collector.add_new_book('Что')
        collector.add_new_book('Что делать')
        collector.add_new_book('Что делать, если')
        collector.set_book_genre('Что', 'Ужасы')
        collector.set_book_genre('Что делать', 'Ужасы')
        collector.set_book_genre('Что делать, если', 'Комедии')
        assert len(collector.get_books_with_specific_genre('Ужасы')) == 2 and len(collector.get_books_with_specific_genre('Комедии')) == 1 and 'Что' in collector.get_books_with_specific_genre('Ужасы')

    def test_get_books_genre_tree_books(self):
        collector = BooksCollector()
        collector.add_new_book('Что')
        collector.add_new_book('Что делать')
        collector.add_new_book('Что делать, если')
        collector.set_book_genre('Что', 'Ужасы')
        collector.set_book_genre('Что делать', 'Ужасы')
        collector.set_book_genre('Что делать, если', 'Комедии')
        assert len(collector.books_genre) == 3 and collector.books_genre['Что'] == 'Ужасы' and collector.books_genre['Что делать'] == 'Ужасы' and collector.books_genre['Что делать, если'] == 'Комедии'

    def test_get_books_for_children_two_books_from_four(self):
        collector = BooksCollector()
        collector.add_new_book('гарри')
        collector.add_new_book('гарри кошмар')
        collector.add_new_book('поттер веселье')
        collector.add_new_book('поттер расследует')

        collector.set_book_genre('гарри', 'Фантастика')
        collector.set_book_genre('гарри кошмар', 'Ужасы')
        collector.set_book_genre('поттер веселье', 'Комедии')
        collector.set_book_genre('поттер расследует', 'Детектив')

        assert len(collector.get_books_for_children()) == 2 and 'гарри' in collector.get_books_for_children() and 'поттер веселье' in collector.get_books_for_children() and 'гарри кошмар' not in collector.get_books_for_children()

    def test_add_book_in_favorites_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('гарри')
        collector.add_new_book('гарри кошмар')
        collector.add_new_book('поттер веселье')
        collector.add_new_book('поттер расследует')

        collector.add_book_in_favorites('гарри')
        collector.add_book_in_favorites('поттер веселье')

        assert len(collector.favorites) == 2 and 'гарри' in collector.favorites

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('гарри')
        collector.add_new_book('гарри кошмар')
        collector.add_new_book('поттер веселье')
        collector.add_new_book('поттер расследует')

        collector.add_book_in_favorites('гарри')
        collector.add_book_in_favorites('поттер веселье')
        collector.delete_book_from_favorites('гарри')

        assert len(collector.favorites) == 1 and 'поттер веселье' in collector.favorites

    @pytest.mark.parametrize('name', ['гарри', 'гарри пожар', 'гарри горит', 'гарри ушел'])
    def test_get_list_of_favorites_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.favorites) == 1 and name in collector.favorites

    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()