from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    db_name = 'mydb'
    
    def __init__( self, data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate_email( data ):
        is_valid = True
        if not EMAIL_REGEX.match( data['email'] ):
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    
    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO emails ( email, created_at, updated_at ) "+
                "VALUES ( %(email)s, NOW(), NOW() );")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def delete( cls, data ):
        query = ("DELETE FROM emails WHERE id = %(id)s;")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM emails;"
        results = connectToMySQL( cls.db_name ).query_db( query )
        
        emails = []
        for result in results:
            emails.append( cls(result) )
        return emails