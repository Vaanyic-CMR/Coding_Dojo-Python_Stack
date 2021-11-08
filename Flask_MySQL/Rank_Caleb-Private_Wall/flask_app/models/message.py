from flask import flash, session
from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
import re

class Message:
    db_name = 'mydb'
    
    def __init__( self, data ):
        self.id = data['id']
        self.content = data['content']
        self.sender_id = data['sender_id']
        self.recipient_id = data['recipient_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO messages ( content, sender_id, recipient_id, created_at, updated_at ) "+
                "VALUES ( %(content)s, %(sender_id)s, %(recipient_id)s, NOW(), NOW() );")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def delete( cls, data ):
        query = ("DELETE FROM messages WHERE id = %(id)s")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def get_all_by_id( cls, data ):
        query = ("SELECT * FROM messages "+
                "WHERE recipient_id = %(recipient_id)s "+
                "ORDER BY updated_at;")
        results = connectToMySQL( cls.db_name ).query_db( query, data )
        messages = []
        
        for result in results:
            messages.append( cls(result) )
        return messages