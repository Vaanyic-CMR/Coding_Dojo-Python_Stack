from flask_app import app
from flask_app.models import author, book
from flask import render_template, redirect, request, session, flash

@app.route('/books')
def books():
    books = book.Book.get_books()
    return render_template('books.html', books=books)

@app.route('/books/new', methods=['POST'])
def new_book():
    data = {
        'title': request.form['title'],
        'num_of_pages': int(request.form['num_of_pages'])
        }
    book.Book.save( data )
    return redirect('/books')

@app.route('/books/<int:x>')
def view_book(x=None):
    if x != None:
        data = { 'id': x }
        selected_book = book.Book.get_authors_with_book( data )
        authors = author.Author.get_authors()
        return render_template('view_book.html', book=selected_book, authors=authors)
    else:
        return redirect('/books')

@app.route('/books/fav', methods=['POST'])
def book_add_fav():
    req = request.form['fav'].split()
    data = {
        'author_id': req[0],
        'book_id': req[1]
        }
    print(data)
    book.Book.add_fav( data )
    return redirect(f'/books/{req[1]}')