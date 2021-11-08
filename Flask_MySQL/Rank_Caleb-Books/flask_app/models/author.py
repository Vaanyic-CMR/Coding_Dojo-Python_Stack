from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book

class Author:
    db_name = 'mydb'
    
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.author_fav = []
    
    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO authors ( name, created_at, updated_at )"+
                "VALUES( %(name)s, NOW(), NOW() );")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def add_fav( cls, data ):
        query = ("INSERT INTO favorites (author_id, book_id) "+
                "VALUES( %(author_id)s, %(book_id)s )")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def get_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL( cls.db_name ).query_db( query )
        authors = []
        
        for result in results:
            authors.append( cls(result) )
        return authors
    
    @classmethod
    def get_author_with_books( cls , data ):
        query = ("SELECT * FROM authors "+
                "LEFT JOIN favorites ON favorites.author_id = authors.id "+
                "LEFT JOIN books ON favorites.book_id = books.id "+
                "WHERE authors.id = %(id)s;")
        results = connectToMySQL( cls.db_name ).query_db( query , data )
        
        author = cls( results[0] )
        
        for row_from_db in results:
            book_data = {
                "id" : row_from_db["books.id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["books.created_at"],
                "updated_at" : row_from_db["books.updated_at"]
            }
            author.author_fav.append( book.Book( book_data ) )
        return author