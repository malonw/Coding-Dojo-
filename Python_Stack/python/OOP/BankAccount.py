class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        balance = 0
                
    def deposit(self, amount):
        print(f"A deposit in the amount of ${amount} was made")
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        print(f"A withdraw in the amount of ${amount} was made")
        self.balance -= amount
        return self
    
    def display_Info(self):
        print(f"The Balance is: ${self.balance}, the interest rate is: {self.int_rate *100}%")
        return self

    def yield_interest(self):
        self.newbalance = (self.balance * self.int_rate) + self.balance
        self.balance= self.newbalance
        print(f"The Balance plus interest is ${self.balance}")
        
        return self
    
acct1 = BankAccount(float(.10),int(1000))
acct2 = BankAccount(float(.10),int(5000))

acct1.deposit(10000).deposit(5000).deposit(1000).withdraw(3500).display_Info().yield_interest().display_Info()
print("-------------------------------------------------------------------------")
acct2.deposit(10000).deposit(15000).withdraw(1000).withdraw(3500).withdraw(500).withdraw(500).display_Info().yield_interest().display_Info()
    