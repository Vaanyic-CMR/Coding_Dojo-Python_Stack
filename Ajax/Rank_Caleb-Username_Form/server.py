from flask import render_template, session
from flask_app.controllers import users
from flask_app import app

if __name__ == '__main__':
    app.run(debug=True)