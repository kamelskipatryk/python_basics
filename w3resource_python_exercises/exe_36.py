def add_int(a,b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        return 'Not the same mate!'

print(add_int(12,22))
print(add_int(12,'not int'))

