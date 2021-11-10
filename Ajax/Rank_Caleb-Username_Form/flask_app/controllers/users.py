from flask import render_template, jsonify, request, redirect
from flask_app.models import user
from flask_app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return jsonify(user.User.get_all_json())

@app.route('/create/user', methods=['POST'])
def create_user():
    print( request.form )
    user.User.save( request.form )
    return jsonify(message="Add a user!!!")