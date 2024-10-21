import pytest

from src.vacancies import Vacancy


@pytest.fixture
def vacancy1():
    return Vacancy(
        "Инженер-тестировщик ПО 1 / Middle QA-engineer",
        {"from": 150000, "to": None, "currency": "RUR", "gross": True},
        "Опыт работы QA - не менее 3х лет.",
        "Москва",
    )


@pytest.fixture
def vacancy2():
    return Vacancy(
        "Инженер-тестировщик ПО 2 / Middle QA-engineer",
        {"from": 200000, "to": None, "currency": "RUR", "gross": True},
        "Опыт работы QA - не менее 3х лет.",
        "Москва",
    )


def test_vacancy(vacancy1, vacancy2):
    with pytest.raises(TypeError):
        vacancy1.salary = "йоу"

    assert Vacancy.get_vacancies_by_salary([vacancy1, vacancy2], [100000, 180000]) == [
        vacancy1
    ]
    assert Vacancy.sort_vacancies([vacancy1, vacancy2]) == [vacancy2, vacancy1]
    assert Vacancy.get_top_vacancies([vacancy1, vacancy2], 2) == [vacancy1, vacancy2]
