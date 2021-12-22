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
        self.expected_code = 200
        

    def test_main_page(self):
        url = "/"
        response = self.student_app_get(url)
        self.assertTrue(
            response.status_code ==  self.expected_code,
            f"%@Проверьте, что адрес 127.0.0.1:5000'{url}' доступен из браузера"
        )
        soup = BeautifulSoup(response.data, features="html.parser")
        header = soup.h1
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 1 уровня на главную страницу.")
        self.assertEqual(
            header.text, 'Главная страница',
            "%@Проверьте что заголовок 1 уровня содержит правильный текст")
        
        html_paragraph = soup.p
        self.assertIsNotNone(
            html_paragraph,
            "%@Проверьте, что главная страница содержит тег абзац")
        p_elements = soup.find_all('p')
        len_elements = len(p_elements)
        self.assertEqual(
            len_elements, 2,
            ("%@Проверьте что добавили 2 абзаца на главную страницу."
             f" Должно быть 2, тогда как у вас {len_elements}"))
        for element in p_elements:
            self.assertIsNotNone(
                element.a,
                "%@Проверьте, что в ваши абзацах содержатся теги со ссылками"
            )
            href = element.a.attrs.get('href')
            self.assertIsNotNone(
                href,
                "%@Проверьте что ваши ссылки имеют аттрибут href"
            )
            self.assertIn(
                href, ['/courses/', '/students/'],
                "Проверьте, что главная страница имеет необходимые ссылки"
            )

    def test_courses_page(self):
        url = "/courses/"
        response = self.student_app_get(url)
        self.assertTrue(
            response.status_code ==  self.expected_code,
            f"%@Проверьте, что адрес 127.0.0.1:5000'{url}' доступен из браузера"
        )
        soup = BeautifulSoup(response.data, features="html.parser")
        header = soup.h1
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 1 уровня на страницу с курсами.")
        self.assertEqual(
            header.text, 'Наши курсы',
            "%@Проверьте что заголовок 1 уровня на странице с курсами содержит правильный текст")
        
        html_paragraph = soup.p
        self.assertIsNotNone(
            html_paragraph,
            "%@Проверьте, что страница с курсами содержит тег абзац")
        self.assertIsNotNone(
            html_paragraph.a,
            "%@Проверьте, что в абзаце на странице с курсами содержится тег со ссылкой"
        )
        href = html_paragraph.a.attrs.get('href')
        self.assertIsNotNone(
            href,
            "%@Проверьте что ваша ссылка на странице с курсами имеет аттрибут href"
        )
        self.assertTrue(
            href == '/',
            "Проверьте, что страница с курсами имеет ссылку на главную страницу"
        )
        html_list = soup.ul
        self.assertIsNotNone(
            html_list,
            "%@Проверьте, что добавили тег 'маркированный список' на страницу с курсами")
        li_elements = html_list.find_all('li')
        len_elements = len(li_elements)
        self.assertEqual(
            len_elements, 3,
            ("%@Проверьте что добавили все элементы списка."
             f" Должно быть 3, тогда как у вас {len_elements}"))
        courses = [
            'Статистика',
            'Мехатроника',
            'Аналитика данных',
        ]
        for element, course, index in zip(li_elements, courses, range(3)):
            self.assertTrue(
            element.text == course,
                f"%@Проверьте, что {index+1} элемент списка имеет верное значение")


    def test_students_page(self):
        url = "/students/"
        response = self.student_app_get(url)
        self.assertTrue(
            response.status_code ==  self.expected_code,
            f"%@Проверьте, что адрес 127.0.0.1:5000'{url}' доступен из браузера"
        )
        soup = BeautifulSoup(response.data, features="html.parser")
        header = soup.h1
        self.assertIsNotNone(
            header,
            "%@Проверьте, что добавили заголовок 1 уровня на страницу со студентами.")
        self.assertEqual(
            header.text, 'Наши студенты',
            "%@Проверьте что заголовок 1 уровня на странице с курсами содержит правильный текст")
        
        html_paragraph = soup.p
        self.assertIsNotNone(
            html_paragraph,
            "%@Проверьте, что страница со студентами содержит тег абзац")
        self.assertIsNotNone(
            html_paragraph.a,
            "%@Проверьте, что в абзаце на странице со студентами содержится тег со ссылкой"
        )
        href = html_paragraph.a.attrs.get('href')
        self.assertIsNotNone(
            href,
            "%@Проверьте что ваша ссылка на странице с курсами имеет аттрибут href"
        )
        self.assertTrue(
            href == '/',
            "Проверьте, что страница с курсами имеет ссылку на главную страницу"
        )
        html_list = soup.ul
        self.assertIsNotNone(
            html_list,
            "%@Проверьте, что добавили тег 'маркированный список' на страницу со студентами")
        li_elements = html_list.find_all('li')
        len_elements = len(li_elements)
        self.assertEqual(
            len_elements, 3,
            ("%@Проверьте что добавили все элементы списка."
             f" Должно быть 3, тогда как у вас {len_elements}"))
        courses = [
            'Чаурина Луиза',
            'Доценко Ефросинья',
            'Ичёткин Епифан',
        ]
        for element, course, index in zip(li_elements, courses, range(3)):
            self.assertTrue(
            element.text == course,
                f"%@Проверьте, что {index+1} элемент списка имеет верное значение")

if __name__ == "__main__":
    unittest.main()