list = [-1, 2,-3,-4,-5,-6,-7]

max_value = list[0]

for i in range(1, len(list)):
    if list[i] > max_value:
       max_value = list[i]

print(max_value)