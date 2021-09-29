class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = 0

    def make_deposit(self,amount):
        self.account += amount
        return self
    
    def make_withdrawal(self, amount):
        self.account -= amount
        return self
    
    # def transfer_money(self, user, amount):
    #     self.account -= amount
    #     user.account += amount
    #     self.display_user_balance()
    #     user.display_user_balance()
    #     return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account} ")


user1 = User("Don Brown", "don@python.com")
user2 = User("Sarah Brown", "sarah@python.com")
user3 = User("Chris Brown", "chris@python.com")
# print(user1.name)
# print(user2.name)

user1.make_deposit(400).make_deposit(300).make_deposit(200).make_withdrawal(350).display_user_balance()
user2.make_deposit(800).make_deposit(700).make_withdrawal(300).make_withdrawal(200).display_user_balance()
user3.make_deposit(800).make_withdrawal(200).make_withdrawal(300).make_withdrawal(200).display_user_balance()