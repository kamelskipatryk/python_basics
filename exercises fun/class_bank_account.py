class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

account = BankAccount()
print(account.balance)  # 0
account.deposit(1000)
print(account.balance)  # 1000
account.deposit(2000)
print(account.balance)  # 3000
res = account.withdraw(1500)
print(res)  # True
print(account.balance)  # 1500
res = account.withdraw(2000)
print(res)  # False
print(account.balance)  # 1500