BasicAccount

+ name : string
+ ac_num : int
+ balance : float
+ card_num : string
+ card_exp : tuple(int, int)

+ __init__(self : BasicAccount, ac_name: string, opening_balance : float)
+ __str__(self : BasicAccount) : string
+ deposit (self: BasicAccount, amount : float)
+ withdraw(self : BasicAccount, amount : float)
+ get_available_balance (self: BasicAccount) float
+ get_balance (self: BasicAccount): float
+ print_balance (self: BasicAccount)
+ get_name(self: BasicAccount) : string
+ get_ac_num(self: BasicAccount): string
+ issue_new_card(self: BasicAccount)
+ close_account(self: BasicAccount) : boolean


PremiumAccount

+ overdraft : boolean
+ overdraft_limit : float

+ _init__(self : PremiumAccount, ac_name : string, opening_balance : float, initial_overdraft : float)
+ _str__(self : PremiumAccount) : string
+ set_ovedraft_limit(self : PremiumAccount, new_limit: float)
+ get_available_balance (self : PremiumAccount): float
+ print_balance (self: PremiumAccount)
+ close_account(self : PremiumAccount) : boolean
The variables of the classes are described as follows:
(note that these are not class variables, but instance variables. You'll have to decide whether to use class variables and how).

name – the account holder's name.

ac_num – the number of the account. This should be “serial”, meaning that the first account to be created should have number 1, the second account to be created should have number 2, and so on.

balance – The balance (in pounds) of the account.

card_num – The card number, which should be a string containing a 16-digit number (you should import and use the random module for this).

card_exp - a tuple, where the first element is an integer corresponding to the month and the second element is 2-digit year. Eg: 03/23 represents March 2023. (you should import and use the datetime module for this).

overdraft – a Boolean variable, which is True if the account has an overdraft, and False if  does not.

overdraft_limit – The amount that the account can go overdrawn by.

 

 

Methods:

 

The methods are as follows:

__init__(self, str, float)

Initialiser giving the account name and opening balance.

__init__(self, str, float, float) for the Premium account
initialiser giving the account name, opening balance, and overdraft limit (0 or above).

deposit(self, float)
Deposits the stated amount into the account, and adjusts the balance appropriately. Deposits must be a positive amount.

withdraw(self, float)
Withdraws the stated amount from the account, prints a message of “<Name> has withdrawn £<amount>. New balance is £<amount>”.
If an invalid amount is requested, then the following message should be printed, and the method should then terminate: “Can not withdraw £<amount>".
An amount is considered to be invalid if it is larger than the balance for (normal) accounts and if it is larger than the balance + overdraft limit for premium accounts.

get_available_balance(self)
Returns the total balance that is available in the account as a float. It should also take into account any overdraft that is available.

get_balance(self)
returns the balance of the account as a float. If the account is overdrawn, then it should return a negative value.


print_balance(self)
Should print to screen in a sensible way the balance of the account. If an overdraft is available, then this should also be printed and it should show how much overdraft is remaining.
get_name(self)
Returns the name of the account holder as a string.

get_ac_num(self)
Returns the account number as a string.

issue_new_card(self)
Creates a new card number, with the expiry date being 3 years to the month from now (e.g., if today is 1/12/21, then the expiry date would be (12/24)).

close_account(self)
To be called before deleting of the object instance. Returns any balance to the customer (via the withdraw method) and returns True.
Returns False if the customer is in debt to the bank, and prints message “Can not close account due to customer being overdrawn by £<amount>”.
You should not actually delete the account instance. This function will simply do the relevant "housekeeping" in the account, and return a Boolean value.

set_overdraft_limit(self, float)
Sets the overdraft limit to the stated amount

 

In addition to the above, you must also define suitable string representations that give the account name, available balance, and overdraft details (that is: you need to also implement the __str__ methods for each class).

