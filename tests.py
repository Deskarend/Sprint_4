import random
import pytest
from conftest import DEFAULT_BOOK_GENRE, DEFAULT_FAVORITES, DEFAULT_GENRE, DEFAULT_GENRE_AGE_RATING


class TestBooksCollector:

    def test_default_books_genre_is_empty_dictionary(self, default_collector):
        assert default_collector.books_genre == DEFAULT_BOOK_GENRE

    def test_default_favorites_is_empty_list(self, default_collector):
        assert default_collector.favorites == DEFAULT_FAVORITES

    def test_default_genre_true(self, default_collector):
        # Сортировка для более удобной проверки: шоб не было циклов с 'in' и сравнения длин списков
        assert sorted(default_collector.genre) == sorted(DEFAULT_GENRE)

    def test_default_genre_age_rating_true(self, default_collector):
        assert sorted(default_collector.genre_age_rating) == sorted(DEFAULT_GENRE_AGE_RATING)

    @pytest.mark.parametrize('book_name', [
        pytest.param('a', id="book's name is 1 symbol"),
        pytest.param('aя', id="book's name is 2 symbols"),
        pytest.param('И смех и грех', id="book's name is 13 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetue', id="book's name is 39 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetuer', id="book's name is 40 symbols")
    ])
    def test_add_new_book_add_one_book_with_name_in_1_and_2_and_13_and_39_and_40symbols_to_empty_collector_added_one_book_without_genre \
    (self, default_collector, book_name):

        default_collector.add_new_book(book_name)

        assert default_collector.books_genre == {book_name: ''}

    @pytest.mark.parametrize('book_name', [
        pytest.param('a', id="book's name is 1 symbol"),
        pytest.param('aя', id="book's name is 2 symbols"),
        pytest.param('И смех и грех', id="book's name is 13 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetue', id="book's name is 39 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetuer', id="book's name is 40 symbols")
    ])
    def test_add_new_book_add_one_book_with_name_in_1_and_2_and_13_and_39_and_40symbols_to_non_empty_collector_added_one_book_without_genre \
    (self, collector, book_name):

        expected_books_genre = collector.books_genre.copy()
        expected_books_genre.update({book_name: ''})

        collector.add_new_book(book_name)
        assert sorted(collector.books_genre.items()) == sorted(expected_books_genre.items())

    @pytest.mark.parametrize('books', [
        pytest.param(['Книга_11', 'Книга_22'], id='2 books'),
        pytest.param(['Книга_11', 'Книга_22', 'Книга_33', 'Книга_44', 'Книга_55'], id="5 books")
    ])
    def test_add_new_book_add_2_and_5books_to_empty_collector_added_books(self, default_collector, books):
        expected_books_genre = default_collector.books_genre.copy()

        for book in books:
            expected_books_genre.update({book: ''})
            default_collector.add_new_book(book)

            assert sorted(expected_books_genre.items()) == sorted(default_collector.books_genre.items())

    @pytest.mark.parametrize('books', [
        pytest.param(['Книга_11', 'Книга_22'], id='2 books'),
        pytest.param(['Книга_11', 'Книга_22', 'Книга_33', 'Книга_44', 'Книга_55'], id="5 books")
    ])
    def test_add_new_book_add_2_and_5books_to_non_empty_collector_added_books(self, collector, books):
        expected_books_genre = collector.books_genre.copy()

        for book in books:
            expected_books_genre.update({book: ''})
            collector.add_new_book(book)

            assert sorted(expected_books_genre.items()) == sorted(collector.books_genre.items())

    def test_add_new_book_add_the_one_book_twice_to_non_empty_collector_added_one_book(self, collector):
        name = 'Дважды два равняется одуванчику'

        collector.add_new_book(name)
        expected_books_genre = collector.books_genre
        collector.add_new_book(name)
        books_genre = collector.books_genre

        assert sorted(expected_books_genre.items()) == sorted(books_genre.items())

    def test_add_new_book_add_the_one_book_twice_to_empty_collector_added_one_book(self, default_collector):
        name = 'Дважды два равняется одуванчику'

        default_collector.add_new_book(name)
        expected_books_genre = default_collector.books_genre
        default_collector.add_new_book(name)
        books_genre = default_collector.books_genre

        assert sorted(expected_books_genre.items()) == sorted(books_genre.items())

    @pytest.mark.parametrize('name', [
        pytest.param('', id="book's name is 0 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetuerr', id="book's name is 41 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetuer a', id="book's name is 42 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetuer adipiscing elit, se', id="book's name is 60 symbols")
    ])
    def test_add_new_book_add_one_book_with_name_in_0_and_41_and_42_and_60_symbols_to_empty_collector_no_added_book\
    (self, default_collector, name):

        default_collector.add_new_book(name)

        assert default_collector.books_genre == {}

    @pytest.mark.parametrize('name', [
        pytest.param('', id="book's name is 0 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetuerr', id="book's name is 41 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetuer a', id="book's name is 42 symbols"),
        pytest.param('Lorem ipsum dolor sit amet, consectetuer adipiscing elit, se', id="book's name is 60 symbols")
    ])
    def test_add_new_book_add_one_book_with_name_in_0_and_41_and_42symbols_to_non_empty_collector_no_added_book\
    (self, collector, name):

        expected_books_genre = collector.books_genre.copy()
        collector.add_new_book(name)

        assert sorted(expected_books_genre.items()) == sorted(collector.books_genre.items())

    def test_set_book_genre_set_genre_of_1_to_5books_to_no_genre_books_added_genre_to_books\
    (self, default_collector):

        books = {'Книга_1': '', 'Книга_2': '', 'Книга_3': '', 'Книга_4': '', 'Книга_5': ''}
        default_collector.books_genre = books
        expected_books_genre = books.copy()

        for book in books:
            genre = random.choice(default_collector.genre)
            default_collector.set_book_genre(book, genre)
            expected_books_genre[book] = genre

            assert sorted(expected_books_genre.items()) == sorted(default_collector.books_genre.items())


    def test_set_book_genre_set_genre_of_1_to_5books_to_books_with_genres_added_genre_to_books\
    (self, collector):

        expected_books_genre = collector.books_genre.copy()

        for book in collector.books_genre:
            genre = random.choice(collector.genre)
            collector.set_book_genre(book, genre)
            expected_books_genre[book] = genre

            assert sorted(expected_books_genre.items()) == sorted(collector.books_genre.items())

    def test_set_book_genre_set_genre_of_not_added_book_not_added_book_and_not_set_genre(self, collector):
        book = "a not added book"
        genre = random.choice(collector.genre)
        expected_books_genre = collector.books_genre.copy()

        collector.set_book_genre(book, genre)

        assert (collector.books_genre.get(book) is None
                and expected_books_genre.items() == collector.books_genre.items())

    def test_set_book_genre_set_not_added_genre_not_set_genre(self, collector):
        book = random.choice(list(collector.books_genre))
        expected_books_genre = collector.books_genre.copy()

        genre = "a not added genre"
        collector.set_book_genre(book, genre)

        assert (collector.books_genre.get(book) != genre
                and expected_books_genre.items() == collector.books_genre.items())

    def test_set_book_genre_set_not_added_genre_of_not_added_book_not_added_book_and_not_set_genre(self, collector):
        book = "a not added book"
        genre = "a not added genre"
        expected_books_genre = collector.books_genre.copy()

        collector.set_book_genre(book, genre)

        assert (collector.books_genre.get(book) is None
                and expected_books_genre.items() == collector.books_genre.items())

    def test_get_book_genre_get_genre_of_1_to_5books_got_genres(self, collector):

        for book, genre in collector.books_genre.items():
            assert collector.get_book_genre(book) == genre

    def test_get_book_genre_get_genre_of_not_added_book_not_got_genre(self, collector):
        book = 'A not added book'

        assert collector.books_genre.get(book) is None

    def test_get_books_with_specific_genre_get_books_with_specific_genre_got_books_with_specific_genre(self, collector):

        specific_genre = random.choice(collector.genre)
        expected_books_with_specific_genre = [book for book, genre in collector.books_genre.items()
                                              if genre == specific_genre]
        books_with_specific_genre = collector.get_books_with_specific_genre(specific_genre)

        assert sorted(expected_books_with_specific_genre) == sorted(books_with_specific_genre)

    def test_get_books_with_specific_genre_get_books_with_not_added_genre_no_got_books(self, collector):
        specific_genre = 'A not added genre'

        books_with_specific_genre = collector.get_books_with_specific_genre(specific_genre)

        assert books_with_specific_genre == []

    def test_get_books_genre_get_book_genre_with_or_without_genre_got_book_genre(self, collector):

        assert sorted(collector.books_genre.items()) == sorted(collector.get_books_genre().items())

    def test_get_books_genre_get_empty_book_genre_got_empty_book_genre(self, default_collector):

        assert default_collector.get_books_genre() == {}

    def test_get_books_for_children_get_books_with_or_without_genre_got_books(self, collector):

        expected_books_for_children = [book for book, genre in collector.books_genre.items()
                                       if genre not in collector.genre_age_rating
                                       and genre in collector.genre]

        books_for_children = collector.get_books_for_children()

        assert sorted(expected_books_for_children) == sorted(books_for_children)

    def test_add_book_in_favorites_add_of_1_to_5_books_got_books(self, collector):
        # Создаем проверочный список любимых книг и добавляем книги в любимые
        expected_favorite_books = []
        favorite_books = collector.books_genre
        for book in favorite_books:
            collector.add_book_in_favorites(book)
            expected_favorite_books.append(book)

            assert sorted(expected_favorite_books) == sorted(collector.favorites)

    def test_add_book_in_favorites_add_the_one_book_twice_added_one_book(self, collector):

        favorite_book = random.choice(list(collector.books_genre))
        collector.add_book_in_favorites(favorite_book)
        collector.add_book_in_favorites(favorite_book)

        assert favorite_book in collector.favorites and len(collector.favorites) == 1

    def test_add_book_in_favorites_add_not_added_book_not_added_book(self, collector):

        book = 'A not added book'
        collector.add_book_in_favorites(book)

        assert book not in collector.favorites and len(collector.favorites) == 0

    def test_delete_book_from_favorites_delete_of_1_to_5_books_deleted_books(self, collector):
        collector.favorites = ['Книга_1', 'Книга_2', 'Книга_3', 'Книга_4', 'Книга_5']

        expected_favorite_books = collector.favorites[:]
        for book in collector.favorites:
            collector.delete_book_from_favorites(book)
            expected_favorite_books.remove(book)

            assert sorted(expected_favorite_books) == sorted(collector.favorites)

    def test_delete_book_from_favorites_delete_deleted_book_favorites_not_changed(self, collector):
        collector.favorites = ['Книга_1', 'Книга_2', 'Книга_3', 'Книга_4', 'Книга_5']

        del_book = random.choice(collector.favorites)
        collector.delete_book_from_favorites(del_book)

        expected_favorite_books = collector.favorites[:]

        collector.delete_book_from_favorites(del_book)

        assert collector.favorites == expected_favorite_books

    def test_delete_book_from_favorites_delete_not_favorite_book_favorites_not_changed(self, collector):
        collector.favorites = ['Книга_1', 'Книга_2', 'Книга_3', 'Книга_4', 'Книга_5']
        expected_favorite_books = collector.favorites[:]

        del_book = 'A not favorite book'
        collector.delete_book_from_favorites(del_book)

        assert collector.favorites == expected_favorite_books

    def test_delete_book_from_favorites_delete_not_added_book_favorites_not_changed(self, collector):
        collector.favorites = ['Книга_1', 'Книга_2', 'Книга_3', 'Книга_4', 'Книга_5']
        expected_favorite_books = collector.favorites[:]

        del_book = 'A not added book'
        collector.delete_book_from_favorites(del_book)

        assert collector.favorites == expected_favorite_books

    @pytest.mark.parametrize('favorite_books', [
        [],
        ['Книга_1'],
        ['Книга_1', 'Книга_2'],
        ['Книга_1', 'Книга_2', 'Книга_3', 'Книга_4', 'Книга_5']
    ])
    def test_get_list_of_favorites_books_get_0_and_1_and_2_and_5books_got_books(self, collector, favorite_books):
        collector.favorites = favorite_books

        assert sorted(collector.favorites) == sorted(collector.get_list_of_favorites_books())
