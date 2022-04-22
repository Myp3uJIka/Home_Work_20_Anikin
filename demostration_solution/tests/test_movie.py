from unittest.mock import MagicMock

import pytest as pytest

from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.movie import MovieService


@pytest.fixture
def test_objects_movies():
    movie_1 = Movie(id=1, title="Майор", description="", trailer="", year="2013", rating=7.5, genre_id=1, director_id=1)
    movie_2 = Movie(id=2, title="Духless", description="", trailer="", year="2011", rating=6.6, genre_id=1, director_id=2)
    movie_3 = Movie(id=3, title="Триггер", description="", trailer="", year="2020", rating=8.4, genre_id=2, director_id=3)
    movies = [movie_1, movie_2, movie_3]

    MovieDAO.get_all = MagicMock(return_value=movies)
    MovieDAO.get_one = MagicMock(return_value=movie_1)
    MovieDAO.create = MagicMock()
    MovieDAO.update = MagicMock(return_value=movie_2)
    MovieDAO.delete = MagicMock()

    return MovieDAO


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, test_objects_movies):
        self.movie_service = MovieService(dao=test_objects_movies)

    def test_movie_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_movie_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None

    def test_movie_create(self):
        new_movie = {
            'id': 4,
            'title': "new movie",
            'description': "",
            'trailer': "",
            'year': "",
            'rating': None,
            'genre_id': None,
            'director_id': None
        }
        result = self.movie_service.create(new_movie)
        assert result is not None

    def test_movie_update(self):
        mod_movie = {
            'id': 2,
            'title': "modificated title",
            'description': "",
            'trailer': "",
            'year': "",
            'rating': None,
            'genre_id': None,
            'director_id': None
        }
        result = self.movie_service.update(mod_movie)
        assert result is not None

    def test_movie_delete(self):
        result = self.movie_service.delete(3)
        assert result is None

