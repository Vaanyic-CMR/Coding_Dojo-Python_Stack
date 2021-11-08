from flask_app import app
from flask_app.controllers import authors, books
from flask import redirect

@app.route('/')
def home():
    return redirect('/authors')

if __name__ == '__main__':
    app.run(debug=True)