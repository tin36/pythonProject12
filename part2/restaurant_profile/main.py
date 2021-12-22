# У вас есть словарь с данными 
# ресторана и шаблон index.html. 
# Измените шаблон так, чтобы он принимал переменные
# А также напишите view-функцию чтобы передать переменные в шаблон
from flask import Flask
app = Flask(__name__)


variables = {
    "title": "Рогаси лосяси",
    "cuisine": "Японская",
    "address": "Ул Охотничья 7",
}

@app.route('/place/')
def get_profile():
    # TODO напишите view-функцию здесь
    pass

if __name__=="__main__":
    app.run()