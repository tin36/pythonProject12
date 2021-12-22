# Исправьте шаблон в файле /templates/index.html так,
# чтобы он выводил данные в соответсвии со словарём.
# Статусы указаны ниже:
# 
# Статусы:
# 1 - заказ принят
# 2 - заказ готовится
# 3 - заказ в пути
# 4 - заказ доставлен
# 5 - заказ отменен

from flask import Flask, render_template
app = Flask(__name__)


checkout = {
  "name" : "Чистякова Берта",
  "address": "Щетининский пер, дом 188, квартира 712",
  "phone": "+7 (971) 300-90-90",
  "meals" : ["Пицца с сыром","Суп с грибами"] ,
  "total": 950, 
  "discount": 20,
  "status": 3
}


@app.route('/payment/')
def search():
    # TODO напишите view-функцию здесь
    pass

if __name__=="__main__":
    app.run()