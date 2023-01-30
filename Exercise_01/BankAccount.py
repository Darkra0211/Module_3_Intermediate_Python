BankAccount
class BankAccount:


    Account_name  = ""
    Account_balance = 0
    def __init__(self,name,balance):
        self.Account_name = name
        self.Account_balance= balance


    def deposit(self,int):
        self.Account_balance = self.Account_balance + int
   
    def withdraw(self,int):
        self.Account_balance = self.Account_balance - int
   
    def get_Balance(self):
        print(str(self.Account_name) + " has a balance of " + str(self.Account_balance))
