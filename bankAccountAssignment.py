import userAccount
class BankAccount:

    def __init__(self, int_rate = 0.01, balance = 0):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdrawl(self, amount):
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

bankAccount1.deposit(300).deposit(300).deposit(400).withdrawl(600).yield_interest().display_account_info()

bankAccount2.deposit(50).deposit(50).withdrawl(20).withdrawl(30).withdrawl(40).withdrawl(50).yield_interest().display_account_info()


#Test Code Below
# bankAccount = BankAccount(.01, 100)
# bankAccount.withdraw(100)
# bankAccount.display_account_info()
# bankAccount.yield_interest()
# bankAccount.display_account_info()