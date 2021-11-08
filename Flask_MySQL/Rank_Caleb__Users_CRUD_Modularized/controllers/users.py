# burgers.py
from Rank_Caleb__Users_CRUD_Modularized import app
from flask import render_template,redirect,request,session,flash
from Rank_Caleb__Users_CRUD_Modularized.models.user import User

@app.route('/users')
def users():
    users = User.get_all()
    return render_template('users.html', users=users)

@app.route('/users/show/<int:x>')
def show_user(x=None):
    if x != None:
        user = User.get_user(x)
        return render_template('display_user.html', user=user)

@app.route('/users/new')
def create_user():
    return render_template('new_user.html')

@app.route('/users/new/add', methods=['POST'])
def add_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }
    User.new_user(data)
    return redirect('/users')

@app.route('/users/delete/<int:x>')
def delete_user(x=None):
    if x != None:
        User.delete_user(x)
    return redirect('/')

@app.route('/users/edit/<int:x>')
def edit_user(x=None):
    if x != None:
        user = User.get_user(x)
        return render_template('edit_user.html', user=user)
    else:
        return redirect('/')

@app.route('/users/edit/update/<int:x>', methods=['POST'])
def update_user(x=None):
    if x != None:
        data = {
            'id': x,
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
        }
        print(data)
        User.update_user(data)
        return redirect(f'/users/show/{x}')
    else:
        return redirect('/users')