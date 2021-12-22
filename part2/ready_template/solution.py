from flask import Flask
from flask import render_template
app = Flask(__name__)


variables = {
    "username": "Skypro",
    "phone": "+7 777 77 77",
    "location": "Москва"
}

@app.route('/sign-in/')
def sign_in():
    return render_template('index.html', **variables)

if __name__=="__main__":
    app.run()