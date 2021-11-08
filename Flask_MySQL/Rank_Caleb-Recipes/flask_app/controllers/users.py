from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe
from flask_bcrypt import Bcrypt
from flask_app import app

bcrypt = Bcrypt(app)

@app.route('/register/user', methods=['POST'])
def register():
    if user.User.validate_register( request.form ):
        pw_hash = bcrypt.generate_password_hash( request.form['password'] )
        print(pw_hash)
        
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
        }
        user_id = user.User.save( data )
        session['user_id'] = user_id
        return redirect('/dashboard')
    session['attempt'] = 'register'
    return redirect('/')

@app.route('/login/user', methods=['POST'])
def login():
    data = { 'email': request.form['email'] }
    user_in_db = user.User.get_by_email( data )
    session['attempt'] = 'login'
    
    if not user_in_db:
        flash("Invalid Email/Password")
        return redirect('/')
    if not bcrypt.check_password_hash( user_in_db.password, request.form['password'] ):
        flash("Invalid Email/Password")
        return redirect('/')
    
    session['user_id'] = user_in_db.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    try:
        active_user = user.User.get_by_id( session['user_id'] )
        recipes = recipe.Recipe.get_all()
        return render_template( 'dashboard.html', user=active_user, recipes=recipes )
    except:
        return redirect('/')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')