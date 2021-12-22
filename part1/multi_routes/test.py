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
        

    def test_main_page(self):
        url_answers = {
            "/all/": "1240 60 230 20 310", 
            "/max/": "1240", 
            "/min/": "20",
            "/avg/": "372"
        }
        for key, value in url_answers.items():
            response = self.student_app_get(key)
            self.assertTrue(
                response.status_code ==  self.expected_code,
                f"%@Проверьте, что адрес 127.0.0.1:5000'{key}' доступен из браузера"
            )
            soup = BeautifulSoup(response.data, features="html.parser")
            self.assertTrue(
                soup.text == value,
                f"%@Проверьте, что при переходе на страницу {key} выводится правильный текст"
            )
        


if __name__ == "__main__":
    unittest.main()