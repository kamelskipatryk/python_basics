array = [1,2,3,4]
array_2 = [-1,-2,-3,-4]
array_3 = []
array_4 = [5,5,5]
array_5 = [1,2]

def sum_int(table):
    sum_total = 0
    index = 0
    if table:
        for number in table:
                sum = index * number
                print('sum: ' + str(sum))
                sum_total += sum
                index += 1
                print('sum_total: ' + str(sum_total))
    else:
        print('Empty list: ' + str(sum_total))

def sum_index_multiplier(nums):
	return sum(j*i for i, j in enumerate(nums))


sum_int(array)
print(sum_index_multiplier(array))
print('')
sum_int(array_2)
print('')
sum_int(array_3)
print('')
sum_int(array_4)
print(sum_index_multiplier(array_4))
print(bool(array_4))
print('')
sum_int(array_5)
print(sum_index_multiplier(array_5))