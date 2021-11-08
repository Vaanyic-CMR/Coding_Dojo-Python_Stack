from flask_app import app
from flask_app.models import user
from flask import render_template, redirect, request, session, flash

@app.route('/friendships')
def friendships():
    friends = user.User.get_friendships()
    users = user.User.get_users()
    return render_template('friendships.html', friends=friends, users=users)

@app.route('/friendships/user', methods=['POST'])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name']
    }
    user.User.add_user( data )
    return redirect('/')

@app.route('/friendships/friend', methods=['POST'])
def add_friendship():
    data = {
        'user_id': int(request.form['user']),
        'friend_id': int(request.form['friend'])
    }
    user.User.add_friendship( data )
    return redirect('/')