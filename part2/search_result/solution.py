from flask import Flask, request
from flask import render_template
app = Flask(__name__)


meals = [
    "Пицца с ананасами",
    "Пицца с сыром",
    "Суп с грибами",
    "Суп со шпинатом",
    "Кальцоне",
    "Креветта",
    "Вишневый пирог",
    "Лимонный пирог"
]


@app.route('/search/')
def search():
    s = request.args.get("meal")
    if s is None:
        return "Введите параметр meal"
    s = s.lower()
    meals_match = [x for x in meals if s in x.lower()]
    if len(meals_match):
        return render_template('index.html', meals_count = len(meals_match), meals=meals_match)
    return "Блюд не найдено"

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
#       <h2>Найдено: {{ meals_count }}</h2>
#         <ul>
#          {% for meal in meals %}
#            <li>{{ meal }}</li>
#          {% endfor %}
#       </ul> 
#     </main>
#   </body>
# </html>