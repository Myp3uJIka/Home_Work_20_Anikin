from unittest.mock import MagicMock

import pytest as pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService


@pytest.fixture
def test_objects_directors():
    dir_1 = Director(id=1, name="Юрий Быков")
    dir_2 = Director(id=2, name="Роман Прыгунов")
    dir_3 = Director(id=3, name="Дмитрий Тюрин")
    directors = [dir_1, dir_2, dir_3]

    DirectorDAO.get_all = MagicMock(return_value=directors)
    DirectorDAO.get_one = MagicMock(return_value=dir_1)
    DirectorDAO.create = MagicMock()
    DirectorDAO.delete = MagicMock()
    DirectorDAO.update = MagicMock(return_value=dir_2)

    return DirectorDAO


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, test_objects_directors):
        self.director_service = DirectorService(dao=test_objects_directors)

    def test_dir_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0, "Вывести данные из таблицы (directors) не удаётся."

    def test_dir_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None, "Получить указанную запись (director) не удаётся."

    def test_dir_create(self):
        new_dir = {id: 4, 'name': "new_name"}
        result = self.director_service.create(new_dir)
        assert result is not None, "Добавить запись (director) не удаётся."

    def test_dir_delete(self):
        result = self.director_service.delete(3)
        assert result is None, "Удалить запись (director) не удаётся."

    def test_dir_update(self):
        director = {'id': 2, 'name': "renamed"}
        result = self.director_service.update(director)
        assert result is not None, "Обновить запись (director) не удаётся."

