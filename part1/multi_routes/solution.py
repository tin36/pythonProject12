# В данном задании вам необходимо 
# создать фласк приложение, с четырьмя html-страницами.
# У Вас имеется список с 5 числовыми значениями
# Вам необходимо при переходе на страницу по адресу:
#
# 1. 127.0.0.1:5000/all/
#    отобразить все значения списка через пробел
#
# 2. 127.0.0.1:5000/max/
#    отобразить максимальное значение списка
#
# 3. 127.0.0.1:5000/min/
#    отобразить минимальное значение списка
#
# 4. 127.0.0.1:5000/avg/
#    рассчитать и отобразить среднее значение списка
#
from flask import Flask
from statistics import mean
app = Flask(__name__)

expenses = [1240, 60, 230, 20, 310]

@app.route("/all/")
def page_all():
   return " ".join([str(element) for element in expenses])

@app.route("/max/")
def page_max():
   return str(max(expenses))

@app.route("/min/")
def page_min():
   return str(min(expenses))

@app.route("/avg/")
def page_avg():
   return str(mean(expenses))

if __name__ == "__main__":
    app.run()