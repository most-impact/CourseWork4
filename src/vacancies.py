class Vacancy:

    def __init__(self, name, salary, snippet, area):
        self.__name = name
        self.__salary = salary
        self.__snippet = snippet
        self.__area = area

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if type(salary) is int or salary < 0:
            self.__salary = 0
        else:
            self.__salary = salary

    @property
    def snippet(self):
        return self.__snippet

    @snippet.setter
    def snippet(self, snippet):
        self.__snippet = snippet

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, area):
        self.__area = area

    def __str__(self):
        return f"{self.__name} - {self.__salary['to']}"

    @classmethod
    def new_vacancy(cls, vacancy_info):
        return cls(
            vacancy_info["name"],
            vacancy_info["salary"],
            vacancy_info["snippet"]["requirement"],
            vacancy_info["area"]["name"],
        )

    @staticmethod
    def get_vacancies_by_salary(filtered_vacancies, salary_range):
        result = []
        for vacancy in filtered_vacancies:
            if vacancy.salary is not None and vacancy.salary["from"] is not None:
                if salary_range[0] <= vacancy.salary["from"] <= salary_range[1]:
                    result.append(vacancy)
        return result

    @staticmethod
    def sort_vacancies(ranged_vacancies):
        return sorted(
            ranged_vacancies, key=lambda vacancy: vacancy.salary["from"], reverse=True
        )

    @staticmethod
    def get_top_vacancies(sorted_vacancies, top_n):
        return sorted_vacancies[:top_n]

    @staticmethod
    def print_vacancies(top_vacancies):
        for i in top_vacancies:
            print(i)
