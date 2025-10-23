#Create an empty class to create a possible exception error for withdrawing from the account
class BalanceException(Exception):
    pass

#Create class 'BankAccount'
class  BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    #Create method to get the output of the balance of the account
    def GetBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    #Create method to deposit an amount into account
    def Deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.GetBalance()
    
    #Create a viable transaction method
    def ViableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    #Create a withdraw method
    def Withdraw(self, amount):
        try:
            self.ViableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.GetBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    #Create a transfer method between accounts
    def Transfer(self, amount, account):
        try:
            print('\n**********\n\nBegining Trasfer...')
            self.ViableTransaction(amount)
            self.Withdraw(amount)
            account.Deposit(amount)
            print('\nTransfer complete!\n*********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. {error}')

#Use inheritance from the BankAccount class to create a new intrest account
class IntrestRewardsAcct(BankAccount):
    def Deposit(self, amount):
        self.balance = self.balance + (amount*1.05)
        print("\nDeposit complete.")
        self.GetBalance()

#Create savings account that inherits from the intrest rewards account but with an additional fee
class SavingsAcct(IntrestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    #overide the Withdraw method
    def Withdraw(self, amount):
        try:
            self.ViableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.GetBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

