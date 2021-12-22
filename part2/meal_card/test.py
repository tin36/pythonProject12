import sys
import unittest
from pathlib import Path
from bs4 import BeautifulSoup
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
        main_tag = self.check_code_and_get_soup("/meal/", 200).main
        h2 = main_tag.h2
        self.assertIsNotNone(
            h2,
            "%@Проверьте, что тег main содержит заголовок h2"
        )
        self.assertTrue(
            h2.text == "Название: Пицца с ананасами",
            "%@Проверьте что в заголовке h2 правильно передан текст"
        )
        paragraphs = main_tag.p
        self.assertIsNotNone(
            paragraphs,
            "%@Проверьте, что тег main содержит абзацы"
        )
        expected = {
            0: [("Цена: 690")],
            1: [("Вес: 400")],
        }
        expected_len = len(expected)
        paragraphs = main_tag.find_all('p', recursive=False)
        current_len = len(paragraphs)
        self.assertEqual(
            current_len, expected_len,
            (f"%@Проверьте, что добавили все абзацы. У Вас их {current_len}, "
             f"тогда как должно быть {expected_len}"))


        for paragraph, index in zip(paragraphs, range(len(expected))):
            self.assertEqual(
                paragraph.text, expected.get(index)[0],
                f"%@Проверьте, правильный ли текст в абзаце {index+1}")

   
        


if __name__ == "__main__":
    unittest.main()