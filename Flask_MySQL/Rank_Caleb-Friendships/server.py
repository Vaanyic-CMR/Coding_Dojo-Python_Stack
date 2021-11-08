from flask_app import app
from flask_app.controllers import users
from flask import redirect

@app.route('/')
def home():
    return redirect('/friendships')

if __name__ == '__main__':
    app.run(debug=True)