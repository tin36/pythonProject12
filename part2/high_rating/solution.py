from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/rest_rating/')
def search():
    with open("restaurants.txt") as file:
        rest_list = file.readlines()
    rest_ratings = []
    for rest in rest_list:
        name, rating = rest.split()
        if float(rating) >= 4.6:
            rest_ratings.append((name, rating))
    sorted_list = sorted(rest_ratings, key=lambda tup: tup[1], reverse=True)
    return render_template('index.html', restaurants=sorted_list)

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
#       <h2>Название:</h2>
#         <ul>
#           {% for name, rating in restaurants %}
#             <li>{{ name }} {{ rating }}</li>
#           {% endfor %}
#         </ul>
#     </main>
#   </body>
# </html>