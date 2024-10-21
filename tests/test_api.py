import pytest

from src.api import ApiService, HeadHunterAPI


def test_hh_api():
    hh_api = HeadHunterAPI()
    assert hh_api.url == "https://api.hh.ru/vacancies"
    assert type(hh_api.get_vacancies("разработчик")) == dict

    hh_api.url = "qwerty"
    with pytest.raises(Exception):
        hh_api.get_vacancies("разработчик")

    assert isinstance(hh_api, HeadHunterAPI)
    assert issubclass(HeadHunterAPI, ApiService)
