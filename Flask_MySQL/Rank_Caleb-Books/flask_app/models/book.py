from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author

class Book:
    db_name = 'mydb'
    
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.book_fav = []
    
    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO books ( title, num_of_pages, created_at, updated_at )"+
                "VALUES( %(title)s, %(num_of_pages)s, NOW(), NOW() );")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def add_fav( cls, data ):
        query = ("INSERT INTO favorites (author_id, book_id) "+
                "VALUES( %(author_id)s, %(book_id)s )")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def get_books( cls ):
        query = "SELECT * FROM books;"
        results = connectToMySQL( cls.db_name ).query_db( query )
        books = []
        
        for result in results:
            books.append( cls(result) )
        return books
    
    @classmethod
    def get_authors_with_book( cls , data ):
        query = ("SELECT * FROM books "+
                "LEFT JOIN favorites ON favorites.book_id = books.id "+
                "LEFT JOIN authors ON favorites.author_id = authors.id "+
                "WHERE books.id = %(id)s;")
        results = connectToMySQL( cls.db_name ).query_db( query , data )
        
        book = cls( results[0] )
        
        for row_from_db in results:
            author_data = {
                "id" : row_from_db["authors.id"],
                "name" : row_from_db["name"],
                "created_at" : row_from_db["authors.created_at"],
                "updated_at" : row_from_db["authors.updated_at"]
            }
            book.book_fav.append( author.Author( author_data ) )
        return book