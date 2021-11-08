from flask_app import app
from flask_app.controllers import users, messages
from flask import render_template, session

@app.route('/')
def home():
    if 'attempt' not in session:
        session['attempt'] = ''
    return render_template('login_register.html', attempt=session['attempt'])

if __name__ == '__main__':
    app.run(debug=True)