
def add_number(a, b):
    return a + b

def sub_number(a, b):
    return a - b

def multiply_number(a, b):
    return a * b

def division_number(a, b):
    return a / b

def add_4_numbers(a, b, c, d):
    result = a + b + c + d
    return result

print(add_number(5, 10)) # 15
print(sub_number(5, 10)) # -5
print(add_4_numbers(5, 10, 10, 15)) # 40

number = multiply_number(2,6)
print(number) # 12

number_2 = division_number(100, add_number(10,10))
print(number_2) # 5.0

print(number_2/2)


