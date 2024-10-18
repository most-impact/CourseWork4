class Vacancy:

    def __init__(self, vacancy, link_to_vacancy, salary, description):
        self.__description = description
        self.__link_to_vacancy = link_to_vacancy
        self.__salary = salary
        self.__vacancy = vacancy

    @property
    def vacancy(self):
        return self.__vacancy

    @vacancy.setter
    def vacancy(self, vacancy):
        self.__vacancy = vacancy

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary < 0 or salary is None:
            self.__salary = 0
        else:
            self.__salary = salary

    @property
    def link_to_vacancy(self):
        return self.__link_to_vacancy

    @link_to_vacancy.setter
    def link_to_vacancy(self, link_to_vacancy):
        self.__link_to_vacancy = link_to_vacancy

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    def __str__(self):
        return f"{self.__vacancy} - {self.__salary}"

    @staticmethod
    def cast_to_object_list(vacancies):
        return vacancies.json()["items"]
