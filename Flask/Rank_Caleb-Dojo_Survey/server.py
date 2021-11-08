from flask import Flask, render_template, session, redirect, request

app = Flask(__name__)
app.secret_key = 'my_temp_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_result', methods=['POST'])
def get_result():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/show_result')

@app.route('/show_result')
def show_result():
    return render_template('results.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

@app.route('/clear_data')
def clear():
    session.clear()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)