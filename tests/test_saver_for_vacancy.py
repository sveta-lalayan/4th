# import unittest
# from unittest.mock import patch, MagicMock
# from src.saver_for_vacancy import JSONVacancySaver
# from src.vacancy import Vacancy
#
# class TestJSONVacancySaver(unittest.TestCase):
#     def setUp(self):
#         self.saver = JSONVacancySaver()
#
#     def test_add_vacancy(self):
#         vacancy = Vacancy("Test Vacancy", "https://example.com", "100000", "Test responsibility")
#         self.saver.add_vacancy(vacancy)
#         self.assertEqual(len(self.saver.vacancies), 1)
#         self.assertIn(vacancy.name, [v['name'] for v in self.saver.vacancies])
#
#     def test_add_vacancy_invalid_type(self):
#         with self.assertRaises(ValueError):
#             self.saver.add_vacancy("Not a Vacancy object")
#
#     def test_add_vacancies_to_json(self):
#         vacancy1 = Vacancy("Test Vacancy 1", "https://example.com", "100000", "Test responsibility 1")
#         vacancy2 = Vacancy("Test Vacancy 2", "https://example.com", "200000", "Test responsibility 2")
#         self.saver.add_vacancy(vacancy1)
#         self.saver.add_vacancy(vacancy2)
#         self.saver.add_vacancies_to_json()
#         with open(self.saver.file_with_vacancies, 'r') as file:
#             data = json.load(file)
#             self.assertEqual(len(data), 2)
#             self.assertIn(vacancy1.name, [v['name'] for v in data])
#             self.assertIn(vacancy2.name, [v['name'] for v in data])
#
#     def test_get_vacancy(self):
#         vacancy = Vacancy("Test Vacancy", "https://example.com", "100000", "Test responsibility")
#         self.saver.add_vacancy(vacancy)
#         retrieved_vacancy = self.saver.get_vacancy(vacancy.name, vacancy.url)
#         self.assertIsInstance(retrieved_vacancy, Vacancy)
#         self.assertEqual(retrieved_vacancy.name, vacancy.name)
#
#     def test_get_vacancy_not_found(self):
#         self.assertIsNone(self.saver.get_vacancy("Non-existent vacancy", "https://example.com"))
#
#     def test_delete_vacancy(self):
#         vacancy = Vacancy("Test Vacancy", "https://example.com", "100000", "Test responsibility")
#         self.saver.add_vacancy(vacancy)
#         self.saver.delete_vacancy(vacancy)
#         self.assertEqual(len(self.saver.vacancies), 0)
#         with open(self.saver.file_with_vacancies, 'r') as file:
#             data = json.load(file)
#             self.assertEqual(len(data), 0)
#
#     @patch('builtins.open', new_callable=MagicMock)
#     def test_delete_vacancy_file_not_found(self, mock_open):
#         vacancy = Vacancy("Test Vacancy", "https://example.com", "100000", "Test responsibility")
#         self.saver.add_vacancy(vacancy)
#         mock_open.side_effect = FileNotFoundError()
#         with self.assertRaises(FileNotFoundError):
#             self.saver.delete_vacancy(vacancy)
#
# if __name__ == '__main__':
#     unittest.main()