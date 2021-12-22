# У вас есть список словарей словарь со спецпредложениями. 
# Выведите их cписом!
# - исправьте шаблон в папке templates
# (Поблочно в шаблоне, с использованием тега <div>)


from flask import Flask, request
from flask import render_template
app = Flask(__name__)


Skypro = [
  {“title”: “Главная”, “link”: “/ ”}, 
  {“title”: “Лента”, “link”: “/feed ”}, 
  {“title”: “Профиль”, “link”: “/me ”}, 
]



@app.route('/discounts/')
def discounts():
    # TODO напишите view-функцию здесь
    pass

if __name__=="__main__":
    app.run()