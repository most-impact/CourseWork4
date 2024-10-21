from src.api import HeadHunterAPI
from src.saving import JSONSaver
from src.vacancies import Vacancy


# Function for user interaction
def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    salary_range = list(
        map(int, input("Введите диапазон зарплат (через тире или пробел): ").split())
    )

    dict_with_vacancies = hh_api.get_vacancies(search_query)
    list_with_vacancies = [
        Vacancy.new_vacancy(vacancy) for vacancy in dict_with_vacancies["items"]
    ]
    ranged_vacancies = Vacancy.get_vacancies_by_salary(
        list_with_vacancies, salary_range
    )
    sorted_vacancies = Vacancy.sort_vacancies(ranged_vacancies)
    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)
    Vacancy.print_vacancies(top_vacancies)

    json_saver = JSONSaver()
    for vacancy in top_vacancies:
        json_saver.add_vacancy_to_file(vacancy)


if __name__ == "__main__":
    user_interaction()
