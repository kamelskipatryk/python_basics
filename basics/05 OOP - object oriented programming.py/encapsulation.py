
class Vehicle:
    def __init__(self, brand, name):
        self.brand = brand
        self.name = name
        self.__gears = 5 # prywatna zmienna

    def __get_gears_info_str(self): # prywatna metoda
        return 'gears number ' + str(self.__gears)
    
    def print_info(self):
        print(self.brand, self.name, self.__get_gears_info_str())

vehicle_1 = Vehicle('Dodge', 'Charger')
# print(vehicle_1.__gears) # AttributeError: 'Vehicle' object has no attribute '__gears'
print(vehicle_1.brand)
# vehicle_1.__get_gears_info_str() # AttributeError: 'Vehicle' object has no attribute '__get_gears_info_str'.
vehicle_1.print_info()
print()

class Car(Vehicle):
    def __init__(self, brand, name):
        Vehicle.__init__(self, brand, name)
        # print(self.__gears) # AttributeError: 'Car' object has no attribute '_Car__gears' -> w klasie pochodnej nie mamy dostępu do "prywatnych zmiennych" innej klasy

car_1 = Car('Ford', 'Mustang')

# name mungling
print(vehicle_1._Vehicle__gears) # 5 NIEZALECANE
print(vehicle_1._Vehicle__get_gears_info_str()) # gears number 5 NIEZALECANE
