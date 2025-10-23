# OOP_Bank_accounts_Python_project

# 🏦 Object-Oriented Banking System

This project demonstrates my understanding of **Object-Oriented Programming (OOP)** in Python through the design of a simple banking system.  
It includes features like deposits, withdrawals, transfers, and account types that use **inheritance**, **encapsulation**, and **exception handling**.

---

## 📁 Project Structure

├── bank_accounts.py # Contains all the OOP class definitions
├── oop_project.py # Demonstrates how the classes interact

---

## 🚀 Features Implemented

### 1. **Encapsulation**
Each account holds its own `balance` and `name`, with methods that safely modify or access account data.

### 2. **Inheritance**
- `BankAccount` → Base class  
- `InterestRewardsAcct` → Inherits from `BankAccount` and applies a 5% interest on deposits  
- `SavingsAcct` → Inherits from `InterestRewardsAcct` and applies a $5 withdrawal fee  

### 3. **Polymorphism**
The `Deposit()` and `Withdraw()` methods are **overridden** in subclasses to modify behavior (interest and fees).

### 4. **Exception Handling**
A custom exception, `BalanceException`, prevents invalid withdrawals and transfers when funds are insufficient.

---

## 🧩 Classes Overview

### `BalanceException`
```python
class BalanceException(Exception):
    pass
```
Used to handle invalid transactions (e.g., withdrawing more than available balance).


### BankAccount

```python
class BankAccount:
    def __init__(self, initial_amount, acct_name):
        self.balance = initial_amount
        self.name = acct_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def GetBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def Deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.GetBalance()

    def ViableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def Withdraw(self, amount):
        try:
            self.ViableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.GetBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def Transfer(self, amount, account):
        try:
            print('\n**********\n\nBeginning Transfer...')
            self.ViableTransaction(amount)
            self.Withdraw(amount)
            account.Deposit(amount)
            print('\nTransfer complete!\n*********')
        except BalanceException as error:
            print(f'\nTransfer interrupted. {error}')
```

### InterestRewardsAcct
```python
class IntrestRewardsAcct(BankAccount):
    def Deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.GetBalance()
```
✅ Adds a 5% interest reward to every deposit.

### SavingsAcct
```python
class SavingsAcct(IntrestRewardsAcct):
    def __init__(self, initial_amount, acct_name):
        super().__init__(initial_amount, acct_name)
        self.fee = 5

    def Withdraw(self, amount):
        try:
            self.ViableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.GetBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
```
✅ Charges a $5 fee per withdrawal in addition to the requested amount.

### 🧠 Demonstration Script
oop_project.py shows how these classes work together.

```python
from bank_accounts import *

# Create bank accounts
Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")

# Get balances
Dave.GetBalance()
Sara.GetBalance()

# Deposit and withdraw
Sara.Deposit(500)
Dave.Withdraw(10000)  # Fails due to insufficient funds
Dave.Withdraw(10)     # Succeeds

# Transfers
Dave.Transfer(10000, Sara)  # Invalid
Dave.Transfer(100, Sara)    # Valid

# Interest rewards account
Jim = IntrestRewardsAcct(1000, "Jim")
Jim.Deposit(100)
Jim.Transfer(100, Dave)

# Savings account with withdrawal fees
Blaze = SavingsAcct(1000, "Blaze")
Blaze.Deposit(100)
Blaze.Transfer(10000, Sara)  # Fails
Blaze.Transfer(1000, Sara)   # Valid
```
🧪 Example Output
```python
Account 'Dave' created.
Balance = $1000.00

Account 'Sara' created.
Balance = $2000.00

Deposit complete.
Account 'Sara' balance = $2500.00

Withdraw interrupted: Sorry, account 'Dave' only has a balance of $1000.00
Withdraw complete.
Account 'Dave' balance = $990.00
...
```
🧰 Concepts Demonstrated
✅ Classes and Objects

✅ Constructors and Instance Attributes

✅ Method Overriding

✅ Inheritance and Polymorphism

✅ Exception Handling

✅ Encapsulation

✅ Code Reusability

# End of project
