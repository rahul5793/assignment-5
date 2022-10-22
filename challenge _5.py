#challenge 5
#handling bank account



class account:
    def __init__(self,title=None,balance=0,diposite=0):
        self.title=input("enter your name",) 
        self.balance=int(input("enter your account balance",))

    def withdrawal(self,ammount):
        self.ammount=ammount
        self.balance-=ammount

    def deposit(self,ammount):
        self.ammount=ammount
        self.balance+=ammount

    def get_balance(self):
        print("account balance:",self.balance)   

class savingaccount(account):
    def __init__(self, title=None, balance=0):
        super().__init__(title, balance)
        self.interestrate=int(input("interest rate",)) 

    def interestammount(self):
        interest_ammount=self.interestrate*self.balance/100
        print("interest_ammount")

    def display(self):
        print("self.title","self.balance","self.interestrate")


account_obj=account()
account_obj.withdrawal(int(input("enter withdrawa ammount:")))     
account_obj.get_balance()
account_obj.diposit(int(input("enter diposite ammount:")))
account_obj.get_balance() 
account_obj.display()
savingaccount_obj=savingaccount()
savingaccount_obj.interestrate()
savingaccount_obj.display()






        
             
    
