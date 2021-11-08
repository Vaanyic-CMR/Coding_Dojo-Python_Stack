class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("Account has negative balance")
        return self

class User:
    def __init__(self, name, email, int_rate, balance):
        self.name = name
        self.email = email
        self.account = [BankAccount(int_rate, balance)]
    
    def make_deposit(self, amount, account_num=0):
        self.account[account_num].balance += amount
    
    def make_withdrawal(self, amount, account_num=0):
        self.account[account_num].balance -= amount
    
    def add_account(self, int_rate=0, balance=0):
        self.account.append(BankAccount(int_rate, balance))
    
    def display_user_balance(self):
        for i in range(0, len(self.account)):
            print(f"User: {self.name}, Account {i+1} Balance: ${self.account[i].balance}")
    
    def transfer_money(self, other_user, amount, other_account=0, account_num=0):
        other_user.account[other_account].balance += amount
        self.account[account_num].balance -= amount

# ----------- Class Instances
guido = User("Guido van Rossum", "guido@email.com", 0.01, 500)
john = User("John G Doe", "john@email.com", 0.05, 1000)
caleb = User("Caleb M Rank", "caleb@email.com", 0.07, 5000)

guido.make_deposit(200)
guido.display_user_balance()

john.make_withdrawal(250)
john.display_user_balance()

caleb.add_account(0.02, 1000)
caleb.make_withdrawal(500)
caleb.make_deposit(500, 1)
caleb.display_user_balance()