# У вас есть несколько статусов заказа

# 1 - заказ принят
# 2 - заказ готовится
# 3 - заказ в пути
# 4 - заказ доставлен
# 5 - заказ отменен

# Получите статус цифрой, выведите статус текстом
# Используйте конструкции IF в шаблоне.
from flask import Flask
app = Flask(__name__)



@app.route("/getstatus/<int:code>")
def page_orderstatus(code):
    # TODO напишите view-функцию здесь
    pass


if __name__=="__main__":
    app.run()