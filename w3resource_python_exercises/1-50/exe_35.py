def are_equal(a, b):
    sum = a + b
    dif = a - b
    if a == b or sum == 5 or dif == 5:
        return True
    else:
        print('not equal')
        return False

print(are_equal(1,2))
print(are_equal(2,2))
print(are_equal(1,4))