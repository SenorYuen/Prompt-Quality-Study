class BankAccount:
    # Constructor to initialize a bank account object with an attribute balance
    def __init__(self, balance=0):
        """
        Initialize a bank account object with an attribute balance.
        
        Args:
            balance (int): The initial balance of the account. Defaults to 0.
        """
        self.balance = balance

    # Method to deposit a certain amount into the account
    def deposit(self, amount):
        """
        Deposit a certain amount into the account, increasing the account balance.
        
        Args:
            amount (int): The amount to be deposited.
        
        Returns:
            int: The current account balance.
        
        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        self.balance += amount
        return self.balance

    # Method to withdraw a certain amount from the account
    def withdraw(self, amount):
        """
        Withdraw a certain amount from the account, decreasing the account balance.
        
        Args:
            amount (int): The amount to be withdrawn.
        
        Returns:
            int: The current account balance.
        
        Raises:
            ValueError: If the amount is negative or exceeds the account balance.
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    # Method to return the account balance
    def view_balance(self):
        """
        Return the account balance.
        
        Returns:
            int: The current account balance.
        """
        return self.balance

    # Method to transfer a certain amount from the current account to another account
    def transfer(self, other_account, amount):
        """
        Transfer a certain amount from the current account to another account.
        
        Args:
            other_account (BankAccount): The account where the money will be transferred.
            amount (int): The amount to be transferred.
        
        Returns:
            None
        """
        if amount < 0:
            raise ValueError("Invalid amount")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        other_account.balance += amount