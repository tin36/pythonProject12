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
        statuses = {
            1: "заказ принят",
            2: "заказ готовится",
            3: "заказ в пути",
            4: "заказ доставлен",
            5: "заказ отменен",
        }
        for sid in range(1, 6):
            p_tag = self.check_code_and_get_soup(f"/getstatus/{sid}", 200).p
            self.assertIsNotNone(
                p_tag,
                "%@Проверьте, что тег main содержит абзац"
            )

        self.assertTrue(
            p_tag.text == statuses.get(sid),
            f"%@Проверьте что в заголовке p правильно передан текст при запросе на адрес /getstatus/{sid}"
        )


if __name__ == "__main__":
    unittest.main()