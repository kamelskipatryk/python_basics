arr = [[3,21,37],[61,79,101,120],[133,149]]

def numberInArrayOfArrays(number, arrayOfarrays):
    if number < arr[0][0]:
        return False
    
    if number > arr[len(arr)-1][-1]:
        return False

    for array in arrayOfarrays:
        if number in array:
            return True

print(numberInArrayOfArrays(0, arr))
print(numberInArrayOfArrays(3, arr))
print(numberInArrayOfArrays(101, arr))
print(numberInArrayOfArrays(149, arr))
print(numberInArrayOfArrays(221, arr))
print(numberInArrayOfArrays(79, arr))

