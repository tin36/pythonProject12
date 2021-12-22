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
        main.order = ["Греческий салат", "Суп с грибами", "Лазанья", "Вишневый пирог"]
        self.categories = ["салаты", "супы", "основные блюда", "десерты"]
        self.app = main.app.test_client()
    
    def test_cats_page(self):
        main_tag = self.check_code_and_get_soup(f"/cats/", 200).main
        all_lists = main_tag.find_all('li')
        
        for li, ord, category in zip(all_lists, main.order, self.categories):
            self.assertTrue(
                li.text == ord,
                f"%@Проверьте правильно ли в вашем шаблоне отображается категория {category}"
            )


if __name__ == "__main__":
    unittest.main()