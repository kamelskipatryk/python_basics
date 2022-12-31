txt = [0,1,2,3,4,5,6,7,8,9,10]
for x in txt[::2]:
    print(x)

print()

name = 'patryk'
for x in name[::2]:
    print(x)

print()

d = {'patryk': 1, 'klaudia':2, 'ktoś': 3, 'coścoś':4}
d_items = d.items()
list_d_items = list(d_items)
for x in list_d_items[::2]:
  print(x)

print()

#bonus
txt2 = ['12','24'] # 12,24 -> '12','24'

for x in txt2:
  print(x[0])


print()
#bonus2
dict1 = {'patryk': 1, 'klaudia':2, 'ktoś': 3, 'coścoś':4}
for x in dict1:
    print(x[0])

print()
# with range()
numbers = [1,2,5,6,8]
numbers_to_sum = []
for i in range(0, len(numbers), 2):
  numbers_to_sum.append(numbers[i])
  print(numbers[i])

print('numbers_to_sum 1:', sum(numbers_to_sum))

print()
# with lambda
numbers_to_sum_2 = [numbers[i] for i in range(0, len(numbers), 2)]
print('numbers_to_sum 2:', sum(numbers_to_sum_2))

print()
# with lambda + sum in 1 line
print(sum(numbers[i] for i in range(0, len(numbers), 2)))





