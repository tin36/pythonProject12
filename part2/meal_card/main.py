# У вас есть словарь с данными 
# ресторана и шаблон index.html. 
# Измените шаблон так, чтобы он принимал переменные cловаря meal,
# а также напишите view-функцию чтобы передать переменные в шаблон
from flask import Flask, render_template

app = Flask(__name__)


meal = {
  "title": "Пицца с ананасами",
  "price": 690,
  "weight": 400, 
 }


@app.route('/')
def sign_in():
    return render_template("index.html", **meal)

if __name__=="__main__":
    app.run()