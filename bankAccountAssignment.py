# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

class BankAccount:

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if (self.balance < amount):
            print(f"Insufficient Funds: Charging a $5")
            self.balance -= 5
            self.balance -= amount
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    
    def yield_interest(self):
        if (self.balance > 0):
            self.balance += self.int_rate * self.balance
        else:
            print("Not Enough Money!")
        return self


bankAccount1 = BankAccount()
bankAccount2 = BankAccount()
#self referes to the object that performs the method during a method call

bankAccount1.deposit(300).deposit(300).deposit(400).withdraw(600).yield_interest().display_account_info()

bankAccount2.deposit(50).deposit(50).withdraw(20).withdraw(30).withdraw(40).withdraw(50).yield_interest().display_account_info()


#Test Code Below
# bankAccount = BankAccount(.01, 100)
# bankAccount.withdraw(100)
# bankAccount.display_account_info()
# bankAccount.yield_interest()
# bankAccount.display_account_info()