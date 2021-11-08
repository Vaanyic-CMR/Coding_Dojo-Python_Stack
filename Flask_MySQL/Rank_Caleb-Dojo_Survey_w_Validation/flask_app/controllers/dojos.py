from flask_app import app
from flask_app.models import dojo
from flask import render_template, redirect, request, session, flash

@app.route('/get_result', methods=['POST'])
def get_result():
    if dojo.Dojo.validate_dojo( request.form ):
        dojo.Dojo.save( request.form )
        session['name'] = request.form['name']
        session['location'] = request.form['location']
        session['language'] = request.form['language']
        session['comment'] = request.form['comment']
        return redirect('/show_result')
    else:
        return redirect('/')

@app.route('/show_result')
def show_result():
    return render_template('results.html', name=session['name'], location=session['location'], language=session['language'], comment=session['comment'])

@app.route('/clear_data')
def clear():
    session.clear()
    return render_template('index.html')