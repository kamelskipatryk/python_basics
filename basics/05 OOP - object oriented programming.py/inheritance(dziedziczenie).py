

class Vehicle:
    def __init__(self):
        self.brand = 'unknown'
        self.name = 'unknown'
        self.top_speed = 100
        self.num_wheels = 4

    def print_vehicle_info(self):
        print(self.brand, self.name, self.top_speed)

vehicle_1 = Vehicle()
vehicle_1.print_vehicle_info() # unknown unknown 100

class Car(Vehicle): # Car dziedziczy po Vehicle
    def print_car_info(self):
        # można nadpisac odziedziczone atrubuty
        self.brand = 'Ford'
        self.name = 'Mustang'
        print('Car brand:', self.brand)
        print('Car name:', self.name)
        #self.print_vehicle_info()

car_1 = Car()
car_1.print_vehicle_info() # unknown unknown 100
car_1.print_car_info() # Car brand: Ford \nCar name: Mustang
car_1.print_vehicle_info() # Ford Mustang 100
