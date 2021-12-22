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

    def test_get_query_param_page(self):
        soup = self.check_code_and_get_soup("/discounts/", 200)
        html_div = soup.div
        self.assertIsNotNone(
            html_div,
            "%@Проверьте, что правильно добавили блоки (div) в тег main"
        )
        html_div_list = soup.main.find_all('div')
        ln_div_list = len(html_div_list)
        self.assertEqual(
            ln_div_list, 2,
            ("%@Проверьте, что у Вас правильное"
             f" количество блоков. У Вас {ln_div_list},"
             " тогда как должно быть 2.")
        )
        tags = {
            'h3':'заголовок 3 уровня',
            'p': 'абзаицы'}
        
        expected_headers = {
            1: "Треть на доставку",
            2: "Цены пополам"
        }

        for div, index in zip(html_div_list, range(2)):
            for key in tags.keys():
                value = tags.get(key)
                self.assertIsNotNone(
                    getattr(div, key), f"%@Проверьте что {index+1} блок содержит {value}"
                )
            expected_text = expected_headers.get(index+1)
            self.assertTrue(
                div.h3.text == expected_text,
                f"%@Проверьте что заголовок h3 в {index+1} блоке содержит текст {expected_text}"
            )
            paragraphs = div.find_all('p')
            self.assertIsNotNone(
                paragraphs,
                "%@Проверьте, что все теги div содержит абзацы"
            )
            expected = {
                0:{0: "Скидка: 30",
                   1: "Код: minidelivery",
                   },
                1:{0: "Скидка: 50",
                   1: "Код: halflings"
                   }
                }
            expected_len = len(expected)
            current_len = len(paragraphs)
            self.assertEqual(
                current_len, expected_len,
                (f"%@Проверьте, что добавили все абзацы. У Вас их {current_len}, "
                 f"тогда как должно быть {expected_len}"))
    
    
            for paragraph, index_p in zip(paragraphs, range(len(expected))):
                self.assertEqual(
                    paragraph.text, expected.get(index).get(index_p),
                    f"%@Проверьте, правильный ли текст в блоке {index+1}")



if __name__ == "__main__":
    unittest.main()