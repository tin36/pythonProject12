from flask import Flask
from flask import render_template
app = Flask(__name__)


meal = {
  "title": "Пицца с ананасами",
  "price": 690,
  "weight": 400, 
 }


@app.route('/meal/')
def sign_in():
    return render_template('index.html', **meal)

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
#       <h2>Название: {{ title }}</h2>
#       <p>Цена: {{ price }}</p>
#       <p>Вес: {{ weight }}</p>   
#     </main>
#   </body>
# </html>