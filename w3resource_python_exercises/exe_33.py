
def sum_int(a, b, c):
    sum = a + b + c
    if a == b or b == c or a == c:
        sum = 0
    return sum


print(sum_int(1,2,3))
print(sum_int(2,2,3))
print(sum_int(2,5,5))

