from flask_app import app
from flask_app.controllers import dojos, ninjas
from flask import redirect

@app.route('/')
def home():
    return redirect('/dojos')

if __name__ == '__main__':
    app.run(debug=True)