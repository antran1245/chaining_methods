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
        
    def transfer_money(self, amount, other):
        self.account_balance -= amount
        other.make_deposit(amount)
        print(f"First User: {self.name}, Balance: ${self.account_balance}")
        print(f"Second User: {other.name}, Balance: ${other.account_balance}")
        return self

# 3 Users
tony = User('Tony', 'tony@gmail.com')
apple = User('Apple', 'apple@gmail.com')
zack = User('Zack', 'zack@gmail.com')

# 1st user
# Make 3 deposits, a withdrawal, display the balance
tony.make_deposit(300).make_deposit(350).make_deposit(150).make_withdrawal(200).display_user_balance()

# 2nd user
# Make 2 deposits, 2 withdrawals, display the balance
apple.make_deposit(200).make_deposit(300).make_withdrawal(200).make_withdrawal(150).display_user_balance()

# 3rd user
# A deposit, 3 withdrawals, display the balance 
zack.make_deposit(340).make_withdrawal(70).make_withdrawal(120).make_withdrawal(55).display_user_balance()

# BONUS
tony.transfer_money(150, apple)