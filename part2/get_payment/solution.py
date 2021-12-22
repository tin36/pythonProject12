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
    return render_template('index.html', checkout=checkout)

if __name__=="__main__":
    app.run()

# <!DOCTYPE html >
# <html>
#   <head>
#     <meta charset="utf-8">
#     <title>Skypro</title>
#   </head>
#   <body>
#     <main style ="width: 500px; margin: 0 auto;">
#       <p>Клиент: {{ checkout.name }}</p>
#       <p>Адрес: {{ checkout.address }}</p>
#       <p>Телефон: {{ checkout.phone }}</p>
#       <p>Что заказано:</p>
#       <ul>
#         {% for meal in checkout.meals%}
#           <li>{{ meal }}</li>
#         {% endfor %}
#       </ul>
#         {% if checkout.status == 1 %}
#           <li>заказ принят</li>
#         {% elif checkout.status == 2 %}
#           <li>заказ готовится</li>
#         {% elif checkout.status == 3 %}
#           <li>заказ в пути</li>
#         {% elif checkout.status == 4 %}
#           <li>заказ доставлен</li>
#         {% elif checkout.status == 5 %}
#           <li>заказ отменен</li>
#         {% endif %}
#       <p>Сумма заказа: {{ checkout.total }}Р</p>
#       <p>Скидка {{ checkout.discount }}%</p>
#     </main>
#   </body>
# </html>