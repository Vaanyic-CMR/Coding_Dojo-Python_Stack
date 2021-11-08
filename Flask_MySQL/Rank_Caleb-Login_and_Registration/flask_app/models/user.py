from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash
from flask_bcrypt import Bcrypt        
from flask_app import app
import re

bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    db_name = 'mydb'
    
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def full_name( self ):
        return f"{self.first_name} {self.last_name}"
    
    @staticmethod
    def validate_register( data ):
        is_valid = True
        if not EMAIL_REGEX.match( data['email'] ):
            flash("Invalid email address!")
            is_valid = False
        if len(data['first_name']) < 3:
            flash("First Name must be at least 3 characters.")
            is_valid = False
        if len(data['last_name']) < 3:
            flash("last_name must be at least 3 characters.")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        if data['password'] != data['con_pass']:
            flash("Password confirmation must match.")
            is_valid = False
        session['attempt'] = 'register'
        return is_valid
    
    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO users ( first_name, last_name, email, password, created_at, updated_at ) "+
                "VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW() );")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def delete( cls, data ):
        query = ("DELETE FROM users WHERE id = %(id)s;")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL( cls.db_name ).query_db( query )
        
        users = []
        for result in results:
            users.append( cls(result) )
        return users
    
    @classmethod
    def get_by_id( cls, data ):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL( cls.db_name ).query_db( query, data )
        
        if len(result) < 1:
            return False
        return cls( result[0] )
    
    @classmethod
    def get_by_email( cls, data ):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL( cls.db_name ).query_db( query, data )
        print(result)
        if len(result) < 1:
            return False
        return cls( result[0] )
