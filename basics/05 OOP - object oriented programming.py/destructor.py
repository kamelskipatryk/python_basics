
class Car:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)

    def __del__(self):
        print('Obiekt usunięty!')

car_1 = Car('Ferrari')
car_1.print_info()
# del car_1 -> usuwanie ręczne z pamięci, na końcu programu destruktor wykona się automatycznie
# car_1.print_info() -> NameError: name 'car_1' is not defined

print(' ')

class Dog:
    def __init__(self):
        print('Konstruktor')

    def __del__(self): # destruktor się wykona, ponieważ zakończy się program i musi być posprzątana pamięć przez garbage collector
        print('Destruktor')

dog_1 = Dog()

