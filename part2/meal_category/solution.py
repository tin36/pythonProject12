from flask import Flask, render_template
app = Flask(__name__)

order = ["Суп с лосем", "Чизбургер",  "Тирамису"]

cats = {
  "soup" : ["Суп с грибами", "Суп с тыквой", "Суп с лосем", "Суп с вермишелью"], 
  "main" : ["Лазанья", "Паста Карбонара", "Чизбургер"], 
  "salads" : ["Греческий салат", "Салат Цезарь", "Салат из свежих овощей"],
  "desserts": ["Чизкейк", "Тирамису", "Вишневый пирог"]
}


@app.route("/cats/")
def page_cats():
    return render_template("meals.html", order=order, cats=cats)

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
#       <h1> Ваш заказ </h1>
#       {% for element in order %}
#         {% if element in cats.salads %}
#           <h2> Салаты: </h2>
#           <ul>
#             <li>{{ element }}</li>
#           </ul>
#           {% elif element in cats.soup %}
#           <h2> Супы: </h2>
#           <ul>
#             <li>{{ element }}</li>
#           </ul>
#           {% elif element in cats.main %}
#           <h2> Основные блюда: </h2>
#           <ul>
#             <li>{{ element }}</li>
#           </ul>
#           {% elif element in cats.desserts %}
#           <h2> Десерты: </h2>
#           <ul>
#             <li>{{ element }}</li>
#           </ul>
#         {% endif %}
#       {% endfor %}
#     </main>
#   </body>
# </html>