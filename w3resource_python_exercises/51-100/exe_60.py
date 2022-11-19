from math import sqrt
# a2 + b2 = c2

def calculate_hypotenuse(a, b):
    sum = a ** 2 + b ** 2
    c = sqrt(sum)
    return c

print(calculate_hypotenuse(4, 3))

from math import sqrt
print("Input lengths of shorter triangle sides:")
a = float(input("a: "))
b = float(input("b: "))
c = sqrt(a**2 + b**2)
print("The length of the hypotenuse is:", round(c, 2) )
