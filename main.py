from src.api import HeadHunterAPI
from src.fileVacancy import JSONSaver
from src.vacancies import Vacancy


def filter_vacancies(filtering_list, filter_words):
    result = []
    if filter_words:
        for vacancy in filtering_list:
            for word in filter_words:
                if word.lower() in vacancy.description.lower():
                    result.append(vacancy)
    else:
        result = filtering_list
    return result


def get_vacancies_by_salary(filtered_vacancies, salary_range):
    result = []
    for vacancy in filtered_vacancies:
        if vacancy["salary"] is not None and vacancy["salary"]["from"] is not None:
            if salary_range[0] <= vacancy["salary"]["from"] <= salary_range[1]:
                result.append(vacancy)
    return result


def sort_vacancies(ranged_vacancies):
    return sorted(ranged_vacancies, key=lambda x: x['salary']['from'])


def get_top_vacancies(sorted_vacancies, top_n):
    return sorted_vacancies[:top_n]


def print_vacancies(top_vacancies):
    for i in top_vacancies:
        print(i)


# Function for user interaction
def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = list(
        map(int, input("Введите диапазон зарплат (через тире или пробел): ").split())
    )

    list_with_vacancies = Vacancy.cast_to_object_list(hh_api.get_vacancies(search_query))

    filtered_vacancies = filter_vacancies(list_with_vacancies, filter_words)

    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)

    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
