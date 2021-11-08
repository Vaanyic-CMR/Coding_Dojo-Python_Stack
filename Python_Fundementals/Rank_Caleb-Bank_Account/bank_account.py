class BankAccount:
    def __init__(self, int_rate = 0, balance = 0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        else:
            print("Account has negative balance")
        return self

acc1 = BankAccount(0.01, 100)
acc2 = BankAccount(0.05)

acc1.deposit(100).deposit(300).deposit(20).withdraw(500).yield_interest().display_account_info()
acc2.deposit(200).deposit(500).withdraw(50).withdraw(60).withdraw(200).withdraw(100).yield_interest().display_account_info()