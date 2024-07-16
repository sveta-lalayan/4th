class Vacancy:
    """ Это класс для обработки вакансии"""

    @classmethod
    def cast_to_object_list(cls, vacancies_list: list) -> list:
        """Класс-метод для создания списка объектов Vacancy из списка вакансий в формате JSON"""

        vacancies_object_list = []

        for vacancy in vacancies_list:
            vacancy_object = cls(vacancy['name'], vacancy['url'], vacancy['salary'],
                                 vacancy['snippet']['responsibility'])

            vacancies_object_list.append(vacancy_object)

        return vacancies_object_list

    def __init__(self, name: str, url: str, salary: dict, responsibility: str):
        """Конструктор класса Vacancy"""

        if not name:
            raise ValueError("Нужно указать вакансию")
        self.name = name

        if not url:
            raise ValueError("Должен быть указан URL")
        self.url = url

        if not salary:
            self.__salary = {"from": 0, "to": 0}
        elif not salary.get('to') and not salary.get('from'):
            self.__salary = {"from": 0, "to": 0}
        elif not salary.get('to'):
            self.__salary = {"from": salary['from']}
        elif not salary.get('from'):
            self.__salary = {"from": 0, "to": salary['to']}
        else:
            self.__salary = {"from": salary['from'], "to": salary['to']}

        if not responsibility or responsibility == 'None':
            self.responsibility = 'Описание не указано'
        else:
            self.responsibility = responsibility

    @property
    def get_salary(self) -> dict:
        """Геттер для зарплаты"""

        return self.__salary

    def __eq__(self, other):
        """Магический метод для сравнения 'равно' зарплат"""

        return self.__salary['from'] == other.get_salary['from']

    def __ne__(self, other):
        """Магический метод для сравнения 'неравно' зарплат"""

        return self.__salary['from'] != other.get_salary['from']

    def __lt__(self, other):
        """Магический метод для сравнения 'меньше' зарплат"""

        return self.__salary['from'] < other.get_salary['from']

    def __gt__(self, other):
        """Магический метод для сравнения 'больше' зарплат"""

        return self.__salary['from'] > other.get_salary['from']

    def __le__(self, other) -> bool:
        """Магический метод для сравнения 'меньше или равно' зарплат"""

        return self.__salary['from'] <= other.get_salary['from']

    def __ge__(self, other) -> bool:
        """Магический метод для сравнения 'больше или равно' зарплат"""

        return self.__salary['from'] >= other.get_salary['from']

    def __repr__(self) -> str:
        """Магический метод для отображения созданного экземпляра класса Vacancy"""

        return f"Vacancy('{self.name}', '{self.url}', {self.__salary}, '{self.responsibility}')"

    def __str__(self):
        if self.__salary['from'] != 0 and self.__salary.get('to') != 0 and self.__salary.get('to') is not None:
            return f"Название: {self.name}, зарплата: {self.__salary['from']} - {self.__salary['to']}, " \
                   f"описание: {self.responsibility}\nСсылка: {self.url}"
        elif self.__salary['from'] == 0 and self.__salary.get('to') != 0:
            return f"Название: {self.name}, зарплата до {self.__salary['to']}, " \
                   f"описание: {self.responsibility}\nСсылка: {self.url}"
        elif self.__salary.get('to') is None and self.__salary['from'] != 0:
            return f"Название: {self.name}, зарплата от {self.__salary['from']}, " \
                   f"описание: {self.responsibility}\nСсылка: {self.url}"
        else:
            return f"Название: {self.name}, зарплата не указана :(, " \
                   f"описание: {self.responsibility}\nСсылка: {self.url}"