import sys
import unittest
from pathlib import Path
import os
import main

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402
from ttools.skyprotests.tests_mixins import TemplateMixin


class SettingsTestCase(SkyproTestCase, TemplateMixin):
    def setUp(self):
        self.app = main.app.test_client()

    def test_get_query_param_page(self):
        soup = self.check_code_and_get_soup("/search/", 200)
        self.assertTrue(
            soup.text == "Введите параметр meal",
            "%@Проверьте что если параметр не задан, то отрображается ожидаемая строка"
        )
    def test_meal_not_found(self):
        soup = self.check_code_and_get_soup("/search/?meal=qwe", 200)
        self.assertTrue(
            soup.text == "Блюд не найдено",
            "%@Проверьте что если блюд не найдено, то отрображается ожидаемая строка"
        )
    def test_meal_search(self):
        main_tag = self.check_code_and_get_soup("/search/?meal=пи", 200).main
        h2 = main_tag.h2
        self.assertIsNotNone(
            h2,
            "%@Проверьте, что тег main содержит заголовок"
        )
        self.assertTrue(
            h2.text == "Найдено: 5",
            ("%Проверьте что, надпись в заголовке h2 отображается верно, а также правильно "
             "считается количество найденных блюд")
        )
        html_list_numbers = main_tag.ul
        self.assertIsNotNone(
            html_list_numbers,
            "%@Проверьте, что добавили тег 'Маркированный список'")
        li_elements = html_list_numbers.find_all('li')
        len_elements = len(li_elements)
        self.assertEqual(
            len_elements, 5,
            ("%@Проверьте что добавляются все элементы списка."
             f" Должно быть 5, тогда как у вас {len_elements}"))


if __name__ == "__main__":
    unittest.main()