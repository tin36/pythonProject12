# В данном задании вам необходимо 
# создать фласк приложение, с тремя html-страницами
# связаннами между собой ссылками.
# Для этого вам потребуется использовать в коде
# язык разметки htlm.
# Адреса и содержание страниц оформите следующим образом:
#
# 1. Адрес страницы: 127.0.0.1:5000
# - Заголовок первого уровня: "Главная страница"
# - абзац со ссылкой на страницу /students/ и текстом "Наши студенты"
# - абзац cо ссылкой на страницу /courses/ и текстом "Наши курсы"
#
# 2. Адрес страницы: 127.0.0.1:5000/students/
# - Заголовок первого уровня: "Наши студенты"
# - Маркированный список с элементами:
#       "Чаурина Луиза"
#       "Доценко Ефросинья"
#       "Ичёткин Епифан"
# - абзац cо ссылкой на страницу "/"" и текстом "Вернуться на главную"
#
# 3. Адрес страницы: 127.0.0.1:5000/courses/
# - Заголовок первого уровня: "Наши курсы"
# - Маркированный список с элементами:
#       "Статистика"
#       "Мехатроника"
#       "Аналитика данных"
# - абзац cо ссылкой на страницу "/"" и текстом "Вернуться на главную"
#
from flask import Flask
app = # TODO инициализируйте приложение фласк здесь

# TODO напишите view-функции здесь

if __name__=="__main__":
    app.run()
