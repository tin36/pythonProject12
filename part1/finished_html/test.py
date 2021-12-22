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
from ttools.skyprotests.tests_mixins import ResponseTestsMixin

class SettingsTestCase(SkyproTestCase, ResponseTestsMixin):
    def setUp(self):
        self.app = main.app.test_client()
        self.student_app_get = self.app.get
        self.url = "/"
        self.expected_code = 200
        

    def test_client_post_get_token_with_valid_data(self):
        answers = {
            "/": "Главная страничка",
            "/catalog/": "Страничка каталога",
            "/settings/": "Страничка настроек",
        }
        for key in answers.keys():
            response = self.student_app_get(key)
            self.assertTrue(
                response.status_code ==  self.expected_code,
                f"%@Проверьте, что адрес {key} доступен из браузера"
            )
        for key, value in answers.items():
            response = self.student_app_get(key)
            soup = BeautifulSoup(response.data)
            self.assertIsNotNone(
                soup.h1,
                (f"%@Проверьте что на странице '{key}' вы использовали "
                 "тег заголовка первого уровня")
            )
            self.assertTrue(
                soup.h1.text == value,
                (f"%@Проверьте, что при запросе на адрес {key}"
                 f" возвращается правильная надпись {value}")
            )
        
        


if __name__ == "__main__":
    unittest.main()