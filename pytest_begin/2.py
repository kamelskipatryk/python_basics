'''
Przygotuj klasę Bank. Klasa powinna mieć możliwość wpłacania oraz wypłacania. W chwili inicjalizacji bank powinien zawierać puste saldo.
Nie testuj sytuacji, w której wypłacasz więcej niż to możliwe.
'''

class Bank:
    def __init__(self):
        self.amount = 0
    
    def add_money(self, money):
        self.amount += money
        return self.amount
    
    def pay_out_money(self, money):
        self.amount -= money
        return money

class TestBank:
    def test_create_bank(self):
        bank = Bank()
        assert bank.amount == 0
        assert isinstance(bank, Bank)
    
    def test_add_money(self):
        bank = Bank()
        bank.add_money(10)
        assert bank.amount == 10
    
    def test_add_money_twice(self):
        bank = Bank()
        bank.add_money(10)
        bank.add_money(10)
        assert bank.amount == 20
    
    def test_pay_out_money(self):
        bank = Bank()
        bank.add_money(10)
        money = bank.pay_out_money(10)
        assert money == 10
        assert bank.amount == 0
        




