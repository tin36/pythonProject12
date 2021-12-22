# У вас есть словарь с данными 
# ресторана и шаблон index.html. 
# Измените шаблон так, чтобы он принимал переменные
# А также напишите view-функцию чтобы передать переменные в шаблон
from flask import Flask, render_template

app = Flask(__name__)


variables = {
    "title": "Рогаси лосяси",
    "cuisine": "Японская",
    "address": "Ул Охотничья 7",
}

@app.route('/')
def sign_in():
    return render_template('index.html', **variables)

if __name__=="__main__":
    app.run(debug=True, port=1002)