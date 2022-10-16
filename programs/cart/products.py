class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.name) + ' ' + str(self.price)

class Phone(Product):
    def __init__(self, name, price, color):
        Product.__init__(self, name, price)
        self.color = color

    def __str__(self):
        return super().__str__() + ' ' + str(self.color)

# phone_1 = Phone('Iphone', 5000, 'red')
# print(phone_1)

class Tv(Product):
    def __init__(self, name, price, screen_size):
        super().__init__(name, price) # self automatycznie przekazane
        self.screen_size = screen_size

    def __str__(self):
        return super().__str__() + ' ' + str(self.screen_size)

# tv_1 = Tv('Samsung', 3499, 60)
# print(tv_1)
    
