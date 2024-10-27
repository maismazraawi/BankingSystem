from account import Account, Savings, Checking, Transfer


#for a collection of accounts
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account_holder:int, balance:int, account_type:str):
        if account_type == 'savings':
            new_account = Savings(account_holder, balance, interest_rate=0.03)
        elif account_type == 'checking':
            new_account = Checking(account_holder, balance, overdraft_limit= 300)
        self.accounts.append(new_account)
        print(f"Account for {account_holder} added.")
        
    def get_account(self, account_holder: int):
        for account in self.accounts:
            if account.account_holder == account_holder:
                return account
        return None

    #now accessing the methods to control them according to bank accounts:
    def deposit(self, account_holder:int, amount:int):
        account = self.get_account(account_holder)
        if account:
            account.deposit(amount)
            
    def withdraw(self, account_holder:int, amount:int):
        account = self.get_account(account_holder)
        if account:
            account.withdraw(amount)
    
    def add_interest(self, account_holder:int):
        account = self.get_account(account_holder)
        if isinstance(account, Savings):
            account.add_interest()
        else:
            print(f"account {account_holder} isn't a savings account, cannot add interest ...")
    
    def transfer(self, sender:int, receiver:int, amount:int):
        sender = self.get_account(sender)
        receiver = self.get_account(receiver)
        if sender and receiver:
            transferring = Transfer(sender, receiver, amount)
            transferring.transfer()
        else:
            print("Either sender or receiver account not found...")
            
    def check_balance(self, account_holder:int):
        account = self.get_account(account_holder)
        if account:
            account.check_balance()
        else:
            print("Account not found...")
            
    
### accounts:    
bank = Bank()
acount1 = bank.add_account(account_holder=1, balance=200, account_type='savings')
acount2 = bank.add_account(account_holder=2, balance=200, account_type='checking')

bank.withdraw(account_holder=1, amount=50)
bank.add_interest(account_holder=1)

bank.deposit(account_holder=2, amount=50)
bank.add_interest(account_holder=2)

bank.transfer(sender=1, receiver=2, amount=100)
bank.check_balance(account_holder=2)