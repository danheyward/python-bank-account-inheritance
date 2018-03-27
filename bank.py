class BankAccount():
    name = 'Basic'

    def __init__(self, balance = 0):
        self.balance = balance

    def balance(self):
        print(f'{self.name} account has ${self.balance}')

    def deposit(self, amount = 0):
        self.balance = self.balance + amount
        print(f'{self.name} account has ${self.balance}')

    def withdraw(self, amount = 0):
        if (amount > self.balance):
            print(f'Not enough funds in {self.name} account!')
        else:
            self.balance = self.balance - amount
            print(f'{self.name} account has ${self.balance}')

    def accumulate_interest(self):
        self.balance = self.balance * 1.02
        print(f'{self.name} account has ${self.balance}')


class ChildrensAccount(BankAccount):
    name = "Child's"

    def __init__(self, balance = 0):
        super().__init__(balance = 0)

    def accumulate_interest(self):
        self.balance = self.balance + 10
        print(f'{self.name} account has ${self.balance}')


class OverdraftAccount(BankAccount):
    name = 'Overdraft'
    overdraft_penalty = 40

    def __init__(self, balance = 0):
        super().__init__(balance)

    def withdraw(self, amount = 0):
        if (amount > self.balance):
            self.balance = self.balance - 40
            print(f'Not enough funds in {self.name} account! Your account has been deducted ${self.overdraft_penalty}')
        else:
            self.balance = self.balance - amount
            print(f'{self.name} account has ${self.balance}')

    def accumulate_interest(self):
        if (self.balance < 0):
            print(f'No interest for accounts with negative amounts!')
        else:
            self.balance = self.balance * 1.02
            print(f'{self.name} account has ${self.balance}')


basic_account = BankAccount()
basic_account.deposit(600)
# print("Basic account has ${}".format(basic_account.balance))
basic_account.withdraw(17)
# print("Basic account has ${}".format(basic_account.balance))
basic_account.accumulate_interest()
# print("Basic account has ${}".format(basic_account.balance))
# print()

childs_account = ChildrensAccount()
childs_account.deposit(34)
# print("Child's account has ${}".format(childs_account.balance))
childs_account.withdraw(17)
# print("Child's account has ${}".format(childs_account.balance))
childs_account.accumulate_interest()
# print("Child's account has ${}".format(childs_account.balance))
# print()

overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
# print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.withdraw(17)
# print("Overdraft account has ${}".format(overdraft_account.balance))
overdraft_account.accumulate_interest()
# print("Overdraft account has ${}".format(overdraft_account.balance))
