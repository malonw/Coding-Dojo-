class bank:
    # This class contains account information
    def __init__(self, username, account_balance ):
        User.name = username
        self.account = account_balance
        account_balance = 0
        
        

class User(bank):
    # This class is the User Information
    def __init__(self, username, email_address) :
        self.name = username
        self.email = email_address
        bank.account_balance = 0
    
        
    # adding a deposit method
    def make_deposit(self, amount):
        print(f"{self.name} made a deposit in the amount of ${amount}")
        self.account_balance += amount
        return self

    # addomg a withdrawl method
    def make_withdrawl(self, amount):
        print(f"{self.name} made a withdrawl in the amount of ${amount}")
        self.account_balance -= amount
        return self
    # adding a display balance method
    def display_user_balance(self):
        print(f"User: {self.name}: Balance: ${ self.account_balance}")
        print("--------------------------------------------------------")
        return self
    # adding a transfer money
    def transfer_money(self,username,amount):
        # print(f"{self.name} transfered ${amount} to {username}")  #How to get name of user transfered to!
        
        self.account_balance -= amount
        username.account_balance += amount
        return self
        
        

# Instances
guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
# add thrid user
code = User("code Review", "codereview@isneeded.com")
# Have 1 user make 3 deposits and 1 withdrawl and then display their balance

guido.make_deposit(100).make_deposit(2000).make_deposit(500).display_user_balance().make_withdrawl(75).display_user_balance()
# Have 2nd user make 2 deposits and 2 withdrawls and then display their balance.
monty.make_deposit(50).make_deposit(5000).make_withdrawl(500).make_withdrawl(1000).display_user_balance()
# Have the third user make 1 deposi and 3 withdrawls and then display their balance
code.make_deposit(10000).make_withdrawl(1000).make_withdrawl(1500).make_withdrawl(1750).display_user_balance()
# Bonus Add a Transfer money method, have the first user transfer money to the third user and then print both users' balance
guido.transfer_money(code,1000).display_user_balance()
code.display_user_balance()

