# Python3 code to demonstrate working of
# Check if element is present in tuple
# using loop

# initialize tuple
tup_1 = (10, 2, 3, 4, 5)
tup_2 = (6, 7, 8, 9, 10)

# printing original tuples
print('The tuple number 1 : ' + str(tup_1))
print('The tuple number 2 : ' + str(tup_2))

#set
result = set(tup_1) & set(tup_2)

if result:
	print('There are common elements in tuples', result)
else:
	print('There are not common elements in tuples.')

#for lopp
for x in tup_1:
	for y in tup_2:
		if (x == y):
			print(x)
			break


tup_3 = (10, 2, 3, 4, 5)
tup_4 = (6, 7, 8, 9, 10, 2, 3, 4, 5)
#if all elements cantains other tuple
def whole_tup_in_tup(tup_3, tup_4):
	for x in tup_3:
		if x not in tup_4:
			return False
	return True

print(whole_tup_in_tup(tup_3, tup_4))
			
# printing result
# print("Does tuples contains same value ? : " + str(ele))
