from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = 'mydb'
    
    def __init__( self, data ):
        self.id = data['id']
        self.username = data['username']
        self.email = data['email']
    
    @classmethod
    def save( cls, data ):
        query = ("INSERT INTO users ( username, email )"+
                "VALUES( %(username)s, %(email)s );")
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
    def get_all_json(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL( cls.db_name ).query_db( query )
        users = []
        for user_data in results:
            users.append( user_data )
        return users
