from flask import Flask, render_template, redirect, request, session
from random import randint

app = Flask(__name__)
app.secret_key = 'my_temp_secret_key'

@app.route('/')
def main_page():
    if 'secret_number' not in session:
        session['secret_number'] = randint(1, 100)
    if 'guess' in session:
        print(session['guess'], session['secret_number'])
        if session['guess'] == session['secret_number']:
            return render_template('index.html', success='yes', num=session['secret_number'])
        elif session['guess'] > session['secret_number']:
            return render_template('index.html', success='high')
        elif session['guess'] < session['secret_number']:
            return render_template('index.html', success='low')
    else:
        return render_template('index.html', success='none')

@app.route('/check_guess', methods=['POST'])
def check_guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/clear_session')
def clear_session():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)