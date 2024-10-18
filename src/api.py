from abc import ABC, abstractmethod

import requests


class ApiService(ABC):

    @abstractmethod
    def get_vacancies(self, search_request):
        pass


class HeadHunterAPI(ApiService):
    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_request: str):
        params = {"text": search_request, "per_page": 20}
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response
        else:
            raise Exception(f"Ошибка подключения: {response.status_code}")
