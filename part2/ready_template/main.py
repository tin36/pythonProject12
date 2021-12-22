# У вас есть подготовленный шаблон. 
# Передайте в него переменные "username" , "phone", "location"

from flask import Flask
app = Flask(__name__)


variables = {
    "username": "Skypro",
    "phone": "+7 777 77 77",
    "location": "Москва"
}

@app.route('/sign-in/')
def sign_in():
    return f'Имя - {variables["username"]}<br>' \
           f'Телефон - {variables["phone"]}<br>' \
           f'Город - {variables["location"]}<br>'

if __name__=="__main__":
    app.run(debug=True, port=1001)