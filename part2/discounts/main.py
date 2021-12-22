# У вас есть список словарей словарь со спецпредложениями. 
# Выведите их cписом!
# - исправьте шаблон в папке templates
# (Поблочно в шаблоне, с использованием тега <div>)


from flask import Flask, request
from flask import render_template
app = Flask(__name__)


discounts_list = [
    {"title": "Треть на доставку", "discount":30, "code":"minidelivery"},
    {"title": "Цены пополам", "discount":50, "code":"halflings"},
]


@app.route('/discounts/')
def discounts():
    # TODO напишите view-функцию здесь
    pass

if __name__=="__main__":
    app.run()