from flask_app.config.mysqlconnection import connectToMySQL
from flask import session, flash

class Recipe:
    db_name = 'mydb'
    
    def __init__( self, data ):
        self.id = data['id']
        self.creator_id = data['creator_id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.made_on = data['made_on']
        self.time = data['time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @staticmethod
    def validate( data ):
        is_valid = True
        if len(data['name']) < 3:
            flash("Recipe Name must be at least 3 characters.")
            is_valid = False
        if len(data['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if len(data['instructions']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        if len(data['made_on']) < 1:
            flash("Must have a date.")
            is_valid = False
        return is_valid
    
    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO recipes ( creator_id, name, description, instructions, made_on, time, created_at, updated_at ) "+
                "VALUES ( %(creator_id)s, %(name)s, %(description)s, %(instructions)s, %(made_on)s, %(time)s, NOW(), NOW() );")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def update( cls, data ):
        query = ("UPDATE recipes SET name=%(name)s, description=%(description)s, "+
                "instructions=%(instructions)s, made_on=%(made_on)s, time=%(time)s, "+
                "updated_at=NOW() "+
                "WHERE id = %(id)s;")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def delete( cls, recipe_id ):
        query = ("DELETE FROM recipes WHERE id = %(id)s;")
        data = { 'id': recipe_id }
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL( cls.db_name ).query_db( query )
        
        recipes = []
        for result in results:
            recipes.append( cls(result) )
        return recipes
    
    @classmethod
    def get_by_id( cls, recipe_id ):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        data = { 'id': recipe_id }
        result = connectToMySQL( cls.db_name ).query_db( query, data )
        
        if len(result) < 1:
            return False
        return cls( result[0] )