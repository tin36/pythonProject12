from flask import Flask, request
from flask import render_template
app = Flask(__name__)


discounts_list = [
    {"title": "Треть на доставку", "discount":30, "code":"minidelivery"},
    {"title": "Цены пополам", "discount":50, "code":"halflings"},
]


@app.route('/discounts/')
def discounts():
    return render_template('index.html', discounts=discounts_list)

if __name__=="__main__":
    app.run()

# <!DOCTYPE html >
# <html>
#   <head>
#     <meta charset="utf-8">
#     <title>Skypro</title>
#   </head>
#   <body>
#     <main style ="width: 320px; margin: 0 auto;">
#       {% for item in discounts %}
#          <div>
#            <h3>{{ item.title }}</h3>
#            <p>Скидка: {{ item.discount }}</p>
#            <p>Код: {{ item.code }}</p>
#          </div>
#       {% endfor %}
#     </main>
#   </body>
# </html>