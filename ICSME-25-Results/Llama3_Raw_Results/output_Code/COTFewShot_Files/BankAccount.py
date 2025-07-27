class BankAccount:
    def __init__(self, balance=0):
        # Initialize a bank account object with an attribute balance, default value is 0.
        self.balance = balance

    def deposit(self, amount):
        # Deposit a certain amount into the account, increasing the account balance, return the current account balance.
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        # Withdraw a certain amount from the account, decreasing the account balance, return the current account balance.
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        return self.balance

    def view_balance(self):
        # Return the account balance.
        return self.balance

    def transfer(self, other_account, amount):
        # Transfer a certain amount from the current account to another account.
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        other_account.balance += amount
        return self.balance