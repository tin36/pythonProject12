# У вас есть словарь с данными 
# ресторана и шаблон index.html. 
# Измените шаблон так, чтобы он принимал переменные cловаря meal,
# а также напишите view-функцию чтобы передать переменные в шаблон
from flask import Flask
app = Flask(__name__)


meal = {
  "title": "Пицца с ананасами",
  "price": 690,
  "weight": 400, 
 }


@app.route('/meal/')
def sign_in():
    # TODO напишите view-функцию здесь
    pass

if __name__=="__main__":
    app.run()