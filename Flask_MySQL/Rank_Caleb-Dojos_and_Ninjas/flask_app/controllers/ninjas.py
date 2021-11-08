from flask_app import app
from flask_app.models import dojo, ninja
from flask import render_template, redirect, request, session, flash

@app.route('/ninjas')
def ninjas():
    dojos = dojo.Dojo.get_dojos()
    return render_template('new_ninja.html', dojos=dojos)

@app.route('/ninjas/create', methods=['POST'])
def create_ninja():
    dojo_id = dojo.Dojo.get_dojo_by_name(request.form['dojo'])
    print(dojo_id)
    data = {
        'first_name': request.form['first-name'],
        'last_name': request.form['last-name'],
        'age': int(request.form['age']),
        'dojo_id': dojo_id
    }
    ninja.Ninja.save(data)
    return redirect(f'/dojos/{dojo_id}')