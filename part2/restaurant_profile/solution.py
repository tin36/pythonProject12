from flask import Flask
from flask import render_template
app = Flask(__name__)


variables = {
    "title": "Рогаси лосяси",
    "cuisine": "Японская",
    "address": "Ул Охотничья 7",
}

@app.route('/place/')
def sign_in():
    return render_template('index.html', **variables)

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
#       <p>Кухня: {{ cuisine }}</p>
#       <p>Адрес: {{ address }}</p>   
#     </main>
#   </body>
# </html>