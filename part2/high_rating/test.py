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

    def test_main_page(self):
        main_tag = self.check_code_and_get_soup("/rest_rating/", 200).main
        ul_tag = main_tag.ul
        self.assertIsNotNone(
            ul_tag,
            "%@Проверьте, что тег main содержит маркированный список (тег ul)"
        )
        expected = {
            0: [("Борис 5.0")],
            1: [("Цоколь 4.9")],
            2: [("Геральт 4.7")],
        }
        expected_len = len(expected)
        paragraphs = ul_tag.find_all('li', recursive=False)
        current_len = len(paragraphs)
        self.assertEqual(
            current_len, expected_len,
            (f"%@Проверьте, что добавляются все элементы списка'. У Вас их {current_len}, "
             f"тогда как должно быть {expected_len}"))


        for paragraph, index in zip(paragraphs, range(len(expected))):
            self.assertEqual(
                paragraph.text, expected.get(index)[0],
                f"%@Проверьте, правильный ли текст содержит элемент {index+1}")

if __name__ == "__main__":
    unittest.main()