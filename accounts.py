# Student Name:- Sanket Manoj Churi
# Student ID:- 201700900

import random
import datetime


class BasicAccount:
    """Creating class BasicAccount"""
    account_number_counter = 1

    def get_ac_num(self):
        """Returns the account number in a string format."""
        self.ac_num = BasicAccount.account_number_counter
        BasicAccount.account_number_counter += 1
        return str(self.ac_num)

    def __init__(self, ac_name: str, opening_balance: float):
        """Constructor for the BankAccount class."""
        self.name = ac_name
        self.balance = opening_balance

    def __str__(self):
        """A formatted string containing the account name, account number and balance"""
        return f"Account Name: {self.name}, Account Number: {self.get_ac_num()}, Balance: {self.balance}"

    def deposit(self, amount: float):
        """Deposits the amount into the account"""
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.balance += amount

    def withdraw(self, amount: float):
        """Withdraws the amount from the Basic account"""
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} has withdrawn £{amount}.New balance is £{self.balance}")
            return
        else:
            print(f"Can not withdraw £{amount}")

    def get_available_balance(self):
        """Returns the total balance that is available in the account."""
        return self.balance

    def get_balance(self):
        """Returns the balance of the account."""
        return self.balance

    def print_balance(self):
        """Print balance of the account."""
        print(f"Balance: {self.balance}")

    def get_name(self):
        """Returns the name of the account holder."""
        return self.name

    def issue_new_card(self):
        """Generates a new card number along with card expire."""
        self.card_num = str(random.randint(1000000000000000, 9999999999999999))
        expire_year = datetime.date.today().year + 3
        self.card_exp = (datetime.date.today().month, expire_year % 100)
        return self.card_num, self.card_exp

    def close_account(self):
        """Close the Basic bank account"""
        if self.balance < 0:
            print(f"Can not close account due to customer being overdrawn by £{abs(self.balance)}")
            return False
        else:
            self.withdraw(self.balance)
            return True


class PremiumAccount(BasicAccount):
    """Creating class PremiumAccount"""
    def __init__(self, ac_name: str, opening_balance: float, initial_overdraft: float):
        """Constructor for the PremiumAccount class."""
        super().__init__(ac_name, opening_balance)
        self.overdraft = False
        self.overdraft_limit = initial_overdraft

    def __str__(self):
        """A formatted string containing the account name, balance, overdraft, and overdraft limit."""
        return f"Account Name: {self.name}, Balance: {self.balance}, Overdraft: {self.overdraft}, Overdraft Limit: {self.overdraft_limit}"

    def withdraw(self, amount: float):
        """Withdraws the stated amount from the Premium account"""
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"{self.name} has withdrawn £{amount}.New balance is £{self.balance}")
            return
        else:
            raise ValueError(f"Can not withdraw £{amount}")

    def set_overdraft_limit(self, new_limit: float):
        """Sets the overdraft limit"""
        self.overdraft_limit = new_limit

    def get_available_balance(self):
        """Returns the total balance that is available in the Premium account."""
        return self.balance + self.overdraft_limit

    def print_balance(self):
        """Prints balance of the Premium account."""
        if self.overdraft:
            print(f"Balance: {self.balance}, Available Balance: {self.get_available_balance()}, Overdraft: {self.overdraft}, Overdraft Limit: {self.overdraft_limit}")
        else:
            print(f"Balance: {self.balance}, Available Balance: {self.get_available_balance()}")

    def close_account(self):
        """Close the Premium bank account."""
        if self.get_available_balance() < 0:
            print(f"Can not close account due to customer being overdrawn by £{abs(self.balance)}")
            return False
        else:
            return True
