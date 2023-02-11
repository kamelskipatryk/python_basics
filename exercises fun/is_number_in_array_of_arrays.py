arr2 = [[3,21,37],[61,79,101,120],[133,149]]

def numberInArrayOfArrays(number, arrayOfarrays):
    if number < arrayOfarrays[0][0]:
        return False
    
    if number > arrayOfarrays[len(arrayOfarrays)-1][-1]:
        return False

    for array in arrayOfarrays:
        if number in array:
            return True

print(numberInArrayOfArrays(0, arr2))
print(numberInArrayOfArrays(3, arr2))
print(numberInArrayOfArrays(101, arr2))
print(numberInArrayOfArrays(149, arr2))
print(numberInArrayOfArrays(221, arr2))
print(numberInArrayOfArrays(79, arr2))

