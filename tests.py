import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books_added_two(self):
        collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_one_book_empty_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == ''

    def test_set_book_genre_with_name_and_genre_check_genre(self):
        collector = BooksCollector()
        film_name = 'Что делать, если ва'
        collector.add_new_book(film_name)
        collector.set_book_genre(film_name, collector.genre[1])
        assert collector.get_book_genre(film_name) == collector.genre[1]

    def test_get_book_genre_correct_name_with_genre(self):
        collector = BooksCollector()
        film_name = 'Дратути'
        collector.add_new_book(film_name)
        collector.set_book_genre(film_name, collector.genre[4])
        assert collector.get_book_genre(film_name) == collector.genre[4]

    def test_get_books_with_specific_genre_two_books_from_three(self):
        collector = BooksCollector()
        collector.add_new_book('Что')
        collector.add_new_book('Что делать')
        collector.add_new_book('Что делать, если')
        collector.set_book_genre('Что', collector.genre[1])
        collector.set_book_genre('Что делать', collector.genre[1])
        collector.set_book_genre('Что делать, если', collector.genre[4])
        assert len(collector.get_books_with_specific_genre(collector.genre[1])) == 2 and len(collector.get_books_with_specific_genre(collector.genre[4])) == 1 and 'Что' in collector.get_books_with_specific_genre(collector.genre[1])

    def test_get_books_genre_three_books_check_amount(self):
        collector = BooksCollector()
        collector.add_new_book('Что')
        collector.add_new_book('Что делать')
        collector.add_new_book('Что делать, если')
        collector.set_book_genre('Что', collector.genre[1])
        collector.set_book_genre('Что делать', collector.genre[1])
        collector.set_book_genre('Что делать, если', collector.genre[4])
        assert len(collector.get_books_genre()) == 3

    def test_get_books_genre_three_books_check_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Что')
        collector.add_new_book('Что делать')
        collector.add_new_book('Что делать, если')
        collector.set_book_genre('Что', collector.genre[1])
        collector.set_book_genre('Что делать', collector.genre[1])
        collector.set_book_genre('Что делать, если', collector.genre[4])
        assert collector.get_book_genre('Что') == collector.genre[1] and collector.get_book_genre('Что делать') == collector.genre[1] and collector.get_book_genre('Что делать, если') == collector.genre[4]


    def test_get_books_for_children_two_books_from_four(self):
        collector = BooksCollector()
        collector.add_new_book('гарри')
        collector.add_new_book('гарри кошмар')
        collector.add_new_book('поттер веселье')
        collector.add_new_book('поттер расследует')

        collector.set_book_genre('гарри', collector.genre[0])
        collector.set_book_genre('гарри кошмар', collector.genre[1])
        collector.set_book_genre('поттер веселье', collector.genre[4])
        collector.set_book_genre('поттер расследует', collector.genre[2])

        assert len(collector.get_books_for_children()) == 2 and 'гарри' in collector.get_books_for_children() and 'поттер веселье' in collector.get_books_for_children() and 'гарри кошмар' not in collector.get_books_for_children()

    def test_add_book_in_favorites_new_book(self):
        collector = BooksCollector()
        collector.add_new_book('гарри')
        collector.add_new_book('гарри кошмар')
        collector.add_new_book('поттер веселье')
        collector.add_new_book('поттер расследует')

        collector.add_book_in_favorites('гарри')
        collector.add_book_in_favorites('поттер веселье')

        assert len(collector.get_list_of_favorites_books()) == 2 and 'гарри' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('гарри')
        collector.add_new_book('гарри кошмар')
        collector.add_new_book('поттер веселье')
        collector.add_new_book('поттер расследует')

        collector.add_book_in_favorites('гарри')
        collector.add_book_in_favorites('поттер веселье')
        collector.delete_book_from_favorites('гарри')

        assert len(collector.get_list_of_favorites_books()) == 1 and 'поттер веселье' in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name', ['гарри', 'гарри пожар', 'гарри горит', 'гарри ушел'])
    def test_get_list_of_favorites_books(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        assert len(collector.get_list_of_favorites_books()) == 1 and name in collector.get_list_of_favorites_books()
