from flask_app import app
from flask_app.models import author, book
from flask import render_template, redirect, request, session, flash

@app.route('/authors')
def authors():
    authors = author.Author.get_authors()
    return render_template('authors.html', authors=authors)

@app.route('/authors/new', methods=['POST'])
def new_author():
    data = { 'name': request.form['name'] }
    author.Author.save( data )
    return redirect('/authors')

@app.route('/authors/<int:x>')
def view_author(x=None):
    if x != None:
        data = { 'id': x }
        selected_author = author.Author.get_author_with_books(data)
        books = book.Book.get_books()
        return render_template('view_author.html', author=selected_author, books=books)
    else:
        return redirect('/authors')
    
@app.route('/authors/fav', methods=['POST'])
def author_add_fav():
    req = request.form['fav'].split()
    data = {
        'author_id': req[0],
        'book_id': req[1]
        }
    print(data)
    author.Author.add_fav( data )
    return redirect(f'/authors/{req[0]}')