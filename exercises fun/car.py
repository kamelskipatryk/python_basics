class Car:
    
    def __init__(self):
        
        self.__engine = False
        self.__gear = 0
        self.__speed = 0
        self.__drive_mode = False
        self.__park_mode = True
        
    def turn_on(self):
        self.__engine = True
    
    def turn_off(self):
        self.__engine = False
    
    def turn_drive_mode_on(self):
        self.__drive_mode = True
        self.__park_mode = False
    
    def turn_park_mode_on(self):
        self.__park_mode = True
        self.__drive_mode = False

    def __next_gear(self):
        if self.__gear < 6: self.__gear += 1; print('gear', self.__gear)
        elif self.__gear == 6: print('You have max gear!')
            
    def __previous_gear(self):
        if self.__gear > 0: self.__gear -= 1; print('gear', self.__gear)
            
    def speed_up(self):
        if self.__drive_mode == True and self.__engine == True:
            self.__speed += 10
            print('speed after speed up', self.__speed)
            self.__next_gear()
        else:
            print('Turn drive mode on!')
        
    def brake(self):
        if self.__speed >= 60: self.__speed -= 10
        elif self.__speed >= 10 and self.__speed < 60:
            self.__speed -= 10
            self.__previous_gear()
        else: self.__speed = 0
        print('speed after brake:', self.__speed)
    
car = Car()
car.turn_on()

car.speed_up()
car.brake()

car.turn_drive_mode_on()
car.speed_up()
car.speed_up()
car.speed_up()
car.speed_up()
car.speed_up()
car.speed_up()
car.speed_up()
car.speed_up()
car.speed_up()

car.brake()
car.brake()
car.brake()
car.brake()
car.brake()
car.brake()
car.brake()
car.brake()
car.brake()
car.brake()

car.turn_park_mode_on()
car.speed_up()
car.turn_off()