# В данном задании вам предстоит инициализировать 
# Flask-приложение, а также создать 3 view-функции, которые:
#
# 1. При переходе в бразузере на по адресу 127.0.0.1:5000 
#    отображает надпись "Это главная страница".
#
# 2. При переходе в бразузере на по адресу 127.0.0.1:5000/feed/ 
#    отображает надпись "Это страница ленты".
#
# 3. При переходе в бразузере на по адресу 127.0.0.1:5000/feedback/ 
#    отображает надпись "Тут вы можете оставить обратную связь".
#
# 4. При переходе в бразузере на по адресу 127.0.0.1:5000/profile/ 
#    отображает надпись "А это информация про пользователя".
#
# P.S. В данном задании не используйте язык разметки html.
#      тестироваться будет только текст.
from flask import Flask
app = Flask(__name__)


@app.route("/")
def main():
    return f'Это главная страница'

@app.route("/feed/")
def feed():
        return f'Это страница ленты'

@app.route("/feedback/")
def feedback():
    return f'Тут вы можете оставить обратную связь'


@app.route("/profile/")
def profile():
    return f'А это информация про пользователя'
app.run()