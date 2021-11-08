from flask_app import app
from flask_app.models import email
from flask import render_template, redirect, request, session, flash

@app.route('/submit', methods=['POST'])
def submit():
    if email.Email.validate_email( request.form ):
        session['email'] = request.form['email']
        email.Email.save( request.form )
        return redirect('/success')
    else:
        return redirect('/')

@app.route('/success')
def success():
    emails = email.Email.get_all()
    return render_template('success.html', entered_email=session['email'], emails=emails)

@app.route('/delete/<int:x>')
def delete( x=None ):
    email.Email.delete( {'id': x } )
    return redirect('/success')