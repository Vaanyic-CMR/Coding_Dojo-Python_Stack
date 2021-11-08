from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    database = 'mydb'
    
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        
        self.ninjas = []
    
    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO dojos ( name, created_at, updated_at ) " +
                "VALUES( %(name)s, NOW(), NOW() );")
        return connectToMySQL(cls.database).query_db( query, data )
    
    @classmethod
    def get_dojos( cls ):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL( cls.database ).query_db( query )
        
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def get_dojo_by_name( cls, name ):
        query = ("SELECT id FROM dojos " +
                "WHERE name = %(name)s;")
        data = { 'name': name }
        return connectToMySQL( cls.database ).query_db( query, data )[0]['id']

    @classmethod
    def get_dojo_with_ninjas( cls, data ):
        query = ("SELECT * FROM dojos " +
                "LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id " +
                "WHERE dojos.id = %(id)s;")
        results = connectToMySQL( cls.database ).query_db( query, data )
        
        dojo = cls( results[0] )
        for row_from_db in results:
            ninja_data = {
                'id': row_from_db['ninjas.id'],
                'first_name': row_from_db['first_name'],
                'last_name': row_from_db['last_name'],
                'age': row_from_db['age'],
                'created_at': row_from_db['created_at'],
                'updated_at': row_from_db['updated_at'],
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo