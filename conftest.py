import random
import pytest
from main import BooksCollector


DEFAULT_BOOK_GENRE = {}
DEFAULT_FAVORITES = []
DEFAULT_GENRE = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
DEFAULT_GENRE_AGE_RATING = ['Ужасы', 'Детективы']


@pytest.fixture
def default_collector():
    """ Возвращает пустой(дефолтный) коллектор """
    default_collector = BooksCollector()
    return default_collector


@pytest.fixture
def collector(default_collector, n=5+1):
    """
        Возвращает коллектор заполненный книгами формата {книга_ее номер}:{случайный жанр из списка жанров}
        Размер коллектора задается параметров n, по умолчанию размер равен 5
    """
    default_collector.books_genre = {f'Книга_{i}': random.choice(default_collector.genre + [''])
                                     for i in range(1, n + 1)}
    return default_collector
