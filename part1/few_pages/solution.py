# 
# <h1> Страничка настроек </h1>
# <h1> Страничка каталога </h1>
# 
# В данном задании вам предстоит инициализировать Flask-приложение
# для этого
#
#
from flask import Flask
app = Flask(__name__)

@app.route("/")
def page_index():
   return "Это главная страница"

@app.route("/feed/")
def page_feed():
   return "Это страница ленты"

@app.route("/feedback/")
def page_feedback():
   return "Тут вы можете оставить обратную связь"

@app.route("/profile/")
def page_profile():
   return "А это информация про пользователя"

app.run()