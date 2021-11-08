from flask_app import app
from flask_app.models import dojo, ninja
from flask import render_template, redirect, request, session, flash

@app.route('/dojos')
def dojos():
    dojos = dojo.Dojo.get_dojos()
    return render_template('dojos.html', dojos=dojos)

@app.route('/dojos/create', methods=['POST'])
def create_dojo():
    data = { 'name': request.form['name'] }
    dojo.Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def view_ninjas(dojo_id=None):
    if dojo_id != None:
        dojo_w_ninjas = dojo.Dojo.get_dojo_with_ninjas( {'id': dojo_id} )
        return render_template('view_ninjas.html', dojo_w_ninjas=dojo_w_ninjas)
    else:
        return redirect('/')