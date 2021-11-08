from logging import debug
import base64
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'my_temp_secret_key'

@app.route('/')
def counter():
    if 'visit_num' in session:
        session['visit_num'] += 1
    else:
        session['visit_num'] = 1
    
    if 'total_count' in session:
        session['total_count'] += 1
    else:
        session['total_count'] = 1
    
    return render_template('counter.html', count = session['total_count'] , visiting = session['visit_num'])

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/add_visits', methods=['POST'])
def add_visits():
    session['total_count'] += int(request.form['add_by'])
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)