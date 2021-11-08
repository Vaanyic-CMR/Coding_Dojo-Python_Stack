from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash

class Dojo:
    db_name = 'mydb'
    
    def __init__( self, data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO dojos ( name, location, language, comment, created_at, updated_at ) "+
                "VALUES ( %(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW() );")
        return connectToMySQL( cls.db_name ).query_db( query, data )

    @staticmethod
    def validate_dojo( data ):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['location']) < 3:
            flash("Location must be at least 3 characters.")
            is_valid = False
        if len(data['language']) < 3:
            flash("language must be at least 3 characters.")
            is_valid = False
        if len(data['comment']) < 5:
            flash("Comment must be at least 5 characters.")
            is_valid = False
        return is_valid