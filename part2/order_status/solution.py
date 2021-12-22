from flask import Flask, render_template
app = Flask(__name__)

@app.route("/getstatus/<int:code>")
def page_orderstatus(code):
    return render_template("status.html", code=code)


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
#         {% if code == 1 %}
#         <p>заказ принят</p>
#         {% elif code == 2 %}
#         <p>заказ готовится</p>
#         {% elif code == 3 %}
#         <p>заказ в пути</p>
#         {% elif code == 4 %}
#         <p>заказ доставлен</p>
#         {% elif code == 5 %}
#         <p>заказ отменен</p>
#         {% endif %}
#     </main>
#   </body>
# </html>