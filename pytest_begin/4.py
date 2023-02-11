'''
Rozwiń zadanie 2, w taki sposób by nie mozna było wypłacić więcej niż jest w kasie. W takim przypadku program powinien wyrzucić wyjątek.
'''

import pytest

class Bank:
    def __init__(self):
        self.amount = 0
    
    def add_money(self, money):
        self.amount += money
        return self.amount
    
    def pay_out_money(self, money):
        if money > self.amount:
            raise NotEnoughMoney('You dont have that amount of money!')
        self.amount -= money
        return money

class NotEnoughMoney(Exception):
    pass

class TestBank:
    def test_pay_out_money_over_amount(self):
        with pytest.raises(NotEnoughMoney):
            bank = Bank()
            bank.pay_out_money(200)
        
