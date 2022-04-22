from unittest.mock import MagicMock

import pytest as pytest

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService


@pytest.fixture
def test_objects_genres():
    genre_1 = Genre(id=1, name="Драма")
    genre_2 = Genre(id=2, name="Триллер")
    genres = [genre_1, genre_2]

    GenreDAO.get_all = MagicMock(return_value=genres)
    GenreDAO.get_one = MagicMock(return_value=genre_1)
    GenreDAO.create = MagicMock()
    GenreDAO.update = MagicMock(return_value=genre_2)
    GenreDAO.delete = MagicMock()

    return GenreDAO

class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, test_objects_genres):
        self.genre_service = GenreService(dao=test_objects_genres)

    def test_genre_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_genre_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None

    def test_genre_create(self):
        new_genre = {"id": 4, "name": "new_genre"}
        result = self.genre_service.create(new_genre)
        assert result is not None

    def test_genre_update(self):
        mod_genre = {'id': 2, 'name': 'modificated name'}
        result = self.genre_service.update(mod_genre)
        assert result is not None

    def test_genre_delete(self):
        result = self.genre_service.delete(3)
        assert result is None
