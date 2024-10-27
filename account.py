#Account as a BASE Class
class Account:
    def __init__(self, account_holder:int, balance:int, account_type:str):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type
    
    def deposit(self, amount:int):
        if amount > 0:
            self.balance += amount
            print(f"{amount} is added into the account {self.account_holder}")
        else:
            print("Invalid amount")
    
    def withdraw(self, amount:int):
        if 0 < amount < self.balance:
            self.balance -= amount
            print(f"{amount} is withdrawn from the account {self.account_holder}")
        elif amount > self.balance:
            print("Can't withdraw any more :(") # handles any overdraft
        else:
            print("Insufficient amount :(")

    def check_balance(self):
        print(f"acount {self.account_holder} has balance = {self.balance} with {self.account_type} type")
    
    
class Savings(Account):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance, 'savings')
        self.interest_rate = interest_rate
        
    def add_interest(self):
        self.balance += self.balance * self.interest_rate / 100
        print(f"Interest added, New balance: {self.balance}")
    


class Checking(Account):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance, 'checking')
        self.overdraft_limit = overdraft_limit
        
        

class Transfer:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        
    def transfer(self):
            if self.sender.balance >= self.amount:
                    self.sender.withdraw(self.amount)
                    self.receiver.deposit(self.amount)
                    print(f"account {self.sender.account_holder} has successfully transferred {self.amount} into account {self.receiver.account_holder}")
            else:
                print(f"There is no enough balance in account {self.sender}")