import random
import datetime


class BasicAccount:
    account_counter = 0

    def generate_account_number(self):
        account_number = BasicAccount.account_counter
        BasicAccount.account_counter += 1
        return account_number

    def generate_card_number(self):
        return random.randint(1000000000000000, 9999999999999999)

    def generate_card_expire(self):
        current_year = datetime.date.today().year
        month = random.randint(1, 12)
        year = random.randint(current_year, current_year + 3)
        return f"{month:02d}/{year % 100:02d}"

    def __init__(self, acc_name: str, opening_balance: float):
        self.name = acc_name
        self.ac_num = self.get_ac_num()
        self.balance = opening_balance
        card_number = self.generate_card_number()
        self.card_num = card_number
        card_expire = self.generate_card_expire()
        self.card_exp = card_expire

    def deposit(self, amount: float):
        self.balance += amount
        return amount

    def get_balance(self):
        return self.balance

    def withdraw(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            print(self.name, " has withdrawn £", amount, ".New balance is £", self.balance)
            return
        else:
            print("Can not withdraw £", amount)

    def get_available_balance(self):
        available_balance = self.get_balance() - self.withdraw()
        return available_balance

    def get_name(self):
        return self.name
    
    def get_ac_num(self):
        ac_num = BasicAccount.account_counter
        BasicAccount.account_counter += 1
        return ac_num
    
    def issue_new_card(self):
        current_year = datetime.date.today().year
        month = random.randint(1, 12)
        year = random.randint(current_year, current_year + 3)
        card_exp = f"{month:02d}/{year % 100:02d}"
        return card_exp
