import requests
from abc import ABC, abstractmethod



class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""

    @abstractmethod
    def _connect(self) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, keyword: str, per_page: int = 20):
        pass


class HeadHunterAPI(AbstractAPI):
    """Класс для работы с hh.ru"""

    def __init__(self):
        self.__base_url = "https://api.hh.ru/vacancies"

    def _connect(self) -> None:
        """Метод получения запроса"""
        response = requests.get(self.__base_url)
        if response.status_code != 200:
            raise Exception("Не удалось подключиться к API")

    def get_vacancies(self, keyword: str, per_page: int = 20):
        """Метод получения вакансий по ключевому слову"""
        self._connect()
        params = {"text": keyword, "per_page": per_page}
        response = requests.get(self.__base_url, params=params)
        return response.json().get("items", [])
