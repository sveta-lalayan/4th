import pytest
from src.utils import top_n_vacancies, filter_vacancies
from src.vacancy import Vacancy
from universal_root_path import ROOT_DIR


#@pytest.fixture()
#def vacancies_list():
#    vac1 = Vacancy('python', 'anything', 123, 'hard-working')
 #   vac2 = Vacancy('java', 'anything', 125, 'not hard-working')
  #  vac3 = Vacancy('flusk', 'anything', 128, 'really hard-working')
   # playlist_v = [vac1, vac2, vac3]
    #return playlist_v


vac1 = Vacancy('python', 'anything', {'from':10, 'to':100}, '-working')
vac2 = Vacancy('java', 'anything', {'from':5, 'to':90}, 'not hard-working')
vac3 = Vacancy('flusk', 'anything', {'from':1, 'to':80}, 'really hard-working')
playlist_v = [vac1, vac2, vac3]


def test_top_n_vacancies():
    data = playlist_v

    expected = [vac1,vac2]
    expected_1 = playlist_v
    assert top_n_vacancies(2, data) == expected
    assert top_n_vacancies(20, data) == expected_1

# def test_top_n_vacancies_1():
#     data = playlist_v
#
#     expected = [vac1,vac2]
#
#     assert top_n_vacancies(2, data) == expected


def test_filter_vacancies():
    data = playlist_v

    expected = [vac1,vac2,vac3]

    assert filter_vacancies('hard', data) == expected

def test_filter_vacancies_1():
    data = playlist_v

    expected = [vac1,vac2,vac3]

    assert filter_vacancies('', data) == expected


#pytest --cov=путь_к_вашему_проекту --cov-report=html


