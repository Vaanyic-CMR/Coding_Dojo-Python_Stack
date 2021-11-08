class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        other_user.account_balance += amount
        self.account_balance -= amount
        return self
    
# ----------- Class Instances
guido = User("Guido van Rossum", "guido@gmail.com")
john = User("John G Doe", "john@gmail.com")
caleb = User("Caleb M Rank", "caleb@gmail.com")

guido.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawal(150).display_user_balance()

john.make_deposit(200).make_deposit(200).make_withdrawal(150).make_withdrawal(150).display_user_balance()

caleb.make_deposit(1000).make_withdrawal(250).make_withdrawal(250).make_withdrawal(250).display_user_balance()

guido.transfer_money(caleb, 100).display_user_balance()
caleb.display_user_balance()