from flask import render_template, redirect, request, session, flash
from flask_app.models import user, message
from flask_app import app

@app.route('/dashboard')
def dashboard():
    data = { 'id': session['user_id'], 'recipient_id': session['user_id'] }
    user_data = user.User.get_by_id( data )
    messages = message.Message.get_all_by_id( data )
    num_messages = len(messages)
    friends = user.User.get_all_ex_id( data )
    return render_template( 'dashboard.html', user=user_data,
                            messages=messages, num_messages=num_messages,
                            friends=friends )

@app.route('/message/delete/<int:x>')
def delete_message( x=None ):
    message.Message.delete( { 'id': x } )
    return redirect("/dashboard")

@app.route('/message/send/<int:x>', methods=['POST'])
def send_message( x=None ):
    data = {
        'sender_id': session['user_id'],
        'recipient_id': x,
        'content': request.form['content']
        }
    message.Message.save( data )
    return redirect('/dashboard')