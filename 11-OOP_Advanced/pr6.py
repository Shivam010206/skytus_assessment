class BankAccount:
    def __init__(self, balance):
        self.balance = balance


class SavingsAccount(BankAccount):
    def show_balance(self):
        print("Savings Balance:", self.balance)


class CurrentAccount(BankAccount):
    def show_balance(self):
        print("Current Balance:", self.balance)


s = SavingsAccount(10000)
c = CurrentAccount(5000)

s.show_balance()
c.show_balance()