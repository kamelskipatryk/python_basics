tup_1 = ([0,1,2,'start'],[4,5,6,7])

print(tup_1[1][3])

dict = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5}
tup_from_dict = dict.items() # give me 2 tuples in the list
print(tup_from_dict) # dict_items([('sms', 1), ('email', 2)])
print(type(tup_from_dict))

# sort by keys
for tup in sorted(tup_from_dict):
    print(tup[0], tup[1])
    
# sort by values
print('')
for k, v in sorted(tup_from_dict, reverse=True):
    print(v, k)
print('')

# sort by values -> Python 3.6 and down
tmp = []

for k, v in tup_from_dict:
    tmp.append((v, k))

print(tmp) # [(1, 'a'), (2, 'b')]

tmp = sorted(tmp, reverse=True)
print(tmp) # [(2, 'b'), (1, 'a')]
