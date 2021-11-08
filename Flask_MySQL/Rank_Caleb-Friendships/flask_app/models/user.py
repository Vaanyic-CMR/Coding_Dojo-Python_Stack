from flask_app.config.mysqlconnection import connectToMySQL

class User:
    db_name = 'mydb'
    
    def __init__( self, data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.friend = None
    
    def full_name( self ):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def add_user( cls, data ):
        query = ("INSERT INTO users ( first_name, last_name, created_at, updated_at )"+
                "VALUES ( %(first_name)s, %(last_name)s, NOW(), NOW() );")
        return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def get_users( cls ):
        query = ("SELECT * FROM users;")
        results = connectToMySQL( cls.db_name ).query_db( query )
        users = []
        
        for result in results:
            users.append( cls(result) )
        return users
    
    @classmethod
    def add_friendship( cls, data ):
        if cls.check_friendship( data ):
            query = ("INSERT INTO friendships ( user_id, friend_id, created_at, updated_at )"+
                    "VALUES ( %(user_id)s, %(friend_id)s, NOW(), NOW() );")
            return connectToMySQL( cls.db_name ).query_db( query, data )
    
    @classmethod
    def get_friendships( cls ):
        query = ("SELECT * FROM users "+
                "JOIN friendships ON users.id = friendships.user_id "+
                "JOIN users as friend ON friend.id = friendships.friend_id "+
                "ORDER BY users.id;")
        results = connectToMySQL( cls.db_name ).query_db( query )
        
        friends = []
        for row_from_db in results:
            friends.append( cls(row_from_db) )
            friend_data = {
                "id" : row_from_db["friend.id"],
                "first_name" : row_from_db["friend.first_name"],
                "last_name" : row_from_db["friend.last_name"],
                "created_at" : row_from_db["friend.created_at"],
                "updated_at" : row_from_db["friend.updated_at"]
            }
            friends[-1].friend = cls( friend_data )
        return friends
    
    @classmethod
    def check_friendship( cls, data ):
        check = True
        
        query = ("SELECT * FROM friendships "+
                "WHERE user_id = %(user_id)s and friend_id = %(friend_id)s;")
        result1 = connectToMySQL( cls.db_name ).query_db( query, data )
        print(result1)
        query = ("SELECT * FROM friendships "+
                "WHERE user_id = %(friend_id)s and friend_id = %(user_id)s;")
        result2 = connectToMySQL( cls.db_name ).query_db( query, data )
        print(result2)
        
        if len(result1) > 0 or len(result2) > 0:
            check = False
        
        return check