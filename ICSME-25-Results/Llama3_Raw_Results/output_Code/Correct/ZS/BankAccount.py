# This is a class as a bank account system, which supports deposit money, withdraw money, view balance, and transfer money.

class BankAccount:
    def __init__(self, balance=0):
        # Initializes a bank account object with an attribute balance, default value is 0.
        self.balance = balance  # Set the initial balance

    def deposit(self, amount):
        # Deposits a certain amount into the account, increasing the account balance, return the current account balance.
        # If amount is negative, raise a ValueError("Invalid amount").
        if amount < 0:  # Check if amount is negative
            raise ValueError("Invalid amount")
        self.balance += amount  # Increase the account balance
        return self.balance  # Return the current account balance

    def withdraw(self, amount):
        # Withdraws a certain amount from the account, decreasing the account balance, return the current account balance.
        # If amount is negative, raise a ValueError("Invalid amount").
        # If the withdrawal amount is greater than the account balance, raise a ValueError("Insufficient balance.").
        if amount < 0:  # Check if amount is negative
            raise ValueError("Invalid amount")
        if amount > self.balance:  # Check if withdrawal amount is greater than the account balance
            raise ValueError("Insufficient balance.")
        self.balance -= amount  # Decrease the account balance
        return self.balance  # Return the current account balance

    def view_balance(self):
        # Return the account balance.
        return self.balance  # Return the current account balance

    def transfer(self, other_account, amount):
        # Transfers a certain amount from the current account to another account.
        if amount < 0:  # Check if amount is negative
            raise ValueError("Invalid amount")
        if amount > self.balance:  # Check if transfer amount is greater than the account balance
            raise ValueError("Insufficient balance.")
        self.balance -= amount  # Decrease the account balance
        other_account.balance += amount  # Increase the other account balance
        return self.balance  # Return the current account balance

# Example usage:
if __name__ == "__main__":
    account1 = BankAccount(1000)  # Create a bank account with initial balance 1000
    account2 = BankAccount(500)  # Create another bank account with initial balance 500
    
    print("Account 1 initial balance:", account1.view_balance())  # View account 1 balance
    print("Account 2 initial balance:", account2.view_balance())  # View account 2 balance
    
    account1.deposit(500)  # Deposit 500 into account 1
    print("Account 1 balance after deposit:", account1.view_balance())  # View account 1 balance
    
    account1.withdraw(200)  # Withdraw 200 from account 1
    print("Account 1 balance after withdrawal:", account1.view_balance())  # View account 1 balance
    
    account1.transfer(account2, 300)  # Transfer 300 from account 1 to account 2
    print("Account 1 balance after transfer:", account1.view_balance())  # View account 1 balance
    print("Account 2 balance after transfer:", account2.view_balance())  # View account 2 balance