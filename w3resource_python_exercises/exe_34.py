def sum_int(a, b):
    sum = a + b 
    if sum in range(15,21):
        sum = 20
    return sum

print(sum_int(1,2))
print(sum_int(15,16))
print(sum_int(15,4))


