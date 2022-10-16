from cart import *

phone_1 = Phone('Iphone', 5000, 'red')
tv_1 = Tv('Samsung', 3499, 60)

cart = Cart()
cart.add_product(phone_1)
cart.add_product(tv_1)
print(cart)