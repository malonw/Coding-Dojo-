class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        self.acct_num = 1234
        
        
    def deposit(self, amount):
        print(f"A deposit in the amount of ${amount} in acct #{self.acct_num} ")
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance >= amount :
            print(f"A withdraw in the amount of ${amount} from acct #{self.acct_num}")
            self.balance -= amount
        else:
            print("-------------------------------------------------------------------------------")
            print(f"Insufficient Balance!\nThe amount of ${amount} is more than your available balance of ${self.balance}")
        return self
    
    def display_Info(self):
        print(f"The Balance of acct #{self.acct_num} is: ${self.balance}, the interest rate is: {self.int_rate *100}%")
        print("-------------------------------------------------------------------------------")

        return self

    def yield_interest(self):
        self.newbalance = (self.balance * self.int_rate) + self.balance
        self.balance= self.newbalance
        print(f"The Balance plus interest in acct #{self.acct_num} is ${self.balance}")
        
        return self
    

class User:
    # This class is the User Information
    def __init__(self, username, email_address) :
        self.name = username
        self.email = email_address
        self.account = BankAccount(int_rate=0.02, balance = 0)
                

bob = User("Bob Cat", "bobcat@meow.com")    
bob.account.deposit(10000).deposit(50000).withdraw(2000).withdraw(200000).display_Info().yield_interest().display_Info()   
    