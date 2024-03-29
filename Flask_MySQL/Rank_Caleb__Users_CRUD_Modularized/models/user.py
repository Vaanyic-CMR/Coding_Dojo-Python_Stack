from Rank_Caleb__Users_CRUD_Modularized.config.mysqlconnection import connectToMySQL

class User:
    database = 'mydb'
    
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.database).query_db(query)
        users = []
        for user in results:
            users.append( User(user) )
        return users
    
    @classmethod
    def get_user(cls, x):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = { 'id': x }
        return User(connectToMySQL(cls.database).query_db(query, data)[0])
    
    @classmethod
    def new_user(cls, data):
        query = (
            "INSERT INTO users (first_name, last_name, email, created_at, updated_at)" +
            "VALUES( %(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
            )
        return connectToMySQL(cls.database).query_db(query, data)
    
    @classmethod
    def update_user(cls, data):
        query = ("UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = NOW() " + 
                "WHERE id = %(id)s;")
        return connectToMySQL(cls.database).query_db(query, data)
    
    @classmethod
    def delete_user(cls, user_id):
        query = "DELETE FROM users WHERE id = %(user_id)s;"
        data = { 'user_id': user_id }
        return connectToMySQL(cls.database).query_db(query, data)