from flask import render_template, redirect, request, session, flash
from flask_app.models import user, recipe
from flask_app import app

@app.route('/recipes/delete/<int:recipe_id>')
def delete_recipe( recipe_id=None ):
    if 'user_id' in session:
        selected_recipe = recipe.Recipe.get_by_id( recipe_id )
        if session['user_id'] == selected_recipe.creator_id:
            recipe.Recipe.delete( recipe_id )
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/recipes/new')
def new_recipe():
    if 'user_id' in session:
        return render_template('create_recipe.html')
    else:
        return redirect('/')

@app.route('/recipes/create', methods=['POST'])
def create_recipe():
    if 'user_id' in session:
        if recipe.Recipe.validate( request.form ):
            data = {
                'creator_id': session['user_id'],
                'name': request.form['name'],
                'description': request.form['description'],
                'instructions': request.form['instructions'],
                'made_on': request.form['made_on'],
                'time': int(request.form['time'])
            }
            recipe.Recipe.save( data )
            return redirect('/dashboard')
        return redirect('/recipes/new')
    else:
        return redirect('/')

@app.route('/recipes/edit/<int:recipe_id>')
def edit_recipe( recipe_id=None ):
    if 'user_id' in session:
        selected_recipe = recipe.Recipe.get_by_id( recipe_id )
        if session['user_id'] == selected_recipe.creator_id:
            return render_template('edit_recipe.html', recipe=selected_recipe)
        else:
            return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/recipes/edit/<int:recipe_id>/save', methods=['POST'])
def update_recipe( recipe_id=None ):
    if 'user_id' in session:
        if recipe.Recipe.validate( request.form ):
            data = {
                'id': recipe_id,
                'creator_id': session['user_id'],
                'name': request.form['name'],
                'description': request.form['description'],
                'instructions': request.form['instructions'],
                'made_on': request.form['made_on'],
                'time': int(request.form['time'])
            }
            recipe.Recipe.update( data )
            return redirect('/dashboard')
        return redirect('/recipes/edit')
    else:
        return redirect('/')

@app.route('/recipes/<int:recipe_id>')
def view_instructions( recipe_id=None ):
    if 'user_id' in session:
        selected_recipe = recipe.Recipe.get_by_id( recipe_id )
        made_on = selected_recipe.made_on.strftime('%B %d, %Y')
        return render_template('view_instructions.html', recipe=selected_recipe, made_on=made_on)
    else:
        return redirect('/')