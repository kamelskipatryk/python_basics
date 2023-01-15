
class Vehicle:
    def __init__(self):
        pass

    @property # get
    def gears(self):
        print('getter:', self.__gears)
        if(self.__gears > 0):
            return self.__gears
        else:
            return -1
    
    @gears.setter # set
    def gears(self, new_gears):
        print('new_gears:', new_gears)
        self.__gears = new_gears
        


vehicle_1 = Vehicle()
vehicle_1.gears = -7 # set
print(vehicle_1.gears) # get