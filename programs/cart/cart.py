from products import *

class Cart:
    def __init__(self):
        self.__products_list = []
        self.__cart_value = 0
    
    # dodaje produkt do koszyka
    def add_product(self, product):
        # if isinstance(product, Phone) or isinstance(product, Tv):
        if isinstance(product, Product):
            self.__products_list.append(product)
            self.calculate_cart()
    
    # zlicza cene wszystkich produktów
    def calculate_cart(self): 
        self.__cart_value = 0
        for el in self.__products_list:
           self.__cart_value += el.price

    # wyświetla informację o zamówieniu
    def __str__(self):
        str_data = 'Cart info, products list:'
        for el in self.__products_list:
            str_data += '\n- ' + str(el.name) + ' ' + str(el.price)
        str_data += '\n cart value: ' + str(self.__cart_value)
        return str_data

