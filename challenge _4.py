# challenge 4 saving account


class account:
    def __init__(self,title=None,balance=0):
        self.title=title
        self.balance=balance

class saving_account(account):
    def __init__(self,title=None,balance=0,intrest_rate=0):
        super().__init__(title,balance)
        self.intrest_rate=intrest_rate


account_obj=account("asish",5000)
saving_account_obj=saving_account("ashish",5000,5)
print(saving_account_obj.title)
print(saving_account_obj.balance)
print(saving_account_obj.intrest_rate)











