from flask_app import app
from flask_app.controllers import emails
from flask import render_template, redirect

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)