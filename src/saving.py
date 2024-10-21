import json
from abc import ABC, abstractmethod


class FileVacancy(ABC):
    @abstractmethod
    def add_vacancy_to_file(self, vacancy):
        pass

    @abstractmethod
    def get_vacancy_by_request(self, request):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(FileVacancy):

    def add_vacancy_to_file(self, vacancy):
        try:
            with open("data/vacancies.json", "r", encoding="utf-8") as file:
                vacancies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []

        vacancies.append(vacancy.__dict__)

        with open("data/vacancies.json", "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)

    def get_vacancy_by_request(self, request):
        try:
            with open("data/vacancies.json", "r", encoding="utf-8") as file:
                vacancies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            vacancies = []

        vacancies = [vacancy for vacancy in vacancies if request in vacancy['name']]
        return vacancies

    def delete_vacancy(self, vacancy):
        try:
            with open("data/vacancies.json", "r", encoding="utf-8") as file:
                vacancies = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Файл с вакансиями не найден или поврежден.")
            return

        vacancies = [i for i in vacancies if i != vacancy.__dict__]

        with open("data/vacancies.json", "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
