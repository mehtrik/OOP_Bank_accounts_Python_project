#import bank_accounts module
from bank_accounts import *

#Create some bank accounts
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

#Get the balance of Dave and Sara's accounts
Dave.GetBalance()
Sara.GetBalance()

#Deposit into account
Sara.Deposit(500)

#Withdraw an amount that Dave does not have in his account
Dave.Withdraw(10000)
#Withdraw an amount that will work
Dave.Withdraw(10)

#Transfer an a non viable amount
Dave.Transfer(10000, Sara)
#Transfer a viable amount
Dave.Transfer(100,Sara)

#Open new account and deposit into this account
Jim = IntrestRewardsAcct(1000, "Jim")
Jim.GetBalance()
Jim.Deposit(100)

#Transfer from Jim to Dave
Jim.Transfer(100, Dave)

#create new account for Blaze
Blaze = SavingsAcct(1000, "Blaze")
Blaze.GetBalance()
Blaze.Deposit(100)
Blaze.Transfer(10000, Sara)
Blaze.Transfer(1000, Sara)