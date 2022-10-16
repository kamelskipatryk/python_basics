
class Car:
    def __init__(self, brand, name, color, year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year
        self.mileage = 1
        # print('Wywołanie konstruktora', self.brand, self.name) # wywołanie konstruktora następuje od razu po stworzeniu nowego obiektu danej klasy
        self.set_top_speed(240)
        self.print_info()

    def print_info(self):
        print(self.brand, self.name, self.color, self.year, self.mileage, self.top_speed)

    def set_top_speed(self, top_speed):
        self.top_speed = top_speed

mustang = Car('Ford', "Mustang", 'red', 1970)
mustang.mileage = 100
# mustang.top_speed = 230 # dodanie nowej zmiennej wewnętrznej do obiektu mustang
mustang.print_info()
# mustang.print_info()
# print(mustang.top_speed) # 230


charger = Car('Dodge', 'Charger', 'blue', 1971)
charger.set_top_speed(213)
charger.print_info()