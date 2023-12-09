import random
import datetime


class BasicAccount:
    account_number_counter = 1

    # def generate_account_number(self):
    #     account_number = BasicAccount.account_number_counter
    #     BasicAccount.account_number_counter += 1
    #     return account_number

    # def generate_card_number(self):
    #     return random.randint(1000000000000000, 9999999999999999)

    # def generate_card_expire(self):
    #     current_year = datetime.date.today().year
    #     month = datetime.date.today().month
    #     year = current_year + 3
    #     return f"({month}/{year % 100:02d})"

    def get_ac_num(self):
        Accou_num = BasicAccount.account_number_counter
        # print('Accou_num',Accou_num)
        BasicAccount.account_number_counter += 1
        return str(Accou_num)

    def __init__(self, acc_name: str, opening_balance: float):
        self.name = acc_name
        self.ac_num = (self.get_ac_num())
        # print('self.ac_num',self.ac_num)
        self.balance = opening_balance

    def __str__(self):
        return f"Account Name: {self.name}, Account Number: {self.ac_num}, Balance: {self.balance}"

    def deposit(self, amount: float):
        if amount <= 0:
            print("Deposit amount must be positive")
        else:
            self.balance += amount

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} has withdrawn £{amount}. New balance is £{self.balance}")
            return 
        else:
            raise ValueError(f"Can not withdraw £{amount}")

    def get_available_balance(self):
        available_balance = self.get_balance() - self.withdraw()
        return available_balance

    def get_balance(self):
        return self.balance

    def print_balance(self):
        print(f"Balance: {self.balance}")

    def get_name(self):
        return self.name

    def issue_new_card(self):
        self.card_num = str(random.randint(1000000000000000, 9999999999999999))
        expire_year = datetime.date.today().year + 3
        self.card_exp = (datetime.date.today().month, expire_year % 100)
        return self.card_num, self.card_exp

    def close_account(self):
        if self.balance < 0:
            print(f"Can not close account due to customer being overdrawn by £{abs(self.balance)}")
            return False
        else:
            self.withdraw(self.balance)
            return True

# account1 = BasicAccount( "John Doe", 1000)
# account2 = BasicAccount( "Rose Ado", 1000)
# account3 = BasicAccount( "Mary lolu", 1000)
# print('account1',type(account1.ac_num),type(account1.get_ac_num()))
# print('account2',account2.ac_num)
# print('account3',account3.ac_num)


class PremiumAccount(BasicAccount):
    def __init__(self, ac_name: str, opening_balance: float, initial_overdraft: float):
        super().__init__(ac_name, opening_balance)
        self.overdraft = False
        self.overdraft_limit = initial_overdraft

    def __str__(self):
        return f"Account Name: {self.name}, Balance: {self.balance}, Overdraft: {self.overdraft}, Overdraft Limit: {self.overdraft_limit}"

    def set_overdraft_limit(self, new_limit: float):
        self.overdraft_limit = new_limit

    def get_available_balance(self):
        if self.balance >= 0:
            return self.balance
        elif self.balance < -self.overdraft_limit:
            self.overdraft = True
            return 0.0
        else:
            self.overdraft = True
            return self.balance + self.overdraft_limit

    def print_balance(self):
        if self.overdraft:
            print(f"Balance: {self.balance}, Available Balance: {self.get_available_balance()}, Overdraft: {self.overdraft}, Overdraft Limit: {self.overdraft_limit}")
        else:
            print(f"Balance: {self.balance}, Available Balance: {self.get_available_balance()}")

    def close_account(self):
        if self.get_available_balance() > 0:
            print("Account cannot be closed. There is a balance.")
            return False
        else:
            self.card_num = None
            self.card_exp = None
            self.balance = 0.0
            self.overdraft = False
            self.overdraft_limit = 0.0
            return True
