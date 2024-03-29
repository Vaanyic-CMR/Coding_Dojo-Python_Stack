from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    database = 'mydb'
    
    def __init__(self, db_data):
        self.id = db_data['id']
        self.first_name = db_data['first_name']
        self.last_name = db_data['last_name']
        self.age = db_data['age']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO ninjas ( first_name, last_name, age, dojo_id, created_at, updated_at ) " +
                "VALUES( %(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, NOW(), NOW() );")
        return connectToMySQL(cls.database).query_db( query, data )